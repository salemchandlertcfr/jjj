"""Entrada e independência estrutural do conselho, sem chamar modelos."""
from __future__ import annotations

import copy
import importlib
import json
from pathlib import Path
import sys
import unittest


SCRIPTS = Path(__file__).resolve().parents[1] / "skills/conselho-especialistas/scripts"
sys.path.insert(0, str(SCRIPTS))
common = importlib.import_module("_comum")
brief_module = importlib.import_module("valida_brief")
anonymizer = importlib.import_module("anonimiza")
draw = importlib.import_module("sorteio")
panels = importlib.import_module("painel")
members = importlib.import_module("briefs_membros")


class ConselhoEntradaTest(unittest.TestCase):
    def brief(self, *, council="rapido", dose="padrao", template="evidencia", count=2):
        criteria = [{"id": "C1", "descricao": "A hipótese respeita o limite demonstrado.",
                     "refuta_se": "Existe contraexemplo documentado.", "decisivo": True}]
        frozen = brief_module.freeze_criteria(criteria, "REG-CRITERIOS-ANTES", em="2026-10-23T10:00:00Z")
        raw = [{"id": f"original-{n}", "texto": f"A capacidade {n} satisfaz a função declarada.",
                "origem": "versao-privada", "autoria": f"AUTORIA_PRIVADA_{n}"} for n in range(count)]
        anonymous = anonymizer.anonymize(raw, seed=17)
        return {"schema_version": 1, "id": "B-teste", "conselho": council, "template": template,
                "dose": dose, "pergunta": "Quais hipóteses resistem aos critérios?", "criterios": criteria,
                "criterios_fixados": frozen, "hipoteses": anonymous["hipoteses"],
                "fontes": [{"id": "F-1", "url": "https://example.org/fonte", "trecho": "Trecho usado apenas como fixture.",
                            "afirmacao": "Fixture de teste; não evidência real.", "verificada": True}],
                "parecer": None, "restricoes": {"nao_buscar_workspace": "Não consultar o projeto."}}

    def mapa(self):
        return {"familia": "anthropic", "modelo": "claude-juiz-ficticio-de-teste", "nivel": "juiz",
                "via": "duble-local", "autorizado": True}

    def panel(self, brief=None, **extra):
        brief = brief or self.brief()
        options = {"semente": 31, "sessoes_produtoras": ["sess-produtora"]}
        if brief["conselho"] == "rapido":
            options["oticas"] = ["refutador de método", "especialista do domínio"]
        options.update(extra)
        return panels.build_panel(brief, self.mapa(), **options)

    def test_criteria_are_bound_to_prior_record_and_tampering_is_rejected(self):
        brief = self.brief()
        before = copy.deepcopy(brief)
        validated = brief_module.validate_brief(brief)
        self.assertEqual(brief, before)
        self.assertEqual(validated["criterios_fixados"]["sha256"], common.canonical_hash(brief["criterios"]))
        brief["criterios"][0]["refuta_se"] = "Critério sob medida depois."
        with self.assertRaises(common.CouncilError):
            brief_module.validate_brief(brief)

    def test_missing_criteria_refutation_or_prior_declaration_is_rejected(self):
        for mutation in (lambda b: b.update(criterios=[]),
                         lambda b: b["criterios"][0].update(refuta_se=" "),
                         lambda b: b["criterios_fixados"].update(antes_das_hipoteses=False),
                         lambda b: b["criterios_fixados"].update(em="2026-10-23T10:00:00")):
            brief = self.brief()
            mutation(brief)
            with self.assertRaises(common.CouncilError):
                brief_module.validate_brief(brief)

    def test_names_normalize_accents_and_spacing_without_changing_criteria(self):
        brief = self.brief()
        brief.update(conselho="RÁPIDO", template=" Evidência ", dose="Padrão")
        result = brief_module.validate_brief(brief)
        self.assertEqual((result["conselho"], result["template"], result["dose"]), ("rapido", "evidencia", "padrao"))

    def test_structural_authorship_is_private_and_input_is_unchanged(self):
        raw = [{"id": "humano-A", "texto": "Minha versão: Reduzir esforço sem perder eficácia.", "origem": "usuario", "autoria": "AUTORIA_OCULTA"},
               {"id": "maquina-B", "texto": "Uma capacidade alternativa preserva o propósito.", "origem": "ia", "autoria": "OUTRA_AUTORIA"}]
        before = copy.deepcopy(raw)
        result = anonymizer.anonymize(raw, seed=1)
        self.assertEqual(raw, before)
        public = json.dumps(result["hipoteses"], ensure_ascii=False)
        for forbidden in ("AUTORIA_OCULTA", "OUTRA_AUTORIA", "humano-A", "maquina-B", "Minha versão"):
            self.assertNotIn(forbidden, public)
        self.assertEqual(set(result["chave_privada"]["hipoteses"]), {h["id"] for h in result["hipoteses"]})
        self.assertIn("Reduzir esforço sem perder eficácia.", [h["texto"] for h in result["hipoteses"]])

    def test_authorship_that_cannot_be_removed_faithfully_is_rejected(self):
        with self.assertRaises(common.CouncilError):
            anonymizer.anonymize([{"id": "orig", "texto": "Minha versão é melhor porque foi gerada por mim."}], seed=1)
        with self.assertRaises(common.CouncilError):
            anonymizer.anonymize([{"id": "orig", "texto": "A escolha de ANA_PRIVADA precisa vencer.", "autoria": "ANA_PRIVADA"}], seed=1)

    def test_public_brief_rejects_private_fields_and_authorship_markers(self):
        for edit in (lambda b: b.update(mapa_de_modelos=self.mapa()),
                     lambda b: b["hipoteses"][0].update(origem="usuario"),
                     lambda b: b["hipoteses"][0].update(texto="Esta é a versão da IA."),
                     lambda b: b["restricoes"].update(modelo="MODELO_PRIVADO")):
            brief = self.brief()
            edit(brief)
            with self.assertRaises(common.CouncilError):
                brief_module.validate_brief(brief)

    def test_unverified_source_and_credential_url_are_rejected(self):
        for edit in (lambda f: f.update(verificada=False), lambda f: f.update(url="https://senha@example.org")):
            brief = self.brief()
            edit(brief["fontes"][0])
            with self.assertRaises(common.CouncilError):
                brief_module.validate_brief(brief)

    def test_seed_is_reproducible_and_boolean_is_not_seed(self):
        hypotheses = [{"id": f"H{n}", "texto": str(n)} for n in range(6)]
        expected = draw.assign_hypotheses(hypotheses, ["M1", "M2"], seed=4)
        self.assertEqual(expected, draw.assign_hypotheses(hypotheses, ["M1", "M2"], seed=4))
        self.assertNotEqual(expected, draw.assign_hypotheses(hypotheses, ["M1", "M2"], seed=5))
        with self.assertRaises(common.CouncilError):
            draw.assign_hypotheses(hypotheses, ["M1", "M2"], seed=True)

    def test_more_than_six_has_full_coverage_overlap_and_six_per_member(self):
        hypotheses = [f"H{n}" for n in range(11)]
        assignments = draw.assign_hypotheses(hypotheses, ["M1", "M2"], seed=7)
        self.assertEqual(set().union(*(set(v) for v in assignments.values())), set(hypotheses))
        self.assertTrue(set.intersection(*(set(v) for v in assignments.values())))
        self.assertTrue(all(len(v) == 6 for v in assignments.values()))
        with self.assertRaises(common.CouncilError):
            draw.assign_hypotheses([f"H{n}" for n in range(12)], ["M1", "M2"], seed=7)

    def test_panel_uses_distinct_nonproducer_sessions_and_same_authorized_judge(self):
        brief = self.brief()
        panel = self.panel(brief, sessoes={"membros": ["sess-a", "sess-b"], "critico": "sess-c"})
        self.assertTrue(panel["so_claude"])
        self.assertTrue(all(m["modelo"] == self.mapa()["modelo"] for m in panel["membros"]))
        self.assertEqual(panel["critico"]["modelo"], self.mapa()["modelo"])
        for invalid in ({"membros": ["sess-a", "sess-a"], "critico": "sess-c"},
                        {"membros": ["sess-a", "sess-b"], "critico": "sess-a"},
                        {"membros": ["sess-produtora", "sess-b"], "critico": "sess-c"}):
            with self.assertRaises(common.CouncilError):
                self.panel(brief, sessoes=invalid)

    def test_panel_requires_explicit_producer_declaration_and_real_judge_level(self):
        brief = self.brief()
        with self.assertRaises(common.CouncilError):
            panels.build_panel(brief, self.mapa(), oticas=["refutador", "guardião"])
        for edit in (lambda m: m.update(familia="openai"), lambda m: m.update(modelo="Claude Haiku escolhido"),
                     lambda m: m.update(nivel="gerador"), lambda m: m.update(autorizado=False)):
            mapa = self.mapa()
            edit(mapa)
            with self.assertRaises(common.CouncilError):
                panels.build_panel(brief, mapa, oticas=["refutador", "guardião"], sessoes_produtoras=[])

    def test_duplicate_optics_are_not_independent_roles(self):
        with self.assertRaises(common.CouncilError):
            self.panel(oticas=["Guardião", "guardiao"])

    def test_complete_panel_has_nonvoting_critic_reporter_and_normalizer(self):
        brief = self.brief(council="completo", dose="completa")
        panel = self.panel(brief)
        self.assertEqual(len(panel["membros"]), 3)
        sessions = [m["sessao"] for m in panel["membros"]]
        sessions += [panel[r]["sessao"] for r in ("critico", "relator", "normalizador")]
        self.assertEqual(len(set(sessions)), 6)

    def test_complete_briefs_require_external_normalization_attestation(self):
        brief = self.brief(council="completo", dose="completa")
        panel = self.panel(brief)
        with self.assertRaises(common.CouncilError):
            members.build_member_briefs(brief, panel)
        note = {"confirmada": True, "fidelidade_confirmada": True, "sessao": panel["normalizador"]["sessao"],
                "referencia": "N-QA-1", "hipoteses_sha256": common.canonical_hash(brief["hipoteses"])}
        prepared = members.build_member_briefs(brief, panel, normalizacao=note)
        self.assertEqual(len(prepared), 3)
        note["hipoteses_sha256"] = "0" * 64
        with self.assertRaises(common.CouncilError):
            members.build_member_briefs(brief, panel, normalizacao=note)

    def test_member_briefs_hide_private_model_seed_sessions_and_origins(self):
        brief = self.brief()
        panel = self.panel(brief, sessoes={"membros": ["SESSION_PRIVATE_A", "SESSION_PRIVATE_B"], "critico": "SESSION_PRIVATE_C"})
        before = copy.deepcopy((brief, panel))
        prepared = members.build_member_briefs(brief, panel)
        self.assertEqual((brief, panel), before)
        serialized = json.dumps(prepared, ensure_ascii=False)
        for hidden in (self.mapa()["modelo"], "SESSION_PRIVATE", "AUTORIA_PRIVADA", "id_original", "semente", "chave_privada", "origem"):
            self.assertNotIn(hidden, serialized)
        self.assertEqual(set(prepared[0]), {"schema_version", "conselho_id", "membro", "otica", "rodada", "pergunta", "criterios", "criterios_sha256", "hipoteses", "fontes", "parecer", "restricoes", "instrucoes", "entregar"})

    def test_modified_assignment_or_model_is_rejected_before_publication(self):
        brief = self.brief()
        for edit in (lambda p: p["membros"][0].update(modelo="outro-modelo"),
                     lambda p: p["membros"][0].update(hipoteses=["H-inexistente"])):
            panel = self.panel(brief)
            edit(panel)
            with self.assertRaises(common.CouncilError):
                members.build_member_briefs(brief, panel)


if __name__ == "__main__":
    unittest.main()
