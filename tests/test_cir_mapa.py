"""Mecanismos locais com dados sintéticos; não são pesquisa nem avaliação de modelos."""
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
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/cir-mapa"
sys.path.insert(0, str(SKILL / "scripts"))
core = importlib.import_module("mapa_core")
mapa = importlib.import_module("mapa")
casos = importlib.import_module("casos")
pacote = importlib.import_module("pacote")
inventario = importlib.import_module("inventario")
cartoes = importlib.import_module("cartoes")
sinais = importlib.import_module("sinais")


def source(key="F-A"):
    return {"id": key, "referencia": "Documento sintético de teste, não fonte real",
            "trecho": "A medição sintética foi registrada no ponto de entrega.",
            "afirmacao": "Descrição fornecida no exercício", "data": "2020-01-01", "conferida": True}


def cause(key="C1", origin="sua"):
    return {"id": key, "texto": "Pressão varia ao longo da distribuição", "origem": origin,
            "falha": "F1", "cadeia": ["Pressão oscila no percurso", "A entrega fica irregular"],
            "previsoes": {"se_verdadeira": "Irregularidade acompanha a pressão", "se_falsa": "Permanece com pressão estável"},
            "pergunta_contra": "Onde a falha persiste sem oscilação?", "observacao_faltante": "Controle com pressão estável",
            "mudaria_se": "Irregularidade persistir sem variação", "busca": {"favor": "P1", "contra": "P2"},
            "evidencias": [{"texto": "Mudança observada no cenário sintético", "teste": "aro", "lado": "favor", "resultado": "passou", "fontes": ["F-E"]}],
            "forca": "media", "motivo_forca": "Comparação sem controle", "fontes_mecanismo": ["F-A"],
            "fontes_dependencia": ["F-E"], "tipo_dependencia": "sem_controle", "falha_igual_sem_causa": False,
            "situacao": "principal" if key == "C1" else "rival_viva"}


def map_data():
    stages = [{"id": "J" + str(n), "categoria": name, "texto": "Verificar condição " + str(n),
               "aplica": True, "executor": "Operador", "hoje": "Prática descrita no exercício", "fontes": ["F-A"]}
              for n, name in enumerate(sorted(mapa.CATEGORIES))]
    return {"schema_version": 1, "job": "Entregar água em condição de uso", "fontes": [source(), source("F-E")],
            "etapas": stages, "passagens": [{"de": "J0", "para": "J1", "o_que_passa": "Informação", "o_que_se_perde": "Horário"}],
            "variacoes": ["Pico de demanda"], "gambiarras": ["Conferência adicional"],
            "falhas": [{"id": "F1", "texto": "Entrega irregular de água", "central": True, "etapas": ["J0"],
                        "partes": ["P1"], "frequencia": "A medir com registros diários", "gravidade": "Interrompe o uso",
                        "arvore": {"outras_causas": "Peso desconhecido", "ramos": [{"causa": "C1", "tipo": "ramo"}, {"causa": "C2", "tipo": "ramo"}]}}],
            "causas": [cause(), cause("C2", "gerador-independente")], "lacos": [],
            "contradicoes": [{"id": "T1", "parametros": ["vazão", "pressão"], "forma_fisica": "Mesma rede",
                              "classe": "limite_hoje", "data": "2020-01-01", "fontes": ["F-A"],
                              "busca_prova": "P3", "busca_contraexemplo": "P4"}],
            "projecao": {"classe_referencia": "Redes do exercício", "sua_versao": "Estabilidade", "fontes": ["F-A"],
                         "taxas_base": "Faixa fornecida no cenário sintético",
                         "horizontes": [{"prazo": p, "faixa": "Condição estável a instável", "partes": "Moradores", "ajuste_motivo": "Sem ajuste"} for p in ["5 anos", "20 anos"]]},
            "conhecimento": [{"id": "K1", "texto": "Variação local pode persistir", "classe": "incerto", "se_falsa": "Rever causa",
                              "resolveria": "Medir em ponto fixo", "custo_investigar": "A estimar por plano de medição"},
                             {"id": "K2", "texto": "Horário de uma avaria futura", "classe": "impossivel_saber", "se_falsa": "Rever antecipação",
                              "por_que": "Evento aleatório", "natureza": "aleatorio"}],
            "analogias": [], "partes": [{"id": "P1", "texto": "Moradores"}],
            "contagem_casos": {"comum": 1, "falha": 3, "sucesso": 3, "simetria": 4, "evidencia_contraria": 2, "nada_relevante": 2}}


def bank_data():
    kinds = ["falha"] * 3 + ["sucesso"] * 3 + ["simetria"] * 4 + ["evidencia_contraria"] * 2 + ["nada_relevante"] * 2 + ["comum"] * 6
    result = {"schema_version": 1, "fontes": [source()], "modelo_sonda": "modelo-sintetico", "modelo_geradores": "modelo-sintetico", "casos": []}
    for n, kind in enumerate(kinds):
        result["casos"].append({"id": f"A{n}", "tipo": kind, "marcador": f"⟦teste-{n:04d}⟧", "origem": "Exercício sintético",
            "dificuldade": "Informação incompleta no ponto de entrega", "data_corte": "2020-01-01",
            "antes": [{"texto": f"Registro {n} descrevia a distribuição sem informação sobre a entrega posterior.", "disponivel_em": "2019-12-30", "fontes": ["F-A"]}],
            "desfecho": {"texto": f"Resultado documentado {n} foi registrado apenas no dia seguinte.", "data": "2020-01-02", "fontes": ["F-A"]},
            "lado": "ruim" if kind == "falha" else "bom", "construido": False,
            "visto": False, "depois_solucao": False, "conhecido_modelo": False,
            "sonda": {"modelo": "modelo-sintetico", "continuacao": "Não sei o resultado", "acertos_nao_no_antes": []}})
        if kind == "simetria":
            result["casos"][-1].update(par="S" + str((n - 6) // 2), relacao_esperada="Trocar junto com os lados")
    return result


class MapTest(unittest.TestCase):
    def test_full_map_and_fifteen_clean_variants(self):
        for n in range(15):
            with self.subTest(n=n):
                v = map_data(); v["job"] += " no contexto " + str(n)
                self.assertTrue(mapa.validate(v)["valido"])

    def test_thirty_planted_structural_defects(self):
        edits = [
            lambda v: v.update(schema_version=True),
            lambda v: v.update(job=""),
            lambda v: v["etapas"].pop(),
            lambda v: v["etapas"][0].update(fontes=[], hipotese=False),
            lambda v: v["etapas"][0].update(aplica=False, motivo=""),
            lambda v: v["passagens"][0].update(para="NA"),
            lambda v: v["causas"][1].update(origem="sua"),
            lambda v: v["falhas"][0]["arvore"].pop("outras_causas"),
            lambda v: v["falhas"][0]["arvore"]["ramos"][0].update(causa="NA"),
            lambda v: v["causas"][0].update(cadeia=["erro humano"]),
            lambda v: v["causas"][0].update(cadeia=["Carga alta", "erro humano"]),
            lambda v: v["causas"][0]["previsoes"].update(se_falsa=""),
            lambda v: v["causas"][0]["busca"].update(contra="P1"),
            lambda v: v["causas"][0]["evidencias"][0].update(teste="contagem"),
            lambda v: v["causas"][0].update(fontes_dependencia=[]),
            lambda v: v["causas"][0].update(tipo_dependencia="correlacao"),
            lambda v: v["causas"][0].update(forca="forte"),
            lambda v: v["causas"][0]["evidencias"][0].update(teste="nao_diagnostica"),
            lambda v: v["contradicoes"][0].update(classe="principio"),
            lambda v: v["contradicoes"][0].update(classe="eterna"),
            lambda v: v["contradicoes"][0].update(data="ontem"),
            lambda v: v["contradicoes"][0].update(busca_contraexemplo="P3"),
            lambda v: v["contradicoes"][0].update(parametros=["A"]),
            lambda v: v["projecao"].update(horizontes=[]),
            lambda v: v["projecao"].update(fontes=["NA"]),
            lambda v: v["conhecimento"][0].update(resolveria=""),
            lambda v: v["conhecimento"][1].update(natureza="limite_tecnico"),
            lambda v: v["fontes"][0].update(conferida=False),
            lambda v: v["causas"].append(copy.deepcopy(v["causas"][0])),
            lambda v: v["partes"][0].update(id="C1"),
        ]
        for n, edit in enumerate(edits):
            with self.subTest(n=n):
                v = map_data(); edit(v)
                with self.assertRaises((core.Invalid, ValueError)):
                    mapa.validate(v)

    def test_unknown_cause_requires_auditable_exception(self):
        v = map_data(); v["causas"] = []; f = v["falhas"][0]
        f["arvore"] = {"outras_causas": "Peso desconhecido", "ramos": []}
        with self.assertRaises(core.Invalid): mapa.validate(v)
        f["causa_desconhecida"] = True
        f["excecao_rivais"] = dict(registro="D-01", motivo="Nenhuma causa sustentada", busca_rivais="G1 e G2 buscaram", dissenso="Incerteza preservada", observacao_que_resolveria="Medição discriminante")
        self.assertTrue(mapa.validate(v)["valido"])

    def test_principle_and_counterexample(self):
        v = map_data(); c = v["contradicoes"][0]
        c.update(classe="principio", lei="Lei sintética do cenário", conta="Demonstração sintética",
                 parecer="P-T1", conselho="J-T1", contraexemplo_valido=False,
                 premissas=[{"texto": "Condição fornecida", "fontes": ["F-A"], "movel": True}])
        self.assertTrue(mapa.validate(v)["valido"])
        c["contraexemplo_valido"] = True
        with self.assertRaises(core.Invalid): mapa.validate(v)

    def test_known_k_requires_literal_source_excerpt(self):
        v = map_data(); k = v["conhecimento"][0]
        k.update(classe="sabido", fontes=["F-A"], trecho="Não existe na ficha")
        with self.assertRaises(core.Invalid): mapa.validate(v)
        k["trecho"] = v["fontes"][0]["trecho"]
        self.assertTrue(mapa.validate(v)["valido"])

    def test_force_not_based_on_count_and_strong_requires_control(self):
        v = map_data(); c = v["causas"][0]
        c.update(forca="forte", tipo_dependencia="controle")
        self.assertTrue(mapa.validate(v)["valido"])
        c["falha_igual_sem_causa"] = True
        with self.assertRaises(core.Invalid): mapa.validate(v)

    def test_partial_job_map_and_mermaid_do_not_inject_syntax(self):
        v = map_data(); v["falhas"][0]["texto"] = 'Falha "] --> hack["'
        self.assertTrue(mapa.validate(v, ate="2.1")["valido"])
        self.assertNotIn('"] --> hack', mapa.mermaid(v))
        self.assertIn('outras causas', mapa.mermaid(v))

    def test_markdown_without_canonical_data_is_not_validated(self):
        with self.assertRaises(core.Invalid): core.loads("# Mapa\nTudo parece certo")
        v = map_data()
        self.assertEqual(v, core.loads(core.markdown("Mapa", v)))


class HistoryTest(unittest.TestCase):
    def test_git_chronology_and_retrospective_edit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def git(*args):
                return subprocess.check_output(["git", "-C", tmp, *args], text=True).strip()
            git("init", "-q"); git("config", "user.name", "Teste"); git("config", "user.email", "teste@example.invalid")
            v = map_data(); pre = copy.deepcopy(v)
            pre["fontes"] = [source()]
            for c in pre["causas"]: c["evidencias"] = []
            (root / "02-mapa.md").write_text(core.markdown("Mapa", pre))
            git("add", "."); git("commit", "-qm", "Previsões antes da busca"); before = git("rev-parse", "HEAD")
            (root / "02-mapa.md").write_text(core.markdown("Mapa", v))
            git("add", "."); git("commit", "-qm", "Busca e fichas"); after = git("rev-parse", "HEAD")
            for c in v["causas"]:
                c["historico"] = {"pre_registro": before, "busca": after, "arquivo": "02-mapa.md"}
            self.assertEqual([], mapa.validate(v, root)["pendencias"])
            v["causas"][0]["previsoes"]["se_falsa"] = "Agora reescrevi a previsão"
            with self.assertRaises(core.Invalid): mapa.validate(v, root)
            v["causas"][0]["previsoes"] = pre["causas"][0]["previsoes"]
            v["causas"][0]["historico"]["pre_registro"] = after
            with self.assertRaises(core.Invalid): mapa.validate(v, root)


class BankTest(unittest.TestCase):
    def test_bank_and_stratified_reproducibility_pairs_together(self):
        v = bank_data(); self.assertTrue(casos.validate(v)["valido"])
        a = casos.draw(v, 42, "3.6"); b = copy.deepcopy(v); b["casos"].reverse()
        self.assertEqual(a, casos.draw(b, 42, "3.6"))
        self.assertGreaterEqual(len(a["trabalho"]), 10)
        for left, right in [("A6", "A7"), ("A8", "A9")]:
            self.assertEqual(left in a["reservados"], right in a["reservados"])

    def test_exposed_known_and_post_solution_never_reserved(self):
        for flag in ("visto", "conhecido_modelo", "depois_solucao"):
            v = bank_data(); v["casos"][0][flag] = True
            if flag == "conhecido_modelo": v["casos"][0]["sonda"]["acertos_nao_no_antes"] = ["Detalhe fora do início"]
            self.assertNotIn("A0", casos.draw(v, 42, "3.6")["reservados"])

    def test_pending_probe_and_missing_type_do_not_relax_reserves(self):
        v = bank_data()
        for c in v["casos"]:
            if c["tipo"] == "comum": c["conhecido_modelo"] = None
        with self.assertRaises(core.Invalid): casos.draw(v, 3, "3.6")

    def test_never_redraw_frozen_bank(self):
        v = bank_data(); v["sorteio"] = casos.draw(v, 1, "3.6")
        with self.assertRaises(core.Invalid): casos.draw(v, 2, "3.6")
        with self.assertRaises(core.Invalid): casos.draw(bank_data(), 1, "2.6")

    def test_bad_dates_outcome_in_before_and_quotas(self):
        mutations = [lambda b: b["casos"][0]["antes"][0].update(disponivel_em="2020-01-03"),
                     lambda b: b["casos"][0]["antes"][0].update(texto=b["casos"][0]["desfecho"]["texto"]),
                     lambda b: b["casos"][0].update(marcador=b["casos"][1]["marcador"]),
                     lambda b: b["casos"][0].update(conhecido_modelo=False, sonda={"modelo": "Outro"}),
                     lambda b: [c.update(lado="bom") for c in b["casos"]],
                     lambda b: [c.update(tipo="comum") for c in b["casos"] if c["tipo"] == "nada_relevante"],
                     lambda b: b["casos"][0].update(construido=True)]
        for n, mut in enumerate(mutations):
            with self.subTest(n=n):
                v = bank_data(); mut(v)
                with self.assertRaises(core.Invalid): casos.validate(v)

    def test_probe_cannot_see_outcome_sources_or_markers(self):
        v = bank_data(); result = casos.probe(v)
        raw = core.dump(result)
        self.assertNotIn("desfecho", raw); self.assertNotIn("fontes", raw); self.assertNotIn("⟦", raw)
        for c in v["casos"]: self.assertNotIn(c["desfecho"]["texto"], raw)

    def test_leakage_reports_paths_not_secret_text_and_audit_fails_on_symlink(self):
        v = bank_data()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root / "casos").mkdir(); (root / "briefs").mkdir()
            (root / "casos/candidatos.md").write_text(core.markdown("Casos", v))
            self.assertTrue(casos.leakage(v, root)["limpo"])
            (root / "briefs/vazou.md").write_text(v["casos"][0]["marcador"] + v["casos"][1]["desfecho"]["texto"])
            result = casos.leakage(v, root)
            self.assertFalse(result["limpo"]); self.assertNotIn("⟦", core.dump(result))
            (root / "link").symlink_to(root / "casos")
            with self.assertRaises(core.Invalid): casos.leakage(v, root)


class IntegrationTest(unittest.TestCase):
    def test_forty_flagged_and_twenty_clean_lexical_examples(self):
        corpus = json.loads((ROOT / 'evals/cir-mapa/frases-plantadas.json').read_text())
        self.assertEqual(40, len(corpus['contaminadas']))
        self.assertEqual(20, len(corpus['limpas']))
        for kind, expected in [('contaminadas', True), ('limpas', False)]:
            for entry in corpus[kind]:
                with self.subTest(entry=entry):
                    result = sinais.scan(entry['texto'], entry['peca'])
                    self.assertEqual(expected, bool(result['sinais']))
                    self.assertFalse(result['bloqueia'])

    def test_package_same_shape_no_authorship_no_truncation(self):
        result = pacote.build(map_data()); self.assertEqual(result, pacote.validate(copy.deepcopy(result)))
        self.assertNotIn("origem", result)
        v = copy.deepcopy(result); v["causas"] = "A equipe acredita que X"
        with self.assertRaises(core.Invalid): pacote.validate(v)
        v = copy.deepcopy(result); v["job"] = "palavra " * 601
        with self.assertRaises(core.Invalid): pacote.validate(v)
        v = copy.deepcopy(result); v["banco"] = "Caso do bairro com desfecho conhecido"
        with self.assertRaises(core.Invalid): pacote.validate(v)

    def test_inventory_is_accepted_by_real_coverage_interface(self):
        # Usa a dependência real disponível; não um dublê de especialistas.
        sys.path.insert(0, str(ROOT / "skills/especialistas/scripts"))
        coverage = importlib.import_module("cobertura")
        v = inventario.inventory(map_data()); result = coverage.coverage(v)
        self.assertFalse(result["cobertura_completa"])
        self.assertIn("K1", [k["id"] for k in v["lacunas_espaco_k"]])
        self.assertNotIn("K1", result["cobertura"])
        self.assertIn("C1", result["centrais_sem_cobertura"])

    def test_cards_against_actual_source_and_selected_plan(self):
        source = (ROOT / "sources/originais/fluxograma-completo-ideal.md").read_text()
        import re
        entries = [{"id": k, "titulo": title, "dose": dose}
                   for k, title, dose in re.findall(r"^#### (2\.[1-7]) (.*?) · dose (padrão|completa)", source, re.M)]
        cards = (SKILL / "references/cartoes.md").read_text()
        self.assertTrue(cartoes.check(cards, entries)["valido"])
        plan = (ROOT / "sources/originais/plano-cir-mapa.md").read_text()
        raw = '### Tema 2' + plan.split('```markdown\n### Tema 2', 1)[1].split('```', 1)[0]
        self.assertIn(raw, cards)
        entries[0]["dose"] = "leve"
        with self.assertRaises(core.Invalid): cartoes.check(cards, entries)

    def test_extracted_package_runs_real_clis_without_repository(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); archive = root / "cir-mapa.skill"
            env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
            subprocess.run([sys.executable, str(ROOT / "scripts/empacotar_skill.py"), "--skill", str(SKILL), "--destino", str(archive)], check=True, capture_output=True, env=env)
            with zipfile.ZipFile(archive) as z: z.extractall(root / "extraido")
            scripts = root / "extraido/cir-mapa/scripts"
            (root / "02-mapa.md").write_text(core.markdown("Mapa", map_data()))
            (root / "banco.md").write_text(core.markdown("Casos", bank_data()))
            def run(script, *args):
                p = subprocess.run([sys.executable, str(scripts / script), *map(str, args)], cwd=root, capture_output=True, text=True, env=env)
                self.assertEqual(0, p.returncode, p.stderr)
                return p.stdout
            self.assertTrue(json.loads(run("mapa.py", root / "02-mapa.md"))["valido"])
            self.assertIn("flowchart TD", run("mapa.py", root / "02-mapa.md", "--mermaid"))
            self.assertEqual(20, json.loads(run("casos.py", "validar", root / "banco.md"))["total"])
            self.assertTrue(json.loads(run("casos.py", "sortear", root / "banco.md", "--semente", "42", "--etapa", "3.6"))["reservados"])
            self.assertTrue(json.loads(run("pacote.py", "montar", root / "02-mapa.md"))["banco"])
            self.assertTrue(json.loads(run("inventario.py", root / "02-mapa.md"))["itens"])
            (root / "frase.md").write_text("A correlação não basta para identificar uma causa.")
            self.assertTrue(json.loads(run("sinais.py", root / "frase.md", "--peca", "causa"))["sinais"])
            import re
            source_text = (ROOT / "sources/originais/fluxograma-completo-ideal.md").read_text()
            entries = [{"id": k, "titulo": title, "dose": dose}
                       for k, title, dose in re.findall(r"^#### (2\.[1-7]) (.*?) · dose (padrão|completa)", source_text, re.M)]
            (root / "indice.json").write_text(json.dumps(entries))
            self.assertEqual(7, json.loads(run("cartoes.py", "--indice", root / "indice.json"))["cartoes"])


if __name__ == "__main__":
    unittest.main()
