"""Primitivas do grill; nenhuma dependência da condutora ou de rede."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import unicodedata

VERSION = "0.1.0-alpha.1"
MODES = {"abertura", "desafio", "checagem"}
DOSES = {"leve", "padrao", "completa"}
CLASSES = {"fato do mundo", "fato pessoal", "decisao", "valor"}
VALUES = {"nulo": 0, "baixo": 1, "medio": 2, "alto": 3}


class GrillError(ValueError):
    """Falha de contrato sem reprodução de conteúdo privado no erro."""


def require(condition: object, message: str) -> None:
    if not condition:
        raise GrillError(message)


def fold(value: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", value.casefold())
                   if unicodedata.category(c) != "Mn")


def nonempty(value: object, name: str) -> str:
    require(isinstance(value, str) and bool(value.strip()), f"{name}: texto obrigatório")
    return value  # Nunca normalizar texto de usuário.


def identifier(value: object) -> str:
    require(isinstance(value, str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,99}", value)
            and value not in {".", ".."}, "Identificador inválido")
    return value


def objects(value: object) -> list:
    require(isinstance(value, list) and all(isinstance(x, dict) for x in value),
            "Esperada lista de objetos")
    return value


def indexed(value: object) -> dict:
    result = {}
    for entry in objects(value):
        key = identifier(entry.get("id"))
        require(key not in result, "Identificador duplicado")
        result[key] = entry
    return result


def digest(value: object) -> str:
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True,
                     separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def dump(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"


def checked_path(path: str | Path) -> Path:
    p = Path(path).absolute()
    require(not any(x.is_symlink() for x in (p, *p.parents)), "Caminho contém link simbólico")
    return p


def load(path: str | Path) -> object:
    p = checked_path(path)
    require(p.is_file() and p.stat().st_size <= 2_000_000, "Entrada ausente ou maior que 2 MB")
    def invalid_constant(_):
        raise GrillError("JSON não admite NaN ou infinito")
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, "Chave JSON duplicada")
            result[key] = value
        return result
    try:
        return json.loads(p.read_text(encoding="utf-8"), parse_constant=invalid_constant,
                          object_pairs_hook=unique_pairs)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise GrillError("JSON inválido") from exc


def run_cli(main) -> None:
    try:
        raise SystemExit(main())
    except (GrillError, OSError, UnicodeError) as exc:
        import sys
        # Não mostrar conteúdo de arquivos nem detalhes de exceções de SO.
        print("ERRO: " + (str(exc) if isinstance(exc, GrillError) else "Falha de leitura ou gravação"),
              file=sys.stderr)
        raise SystemExit(1)
