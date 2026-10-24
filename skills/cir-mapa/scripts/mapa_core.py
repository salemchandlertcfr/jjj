"""Contratos locais v1. Não pesquisa, não julga mérito e não grava no dossiê."""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path


class Invalid(ValueError):
    pass


def require(test, message):
    if not test:
        raise Invalid(message)


def text(value, name="Texto"):
    require(isinstance(value, str) and bool(value.strip()), name + " obrigatório")
    require(value.strip().lower() not in {"…", "...", "pendente", "a preencher"}, name + " pendente")
    return value


def array(value):
    require(isinstance(value, list), "Lista obrigatória")
    return value


def index(value):
    result = {}
    for item in array(value):
        require(isinstance(item, dict), "Item deve ser objeto")
        key = text(item.get("id"), "ID")
        require(re.fullmatch(r"[A-Za-z0-9_.-]+", key) is not None, "ID inválido")
        require(key not in result, "ID duplicado: " + key)
        result[key] = item
    return result


def refs(value, known=None, nonempty=True):
    value = array(value)
    require(not nonempty or bool(value), "Referências obrigatórias")
    require(all(isinstance(x, str) for x in value), "Referência deve ser texto")
    require(len(value) == len(set(value)), "Referência duplicada")
    if known is not None:
        require(set(value) <= set(known), "Referência desconhecida")
    return value


def iso(value):
    text(value, "Data ISO")
    try:
        require(date.fromisoformat(value).isoformat() == value, "Data não canônica")
    except ValueError as exc:
        raise Invalid("Data ISO inválida") from exc
    return value


def document(value):
    require(isinstance(value, dict) and type(value.get("schema_version")) is int
            and value["schema_version"] == 1, "Objeto schema_version 1 obrigatório")
    return value


def loads(raw):
    if raw.lstrip().startswith("{"):
        value = json.loads(raw)
    else:
        blocks = re.findall(r"^```json cir-mapa-v1\s*\n(.*?)^```\s*$", raw, re.M | re.S)
        require(len(blocks) == 1, "Markdown exige um bloco json cir-mapa-v1; não se valida prosa livre")
        value = json.loads(blocks[0])
    return document(value)


def load(path):
    return loads(Path(path).read_text(encoding="utf-8"))


def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"


def markdown(title, value):
    return "# " + title + "\n\n```json cir-mapa-v1\n" + dump(value) + "```\n"


def sources(value):
    result = index(value.get("fontes"))
    for f in result.values():
        for field in ("referencia", "trecho", "afirmacao"):
            text(f.get(field), "Fonte: " + field)
        iso(f.get("data"))
        require(type(f.get("conferida")) is bool, "Fonte: conferida deve ser booleano")
    return result


def cited(ids, known):
    refs(ids, known)
    require(all(known[k]["conferida"] for k in ids), "Fonte ainda não conferida")


def cli(main):
    try:
        return main() or 0
    except (Invalid, OSError, ValueError, KeyError, TypeError) as exc:
        print("ERRO: " + str(exc), file=sys.stderr)
        return 1
