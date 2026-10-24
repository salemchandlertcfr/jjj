#!/usr/bin/env python3
"""Estado declarativo do teste: reformulação antes das perguntas e dois juízes separados."""
from __future__ import annotations
import argparse
import copy
from sintese_core import array,cli,digest,dump,ident,index,load,refs,require,text

FIELDS=('proposito','nucleo_principios','o_que_nao_e','primeira_tarefa','bancada')

def seal(s):
    s.pop('hash_estado',None);s['hash_estado']=digest(s);return s

def verify(s):require(s.get('hash_estado')==digest({k:v for k,v in s.items() if k!='hash_estado'}),'Estado de passagem alterado');return s

def start(packet):
    predictions=list(index(packet.get('previstas')).values());require(bool(predictions),'Previstas precisam ser registradas antes dos leitores')
    for p in predictions:text(p.get('texto'))
    return seal({'schema_version':1,'previstas':predictions,'hash_previstas':digest(predictions),'rodadas':[],'limite':'Sequência e sessões declaradas não comprovam anterioridade real ou isolamento.'})

def open_round(s,packet):
    verify(s);s=copy.deepcopy(s);rounds=s['rodadas']
    if rounds:require(rounds[-1].get('resultado') is not None,'Conclua/invalide rodada anterior')
    if len(rounds)>=3:
        a=packet.get('autorizacao',{});require(a.get('resposta')=='sim' and a.get('rodada')==len(rounds)+1 and text(a.get('registro')),'Rodada extra exige sim registrado para esta rodada')
    readers=list(index(packet.get('leitores')).values());judges=list(index(packet.get('juizes')).values())
    require(len(readers)==3 and len(judges)==2,'São três leitores e dois juízes')
    require({r.get('especialidade') for r in readers}=={'sistemas','dominio','generalista'},'Óticas dos leitores incompletas')
    old={r['sessao'] for rd in rounds for role in ('leitores','juizes') for r in rd[role]};new=[]
    for a in readers+judges:
        ident(a.get('sessao'));new.append(a['sessao']);require(a['sessao'] not in old,'Sessão reutilizada')
        require(a.get('modelo')==text(packet.get('modelo_juiz')),'Use o modelo de juiz escolhido')
    require(len(set(new))==5,'Sessões precisam ser distintas')
    cir=text(packet.get('cir'));package=text(packet.get('pacote'));key=packet.get('gabarito',{})
    require(set(key)==set(FIELDS),'Gabarito exige os cinco campos')
    for excerpt in key.values():require(text(excerpt) in cir+'\n'+package,'Gabarito não extraído dos documentos')
    rounds.append({'n':len(rounds)+1,'cir':cir,'pacote':package,'hash_documentos':digest([cir,package]),'leitores':readers,'juizes':judges,'gabarito':key,'reformulacoes':{},'perguntas':{},'julgamentos':{},'resultado':None,'autorizacao':packet.get('autorizacao')})
    return seal(s)

def phase(rd):
    for kind,roles in [('reformulacoes','leitores'),('perguntas','leitores'),('julgamentos','juizes')]:
        missing=[a['id'] for a in rd[roles] if a['id'] not in rd[kind]]
        if missing:return kind,missing
    return 'classificacao',['condutora']

def brief(s,actor):
    verify(s);rd=s['rodadas'][-1];require(rd['resultado'] is None,'Rodada concluída');kind,actors=phase(rd);require(actor in actors,'Ator fora da fase')
    if kind=='reformulacoes':return {'schema_version':1,'cir':rd['cir'],'pacote':rd['pacote'],'hash_documentos':rd['hash_documentos'],'tarefa':'Reformule os cinco campos com suas palavras. Depois receberá a tarefa de perguntas; não preencha lacunas.'}
    if kind=='perguntas':return {'schema_version':1,'cir':rd['cir'],'pacote':rd['pacote'],'sua_reformulacao':rd['reformulacoes'][actor],'tarefa':'Pergunte depois de reformular; registre deduzi/chutei e a frase de apoio; marque se muda a primeira decisão.'}
    if kind=='julgamentos':return {'schema_version':1,'gabarito':rd['gabarito'],'reformulacoes':{'R'+str(i+1):rd['reformulacoes'][r['id']] for i,r in enumerate(rd['leitores'])},'tarefa':'Por campo: bate/diverge/incompleta e trecho do gabarito. Não receberá perguntas, nomes ou previstas.'}
    return {'schema_version':1,'perguntas':rd['perguntas'],'tarefa':'Classifique cada pergunta com o crítico, responsável e destino; mudança de rumo exige volta.'}


def record(s,event):
    verify(s);s=copy.deepcopy(s);rd=s['rodadas'][-1];require(rd['resultado'] is None,'Rodada concluída');kind,actors=phase(rd)
    require(event.get('tipo')==kind and event.get('ator') in actors,'Evento fora da fase');actor=event['ator'];value=event.get('conteudo')
    if kind=='reformulacoes':
        require(isinstance(value,dict) and set(value)==set(FIELDS),'Reformulação exige cinco campos')
        for v in value.values():text(v)
    elif kind=='perguntas':
        for q in index(value).values():
            text(q.get('texto'));require(type(q.get('muda_primeira_decisao')) is bool,'Declare relevância')
            require(q.get('modo') in {'deduzi','chutei','pergunta'},'Declare inferência/chute')
            if q['modo']!='pergunta':require(text(q.get('apoio')) in rd['cir']+'\n'+rd['pacote'],'Frase de apoio não está nos documentos')
        used={q['id'] for qs in rd['perguntas'].values() for q in qs};require(not used&set(index(value)),'Pergunta duplicada')
    elif kind=='julgamentos':
        require(isinstance(value,dict) and set(value)=={'R1','R2','R3'},'Julgue três reformulações anônimas')
        for fields in value.values():
            require(set(fields)==set(FIELDS),'Julgue todos os campos')
            for field,v in fields.items():
                require(v.get('veredito') in {'bate','diverge','incompleta'},'Veredito inválido');require(text(v.get('trecho')) in rd['gabarito'][field],'Juiz sem trecho do gabarito')
    else:
        actual={q['id']:q for qs in rd['perguntas'].values() for q in qs};classified=index(value);require(set(actual)==set(classified),'Classificação incompleta')
        central=[];predicted=set();unpredicted=[]
        for k,c in classified.items():
            require(c.get('classe') in {'central','secundaria'},'Classe inválida');require(c.get('quem') in {'dossie','usuario','ninguem_sabe'},'Responsável inválido');text(c.get('destino'))
            if actual[k]['muda_primeira_decisao']:require(c['classe']=='central','Primeira decisão alterada é central')
            if c.get('muda') in {'proposito','nucleo','principio','restricao','escolha'}:text(c.get('registro_volta'),'Mudança de rumo exige volta')
            if c.get('prevista'):
                require(c['prevista'] in index(s['previstas']),'Prevista inexistente');predicted.add(c['prevista'])
            elif c['classe']=='central':unpredicted.append(k)
            if c['classe']=='central':central.append(k)
        disagreements=[]
        judges=list(rd['julgamentos'].values())
        for label in ('R1','R2','R3'):
            for field in FIELDS:
                if any(j[label][field]['veredito']!='bate' for j in judges):disagreements.append(label+':'+field)
        comparison=event.get('comparacao_leituras',{});require(comparison.get('conferida') is True,'Compare reformulações entre si com o crítico');ambiguity=array(comparison.get('divergencias'))
        rd['comparacao_leituras']=comparison
        rd['classificacao']=value;rd['resultado']={'valida':True,'fechou':not central and not disagreements and not ambiguity,'centrais':central,'ambiguidades':ambiguity,'reformulacoes_pendentes':disagreements,'previstas_apareceram':len(predicted),'centrais_nao_previstas':len(unpredicted),'limite':'Dois julgamentos declarados, não medição automática de equivalência semântica.'}
        return seal(s)
    rd[kind][actor]=copy.deepcopy(value);return seal(s)


def invalidate(s,reason):
    verify(s);s=copy.deepcopy(s);s['rodadas'][-1]['resultado']={'valida':False,'fechou':False,'motivo':text(reason)};return seal(s)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('acao',choices=['previstas','abrir','brief','registrar','invalidar']);p.add_argument('entrada');p.add_argument('--evento');p.add_argument('--ator');p.add_argument('--motivo');a=p.parse_args();v=load(a.entrada)
    if a.acao=='previstas':out=start(v)
    elif a.acao=='abrir':out=open_round(v,load(a.evento))
    elif a.acao=='brief':out=brief(v,a.ator)
    elif a.acao=='invalidar':out=invalidate(v,a.motivo)
    else:out=record(v,load(a.evento))
    print(dump(out),end='')
if __name__=='__main__':raise SystemExit(cli(main))
