"""Contratos locais do grill; não avaliam verdade científica ou qualidade da entrevista."""
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

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/grill-embasado"
sys.path.insert(0, str(SKILL / "scripts"))
questions = importlib.import_module("perguntas")
responses = importlib.import_module("respostas")
understanding = importlib.import_module("entendimento")
core = importlib.import_module("grill_core")


def sample(name):
    return json.loads((SKILL / "modelos" / name).read_text())


class QuestionTest(unittest.TestCase):
    def setUp(self):
        self.p = sample("pergunta.json")

    def test_neutral_case_renders_base_and_motive(self):
        result = questions.validate(self.p)
        self.assertTrue(result["aprovada"], result)
        self.assertIn("Base: C1", result["mensagem"])
        self.assertIn("Por que importa", result["mensagem"])

    def test_missing_or_duplicate_base_rejected(self):
        self.p["perguntas"][0]["base"] = ["inexistente"]
        self.assertRaises(core.GrillError, questions.validate, self.p)
        self.p = sample("pergunta.json")
        self.p["bases"].append(copy.deepcopy(self.p["bases"][0]))
        self.assertRaises(core.GrillError, questions.validate, self.p)

    def test_leading_tag_and_recommendation_blocked(self):
        for text in ["Você não acha que isso funciona?", "Isso funciona, certo?",
                     "Recomendo automatizar, aceita a recomendação?", "Prefere painel ou tabela?"]:
            with self.subTest(text=text):
                self.p["perguntas"][0]["texto"] = text
                self.assertFalse(questions.validate(self.p)["aprovada"])

    def test_full_message_cannot_smuggle_praise(self):
        self.p["mensagem"] = "Excelente ideia!\n" + questions.validate(self.p)["mensagem"]
        self.assertRaises(core.GrillError, questions.validate, self.p)

    def test_motive_also_checked(self):
        self.p["perguntas"][0]["motivo"] = "Você tem razão; precisamos confirmar."
        self.assertFalse(questions.validate(self.p)["aprovada"])

    def test_numeric_anchor_in_question_or_base_blocked(self):
        q = self.p["perguntas"][0]
        q["texto"] = "Em 30% dos casos demora; com que frequência acontece com você?"
        self.assertIn("ancora-numerica", questions.validate(self.p)["erros"])
        q["texto"] = "Com que frequência acontece com você?"
        self.p["bases"][0]["texto"] = "Estimativa do setor: 30%."
        self.assertIn("ancora-numerica", questions.validate(self.p)["erros"])

    def test_double_question_suspicion_needs_justification(self):
        self.p["perguntas"][0]["texto"] = "O que fez primeiro e quando decidiu?"
        self.assertFalse(questions.validate(self.p)["aprovada"])
        self.p["justificativas"] = {"pergunta-dupla": "A data delimita o mesmo episódio; revisão manual registrada."}
        self.assertTrue(questions.validate(self.p)["aprovada"])

    def test_opening_solution_flagged(self):
        self.p["perguntas"][0]["texto"] = "Como usaria um dashboard?"
        self.assertIn("solucao-abertura", questions.validate(self.p)["pendentes"])

    def test_two_rejections_block_even_with_justification(self):
        self.p["perguntas"][0]["tentativas_reprovadas"] = 2
        self.assertIn("duas-reprovacoes", questions.validate(self.p)["erros"])

    def test_reflection_cannot_be_batched(self):
        other = copy.deepcopy(self.p["perguntas"][0]); other["id"] = "Q2"
        self.p["perguntas"].append(other)
        self.assertRaises(core.GrillError, questions.validate, self.p)

    def test_logistics_batch_is_numbered_and_independent(self):
        q = self.p["perguntas"][0]
        q.update(genero="logistica", texto="Qual horário está disponível?")
        for i in [2, 3]:
            node = copy.deepcopy(self.p["mapa"][0]); node["id"] = f"N{i}"
            self.p["mapa"].append(node)
            other = copy.deepcopy(q); other.update(id=f"Q{i}", no=f"N{i}")
            self.p["perguntas"].append(other)
        self.assertTrue(questions.validate(self.p)["aprovada"])
        self.assertIn("3. **Q3", questions.validate(self.p)["mensagem"])
        self.p["mapa"][1]["depende_de"] = ["N1"]
        self.assertRaises(core.GrillError, questions.validate, self.p)

    def test_world_fact_is_excluded_from_frontier(self):
        self.p["mapa"][0]["classe"] = "fato do mundo"
        self.assertEqual(questions.frontier(self.p["mapa"]), [])
        self.assertRaises(core.GrillError, questions.validate, self.p)

    def test_dependency_cycle_and_missing_node_rejected(self):
        self.p["mapa"][0]["depende_de"] = ["N1"]
        self.assertRaises(core.GrillError, questions.frontier, self.p["mapa"])
        self.p["mapa"][0]["depende_de"] = ["N2"]
        self.assertRaises(core.GrillError, questions.frontier, self.p["mapa"])

    def test_higher_value_question_takes_precedence(self):
        other = copy.deepcopy(self.p["mapa"][0]); other["id"] = "N2"
        self.p["mapa"].append(other)
        self.p["mapa"][0]["valor"] = "baixo"
        self.p["perguntas"][0]["valor"] = "baixo"
        self.assertRaises(core.GrillError, questions.validate, self.p)

    def test_repetition_requires_reference_and_reason(self):
        self.p["anteriores"] = [{"id": "Q0", "texto": self.p["perguntas"][0]["texto"]}]
        self.assertRaises(core.GrillError, questions.validate, self.p)
        self.p["perguntas"][0].update(retoma="Q0", motivo_retomada="O contexto mudou.")
        result = questions.validate(self.p)
        self.assertTrue(result["aprovada"])
        self.assertIn("Retoma: Q0", result["mensagem"])

    def source_packet(self):
        self.p["bases"] = [{"id": "F1", "tipo": "ficha", "origem": "F1/T1", "texto": "No experimento houve atraso."}]
        self.p["perguntas"][0].update(base=["F1"], texto="Um estudo, força 4, descreve atraso; o que muda na sua versão?")
        self.p["modo"] = "desafio"
        return {"F1": {"valida": True, "trecho": "No experimento houve atraso.", "forca": 4, "apoio": "conferido"}}

    def test_invalid_or_missing_source_blocked(self):
        src = self.source_packet()
        self.assertRaises(core.GrillError, questions.validate, self.p)
        src["F1"]["valida"] = False
        self.assertRaises(core.GrillError, questions.validate, self.p, src)

    def test_source_strength_and_unverified_support_are_visible(self):
        src = self.source_packet()
        self.assertTrue(questions.validate(self.p, src)["aprovada"])
        src["F1"]["apoio"] = "nao conferido"
        self.assertRaises(core.GrillError, questions.validate, self.p, src)
        self.p["perguntas"][0]["texto"] = "Um estudo, força 4, apoio não conferido, descreve atraso; o que muda na sua versão?"
        self.assertTrue(questions.validate(self.p, src)["aprovada"])

    def test_opening_rejects_source_not_general_overview(self):
        src = self.source_packet(); self.p["modo"] = "abertura"
        self.assertRaises(core.GrillError, questions.validate, self.p, src)
        src["F1"]["visao_geral"] = True
        self.assertTrue(questions.validate(self.p, src)["aprovada"])


class ResponseTest(unittest.TestCase):
    def setUp(self):
        self.r = sample("resposta.json")

    def test_preserves_unicode_spaces_and_newlines(self):
        self.r["texto"] = "  " + self.r["texto"] + "\n\nação\r\n"
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "respostas.jsonl"
            self.assertTrue(responses.register(p, self.r)["gravada"])
            self.assertEqual(responses.read_log(p)[0]["texto"], self.r["texto"])
            self.assertFalse(responses.register(p, self.r)["gravada"])
            self.assertEqual(len(responses.read_log(p)), 1)

    def test_conflicting_id_preserves_file(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "respostas.jsonl"
            responses.register(p, self.r); before = p.read_bytes()
            self.r["texto"] += " Mais."
            self.assertRaises(core.GrillError, responses.register, p, self.r)
            self.assertEqual(p.read_bytes(), before)

    def test_nonliteral_claim_rejected(self):
        self.r["afirmacoes"][0]["trecho"] = "Paráfrase inventada."
        self.assertRaises(core.GrillError, responses.validate_response, self.r)

    def test_only_world_facts_leave_for_research(self):
        exported = responses.export_facts([self.r], "padrao")
        self.assertEqual([x["id"] for x in exported["afirmacoes"]], ["A1"])
        self.assertNotIn("mensagem_id", json.dumps(exported))
        self.assertNotIn("não aceito", json.dumps(exported, ensure_ascii=False))
        self.assertNotIn("painel", json.dumps(exported))

    def test_light_dose_marks_noncentral_as_unverified(self):
        self.r["afirmacoes"][0]["central"] = False
        exported = responses.export_facts([self.r], "leve")
        self.assertEqual(exported["afirmacoes"], [])
        self.assertEqual(exported["nao_conferidas"][0]["situacao"], "nao conferida")

    def test_revision_keeps_history_but_exports_current(self):
        revised = copy.deepcopy(self.r)
        revised.update(id="R2", substitui="R1", usos_anteriores=["01-proposito.md"])
        for claim in revised["afirmacoes"]:
            claim["id"] += "-novo"
        records = responses.validate_log([self.r, revised])
        self.assertEqual(len(records), 2)
        self.assertEqual(responses.active(records), [revised])
        self.assertEqual(responses.export_facts(records, "padrao")["afirmacoes"][0]["id"], "A1-novo")

    def test_revision_cannot_target_missing_or_replaced_response(self):
        self.r.update(substitui="R-inexistente", usos_anteriores=[])
        self.assertRaises(core.GrillError, responses.validate_log, [self.r])

    def test_audit_matches_transcript_exactly(self):
        transcript = [{"id": "M1", "papel": "usuario", "texto": self.r["texto"]}]
        self.assertTrue(responses.audit([self.r], transcript)["fiel"])
        transcript[0]["texto"] += " "
        self.assertFalse(responses.audit([self.r], transcript)["fiel"])
        self.assertFalse(responses.audit([self.r], [])["fiel"])

    def test_timezone_and_known_classes_required(self):
        self.r["em"] = "2026-10-23T10:00:00"
        self.assertRaises(core.GrillError, responses.validate_response, self.r)
        self.r["em"] += "+00:00"
        self.r["afirmacoes"][0]["classe"] = "talvez"
        self.assertRaises(core.GrillError, responses.validate_response, self.r)

    def test_corrupted_partial_log_not_appended(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "respostas.jsonl"; p.write_text('{"id":')
            before = p.read_bytes()
            self.assertRaises(core.GrillError, responses.register, p, self.r)
            self.assertEqual(p.read_bytes(), before)

    def test_symlink_not_followed(self):
        with tempfile.TemporaryDirectory() as d:
            target = Path(d) / "real"; target.write_text("")
            link = Path(d) / "link"; link.symlink_to(target)
            self.assertRaises(core.GrillError, responses.register, link, self.r)
            self.assertEqual(target.read_text(), "")


class UnderstandingTest(unittest.TestCase):
    def setUp(self):
        self.r = sample("resposta.json")
        self.p = sample("entendimento.json")

    def test_literal_and_marked_reading_have_provenance(self):
        result = understanding.understanding(self.p, [self.r])
        self.assertIn("leitura da condutora", result["markdown"])
        self.assertIn("Q-1.3-01/R1", result["markdown"])
        self.assertEqual(result["confirmacao"], "pendente")

    def test_unmarked_paraphrase_and_invented_origin_rejected(self):
        self.p["itens"][0]["texto"] = "Relatórios pouco pontuais."
        self.assertRaises(core.GrillError, understanding.understanding, self.p, [self.r])
        self.p["itens"][0]["leitura"] = True
        self.p["itens"][0]["origens"][0]["id"] = "R-inventada"
        self.assertRaises(core.GrillError, understanding.understanding, self.p, [self.r])

    def test_hash_changes_after_user_correction(self):
        before = understanding.understanding(self.p, [self.r])["sha256"]
        self.p["itens"][2]["texto"] = "Não se conhece ainda a frequência."
        self.assertNotEqual(before, understanding.understanding(self.p, [self.r])["sha256"])

    def test_reader_does_not_get_extra_card_or_response_fields(self):
        card = sample("cartao.json"); card.update(autoria="SEGREDO", dossie="NÃO ENVIAR", conversa=[self.r])
        result = understanding.reader_brief(card, understanding.understanding(self.p, [self.r]), "leve")
        raw = json.dumps(result, ensure_ascii=False)
        self.assertNotIn("SEGREDO", raw)
        self.assertNotIn("NÃO ENVIAR", raw)
        self.assertNotIn("Pensei num painel", raw)
        self.assertEqual(result["restricoes"]["ferramentas"], [])

    def stop_packet(self):
        return {"dose": "padrao", "motivo": "sem valor", "mapa": [], "nao_perguntado": [],
                "entendimento_sha256": "HASH1", "sessao_condutora": "S1",
                "confirmacao": {"confirmado": True, "entendimento_sha256": "HASH1", "resposta_id": "R-confirmacao"},
                "leitor": {"concluido": True, "sessao": "S2", "modelo_verificado": True,
                           "entendimento_sha256": "HASH1", "perguntas": []}}

    def test_all_doses_require_reader_and_current_confirmation(self):
        for dose in ["leve", "padrao", "completa"]:
            with self.subTest(dose=dose):
                p = self.stop_packet(); p["dose"] = dose
                self.assertTrue(understanding.stop(p)["pronto"])
                p["leitor"]["entendimento_sha256"] = "HASH-ANTIGO"
                self.assertFalse(understanding.stop(p)["pronto"])

    def test_same_session_cannot_be_independent_reader(self):
        p = self.stop_packet(); p["leitor"]["sessao"] = "S1"
        self.assertFalse(understanding.stop(p)["pronto"])

    def test_chega_stops_without_fake_readiness(self):
        p = sample("parada.json")
        result = understanding.stop(p)
        self.assertTrue(result["parar_conversa"])
        self.assertFalse(result["pronto"])
        self.assertTrue(result["leitor_pendente"])

    def test_blocked_dependency_does_not_mean_done(self):
        p = self.stop_packet()
        a = sample("pergunta.json")["mapa"][0]
        b = copy.deepcopy(a); b.update(id="N2", depende_de=["N1"])
        a["classe"] = "fato do mundo"
        p["mapa"] = [a, b]
        p["nao_perguntado"] = [{"id": n["id"], "risco": "muda saída", "motivo": "aguarda pesquisa"} for n in p["mapa"]]
        self.assertFalse(understanding.stop(p)["pronto"])

    def test_reader_findings_return_to_conductor(self):
        p = self.stop_packet()
        p["leitor"]["perguntas"] = [{"classe": "decisao", "texto": "Qual decisão está em jogo?", "impacto": "muda o objetivo"}]
        self.assertFalse(understanding.stop(p)["pronto"])
        p["leitor"]["perguntas"][0]["classe"] = "fato do mundo"
        self.assertFalse(understanding.stop(p)["pronto"])
        p["pesquisa_encaminhada"] = True
        self.assertTrue(understanding.stop(p)["pronto"])

    def test_contradiction_keeps_evidence_and_escalates(self):
        p = sample("checagem.json")
        result = understanding.check_contradictions([self.r], p["conferencias"], p["eventos"], "padrao")
        self.assertEqual(result["dose_sugerida"], "completa")
        self.assertEqual(result["mostrar_uma_vez"], [])
        self.assertEqual(understanding.check_contradictions([self.r], [], [], "leve")["nao_conferidas"], ["A1"])

    def test_second_challenge_and_altered_evidence_rejected(self):
        p = sample("checagem.json")
        event = copy.deepcopy(p["eventos"][0]); event["id"] = "E2"
        self.assertRaises(core.GrillError, understanding.check_contradictions, [self.r], p["conferencias"], p["eventos"] + [event], "padrao")
        p["eventos"][0]["evidencias_mostradas"][0]["forca"] = 1
        self.assertRaises(core.GrillError, understanding.check_contradictions, [self.r], p["conferencias"], p["eventos"], "padrao")

    def test_values_cannot_be_checked_as_world_facts(self):
        p = sample("checagem.json"); p["conferencias"][0]["id"] = "A2"
        self.assertRaises(core.GrillError, understanding.check_contradictions, [self.r], p["conferencias"], [], "padrao")


class PortableWorkflowTest(unittest.TestCase):
    def test_package_extract_and_real_cli_workflow(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); archive = root / "grill.skill"
            result = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/empacotar_skill.py"),
                                     "--skill", str(SKILL), "--destino", str(archive)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            with zipfile.ZipFile(archive) as z:
                z.extractall(root)
            skill = root / "grill-embasado"
            def run(script, *args):
                return subprocess.run([sys.executable, "-B", str(skill / "scripts" / script), *map(str, args)],
                                      cwd=root, capture_output=True, text=True)
            q = run("perguntas.py", skill / "modelos/pergunta.json")
            self.assertEqual(q.returncode, 0, q.stderr)
            self.assertTrue(json.loads(q.stdout)["aprovada"])
            log = root / "respostas.jsonl"
            r = run("respostas.py", "--registrar", skill / "modelos/resposta.json", "--registro", log)
            self.assertEqual(r.returncode, 0, r.stderr)
            r = run("respostas.py", "--buscar", "relatórios", "--registro", log)
            self.assertEqual(len(json.loads(r.stdout)["respostas"]), 1)
            e = run("entendimento.py", skill / "modelos/entendimento.json", "--registro", log)
            self.assertEqual(e.returncode, 0, e.stderr)
            transcript = root / "transcricao.json"
            transcript.write_text(json.dumps([{"id": "M1", "papel": "usuario", "texto": "alterado"}]))
            a = run("respostas.py", "--auditar", transcript, "--registro", log)
            self.assertEqual(a.returncode, 1)
            self.assertFalse(json.loads(a.stdout)["fiel"])
