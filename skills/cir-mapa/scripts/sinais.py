#!/usr/bin/env python3
"""Triagem lexical contextual PT/EN para o crítico; sinal nunca é bloqueio ou veredito."""
import argparse
import json
from pathlib import Path
import re
from mapa_core import cli, dump


def scan(content, piece):
    lex = json.loads((Path(__file__).resolve().parents[1] / "assets/lexicos/sinais.json").read_text())
    hits = []
    for n, line in enumerate(content.splitlines(), 1):
        for rule in lex["regras"]:
            if piece not in rule["pecas"] or not re.search(rule["padrao"], line, re.I):
                continue
            if any(re.search(ex, line, re.I) for ex in rule.get("excecoes", [])):
                continue
            hits.append({"linha": n, "sinal": rule["id"], "revisar": rule["motivo"]})
    return {"peca": piece, "sinais": hits, "bloqueia": False,
            "limite": "Heurística por linha; não prova limpeza, indução, rivalidade substantiva nem verdade."}


def main():
    p = argparse.ArgumentParser(description=__doc__); p.add_argument("entrada", type=Path)
    p.add_argument("--peca", required=True, choices=["job", "falha", "causa", "contradicao", "projecao", "k", "caso"])
    a = p.parse_args(); print(dump(scan(a.entrada.read_text(encoding="utf-8"), a.peca)), end="")


if __name__ == "__main__":
    raise SystemExit(cli(main))
