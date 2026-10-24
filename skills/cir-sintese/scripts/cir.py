#!/usr/bin/env python3
"""Monta cópias literais e ligações; confere a versão e prepara tarefas sem executar agentes."""
from __future__ import annotations
import argparse
import re
import random
from sintese_core import (TITLES,array,cli,context,digest,dump,fold,hash_bytes,ident,index,load,refs,require,section,signals,text)


def links(manifest,blocks):
    out=index(manifest.get('ligacoes',[]));claims={}
    versions=manifest.get('suas_versoes',{})
    if out:
        require(versions.get('hash')==digest({k:versions[k] for k in ('essencia','o_que_nao_e','temor','sequencia')}),'Suas versões não foram seladas')
        require(type(versions.get('sequencia')) is int,'Sequência anterior obrigatória')
    for k,l in out.items():
        require(k.startswith('lig-') and type(l.get('secao')) is int and 1<=l['secao']<=17,'Ligação sem seção')
        body=text(l.get('texto'));r=refs(l.get('origens'),blocks);require(bool(r),'Ligação sem origem')
        ident(l.get('sessao_redator'));ident(l.get('sessao_decompositor'));require(l['sessao_redator']!=l['sessao_decompositor'],'Quem escreve não decompõe')
        require(type(l.get('sequencia')) is int and l['sequencia']>versions['sequencia'],'Redação anterior às suas versões')
        require(type(l.get('conclusao')) is bool,'Declare conclusão da seção')
        covered=set()
        for a in index(l.get('afirmacoes')).values():
            require(a['id'] not in claims,'Afirmação duplicada');orig=refs(a.get('origens'),r);require(bool(orig),'Afirmação sem origem')
            start,end=a.get('inicio'),a.get('fim');require(type(start) is int and type(end) is int and 0<=start<end<=len(body),'Span de afirmação inválido')
            require(a.get('texto')==body[start:end],'Afirmação não corresponde à ligação')
            span=set(range(start,end));require(not span&covered,'Afirmações sobrepostas');covered|=span
            claims[a['id']]={**a,'ligacao':k,'sessao_redator':l['sessao_redator'],'sessao_decompositor':l['sessao_decompositor'],'secao':l['secao']}
        require(all(i in covered for i,c in enumerate(body) if not c.isspace()),'Frase da ligação sem afirmação')
    return out,claims


def seal_versions(value):
    for k in ('essencia','o_que_nao_e','temor'):text(value.get(k))
    require(type(value.get('sequencia')) is int and value['sequencia']>=0,'Sequência inválida')
    clean={k:value[k] for k in ('essencia','o_que_nao_e','temor','sequencia')};return {**clean,'hash':digest(clean)}


def mount(manifest,root):
    blocks,catalog=context(manifest,root);ls,claims=links(manifest,blocks)
    lines=['# CIR · NÃO APROVADO · gerado; não editar',f"\nCommit das fontes: {manifest['commit_base']} · blocos: {digest(manifest)}",'\n## Como ler','«…» é cópia literal da origem; o restante é ligação, sujeita a conferência atômica. IDs, arquivo, registro e hash acompanham cada cópia. Hash não prova suporte semântico.']
    lines+=['Avisos de método: '+text(manifest.get('avisos_metodo'))]
    if manifest['escolha']=='refutada':lines+=['Escolha humana de conceito REFUTADO: a escolha não significa que resistiu à prova. Preserve refutação e motivo dos registros.']
    for n,title in enumerate(TITLES,1):
        lines+=['',f'## {n}. {title}']
        if manifest['escolha']=='abstencao' and 7<=n<=10:
            lines+=['Sem conceito de referência: encerramento por abstenção.'];continue
        selected=[(k,v) for k,v in blocks.items() if section(v,manifest)==n]
        conclusions=[l for l in ls.values() if l['secao']==n and l['conclusao']]
        require(len(conclusions)<=1,'Duas conclusões na seção')
        for l in conclusions:lines += [l['texto']+' ('+l['id']+' · '+', '.join(l['origens'])+')']
        if not selected:lines+=['SEM BLOCO · pendência à origem.']
        for k,v in sorted(selected):
            b,item=v['bloco'],v['item'];o=b['origem'];suffix=(' · superado por '+ident(b['superado_por'])) if b.get('superado_por') else ''
            if b.get('superado_por'):require(b['superado_por'] in blocks,'Sucessor inexistente')
            lines += [f"- {k}{suffix} · «{item['texto']}» · {item['subetapa']} · {item['registro']} · {o['arquivo']} · {o['commit']} · {o['sha256']}"]
            if item.get('dados'):lines+=['  Dados literais: '+dump(item['dados']).strip().replace('\n',' ')]
        for l in ls.values():
            if l['secao']==n and not l['conclusao']:lines += [l['texto']+' ('+l['id']+' · '+', '.join(l['origens'])+')']
    return {'schema_version':1,'commit_base':manifest['commit_base'],'hash_blocos':digest(manifest),'arquivos':{'06-cir.md':'\n'.join(lines)+'\n'},'aprovado':False,'limite':'A montagem não executa verificação, pesquisa, leitores, vigia externa ou aprovação.'}


def batches(manifest,root,seed=0):
    blocks,_=context(manifest,root);_,claims=links(manifest,blocks);tasks=[]
    for k,a in claims.items():
        sources=[{'id':r,'texto':blocks[r]['item']['texto'],'dados':blocks[r]['item'].get('dados',{})} for r in a['origens']]
        tasks.append({'id':k,'afirmacao':a['texto'],'hash':digest({'texto':a['texto'],'fontes':sources}),'fontes':sources})
    require(type(seed) is int,'Semente inteira');random.Random(seed).shuffle(tasks)
    return {'schema_version':1,'lotes':[tasks[i:i+20] for i in range(0,len(tasks),20)],'limite':'Sem autoria, seção ou outras respostas. Ordem sorteada; diversidade de seções não garantida em lote pequeno.'}


def check(manifest,root,actual=None,reviews=None):
    blocks,catalog=context(manifest,root);ls,claims=links(manifest,blocks);expected=mount(manifest,root)['arquivos']['06-cir.md'];issues=[]
    if actual is not None and actual!=expected:issues.append({'tipo':'edicao_manual','destino':'remontar da origem'})
    missing=sorted(set(catalog)-set(blocks))
    if missing:issues.append({'tipo':'cobertura','ids':missing})
    cases=[v for v in catalog.values() if v['item']['tipo']=='caso']
    if len(cases)<10:issues.append({'tipo':'casos_insuficientes','quantidade':len(cases)})
    for n in range(1,18):
        if manifest['escolha']=='abstencao' and 7<=n<=10:continue
        if not any(section(v,manifest)==n for v in blocks.values()):issues.append({'tipo':'secao_sem_bloco','secao':n})
    rows={a['id']:a for batch in batches(manifest,root)['lotes'] for a in batch};verdicts=index((reviews or {}).get('vereditos',[]))
    require(set(verdicts)<=set(rows),'Veredito de afirmação inexistente')
    distribution={}
    for k,a in claims.items():
        for r in a['origens']:
            tema=str(blocks[r]['item']['tema']);distribution[tema]=distribution.get(tema,0)+1
        body=a['texto'];source=' '.join(blocks[r]['item']['texto']+' '+dump(blocks[r]['item'].get('dados',{})) for r in a['origens'])
        numbers=lambda s:set(re.findall(r'(?<![\w])\d+(?:[.,]\d+)?',s))
        if numbers(body)-numbers(source):issues.append({'tipo':'numero_fora_origem','id':k})
        if re.search(r'\b(alta|media|provavel|confian[cç]a)\b',fold(body)) and not numbers(body):issues.append({'tipo':'confianca_sem_base','id':k})
        for s in signals(body):issues.append({'id':k,**s,'destino':'revisao_semantica'})
        v=verdicts.get(k)
        if not v:issues.append({'tipo':'verificacao_pendente','id':k});continue
        require(v.get('hash')==rows[k]['hash'],'Veredito obsoleto')
        require(v.get('sessao') not in {a['sessao_redator'],a['sessao_decompositor']},'Quem escreveu/decompôs não verifica');ident(v.get('sessao'))
        require(v.get('veredito') in {'sustentada','nao_sustentada','exagerada','contradiz'},'Veredito inválido')
        excerpt=text(v.get('trecho'));require(any(excerpt in f['texto'] or excerpt in dump(f['dados']) for f in rows[k]['fontes']),'Veredito sem trecho da fonte')
        if v['veredito']!='sustentada':issues.append({'tipo':v['veredito'],'id':k})
    return {'schema_version':1,'limpo':not issues,'sinais':issues,'distribuicao_referencias_por_tema':distribution,'cobertura_faltante':missing,'afirmacoes':len(claims),'limite':'Triagem lexical e coerência dos artefatos; decomposição, semântica e independência exigem auditoria real.'}


def writer(manifest,root,n):
    blocks,_=context(manifest,root);require(type(n) is int and 1<=n<=17,'Seção inválida')
    selected=[{'id':k,**v['item']} for k,v in blocks.items() if section(v,manifest)==n]
    out={'schema_version':1,'secao':n,'blocos':selected,'tarefa':'Escreva conclusão e ligações com IDs; não reescreva cópias, números ou dissenso. Decompositor separado depois.'}
    if n in {1,14}:out['cir']=mount(manifest,root)['arquivos']['06-cir.md']
    return out


def uses(manifest,root,term):
    blocks,_=context(manifest,root);ls,_=links(manifest,blocks);text(term)
    direct={k for k,v in blocks.items() if term==k or term.casefold() in dump(v['item']).casefold()}
    dependent=set(direct)
    while True:
        old=set(dependent)
        for k,v in blocks.items():
            if set(v['item'].get('dados',{}).get('depende_de',[]))&dependent:dependent.add(k)
        if old==dependent:break
    return {'schema_version':1,'diretos':sorted(direct),'dependentes':sorted(dependent),'ligacoes':[k for k,l in ls.items() if set(l['origens'])&dependent],'limite':'Arestas declaradas e busca literal não determinam sozinhas se um veredito mudaria.'}


def audit(body):return {'schema_version':1,'sem_dossie':True,'montagem':False,'numeros':re.findall(r'\d+(?:[.,]\d+)?',body),'sinais':signals(body),'limite':'Sem registros não há conferência de origem; números e garantias são candidatos para revisão.'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('acao',choices=['montar','conferir','afirmacoes','usos','redator','suas-versoes']);p.add_argument('entrada');p.add_argument('--git');p.add_argument('--documento');p.add_argument('--vereditos');p.add_argument('--termo');p.add_argument('--secao',type=int);p.add_argument('--semente',type=int,default=0);p.add_argument('--sem-dossie',action='store_true');a=p.parse_args()
    if a.sem_dossie:
        require(a.acao=='conferir','Auditoria usa conferir');from pathlib import Path
        out=audit(Path(a.entrada).read_text())
    else:
        m=load(a.entrada)
        if a.acao=='suas-versoes':out=seal_versions(m)
        else:
            require(a.git,'Informe --git com o dossiê explicitamente autorizado')
            if a.acao=='montar':out=mount(m,a.git)
            elif a.acao=='afirmacoes':out=batches(m,a.git,a.semente)
            elif a.acao=='usos':out=uses(m,a.git,a.termo)
            elif a.acao=='redator':out=writer(m,a.git,a.secao)
            else:
                from pathlib import Path
                out=check(m,a.git,Path(a.documento).read_text() if a.documento else None,load(a.vereditos) if a.vereditos else None)
    print(dump(out),end='');return int(a.acao=='conferir' and not a.sem_dossie and not out['limpo'])
if __name__=='__main__':raise SystemExit(cli(main))
