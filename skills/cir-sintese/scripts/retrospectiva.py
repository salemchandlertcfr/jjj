#!/usr/bin/env python3
"""Compara registros anteriores e desfechos sem transformar resultado em qualidade da decisão."""
from __future__ import annotations
import argparse
from datetime import date
import math
from statistics import median
from sintese_core import array,cli,digest,dump,git,hash_bytes,index,load,read_ref,require,text,COMMIT,SHA

NOTES={'termo_sem_definicao','ideia_sem_tipo','custo_uso_tardio','leitura_ambigua','registro_sem_bloco','fonte_divergente','comparacao_sem_previsao'}


def brier(rows):
    known=[]
    for row in array(rows):
        p=row.get('probabilidade');outcome=row.get('desfecho')
        if p is None or outcome is None:continue
        require(type(p) in {int,float} and math.isfinite(p) and 0<=p<=1 and type(outcome) is bool,'Previsão ou desfecho factual inválido')
        text(row.get('referencia_desfecho'));known.append((p-int(outcome))**2)
    return {'n':len(known),'brier':sum(known)/len(known) if known else None}


def run(v,root):
    approval=v.get('aprovacao',{});require(approval.get('resposta')=='sim' and approval.get('hash')==digest({k:x for k,x in approval.items() if k!='hash'}),'Retrospectiva vem após aprovação registrada')
    for name,h in approval.get('artefatos',{}).items():require(hash_bytes(git(root,'show',approval['commit']+':'+name))==h,'Aprovação de artefato diferente')
    review=v.get('sua_avaliacao',{});text(review.get('funcionou'));text(review.get('nao_funcionou'));require(review.get('hash')==digest({k:x for k,x in review.items() if k!='hash'}),'Avaliação anterior precisa estar selada')
    comparisons=[]
    for row in index(v.get('comparacoes',[])).values():
        expectation=row.get('expectativa',{});text(expectation.get('texto'))
        if expectation.get('tipo')=='registrada':
            ref=expectation.get('origem',{});raw=read_ref(root,ref).decode();require(expectation['texto'] in raw,'Expectativa não está no registro')
            end=text(row.get('commit_desfecho'));require(COMMIT.fullmatch(end) and end!=ref['commit'],'Desfecho deve ser posterior')
            git(root,'merge-base','--is-ancestor',ref['commit'],end)
        else:
            require(expectation.get('tipo')=='reconstrucao' and expectation.get('cega_declarada') is True,'Expectativa sem registro ou reconstrução marcada');text(expectation.get('sessao'))
        require(row.get('qualidade_decisao') in {'boa','ruim','indeterminada'},'Qualidade da decisão deve ser independente do desfecho')
        text(row.get('base_na_epoca'));text(row.get('desfecho'));comparisons.append(row)
    changes=list(index(v.get('melhorias',[])).values())
    for c in changes:
        for f in ('dono','skill','secao','acao','origem'):text(c.get(f))
        require(len(c['acao'].split())>=5 and c['acao'].strip().lower() not in {'melhorar a comunicação entre as equipes'},'Melhoria genérica')
    tangents=v.get('tangentes',{});classified=tangents.get('classificadas');used=tangents.get('com_funcao')
    require(type(classified) is int and type(used) is int and 0<=used<=classified,'Contagem de tangentes inválida')
    result={'schema_version':1,'comparacoes':comparisons,'melhorias':changes,'calibracao_conselho':brier(v.get('previsoes_conselho',[])),'calibracao_usuario':brier(v.get('previsoes_usuario',[])),'taxa_surpresa_final':used/classified if classified else None,'regra_surpresa':'S16 §6.10: tangentes com função no CIR / tangentes classificadas; cir-arquitetura/surpresa.py não está instalado para comparação.','aprendizado':None,'espelho':'não publicado; oferta pela condutora só em projeto real aprovado'}
    require(type(v.get('projeto_real')) is bool,'Declare projeto real/teste')
    if v['projeto_real']:
        method=v.get('metodo',{});allowed={'fracao_tangentes_4_4','taxa_4_10','doses','passagem','voltas'};require(set(method)<=allowed,'Campo de conteúdo fora da lista de método')
        def numeric(x,depth=0):
            require(depth<=3,'Métrica muito profunda')
            if isinstance(x,dict):
                allowed_keys={'iguais','subiram','desceram','rodadas','previstas','apareceram','centrais_nao_previstas','falsos_alarmes','proposito','mapa','idealidade','arquitetura','prova','sintese'}
                require(set(x)<=allowed_keys,'Chave de conteúdo em métricas')
                for y in x.values():numeric(y,depth+1)
            else:require(x is None or type(x) in {int,float} and math.isfinite(x) and x>=0,'Métrica de método deve ser numérica')
        for x in method.values():numeric(x)
        for field in ('fracao_tangentes_4_4','taxa_4_10'):
            if method.get(field) is not None:require(0<=method[field]<=1,'Fração fora de 0–1')
        notes=array(v.get('notas_metodo',[]));require(set(notes)<=NOTES,'Notas são códigos de método, sem texto do projeto')
        project=text(v.get('hash_projeto'));require(SHA.fullmatch(project),'Use hash opaco do projeto');date.fromisoformat(text(v.get('data')))
        result['aprendizado']={'schema_version':1,'projeto':'h:'+project,'data':v['data'],**method,'tangentes':classified,'taxa_final':result['taxa_surpresa_final'],'notas':notes}
    return result


def medians(v):
    rows=array(v.get('projetos'));ids=[r.get('projeto') for r in rows];require(len(set(ids))==len(ids),'Projeto duplicado')
    fields=('fracao_tangentes_4_4','taxa_4_10','taxa_final','tangentes');out={}
    for f in fields:
        values=[r[f] for r in rows if r.get(f) is not None]
        require(all(type(x) in {int,float} and math.isfinite(x) and x>=0 for x in values),'Métrica inválida')
        out[f]={'n':len(values),'mediana':median(values) if len(values)>=3 else None,'valores':values if len(values)<3 else None}
    return {'schema_version':1,'metricas':out,'orientacao':'Mostre n; com menos de três projetos, mostre valores e pergunte. Não altere a dose automaticamente.'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('entrada');p.add_argument('--git');p.add_argument('--mediana',action='store_true');a=p.parse_args();v=load(a.entrada)
    if a.mediana:out=medians(v)
    else:require(a.git,'Informe --git');out=run(v,a.git)
    print(dump(out),end='')
if __name__=='__main__':raise SystemExit(cli(main))
