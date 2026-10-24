#!/usr/bin/env python3
"""Mesa declarativa: tarefas filtradas, eventos sequenciais, retomada e pacote externo."""
from __future__ import annotations
import argparse
import copy
import hashlib
from pathlib import Path
import random
from equipe_core import (array, cli, contributions, digest, dump, ident, index, load,
                         refs, require, text, visible)
import pauta


def sign(state):
    state.pop("hash_estado",None);state["hash_estado"]=digest(state);return state


def verify(state):
    require(isinstance(state,dict) and state.get("schema_version")==1,"Estado versão 1 obrigatório")
    require(state.get("hash_estado")==digest({k:v for k,v in state.items() if k!="hash_estado"}),"Estado foi alterado fora da mesa; confira o registro")
    return state


def start(packet):
    p=pauta.validate(packet.get("pauta"));require(p["modo"]!="fusao","Use fusao.py para preparar a fusão e validar sua revisão")
    members=list(index(packet.get("membros")).values());require(bool(members),"Formação vazia")
    seed=packet.get("semente");require(type(seed) is int,"Semente inteira obrigatória")
    specials=[m for m in members if m.get("papel")=="especialista"]
    leaders=[m for m in members if m.get("papel")=="lider"]
    critics=[m for m in members if m.get("papel")=="critico"]
    require(len(critics)==1 and len(leaders)==(0 if p["modo"]=="individual" else 1),"Líder/crítico não correspondem ao modo")
    require(len(specials)+len(leaders)+len(critics)==len(members),"Papel desconhecido")
    if p["modo"]=="individual":require(len(specials)==1,"Individual tem um especialista")
    elif p["modo"]=="verificacao":require(2<=len(specials)<=3,"Verificação tem dois ou três especialistas")
    elif p["dose"]=="padrao" and p["modo"] in {"elaboracao","avulso"}:require(len(specials)==3,"Padrão tem três especialistas")
    else:require(2<=len(specials)<=5,"Equipe precisa de dois a cinco especialistas")
    private_models=[];sessions=[];siglas=[]
    for m in members:
        ident(m.get("sigla"));ident(m.get("sessao"));ident(m.get("ficha"));ident(m.get("nome"))
        require(m["nome"]==m["nome"].lower(),"Nome precisa ser funcional")
        model=m.get("modelo",{});require(isinstance(model,dict) and model.get("familia")=="anthropic","Perfil v1 exige Claude escolhido para equipes")
        ident(model.get("id"));require(type(model.get("verificado")) is bool,"Verificação de modelo deve ser explícita")
        require(type(model.get("nivel")) is int and model["nivel"]>=0,"Declare nível escolhido do modelo para comparar papéis")
        private_models.append(model);sessions.append(m["sessao"]);siglas.append(m["sigla"])
        if m["papel"]=="especialista":
            text(m.get("especialidade"));text(m.get("selo"));text(m.get("bloco"))
            require(m.get("hash_transporte")==hashlib.sha256(m["bloco"].encode()).hexdigest(),"Bloco diverge do hash de transporte")
            require(m["selo"] in m["bloco"],"Selo não pertence ao bloco montado")
            require(not visible(m["bloco"],p.get("marcadores",[])),"Bloco contém marcador ou identidade reservada")
            if m.get("esp") is None:require(m["selo"].startswith("sem skill · "),"Sem esp exige selo explícito")
    require(len(set(sessions))==len(sessions) and len(set(siglas))==len(siglas),"Sessão ou sigla duplicada")
    leader=leaders[0] if leaders else specials[0];critic=critics[0]
    require(critic["modelo"]["id"]==leader["modelo"]["id"],"Crítico usa o modelo do líder")
    require(all(leader["modelo"]["nivel"]>=m["modelo"]["nivel"] for m in specials),"Líder não pode ser inferior aos especialistas")
    if p["modo"]=="verificacao":
        producers=refs(packet.get("sessoes_produtoras"));require(bool(producers),"Declare sessões que elaboraram")
        require(not set(sessions)&set(producers),"Quem elaborou não verifica")
    distant=[m for m in specials if m.get("distante")]
    if p["modo"]=="elaboracao":
        expected=1 if p["dose"]=="completa" else 0
        require(len(distant)==expected,"Distante incompatível com a dose")
        if expected:
            require(specials.index(distant[0])>=3,"Distante entra a partir do quarto membro")
            text(distant[0].get("funcao_analoga"))
    orders={};rng=random.Random(seed)
    for r in range(1,p["rodadas"]+1):
        order=sorted(m["id"] for m in specials);rng.shuffle(order);orders[str(r)]=order
    sources=list(index(packet.get("fontes",[])).values())
    for source in sources:
        text(source.get("texto"));require(not visible(source["texto"],p.get("marcadores",[])),"Fonte contém marcador ou identidade reservada")
    state={"schema_version":1,"pauta":copy.deepcopy(p),"membros":copy.deepcopy(members),
           "semente":seed,"ordens":orders,"fontes":sources,"eventos":[],"quarentena":[],
           "faltantes":[],"falhas":{},"suspensa":False,"revisao":0,"auditoria":[]}
    return sign(state)


def next_step(state):
    verify(state)
    if state["suspensa"]:return {"tipo":"suspensa","atores":[],"rodada":None}
    events=state["eventos"];p=state["pauta"]
    specials=[m["id"] for m in state["membros"] if m["papel"]=="especialista" and m["id"] not in state["faltantes"]]
    leader=next((m["id"] for m in state["membros"] if m["papel"]=="lider"),specials[0] if specials else None)
    critic=next(m["id"] for m in state["membros"] if m["papel"]=="critico")
    missing=[k for k in specials if not any(e["tipo"]=="preparacao" and e["ator"]==k for e in events)]
    if missing:return {"tipo":"preparacao","atores":missing,"rodada":None}
    if len(specials)<(1 if p["modo"]=="individual" else 2):return {"tipo":"formacao_insuficiente","atores":[],"rodada":None}
    if p["modo"]=="individual":
        for r in range(1,p["rodadas"]+1):
            if not any(e["tipo"]=="critica_individual" and e["rodada"]==r for e in events):return {"tipo":"critica_individual","atores":[critic],"rodada":r}
            if not any(e["tipo"]=="checagem" and e["rodada"]==r for e in events):return {"tipo":"checagem","atores":[],"rodada":r}
            reply=next((e for e in events if e["tipo"]=="replica_individual" and e["rodada"]==r),None)
            if not reply:return {"tipo":"replica_individual","atores":specials,"rodada":r}
            if reply.get("encerrar") is True:break
        return {"tipo":"concluida","atores":[],"rodada":None}
    if not any(e["tipo"]=="abertura" for e in events):return {"tipo":"abertura","atores":[leader],"rodada":None}
    for r in range(1,p["rodadas"]+1):
        for actor in state["ordens"][str(r)]:
            if actor not in specials:continue
            if not any(e["tipo"] in {"fala","sem_fala"} and e["ator"]==actor and e.get("rodada")==r for e in events):return {"tipo":"fala","atores":[actor],"rodada":r}
        for kind,actor in (("critica",critic),("fechamento",leader),("checagem",None)):
            if not any(e["tipo"]==kind and e.get("rodada")==r for e in events):return {"tipo":kind,"atores":[actor] if actor else [],"rodada":r}
        closing=next(e for e in events if e["tipo"]=="fechamento" and e["rodada"]==r)
        if closing.get("parar"):break
    missing=[k for k in specials if not any(e["tipo"]=="posicao" and e["ator"]==k for e in events)]
    if missing:return {"tipo":"posicao","atores":missing,"rodada":None}
    for kind,actor in (("saida",leader),("revisao",critic),("resposta",leader)):
        if not any(e["tipo"]==kind for e in events):return {"tipo":kind,"atores":[actor],"rodada":None}
    return {"tipo":"concluida","atores":[],"rodada":None}


def tasks(state,transport="retomar"):
    phase=next_step(state);require(transport in {"retomar","sem_estado"},"Transporte desconhecido")
    out=[];members=index(state["membros"])
    for actor in phase["atores"]:
        m=members[actor];kind=phase["tipo"]
        # Posições são privadas até todos terminarem; preparação não recebe as outras.
        history=[] if kind=="preparacao" else [e for e in state["eventos"] if e["tipo"]!="posicao" or kind in {"saida","revisao","resposta"}]
        if transport=="retomar" and kind=="fala":
            last=max((i for i,e in enumerate(history) if e["ator"]==actor and e["tipo"]=="fala"),default=-1)
            history=history[last+1:]
        role_file={"especialista":"especialista","lider":"lider","critico":"critico"}[m["papel"]]
        role=(Path(__file__).resolve().parents[1]/"references"/(role_file+".md")).read_text()
        public_members=[{k:x[k] for k in ("id","nome","sigla","papel")}
                        | {"especialidade":x.get("especialidade"),"com_esp":x.get("esp") is not None}
                        for x in state["membros"]]
        initial=kind=="preparacao" or transport=="sem_estado"
        source_ids=m.get("fontes",[]) if m["papel"]=="especialista" else [s["id"] for s in state["fontes"]]
        payload={"tarefa":kind,"ator":actor,"rodada":phase["rodada"],"papel":role,"pauta":pauta.public(state["pauta"]),
                 "membros":public_members,"ata":copy.deepcopy(history),
                 "fontes":[s for s in state["fontes"] if s["id"] in source_ids],
                 "restricoes":"Sem autoria/modelos/dossiê/casos reservados. Honestidade antes de acordo. Não faça perguntas ao usuário."}
        block=m.get("bloco","") if m["papel"]=="especialista" and initial else ""
        out.append({"ator":actor,"sessao":m["sessao"],"mensagem":block+dump(payload)})
    return {"fase":phase,"tarefas":out,"executavel":all(m["modelo"]["verificado"] for m in state["membros"]),
            "limite":"Tarefas não executam sessões nem provam isolamento; o hospedeiro confere modelo, contexto e permissões."}


def record(state,event,revision=None):
    verify(state);require(revision is None or revision==state["revisao"],"Revisão de estado obsoleta")
    require(isinstance(event,dict),"Evento deve ser objeto")
    ident(event.get("id"));require(not any(e["id"]==event["id"] for e in state["eventos"]),"Evento duplicado")
    phase=next_step(state);require(phase["tipo"] not in {"concluida","suspensa","formacao_insuficiente"},"Reunião não aceita nova fala")
    require(event.get("tipo")==phase["tipo"] and event.get("rodada")==phase["rodada"],"Evento fora da fase ou rodada")
    require(event.get("ator") in phase["atores"] if phase["atores"] else event.get("ator")=="mesa","Ator fora da ordem")
    raw=text(event.get("texto"),"Texto original do evento")
    from custos import summarize
    summarize({**state,"eventos":[event]})  # Recusar métricas inválidas antes de serializar/aceitar.
    result=copy.deepcopy(state)
    leaks=visible(dump(event),state["pauta"].get("marcadores",[]))
    if leaks:
        result["quarentena"].append({"evento":copy.deepcopy(event),"alertas":leaks})
        result["suspensa"]=True;result["suspensao_ator"]=event["ator"];result["revisao"]+=1;return sign(result)
    import ata
    kind=event["tipo"]
    require(kind=="preparacao" or "contribuicoes" not in event,"Códigos de contribuição pertencem à preparação; não sobrescreva o registro")
    check={"valida":True}
    if kind=="preparacao":check=ata.preparations(state,event)
    elif kind=="abertura":check=ata.opening(state,event)
    elif kind=="fala":check=ata.speech(state,event)
    elif kind=="posicao":check=ata.positions(state,event)
    elif kind in {"critica","critica_individual","revisao"}:
        points=index(event.get("pontos"));require(bool(array(event.get("conferido"))),"Crítico deve dizer o que conferiu, mesmo sem apontamento")
        for point in points.values():text(point.get("texto"))
        refs(event.get("abertos",[]))
        if kind=="revisao":
            output=next(e["saida"] for e in state["eventos"] if e["tipo"]=="saida")
            require(event.get("hash_saida")==digest(output),"Crítica não revisa a saída atual")
    elif kind=="fechamento":
        opening=next(e for e in state["eventos"] if e["tipo"]=="abertura")
        decisions=index(event.get("decisoes"))
        require(set(decisions)==set(index(opening["divergencias"])),"Fechamento precisa tratar todas as divergências")
        known=set(contributions(state))|{e["id"] for e in state["eventos"]}
        for d in decisions.values():
            require(d.get("situacao") in {"resolvida","aberta","opcoes"},"Situação da divergência inválida")
            text(d.get("motivo"));require(set(refs(d.get("referencias")))<=known,"Fechamento introduz referência nova")
        if event.get("parar") and event["rodada"]<state["pauta"]["rodadas"]:
            r=event["rodada"];require(r>=2,"Não encerrar elaboração na primeira rodada")
            speeches=[e for e in state["eventos"] if e["tipo"]=="fala" and e.get("rodada")==r]
            critic=next(e for e in state["eventos"] if e["tipo"]=="critica" and e["rodada"]==r)
            require(all(e.get("passo") for e in speeches) and not critic.get("abertos"),"Parada antecipada exige todos passarem e crítico sem ponto aberto")
    elif kind=="checagem":
        for c in index(event.get("resultados")).values():require(type(c.get("confere")) is bool,"Resultado de checagem deve ser explícito")
    elif kind in {"saida","resposta","replica_individual"}:
        from sintese import validate as validate_synthesis
        from parecer import validate as validate_report
        output=event.get("saida")
        if state["pauta"]["modo"] in {"verificacao","integracao"}:validate_report(output,state)
        else:validate_synthesis(output,state)
        if kind in {"resposta","replica_individual"}:
            review=next(e for e in reversed(state["eventos"]) if e["tipo"] in {"revisao","critica_individual"})
            answers=index(event.get("respostas"));require(set(answers)==set(index(review["pontos"])),"Líder precisa responder a cada ponto do crítico")
            for a in answers.values():
                require(a.get("acao") in {"aceito","mantido"},"Resposta à crítica inválida");text(a.get("motivo"))
    result["eventos"].append({**copy.deepcopy(event),"checagem":check});result["revisao"]+=1
    return sign(result)


def timeout(state,actor):
    phase=next_step(state);require(actor in phase["atores"],"Timeout não pertence à tarefa atual")
    result=copy.deepcopy(state);key=f"{phase['tipo']}:{phase['rodada']}:{actor}"
    n=result["falhas"].get(key,0)+1;require(n<=2,"Timeout já tratado")
    result["falhas"][key]=n
    if n==2:
        if phase["tipo"]=="preparacao":result["faltantes"].append(actor)
        elif phase["tipo"]=="fala":result["eventos"].append({"id":"sem-fala-"+digest(key)[:12],"tipo":"sem_fala","ator":actor,"rodada":phase["rodada"],"texto":"sem fala após uma repetição"})
        else:result["suspensa"]=True;result["suspensao_ator"]=actor
    result["revisao"]+=1;return sign(result)


def repair(state,actor,new_session,note):
    verify(state);require(state["suspensa"],"Reparo só após suspensão")
    require(state.get("suspensao_ator")==actor,"Substitua a sessão que causou a suspensão")
    ident(new_session);text(note,"Auditoria do reparo")
    require(new_session not in {m["sessao"] for m in state["membros"]},"Sessão nova já pertence à reunião")
    result=copy.deepcopy(state);members=index(result["membros"]);require(actor in members,"Membro inexistente")
    members[actor]["sessao"]=new_session
    quarantined=state["quarentena"][-1]["evento"] if state["quarentena"] else None
    if quarantined and quarantined.get("rodada"):
        r=quarantined["rodada"];removed=[e for e in result["eventos"] if e.get("rodada")==r]
        result["eventos"]=[e for e in result["eventos"] if e not in removed]
        result["quarentena"].append({"rodada_excluida":removed,"motivo":"repetir rodada contaminada"})
    result["auditoria"].append({"ator":actor,"nova_sessao":new_session,"nota":note})
    result["suspensa"]=False;result["revisao"]+=1;return sign(result)


def export(state):
    require(next_step(state)["tipo"]=="concluida","Reunião ainda não concluída")
    from custos import summarize
    from ata import scoreboard
    root="equipe/"+state["pauta"]["id"]+"/"
    result={root+"pauta.md":dump(pauta.public(state["pauta"])),root+"mesa.json":dump(state),
            root+"ata.md":"\n\n".join(e["texto"] for e in state["eventos"]),
            root+"checagem.json":dump([{e["id"]:e.get("checagem")} for e in state["eventos"]]),
            root+"custos.json":dump(summarize(state)),root+"placar.json":dump(scoreboard(state))}
    for e in state["eventos"]:
        if e["tipo"] in {"preparacao","posicao"}:
            folder="preparacoes" if e["tipo"]=="preparacao" else "posicoes"
            result[root+folder+"/"+ident(e["ator"])+".md"]=e["texto"]
    output=next(e["saida"] for e in reversed(state["eventos"]) if e.get("saida"))
    filename={"verificacao":"parecer","integracao":"integracao"}.get(state["pauta"]["modo"],"sintese")
    result[root+filename+".md"]=dump(output)
    return {"arquivos":result,"responsavel_persistencia":"condutora","aprovacao_usuario":False,
            "limite":"Protocolo concluído não é aprovação da hipótese, ganho de equipe ou validação científica."}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("acao",choices=["iniciar","tarefas","registrar","timeout","reparar","entregar"]);p.add_argument("entrada")
    p.add_argument("--evento");p.add_argument("--ator");p.add_argument("--sessao");p.add_argument("--nota");p.add_argument("--revisao",type=int);p.add_argument("--transporte",default="retomar")
    a=p.parse_args();value=load(a.entrada)
    if a.acao=="iniciar":result=start(value)
    elif a.acao=="tarefas":result=tasks(value,a.transporte)
    elif a.acao=="registrar":require(a.evento,"Selecione evento");result=record(value,load(a.evento),a.revisao)
    elif a.acao=="timeout":result=timeout(value,a.ator)
    elif a.acao=="reparar":result=repair(value,a.ator,a.sessao,a.nota)
    else:result=export(value)
    print(dump(result),end="");return 0


if __name__=="__main__":cli(main)
