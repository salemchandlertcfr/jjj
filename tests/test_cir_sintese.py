"""Protocolo local com dossiês Git fictícios; nenhum Claude ou pesquisa real."""
from __future__ import annotations
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT=Path(__file__).resolve().parents[1];SKILL=ROOT/'skills/cir-sintese';SCRIPTS=SKILL/'scripts'
sys.path.insert(0,str(SCRIPTS))
import sintese_core as core

def module(name):
    spec=importlib.util.spec_from_file_location('sintese_test_'+name,SCRIPTS/(name+'.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
cir=module('cir');package=module('pacote');reader=module('leitor');ready=module('pronto');retro=module('retrospectiva');cards=module('cartoes')

class Fixture(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
        self.git('init','-q');self.git('config','user.email','teste@example.invalid');self.git('config','user.name','Teste')
        types=['temor','proposito','familia','metrica','limite','refutada','principio','capacidade','restricao','cenario','confianca','caso','falha_real','descartada','pergunta','estacionamento','dissenso']
        self.items=[{'id':'B'+str(n),'tipo':t,'tema':min(n,5),'subetapa':'4.9','registro':'D-01','texto':'Conteúdo rastreável da área '+chr(64+n)+'.','dados':{}} for n,t in enumerate(types,1)]
        self.items[3]['dados']={'linha_base':'medir com plano registrado','fonte':'F1','limite':'nenhuma perda'}
        self.items[5]['dados']={'refutou':'contradição com a restrição','desafio':'como transferir sem perder?'}
        self.items[6]['dados']={'refuta_se':'um item se perde','onde_mora':'a passagem'}
        self.items[7]['dados']={'metricas':['B4']}
        self.items[8]['dados']={'refuta_se':'piora a perda','onde_mora':'a passagem'}
        self.items[13]['dados']={'refutou':'fora do propósito','desafio':'como manter a cobertura?'}
        self.items[14]['dados']={'data_busca':'2026-10-24','quem_responde':'pesquisa','acoes':['Medir a transferência','Conferir o recebimento','Testar a rastreabilidade']}
        self.items[15]['dados']={'motivo':'não muda o resultado','tipo':'apelo'}
        self.items += [{'id':'C'+str(i),'tipo':'caso','tema':2,'subetapa':'2.6','registro':'D-02','texto':'Caso canônico '+chr(65+i),'dados':{}} for i in range(10)]
        # Motivos de ausência são registros, não texto inventado pelo gerador.
        self.items[0]['dados']={'ausencia_partes':[4,7,9]}
        self.write('saidas.md','# Saídas ideais fictícias\n')
        self.source_commit=self.commit_sources()
        self.m=self.manifest()

    def git(self,*args):
        r=subprocess.run(['git','-C',str(self.root),*args],capture_output=True,text=True);self.assertEqual(r.returncode,0,r.stderr);return r.stdout.strip()
    def write(self,name,body):
        p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(body);return p
    def commit_sources(self):
        self.write('origem.json',core.dump({'schema_version':1,'itens':self.items}));self.git('add','.');self.git('commit','-qm','Fontes fictícias');return self.git('rev-parse','HEAD')
    def manifest(self):
        sha=core.hash_bytes((self.root/'origem.json').read_bytes());head=self.git('rev-parse','HEAD')
        # Referência da saída usa o primeiro commit em que o arquivo existiu.
        output={'arquivo':'saidas.md','commit':self.source_commit,'sha256':core.hash_bytes((self.root/'saidas.md').read_bytes())}
        changed=False
        for item in self.items:
            if item['tipo']=='caso' and item['dados'].get('saida')!=output:item['dados']['saida']=output;changed=True
        if changed:self.commit_sources();return self.manifest()
        entries=[{'id':i['id'],'secao':12 if i['id'].startswith('C') else int(i['id'][1:]),'origem':{'arquivo':'origem.json','commit':head,'sha256':sha,'item':i['id']}} for i in self.items]
        m={'schema_version':1,'commit_base':head,'hashes_estado':{'origem.json':sha},'inventario':copy.deepcopy(entries),'blocos':entries,'ligacoes':[],'escolha':'referencia','avisos_metodo':'Exercício fictício; sem especialidade curada.'}
        m['em_vez_disso']=[]
        for i in self.items:
            if i['tipo'] in {'principio','restricao'}:
                body='Conferir a passagem preservando cada item.'
                m['em_vez_disso'].append({'id':i['id'],'texto':body,'sessao_redator':'RD','verificacao':{'hash':core.digest({'texto':body,'origem':i}),'sessao':'VR','veredito':'sustentada','trecho':i['texto']}})
        return m
    def link(self,body='Conteúdo rastreável da área B.',origins=None):
        self.m['suas_versoes']=cir.seal_versions({'essencia':'a essência anterior','o_que_nao_e':'exclusões anteriores','temor':self.items[0]['texto'],'sequencia':0})
        r=origins or ['B2']
        l={'id':'lig-2.1','secao':2,'texto':body,'origens':r,'sessao_redator':'RD','sessao_decompositor':'DC','sequencia':1,'conclusao':True,'afirmacoes':[{'id':'A1','texto':body,'inicio':0,'fim':len(body),'origens':r}]}
        self.m['ligacoes']=[l];return l
    def verdict(self,status='sustentada'):
        a=cir.batches(self.m,self.root)['lotes'][0][0];return {'schema_version':1,'vereditos':[{'id':a['id'],'hash':a['hash'],'sessao':'VR','veredito':status,'trecho':a['fontes'][0]['texto']}]}
    def evidence_report(self):
        self.write('06-cir.md',cir.mount(self.m,self.root)['arquivos']['06-cir.md'])
        outputs={**package.etapa2(self.m,self.root)['arquivos'],**package.etapa3(self.m,self.root)['arquivos']}
        for name,body in outputs.items():self.write(name,body)
        arts={name:core.hash_bytes((self.root/name).read_bytes()) for name in ['06-cir.md',*outputs]};bound=core.digest(arts)
        es=[{'id':'EV'+k,'item':k,'secao':'Prova '+k,'trecho':'Evidência declarada fictícia','responsavel':'critico-teste','hash_artefatos':bound,'resultado':'passa','verificacoes':{f:True for f in fields},'quantidade':12} for k,fields in ready.RULES.items()]
        self.write('evidencias.json',core.dump({'schema_version':1,'evidencias':es}));self.git('add','.');self.git('commit','-qm','Evidências fictícias');c=self.git('rev-parse','HEAD');sha=core.hash_bytes((self.root/'evidencias.json').read_bytes())
        value={'schema_version':1,'escolha':'referencia','artefatos':arts,'itens':[{'id':e['item'],'evidencia_id':e['id'],'evidencia':{'arquivo':'evidencias.json','commit':c,'sha256':sha,'secao':e['secao']}} for e in es],'pendencias':[],'conferencia_fontes':{'hash_artefatos':bound,'executada':True,'todas_citadas':True,'pendentes':[]}}
        return value

class OriginsTest(Fixture):
    def test_literal_copies_dissent_and_all_sections(self):
        body=cir.mount(self.m,self.root)['arquivos']['06-cir.md'];self.assertIn('«'+self.items[-11]['texto']+'»',body)
        for n in range(1,18):self.assertIn('## '+str(n)+'. ',body)
        self.assertIn('NÃO APROVADO',body);self.assertIn('B17',body.split('## 17.')[1])
    def test_changed_unregistered_file_blocks_mount(self):
        self.write('origem.json','{}');self.assertRaises(core.Invalid,cir.mount,self.m,self.root)
    def test_bad_hash_path_and_future_origin_rejected(self):
        for mutation in ['hash','path','commit']:
            m=copy.deepcopy(self.m);o=m['blocos'][0]['origem']
            if mutation=='hash':o['sha256']='0'*64
            elif mutation=='path':o['arquivo']='../origem.json'
            else:o['commit']='0'*40
            self.assertRaises(core.Invalid,cir.mount,m,self.root)
    def test_symlink_source_rejected(self):
        p=self.root/'origem.json';raw=p.read_bytes();p.unlink();(self.root/'outro').write_bytes(raw);p.symlink_to('outro')
        self.assertRaises(core.Invalid,cir.mount,self.m,self.root)
    def test_missing_blocks_inventory_catches_six_omissions(self):
        missing=[e['id'] for e in self.m['blocos'][:6]];self.m['blocos']=self.m['blocos'][6:]
        result=cir.check(self.m,self.root);self.assertEqual(result['cobertura_faltante'],sorted(missing))
    def test_inventory_cannot_omit_the_same_item_as_blocks(self):
        self.m['blocos']=self.m['blocos'][1:];self.m['inventario']=self.m['inventario'][1:]
        self.assertRaises(core.Invalid,cir.check,self.m,self.root)
    def test_less_than_ten_cases_does_not_pass(self):
        self.items=[i for i in self.items if not i['id'].startswith('C')]
        self.commit_sources();self.m=self.manifest()
        self.assertTrue(any(i['tipo']=='casos_insuficientes' for i in cir.check(self.m,self.root)['sinais']))
    def test_manual_edit_detected_and_five_remounts_preserve_copies(self):
        original=cir.mount(self.m,self.root)['arquivos']['06-cir.md']
        self.assertTrue(any(s['tipo']=='edicao_manual' for s in cir.check(self.m,self.root,original+'inventado')['sinais']))
        for i in range(5):
            self.items[0]['texto']='Temor esclarecido na revisão '+chr(65+i);self.items[0]['registro']='D-REV'+str(i)
            self.commit_sources();self.m=self.manifest();rebuilt=cir.mount(self.m,self.root)['arquivos']['06-cir.md']
            self.assertIn('«'+self.items[8]['texto']+'»',rebuilt)
            self.assertIn('«'+self.items[16]['texto']+'»',rebuilt)
            self.assertNotIn('inventado',rebuilt)
    def test_abstention_has_no_reference_sections_or_packet(self):
        self.m['escolha']='abstencao';self.assertIn('Sem conceito',cir.mount(self.m,self.root)['arquivos']['06-cir.md']);self.assertIsNone(package.etapa2(self.m,self.root)['pacote'])
    def test_lost_family_redirect_and_superceded_history(self):
        self.items[6]['dados']['familia_perdeu']=True;self.commit_sources();self.m=self.manifest();self.m['blocos'][1]['superado_por']='B1'
        body=cir.mount(self.m,self.root)['arquivos']['06-cir.md'];self.assertIn('B7',body.split('## 6.')[1].split('## 7.')[0]);self.assertIn('superado por B1',body.split('## 17.')[1])

class LinksTest(Fixture):
    def test_unsupported_claims_and_verdicts_current(self):
        self.link();result=cir.check(self.m,self.root,reviews=self.verdict());self.assertTrue(result['limpo'])
        self.m['ligacoes'][0]['texto']='Outro texto';self.assertRaises(core.Invalid,cir.check,self.m,self.root)
    def test_missing_or_partial_decomposition_rejected(self):
        l=self.link();l['afirmacoes'][0]['fim']-=1;l['afirmacoes'][0]['texto']=l['texto'][:-1]
        self.assertRaises(core.Invalid,cir.mount,self.m,self.root)
    def test_author_cannot_decompose_or_verify(self):
        l=self.link();l['sessao_decompositor']='RD';self.assertRaises(core.Invalid,cir.mount,self.m,self.root)
        l['sessao_decompositor']='DC';v=self.verdict();v['vereditos'][0]['sessao']='RD';self.assertRaises(core.Invalid,cir.check,self.m,self.root,None,v)
    def test_user_first_seal_and_sequence_enforced(self):
        self.link();self.m['suas_versoes']['essencia']='alterada';self.assertRaises(core.Invalid,cir.mount,self.m,self.root)
    def test_redactor_and_verifier_projection_hide_user_and_authors(self):
        self.link();brief=cir.writer(self.m,self.root,2);self.assertNotIn('essência anterior',core.dump(brief));self.assertEqual(len(brief['blocos']),1)
        tasks=core.dump(cir.batches(self.m,self.root));self.assertNotIn('sessao_redator',tasks);self.assertNotIn('essência anterior',tasks)
    def test_verdict_obsolete_or_unsupported_never_clean(self):
        self.link();v=self.verdict('exagerada');self.assertFalse(cir.check(self.m,self.root,reviews=v)['limpo'])
        v['vereditos'][0]['hash']='0'*64;self.assertRaises(core.Invalid,cir.check,self.m,self.root,None,v)
    def test_numbers_scope_confidence_and_unknown_origin_rejected(self):
        for body,kind in [('Chegou a 95%.','numero_fora_origem'),('Garante todas as entregas.','generalizacao'),('Confiança alta.','confianca_sem_base')]:
            self.link(body);self.assertIn(kind,[s['tipo'] for s in cir.check(self.m,self.root)['sinais']])
        self.link(origins=['NAO_EXISTE']);self.assertRaises(core.Invalid,cir.mount,self.m,self.root)
    def test_batches_bounded_seeded_and_usage_transitive(self):
        l=self.link();self.m['ligacoes']=[]
        for n in range(43):
            x=copy.deepcopy(l);x['id']='lig-2.'+str(n);x['conclusao']=False;x['afirmacoes'][0]['id']='A'+str(n);self.m['ligacoes'].append(x)
        batches=cir.batches(self.m,self.root,5);self.assertEqual([len(b) for b in batches['lotes']],[20,20,3]);self.assertEqual(batches,cir.batches(self.m,self.root,5))
        self.assertEqual(len(cir.uses(self.m,self.root,'B2')['ligacoes']),43)

class PackageTest(Fixture):
    def test_nine_parts_and_same_snapshot(self):
        value=package.etapa2(self.m,self.root)['pacote'];self.assertEqual(len(value['partes']),9);self.assertEqual(value['hash_blocos'],cir.mount(self.m,self.root)['hash_blocos'])
        self.assertEqual(value['partes']['6']['itens'][0]['texto'],self.items[6]['texto'])
    def test_metric_empty_reason_and_alternative_verification_required(self):
        for kind in ['metric','substitute','reason']:
            m=copy.deepcopy(self.m)
            if kind=='substitute':m['em_vez_disso'][0]['verificacao']['hash']='0'*64
            elif kind=='reason':m['blocos']=[b for b in m['blocos'] if b['id']!='B1']
            else:m['blocos']=[b for b in m['blocos'] if b['id']!='B4']
            self.assertRaises(core.Invalid,package.etapa2,m,self.root)
    def test_stage_three_dedup_keeps_every_origin_and_reason(self):
        i=copy.deepcopy(self.items[15]);i['id']='B99';self.items.append(i);self.commit_sources();self.m=self.manifest();next(b for b in self.m['blocos'] if b['id']=='B99')['secao']=16
        x=package.etapa3(self.m,self.root)['consolidado'];self.assertEqual(len(x['itens']),1);self.assertEqual(x['itens'][0]['origens'],['B16','B99']);self.assertEqual(len(x['itens'][0]['motivos']),2)

class ReaderTest(unittest.TestCase):
    def packet(self,n=1):
        return {'schema_version':1,'cir':'propósito núcleo exclusão tarefa bancada','pacote':'passagem','gabarito':{k:v for k,v in zip(reader.FIELDS,['propósito','núcleo','exclusão','tarefa','bancada'])},'modelo_juiz':'claude-escolhido','leitores':[{'id':'L'+str(i),'sessao':f'R{n}-L{i}','especialidade':s,'modelo':'claude-escolhido'} for i,s in enumerate(['sistemas','dominio','generalista'],1)],'juizes':[{'id':'J'+str(i),'sessao':f'R{n}-J{i}','modelo':'claude-escolhido'} for i in (1,2)]}
    def start(self):return reader.open_round(reader.start({'previstas':[{'id':'P1','texto':'pergunta privada'}]}),self.packet())
    def advance(self,s,central=False,disagree=False,ambiguity=None):
        r=s['rodadas'][-1]
        for a in r['leitores']:s=reader.record(s,{'tipo':'reformulacoes','ator':a['id'],'conteudo':{f:'Minha leitura' for f in reader.FIELDS}})
        for i,a in enumerate(r['leitores']):s=reader.record(s,{'tipo':'perguntas','ator':a['id'],'conteudo':[{'id':'Q1','texto':'Qual encerra?','modo':'pergunta','muda_primeira_decisao':central}] if i==0 else []})
        for a in r['juizes']:
            value={'R'+str(i):{f:{'veredito':'diverge' if disagree and a['id']=='J2' else 'bate','trecho':r['gabarito'][f]} for f in reader.FIELDS} for i in (1,2,3)}
            s=reader.record(s,{'tipo':'julgamentos','ator':a['id'],'conteudo':value})
        return reader.record(s,{'tipo':'classificacao','ator':'condutora','conteudo':[{'id':'Q1','classe':'central' if central else 'secundaria','quem':'dossie','destino':'registrar na origem'}],'comparacao_leituras':{'conferida':True,'divergencias':ambiguity or []}})
    def test_private_prediction_and_reformulation_first(self):
        s=self.start();self.assertNotIn('pergunta privada',core.dump(reader.brief(s,'L1')))
        self.assertRaises(core.Invalid,reader.record,s,{'tipo':'perguntas','ator':'L1','conteudo':[]})
    def test_clean_round_closes_but_central_disagreement_or_ambiguity_do_not(self):
        for flags in [{},{'central':True},{'disagree':True},{'ambiguity':['núcleo diferente']}]:
            s=self.advance(self.start(),**flags);self.assertEqual(s['rodadas'][-1]['resultado']['fechou'],not flags)
    def test_new_sessions_and_extra_round_require_permission(self):
        s=self.advance(self.start(),central=True);self.assertRaises(core.Invalid,reader.open_round,s,self.packet())
        for n in (2,3):s=reader.open_round(s,self.packet(n));s=self.advance(s,central=True)
        self.assertRaises(core.Invalid,reader.open_round,s,self.packet(4));p=self.packet(4);p['autorizacao']={'resposta':'sim','registro':'D-04','rodada':4};self.assertEqual(len(reader.open_round(s,p)['rodadas']),4)
    def test_contamination_invalidation_preserves_history(self):
        s=reader.invalidate(self.start(),'leu dossiê');self.assertFalse(s['rodadas'][-1]['resultado']['valida']);s=reader.open_round(s,self.packet(2));self.assertEqual(len(s['rodadas']),2)
    def test_model_and_state_edit_rejected(self):
        p=self.packet();p['leitores'][0]['modelo']='outro';self.assertRaises(core.Invalid,reader.open_round,reader.start({'previstas':[{'id':'P','texto':'prevista'}]}),p)
        s=self.start();s['previstas'][0]['texto']='alterado';self.assertRaises(core.Invalid,reader.brief,s,'L1')

class ReadinessRetroTest(Fixture):
    def test_no_evidence_is_not_verified(self):
        v=self.evidence_report();v['itens']=[];r=ready.assess(v,self.root);self.assertTrue(all(i['estado']=='nao_verificado' for i in r['itens']));self.assertFalse(r['pronto_sem_ressalvas'])
    def test_planted_three_missing_and_one_wrong_evidence_fail_four(self):
        v=self.evidence_report();v['itens']=v['itens'][3:];v['itens'][0]['evidencia_id']='EVI5';r=ready.assess(v,self.root)
        self.assertEqual(sum(i['estado']!='passa' for i in r['itens']),4)
    def test_evidence_current_version_and_stale_rejected(self):
        v=self.evidence_report();r=ready.assess(v,self.root);self.assertTrue(all(i['estado']=='passa' for i in r['itens']))
        self.write('06-cir.md','outra versão');self.assertRaises(core.Invalid,ready.assess,v,self.root)
    def approval(self):
        v=self.evidence_report();r=ready.assess(v,self.root);c=self.git('rev-parse','HEAD')
        packet={'resposta':'sim','commit':c,'data':'2026-10-24','registro':'D-AP','ressalvas':[]}
        for k,needed in [('vigia',bool(r['vigia_local'])),('fontes',not r['fontes_conferidas_declaradas']),('pendencias',not r['pendencias_com_destino'])]:
            if needed:packet['ressalvas'].append({'id':k,'registro':'D-R','motivo':'limite declarado','objetivo':'conservar incerteza'})
        return r,packet,ready.approve(r,packet,self.root)
    def test_approval_exact_yes_commit_and_waivers(self):
        r,p,a=self.approval();self.assertEqual(a['commit'],p['commit']);p['resposta']='pode ser';self.assertRaises(core.Invalid,ready.approve,r,p,self.root)
        p['resposta']='sim';p['commit']=self.source_commit;self.assertRaises(core.Invalid,ready.approve,r,p,self.root)
    def retrospective(self):
        _,_,a=self.approval();review={'funcionou':'rastreabilidade','nao_funcionou':'termo sem definição'};review['hash']=core.digest(review)
        return {'schema_version':1,'aprovacao':a,'sua_avaliacao':review,'comparacoes':[],'melhorias':[],'tangentes':{'classificadas':0,'com_funcao':0},'projeto_real':False}
    def test_retro_after_approval_and_zero_denominator_unknown(self):
        v=self.retrospective();r=retro.run(v,self.root);self.assertIsNone(r['aprendizado']);self.assertIsNone(r['taxa_surpresa_final']);v['aprovacao']['resposta']='não';self.assertRaises(core.Invalid,retro.run,v,self.root)
    def test_decision_outcome_separate_and_reconstruction_marked(self):
        v=self.retrospective()
        for i,(quality,outcome) in enumerate([('boa','ruim'),('ruim','bom'),('boa','bom'),('ruim','ruim')]):v['comparacoes'].append({'id':'D'+str(i),'expectativa':{'tipo':'reconstrucao','texto':'o que se esperava','cega_declarada':True,'sessao':'RE'},'qualidade_decisao':quality,'base_na_epoca':'informação anterior','desfecho':outcome})
        r=retro.run(v,self.root);self.assertEqual([c['qualidade_decisao'] for c in r['comparacoes']],['boa','ruim','boa','ruim'])
        v['comparacoes'][0]['expectativa']['cega_declarada']=False;self.assertRaises(core.Invalid,retro.run,v,self.root)
    def test_generic_improvement_and_domain_leak_blocked(self):
        v=self.retrospective();v['melhorias']=[{'id':'M1','dono':'equipe','skill':'cir-mapa','secao':'2.1','acao':'melhorar comunicação','origem':'D1'}];self.assertRaises(core.Invalid,retro.run,v,self.root)
        v['melhorias']=[];v.update(projeto_real=True,metodo={'nome_projeto':'Lago Azul'});self.assertRaises(core.Invalid,retro.run,v,self.root)
    def test_real_learning_strict_whitelist_and_test_suppression(self):
        v=self.retrospective();v.update(projeto_real=True,hash_projeto='a'*64,data='2026-10-24',metodo={'fracao_tangentes_4_4':0.3,'taxa_4_10':0.1,'passagem':{'rodadas':2}},notas_metodo=['termo_sem_definicao'])
        r=retro.run(v,self.root);self.assertNotIn('rastreabilidade',core.dump(r['aprendizado']));v['projeto_real']=False;self.assertIsNone(retro.run(v,self.root)['aprendizado'])
        v['projeto_real']=True;v['notas_metodo']=['Lago Azul'];self.assertRaises(core.Invalid,retro.run,v,self.root)
    def test_brier_unknown_not_value_decision_and_median_small_n(self):
        self.assertIsNone(retro.brier([{'probabilidade':None}])['brier']);self.assertAlmostEqual(retro.brier([{'probabilidade':0.8,'desfecho':True,'referencia_desfecho':'registro'}])['brier'],0.04)
        v={'projetos':[{'projeto':'A','taxa_final':0.2},{'projeto':'B','taxa_final':0.4}]};r=retro.medians(v)['metricas']['taxa_final'];self.assertIsNone(r['mediana']);self.assertEqual(r['valores'],[0.2,0.4])
    def test_audit_never_claims_done_or_rewrites(self):
        a=ready.audit('Uma plataforma com preço e tela.');self.assertEqual(len(a['itens']),14);self.assertTrue(all(i['estado']=='nao_verificado' for i in a['itens']));self.assertFalse(a['reescreveu']);self.assertTrue(cir.audit('Garante 100%')['sinais'])

class PortableTest(Fixture):
    def test_cards_match_selected_source_and_explicit_index(self):
        body=(SKILL/'references/cartoes.md').read_text();source=(ROOT/'sources/originais/plano-cir-sintese.md').read_text();literal=source.split('## 5. Cartões das sub-etapas')[1].split('```markdown\n')[1].split('```')[0];self.assertIn(literal,body)
        import re
        entries=[{'id':k,'titulo':title,'dose':cards.DOSES[k]} for k,title in re.findall(r'^### (6\.[1-6]) ([^\n]+)',body,re.M)];self.assertTrue(cards.check(body,entries)['valido']);entries[0]['dose']='leve';self.assertRaises(core.Invalid,cards.check,body,entries)
    def test_package_extracted_cli_mount_check_and_handoff(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);archive=p/'cir-sintese.skill';r=subprocess.run([sys.executable,'-B',str(ROOT/'scripts/empacotar_skill.py'),'--skill',str(SKILL),'--destino',str(archive)],capture_output=True,text=True);self.assertEqual(r.returncode,0,r.stderr)
            with zipfile.ZipFile(archive) as z:z.extractall(p)
            inp=self.write('06-blocos.md','# Blocos\n\n```json cir-sintese-v1\n'+core.dump(self.m)+'```\n')
            for script,args in [('cir',['montar']),('cir',['conferir']),('pacote',['etapa2']),('pacote',['etapa3'])]:
                r=subprocess.run([sys.executable,'-B',str(p/'cir-sintese/scripts'/ (script+'.py')),*args,str(inp),'--git',str(self.root)],cwd=p,capture_output=True,text=True);self.assertEqual(r.returncode,0,r.stderr);self.assertEqual(json.loads(r.stdout)['schema_version'],1)

if __name__=='__main__':unittest.main()
