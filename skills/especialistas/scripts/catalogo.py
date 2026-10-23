#!/usr/bin/env python3
"""Consulta catálogo e audita texto fixado no Git, sem ler placar no recrutamento."""
from __future__ import annotations
import argparse
from datetime import date
import re
from esp_core import (array, cli, dump, fold, functional, git, ident, index, iso_date,
                      load, refs, require, sha, text)

STATES = {"em_teste", "em_uso", "em_revisao", "bloqueada", "aposentada"}


def catalog(value):
    require(isinstance(value, dict) and value.get("schema_version") == 1, "Catálogo versão 1 obrigatório")
    entries = index(value.get("especialidades"))
    for entry in entries.values():
        require(entry["id"].startswith("esp-"), "Nome de especialidade deve começar por esp-")
        text(entry.get("versao"), "Versão")
        ident(entry.get("tag"))
        functional(entry.get("escopo"))
        require(entry.get("situacao") in STATES, "Situação do catálogo inválida")
        require(isinstance(entry.get("commit"), str) and re.fullmatch(r"[a-f0-9]{40,64}", entry["commit"]), "Commit completo obrigatório")
        require(isinstance(entry.get("hash"), str) and re.fullmatch(r"[a-f0-9]{64}", entry["hash"]), "SHA-256 obrigatório")
        require(len(refs(entry.get("modulos"))) <= 3, "Máximo de três módulos")
        for module in entry["modulos"]:
            require(re.fullmatch(r"[a-z0-9][a-z0-9-]*", module), "Nome de módulo inválido")
        iso_date(entry.get("valida_ate"))
        refs(entry.get("modelos_testados", []))
        for erratum in index(entry.get("errata", [])).values():
            text(erratum.get("texto")); text(erratum.get("fonte")); iso_date(erratum.get("em"))
        require(entry["situacao"] != "em_revisao" or bool(entry.get("errata")), "Em revisão exige errata explícita")
    return entries


def snapshot(repo, entry):
    resolved = git(repo, "rev-parse", "--verify", f"refs/tags/{entry['tag']}^{{commit}}").decode().strip()
    require(resolved == entry["commit"], "Tag foi movida ou commit diverge do catálogo")
    paths = [f"{entry['id']}/SKILL.md", *[f"{entry['id']}/references/{m}.md" for m in entry["modulos"]]]
    contents, framed = {}, bytearray()
    for path in paths:
        # git show segue blobs simbólicos como texto; recuse seu modo antes da leitura.
        mode = git(repo, "ls-tree", entry["commit"], "--", path).decode().split(" ", 1)[0]
        require(mode == "100644" or mode == "100755", "Esperado arquivo regular na tag")
        raw = git(repo, "show", f"{entry['commit']}:{path}")
        require(len(raw) <= 160_000, "Texto da especialidade excede limite")
        contents[path] = raw.decode("utf-8")
        framed.extend(path.encode() + b"\0" + str(len(raw)).encode() + b"\0" + raw)
    require(sha(framed) == entry["hash"], "Hash da especialidade diverge do conteúdo Git")
    return contents


def audit(repo, entry, markers=None, today=None, model=None):
    contents = snapshot(repo, entry)
    main = contents[f"{entry['id']}/SKILL.md"]
    require(main.startswith("---\n") and "\n---\n" in main[4:], "Frontmatter da esp ausente")
    header, body = main[4:].split("\n---\n", 1)
    require(re.search(rf"^name: {re.escape(entry['id'])}$", header, re.M), "Nome da esp diverge do cabeçalho")
    fields = set(re.findall(r"^([a-z][a-z-]*):", header, re.M))
    require({"name", "description"} <= fields <= {"name", "description", "metadata", "license", "compatibility", "allowed-tools"}, "Campos fora do padrão aberto")
    require(len(main.splitlines()) <= 300, "SKILL.md ultrapassa 300 linhas")
    full = "\n".join(contents.values())
    require(len(full.split()) <= 8000, "Especialidade ultrapassa 8.000 palavras")
    require(not re.search(r"\bvoce e (?:um|uma)\b", fold(body)), "Conhecimento deve ser escrito sem persona")
    origin_path = f"{entry['id']}/ORIGEM.md"
    origin_mode = git(repo, "ls-tree", entry["commit"], "--", origin_path).decode().split(" ", 1)[0]
    require(origin_mode in {"100644", "100755"}, "ORIGEM.md precisa ser arquivo regular na tag")
    origin = git(repo, "show", f"{entry['commit']}:{origin_path}").decode()
    require(bool(origin.strip()), "ORIGEM.md obrigatório")
    hits = []
    for marker in array(markers or []):
        if fold(text(marker, "Marcador externo")) in fold(full + origin):
            # Não publicar o marcador do teste fechado.
            hits.append(sha(marker.encode())[:12])
    return {"integra": True, "contaminacao": hits, "sala_limpa_verificada": markers is not None,
            "a_retestar": iso_date(entry["valida_ate"]) < (today or date.today())
                          or bool(model and model not in entry.get("modelos_testados", [])),
            "limite": "Marcadores só detectam coincidência textual; origem e sala limpa exigem auditoria externa."}


def recruiting_view(value):
    return [{k: e[k] for k in ("id", "versao", "tag", "commit", "hash", "escopo", "situacao", "valida_ate", "modulos")}
            for e in catalog(value).values()]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("entrada"); p.add_argument("--biblioteca"); p.add_argument("--auditar", action="store_true")
    p.add_argument("--marcadores"); p.add_argument("--modelo")
    a = p.parse_args(); value = load(a.entrada)
    if not a.auditar:
        print(dump(recruiting_view(value)), end=""); return 0
    require(a.biblioteca, "Auditoria exige biblioteca Git explícita")
    entries = catalog(value)
    result = {k: audit(a.biblioteca, e, load(a.marcadores) if a.marcadores else None, model=a.modelo) for k, e in entries.items()}
    print(dump(result), end="")
    return int(any(r["contaminacao"] for r in result.values()))


if __name__ == "__main__":
    cli(main)
