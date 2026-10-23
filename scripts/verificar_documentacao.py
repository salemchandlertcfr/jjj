#!/usr/bin/env python3
"""Confere links da documentação curada, índice e bytes das fontes; sem rede."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
ORIGINAIS = ROOT / "sources" / "originais"
IGNORADOS = {".git", ".venv", "__pycache__", "work"}
LINK = re.compile(r"\[[^\]\n]+\]\(([^)\n]+)\)")


def sem_blocos(texto: str) -> str:
    linhas = []
    cerca = None
    for linha in texto.splitlines():
        marca = re.match(r"^\s*(`{3,}|~{3,})", linha)
        if marca:
            atual = marca.group(1)
            if cerca is None:
                cerca = atual
            elif atual[0] == cerca[0] and len(atual) >= len(cerca):
                cerca = None
            continue
        if cerca is None:
            linhas.append(linha)
    return "\n".join(linhas)


def ancoras(texto: str) -> set[str]:
    vistos: dict[str, int] = {}
    resultado = set()
    for titulo in re.findall(r"^#{1,6}\s+(.+)$", sem_blocos(texto), re.MULTILINE):
        titulo = re.sub(r"\s+#+\s*$", "", titulo)
        titulo = re.sub(r"<[^>]+>", "", titulo)
        titulo = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", titulo)
        base = re.sub(r"[^\w\- ]", "", titulo.lower()).replace(" ", "-")
        numero = vistos.get(base, 0)
        vistos[base] = numero + 1
        resultado.add(base if numero == 0 else f"{base}-{numero}")
    return resultado


def main() -> int:
    erros: list[str] = []
    paginas = sorted(
        p for p in ROOT.rglob("*.md")
        if not (set(p.relative_to(ROOT).parts) & IGNORADOS)
        and not p.is_relative_to(ORIGINAIS)
    )
    destinos: dict[Path, set[Path]] = {}
    links_locais = 0
    for pagina in paginas:
        destinos[pagina] = set()
        texto = sem_blocos(pagina.read_text(encoding="utf-8"))
        for alvo in LINK.findall(texto):
            alvo = alvo.strip()
            if alvo.startswith("<") and alvo.endswith(">"):
                alvo = alvo[1:-1]
            url = urlsplit(alvo)
            if url.scheme or url.netloc:
                continue
            links_locais += 1
            caminho = (pagina.parent / unquote(url.path)).resolve() if url.path else pagina
            origem = pagina.relative_to(ROOT)
            if not caminho.is_relative_to(ROOT):
                erros.append(f"{origem}: link fora do repositório: {alvo}")
                continue
            destinos[pagina].add(caminho)
            if not caminho.exists():
                erros.append(f"{origem}: destino ausente: {alvo}")
            elif url.fragment and caminho.suffix == ".md":
                if unquote(url.fragment) not in ancoras(caminho.read_text(encoding="utf-8")):
                    erros.append(f"{origem}: âncora ausente: {alvo}")

    indice = ROOT / "wiki" / "index.md"
    for pagina in sorted((ROOT / "wiki").glob("*.md")):
        if pagina != indice and pagina not in destinos.get(indice, set()):
            erros.append(f"Página fora do índice: {pagina.relative_to(ROOT)}")

    fontes = []
    registradas: set[Path] = set()
    ids = set()
    try:
        manifesto = json.loads((ROOT / "sources" / "manifest.json").read_text(encoding="utf-8"))
        fontes = manifesto["sources"]
        if not isinstance(fontes, list) or not fontes:
            raise ValueError("a lista sources precisa conter fontes")
        for fonte in fontes:
            for campo in ("id", "original_filename", "path", "sha256", "bytes"):
                if campo not in fonte:
                    raise ValueError(f"campo ausente na fonte: {campo}")
            identificador = fonte["id"]
            if identificador in ids:
                erros.append(f"ID de fonte duplicado: {identificador}")
            ids.add(identificador)
            caminho = (ROOT / fonte["path"]).resolve()
            if not caminho.is_relative_to(ORIGINAIS):
                erros.append(f"{identificador}: caminho fora de sources/originais")
                continue
            if caminho in registradas:
                erros.append(f"Fonte duplicada: {fonte['path']}")
            registradas.add(caminho)
            if not caminho.is_file():
                erros.append(f"{identificador}: arquivo ausente")
                continue
            dados = caminho.read_bytes()
            if len(dados) != fonte["bytes"] or hashlib.sha256(dados).hexdigest() != fonte["sha256"]:
                erros.append(f"{identificador}: tamanho ou SHA-256 divergente")
            inventario = ROOT / "sources" / "README.md"
            if caminho not in destinos.get(inventario, set()):
                erros.append(f"{identificador}: fonte fora do inventário")
        arquivos = {p.resolve() for p in ORIGINAIS.rglob("*") if p.is_file()}
        for caminho in sorted(arquivos - registradas):
            erros.append(f"Original não registrado: {caminho.relative_to(ROOT)}")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        erros.append(f"Manifesto inválido: {exc}")

    if erros:
        for erro in erros:
            print(f"ERRO: {erro}", file=sys.stderr)
        return 1
    palavras = sum(len(p.read_text(encoding="utf-8").split()) for p in paginas)
    print(f"OK: {len(paginas)} páginas curadas, {links_locais} links locais, "
          f"{len(fontes)} fontes íntegras; aproximadamente {palavras} palavras curadas.")
    print("Escopo: links/âncoras locais, índice, inventário e hashes. "
          "Sem checagem de URLs externas, fontes científicas ou eficácia do método.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
