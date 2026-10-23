#!/usr/bin/env python3
"""Valida uma mensagem de perguntas e calcula a fronteira de um mapa explícito."""
from __future__ import annotations

import argparse
from pathlib import Path
import re

from grill_core import (CLASSES, DOSES, MODES, VALUES, GrillError, dump, fold,
                        indexed, load, nonempty, objects, require, run_cli)

TYPES = {"esclarecimento", "suposicao", "evidencia", "alternativa", "consequencia",
         "e se", "contraexemplo", "limite teorico"}


def frontier(nodes: list) -> list:
    by_id = indexed(nodes)
    visiting, done = set(), set()
    def visit(key):
        require(key not in visiting, "Mapa contém ciclo")
        if key in done:
            return
        visiting.add(key)
        node = by_id[key]
        require(node.get("classe") in CLASSES and node.get("valor") in VALUES,
                "Nó sem classe ou valor válido")
        require(node.get("estado") in {"pendente", "respondido", "descartado"}, "Estado de nó inválido")
        nonempty(node.get("impacto"), "Impacto na decisão")
        if node["estado"] == "descartado":
            nonempty(node.get("motivo"), "Motivo do descarte")
        deps = node.get("depende_de", [])
        require(isinstance(deps, list) and all(isinstance(d, str) and d in by_id for d in deps),
                "Dependência ausente do mapa")
        for dep in deps:
            visit(dep)
        visiting.remove(key)
        done.add(key)
    for key in by_id:
        visit(key)
    return sorted((n for n in nodes if n["estado"] == "pendente"
                   and n["classe"] != "fato do mundo" and VALUES[n["valor"]] > 0
                   and all(by_id[d]["estado"] == "respondido" for d in n.get("depende_de", []))),
                  key=lambda n: (-VALUES[n["valor"]], n["id"]))


def rules() -> list:
    """A tabela mantida em indutoras.md é a fonte das regras léxicas."""
    text = (Path(__file__).resolve().parents[1] / "references/indutoras.md").read_text()
    match = re.search(r"```json\n(.*?)\n```", text, re.S)
    require(match, "Tabela de padrões ausente")
    import json
    return json.loads(match.group(1))


def lint(text: str, reflection: bool, estimate: bool, opening: bool) -> tuple[list, list]:
    normalized = fold(text)
    errors, warnings = [], []
    for rule in rules():
        if rule.get("so_reflexao") and not reflection:
            continue
        if rule.get("so_abertura") and not opening:
            continue
        if re.search(rule["regex"], normalized):
            (errors if rule["nivel"] == "erro" else warnings).append(rule["id"])
    if estimate and re.search(r"\d|\b(?:dez|vinte|trinta|cem|mil|metade|dobro)\b", normalized):
        errors.append("ancora-numerica")
    return errors, warnings


def render(questions: list, bases: dict) -> str:
    blocks = []
    for i, q in enumerate(questions, 1):
        prefix = f"{i}. " if len(questions) > 1 else ""
        base = " · ".join(f"{key}: {bases[key]['texto']}" for key in q["base"])
        blocks.append(f"{prefix}**{q['id']} · {q['tipo']}**\n{q['texto']}\n"
                      f"Base: {base}\nPor que importa: {q['motivo']}")
        if q.get("retoma"):
            blocks[-1] += f"\nRetoma: {q['retoma']} · {q['motivo_retomada']}"
    return "\n\n".join(blocks)


def validate(packet: dict, source_index: dict | None = None) -> dict:
    require(isinstance(packet, dict), "Envelope deve ser objeto")
    require(packet.get("schema_version") == 1, "Versão do envelope inválida")
    require(packet.get("modo") in MODES and packet.get("dose") in DOSES, "Modo ou dose inválida")
    nonempty(packet.get("objetivo"), "Objetivo")
    bases = indexed(packet.get("bases", []))
    questions = objects(packet.get("perguntas"))
    indexed(questions)
    require(1 <= len(questions) <= 3, "Mensagem deve ter de uma a três perguntas")
    opening = packet["modo"] == "abertura"
    errors, warnings = [], []
    nodes = objects(packet.get("mapa"))
    require(bool(nodes), "Mapa decisório obrigatório")
    available = frontier(nodes)
    available_ids = {n["id"] for n in available}
    selected = set()
    history = indexed(packet.get("anteriores", []))
    for q in questions:
        require(q.get("tipo") in TYPES and q.get("genero") in {"reflexao", "logistica"},
                "Tipo ou gênero da pergunta inválido")
        require(q.get("valor") in VALUES and VALUES[q["valor"]] > 0, "Pergunta sem valor decisório")
        reflection = q["genero"] == "reflexao"
        require(not reflection or len(questions) == 1, "Reflexão exige uma pergunta por mensagem")
        require(type(q.get("estimativa", False)) is bool, "Estimativa deve ser booleana")
        text = nonempty(q.get("texto"), "Pergunta")
        nonempty(q.get("motivo"), "Motivo")
        require(text.count("?") == 1, "Pergunta deve conter uma única interrogação")
        require(isinstance(q.get("base"), list) and q["base"], "Base obrigatória")
        for key in q["base"]:
            require(isinstance(key, str) and key in bases, "Base inexistente")
            base = bases[key]
            require(base.get("tipo") in {"cartao", "dossie", "resposta", "ficha", "pedido"}, "Tipo de base inválido")
            nonempty(base.get("texto"), "Trecho da base")
            nonempty(base.get("origem"), "Origem da base")
            if base["tipo"] == "ficha":
                require(isinstance(source_index, dict) and key in source_index, "Ficha ausente do índice autorizado")
                src = source_index[key]
                require(isinstance(src, dict) and src.get("valida") is True, "Ficha inválida")
                require(type(src.get("forca")) is int and 1 <= src["forca"] <= 5, "Força deve ser de 1 a 5")
                require(src.get("apoio") in {"conferido", "nao conferido"}, "Estado do apoio obrigatório")
                require(base["texto"] in nonempty(src.get("trecho"), "Trecho autorizado"), "Base diverge da ficha")
                require(not opening or src.get("visao_geral") is True, "Abertura só aceita ficha de visão geral")
                require(f"força {src['forca']}" in text.casefold() or f"forca {src['forca']}" in text.casefold(),
                        "Pergunta deve mostrar a força da ficha")
                if src["apoio"] == "nao conferido":
                    require("apoio nao conferido" in fold(text), "Apoio não conferido deve aparecer")
        attempts = q.get("tentativas_reprovadas", 0)
        require(type(attempts) is int and attempts >= 0, "Contagem de reprovações inválida")
        if attempts >= 2:
            errors.append("duas-reprovacoes")
        # O chamador declara estimativa; a heurística cobre omissões comuns.
        estimate = q.get("estimativa", False) or bool(re.search(
            r"\b(?:quantos?|quantas?|porcentagem|percentual|frequencia|estime|estimativa)\b", fold(text)))
        e, w = lint(text, reflection, estimate, opening)
        errors.extend(e)
        warnings.extend(w)
        if estimate:
            displayed_context = q["motivo"] + " " + " ".join(bases[k]["texto"] for k in q["base"])
            context_errors, _ = lint(displayed_context, reflection, True, opening)
            errors.extend(context_errors)
        for old in history.values():
            old_text = nonempty(old.get("texto"), "Texto de pergunta anterior")
            if fold(old_text).strip() == fold(text).strip():
                require(q.get("retoma") == old["id"] and bool(q.get("motivo_retomada")),
                        "Pergunta repetida sem citar a anterior e o contexto alterado")
        if q.get("retoma"):
            require(q["retoma"] in history, "Retomada sem pergunta anterior fornecida")
            nonempty(q.get("motivo_retomada"), "Motivo da retomada")
        if nodes:
            node_id = q.get("no")
            require(node_id in available_ids and node_id not in selected, "Pergunta fora da fronteira")
            selected.add(node_id)
            require(q["valor"] == next(n["valor"] for n in available if n["id"] == node_id),
                    "Valor diverge do mapa")
    if nodes:
        chosen = [VALUES[n["valor"]] for n in available if n["id"] in selected]
        rest = [VALUES[n["valor"]] for n in available if n["id"] not in selected]
        require(not rest or min(chosen) >= max(rest), "Existe pergunta disponível de maior valor")
        require(not any(d in selected for n in available if n["id"] in selected for d in n.get("depende_de", [])),
                "Rodada contém perguntas dependentes")
    canonical = render(questions, bases)
    message = packet.get("mensagem", canonical)
    require(message == canonical, "Mensagem diverge da renderização conferida; não acrescente elogios ou alternativas")
    # Também confere base e motivo exibidos, que podem induzir fora da pergunta.
    e, w = lint(message, any(q["genero"] == "reflexao" for q in questions), False, opening)
    errors.extend(e)
    # Conjunções no cartão/base não transformam uma pergunta simples em dupla.
    # Essa suspeita é calculada só sobre o texto de cada pergunta.
    warnings.extend(x for x in w if x != "pergunta-dupla")
    warnings = sorted(set(warnings))
    justifications = packet.get("justificativas", {})
    require(isinstance(justifications, dict), "Justificativas devem ser objeto")
    unresolved = [w for w in warnings if not isinstance(justifications.get(w), str) or not justifications[w].strip()]
    return {"aprovada": not errors and not unresolved, "erros": sorted(set(errors)),
            "suspeitas": warnings, "pendentes": unresolved, "mensagem": message,
            "limite": "Triagem estrutural e lexical; requer revisão semântica da condutora."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entrada", help="Envelope de perguntas JSON")
    parser.add_argument("--indice", help="Índice JSON de fichas autorizado pela condutora")
    parser.add_argument("--fronteira", action="store_true", help="Entrada é uma lista de nós")
    args = parser.parse_args()
    value = load(args.entrada)
    if args.fronteira:
        print(dump(frontier(objects(value))), end="")
        return 0
    result = validate(value, load(args.indice) if args.indice else None)
    print(dump(result), end="")
    return 0 if result["aprovada"] else 1


if __name__ == "__main__":
    run_cli(main)
