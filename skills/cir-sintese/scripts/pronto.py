#!/usr/bin/env python3
"""Critério por evidência versionada: marca ausente como não verificado, nunca como passa."""
from __future__ import annotations
import argparse
from datetime import date
from pathlib import Path
from sintese_core import cli,digest,dump,evidence,file_at,git,hash_bytes,index,load,require,signals,text,COMMIT

import json
_RULE_FILE=Path(__file__).resolve().parents[1]/'assets/pronto.yaml'
RULES={r['id']:r['verificacoes'] for r in json.loads(_RULE_FILE.read_text())['itens']}



def assess(v,root):
    supplied=index(v.get('itens',[]));require(set(supplied)<=set(RULES),'Item pronto inexistente')
    artifacts=v.get('artefatos',{});require(isinstance(artifacts,dict),'Artefatos da montagem obrigatórios')
    require(v.get('escolha') in {'referencia','refutada','abstencao'},'Declare a escolha')
    required={'06-cir.md','06-estacionamento-etapa-3.md'}
    if v['escolha']!='abstencao':required|={'06-pacote-etapa-2.md','pacote.json'}
    require(required<=set(artifacts),'Artefatos finais incompletos')
    for name,h in artifacts.items():require(hash_bytes(file_at(root,name).read_bytes())==h,'Artefato mudou desde a evidência')
    bound=digest(artifacts);out=[]
    for key,fields in RULES.items():
        state='nao_verificado';reason='Sem evidência versionada'
        if key in supplied:
            entry=supplied[key];ref=entry.get('evidencia',{});ref={**ref,'criterio':key}
            try:
                ev=evidence(root,ref,entry.get('evidencia_id'))
                require(ev.get('hash_artefatos')==bound,'Evidência de outra montagem')
                checks=ev.get('verificacoes',{});require(all(checks.get(f) is True for f in fields),'Verificação faltante/falhou')
                if key in {'I4','I10','I11'}:
                    count=ev.get('quantidade');minimum=10 if key=='I11' else 3
                    require(type(count) is int and count>=minimum,'Quantidade insuficiente')
                require(ev.get('resultado')=='passa','Evidência não passou');text(ev.get('trecho'));text(ev.get('responsavel'))
                state='passa';reason='Arquivo, seção, ID, hash e requisitos declarados conferem; mérito exige crítico.'
            except (ValueError,OSError,KeyError,TypeError) as exc:state='falha';reason=str(exc)
        out.append({'id':key,'estado':state,'motivo':reason})
    scan=[]
    for name in artifacts:
        for s in signals(file_at(root,name).read_text()):scan.append({'arquivo':name,**s})
    fresh=v.get('conferencia_fontes',{})
    sources_ok=fresh.get('hash_artefatos')==bound and fresh.get('executada') is True and fresh.get('todas_citadas') is True and fresh.get('pendentes')==[]
    pend=v.get('pendencias')
    pend_ok=isinstance(pend,list) and all(p.get('destino') in {'volta','ressalva'} and p.get('registro') and p.get('motivo') and p.get('objetivo') for p in pend)
    report={'schema_version':1,'itens':out,'artefatos':artifacts,'hash_artefatos':bound,'vigia_local':scan,'fontes_conferidas_declaradas':sources_ok,'pendencias_com_destino':pend_ok,'integracao_condutora':'pendente: pendencias.py e vigia.py externos não executados por este comando','pronto_sem_ressalvas':all(r['estado']=='passa' for r in out) and not scan and sources_ok and pend_ok,'limite':'Não substitui pesquisa, crítico, fontes reais ou vigia da condutora. Um JSON declarando evidência não autentica sua execução.'}
    report['hash']=digest(report);return report


def approve(report,packet,root):
    require(report.get('hash')==digest({k:v for k,v in report.items() if k!='hash'}),'Relatório de pronto alterado')
    require(packet.get('resposta')=='sim','Só sim explícito aprova');commit=text(packet.get('commit'));require(COMMIT.fullmatch(commit),'Commit completo obrigatório')
    date.fromisoformat(text(packet.get('data')));text(packet.get('registro'))
    current=report['artefatos']
    for name,h in current.items():
        require(hash_bytes(file_at(root,name).read_bytes())==h and hash_bytes(git(root,'show',commit+':'+name))==h,'Aprovação aponta para outra versão')
    failed={r['id'] for r in report['itens'] if r['estado']!='passa'}
    exceptions=index(packet.get('ressalvas',[]));require(failed<=set(exceptions),'Item pendente sem ressalva sua')
    issues=[]
    if report['vigia_local']:issues.append('vigia')
    if not report['fontes_conferidas_declaradas']:issues.append('fontes')
    if not report['pendencias_com_destino']:issues.append('pendencias')
    if issues:require(set(issues)<=set(exceptions),'Validação integrada pendente sem ressalva')
    for e in exceptions.values():
        for f in ('registro','motivo','objetivo'):text(e.get(f))
    require(set(r['id'] for r in report['itens'])==set(RULES),'Relatório não cobre 14 itens')
    value={'schema_version':1,'resposta':'sim','commit':commit,'registro':packet['registro'],'data':packet['data'],'artefatos':current,'ressalvas':list(exceptions.values()),'teste_passagem_pulado':'I14' in exceptions,'integracao_condutora':'registro externo: condutora persiste e autentica consentimento'}
    value['hash']=digest(value);return value


def audit(body):
    return {'schema_version':1,'auditoria':True,'reescreveu':False,'itens':[{'id':k,'estado':'nao_verificado','pergunta':'Onde está a evidência de '+', '.join(fields)+'?'} for k,fields in RULES.items()],'sinais':signals(body),'limite':'Documento sem dossiê não demonstra os 14 itens; apontar locais e lacunas por revisão.'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('entrada');p.add_argument('--git');p.add_argument('--auditoria',action='store_true');p.add_argument('--aprovar');a=p.parse_args()
    if a.auditoria:out=audit(Path(a.entrada).read_text())
    else:
        require(a.git,'Informe --git');v=load(a.entrada);out=approve(v,load(a.aprovar),a.git) if a.aprovar else assess(v,a.git)
    print(dump(out),end='')
if __name__=='__main__':raise SystemExit(cli(main))
