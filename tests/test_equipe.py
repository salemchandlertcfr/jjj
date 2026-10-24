"""Protocolo local com eventos fictícios; não executa modelos ou especialistas reais."""
from __future__ import annotations
import copy
import importlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT=Path(__file__).resolve().parents[1];SKILL=ROOT/"skills/equipe-especialistas"
sys.path.insert(0,str(SKILL/"scripts"))
core=importlib.import_module("equipe_core");agenda=importlib.import_module("pauta")
desk=importlib.import_module("mesa");minutes=importlib.import_module("ata")
synthesis=importlib.import_module("sintese");report=importlib.import_module("parecer")
fusion=importlib.import_module("fusao");costs=importlib.import_module("custos")


def sample(name):return json.loads((SKILL/"assets/modelos"/name).read_text())


def event_for(state,actor=None):
    phase=desk.next_step(state);kind=phase["tipo"];actor=actor or (phase["atores"][0] if phase["atores"] else "mesa")
    member=next((m for m in state["membros"] if m["id"]==actor),{})
    data={"id":f"EV-{state['revisao']}","tipo":kind,"ator":actor,"rodada":phase["rodada"]}
    if kind=="preparacao":
        data.update(leitura="a área examina a transferência",posicao_inicial="Manter informação rastreável.",critica_base="critério ainda precisa de precisão",
                    contribuicoes=[{"id":member["sigla"]+"-1","texto":"Conferir o recebimento pela área "+member["sigla"],"por_que":"preservar informação","muda":"o critério de término","evidencias":[{"tipo":"fonte","id":"F1"}]}],fontes_novas=[],perguntas=[],nao_sei=[])
    elif kind=="abertura":
        ids=list(core.contributions(state));data.update(mapa=ids,unicas=ids,divergencias=[{"id":"D1","texto":"critério de término","contribuicoes":ids}])
    elif kind=="fala":
        data.update(passo=phase["rodada"]>1)
        if not data["passo"]:data.update(motivo="A informação precisa chegar.",posicao="Manter conferência explícita.",referencias=list(core.contributions(state)),fatos_novos=["o recebimento ainda pode estar pendente"],contra_proposta="terminar cedo perde informação")
    elif kind in {"critica","critica_individual","revisao"}:
        data.update(pontos=[],conferido=["pauta, fontes e destinos"],abertos=[])
        if kind=="revisao":data["hash_saida"]=core.digest(next(e["saida"] for e in state["eventos"] if e["tipo"]=="saida"))
    elif kind=="fechamento":data.update(decisoes=[{"id":"D1","situacao":"opcoes","motivo":"precisa de condição discriminante","referencias":list(core.contributions(state))}],parar=False)
    elif kind=="checagem":data.update(resultados=[])
    elif kind=="posicao":data.update(apoio="Manter informação rastreável.",evidencia_mais_forte="F1",incerteza="a condição de término",mudaria_se="nova evidência",dissenso=[{"id":"D1","argumento":"critério único não serve a todos os casos de "+actor,"mudaria_se":"houver evidência discriminante"}])
    elif kind in {"saida","resposta","replica_individual"}:
        data["saida"]=output_for(state)
        if kind!="saida":data.update(respostas=[],encerrar=True)
    prefix=member.get("selo","")+"\n" if kind in {"preparacao","fala","posicao"} else "Registro do protocolo\n"
    data["texto"]=prefix+json.dumps(data,ensure_ascii=False)
    return data


def output_for(state):
    destinations=[{"id":k,"destino":"entrou","motivo":"preservar informação única","lastro":["F1"]} for k in core.contributions(state)]
    dissent=[]
    for e in state["eventos"]:
        if e["tipo"]=="posicao":
            for d in e["dissenso"]:dissent.append({"id":d["id"],"argumentos":[{"ator":e["ator"],"argumento":d["argumento"]}],"mudaria_se":d["mudaria_se"]})
    mode=state["pauta"]["modo"]
    if mode=="verificacao":
        return {"destinos":destinations,"dissenso":dissent,"afirmacoes":[{"id":c["id"],"conclusao":"indeterminado","justificativa":"falta uma medição","lastro":[],"incerteza":"a condição do processo","especialidade":"controle e sinais","mudaria_se":"houver medição"} for c in state["pauta"]["afirmacoes"]]}
    if mode=="integracao":return {"destinos":destinations,"dissenso":dissent,"conflitos":[],"combinam":[],"dependencias":[]}
    return {"versao":"Transferência rastreável com critérios de término mantidos como opções.","por_que":[],"mudancas":[],"destinos":destinations,"dissenso":dissent,
            "divergencias":[{"id":"D1","situacao":"opcoes","motivo":"não fundir incompatíveis","decidiria":"evidência discriminante"}] if any(e["tipo"]=="abertura" for e in state["eventos"]) else [],"lacunas":[],"perguntas_usuario":[],"do_lider":[],"numeros":[]}


def advance(state,until=None):
    for _ in range(80):
        phase=desk.next_step(state)["tipo"]
        if phase==until or phase=="concluida":return state
        state=desk.record(state,event_for(state))
    raise AssertionError("protocolo não terminou")


class AgendaTest(unittest.TestCase):
    def test_missing_question_format_or_refutation_rejected(self):
        for key in ["pergunta","formato_entrega","refuta_se"]:
            p=sample("pauta.json");p.pop(key)
            self.assertRaises(core.TeamError,agenda.validate,p)

    def test_authorship_preference_consensus_and_vote_rejected(self):
        for value in ["a sua versão é esta","o usuário propôs esta solução","minha preferência é esta","buscar consenso","votação das opções"]:
            p=sample("pauta.json");p["versao_base"]=value
            self.assertRaises(core.TeamError,agenda.validate,p)
        p=sample("pauta.json");p["marcadores"]=["CASO-RESERVADO"];p["validacao_depois"]="Conferir CASO-RESERVADO"
        self.assertRaises(core.TeamError,agenda.validate,p)

    def test_light_is_not_a_fake_meeting_and_no_extra_round(self):
        p=sample("pauta.json");p["dose"]="leve"
        self.assertRaises(core.TeamError,agenda.validate,p)
        p=sample("pauta.json");p["rodadas"]=3
        self.assertRaises(core.TeamError,agenda.validate,p)

    def test_central_complete_requires_parallel_plan(self):
        p=sample("pauta.json");p.update(dose="completa",central=True,rodadas=3)
        self.assertRaises(core.TeamError,agenda.validate,p)
        p["paralelas"]=2;self.assertEqual(agenda.validate(p),p)


class MeetingTest(unittest.TestCase):
    def setUp(self):self.packet=sample("inicio.json");self.state=desk.start(self.packet)

    def test_seeds_repeat_order_and_preparations_are_private(self):
        self.assertEqual(self.state["ordens"],desk.start(self.packet)["ordens"])
        first=desk.record(self.state,event_for(self.state))
        task=desk.tasks(first)["tarefas"][0]["mensagem"]
        self.assertNotIn('"tipo": "preparacao"',task)
        self.assertNotIn("modelo-a-configurar",task)
        self.assertFalse(desk.tasks(first)["executavel"])

    def test_no_opening_before_preparations_and_out_of_order_rejected(self):
        event={"id":"bad","tipo":"abertura","ator":"LD","rodada":None,"texto":"mapa"}
        self.assertRaises(core.TeamError,desk.record,self.state,event)
        s=advance(self.state,"fala");event=event_for(s);event["ator"]="CR"
        self.assertRaises(core.TeamError,desk.record,s,event)

    def test_opening_must_map_every_contribution_without_preference(self):
        s=advance(self.state,"abertura");e=event_for(s);e["mapa"].pop()
        self.assertRaises(core.TeamError,desk.record,s,e)
        e=event_for(s);e["texto"]="Minha proposta é a melhor."
        self.assertRaises(core.TeamError,desk.record,s,e)

    def test_opening_and_full_preparations_reach_first_speaker(self):
        s=advance(self.state,"fala");message=desk.tasks(s)["tarefas"][0]["mensagem"]
        for event in s["eventos"]:
            if event["tipo"]=="preparacao":self.assertIn(event["contribuicoes"][0]["texto"],message)

    def test_resume_sends_delta_while_stateless_restores_full_context(self):
        s=advance(self.state,"fala")
        first=event_for(s);actor=first["ator"];s=desk.record(s,first)
        while not (desk.next_step(s)["tipo"]=="fala" and desk.next_step(s)["rodada"]==2 and desk.next_step(s)["atores"]==[actor]):s=desk.record(s,event_for(s))
        resumed=desk.tasks(s)["tarefas"][0]["mensagem"]
        restored=desk.tasks(s,"sem_estado")["tarefas"][0]["mensagem"]
        self.assertNotIn('"id": "'+first["id"]+'"',resumed)
        self.assertIn('"id": "'+first["id"]+'"',restored)
        self.assertIn("<especialidade",restored)

    def test_first_round_requires_facts_and_reason_against(self):
        s=advance(self.state,"fala");e=event_for(s);e["passo"]=True
        self.assertRaises(core.TeamError,desk.record,s,e)
        e=event_for(s);e["fatos_novos"]=[]
        self.assertRaises(core.TeamError,desk.record,s,e)

    def test_counterproof_required_for_verified_domain_contribution(self):
        s=advance(self.state,"fala");e=event_for(s)
        e["contraria"]=[{"contribuicao":"M1-1"}]
        self.assertRaises(core.TeamError,desk.record,s,e)
        e["contraria"][0]["contraprova"]={"tipo":"contraexemplo","texto":"um caso discriminante documentado"}
        self.assertEqual(desk.next_step(desk.record(s,e))["tipo"],"fala")

    def test_change_of_position_needs_previous_other_speech(self):
        s=advance(self.state,"fala");e=event_for(s);e.update(mudou=True,porque="a outra fala convenceu",cita_fala="inexistente")
        self.assertRaises(core.TeamError,desk.record,s,e)

    def test_speech_cannot_overwrite_original_contribution(self):
        s=advance(self.state,"fala");e=event_for(s)
        e["contribuicoes"]=[{"id":"M1-1","texto":"substituição indevida"}]
        self.assertRaises(core.TeamError,desk.record,s,e)
        self.assertNotEqual(core.contributions(s)["M1-1"]["texto"],"substituição indevida")

    def test_later_nonpass_speech_needs_declared_new_information(self):
        s=advance(self.state,"fala")
        while desk.next_step(s)["rodada"]!=2:s=desk.record(s,event_for(s))
        e=event_for(s);e.update(passo=False,motivo="Uma informação nova",posicao="Manter conferência",fatos_novos=[])
        e["texto"]+=" Uma informação nova Manter conferência"
        self.assertRaises(core.TeamError,desk.record,s,e)
        e["fatos_novos"]=["Foi relatada outra condição"]
        e["texto"]+=" Foi relatada outra condição"
        self.assertEqual(desk.next_step(desk.record(s,e))["tipo"],"fala")

    def test_critic_can_have_no_objections_but_must_say_what_checked(self):
        s=advance(self.state,"critica");e=event_for(s);e["conferido"]=[]
        self.assertRaises(core.TeamError,desk.record,s,e)
        self.assertEqual(desk.next_step(desk.record(s,event_for(s)))["tipo"],"fechamento")

    def test_agreement_does_not_close_standard_in_round_one(self):
        s=advance(self.state,"fechamento");e=event_for(s);e["parar"]=True
        self.assertRaises(core.TeamError,desk.record,s,e)

    def test_final_positions_stay_private_until_all_return(self):
        s=advance(self.state,"posicao");first=event_for(s);s=desk.record(s,first)
        message=desk.tasks(s)["tarefas"][0]["mensagem"]
        self.assertNotIn('"id": "'+first["id"]+'"',message)

    def test_missing_change_reason_is_marked_not_faked_as_convinced(self):
        s=advance(self.state,"posicao");e=event_for(s);e["apoio"]="Nova posição";e["texto"]+=" Nova posição"
        s=desk.record(s,e)
        self.assertTrue(s["eventos"][-1]["checagem"]["mudanca_sem_motivo"])

    def test_duplicate_event_stale_revision_and_manual_state_edit_fail(self):
        e=event_for(self.state);s=desk.record(self.state,e)
        self.assertRaises(core.TeamError,desk.record,s,e)
        self.assertRaises(core.TeamError,desk.record,s,event_for(s),0)
        s["revisao"]+=1;self.assertRaises(core.TeamError,desk.tasks,s)

    def test_timeout_retries_once_and_requires_two_preparations(self):
        s=desk.timeout(desk.timeout(self.state,"M1"),"M1")
        self.assertIn("M1",s["faltantes"])
        s=desk.record(s,event_for(s));s=desk.record(s,event_for(s))
        self.assertEqual(desk.next_step(s)["tipo"],"abertura")
        s=desk.timeout(desk.timeout(self.state,"M1"),"M1")
        s=desk.timeout(desk.timeout(s,"M2"),"M2");s=desk.record(s,event_for(s))
        self.assertEqual(desk.next_step(s)["tipo"],"formacao_insuficiente")

    def test_leak_suspends_quarantines_and_repeats_round_with_new_session(self):
        self.packet["pauta"]["marcadores"]=["SEGREDO-RESERVADO"]
        s=advance(desk.start(self.packet),"fala");s=desk.record(s,event_for(s))
        bad=event_for(s);actor=bad["ator"];bad["texto"]+=" SEGREDO-RESERVADO"
        paused=desk.record(s,bad)
        self.assertTrue(paused["suspensa"])
        self.assertFalse(any(e["id"]==bad["id"] for e in paused["eventos"]))
        self.assertRaises(core.TeamError,desk.repair,paused,"LD","nova","auditada")
        repaired=desk.repair(paused,actor,"sessao-nova","eventos auditados")
        self.assertEqual(desk.next_step(repaired)["rodada"],1)
        self.assertFalse(any(e["tipo"]=="fala" for e in repaired["eventos"]))
        self.assertNotIn("SEGREDO-RESERVADO",desk.tasks(repaired)["tarefas"][0]["mensagem"])

    def test_model_hierarchy_and_producer_sessions_checked(self):
        self.packet["membros"][0]["modelo"]["nivel"]=2
        self.assertRaises(core.TeamError,desk.start,self.packet)
        p=sample("inicio.json");p["pauta"].update(modo="verificacao",dose="completa",rodadas=1,afirmacoes=[{"id":"A1","texto":"a medição limita a incerteza"}])
        p["membros"]=[m for m in p["membros"] if m["id"]!="M3"];p["sessoes_produtoras"]=["sessao-1"]
        self.assertRaises(core.TeamError,desk.start,p)

    def test_complete_meeting_exports_without_user_approval(self):
        final=advance(self.state);result=desk.export(final)
        self.assertIn("equipe/4.3-r1/sintese.md",result["arquivos"])
        self.assertFalse(result["aprovacao_usuario"])
        self.assertEqual([e["rodada"] for e in final["eventos"] if e["tipo"]=="critica"],[1,2])
        self.assertEqual([e["tipo"] for e in final["eventos"][-3:]],["saida","revisao","resposta"])
        self.assertRaises(core.TeamError,desk.record,final,{"id":"extra","tipo":"fala","ator":"M1","rodada":3,"texto":"mais uma"})

    def test_individual_has_critique_response_without_fake_team_rounds(self):
        p=sample("inicio.json");p["pauta"].update(modo="individual",rodadas=2)
        p["membros"]=[m for m in p["membros"] if m["id"] in {"M1","CR"}]
        final=advance(desk.start(p))
        self.assertEqual([e["tipo"] for e in final["eventos"]],["preparacao","critica_individual","checagem","replica_individual"])

    def test_invalid_metrics_rejected_before_event_is_accepted(self):
        for metrics in [[],{"tokens":True},{"segundos":-1},{"creditos":float("inf")}]:
            e=event_for(self.state);e["metricas"]=metrics
            self.assertRaises(core.TeamError,desk.record,self.state,e)
            self.assertEqual(self.state["eventos"],[])

    def test_verification_and_integration_complete_their_own_deliveries(self):
        for mode in ["verificacao","integracao"]:
            p=sample("inicio.json");p["pauta"].update(modo=mode,dose="completa",rodadas=1)
            if mode=="verificacao":
                p["pauta"]["afirmacoes"]=[{"id":"A1","texto":"Uma afirmação a verificar"}]
                p["sessoes_produtoras"]=["sessao-produtora-externa"]
            else:p["pauta"]["saidas_aprovadas"]=[{"id":"S1","texto":"Saída rastreável","aprovada":True,"decisao":"registro-anterior"}]
            final=advance(desk.start(p));files=desk.export(final)["arquivos"]
            suffix="parecer" if mode=="verificacao" else "integracao"
            self.assertIn("equipe/4.3-r1/"+suffix+".md",files)

    def test_complete_can_stop_after_second_round_only_if_all_pass(self):
        p=sample("inicio.json");p["pauta"].update(dose="completa",rodadas=3)
        distant=copy.deepcopy(p["membros"][0]);distant.update(id="M4",nome="analogias",sigla="M4",sessao="sessao-distante",distante=True,funcao_analoga="transferir estados em outra área")
        p["membros"].insert(3,distant);s=desk.start(p)
        while not (desk.next_step(s)["tipo"]=="fechamento" and desk.next_step(s)["rodada"]==2):s=desk.record(s,event_for(s))
        e=event_for(s);e["parar"]=True;s=desk.record(s,e)
        final=advance(s)
        self.assertFalse(any(e["rodada"]==3 for e in final["eventos"]))
        self.assertEqual(desk.next_step(final)["tipo"],"concluida")


class OutputAndCheckTest(unittest.TestCase):
    def setUp(self):self.s=advance(desk.start(sample("inicio.json")),"saida")

    def test_lost_contribution_and_dissent_rejected(self):
        output=output_for(self.s);output["destinos"].pop()
        self.assertRaises(core.TeamError,synthesis.validate,output,self.s)
        output=output_for(self.s);output["dissenso"].pop()
        self.assertRaises(core.TeamError,synthesis.validate,output,self.s)

    def test_numeric_compromise_or_unverified_source_cannot_support_output(self):
        output=output_for(self.s);output.update(versao="Pausa de 3 minutos",numeros=[{"valor":3,"lastro":[],"motivo":"meio-termo","entre_posicoes":[2,4]}])
        self.assertRaises(core.TeamError,synthesis.validate,output,self.s)
        self.s["fontes"][0]["apoio_conferido"]=False
        self.assertRaises(core.TeamError,synthesis.validate,output_for(self.s),self.s)

    def test_leader_addition_must_be_marked_and_review_hash_current(self):
        output=output_for(self.s);output["do_lider"]=[{"texto":"novo conteúdo","marcado":False,"lastro":["F1"]}]
        self.assertRaises(core.TeamError,synthesis.validate,output,self.s)
        s=desk.record(self.s,event_for(self.s));review=event_for(s);review["hash_saida"]="antigo"
        self.assertRaises(core.TeamError,desk.record,s,review)

    def test_all_critic_points_require_reasoned_reply(self):
        s=desk.record(self.s,event_for(self.s));review=event_for(s);review["pontos"]=[{"id":"K1","texto":"preservar a minoria"}]
        s=desk.record(s,review);reply=event_for(s)
        self.assertRaises(core.TeamError,desk.record,s,reply)
        reply["respostas"]=[{"id":"K1","acao":"aceito","motivo":"argumento preservado na saída"}]
        self.assertEqual(desk.next_step(desk.record(s,reply))["tipo"],"concluida")

    def test_arithmetic_reproduces_and_forbidden_code_never_writes(self):
        result=minutes.calculations(sample("contas.json"));self.assertTrue(result["resultados"][0]["confere"])
        self.assertEqual(result["resultados"][0]["resultado"],299)
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/"nao-criar"
            code=f"open({str(target)!r}, 'w').write('x')\nprint(1)"
            result=minutes.calculations([{"id":"BAD","codigo":code,"resultado":1}])
            self.assertFalse(result["resultados"][0]["confere"]);self.assertFalse(target.exists())
        self.assertFalse(minutes.calculations([{"id":"C","codigo":"print(2+2)","resultado":5}])["resultados"][0]["confere"])

    def test_absent_research_never_becomes_verified(self):
        result=minutes.sources([{"id":"N1","texto":"alegação para conferir"}])
        self.assertFalse(result["executadas"]);self.assertFalse(result["resultados"][0]["confere"])

    def test_technical_report_has_all_claims_and_no_verdict(self):
        self.s["pauta"].update(modo="verificacao",afirmacoes=[{"id":"A1","texto":"uma afirmação técnica"}])
        value=output_for(self.s);self.assertTrue(report.validate(value,self.s)["valida"])
        value["afirmacoes"][0]["justificativa"]="Recomendo aprovar a hipótese."
        self.assertRaises(core.TeamError,report.validate,value,self.s)

    def test_integration_cannot_decide_the_conflict(self):
        self.s["pauta"].update(modo="integracao",saidas_aprovadas=[{"id":"S1"},{"id":"S2"}])
        value=output_for(self.s);value["conflitos"]=[{"id":"I1","saidas":["S1","S2"],"texto":"dependência incompatível","lastro":["F1"],"gravidade":"bloqueia","resolveria":"nova evidência","decisao":"adotar S1"}]
        self.assertRaises(core.TeamError,report.validate,value,self.s)
        value["conflitos"][0].pop("decisao");self.assertTrue(report.validate(value,self.s)["valida"])

    def test_unknown_costs_stay_unknown_and_partial_is_visible(self):
        self.s["eventos"][0]["metricas"]={"tokens":10}
        result=costs.summarize(self.s);self.assertIsNone(result["tokens"]["total"])
        self.assertEqual(result["tokens"]["conhecido"],10)
        self.assertIsNone(result["creditos"]["total"])


class FusionAndPortableTest(unittest.TestCase):
    def packet(self):
        p=sample("pauta.json");p.update(modo="fusao",rodadas=1)
        return {"pauta":p,"sessao_lider":"lider-novo","sessoes_lideres":["lider-antigo"],"semente":4,
                "sinteses":[{"id":"reuniao-1","modelo":"PRIVADO","ata":"PRIVADA","partes":[{"id":"p1","texto":"Manter opção curta"}],"dissenso":[{"id":"D1","argumento":"critério depende do caso"}]},
                            {"id":"reuniao-2","partes":[{"id":"p1","texto":"Manter opção longa"}],"dissenso":[]}]}

    def merged(self,public):
        parts=[]
        for label,s in public["sinteses"].items():
            for p in s["partes"]:parts.append({"id":"parte-"+label,"texto":p["texto"],"origens":[{"sintese":label,"parte":p["id"],"trecho":p["texto"]}]})
        output={"partes":parts,"fora":[],"dissenso":[{"sintese":l,**d} for l,s in public["sinteses"].items() for d in s["dissenso"]],"conflitos":[]}
        output["revisao"]={"conferido":["origens e dissenso"],"pontos":[],"hash_saida":core.digest(output)}
        output["respostas_critico"]=[];return output

    def test_fusion_hides_identity_and_needs_fresh_leader(self):
        p=self.packet();p["sinteses"][0]["partes"][0]["modelo"]="PRIVADO"
        p["sinteses"][0]["dissenso"][0]["autor"]="PRIVADO"
        result=fusion.prepare(p)
        self.assertNotIn("PRIVADO",json.dumps(result["brief"]))
        self.assertNotIn("reuniao-1",json.dumps(result["brief"]))
        p["sessao_lider"]="lider-antigo";self.assertRaises(core.TeamError,fusion.prepare,p)

    def test_fusion_blocks_reserved_markers_in_dissent(self):
        p=self.packet();p["pauta"]["marcadores"]=["CASO-RESERVADO"]
        p["sinteses"][0]["dissenso"][0]["argumento"]="Veja CASO-RESERVADO"
        self.assertRaises(core.TeamError,fusion.prepare,p)

    def test_fusion_rejects_lost_part_dissent_or_invented_origin(self):
        public=fusion.prepare(self.packet())["brief"];value=self.merged(public)
        self.assertTrue(fusion.validate(value,public)["valida"])
        for mutation in ["parte","dissenso","origem"]:
            v=copy.deepcopy(value)
            if mutation=="parte":v["partes"].pop()
            elif mutation=="dissenso":v["dissenso"]=[]
            else:v["partes"][0]["origens"][0]["trecho"]="inventado"
            self.assertRaises(core.TeamError,fusion.validate,v,public)

    def test_extracted_package_runs_entire_meeting_via_cli(self):
        final=advance(desk.start(sample("inicio.json")))
        events=[{k:v for k,v in e.items() if k!="checagem"} for e in final["eventos"]]
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);archive=root/"equipe.skill"
            r=subprocess.run([sys.executable,"-B",str(ROOT/"scripts/empacotar_skill.py"),"--skill",str(SKILL),"--destino",str(archive)],capture_output=True,text=True)
            self.assertEqual(r.returncode,0,r.stderr)
            with zipfile.ZipFile(archive) as z:z.extractall(root)
            code=root/"equipe-especialistas/scripts/mesa.py"
            def run(*args):
                result=subprocess.run([sys.executable,"-B",str(code),*map(str,args)],cwd=root,capture_output=True,text=True)
                self.assertEqual(result.returncode,0,result.stderr);return json.loads(result.stdout)
            state=run("iniciar",root/"equipe-especialistas/assets/modelos/inicio.json")
            for e in events:
                sp=root/"estado.json";ep=root/"evento.json";sp.write_text(core.dump(state));ep.write_text(core.dump(e))
                state=run("registrar",sp,"--evento",ep,"--revisao",str(state["revisao"]))
            sp.write_text(core.dump(state));self.assertIn("arquivos",run("entregar",sp))


if __name__=="__main__":unittest.main()
