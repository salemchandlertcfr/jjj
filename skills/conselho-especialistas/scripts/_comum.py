"""Primitivas locais do conselho. Sem dependência da condutora ou de serviços."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import ipaddress
import json
import math
from pathlib import Path
import re
from urllib.parse import urlsplit


MAX_BYTES = 2_000_000
VERSION = "0.1.0-alpha.1"


class CouncilError(Exception):
    """Erro verificável do protocolo, apresentado sem traceback pelas CLIs."""


def require(condition: object, message: str) -> None:
    if not condition:
        raise CouncilError(message)


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def canonical_hash(value: object) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True,
                         separators=(",", ":"), allow_nan=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def dump_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"


def _finite(value: object) -> None:
    if isinstance(value, float) and not math.isfinite(value):
        raise CouncilError("JSON não admite NaN ou infinito no protocolo")
    if isinstance(value, dict):
        for child in value.values():
            _finite(child)
    if isinstance(value, list):
        for child in value:
            _finite(child)


def load_json(path: str | Path) -> object:
    path = Path(path).expanduser()
    require(not any(p.is_symlink() for p in (path.absolute(), *path.absolute().parents)),
            "Entrada não pode atravessar links simbólicos")
    require(path.is_file(), "Entrada precisa ser arquivo JSON regular")
    require(path.stat().st_size <= MAX_BYTES, "Entrada JSON excede 2 MB")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        _finite(value)
        return value
    except (ValueError, OSError, UnicodeError) as exc:
        raise CouncilError("JSON inválido ou ilegível") from exc


def identifier(value: object, name: str = "ID") -> str:
    require(isinstance(value, str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,79}", value),
            f"{name} deve conter apenas letras, dígitos, ponto, hífen ou sublinhado")
    require(value not in {".", ".."}, f"{name} inválido")
    return value


def text(value: object, name: str) -> str:
    require(isinstance(value, str) and value.strip(), f"{name} precisa de texto não vazio")
    return value.strip()


def public_url(value: object) -> str:
    """Barreira sintática antes de circular; não resolve DNS nem prova publicidade."""
    value = text(value, "URL da fonte")
    try:
        parts = urlsplit(value)
        host = (parts.hostname or "").lower().rstrip(".")
        require(parts.scheme in {"http", "https"} and bool(host)
                and not parts.username and not parts.password,
                "Fonte exige URL pública HTTP(S), sem credencial")
        parts.port  # Também rejeita porta malformada sem ecoar a entrada.
    except ValueError as exc:
        raise CouncilError("URL de fonte malformada") from exc
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        address = None
    require(address is None or address.is_global,
            "Possível vazamento: fonte aponta para IP não global")
    require(host != "localhost" and (address is not None or "." in host) and not host.endswith((".local", ".internal")),
            "Possível vazamento: fonte aponta para endereço local ou interno")
    require(host not in {"notion.so", "notion.site"} and not host.endswith((".notion.so", ".notion.site")),
            "Possível vazamento: página de workspace não integra as fontes públicas autorizadas")
    return value
