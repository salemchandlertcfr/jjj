#!/usr/bin/env python3
"""Dublê de pesquisa das avaliações: devolve premissas fixas, sem acessar rede."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path


FIXTURES = Path(__file__).resolve().parent


def pesquisar(cenario: str, *, modo: str = "refutar") -> dict:
    if modo not in {"refutar", "conferir"}:
        raise ValueError("O dublê só oferece os modos refutar e conferir.")
    cases = [json.loads(path.read_text(encoding="utf-8")) for path in FIXTURES.glob("[0-9][0-9]-*.json")]
    case = next((item for item in cases if item["cenario_id"] == cenario), None)
    if case is None:
        raise ValueError("Cenário não encontrado no banco controlado.")
    return {"modo": "duble-pesquisa-" + modo, "cenario": cenario,
            "fontes": copy.deepcopy(case["fontes_stub"]),
            "limites": "Premissas sintéticas de teste; nenhuma busca ou verificação de fonte externa foi executada."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cenario", required=True)
    parser.add_argument("--modo", choices=("refutar", "conferir"), default="refutar")
    args = parser.parse_args()
    try:
        print(json.dumps(pesquisar(args.cenario, modo=args.modo), ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Erro: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
