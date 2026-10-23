"""Contratos de julgamento e dissenso; sem invocar modelos nem rede."""
from __future__ import annotations

import copy
import importlib
from pathlib import Path
import sys
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "skills/conselho-especialistas/scripts"
sys.path.insert(0, str(SCRIPTS))
from _comum import CouncilError, canonical_hash
from valida_veredito import validate_critique, validate_verdict
from divergencia import detect_divergences
from matriz import build_matrix, quick_synthesis
from sintese_check import check_synthesis


class ResultadosConselhoTest(unittest.TestCase):
    def setUp(self):
        self.brief = {"schema_version": 1, "id": "C-QA", "conselho": "rapido", "template": "evidencia", "dose": "padrao",
                      "pergunta": "As duas hipóteses resistem?",
                      "criterios": [{"id": "C1", "descricao": "Coerência", "refuta_se": "Há contradição lógica", "decisivo": True},
                                    {"id": "C2", "descricao": "Robustez", "refuta_se": "Há caso adverso documentado", "decisivo": False}],
                      "hipoteses": [{"id": "H1", "texto": "Uma hipótese conceitual."}, {"id": "H2", "texto": "Outra hipótese conceitual."}],
                      "fontes": [{"id": "F1", "url": "https://example.org/paper", "trecho": "Trecho do estudo fictício de teste.",
                                  "afirmacao": "Premissa desta avaliação fictícia.", "verificada": True}]}
        self.panel = {"id": self.brief["id"],
                      "critico": {"rotulo": "critico-QA", "sessao": "s-critico", "fora_do_painel": True},
                      "sessoes_produtoras_excluidas": [], "membros": [
            {"rotulo": "M1", "otica": "refutador", "modelo": "juiz-test", "sessao": "s1", "hipoteses": ["H1", "H2"]},
            {"rotulo": "M2", "otica": "guardiao", "modelo": "juiz-test", "sessao": "s2", "hipoteses": ["H1", "H2"]}]}

    def member_brief(self, member="M1"):
        assignment = next(item for item in self.panel["membros"] if item["rotulo"] == member)
        return {"conselho_id": self.brief["id"], "membro": member, "criterios": copy.deepcopy(self.brief["criterios"]),
                "criterios_sha256": canonical_hash(self.brief["criterios"]),
                "hipoteses": [copy.deepcopy(h) for h in self.brief["hipoteses"] if h["id"] in assignment["hipoteses"]],
                "fontes": copy.deepcopy(self.brief["fontes"])}

    def verdict(self, member="M1", sign="+"):
        brief = self.member_brief(member)
        return {"schema_version": 1, "conselho_id": self.brief["id"], "membro": member, "rodada": 1,
                "criterios_sha256": canonical_hash(brief["criterios"]),
                "avaliacoes": [{"hipotese": h["id"], "criterio": c["id"], "sinal": sign,
                                "justificativa": f"Argumento verificável de {member} em {h['id']}/{c['id']}.",
                                "fontes": ["F1"] if sign in {"+", "-"} else [], "raciocinio": "",
                                "mudaria": "Um contraexemplo documentado.", "prob_resistir": None, "evidencias_novas": []}
                               for h in brief["hipoteses"] for c in brief["criterios"]],
                "falhas_fatais": [], "fontes_novas": []}

    def critique(self, findings=None):
        return {"schema_version": 1, "conselho_id": self.brief["id"], "aprovada": True,
                "revisor": "critico-QA", "achados": findings or [], "referencia": "Revisão de teste, sem serviço real."}

    def test_complete_coverage_and_inputs_are_not_mutated(self):
        verdict = self.verdict(); original = copy.deepcopy(verdict)
        result = validate_verdict(verdict, self.member_brief())
        self.assertEqual(result, verdict)
        result["avaliacoes"][0]["sinal"] = "?"
        self.assertEqual(verdict, original)

    def test_missing_or_duplicate_cells_are_rejected(self):
        for change in (lambda v: v["avaliacoes"].pop(), lambda v: v["avaliacoes"].append(copy.deepcopy(v["avaliacoes"][0]))):
            verdict = self.verdict(); change(verdict)
            with self.assertRaises(CouncilError): validate_verdict(verdict, self.member_brief())

    def test_criterion_hash_changes_are_rejected(self):
        verdict = self.verdict(); verdict["criterios_sha256"] = "0" * 64
        with self.assertRaises(CouncilError): validate_verdict(verdict, self.member_brief())

    def test_signs_need_presented_support_but_uncertainty_is_valid(self):
        verdict = self.verdict(); verdict["avaliacoes"][0]["fontes"] = []
        with self.assertRaises(CouncilError): validate_verdict(verdict, self.member_brief())
        verdict["avaliacoes"][0].update(sinal="?", justificativa="Evidência insuficiente para afirmar.")
        validate_verdict(verdict, self.member_brief())

    def test_unknown_source_and_private_addresses_are_rejected(self):
        verdict = self.verdict(); verdict["avaliacoes"][0]["fontes"] = ["F-SECRETO"]
        with self.assertRaises(CouncilError): validate_verdict(verdict, self.member_brief())
        for url in ("file:///segredo", "https://localhost/x", "http://10.1.2.3/x", "http://192.168.1.1/x", "http://169.254.169.254/x", "http://[fd00::1]/x", "https://private.notion.so/x"):
            with self.subTest(url=url):
                brief = self.member_brief(); brief["fontes"][0]["url"] = url
                with self.assertRaises(CouncilError): validate_verdict(self.verdict(), brief)

    def test_probability_boolean_nan_and_out_of_range_are_rejected(self):
        for probability in (True, float("nan"), float("inf"), -0.1, 1.1):
            verdict = self.verdict(); verdict["avaliacoes"][0]["prob_resistir"] = probability
            with self.assertRaises(CouncilError): validate_verdict(verdict, self.member_brief())

    def test_private_fields_and_markers_are_rejected(self):
        verdict = self.verdict(); verdict["modelo"] = "private-model"
        with self.assertRaises(CouncilError): validate_verdict(verdict, self.member_brief())
        verdict.pop("modelo"); verdict["avaliacoes"][0]["justificativa"] += " AUTORIA"
        with self.assertRaises(CouncilError): validate_verdict(verdict, self.member_brief(), marcadores_privados=["AUTORIA"])

    def test_second_round_requires_authorization_previous_and_new_evidence(self):
        previous = self.verdict(); current = copy.deepcopy(previous); current["rodada"] = 2
        current["avaliacoes"][0]["sinal"] = "-"
        with self.assertRaises(CouncilError): validate_verdict(current, self.member_brief(), anterior=previous)
        with self.assertRaises(CouncilError): validate_verdict(current, self.member_brief(), anterior=previous, troca_autorizada=True)
        current["avaliacoes"][0]["evidencias_novas"] = ["F1"]
        with self.assertRaises(CouncilError): validate_verdict(current, self.member_brief(), anterior=previous, troca_autorizada=True)
        current["fontes_novas"] = [{"id": "F2", "url": "https://example.org/new", "trecho": "Contraexemplo fictício.", "afirmacao": "Premissa antes desconhecida.", "verificada": True}]
        current["avaliacoes"][0]["evidencias_novas"] = ["F2"]
        current["avaliacoes"][0]["fontes"] = ["F2"]
        validate_verdict(current, self.member_brief(), anterior=previous, troca_autorizada=True)
        current["rodada"] = 3
        with self.assertRaises(CouncilError): validate_verdict(current, self.member_brief(), anterior=previous, troca_autorizada=True)

    def test_critic_is_external_and_leak_invalidates_member(self):
        verdicts = [self.verdict(), self.verdict("M2")]
        critique = self.critique(); critique["revisor"] = "M1"
        with self.assertRaises(CouncilError): validate_critique(critique, verdicts, self.brief["id"])
        finding = {"membro": "M1", "hipotese": "H1", "criterio": "C1", "tipo": "possivel_vazamento", "justificativa": "Citou material vedado.", "evidencias": ["auditoria"]}
        critique = self.critique([finding])
        with self.assertRaises(CouncilError): validate_verdict(verdicts[0], self.member_brief(), critica=critique)
        matrix = build_matrix(self.brief, self.panel, verdicts, critique)
        self.assertFalse(matrix["completo"])
        self.assertTrue(all(sign["membro"] != "M1" for cell in matrix["celulas"] for sign in cell["sinais"]))

    def test_relevant_divergence_and_dose_control_exchange(self):
        verdicts = [self.verdict(), self.verdict("M2", "-")]
        result = detect_divergences(self.brief, verdicts, self.critique())
        self.assertTrue(result["ha_divergencia"]); self.assertTrue(result["troca_permitida"])
        self.assertEqual(len(result["pontos"]), 2)  # Só C1 é decisivo.
        brief = copy.deepcopy(self.brief); brief["dose"] = "leve"
        self.assertFalse(detect_divergences(brief, verdicts, self.critique())["troca_permitida"])
        brief["conselho"] = "triagem"; brief["dose"] = "completa"
        self.assertFalse(detect_divergences(brief, verdicts, self.critique())["troca_permitida"])

    def test_majority_unknown_and_critic_support_trigger_divergence(self):
        unknown = [self.verdict(sign="?"), self.verdict("M2", "?")]
        self.assertEqual(len(detect_divergences(self.brief, unknown, self.critique())["pontos"]), 4)
        finding = {"membro": "M1", "hipotese": "H1", "criterio": "C1", "tipo": "lastro_insuficiente", "justificativa": "Fonte não sustenta.", "evidencias": ["F1"]}
        result = detect_divergences(self.brief, [self.verdict(), self.verdict("M2")], self.critique([finding]))
        self.assertTrue(result["ha_divergencia"])

    def test_solitary_fatal_needs_second_refuter_before_complete(self):
        one = self.verdict(); one["falhas_fatais"] = [{"hipotese": "H1", "criterio": "C1", "motivo": "Contradição lógica explícita.", "fontes": []}]
        critique = self.critique(); verdicts = [one, self.verdict("M2")]
        matrix = build_matrix(self.brief, self.panel, verdicts, critique)
        self.assertFalse(matrix["completo"])
        self.assertTrue(any(a["tipo"] == "segundo_refutador_pendente" for a in matrix["alertas"]))
        critique["confirmacoes_falha_fatal"] = [{"hipotese": "H1", "criterio": "C1", "sessao": "refutador-extra", "otica": "limites", "referencia": "Revisão extra documentada."}]
        self.assertTrue(build_matrix(self.brief, self.panel, verdicts, critique)["completo"])

    def test_matrix_preserves_signs_and_explicit_nonobservations(self):
        self.panel["membros"][1]["hipoteses"] = ["H1"]
        matrix = build_matrix(self.brief, self.panel, [self.verdict(), self.verdict("M2", "-")], self.critique())
        cell = next(c for c in matrix["celulas"] if c["hipotese"] == "H2" and c["criterio"] == "C1")
        self.assertEqual(cell["nao_observados"], [{"membro": "M2", "motivo": "nao_atribuida"}])
        self.assertNotIn("vencedor", matrix); self.assertNotIn("score", matrix)

    def test_missing_member_remains_partial_not_concordance(self):
        matrix = build_matrix(self.brief, self.panel, [self.verdict()], self.critique())
        self.assertFalse(matrix["completo"])
        self.assertTrue(all(c["nao_observados"] for c in matrix["celulas"]))

    def test_quick_synthesis_copies_all_arguments_and_checker_accepts_it(self):
        matrix = build_matrix(self.brief, self.panel, [self.verdict(), self.verdict("M2", "-")], self.critique())
        synthesis = quick_synthesis(matrix)
        self.assertEqual(synthesis["pontos"][0]["argumentos"][0]["justificativa"], matrix["celulas"][0]["sinais"][0]["justificativa"])
        self.assertTrue(check_synthesis(matrix, synthesis)["valida"])

    def test_synthesis_omitted_dissent_or_changed_sign_fails(self):
        matrix = build_matrix(self.brief, self.panel, [self.verdict(), self.verdict("M2", "-")], self.critique())
        synthesis = quick_synthesis(matrix); synthesis["tipo"] = "completa"
        synthesis["pontos"][0]["argumentos"].pop()
        self.assertFalse(check_synthesis(matrix, synthesis)["valida"])
        synthesis = quick_synthesis(matrix); synthesis["pontos"][0]["argumentos"][0]["sinal"] = "-"
        self.assertFalse(check_synthesis(matrix, synthesis)["valida"])

    def test_synthesis_recommendation_is_flagged_without_claiming_semantic_proof(self):
        matrix = build_matrix(self.brief, self.panel, [self.verdict(), self.verdict("M2")], self.critique())
        synthesis = quick_synthesis(matrix); synthesis["comentario"] = "Recomendo H1."
        report = check_synthesis(matrix, synthesis)
        self.assertFalse(report["valida"]); self.assertTrue(report["alertas_recomendacao"])
        self.assertIn("neutralidade semântica", report["limites"])


if __name__ == "__main__":
    unittest.main()
