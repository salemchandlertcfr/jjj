"""Configuração operacional sem alterar progresso nem armazenar credenciais."""
from __future__ import annotations

import copy
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


SCRIPTS = Path(__file__).resolve().parents[1] / "skills/etapa-1-cir/scripts"
sys.path.insert(0, str(SCRIPTS))


class ConfiguracaoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.core = importlib.import_module("_core")

    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix="cir-config-test-")
        self.addCleanup(self.directory.cleanup)
        self.base = Path(self.directory.name)
        self.root = self.base / "dossie"
        identity = mock.patch.dict(os.environ, {
            "GIT_AUTHOR_NAME": "CIR Config Test", "GIT_AUTHOR_EMAIL": "cir-config@example.invalid",
            "GIT_COMMITTER_NAME": "CIR Config Test", "GIT_COMMITTER_EMAIL": "cir-config@example.invalid",
            "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull,
        })
        identity.start()
        self.addCleanup(identity.stop)
        self.session = "config-session"
        self.cli("dossie_init.py", self.root, "--projeto", "Configuração", "--session", self.session)

    def cli(self, script, *args, success=True):
        result = subprocess.run([sys.executable, "-B", str(SCRIPTS / script), *map(str, args)],
                                text=True, capture_output=True, timeout=20)
        if success:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def command(self, name, *args, **kwargs):
        return self.cli("estado.py", name, self.root, "--session", self.session, *args, **kwargs)

    def state(self):
        return self.core.load_state(self.root)

    def config_file(self, value):
        path = self.base / "config.json"
        path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")
        return path

    def test_dose_records_plan_and_usage_without_advancing(self):
        before = self.state()
        self.command("dose", "--planejada", "padrao", "--motivo", "Incerteza inicial.")
        dose = self.state()["doses"]["0.1"]
        self.assertEqual(dose["planejada"], "padrao")
        self.assertIsNone(dose["usada"])
        self.command("dose", "--planejada", "padrao", "--usada", "completa", "--motivo", "Divergência exige aprofundar.")
        state = self.state()
        self.assertEqual(state["doses"]["0.1"]["usada"], "completa")
        self.assertEqual(len(state["doses"]["0.1"]["historico"]), 2)
        self.assertEqual((state["tema"], state["subetapa"], state["passo"]),
                         (before["tema"], before["subetapa"], before["passo"]))

    def test_dose_rejects_blank_reason_and_invalid_option_without_writing(self):
        original = (self.root / "estado.json").read_bytes()
        for args in [("--planejada", "leve", "--motivo", " "),
                     ("--planejada", "urgente", "--motivo", "Motivo")]:
            self.command("dose", *args, success=False)
            self.assertEqual((self.root / "estado.json").read_bytes(), original)

    def test_configuration_is_descriptive_and_preserves_progress(self):
        before = self.state()
        model_map = {"condutora": {"modelo": "Claude escolhido no ambiente", "via": "sessão local"},
                     "outras_familias": []}
        restrictions = {"material_sigiloso": "Não enviar dados pessoais", "destinos_proibidos": ["página pública"]}
        path = self.config_file({"mapa_de_modelos": model_map, "restricoes": restrictions,
                                 "ambiente": "notion", "modo": "auditoria"})
        self.command("configurar", "--entrada", path)
        state = self.state()
        self.assertEqual(state["mapa_de_modelos"], model_map)
        self.assertEqual(state["restricoes"], restrictions)
        self.assertEqual(state["ambiente"], "notion")
        self.assertEqual(state["modo"], "auditoria")
        for field in ("tema", "subetapa", "passo", "travas", "historico_ciclo"):
            self.assertEqual(state[field], before[field])

    def test_configuration_rejects_progress_fields_without_partial_update(self):
        original = (self.root / "estado.json").read_bytes()
        for value in ({"ambiente": "notion", "passo": 7}, {"travas": {"1": {"estado": "aprovado"}}},
                      {"proposito": {"texto": "novo"}}, {}):
            self.command("configurar", "--entrada", self.config_file(value), success=False)
            self.assertEqual((self.root / "estado.json").read_bytes(), original)

    def test_configuration_rejects_nested_credentials_and_nontext_values(self):
        original = (self.root / "estado.json").read_bytes()
        payloads = [
            {"mapa_de_modelos": {"condutora": {"api_key": "sentinela-privada"}}},
            {"mapa_de_modelos": {"condutora": {"modelo": "Bearer sentinela-privada"}}},
            {"mapa_de_modelos": {"condutora": {"via": "https://segredo@github.com/owner/repo"}}},
            {"restricoes": {"senha": "sentinela-privada"}},
            {"mapa_de_modelos": {"tokens": 1000}},
            {"restricoes": {"sigiloso": True}},
            {"mapa_de_modelos": []},
        ]
        for value in payloads:
            with self.subTest(value=value):
                result = self.command("configurar", "--entrada", self.config_file(value), success=False)
                self.assertNotIn("sentinela-privada", result.stdout + result.stderr)
                self.assertEqual((self.root / "estado.json").read_bytes(), original)

    def test_configuration_rejects_symlink_input(self):
        actual = self.config_file({"ambiente": "outro"})
        link = self.base / "config-link.json"
        link.symlink_to(actual)
        self.command("configurar", "--entrada", link, success=False)
        self.assertEqual(self.state()["ambiente"], "local")

    def test_round_stop_requires_both_conditions_and_keeps_history(self):
        self.command("rodada", "--familias-novas", "1", "--cir-mudou", "nao")
        self.assertFalse(self.state()["parada"]["0.1"]["parar"])
        self.command("rodada", "--familias-novas", "0", "--cir-mudou", "sim")
        self.assertFalse(self.state()["parada"]["0.1"]["parar"])
        self.command("rodada", "--familias-novas", "0", "--cir-mudou", "nao")
        state = self.state()
        self.assertTrue(state["parada"]["0.1"]["parar"])
        self.assertEqual(state["parada"]["0.1"]["rodadas"], 3)
        self.assertEqual(len(state["parada"]["0.1"]["historico"]), 3)
        self.assertEqual(state["passo"], 1)

    def test_round_rejects_negative_families_without_writing(self):
        original = (self.root / "estado.json").read_bytes()
        self.command("rodada", "--familias-novas", "-1", "--cir-mudou", "nao", success=False)
        self.assertEqual((self.root / "estado.json").read_bytes(), original)

    def test_all_new_mutations_require_own_session(self):
        path = self.config_file({"ambiente": "outro"})
        cases = [("dose", "--planejada", "leve", "--motivo", "Motivo"),
                 ("rodada", "--familias-novas", "0", "--cir-mudou", "nao"),
                 ("configurar", "--entrada", path)]
        original = (self.root / "estado.json").read_bytes()
        for name, *args in cases:
            self.cli("estado.py", name, self.root, "--session", "outra-sessao", *args, success=False)
            self.assertEqual((self.root / "estado.json").read_bytes(), original)

    def test_schema_checks_doses_and_round_types_on_state_load(self):
        cases = [
            {"doses": {"0.1": {"planejada": "leve", "usada": "inexistente", "motivo": "Motivo"}}},
            {"parada": {"0.1": {"rodadas": True, "familias_novas_na_ultima": 0}}},
            {"mapa_de_modelos": {"condutora": {"modelo": 42}}},
        ]
        for change in cases:
            candidate = copy.deepcopy(self.state())
            candidate.update(change)
            with self.assertRaises(self.core.CirError):
                self.core.validate_state(candidate)


if __name__ == "__main__":
    unittest.main()
