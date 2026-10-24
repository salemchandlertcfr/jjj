#!/usr/bin/env python3
"""Confere IDs/doses contra índice explícito; não finge integração com condutora ausente."""
import argparse
import json
from pathlib import Path
import re
from mapa_core import cli, dump, require

EXPECTED = {f"2.{i}": "completa" if i in {2, 3, 5, 6} else "padrão" for i in range(1, 8)}


def check(cards, entries):
    blocks = re.findall(r"^### (2\.[1-7]) ([^\n]+)\n(.*?)(?=^### |\Z)", cards, re.M | re.S)
    require(len(blocks) == 7 and {b[0] for b in blocks} == set(EXPECTED), "Cartões exigem 2.1–2.7 únicos")
    if isinstance(entries, dict):
        entries = entries.get("subetapas")
    require(isinstance(entries, list), "Índice explícito exige lista/subetapas")
    selected = [s for s in entries if str(s.get("id", "")).startswith("2.")]
    require(len(selected) == 7 and {s.get("id") for s in selected} == set(EXPECTED), "Índice da condutora sem os sete IDs")
    for key, title, body in blocks:
        dose = re.search(r"^- dose: (.+)$", body, re.M)
        require(dose and dose[1] == EXPECTED[key], "Dose do cartão divergente")
        for field in ("pré-requisitos", "grill quer entender", "triagem", "pesquisa", "equipe e alternativas", "validação", "sai"):
            require(re.search(r"^- " + field + r": .+", body, re.M), "Campo ausente: " + field)
        entry = next(e for e in selected if e["id"] == key)
        normalize = lambda x: str(x).replace("padrao", "padrão").lower()
        require(normalize(entry.get("dose")) == EXPECTED[key], "Dose no índice divergente")
        require(entry.get("titulo") == title, "Título no índice divergente")
    require("### Validação integrada do tema 2" in cards and "sem trava" in cards, "Falta integração/sem trava")
    return {"valido": True, "cartoes": 7, "limite": "Conferência de IDs, títulos, doses e campos; mudanças metodológicas de S15 constam no registro de diferenças."}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--indice", required=True, type=Path)
    p.add_argument("--cartoes", type=Path, default=Path(__file__).resolve().parents[1] / "references/cartoes.md")
    a = p.parse_args(); print(dump(check(a.cartoes.read_text(), json.loads(a.indice.read_text()))), end="")


if __name__ == "__main__":
    raise SystemExit(cli(main))
