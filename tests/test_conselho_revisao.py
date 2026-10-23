"""Regressões de fronteiras de confiança e preservação do contraditório."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills/conselho-especialistas/scripts"))
from _comum import CouncilError, canonical_hash
from anonimiza import anonymize
from conselho import consolidate, prepare, prepare_exchange
from matriz import build_matrix, quick_synthesis
from sintese_check import check_synthesis
from valida_veredito import validate_verdict


class RevisaoConselhoTest(unittest.TestCase):
    def prepare(self, *, complete=False):
        fixture = json.loads((ROOT / "evals/conselho-especialistas/fixtures/02-dissenso-fonte-desconhecida.json").read_text())
        request = fixture["request"]
        sessions = {"membros": ["sess-a", "sess-b"], "critico": "sess-c"}
        normalization = None
        if complete:
            request.update(conselho="completo", dose="completa",
                           oticas=["refutador de método", "especialista do domínio", "construtivo"])
            sessions.update(membros=["sess-a", "sess-b", "sess-d"], relator="sess-r", normalizador="sess-n")
            normalization = {"confirmada": True, "fidelidade_confirmada": True,
                             "sessao": "sess-n", "referencia": "NORMALIZACAO-QA",
                             "hipoteses_sha256": canonical_hash(anonymize(request["hipoteses"], seed=17)["hipoteses"])}
        return prepare(request, fixture["modelo_de_juiz"], seed=17,
                       sessoes=sessions, sessoes_produtoras=["sess-produtor"], normalizacao=normalization)

    def verdicts(self, packet, *, fatal=False):
        results = []
        for index, brief in enumerate(packet["briefs_membros"]):
            cells = [{"hipotese": h["id"], "criterio": c["id"], "sinal": "+",
                      "justificativa": "A premissa deste teste sustenta a hipótese no caso observado.",
                      "fontes": ["F1"], "raciocinio": "A conclusão está limitada ao caso observado.",
                      "mudaria": "Um contraexemplo documentado para a mesma premissa.",
                      "prob_resistir": None, "evidencias_novas": []}
                     for h in brief["hipoteses"] for c in brief["criterios"]]
            fatals = []
            if fatal and index == 0:
                cells[0]["sinal"] = "-"
                fatals = [{"hipotese": cells[0]["hipotese"], "criterio": cells[0]["criterio"],
                           "motivo": "O caso documentado contradiz a premissa universal.", "fontes": ["F1"]}]
            results.append({"schema_version": 1, "conselho_id": brief["conselho_id"], "membro": brief["membro"],
                            "rodada": 1, "criterios_sha256": brief["criterios_sha256"],
                            "avaliacoes": cells, "falhas_fatais": fatals, "fontes_novas": []})
        return results

    def critique(self, packet):
        return {"schema_version": 1, "conselho_id": packet["brief"]["id"], "aprovada": True,
                "revisor": packet["painel"]["critico"]["rotulo"], "achados": [], "referencia": "REVISAO-QA"}

    def consolidate(self, packet, verdicts, critique, **kwargs):
        return consolidate(packet["brief"], packet["painel"], packet["briefs_membros"], verdicts, critique, **kwargs)

    def full_synthesis(self, packet, verdicts, critique):
        matrix = build_matrix(packet["brief"], packet["painel"], verdicts, critique)
        synthesis = quick_synthesis(matrix)
        synthesis.update(tipo="completa", relator=packet["painel"]["relator"]["rotulo"])
        return matrix, synthesis

    def test_critique_must_be_from_designated_nonvoting_critic(self):
        packet = self.prepare()
        critique = self.critique(packet)
        critique["revisor"] = "critico-sem-designacao"
        with self.assertRaises(CouncilError):
            build_matrix(packet["brief"], packet["painel"], self.verdicts(packet), critique)

    def test_fatal_confirmation_cannot_reuse_panel_producer_or_auxiliary_session(self):
        packet = self.prepare(complete=True)
        verdicts = self.verdicts(packet, fatal=True)
        fatal = verdicts[0]["falhas_fatais"][0]
        panel = packet["painel"]
        excluded = [m["sessao"] for m in panel["membros"]] + ["sess-produtor"]
        excluded += [panel[role]["sessao"] for role in ("critico", "relator", "normalizador")]
        for session in excluded:
            with self.subTest(session=session):
                critique = self.critique(packet)
                critique["confirmacoes_falha_fatal"] = [{"hipotese": fatal["hipotese"], "criterio": fatal["criterio"],
                                                        "sessao": session, "otica": "refutador de limites teóricos",
                                                        "referencia": "SEGUNDA-REVISAO-QA"}]
                matrix = build_matrix(packet["brief"], panel, verdicts, critique)
                self.assertFalse(matrix["completo"])
                self.assertTrue(any(a["tipo"] == "segundo_refutador_pendente" for a in matrix["alertas"]))

    def test_fatal_confirmation_requires_a_different_optic(self):
        packet = self.prepare()
        verdicts = self.verdicts(packet, fatal=True)
        fatal = verdicts[0]["falhas_fatais"][0]
        critique = self.critique(packet)
        confirmation = {"hipotese": fatal["hipotese"], "criterio": fatal["criterio"], "sessao": "sess-extra",
                        "otica": packet["painel"]["membros"][0]["otica"], "referencia": "SEGUNDA-REVISAO-QA"}
        critique["confirmacoes_falha_fatal"] = [confirmation]
        self.assertFalse(build_matrix(packet["brief"], packet["painel"], verdicts, critique)["completo"])
        confirmation["otica"] = "refutador de limites teóricos"
        self.assertTrue(build_matrix(packet["brief"], packet["painel"], verdicts, critique)["completo"])

    def test_complete_synthesis_is_bound_to_independent_reporter(self):
        packet = self.prepare(complete=True)
        verdicts, critique = self.verdicts(packet), self.critique(packet)
        _, synthesis = self.full_synthesis(packet, verdicts, critique)
        for edit in (lambda s: s.pop("relator"), lambda s: s.update(relator="relator-sem-designacao"),
                     lambda s: s.update(relator=packet["painel"]["membros"][0]["rotulo"]),
                     lambda s: s.update(tipo="rapida")):
            candidate = copy.deepcopy(synthesis)
            edit(candidate)
            with self.assertRaises(CouncilError):
                self.consolidate(packet, verdicts, critique, synthesis=candidate)
        self.assertEqual(self.consolidate(packet, verdicts, critique, synthesis=synthesis)["estado"], "consolidado_localmente")

    def test_unconfirmed_solitary_fatal_is_returned_as_partial(self):
        packet = self.prepare()
        result = self.consolidate(packet, self.verdicts(packet, fatal=True), self.critique(packet))
        self.assertFalse(result["matriz"]["completo"])
        self.assertEqual(result["estado"], "parcial_requer_revisao")

    def test_private_source_addresses_are_rejected_before_member_briefs(self):
        fixture = json.loads((ROOT / "evals/conselho-especialistas/fixtures/02-dissenso-fonte-desconhecida.json").read_text())
        for url in ("https://private.notion.so/contexto", "https://localhost/contexto", "http://10.2.3.4/contexto", "http://[fd00::1]/contexto"):
            with self.subTest(url=url):
                request = copy.deepcopy(fixture["request"])
                request["fontes"][0]["url"] = url
                with self.assertRaises(CouncilError):
                    prepare(request, fixture["modelo_de_juiz"], seed=17, sessoes_produtoras=[])

    def test_synthesis_cannot_forge_source_reasoning_or_counterevidence_condition(self):
        packet = self.prepare(complete=True)
        verdicts, critique = self.verdicts(packet), self.critique(packet)
        matrix, synthesis = self.full_synthesis(packet, verdicts, critique)
        self.assertTrue(check_synthesis(matrix, synthesis)["valida"])
        for field, value in (("fontes", ["F-INVENTADA"]), ("raciocinio", "Conclusão sem o limite registrado."),
                             ("mudaria", "Nenhuma evidência mudaria esta posição.")):
            with self.subTest(field=field):
                candidate = copy.deepcopy(synthesis)
                candidate["pontos"][0]["argumentos"][0][field] = value
                self.assertFalse(check_synthesis(matrix, candidate)["valida"])

    def test_private_critique_fields_never_enter_public_packet(self):
        packet = self.prepare()
        critique = self.critique(packet)
        critique["modelo"] = "MODELO-PRIVADO-NA-CRITICA"
        critique["chave_privada"] = packet["chave_privada"]
        try:
            result = self.consolidate(packet, self.verdicts(packet), critique)
        except CouncilError:
            return  # Recusar o pacote contaminado também preserva a fronteira.
        public = json.dumps(result["arquivos"], ensure_ascii=False)
        self.assertFalse("MODELO-PRIVADO-NA-CRITICA" in public, "Modelo privado foi copiado ao pacote público")
        self.assertFalse("AUTORIA_PRIVADA" in public, "Chave de autoria foi copiada ao pacote público")

    def test_invalidated_leaked_verdict_is_not_republished_in_public_packet(self):
        packet = self.prepare()
        verdicts, critique = self.verdicts(packet), self.critique(packet)
        cell = verdicts[0]["avaliacoes"][0]
        cell["justificativa"] = "SEGREDO-CONTEXTO-VAZADO"
        critique["achados"] = [{"membro": verdicts[0]["membro"], "hipotese": cell["hipotese"], "criterio": cell["criterio"],
                               "tipo": "possivel_vazamento", "justificativa": "Citou contexto fora do brief.", "evidencias": ["AUDITORIA-QA"]}]
        try:
            result = self.consolidate(packet, verdicts, critique)
        except CouncilError:
            return
        self.assertFalse(result["matriz"]["completo"])
        self.assertFalse("SEGREDO-CONTEXTO-VAZADO" in json.dumps(result["arquivos"], ensure_ascii=False),
                         "Veredito invalidado por vazamento foi republicado")

    def test_private_synthesis_fields_never_enter_public_packet(self):
        packet = self.prepare(complete=True)
        verdicts, critique = self.verdicts(packet), self.critique(packet)
        _, synthesis = self.full_synthesis(packet, verdicts, critique)
        synthesis["modelo"] = "MODELO-PRIVADO-NA-SINTESE"
        synthesis["chave_privada"] = packet["chave_privada"]
        try:
            result = self.consolidate(packet, verdicts, critique, synthesis=synthesis)
        except CouncilError:
            return
        public = json.dumps(result["arquivos"], ensure_ascii=False)
        self.assertFalse("MODELO-PRIVADO-NA-SINTESE" in public, "Modelo privado foi copiado ao pacote público")
        self.assertFalse("AUTORIA_PRIVADA" in public, "Chave de autoria foi copiada ao pacote público")

    def test_new_source_cannot_carry_extra_private_fields(self):
        packet = self.prepare()
        verdict = self.verdicts(packet)[0]
        source = {"id": "F-NOVA", "url": "https://example.org/contraexemplo", "trecho": "Caso adverso registrado.",
                  "afirmacao": "A premissa não cobre este caso.", "verificada": True}
        verdict["fontes_novas"] = [source]
        verdict["avaliacoes"][0]["fontes"] = [source["id"]]
        validate_verdict(verdict, packet["briefs_membros"][0])
        source["chave_privada"] = packet["chave_privada"]
        with self.assertRaises(CouncilError):
            validate_verdict(verdict, packet["briefs_membros"][0])

    def test_exchange_transmits_peer_source_cards_anonymously_and_deterministically(self):
        packet = self.prepare(complete=True)
        verdicts, critique = self.verdicts(packet), self.critique(packet)
        for index, verdict in enumerate(verdicts):
            source = {"id": f"F-PESQUISA-{index}", "url": f"https://example.org/pesquisa/{index}",
                      "trecho": f"Observação independente {index}.", "afirmacao": "O caso testa a premissa.", "verificada": True}
            verdict["fontes_novas"] = [source]
            for cell in verdict["avaliacoes"]:
                cell.update(sinal="-" if index == 0 else "+", fontes=[source["id"]],
                            justificativa=f"Argumento independente {index} sobre {cell['hipotese']}.")
        inputs = (packet["brief"], packet["painel"], packet["briefs_membros"], verdicts, critique)
        before = copy.deepcopy(inputs)
        exchange = prepare_exchange(*inputs)
        self.assertEqual(prepare_exchange(*inputs), exchange, "A mesma semente privada deve reproduzir a troca")
        self.assertEqual(inputs, before, "Preparar a troca não pode alterar o registro da rodada independente")
        private_tokens = [m["rotulo"] for m in packet["painel"]["membros"]]
        private_tokens += [packet["painel"]["modelo_de_juiz"], "AUTORIA_PRIVADA", "chave_privada", "semente"]
        for envelope in exchange:
            peer_sources = [source for verdict in verdicts if verdict["membro"] != envelope["membro"]
                            for source in verdict["fontes_novas"]]
            received = envelope["fontes_da_troca"]
            self.assertEqual({s["id"]: s for s in received}, {s["id"]: s for s in peer_sources})
            arguments = envelope["argumentos_anonimos"]
            self.assertEqual(len(arguments), 4)
            self.assertTrue(all(set(argument["fontes"]) <= {source["id"] for source in received} for argument in arguments))
            public_exchange = json.dumps({"argumentos": arguments, "fontes": received,
                                          "notas": envelope["notas_do_critico"]}, ensure_ascii=False)
            for token in private_tokens:
                self.assertFalse(token in public_exchange, f"Troca revelou marcador privado: {token}")


if __name__ == "__main__":
    unittest.main()
