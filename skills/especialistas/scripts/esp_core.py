"""Contratos locais, sem execução de modelos ou acesso implícito ao dossiê."""
from __future__ import annotations
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import subprocess
import unicodedata

VERSION = "0.1.0-alpha.1"
DOSES = {"leve", "padrao", "completa"}


class EspError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise EspError(message)


def text(value, field="Texto"):
    require(isinstance(value, str) and value.strip(), f"{field}: texto obrigatório")
    return value


def ident(value):
    require(isinstance(value, str) and re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_.-]{0,99}", value)
            and value not in {".", ".."}, "Identificador inválido")
    return value


def array(value):
    require(isinstance(value, list), "Esperada lista")
    return value


def index(value):
    result = {}
    for entry in array(value):
        require(isinstance(entry, dict), "Esperado objeto na lista")
        key = ident(entry.get("id"))
        require(key not in result, "ID duplicado")
        result[key] = entry
    return result


def refs(value):
    result = array(value)
    for entry in result:
        ident(entry)
    require(len(set(result)) == len(result), "Referência duplicada")
    return result


def fold(value):
    return "".join(c for c in unicodedata.normalize("NFD", value.casefold()) if unicodedata.category(c) != "Mn")


def functional(value):
    value = text(value, "Especialidade funcional")
    require(value == value.lower(), "Especialidade deve ser funcional, em minúsculas; revise nomes próprios")
    require(not re.search(r"\b(?:phd|ph\.d|dr|dra|doutor|professor|harvard|stanford|mit|taleb|kahneman|renomad[oa]|melhor|universidade|instituto)\b|anos de experiencia|voce e", fold(value)),
            "Possível credencial, pessoa, instituição ou persona; use descrição funcional")
    return value


def iso_date(value):
    try:
        return date.fromisoformat(value)
    except (ValueError, TypeError) as exc:
        raise EspError("Data ISO YYYY-MM-DD obrigatória") from exc


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"


def safe_path(value):
    p = Path(value).absolute()
    require(not any(x.is_symlink() for x in (p, *p.parents)), "Não atravesse links simbólicos")
    return p


def load(value):
    p = safe_path(value)
    require(p.is_file() and p.stat().st_size <= 4_000_000, "Entrada ausente ou maior que 4 MB")
    def pairs(items):
        result = {}
        for k, v in items:
            require(k not in result, "Chave JSON duplicada")
            result[k] = v
        return result
    def constant(_):
        raise EspError("Número JSON não finito")
    try:
        return json.loads(p.read_text(encoding="utf-8"), object_pairs_hook=pairs, parse_constant=constant)
    except (json.JSONDecodeError, UnicodeError) as exc:
        raise EspError("JSON inválido") from exc


def git(repo, *args):
    root = safe_path(repo)
    result = subprocess.run(["git", "-C", str(root), *args], capture_output=True)
    require(result.returncode == 0, "Git não conseguiu ler o objeto solicitado")
    require(len(result.stdout) <= 1_000_000, "Objeto Git maior que 1 MB")
    return result.stdout


def cli(main):
    try:
        raise SystemExit(main())
    except (EspError, OSError, UnicodeError) as exc:
        import sys
        print("ERRO: " + (str(exc) if isinstance(exc, EspError) else "Falha de leitura ou execução local"), file=sys.stderr)
        raise SystemExit(1)
