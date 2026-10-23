#!/usr/bin/env python3
"""Empacota a skill universal e verifica que seus links são autocontidos."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import zipfile

from verificar_documentacao import LINK, sem_blocos


def package(skill: Path, output: Path) -> int:
    skill = skill.resolve()
    main = skill / "SKILL.md"
    if not main.is_file():
        raise ValueError("SKILL.md ausente")
    source = main.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", source, re.DOTALL)
    if not match:
        raise ValueError("Frontmatter ausente")
    fields = set(re.findall(r"^([a-z][a-z-]*):", match.group(1), re.MULTILINE))
    if not {"name", "description"} <= fields:
        raise ValueError("name e description obrigatórios")
    if fields - {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}:
        raise ValueError("Campo fora do padrão aberto")
    if f"name: {skill.name}" not in match.group(1):
        raise ValueError("name deve corresponder à pasta")
    if len(source.splitlines()) > 250:
        raise ValueError("Revise SKILL.md: ultrapassou a faixa de 250 linhas deste projeto")
    files = []
    for path in sorted(skill.rglob("*")):
        if {"__pycache__", ".git", ".venv"} & set(path.parts):
            continue
        if path.is_symlink():
            raise ValueError("Pacotes não incluem links simbólicos")
        if not path.is_file() or path.suffix in {".pyc", ".pyo"}:
            continue
        if path.suffix == ".md":
            for target in LINK.findall(sem_blocos(path.read_text(encoding="utf-8"))):
                url = urlsplit(target)
                if url.scheme or url.netloc:
                    continue
                dest = (path.parent / unquote(url.path)).resolve() if url.path else path
                if not dest.is_relative_to(skill) or not dest.exists():
                    raise ValueError(f"Link não portável em {path.name}: {target}")
        files.append(path)
    output = output.resolve()
    if output.is_relative_to(skill):
        raise ValueError("Grave o pacote fora da pasta da skill")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, Path(skill.name) / path.relative_to(skill))
    return len(files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill", type=Path, default=Path(__file__).resolve().parents[1] / "skills/etapa-1-cir")
    parser.add_argument("--destino", type=Path, required=True)
    args = parser.parse_args()
    try:
        count = package(args.skill, args.destino)
        print(f"OK: {count} arquivos em {args.destino}")
        return 0
    except (OSError, ValueError) as exc:
        print(f"ERRO: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
