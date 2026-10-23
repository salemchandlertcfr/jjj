"""Fluxo local do conselho até a condutora; julgamentos são dublês declarados."""
from __future__ import annotations

import copy
import importlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


REPO = Path(__file__).resolve().parents[1]
COUNCIL = REPO / "skills/conselho-especialistas/scripts"
CONDUCTOR = REPO / "skills/etapa-1-cir/scripts"
FIXTURES = REPO / "evals/conselho-especialistas/fixtures"
sys.path.insert(0, str(CONDUCTOR))
sys.path.insert(0, str(COUNCIL))


class CouncilIntegrationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.protocol = importlib.import_module("conselho")
        cls.common = importlib.import_module("_comum")
        cls.verdicts_module = importlib.import_module("valida_veredito")
        cls.transport = importlib.import_module("paralelo_cli")
        cls.matrix_module = importlib.import_module("matriz")
        cls.registrar = importlib.import_module("registrar")
        cls.core = importlib.import_module("_core")
        cls.initializer = importlib.import_module("dossie_init")

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="conselho-integracao-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "dossie"
        self.session = "condutora-qa"
        identity = mock.patch.dict(os.environ, {
            "GIT_AUTHOR_NAME": "Council Test", "GIT_AUTHOR_EMAIL": "council-test@example.invalid",
            "GIT_COMMITTER_NAME": "Council Test", "GIT_COMMITTER_EMAIL": "council-test@example.invalid",
            "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull,
            "PYTHONDONTWRITEBYTECODE": "1",
        })
        identity.start()
        self.addCleanup(identity.stop)
        self.initializer.initialize(self.root, "Conselho controlado", session=self.session)

    def case(self, number=2):
        path = next(FIXTURES.glob(f"{number:02d}-*.json"))
        return json.loads(path.read_text(encoding="utf-8"))

    def prepare(self, number=2, *, changes=None):
        fixture = self.case(number)
        request = fixture["request"]
        if changes:
            request.update(changes)
        return self.protocol.prepare(request, fixture["modelo_de_juiz"], seed=48213,
                                     sessoes={"membros": ["sess-qa-a", "sess-qa-b"], "critico": "sess-qa-c"},
                                     sessoes_produtoras=["sess-qa-produtor"])

    def snapshot(self):
        return {str(p.relative_to(self.root)): p.read_bytes()
                for p in self.root.rglob("*") if p.is_file()
                and ".git" not in p.relative_to(self.root).parts}

    def git(self, *args):
        result = subprocess.run(["git", "-C", str(self.root), *map(str, args)],
                                text=True, capture_output=True, timeout=20)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.strip()

    def make_verdicts(self, packet, *, target=None, fatal=False):
        target = target or packet["brief"]["hipoteses"][0]["id"]
        result = []
        for index, brief in enumerate(packet["briefs_membros"]):
            assessments = []
            for hypothesis in brief["hipoteses"]:
                for criterion in brief["criterios"]:
                    sign = "-" if index == 0 and hypothesis["id"] == target else "+"
                    assessments.append({
                        "hipotese": hypothesis["id"], "criterio": criterion["id"], "sinal": sign,
                        "justificativa": f"Argumento literal da ótica {index}: o alcance da premissa deve ser respeitado.",
                        "fontes": ["F1"], "raciocinio": "A conclusão depende das condições descritas na ficha controlada.",
                        "mudaria": "Um contraexemplo documentado que altere a condição avaliada.",
                        "prob_resistir": 0.25 if sign == "-" else 0.75, "evidencias_novas": [],
                    })
            result.append({"schema_version": 1, "conselho_id": brief["conselho_id"],
                           "membro": brief["membro"], "rodada": 1,
                           "criterios_sha256": brief["criterios_sha256"],
                           "avaliacoes": assessments, "falhas_fatais": [], "fontes_novas": []})
        if fatal:
            result[0]["falhas_fatais"] = [{"hipotese": target,
                "criterio": packet["brief"]["criterios"][0]["id"],
                "motivo": "As entradas indistinguíveis não permitem certeza universal.",
                "fontes": ["F1"], "raciocinio": "Uma mesma entrada não distingue dois resultados incompatíveis."}]
        return result

    def critique(self, packet):
        return {"schema_version": 1, "conselho_id": packet["brief"]["id"], "aprovada": True,
                "revisor": packet["painel"]["critico"]["rotulo"], "achados": [],
                "referencia": "DUBLE-CRITICA-CONTROLADA-NAO-LLM"}

    def consolidate(self, packet, verdicts, critique=None, **options):
        return self.protocol.consolidate(packet["brief"], packet["painel"],
                    packet["briefs_membros"], verdicts, critique or self.critique(packet), **options)

    def test_prepare_is_pure_and_member_briefs_exclude_private_provenance(self):
        fixture = self.case()
        original = copy.deepcopy(fixture)
        before, head = self.snapshot(), self.git("rev-parse", "HEAD")
        packet = self.protocol.prepare(fixture["request"], fixture["modelo_de_juiz"], seed=48213,
                                      sessoes_produtoras=[])
        self.assertEqual(fixture, original)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.git("rev-parse", "HEAD"), head)
        public = json.dumps({"brief": packet["brief"], "members": packet["briefs_membros"]}, ensure_ascii=False)
        for hypothesis in fixture["request"]["hipoteses"]:
            self.assertNotIn(hypothesis["origem"], public)
            self.assertNotIn(hypothesis["id"], public)
        self.assertNotIn(fixture["modelo_de_juiz"]["modelo"], public)
        self.assertNotIn('"semente"', public)
        self.assertNotIn('"chave_privada"', public)

    def test_only_conductor_writes_public_packet_to_actual_dossier(self):
        before, head = self.snapshot(), self.git("rev-parse", "HEAD")
        packet = self.prepare()
        verdicts = self.make_verdicts(packet)
        result = self.consolidate(packet, verdicts)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.git("rev-parse", "HEAD"), head)
        for relative in result["arquivos"]:
            path = PurePosixPath(relative)
            self.assertFalse(path.is_absolute())
            self.assertNotIn("..", path.parts)
            self.assertEqual(path.parts[0], "conselho")
        public = "\n".join(result["arquivos"].values())
        for hypothesis in self.case()["request"]["hipoteses"]:
            self.assertNotIn(hypothesis["origem"], public)
        self.assertNotIn(packet["painel"]["modelo_de_juiz"], public)
        with self.assertRaises(self.core.CirError):
            self.registrar.registrar(self.root, "outra-sessao", {
                "tipo": "checkpoint", "escolha": "Receber conselho", "arquivos": result["arquivos"]})
        self.assertEqual(self.snapshot(), before)
        receipt = self.registrar.registrar(self.root, self.session, {
            "tipo": "checkpoint", "escolha": "Receber conselho sem decidir pelas hipóteses.",
            "arquivos": result["arquivos"]})
        self.assertNotEqual(receipt["commit"], head)
        for relative, text in result["arquivos"].items():
            self.assertEqual((self.root / relative).read_text(), text)
            self.assertEqual(self.git("show", "HEAD:" + relative), text.strip())
        self.assertEqual(self.core.load_state(self.root)["passo"], 1)

    def test_untrusted_packet_cannot_escape_dossier_when_conductor_registers(self):
        packet = self.prepare()
        result = self.consolidate(packet, self.make_verdicts(packet))
        result["arquivos"]["../autoria.json"] = "NAO-ESCREVER"
        before, head = self.snapshot(), self.git("rev-parse", "HEAD")
        with self.assertRaises(self.core.CirError):
            self.registrar.registrar(self.root, self.session, {
                "tipo": "checkpoint", "escolha": "Receber pacote", "arquivos": result["arquivos"]})
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.git("rev-parse", "HEAD"), head)
        self.assertFalse((self.base / "autoria.json").exists())

    def test_dissent_survives_without_aggregate_or_recommendation(self):
        packet = self.prepare()
        verdicts = self.make_verdicts(packet)
        result = self.consolidate(packet, verdicts)
        first = packet["brief"]["hipoteses"][0]["id"]
        cell = next(item for item in result["matriz"]["celulas"] if item["hipotese"] == first)
        self.assertEqual({item["sinal"] for item in cell["sinais"]}, {"+", "-"})
        summary = json.dumps(result["sintese"], ensure_ascii=False)
        for verdict in verdicts:
            for assessment in verdict["avaliacoes"]:
                self.assertIn(assessment["justificativa"], summary)
        for forbidden in ("vencedor", "ranking", "nota_geral", "recomendacao"):
            self.assertNotIn(forbidden, result["matriz"])

    def test_unknown_source_cannot_become_valid_evidence(self):
        packet = self.prepare()
        verdicts = self.make_verdicts(packet)
        verdicts[0]["avaliacoes"][0]["fontes"] = ["F-WORKSPACE-PRIVADA"]
        before = self.snapshot()
        with self.assertRaises(self.common.CouncilError):
            self.consolidate(packet, verdicts)
        self.assertEqual(self.snapshot(), before)

    def test_exchange_contains_only_divergent_cells_and_is_anonymous(self):
        packet = self.prepare(3)
        verdicts = self.make_verdicts(packet)
        exchanges = self.protocol.prepare_exchange(packet["brief"], packet["painel"],
                         packet["briefs_membros"], verdicts, self.critique(packet))
        first = packet["brief"]["hipoteses"][0]["id"]
        self.assertTrue(exchanges)
        for exchange in exchanges:
            self.assertEqual(exchange["rodada"], 2)
            self.assertTrue(exchange["argumentos_anonimos"])
            for argument in exchange["argumentos_anonimos"]:
                self.assertEqual(argument["hipotese"], first)
                self.assertNotIn("membro", argument)
                self.assertNotIn("modelo", argument)

    def test_change_without_new_evidence_is_rejected_and_inputs_preserved(self):
        packet = self.prepare(3)
        previous = self.make_verdicts(packet)
        current = copy.deepcopy(previous)
        for verdict in current:
            verdict["rodada"] = 2
        changed = next(item for item in current[0]["avaliacoes"] if item["sinal"] == "-")
        changed.update(sinal="+", justificativa="Mudei porque os demais concordaram.")
        before = copy.deepcopy(previous)
        with self.assertRaises(self.common.CouncilError):
            self.consolidate(packet, current, anteriores=previous, troca_autorizada=True)
        self.assertEqual(previous, before)

    def test_known_source_is_not_new_evidence_and_third_round_is_forbidden(self):
        packet = self.prepare(3)
        previous = self.make_verdicts(packet)
        current = copy.deepcopy(previous)
        for verdict in current:
            verdict["rodada"] = 2
        changed = next(item for item in current[0]["avaliacoes"] if item["sinal"] == "-")
        changed.update(sinal="+", evidencias_novas=["F1"])
        with self.assertRaises(self.common.CouncilError):
            self.consolidate(packet, current, anteriores=previous, troca_autorizada=True)
        self.assertRaises(self.common.CouncilError, self.protocol.prepare_exchange,
            packet["brief"], packet["painel"], packet["briefs_membros"], current, self.critique(packet))
        invalid = copy.deepcopy(previous[0])
        invalid["rodada"] = 3
        self.assertRaises(self.common.CouncilError, self.verdicts_module.validate_verdict,
                          invalid, packet["briefs_membros"][0])

    def test_one_fatal_requires_independent_confirmation(self):
        packet = self.prepare(1)
        target = next(h["id"] for h in packet["brief"]["hipoteses"] if "100%" in h["texto"])
        verdicts = self.make_verdicts(packet, target=target, fatal=True)
        result = self.consolidate(packet, verdicts)
        self.assertTrue(result["matriz"]["falhas_fatais"])
        self.assertFalse(result["matriz"]["completo"])
        self.assertTrue(any(item["tipo"] == "segundo_refutador_pendente" for item in result["alertas"]))

    def test_transport_requires_expected_model_and_explicit_execution(self):
        packet = self.prepare()
        config = {"command": [sys.executable, "-c", "raise SystemExit(77)"],
                  "autorizado": True, "modo_teste": True,
                  "isolamento_declarado": {"contexto_limpo": True, "sem_dossie": True, "modelo_aprovado": True}}
        planned = self.transport.execute_tasks(packet["briefs_membros"], config)
        self.assertEqual(planned["execucoes"], 0)
        self.assertRaises(self.common.CouncilError, self.transport.execute_tasks,
                          packet["briefs_membros"], config, executar=True, modo_teste=True)

    def test_transport_timeout_is_recorded_after_one_retry_without_fake_verdict(self):
        packet = self.prepare()
        config = {"command": [sys.executable, "-c", "import time; time.sleep(1)"],
                  "modelo_esperado": packet["painel"]["modelo_de_juiz"],
                  "timeout_seconds": 0.03, "workers": 2, "autorizado": True, "modo_teste": True,
                  "isolamento_declarado": {"contexto_limpo": True, "sem_dossie": True, "modelo_aprovado": True}}
        result = self.transport.execute_tasks(packet["briefs_membros"], config, executar=True, modo_teste=True)
        self.assertEqual(result["estado"], "parcial")
        for entry in result["resultados"]:
            self.assertEqual(len(entry["tentativas"]), 2)
            self.assertTrue(all(a["situacao"] == "tempo_esgotado" for a in entry["tentativas"]))
            self.assertNotIn("veredito", entry)
            self.assertIsNone(entry["modelo_efetivo"])

    def test_transport_failure_does_not_publish_stderr_or_fabricate_judgment(self):
        packet = self.prepare()
        config = {"command": [sys.executable, "-c", "import sys; print('SEGREDO-STDERR',file=sys.stderr);sys.exit(3)"],
                  "modelo_esperado": packet["painel"]["modelo_de_juiz"],
                  "timeout_seconds": 2, "autorizado": True, "modo_teste": True,
                  "isolamento_declarado": {"contexto_limpo": True, "sem_dossie": True, "modelo_aprovado": True}}
        result = self.transport.execute_tasks(packet["briefs_membros"], config, executar=True, modo_teste=True)
        self.assertEqual(result["estado"], "parcial")
        self.assertNotIn("SEGREDO-STDERR", json.dumps(result))
        self.assertTrue(all("veredito" not in entry for entry in result["resultados"]))


if __name__ == "__main__":
    unittest.main()
