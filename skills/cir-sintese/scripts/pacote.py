#!/usr/bin/env python3
"""Gera passagem das mesmas origens Git, nunca de uma paráfrase do CIR."""
from __future__ import annotations
import argparse
from datetime import date
from sintese_core import array,cli,context,digest,dump,hash_bytes,index,load,read_ref,refs,require,text

PARTS=['O que fazer primeiro','Capacidades e métricas','A bancada','As fronteiras','Perguntas científicas abertas','Princípios e restrições','Alternativas vivas','Não reintroduzir sem prova','O que reverteria a escolha']

def etapa2(m,root):
    blocks,catalog=context(m,root)
    if m['escolha']=='abstencao':return {'schema_version':1,'pacote':None,'nota':'Encerramento por abstenção; a origem deve registrar o que reabriria.'}
    active={k:v['item'] for k,v in blocks.items() if not v['bloco'].get('superado_por') and not v['item'].get('dados',{}).get('familia_perdeu')}
    grouped=lambda t:[v for v in active.values() if v['tipo'] in t]
    parts={str(i):{'titulo':s,'itens':[]} for i,s in enumerate(PARTS,1)}
    def add(n,item,data):parts[str(n)]['itens'].append({'origem':item['id'],'texto':item['texto'],**data})
    for item in grouped({'killer','pergunta','fronteira'}):
        for action in array(item.get('dados',{}).get('acoes',[])):
            add(1,item,{'acao':text(action)})
    require(3<=len(parts['1']['itens'])<=5,'Parte 1 exige três a cinco ações registradas na origem')
    for c in grouped({'capacidade'}):
        mids=refs(c.get('dados',{}).get('metricas'),active);require(bool(mids),'Capacidade sem métricas')
        metrics=[]
        for k in mids:
            metric=active[k];require(metric['tipo']=='metrica','Vínculo não é métrica');d=metric.get('dados',{})
            for field in ('linha_base','fonte','limite'):text(d.get(field),'Métrica: '+field)
            metrics.append({'id':k,'texto':metric['texto'],'dados':d})
        add(2,c,{'metricas':metrics})
    for c in grouped({'caso'}):
        r=c.get('dados',{}).get('saida',{});read_ref(root,r)
        add(3,c,{'saida':r,'nota':'A Etapa 2 precisa também de casos novos que ninguém do projeto viu.'})
    for f in grouped({'fronteira'}):
        require(f['texto'].rstrip().endswith('?'),'Fronteira deve ser pergunta, sem meio escolhido')
        add(4,f,{'respeita':text(f.get('dados',{}).get('respeita'))})
    for q in grouped({'pergunta'}):
        d=q.get('dados',{});date.fromisoformat(text(d.get('data_busca')));add(5,q,{'data_busca':d['data_busca'],'quem_responde':text(d.get('quem_responde'))})
    substitutes=index(m.get('em_vez_disso',[]));required={c['id'] for c in grouped({'principio','restricao'})}
    require(set(substitutes)==required,'Em vez disso deve cobrir todos os princípios/restrições')
    for p in grouped({'principio','restricao'}):
        d=p.get('dados',{});s=substitutes[p['id']];body=text(s.get('texto'));v=s.get('verificacao',{})
        require(v.get('hash')==digest({'texto':body,'origem':p}),'Verificação de em vez disso obsoleta')
        require(text(v.get('sessao'))!=text(s.get('sessao_redator')),'Redator não verifica em vez disso')
        require(v.get('veredito')=='sustentada','Em vez disso ainda não sustentado')
        require(text(v.get('trecho')) in dump(p),'Verificação sem trecho de origem')
        add(6,p,{'refuta_se':text(d.get('refuta_se')),'onde_mora':text(d.get('onde_mora')),'em_vez_disso':body})
    for a in grouped({'alternativa_viva'}):add(7,a,{'prova':text(a.get('dados',{}).get('prova'))})
    for a in grouped({'refutada','descartada'}):
        d=a.get('dados',{});add(8,a,{'refutou':text(d.get('refutou')),'desafio':text(d.get('desafio'))})
    for k in grouped({'killer'}):add(9,k,{'teste_mais_barato':text(k.get('dados',{}).get('teste_mais_barato'))})
    for n,p in parts.items():
        if not p['itens']:
            reasons=[v for v in active.values() if int(n) in v.get('dados',{}).get('ausencia_partes',[])]
            require(bool(reasons),'Parte vazia sem motivo registrado: '+n)
            p['nenhum']=[{'origem':r['id'],'motivo':r['texto']} for r in reasons]
    if m['escolha']=='refutada':parts['9']['aviso']='A escolha é refutada; preservar a refutação e o motivo humano dos registros, sem afirmar que passou.'
    packet={'schema_version':1,'commit_base':m['commit_base'],'hash_blocos':digest(m),'aprovado':False,'escolha':m['escolha'],'partes':parts}
    body=['# Pacote da Etapa 2 · NÃO APROVADO',f"Fontes: {m['commit_base']} · blocos {digest(m)}"]
    for n,p in parts.items():body+=['',f"## {n}. {p['titulo']}",dump(p).strip()]
    return {'schema_version':1,'pacote':packet,'arquivos':{'06-pacote-etapa-2.md':'\n'.join(body)+'\n','pacote.json':dump(packet)},'limite':'Origem e estrutura não validam a primeira decisão, guardião ou pesquisa; conselhos reais continuam necessários.'}


def etapa3(m,root):
    blocks,_=context(m,root);grouped={};ruler=[]
    for k,v in blocks.items():
        if v['bloco'].get('superado_por'):continue
        i=v['item'];d=i.get('dados',{})
        if i['tipo']=='estacionamento':
            reason=text(d.get('motivo'));kind=d.get('tipo');require(kind in {'apelo','necessidade_vizinha','mercado','falha_mercado'},'Tipo de estacionamento inválido')
            key=(kind,i['texto'].strip());row=grouped.setdefault(key,{'tipo':kind,'texto':i['texto'],'origens':[],'motivos':[]})
            row['origens'].append(k);row['motivos'].append({'origem':k,'texto':reason})
        if i['tipo']=='caso':
            output=d.get('saida',{});read_ref(root,output);ruler.append({'caso':k,'saida':output})
    value={'schema_version':1,'commit_base':m['commit_base'],'hash_blocos':digest(m),'itens':list(grouped.values()),'regua_mvp':ruler,'aprovado':False}
    return {'schema_version':1,'consolidado':value,'arquivos':{'06-estacionamento-etapa-3.md':'# Estacionamento · NÃO APROVADO\n\n'+dump(value)},'limite':'Duplicatas literais por tipo; equivalência semântica e efeito no propósito ficam com guardião e pessoa.'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('acao',choices=['etapa2','etapa3']);p.add_argument('entrada');p.add_argument('--git',required=True);a=p.parse_args();print(dump((etapa2 if a.acao=='etapa2' else etapa3)(load(a.entrada),a.git)),end='')
if __name__=='__main__':raise SystemExit(cli(main))
