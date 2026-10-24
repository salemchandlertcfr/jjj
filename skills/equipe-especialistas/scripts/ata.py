#!/usr/bin/env python3
"""Confere artefatos da ata e refaz contas; pesquisa requer adaptador real externo."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import subprocess
import sys
from equipe_core import (array, cli, contributions, digest, dump, evidence_registry, ident,
                         index, load, no_verdict, refs, require, text, visible)


def preparations(state, event):
    member=next(m for m in state["membros"] if m["id"]==event["ator"])
    require(event["texto"].splitlines()[0]==member["selo"],"Preparação sem selo esperado")
    for field in ("leitura","posicao_inicial","critica_base"):
        text(event.get(field),field)
    cs=index(event.get("contribuicoes"));require(bool(cs),"Preparação sem contribuições")
    for c in cs.values():
        require(c["id"].startswith(member["sigla"]+"-"),"Código de contribuição fora da sigla")
        require(c["id"] not in contributions(state),"Código já utilizado")
        require(text(c.get("texto")) in event["texto"],"Contribuição não aparece no texto original")
        text(c.get("por_que"));text(c.get("muda"))
        require(bool(array(c.get("evidencias"))),"Contribuição sem tipo de lastro explícito")
        for e in c["evidencias"]:
            require(e.get("tipo") in {"fonte","esp","conta","geral"},"Tipo de lastro inválido")
            if e["tipo"]=="geral":require(e.get("marca")=="conhecimento geral, sem fonte","Conhecimento geral exige marca explícita")
            else:ident(e.get("id"))
            if e["tipo"]=="esp":require(member.get("esp") is not None,"Sem skill não pode atribuir lastro a esp")
    refs(event.get("fontes_novas",[]));array(event.get("perguntas",[]));array(event.get("nao_sei",[]))
    return {"valida":True,"codigos":list(cs)}


def opening(state, event):
    expected=set(contributions(state))
    mapped=refs(event.get("mapa"))
    require(set(mapped)==expected,"Abertura não mapeia todas as contribuições")
    no_verdict(event["texto"])
    from equipe_core import fold
    import re
    require(not re.search(r"prefiro|minha proposta|a melhor (?:e|opcao)|minha opiniao",fold(event["texto"])),"Líder abre com mapa, sem preferência")
    for d in index(event.get("divergencias")).values():
        text(d.get("texto"));require(set(refs(d.get("contribuicoes")))<=expected,"Divergência sem origem")
        require(bool(d["contribuicoes"]),"Divergência vazia")
    require(set(refs(event.get("unicas",[])))<=expected,"Contribuição única desconhecida")
    return {"valida":True}


def speech(state,event):
    member=next(m for m in state["membros"] if m["id"]==event["ator"])
    require(event["texto"].splitlines()[0]==member["selo"],"Fala sem selo esperado")
    require(type(event.get("passo")) is bool,"Declare passo")
    round_no=event["rodada"]
    if event["passo"]:
        require(round_no>=2,"Rodada inicial exige fato novo e motivo contra")
        return {"valida":True}
    require(text(event.get("motivo")) in event["texto"] and text(event.get("posicao")) in event["texto"],"Motivo/posição não aparecem na fala original")
    refs(event.get("referencias",[]))
    if round_no==1:
        require(1<=len(array(event.get("fatos_novos")))<=2,"Rodada 1 exige um ou dois fatos novos")
        text(event.get("contra_proposta"),"Motivo contra a proposta à frente")
    else:require(bool(array(event.get("fatos_novos"))),"Sem novidade declarada, passe a palavra")
    for fact in event["fatos_novos"]:
        require(text(fact) in event["texto"],"Fato novo não aparece na fala original")
    if event.get("mudou"):
        changed_position(state,event)
    for challenge in array(event.get("contraria",[])):
        key=challenge.get("contribuicao");cs=contributions(state)
        require(key in cs,"Contraria contribuição inexistente")
        author=next(m for m in state["membros"] if m["id"]==cs[key]["ator"])
        authority=author.get("esp") is not None or any(e.get("tipo")=="fonte" and evidence_registry(state).get(e.get("id")) for e in cs[key]["evidencias"])
        if authority:
            counter=challenge.get("contraprova",{})
            require(counter.get("tipo") in {"fonte","conta","contraexemplo"},"Contrariar autoridade exige contraprova")
            if counter["tipo"]=="contraexemplo":text(counter.get("texto"))
            else:
                from equipe_core import supported
                supported([counter.get("id")],state)
    return {"valida":True}


def changed_position(state,event):
    require(bool(event.get("porque")),"Mudança de posição sem motivo")
    cited=event.get("cita_fala")
    require(any(e["id"]==cited and e["tipo"]=="fala" and e["ator"]!=event["ator"] for e in state["eventos"]),"Mudança precisa citar fala anterior de outro membro")


def positions(state,event):
    member=next(m for m in state["membros"] if m["id"]==event["ator"])
    require(event["texto"].splitlines()[0]==member["selo"],"Posição sem selo")
    require(text(event.get("apoio")) in event["texto"],"Posição final diverge do texto original")
    text(event.get("evidencia_mais_forte"));text(event.get("incerteza"));text(event.get("mudaria_se"))
    previous=next(e for e in state["eventos"] if e["tipo"]=="preparacao" and e["ator"]==event["ator"])
    changed=event["apoio"]!=previous["posicao_inicial"]
    warning=changed and not (event.get("porque") and any(e["id"]==event.get("cita_fala") and e["tipo"]=="fala" and e["ator"]!=event["ator"] for e in state["eventos"]))
    for dissent in index(event.get("dissenso")).values():
        text(dissent.get("argumento"));text(dissent.get("mudaria_se"))
    return {"valida":True,"mudanca_sem_motivo":warning}


def calculations(values):
    results=[]
    for calculation in index(values).values():
        code=text(calculation.get("codigo"));expected=calculation.get("resultado")
        # Código é interpretado por AST restrita em outro Python, nunca exec/eval.
        proc=subprocess.run([sys.executable,"-I","-S",str(Path(__file__).with_name("contas_worker.py"))],
                            input=json.dumps({"codigo":code}),text=True,capture_output=True,timeout=3)
        if proc.returncode!=0:
            results.append({"id":calculation["id"],"confere":False,"erro":"código fora do subconjunto ou conta inválida","hash_codigo":digest(code)})
            continue
        result=json.loads(proc.stdout)["resultado"]
        import math
        match=type(expected) in {int,float} and math.isfinite(expected) and math.isclose(result,expected,rel_tol=1e-9,abs_tol=1e-12)
        results.append({"id":calculation["id"],"confere":match,"resultado":result,"hash_codigo":digest(code)})
    return {"resultados":results,"limite":"Reprodução aritmética não valida o modelo científico."}


def sources(values,adapter=None):
    entries=index(values)
    if not adapter:
        return {"executadas":False,"resultados":[{"id":k,"confere":False,"situacao":"nao_conferida"} for k in entries],
                "bloqueio":"pesquisa-cientifica ausente; forneça adaptador verificado para verificar.py e trecho.py"}
    require(adapter.get("autorizado") is True,"Adaptador precisa ser explicitamente autorizado")
    results=[]
    for source in entries.values():
        text(source.get("texto"));checks=[]
        for tool in ("verificar","trecho"):
            command=array(adapter.get(tool));require(bool(command) and all(isinstance(a,str) and a for a in command),"Comando de adaptador inválido")
            proc=subprocess.run(command,input=json.dumps(source),text=True,capture_output=True,timeout=30)
            require(proc.returncode==0 and len(proc.stdout)<1_000_000,"Adaptador falhou; fonte continua não conferida")
            try:value=json.loads(proc.stdout)
            except ValueError as exc:
                from equipe_core import TeamError
                raise TeamError("Adaptador não devolveu JSON") from exc
            require(isinstance(value,dict) and value.get("id")==source["id"] and type(value.get("confere")) is bool,"Resposta de adaptador inválida")
            checks.append(value["confere"])
        results.append({"id":source["id"],"confere":all(checks),"situacao":"conferida" if all(checks) else "nao_confere"})
    return {"executadas":True,"resultados":results,"limite":"Autenticidade e suporte semântico dependem da pesquisa e do adaptador; este pacote não substitui seus scripts."}


def scoreboard(state):
    rows=[];cs=contributions(state)
    output=next((e["saida"] for e in reversed(state["eventos"]) if e.get("saida")),{})
    destinations={d["id"]:d for d in output.get("destinos",[])}
    for key,c in cs.items():
        member=next(m for m in state["membros"] if m["id"]==c["ator"])
        rows.append({"contribuicao":key,"especialidade":member["especialidade"],"selo":member["selo"],
                     "destino":destinations.get(key,{}).get("destino","pendente")})
    return rows


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("acao",choices=["preparacoes","abertura","posicoes","fontes","contas","placar"])
    p.add_argument("entrada");p.add_argument("--estado");p.add_argument("--adaptador")
    a=p.parse_args();value=load(a.entrada)
    if a.acao=="contas":result=calculations(value)
    elif a.acao=="fontes":result=sources(value,load(a.adaptador) if a.adaptador else None)
    elif a.acao=="placar":result=scoreboard(value)
    else:
        require(a.estado,"Selecione estado")
        result={"preparacoes":preparations,"abertura":opening,"posicoes":positions}[a.acao](load(a.estado),value)
    print(dump(result),end="");return int(isinstance(result,dict) and any(not r.get("confere") for r in result.get("resultados",[])))


if __name__=="__main__":cli(main)
