#!/usr/bin/env python3
"""Separa autoria estrutural e rótulos públicos; não reescreve hipóteses."""
from __future__ import annotations

import argparse
import copy
import random
import re
import secrets

from _comum import CouncilError, dump_json, identifier, load_json, require, text
from valida_brief import AUTHORSHIP


PREFIX = re.compile(r"^\s*(?:(?:minha|nossa)\s+(?:vers[aã]o|hip[oó]tese|proposta)|(?:vers[aã]o|hip[oó]tese|proposta)\s+(?:da\s+IA|do\s+usu[aá]rio|de\s+(?:Claude|GPT|Gemini|ChatGPT)))\s*:\s*", re.I)


def anonymize(hipoteses: object, *, seed: int | None = None, normalizacao: dict | None = None) -> dict:
    require(isinstance(hipoteses, list) and 0 < len(hipoteses) <= 100, "Informe a lista de hipóteses de origem")
    if seed is None:
        seed = secrets.randbits(64)
    require(type(seed) is int and seed >= 0, "Semente privada deve ser inteiro não negativo")
    rng = random.Random(f"autoria:{seed}")
    ids = set()
    labels = set()
    public = []
    private = {}
    for hypothesis in hipoteses:
        require(isinstance(hypothesis, dict) and set(hypothesis) <= {"id", "texto", "origem", "autoria", "autor"}, "Hipótese de origem contém campos desconhecidos")
        original = identifier(hypothesis.get("id"), "ID de origem")
        require(original not in ids, "ID de origem duplicado")
        ids.add(original)
        body = text(hypothesis.get("texto"), "Hipótese")
        body = PREFIX.sub("", body, count=1).strip()
        require(body and not AUTHORSHIP.search(body), "Não foi possível retirar autoria sem mudar sentido; peça cartão fiel sem marcas")
        attribution = hypothesis.get("autoria", hypothesis.get("autor"))
        origin = hypothesis.get("origem", "nao-informada")
        require(attribution is None or isinstance(attribution, str), "Autoria estrutural deve ser texto ou null")
        require(isinstance(origin, str) and origin.strip(), "Origem estrutural deve ser texto")
        if attribution:
            require(attribution.casefold() not in body.casefold(), "A autoria persiste no texto; solicite correção na origem")
        label = "H-" + format(rng.getrandbits(40), "010x")
        while label in labels:
            label = "H-" + format(rng.getrandbits(40), "010x")
        labels.add(label)
        public.append({"id": label, "texto": body})
        private[label] = {"id_original": original, "origem": origin, "autoria": attribution}
    rng.shuffle(public)
    return {"hipoteses": public,
            "chave_privada": {"schema_version": 1, "semente": seed, "hipoteses": private},
            "normalizacao": copy.deepcopy(normalizacao)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("hipoteses", help="JSON privado: lista de id/texto/origem/autoria")
    parser.add_argument("--semente", type=int)
    args = parser.parse_args()
    try:
        print(dump_json(anonymize(load_json(args.hipoteses), seed=args.semente)), end="")
        return 0
    except (CouncilError, OSError, ValueError) as exc:
        parser.exit(2, f"Erro: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
