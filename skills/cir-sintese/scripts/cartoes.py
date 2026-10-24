#!/usr/bin/env python3
"""Confere os seis cartões e a trava contra índice explicitamente fornecido."""
import argparse
import json
from pathlib import Path
import re
from sintese_core import cli,dump,require
DOSES={'6.1':'padrão','6.2':'completa','6.3':'leve','6.4':'completa','6.5':'completa','6.6':'trava'}

def check(body,entries):
    cards=re.findall(r'^### (6\.[1-6]) ([^\n]+)\n(.*?)(?=^### |\Z)',body,re.M|re.S)
    require(len(cards)==6 and {c[0] for c in cards}==set(DOSES),'Seis cartões únicos obrigatórios')
    if isinstance(entries,dict):entries=entries.get('subetapas')
    require(isinstance(entries,list),'Índice explícito obrigatório');selected=[e for e in entries if e.get('id') in DOSES]
    require(len(selected)==6 and len({e['id'] for e in selected})==6,'Índice sem os seis IDs')
    for k,title,card in cards:
        for field in ('dose','pré-requisitos','grill quer entender','triagem','pesquisa','equipe e alternativas','validação','sai'):
            require(re.search(r'^- '+field+r': .+',card,re.M),'Campo ausente: '+field)
        require(re.search(r'^- dose: '+DOSES[k]+r'$',card,re.M),'Dose divergente')
        entry=next(e for e in selected if e['id']==k);require(entry.get('titulo')==title,'Título divergente')
        require(str(entry.get('dose')).replace('padrao','padrão')==DOSES[k],'Dose no índice divergente')
        if k=='6.6':require('- trava:' in card,'Trava ausente')
    require('### Tema 6' in body and 'sem conselho completo' in body and 'antes da retrospectiva' in body,'Contrato do tema incompleto')
    return {'schema_version':1,'valido':True,'cartoes':6,'limite':'Índice real da condutora ausente; comparar um índice de teste não instala integração.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--indice',required=True);p.add_argument('--cartoes',default=str(Path(__file__).resolve().parents[1]/'references/cartoes.md'));a=p.parse_args();print(dump(check(Path(a.cartoes).read_text(),json.loads(Path(a.indice).read_text()))),end='')
if __name__=='__main__':raise SystemExit(cli(main))
