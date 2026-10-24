"""Primitivas locais da reunião. Sem provedor, rede ou persistência implícita."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re
import unicodedata

VERSION = "0.1.0-alpha.1"
MODES = {"elaboracao", "verificacao", "integracao", "individual", "fusao", "avulso"}


class TeamError(ValueError):
    pass


def require(value, message):
    if not value:
        raise TeamError(message)


def text(value, name="Texto"):
    require(isinstance(value, str) and value.strip(), f"{name} obrigatório")
    return value


def ident(value):
    require(isinstance(value, str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,99}", value)
            and value not in {".", ".."}, "Identificador inválido")
    return value


def array(value):
    require(isinstance(value, list), "Esperada lista")
    return value


def index(value):
    result = {}
    for entry in array(value):
        require(isinstance(entry, dict), "Esperado objeto")
        key = ident(entry.get("id")); require(key not in result, "ID duplicado")
        result[key] = entry
    return result


def refs(value):
    items = array(value)
    for item in items:
        ident(item)
    require(len(set(items)) == len(items), "Referência duplicada")
    return items


def fold(value):
    return "".join(c for c in unicodedata.normalize("NFD", value.casefold()) if unicodedata.category(c) != "Mn")


def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+"\n"


def digest(value):
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()


def safe_path(value):
    p = Path(value).absolute()
    require(not any(x.is_symlink() for x in (p,*p.parents)), "Não atravesse links simbólicos")
    return p


def load(value):
    p = safe_path(value)
    require(p.is_file() and p.stat().st_size <= 8_000_000, "Entrada ausente ou maior que 8 MB")
    def pairs(values):
        d = {}
        for k,v in values:
            require(k not in d, "Chave JSON duplicada"); d[k] = v
        return d
    def constant(_):
        raise TeamError("JSON não admite NaN/infinito")
    try:
        return json.loads(p.read_text(),object_pairs_hook=pairs,parse_constant=constant)
    except (UnicodeError,json.JSONDecodeError) as exc:
        raise TeamError("JSON inválido") from exc


def visible(value, markers=None):
    """Triagem lexical, não reconhecimento completo de autoria ou contaminação."""
    normalized = fold(value)
    problems = []
    patterns = {"autoria":r"a sua versao|o usuario propos|versao do usuario|escrito pelo usuario",
                "modelo":r"\b(?:gpt-\d|claude (?:opus|sonnet|haiku)|gemini-\d|sou (?:o|um) modelo)"}
    for name, pattern in patterns.items():
        if re.search(pattern,normalized): problems.append(name)
    for marker in array(markers or []):
        if fold(text(marker)) in normalized:
            problems.append("marcador-"+digest(marker)[:12])
    return problems


def no_verdict(value):
    require(not re.search(r"recomendo|recomendamos|hipotese (?:aprovada|reprovada)|mais votad[oa]|por maioria|ranking|veredito\s*:",fold(value)),
            "Saída contém possível recomendação, voto ou veredito; revisão necessária")


def contributions(state):
    result = {}
    for event in state["eventos"]:
        for c in event.get("contribuicoes",[]):
            require(c["id"] not in result,"Contribuição duplicada")
            result[c["id"]] = {**c,"ator":event["ator"]}
    return result


def evidence_registry(state):
    registry = {}
    for source in state.get("fontes",[]):
        registry[source["id"]] = source.get("valida") is True and source.get("apoio_conferido") is True
    for event in state["eventos"]:
        if event["tipo"] == "checagem":
            for check in event["resultados"]:
                registry[check["id"]] = check.get("confere") is True
    return registry


def supported(references, state):
    ids = refs(references)
    registry = evidence_registry(state)
    require(bool(ids) and all(registry.get(k) is True for k in ids), "Lastro ausente, não conferido ou invalidado")
    return ids


def cli(main):
    try:
        raise SystemExit(main())
    except (TeamError,OSError,UnicodeError) as exc:
        import sys
        print("ERRO: "+(str(exc) if isinstance(exc,TeamError) else "Falha de leitura ou operação local"),file=sys.stderr)
        raise SystemExit(1)
