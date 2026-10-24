#!/usr/bin/env python3
"""Confere o mapa estruturado, cronologia Git opcional e desenha árvores sem julgá-las."""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import re
import subprocess

from mapa_core import array, cited, cli, dump, index, iso, load, loads, refs, require, text

CATEGORIES = {"definir", "localizar", "preparar", "confirmar", "executar", "monitorar", "modificar", "concluir"}
TESTS = {"palha_ao_vento", "aro", "arma_fumegante", "duplamente_decisivo", "nao_diagnostica"}
CLASSES = {"principio", "limite_hoje", "quebravel"}


def validate(value, git=None, ate="2.5"):
    from mapa_core import document, sources
    document(value)
    require(ate in {"2.1", "2.2", "2.3", "2.4", "2.5"}, "Sub-etapa inválida")
    text(value.get("job"), "Job")
    fs = sources(value)
    stages = index(value.get("etapas"))
    require(CATEGORIES <= {s.get("categoria") for s in stages.values()}, "Cobrir as oito categorias, inclusive não aplicáveis")
    for s in stages.values():
        text(s.get("texto"), "Etapa verbo/objeto")
        require(s.get("categoria") in CATEGORIES, "Categoria desconhecida")
        require(type(s.get("aplica")) is bool, "Etapa: aplica deve ser booleano")
        if not s["aplica"]:
            text(s.get("motivo"), "Etapa não aplicável: motivo")
        else:
            text(s.get("executor")); text(s.get("hoje"), "Modo atual")
            refs(s.get("fontes"), fs, nonempty=False)
            require(s["fontes"] or s.get("hipotese") is True, "Etapa sem fonte deve ser hipótese")
    for passage in array(value.get("passagens")):
        require(passage.get("de") in stages and passage.get("para") in stages, "Passagem fora do mapa")
        for field in ("o_que_passa", "o_que_se_perde"):
            text(passage.get(field), field)
    array(value.get("variacoes")); array(value.get("gambiarras"))
    pending = []
    if ate == "2.1":
        return {"valido": True, "ate": ate, "pendencias": pending}
    failures = index(value.get("falhas")); causes = index(value.get("causas"))
    parties = index(value.get("partes"))
    for party in parties.values():
        text(party.get("texto"), "Parte afetada")
    require(bool(failures), "Mapa precisa descrever falhas, mesmo com causa desconhecida")
    for f in failures.values():
        text(f.get("texto")); refs(f.get("etapas"), stages)
        require(type(f.get("central")) is bool, "Falha: central deve ser booleano")
        text(f.get("frequencia")); text(f.get("gravidade")); refs(f.get("partes"), parties)
        local = [c for c in causes.values() if c.get("falha") == f["id"]]
        if f["central"]:
            # A exceção é visível e não substitui a busca das rivais.
            exc = f.get("excecao_rivais")
            if len(local) < 2 or len({c.get("origem") for c in local}) < 2:
                require(isinstance(exc, dict), "Falha central exige duas causas de origens diferentes")
                for k in ("registro", "motivo", "busca_rivais", "dissenso", "observacao_que_resolveria"):
                    text(exc.get(k), "Exceção de rivais: " + k)
                require(f.get("causa_desconhecida") is True or len(local) == 1, "Exceção de rivais inválida")
            tree = f.get("arvore")
            require(isinstance(tree, dict), "Falha central exige árvore")
            tree_check(tree, {c['id']: c for c in local}, allow_empty=f.get("causa_desconhecida") is True)
    for c in causes.values():
        require(c.get("falha") in failures, "Causa aponta para falha ausente")
        text(c.get("texto")); text(c.get("origem"))
        require(c.get("situacao") in {"principal", "rival_viva", "pergunta"}, "Situação da causa obrigatória")
        chain = refs(c.get("cadeia"))
        require(len(chain) >= 2, "Causa exige cadeia de mecanismo")
        require(not re.search(r"erro humano|human error|força de vontade", chain[-1], re.I), "Erro humano não fecha cadeia")
        obs = c.get("previsoes")
        require(isinstance(obs, dict), "Previsões antes da busca obrigatórias")
        text(obs.get("se_verdadeira")); text(obs.get("se_falsa"))
        for field in ("pergunta_contra", "observacao_faltante", "mudaria_se"):
            text(c.get(field), field)
        searches = c.get("busca")
        require(isinstance(searches, dict), "Buscas separadas obrigatórias")
        text(searches.get("favor")); text(searches.get("contra"))
        require(searches["favor"] != searches["contra"], "Busca contra exige pesquisador separado")
        evidence = array(c.get("evidencias"))
        for e in evidence:
            require(e.get("teste") in TESTS, "Teste de evidência inválido")
            require(e.get("lado") in {"favor", "contra", "neutra"}, "Lado inválido")
            require(e.get("resultado") in {"passou", "falhou", "incerto"}, "Resultado inválido")
            cited(e.get("fontes"), fs)
            text(e.get("texto"))
        force_check(c, fs)
        if git is not None:
            history_check(c, git, fs)
        else:
            pending.append(c["id"] + ": cronologia Git não verificada")
    for loop in array(value.get("lacos", [])):
        refs(loop.get("nos"), set(causes) | set(failures))
        require(loop.get("sentido") in {"reforco", "equilibrio"}, "Laço exige sentido")
        cited(loop.get("fontes"), fs)
    if ate == "2.2":
        return {"valido": True, "ate": ate, "pendencias": pending}
    contradictions = index(value.get("contradicoes"))
    for c in contradictions.values():
        require(len(refs(c.get("parametros"))) == 2, "Contradição exige dois parâmetros")
        text(c.get("forma_fisica"))
        require(c.get("classe") in CLASSES, "Classe inválida")
        if c["classe"] == "principio":
            for field in ("lei", "conta", "parecer", "conselho"):
                text(c.get(field), "De princípio: " + field)
            cited(c.get("fontes"), fs)
            assumptions = array(c.get("premissas"))
            require(bool(assumptions), "De princípio exige premissas")
            for a in assumptions:
                text(a.get("texto")); cited(a.get("fontes"), fs)
                require(type(a.get("movel")) is bool, "Premissa móvel deve ser explícita")
            require(c.get("contraexemplo_valido") is False, "Prova com contraexemplo válido exige reexaminar premissas")
        elif c["classe"] == "limite_hoje":
            iso(c.get("data")); cited(c.get("fontes"), fs)
        elif c.get("lei"):
            text(c.get("premissa_que_falha"), "Quebrável com lei exige premissa que falha")
        if c.get("busca_prova") or c.get("busca_contraexemplo"):
            text(c.get("busca_prova")); text(c.get("busca_contraexemplo"))
            require(c["busca_prova"] != c["busca_contraexemplo"], "Prova e contraexemplo exigem pesquisadores distintos")
        else:
            require(False, "Faltam buscas de prova e contraexemplo")
    if ate == "2.3":
        return {"valido": True, "ate": ate, "pendencias": pending}
    projection = value.get("projecao")
    require(isinstance(projection, dict), "Projeção obrigatória")
    text(projection.get("classe_referencia")); text(projection.get("sua_versao"))
    cited(projection.get("fontes"), fs); text(projection.get("taxas_base"))
    horizons = array(projection.get("horizontes"))
    require(len(horizons) == 2 and len({h.get("prazo") for h in horizons}) == 2, "Dois horizontes distintos obrigatórios")
    for h in horizons:
        for k in ("prazo", "faixa", "partes", "ajuste_motivo"):
            text(h.get(k), "Horizonte: " + k)
    if ate == "2.4":
        return {"valido": True, "ate": ate, "pendencias": pending}
    for k in index(value.get("conhecimento")).values():
        text(k.get("texto")); text(k.get("se_falsa"))
        require(k.get("classe") in {"sabido", "incerto", "impossivel_saber"}, "Classe K inválida")
        if k["classe"] == "sabido":
            cited(k.get("fontes"), fs); text(k.get("trecho"))
            require(any(k["trecho"] in fs[f]["trecho"] for f in k["fontes"]), "Trecho K ausente da ficha")
        elif k["classe"] == "incerto":
            text(k.get("resolveria")); text(k.get("custo_investigar"))
        else:
            text(k.get("por_que"))
            require(k.get("natureza") in {"aleatorio", "inobservavel", "escolhas_futuras"}, "Limite técnico atual não é impossibilidade de saber")
    for a in index(value.get("analogias")).values():
        for k in ("funcao", "mapeamento"):
            text(a.get(k))
        require(a.get("distancia") in {"proxima", "moderada", "distante"}, "Distância da analogia obrigatória")
        cited(a.get("fontes"), fs)
    # Evita identidades colidindo na projeção para especialistas.
    keys = list(stages) + list(failures) + list(causes) + list(contradictions) + list(index(value.get("conhecimento"))) + list(index(value.get("partes")))
    require(len(keys) == len(set(keys)), "IDs devem ser únicos entre peças")
    return {"valido": True, "ate": ate, "pendencias": pending,
            "limite": "Estrutura válida não prova fontes, causalidade, cegamento ou aprovação humana."}


def tree_check(node, causes, seen=None, allow_empty=False):
    require(isinstance(node, dict), "Nó de árvore inválido")
    children = array(node.get("ramos"))
    require(bool(children) or allow_empty, "Árvore exige ramos ou causa desconhecida registrada")
    text(node.get("outras_causas"), "Ramo outras causas com peso/desconhecimento")
    seen = set() if seen is None else seen
    for branch in children:
        require(isinstance(branch, dict) and branch.get("causa") in causes, "Ramo aponta para causa desconhecida")
        require(branch["causa"] not in seen, "Ciclo ou causa repetida na árvore")
        seen.add(branch["causa"])
        require(branch.get("tipo") in {"unica", "ramo"}, "Marcar causa única ou ramo")
        if "ramos" in branch:
            tree_check(branch, causes, seen)


def force_check(c, fs):
    force = c.get("forca")
    require(force in {"forte", "media", "fraca", "hipotese"}, "Força inválida")
    text(c.get("motivo_forca"))
    if force == "hipotese":
        return
    cited(c.get("fontes_mecanismo"), fs)
    cited(c.get("fontes_dependencia"), fs)
    kind = c.get("tipo_dependencia")
    require(kind in {"controle", "sem_controle", "contexto_parecido", "relatos"}, "Correlação isolada não demonstra causa")
    require(any(e["teste"] != "nao_diagnostica" for e in c["evidencias"]), "Evidência não diagnóstica não aumenta força")
    if force == "forte":
        require(kind == "controle", "Força forte exige dependência medida com controle")
        require(any(e["teste"] in {"aro", "arma_fumegante", "duplamente_decisivo"} and e["resultado"] == "passou"
                    and e["lado"] == "favor" for e in c["evidencias"]), "Forte exige teste diagnóstico favorável")
        require(c.get("falha_igual_sem_causa") is False, "Forte exige busca contra sem falha igual na ausência")
    if force == "media":
        require(kind in {"controle", "sem_controle", "contexto_parecido"}, "Relatos não sustentam força média")
    require(not any(e["teste"] in {"aro", "duplamente_decisivo"} and e["resultado"] == "falhou"
                    and e["lado"] == "favor" for e in c["evidencias"]), "Teste necessário falhou: reexaminar a causa")
    require(c.get("falha_igual_sem_causa") is not True, "Falha persiste igual sem causa: reexaminar antes de admitir força")


def history_check(cause, root, current_sources):
    h = cause.get("historico")
    require(isinstance(h, dict), "Cronologia exige histórico Git")
    before, after = h.get("pre_registro"), h.get("busca")
    require(all(isinstance(x, str) and re.fullmatch(r"[a-f0-9]{40}", x) for x in (before, after)), "Use commits completos")
    require(before != after, "Pré-registro deve ser anterior à busca")
    path = h.get("arquivo")
    require(isinstance(path, str) and path and not path.startswith("-"), "Arquivo do histórico obrigatório")
    rel = PurePosixPath(path)
    require(not rel.is_absolute() and ".." not in rel.parts and "\\" not in path, "Caminho Git inválido")
    def git(*args):
        p = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, timeout=15)
        require(p.returncode == 0, "Não foi possível verificar histórico Git")
        return p.stdout
    git("merge-base", "--is-ancestor", before, after)
    first = loads(git("show", before + ":" + path)); last = loads(git("show", after + ":" + path))
    pre = index(first.get("causas"))[cause["id"]]; post = index(last.get("causas"))[cause["id"]]
    for k in ("previsoes", "cadeia", "pergunta_contra"):
        require(pre.get(k) == cause.get(k) == post.get(k), "Pré-registro alterado: " + k)
    require(not pre.get("evidencias"), "Previsões já continham resultados da busca")
    require(post.get("evidencias") == cause.get("evidencias"), "Busca não corresponde ao commit declarado")
    used = {f for e in cause["evidencias"] for f in e["fontes"]}
    require(used and used <= set(index(last.get("fontes"))), "Fichas ausentes do commit da busca")
    post_sources = index(last.get("fontes"))
    require(all(post_sources[k] == current_sources[k] for k in used), "Fichas atuais divergem do commit da busca")
    require(not used & set(index(first.get("fontes"))), "Fichas da busca já existiam no pré-registro")


def mermaid(value):
    # IDs e rótulos internos evitam injeção de sintaxe Mermaid.
    all_items = {**index(value.get("falhas", [])), **index(value.get("causas", []))}
    labels = {k: "N" + str(i) for i, k in enumerate(all_items)}
    lines = ["flowchart TD"]
    for k in all_items:
        label = re.sub(r'[^\w .-]', ' ', k + " " + all_items[k]["texto"])
        lines.append(f'  {labels[k]}["{label}"]')
    def walk(parent, node):
        other = 'O' + str(len(lines))
        weight = re.sub(r'[^\w .-]', ' ', node['outras_causas'])
        lines.append(f'  {other}["outras causas - {weight}"] --> {labels[parent]}')
        for b in node["ramos"]:
            lines.append(f'  {labels[b["causa"]]} --> {labels[parent]}')
            if "ramos" in b:
                walk(b["causa"], b)
    for f in value.get("falhas", []):
        if f.get("arvore"):
            walk(f["id"], f["arvore"])
    for loop in value.get("lacos", []):
        nodes = loop["nos"]
        for left, right in zip(nodes, nodes[1:] + nodes[:1]):
            lines.append(f'  {labels[left]} -. {loop["sentido"]} .-> {labels[right]}')
    return "\n".join(lines) + "\n"


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("entrada"); p.add_argument("--git", type=Path)
    p.add_argument("--ate", choices=["2.1", "2.2", "2.3", "2.4", "2.5"], default="2.5")
    p.add_argument("--mermaid", action="store_true")
    a = p.parse_args(); value = load(a.entrada)
    result = validate(value, a.git, a.ate)
    print(mermaid(value) if a.mermaid else dump(result), end="")


if __name__ == "__main__":
    raise SystemExit(cli(main))
