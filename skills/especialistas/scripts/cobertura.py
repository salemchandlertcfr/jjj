#!/usr/bin/env python3
"""Cobertura por itens do problema; sugestão gulosa não usa disponibilidade ou placar."""
from __future__ import annotations
import argparse
from esp_core import array, cli, dump, functional, index, load, refs, require, text


def mapping(value):
    require(isinstance(value, dict) and value.get("schema_version") == 1, "Mapa versão 1 obrigatório")
    items, specialties = index(value.get("itens")), index(value.get("especialidades"))
    require(bool(items), "Mapa sem itens não demonstra cobertura")
    for item in items.values():
        require(item.get("tipo") in {"causa", "contradicao", "parte", "job"}, "Tipo de item inválido")
        text(item.get("texto"))
        for flag in ("central", "principio"):
            require(type(item.get(flag, False)) is bool, "Central/princípio devem ser booleanos")
    for spec in specialties.values():
        functional(spec.get("especialidade")); text(spec.get("por_que"))
        require(set(refs(spec.get("cobre"))) <= set(items), "Especialidade cobre item desconhecido")
        require(bool(spec["cobre"]), "Especialidade precisa cobrir item do problema")
        require(bool(refs(spec.get("fontes"))), "Ligação entre problema e disciplina exige fontes explícitas")
        if spec.get("esp") is None:
            text(spec.get("lacuna"), "Lacuna da especialidade sem skill")
    names = [s["especialidade"] for s in specialties.values()]
    require(len(set(names)) == len(names), "Especialidade duplicada no mapa")
    for theme in index(value.get("temas", [])).values():
        require(theme.get("critico") is True, "Equipe-base do tema exige crítico")
        require(bool(refs(theme.get("equipe_base"))) and set(theme["equipe_base"]) <= set(specialties), "Equipe-base fora do mapa")
        require(set(refs(theme.get("reserva", []))) <= set(specialties), "Reserva fora do mapa")
        distant = theme.get("distante")
        require(isinstance(distant, dict) and distant.get("especialidade") in specialties, "Tema exige uma distante identificada")
        text(distant.get("funcao_analoga"), "Função análoga do tema")
    if value.get("etapa") == "2.7":
        require(bool(value.get("temas")), "Mapa 2.7 exige equipes-base e distante por tema")
        dose = value.get("dose")
        require(dose in {"padrao", "completa"}, "Mapa inicial é leve; 2.7 exige padrão/completa")
        recruiters = refs(value.get("recrutadores"))
        generators = refs(value.get("geradores_distantes"))
        require(len(recruiters) == (2 if dose == "padrao" else 3)
                and len(generators) == (1 if dose == "padrao" else 2)
                and not set(recruiters) & set(generators), "Composição do mapa não corresponde à dose")
        text(value.get("fusao"), "Registro da fusão independente")
    return items, specialties


def coverage(value, chosen=None):
    items, specs = mapping(value)
    keys = list(specs) if chosen is None else refs(chosen)
    require(set(keys) <= set(specs), "Seleção fora do mapa")
    covered = {key: [s for s in keys if key in specs[s]["cobre"]] for key in items}
    missing = [k for k, v in covered.items() if not v]
    return {"cobertura": covered, "sem_cobertura": missing,
            "centrais_sem_cobertura": [k for k in missing if items[k].get("central") or items[k].get("principio")],
            "cobertura_completa": not missing,
            "lacunas": sorted({specs[k]["lacuna"] for k in keys if specs[k].get("esp") is None})}


def suggest(value, limit):
    require(type(limit) is int and limit > 0, "Limite positivo obrigatório")
    items, specs = mapping(value)
    missing, chosen = set(items), []
    while missing and len(chosen) < limit:
        gains = {k: sum(3 if items[i].get("central") or items[i].get("principio") else 1
                        for i in set(s["cobre"]) & missing) for k, s in specs.items() if k not in chosen}
        if not gains or max(gains.values()) == 0:
            break
        key = sorted(gains, key=lambda k: (-gains[k], k))[0]
        chosen.append(key); missing.difference_update(specs[key]["cobre"])
    return {"sugeridas": chosen, "reserva": [k for k in specs if k not in chosen],
            **coverage(value, chosen), "regra": "peso 3 para central/princípio, 1 para demais; empate por ID, sem placar ou catálogo"}


def compare(left, right):
    li, ls = mapping(left); ri, rs = mapping(right)
    require(li == ri, "Comparar exige o mesmo problema e itens")
    lnames = {s["especialidade"] for s in ls.values()}; rnames = {s["especialidade"] for s in rs.values()}
    return {"so_primeiro": sorted(lnames-rnames), "so_segundo": sorted(rnames-lnames),
            "primeiro": coverage(left), "segundo": coverage(right),
            "limite": "A fusão precisa justificar cada diferença; comparação não aprova mapa nem decide por usuário."}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("entrada"); g = p.add_mutually_exclusive_group()
    g.add_argument("--sugerir", type=int, metavar="LIMITE"); g.add_argument("--comparar")
    a = p.parse_args(); value = load(a.entrada)
    result = suggest(value, a.sugerir) if a.sugerir is not None else compare(value, load(a.comparar)) if a.comparar else coverage(value)
    print(dump(result), end="")
    return int(result.get("cobertura_completa") is False)


if __name__ == "__main__":
    cli(main)
