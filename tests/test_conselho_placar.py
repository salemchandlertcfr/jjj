"""Previsão factual, decisão de valor e custos desconhecidos não se confundem."""
from __future__ import annotations

import copy
import importlib
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPTS = Path(__file__).resolve().parents[1] / "skills/conselho-especialistas/scripts"
sys.path.insert(0, str(SCRIPTS))


class PlacarTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = importlib.import_module("placar")
        cls.costs = importlib.import_module("custos")
        cls.error = importlib.import_module("_comum").CouncilError

    def setUp(self):
        self.matrix = {
            "schema_version": 1, "conselho_id": "C-QA",
            "criterios": [{"id": "C1", "refuta_se": "Um caso observado contradiz a hipótese."}],
            "hipoteses": [{"id": "H1", "texto": "Hipótese anonimizada"}],
            "celulas": [{"hipotese": "H1", "criterio": "C1", "nao_observados": [],
                         "sinais": [
                             {"membro": "M1", "sinal": "+", "prob_resistir": 0.8, "mudaria": "Um contraexemplo verificável."},
                             {"membro": "M2", "sinal": "-", "prob_resistir": 0.2, "mudaria": "Correção documentada do caso."},
                         ]}],
        }
        self.panel = {"id": "C-QA", "membros": [
            {"rotulo": "M1", "otica": "construtivo", "modelo": "MODELO_PRIVADO_QA", "esp": "esp-teste"},
            {"rotulo": "M2", "otica": "refutador", "modelo": "MODELO_PRIVADO_QA"},
        ]}
        self.key = {"hipoteses": {"H1": {"origem": "ORIGEM_PRIVADA_QA", "autor": "AUTOR_PRIVADO_QA"}}}
        self.decision = {"escolha": "H1", "motivo": "Aceito o risco por um valor.",
                         "objetivo": "Preservar o objetivo do projeto.", "referencia": "D-QA"}

    def entries(self, **kwargs):
        return self.ledger.ledger_entries(self.matrix, self.panel, **kwargs)

    def test_public_ledger_does_not_disclose_private_identity(self):
        output = json.dumps(self.entries(chave=self.key))
        for marker in ("MODELO_PRIVADO_QA", "ORIGEM_PRIVADA_QA", "AUTOR_PRIVADO_QA"):
            self.assertNotIn(marker, output)

    def test_human_choice_is_not_factual_outcome_or_disclosure_permission(self):
        entries = self.entries(decisao=self.decision, chave=self.key)
        self.assertTrue(all(row["desfecho"] is None for row in entries))
        self.assertTrue(all("modelo" not in row and "origem" not in row for row in entries))
        self.assertTrue(all(row["decisao_usuario"]["escolha"] == "H1" for row in entries))
        self.assertIsNone(self.ledger.brier_report(entries)["brier"])

    def test_identity_disclosure_requires_explicit_request_after_decision(self):
        decision = dict(self.decision, revelar_identidades=True)
        entries = self.entries(decisao=decision, chave=self.key)
        self.assertTrue(all(row["modelo"] == "MODELO_PRIVADO_QA" for row in entries))
        self.assertTrue(all(row["origem"] == "ORIGEM_PRIVADA_QA" for row in entries))
        self.assertNotIn("AUTOR_PRIVADO_QA", json.dumps(entries))

    def test_incomplete_decision_cannot_authorize_disclosure(self):
        for decision in ({"revelar_identidades": True}, dict(self.decision, motivo="")):
            with self.assertRaises(self.error):
                self.entries(decisao=decision, chave=self.key)

    def test_ids_are_stable_and_inputs_unchanged(self):
        before = copy.deepcopy((self.matrix, self.panel, self.key))
        first = self.entries(chave=self.key)
        second = self.entries(chave=self.key)
        self.assertEqual(first, second)
        self.assertEqual((self.matrix, self.panel, self.key), before)
        self.assertEqual(first[0]["evento_id"], first[1]["evento_id"])
        self.assertNotEqual(first[0]["id"], first[1]["id"])

    def test_probability_is_optional_and_unknown_is_not_zero(self):
        for signal in self.matrix["celulas"][0]["sinais"]:
            signal["prob_resistir"] = None
        report = self.ledger.brier_report(self.entries())
        self.assertIsNone(report["brier"])
        self.assertEqual(report["previsoes_observadas"], 0)
        self.assertEqual(report["excluidas"]["sem_probabilidade"], 2)

    def test_explicit_observation_computes_brier_with_correct_denominator(self):
        entries = self.entries()
        observed = self.ledger.record_outcome(entries, entries[0]["evento_id"], True, "F-QA-caso-observado")
        report = self.ledger.brier_report(observed)
        self.assertAlmostEqual(report["brier"], 0.34)
        self.assertEqual(report["previsoes_observadas"], 2)
        self.assertEqual(report["eventos_observados_distintos"], 1)
        self.assertIsNone(entries[0]["desfecho"])

    def test_choice_strings_and_numeric_flags_are_not_observations(self):
        entries = self.entries()
        for outcome in ("H1", "sim", 1, 0, None):
            with self.subTest(outcome=outcome), self.assertRaises(self.error):
                self.ledger.record_outcome(entries, entries[0]["evento_id"], outcome, "F-QA")

    def test_outcome_requires_reference_and_known_event(self):
        entries = self.entries()
        for event, reference in ((entries[0]["evento_id"], ""), ("E-inexistente", "F-QA")):
            with self.assertRaises(self.error):
                self.ledger.record_outcome(entries, event, True, reference)

    def test_outcome_is_idempotent_and_conflict_is_not_overwritten(self):
        entries = self.entries()
        observed = self.ledger.record_outcome(entries, entries[0]["evento_id"], False, "F-QA")
        self.assertEqual(observed, self.ledger.record_outcome(observed, entries[0]["evento_id"], False, "F-QA"))
        with self.assertRaises(self.error):
            self.ledger.record_outcome(observed, entries[0]["evento_id"], True, "F-QA-nova")

    def test_nan_infinity_bool_and_out_of_range_probabilities_are_rejected(self):
        for probability in (math.nan, math.inf, True, -0.1, 1.1, 10**400):
            self.matrix["celulas"][0]["sinais"][0]["prob_resistir"] = probability
            with self.subTest(probability=probability), self.assertRaises(self.error):
                self.entries()

    def test_duplicate_prediction_cannot_inflate_brier_count(self):
        entries = self.entries()
        with self.assertRaises(self.error):
            self.ledger.brier_report(entries + [copy.deepcopy(entries[0])])
        self.matrix["celulas"][0]["sinais"].append(copy.deepcopy(self.matrix["celulas"][0]["sinais"][0]))
        with self.assertRaises(self.error):
            self.entries()

    def test_panel_from_another_council_is_rejected(self):
        self.panel["id"] = "C-outro"
        with self.assertRaises(self.error):
            self.entries()

    def test_cli_can_emit_one_json_object_per_prediction(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "matrix.json"
            path.write_text(json.dumps(self.matrix), encoding="utf-8")
            result = subprocess.run([sys.executable, "-B", str(SCRIPTS / "placar.py"), "gerar",
                                     "--matriz", str(path), "--jsonl"], capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            rows = [json.loads(line) for line in result.stdout.splitlines()]
            self.assertEqual(len(rows), 2)
            self.assertNotIn("modelo", rows[0])

    def test_jsonl_round_trip_and_brier_cli_read_canonical_ledger(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "placar.jsonl"
            entries = self.entries()
            observed = self.ledger.record_outcome(entries, entries[0]["evento_id"], True, "F-QA")
            path.write_text(self.ledger.dump_jsonl(observed), encoding="utf-8")
            self.assertEqual(self.ledger.load_ledger(path), observed)
            result = subprocess.run([sys.executable, "-B", str(SCRIPTS / "placar.py"), "brier",
                                     "--placar", str(path)], capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertAlmostEqual(json.loads(result.stdout)["brier"], 0.34)

    def test_jsonl_rejects_symlinks_and_nonfinite_data(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "placar.jsonl"
            path.write_text(self.ledger.dump_jsonl(self.entries()), encoding="utf-8")
            linked = Path(tmp) / "alias.jsonl"
            linked.symlink_to(path)
            with self.assertRaises(self.error):
                self.ledger.load_ledger(linked)
            path.write_text('{"prob_resistir": NaN}\n', encoding="utf-8")
            with self.assertRaises(self.error):
                self.ledger.load_ledger(path)

    def test_all_unknown_costs_remain_unknown(self):
        report = self.costs.summarize_costs([{"membro": "M1", "status": "falhou"}])
        self.assertIsNone(report["tempo_s_conhecido"])
        self.assertIsNone(report["tokens_conhecidos"])
        self.assertEqual(report["custos_por_unidade"], {})
        self.assertEqual(report["desconhecidos"]["custo"], 1)

    def test_partial_costs_keep_units_and_missing_values_separate(self):
        records = [
            {"membro": "M1", "status": "ok", "tempo_s": 2, "tokens": 10, "tentativas": 1,
             "custo": {"valor": 0.3, "unidade": "USD"}},
            {"membro": "M2", "status": "timeout", "tempo_s": 4, "tokens": None, "tentativas": 2,
             "custo": {"valor": 20, "unidade": "creditos"}},
            {"membro": "M3", "status": "falhou", "tempo_s": None, "custo": None},
        ]
        report = self.costs.summarize_costs(records)
        self.assertEqual(report["custos_por_unidade"]["USD"]["valor_conhecido"], 0.3)
        self.assertEqual(report["custos_por_unidade"]["creditos"]["valor_conhecido"], 20)
        self.assertEqual(report["tempo_s_conhecido"], 6)
        self.assertEqual(report["tokens_conhecidos"], 10)
        self.assertEqual(report["desconhecidos"]["tokens"], 2)
        self.assertEqual(report["falhas"], 2)

    def test_known_zero_cost_is_kept_as_observed_zero(self):
        report = self.costs.summarize_costs([{"membro": "M1", "status": "ok", "tempo_s": 0,
            "tokens": 0, "tentativas": 1, "custo": {"valor": 0, "unidade": "USD"}}])
        self.assertEqual(report["tempo_s_conhecido"], 0)
        self.assertEqual(report["tokens_conhecidos"], 0)
        self.assertEqual(report["custos_por_unidade"]["USD"]["valor_conhecido"], 0)

    def test_invalid_cost_numbers_and_status_are_rejected(self):
        for record in (
            {"membro": "M1", "status": "ok", "tempo_s": -1},
            {"membro": "M1", "status": "ok", "tempo_s": math.nan},
            {"membro": "M1", "status": "ok", "tokens": True},
            {"membro": "M1", "status": "ok", "tokens": 1.5},
            {"membro": "M1", "status": "ok", "tentativas": 0},
            {"membro": "M1", "status": "inventado"},
            {"membro": "M1", "status": "ok", "custo": {"valor": 1, "unidade": ""}},
        ):
            with self.subTest(record=record), self.assertRaises(self.error):
                self.costs.summarize_costs([record])


if __name__ == "__main__":
    unittest.main()
