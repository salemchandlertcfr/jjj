"""Infraestrutura do recrutamento. Bibliotecas e executores aqui são dublês temporários."""
from __future__ import annotations
import copy
from datetime import date
import hashlib
import importlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/especialistas"
sys.path.insert(0, str(SKILL / "scripts"))
core = importlib.import_module("esp_core")
cat = importlib.import_module("catalogo")
cov = importlib.import_module("cobertura")
cards = importlib.import_module("fichas")
brief = importlib.import_module("brief_esp")
gaps = importlib.import_module("lacunas")
gate = importlib.import_module("teste_esp")


def sample(name):
    return json.loads((SKILL / "assets/modelos" / name).read_text())


class Setup(unittest.TestCase):
    def setUp(self):
        self.map = sample("mapa.json")
        self.models = sample("modelos.json")
        self.cat = sample("catalogo.json")

    def ficha(self, spec=0, role="especialista", number=1, dose="padrao", step=7):
        draft = sample("ficha.json")
        s = self.map["especialidades"][spec]
        draft.update(id=f"E-{number}", nome=f"especialidade-{number}", sessao=f"sessao-{number}",
                     papel=role, dose=dose, passo=step, especialidade=s["especialidade"], cobre=s["cobre"], lacuna=s["lacuna"])
        if role == "gerador":
            draft.update(operadores=[f"OP-{number}"], semente=42)
        if role == "critico":
            draft.update(especialidade="revisao de metodo", lacuna="LAC-METODO")
        return cards.new(draft, self.models)

    def team(self):
        return {"formacao": "equipe", "fichas": [self.ficha(i, number=i+1) for i in range(3)]
                + [self.ficha(role="critico", number=4)], "itens_exigidos": ["C1", "K1", "P1"]}


class CoverageTest(Setup):
    def test_all_items_covered_even_with_empty_library(self):
        result = cov.coverage(self.map)
        self.assertTrue(result["cobertura_completa"])
        self.assertIn("LAC-S1", result["lacunas"])

    def test_missing_central_is_reported(self):
        self.map["especialidades"] = self.map["especialidades"][1:]
        result = cov.coverage(self.map)
        self.assertEqual(result["centrais_sem_cobertura"], ["C1"])

    def test_greedy_prefers_coverage_not_curated_availability_or_score(self):
        for spec in self.map["especialidades"]:
            spec["placar"] = 10000 if spec["id"] == "S3" else -999
        result = cov.suggest(self.map, 1)
        self.assertEqual(result["sugeridas"], ["S1"])
        self.assertIn("S3", result["reserva"])

    def test_unrelated_discipline_without_source_is_rejected(self):
        self.map["especialidades"][0]["fontes"] = []
        self.assertRaises(core.EspError, cov.coverage, self.map)

    def test_compare_keeps_unique_discipline_visible(self):
        second = copy.deepcopy(self.map)
        second["especialidades"] = second["especialidades"][1:]
        result = cov.compare(self.map, second)
        self.assertIn("hidraulica de redes", result["so_primeiro"])
        self.assertEqual(result["segundo"]["centrais_sem_cobertura"], ["C1"])
        second["itens"][0]["texto"] = "outro problema"
        self.assertRaises(core.EspError, cov.compare, self.map, second)

    def test_theme_needs_one_analogy_and_critic(self):
        self.map["temas"] = [{"id": "T4", "critico": True, "equipe_base": ["S1"], "reserva": [],
                               "distante": {"especialidade": "S4", "funcao_analoga": "transferir sem interromper"}}]
        self.assertTrue(cov.coverage(self.map)["cobertura_completa"])
        self.map["temas"][0]["critico"] = False
        self.assertRaises(core.EspError, cov.coverage, self.map)

    def test_27_requires_recruiters_generators_and_merge_record(self):
        self.map.update(etapa="2.7", dose="padrao")
        self.assertRaises(core.EspError, cov.coverage, self.map)
        self.map.update(recrutadores=["R1", "R2"], geradores_distantes=["G1"], fusao="diferenças registradas",
                        temas=[{"id": "T4", "critico": True, "equipe_base": ["S1"], "distante": {"especialidade": "S4", "funcao_analoga": "passagem contínua"}}])
        self.assertTrue(cov.coverage(self.map)["cobertura_completa"])


class CardTest(Setup):
    def test_valid_preparation_does_not_claim_executable_model(self):
        result = cards.formation(self.team(), self.cat, self.models, self.map)
        self.assertTrue(result["valida"])
        self.assertFalse(result["executavel"])
        self.assertIn("LAC-S1", result["lacunas"])

    def test_model_and_map_approval_are_both_needed(self):
        for model in self.models.values():
            model["verificado"] = True
        self.assertFalse(cards.formation(self.team(), self.cat, self.models, self.map)["executavel"])
        self.map["aprovacao"] = {"aprovada": True, "decisao": "D1"}
        self.assertTrue(cards.formation(self.team(), self.cat, self.models, self.map)["executavel"])

    def test_view_cannot_be_changed_during_creation(self):
        draft = sample("ficha.json"); draft["ve"] = ["dossie"]
        self.assertRaises(core.EspError, cards.new, draft, self.models)

    def test_thirty_planted_invalid_formations_are_rejected(self):
        corpus = json.loads((ROOT / "evals/especialistas/fichas-plantadas.json").read_text())
        self.assertEqual(len(corpus), 30)
        for mutation in corpus:
            with self.subTest(mutation=mutation["id"]):
                packet = self.team()
                if mutation["acao"] == "sem_critico":
                    packet["fichas"] = packet["fichas"][:-1]
                elif mutation["acao"] == "duas_distantes":
                    for f in packet["fichas"][:2]:
                        f.update(distante=True, funcao_analoga="função descrita")
                else:
                    packet["fichas"][0][mutation["campo"]] = mutation["valor"]
                self.assertRaises(core.EspError, cards.formation, packet, self.cat, self.models, self.map)

    def test_outside_map_needs_explicit_decision(self):
        f = self.ficha(); f["especialidade"] = "nova disciplina"
        self.assertRaises(core.EspError, cards.validate, f, self.cat, self.models, self.map)
        f["excecao_mapa"] = {"aprovada": True, "decisao": "D-extra"}
        self.assertEqual(cards.validate(f, self.cat, self.models, self.map), f)

    def test_complete_team_has_fourth_distant_and_separate_critic(self):
        members = [self.ficha(i, number=i+1, dose="completa") for i in range(4)]
        members[-1].update(distante=True, funcao_analoga="transferir um sistema em operação sem perda")
        packet = {"formacao": "equipe", "fichas": members+[self.ficha(role="critico", number=5, dose="completa")], "itens_exigidos": ["C1"]}
        self.assertTrue(cards.formation(packet, self.cat, self.models, self.map)["valida"])
        packet["fichas"][0], packet["fichas"][3] = packet["fichas"][3], packet["fichas"][0]
        self.assertRaises(core.EspError, cards.formation, packet, self.cat, self.models, self.map)

    def test_generator_seed_and_no_repeated_operators(self):
        fs = [self.ficha(i, "gerador", i+1, "completa") for i in range(2)]
        fs[-1].update(distante=True, funcao_analoga="função em outro domínio")
        shuffled = cards.operators(fs, ["A", "B", "C"], 42)
        self.assertEqual(shuffled, cards.operators(fs, ["C", "A", "B"], 42))
        packet = {"formacao": "geradores", "fichas": shuffled, "itens_exigidos": []}
        self.assertTrue(cards.formation(packet, self.cat, self.models, self.map)["valida"])
        shuffled[1]["operadores"] = shuffled[0]["operadores"]
        self.assertRaises(core.EspError, cards.formation, packet, self.cat, self.models, self.map)

    def test_verifier_session_cannot_have_produced(self):
        fs = [self.ficha(i, "verificador", i+1, "completa", 8) for i in range(2)]
        fs.append(self.ficha(role="critico", number=3, dose="completa", step=8))
        packet = {"formacao": "verificacao", "fichas": fs, "itens_exigidos": [], "sessoes_produtoras": ["sessao-produtora"]}
        self.assertTrue(cards.formation(packet, self.cat, self.models, self.map)["valida"])
        packet["sessoes_produtoras"] = ["sessao-1"]
        self.assertRaises(core.EspError, cards.formation, packet, self.cat, self.models, self.map)

    def test_duplicate_specialty_only_with_distinct_schools(self):
        packet = self.team(); first = packet["fichas"][0]; second = packet["fichas"][1]
        second.update(especialidade=first["especialidade"], cobre=first["cobre"], lacuna=first["lacuna"])
        packet["itens_exigidos"] = []
        self.assertRaises(core.EspError, cards.formation, packet, self.cat, self.models, self.map)
        first["escola"] = {"nome": "escola-a", "obras": ["obra-a"]}
        second.update(escola={"nome": "escola-b", "obras": ["obra-b"]}, motivo_escola="divergência relevante ao critério")
        self.assertTrue(cards.formation(packet, self.cat, self.models, self.map)["valida"])

    def test_council_uses_given_optics(self):
        f = self.ficha(role="conselheiro", step=3); f.update(template="evidencia", otica="metodo")
        critic = self.ficha(role="critico", number=2, step=3)
        packet = {"formacao": "conselho", "fichas": [f, critic], "itens_exigidos": [], "oticas": ["metodo"]}
        self.assertTrue(cards.formation(packet, self.cat, self.models, self.map)["valida"])
        packet["oticas"] = ["adversario"]
        self.assertRaises(core.EspError, cards.formation, packet, self.cat, self.models, self.map)


class LibraryTest(Setup):
    def library(self, root):
        p = Path(root); area = p / "esp-teste"; (area / "references").mkdir(parents=True)
        content = "---\nname: esp-teste\ndescription: Dublê de teste, sem conhecimento curado.\n---\n# Conteúdo\nCONHECIMENTO ORIGINAL\n"
        (area / "SKILL.md").write_text(content)
        (area / "references/modulo.md").write_text("MÓDULO INTEIRO\n")
        (area / "ORIGEM.md").write_text("Dublê de infraestrutura, não é curadoria validada.\n")
        def git(*args):
            return subprocess.check_output(["git", "-C", str(p), *args], stderr=subprocess.DEVNULL).decode().strip()
        git("init"); git("add", ".")
        git("-c", "user.name=Teste local", "-c", "user.email=teste@example.invalid", "commit", "-m", "fixture")
        git("tag", "esp-teste-v1")
        raw = bytearray()
        for path in ["esp-teste/SKILL.md", "esp-teste/references/modulo.md"]:
            b = (p/path).read_bytes(); raw.extend(path.encode()+b"\0"+str(len(b)).encode()+b"\0"+b)
        entry = {"id": "esp-teste", "versao": "1", "tag": "esp-teste-v1", "commit": git("rev-parse", "HEAD"),
                 "hash": hashlib.sha256(raw).hexdigest(), "escopo": "disciplina de teste", "situacao": "em_uso",
                 "valida_ate": "2027-10-23", "modulos": ["modulo"], "modelos_testados": ["modelo-nao-configurado"], "errata": []}
        return {"schema_version": 1, "especialidades": [entry]}, git

    def selected(self, catalog):
        f = self.ficha(); e = catalog["especialidades"][0]
        f.update(esp={k: e[k] for k in ("id", "versao", "hash")}, modulos=["modulo"])
        return f

    def test_reads_tag_not_dirty_worktree_and_preserves_full_module(self):
        with tempfile.TemporaryDirectory() as d:
            catalog, _ = self.library(d); f = self.selected(catalog)
            (Path(d)/"esp-teste/SKILL.md").write_text("EDITADO NO WORKTREE")
            result = brief.build(f, catalog, d)
            self.assertIn("CONHECIMENTO ORIGINAL", result["bloco"])
            self.assertIn("MÓDULO INTEIRO", result["bloco"])
            self.assertNotIn("EDITADO NO WORKTREE", result["bloco"])
            self.assertNotEqual(result["hash_biblioteca"], result["hash_conteudo"])

    def test_changed_tag_and_wrong_hash_are_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            catalog, git = self.library(d); entry = catalog["especialidades"][0]
            entry["hash"] = "0"*64
            self.assertRaises(core.EspError, cat.audit, d, entry)
            entry["hash"] = self.library_hash(d)
            (Path(d)/"novo.txt").write_text("novo")
            git("add", "."); git("-c", "user.name=Teste", "-c", "user.email=t@example.invalid", "commit", "-m", "novo")
            git("tag", "-f", "esp-teste-v1")
            self.assertRaises(core.EspError, cat.audit, d, entry)

    def library_hash(self, d):
        raw = bytearray()
        for path in ["esp-teste/SKILL.md", "esp-teste/references/modulo.md"]:
            b = (Path(d)/path).read_bytes(); raw.extend(path.encode()+b"\0"+str(len(b)).encode()+b"\0"+b)
        return hashlib.sha256(raw).hexdigest()

    def test_errata_changes_block_and_overrides_old_seal(self):
        with tempfile.TemporaryDirectory() as d:
            catalog, _ = self.library(d); f = self.selected(catalog)
            first = brief.build(f, catalog, d)
            catalog["especialidades"][0].update(situacao="em_revisao", errata=[{"id":"E1","em":"2026-10-23","texto":"correção conferida","fonte":"F1"}])
            second = brief.build(f, catalog, d)
            self.assertIn("correção conferida", second["bloco"])
            self.assertNotEqual(first["selo"], second["selo"])
            self.assertTrue(brief.seal_check(second, first["selo"]+"\nresposta")["refazer"])

    def test_transport_checks_actual_text_not_copied_hash(self):
        result = brief.build(self.ficha(), self.cat)
        self.assertFalse(brief.seal_check(result, result["selo"]+"\nResposta", result["bloco"]+"Tarefa")["refazer"])
        self.assertTrue(brief.seal_check(result, result["selo"]+"\nResposta", "Resumo do bloco. "+result["hash_transporte"])["refazer"])
        self.assertTrue(brief.seal_check(result, "\n"+result["selo"])["refazer"])

    def test_catalog_does_not_leak_score_and_marks_expiry_or_new_model(self):
        with tempfile.TemporaryDirectory() as d:
            catalog, _ = self.library(d); entry = catalog["especialidades"][0]
            entry["placar"] = {"SEGREDO_PLACAR": 999}
            self.assertNotIn("SEGREDO_PLACAR", json.dumps(cat.recruiting_view(catalog)))
            self.assertTrue(cat.audit(d, entry, today=date(2028,1,1))["a_retestar"])
            self.assertTrue(cat.audit(d, entry, model="modelo-novo")["a_retestar"])

    def test_external_markers_detected_without_echoing_closed_text(self):
        with tempfile.TemporaryDirectory() as d:
            catalog, _ = self.library(d); entry = catalog["especialidades"][0]
            result = cat.audit(d, entry, markers=["CONHECIMENTO ORIGINAL"])
            self.assertTrue(result["contaminacao"])
            self.assertNotIn("CONHECIMENTO ORIGINAL", json.dumps(result))
            self.assertFalse(cat.audit(d, entry)["sala_limpa_verificada"])

    def test_blocked_and_unknown_modules_do_not_produce_knowledge(self):
        with tempfile.TemporaryDirectory() as d:
            catalog, _ = self.library(d); f = self.selected(catalog)
            f["modulos"] = ["nao-existe"]
            self.assertRaises(core.EspError, brief.build, f, catalog, d)
            catalog["especialidades"][0]["situacao"] = "bloqueada"
            self.assertRaises(core.EspError, brief.build, self.selected(catalog), catalog, d)


class QueueAndAdmissionTest(Setup):
    def test_gap_priority_and_duplicate_request(self):
        queue = sample("primeira-leva.json")
        queue[2]["central_ou_principio"] = True
        self.assertEqual(gaps.next_gap(queue)["proxima"]["id"], queue[2]["id"])
        self.assertEqual(gaps.add(queue, queue[2]), queue)
        extra = copy.deepcopy(queue[2]); extra["pedidos"][0]["projeto"] = "outro"
        changed = gaps.add(queue, extra)
        self.assertEqual(len(changed[2]["pedidos"]), 2)
        self.assertEqual(len(queue[2]["pedidos"]), 1)

    def test_rejection_reason_and_admission_reference_are_required(self):
        queue = sample("primeira-leva.json")
        self.assertRaises(core.EspError, gaps.update, queue, {"id": queue[0]["id"], "situacao": "nao_entrou"})
        result = gaps.update(queue, {"id": queue[0]["id"], "situacao": "nao_entrou", "motivo": "empate no teste"})
        self.assertNotEqual(gaps.next_gap(result)["proxima"]["id"], queue[0]["id"])
        self.assertRaises(core.EspError, gaps.update, queue, {"id": queue[0]["id"], "situacao": "entrou", "motivo": "aceita"})

    def results(self, com=70, sem=60):
        problems = [{"id":f"P{i}","enunciado":"dublê: devolver o número sete","escopo":"dentro" if i<5 else "fora",
                     "variante_nova":i<3,"fonte_gabarito":"conta verificável do dublê","gabarito":{"tipo":"numero","min":7,"max":7}} for i in range(6)]
        return {"tipo":"nova","problemas":problems,"modelos_papeis":["modelo-papel"],"modelo_menor":"modelo-menor",
                "resultados":[{"modelo":m,"problema":p["id"],"condicao":c,"execucao":r,"acerto":com if c=="com" else sem}
                              for m in ["modelo-papel","modelo-menor"] for p in problems for c in ["com","sem"] for r in [1,2,3]]}

    def test_ten_points_enters_but_tie_or_incomplete_does_not(self):
        self.assertTrue(gate.gate(self.results())["admitir"])
        self.assertFalse(gate.gate(self.results(60,60))["admitir"])
        data = self.results(); data["resultados"].pop()
        self.assertRaises(core.EspError, gate.gate, data)

    def test_consistent_out_of_scope_regression_rejected_despite_average_gain(self):
        data = self.results(100,0)
        for r in data["resultados"]:
            if r["problema"] == "P5" and r["execucao"] <= 2:
                r["acerto"] = 0 if r["condicao"] == "com" else 100
        result = gate.gate(data)
        self.assertGreater(result["por_modelo"]["modelo-papel"]["ganho"], 10)
        self.assertFalse(result["admitir"])
        self.assertEqual(result["por_modelo"]["modelo-papel"]["piora_consistente"], ["P5"])

    def test_revision_compares_against_previous_not_without(self):
        data = self.results(); data["tipo"] = "revisao"
        for r in data["resultados"]:
            r["condicao"] = "nova" if r["condicao"] == "com" else "anterior"
        self.assertTrue(gate.gate(data)["admitir"])

    def test_suite_requires_new_variants_and_external_problems(self):
        data = self.results()
        for p in data["problemas"]: p["variante_nova"] = False
        self.assertRaises(core.EspError, gate.gate, data)
        data = self.results(); data["problemas"][-1]["escopo"] = "dentro"
        self.assertRaises(core.EspError, gate.gate, data)

    def test_rubric_requires_two_blind_reviewers(self):
        data = self.results(); data["problemas"][0]["gabarito"] = {"tipo":"rubrica"}
        self.assertRaises(core.EspError, gate.gate, data)
        for r in data["resultados"]:
            if r["problema"] == "P0": r.update(avaliadores=["J1","J2"],cego=True)
        self.assertTrue(gate.gate(data)["admitir"])

    def test_external_runner_withholds_ground_truth_and_runs_both_conditions(self):
        data = self.results(); data.pop("resultados")
        with tempfile.TemporaryDirectory() as d:
            runner = Path(d)/"stub.py"
            runner.write_text("import json,sys\np=json.load(sys.stdin)\nassert not set(p)&{'gabarito','fonte_gabarito','escopo','variante_nova'}\nprint(json.dumps({'modelo':p['modelo'],'modelo_verificado':True,'resposta':7 if p['material'] else 0}))\n")
            config = {"autorizado":True,"comando":[sys.executable,"-B",str(runner)],"bloco":"DUBLÊ, não esp curada"}
            result = gate.execute(data, config)
            self.assertEqual(len(result["resultados"]), 72)
            self.assertTrue(gate.gate(result)["admitir"])
            config["autorizado"] = False
            self.assertRaises(core.EspError, gate.execute, data, config)


class PortableTest(unittest.TestCase):
    def test_package_extracted_outside_repo_runs_coverage_and_no_skill_block(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); output=root/"especialistas.skill"
            result = subprocess.run([sys.executable,"-B",str(ROOT/"scripts/empacotar_skill.py"),"--skill",str(SKILL),"--destino",str(output)],capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            with zipfile.ZipFile(output) as z: z.extractall(root)
            skill=root/"especialistas"; model=skill/"assets/modelos"
            def run(name,*args):
                return subprocess.run([sys.executable,"-B",str(skill/"scripts"/name),*map(str,args)],cwd=root,capture_output=True,text=True)
            coverage=run("cobertura.py",model/"mapa.json")
            self.assertEqual(coverage.returncode,0,coverage.stderr)
            self.assertTrue(json.loads(coverage.stdout)["cobertura_completa"])
            new=run("fichas.py","novo",model/"ficha.json","--mapa",model/"mapa.json","--modelos",model/"modelos.json","--catalogo",model/"catalogo.json")
            self.assertEqual(new.returncode,0,new.stderr)
            ficha=root/"ficha.json"; ficha.write_text(new.stdout)
            block=run("brief_esp.py","montar","--ficha",ficha,"--catalogo",model/"catalogo.json")
            self.assertEqual(block.returncode,0,block.stderr)
            self.assertIn("sem skill",json.loads(block.stdout)["selo"])


if __name__ == "__main__":
    unittest.main()
