#!/usr/bin/env python3
"""Monta bloco a partir da tag Git e confere transporte/selo sem reescrever conhecimento."""
from __future__ import annotations
import argparse
from html import escape
from catalogo import audit, catalog, snapshot
from esp_core import cli, dump, load, require, safe_path, sha, text

INSTRUCTION = ("Este é o conhecimento curado da especialidade da ficha. Onde divergir da memória, "
               "siga o texto e diga que divergiu. Ficha de fonte conferida no brief vale mais que este "
               "conhecimento: siga a ficha e aponte o trecho. Use o que serve à tarefa.")


def build(ficha, cat, repo=None):
    # A ficha completa precisa ter passado em fichas.py antes da montagem.
    entries = catalog(cat)
    esp = ficha.get("esp")
    if esp is None:
        gap = text(ficha.get("lacuna"), "Lacuna")
        name = text(ficha.get("especialidade"), "Especialidade pedida")
        seal = f"sem skill · {gap}"
        block = (f'<especialidade nome="nenhuma" pedida="{escape(name, quote=True)}" lacuna="{escape(gap, quote=True)}">\n'
                 '<instrucao>Não há conhecimento curado desta especialidade. Marque "conhecimento geral, sem fonte" '
                 'em toda afirmação central sem ficha de fonte do brief e diga que fonte a conferiria. '
                 f'Comece a entrega pela linha: {seal}</instrucao>\n</especialidade>\n')
        return {"bloco": block, "selo": seal, "hash_transporte": sha(block.encode()), "a_retestar": False}
    require(isinstance(esp, dict) and esp.get("id") in entries, "esp fora do catálogo")
    entry = entries[esp["id"]]
    require(entry["situacao"] in {"em_uso", "em_revisao"}, "esp indisponível")
    require(esp == {k: entry[k] for k in ("id", "versao", "hash")}, "Versão/hash não é a do catálogo")
    require(repo, "Selecione o repositório da biblioteca")
    checks = audit(repo, entry, model=ficha.get("modelo", {}).get("id"))
    contents = snapshot(repo, entry)
    main = contents[f"{entry['id']}/SKILL.md"]
    body = main[4:].split("\n---\n", 1)[1]
    modules = ficha.get("modulos")
    require(isinstance(modules, list) and len(set(modules)) == len(modules)
            and set(modules) <= set(entry["modulos"]), "Módulo não autorizado")
    # Ordem canônica da versão, não a ordem acidental da ficha.
    selected = [m for m in entry["modulos"] if m in modules]
    payload = f"<instrucao>{INSTRUCTION}</instrucao>\n<conteudo>\n{body}\n</conteudo>\n"
    for module in selected:
        value = contents[f"{entry['id']}/references/{module}.md"]
        payload += f'<modulo nome="{module}">\n{value}\n</modulo>\n'
    errata = "\n".join(f"{e['id']} · {e['em']} · {e['texto']} · fonte: {e['fonte']}" for e in entry.get("errata", []))
    payload += f"<errata>\n{errata}\n</errata>\n"
    # Hash do conteúdo selecionado e da errata; não inclui seu próprio atributo.
    content_hash = sha((entry["id"] + "\0" + entry["versao"] + "\0" + payload).encode())
    seal = f"{entry['id']}@{entry['versao']} · {content_hash}"
    block = (f'<especialidade nome="{entry["id"]}" versao="{escape(entry["versao"], quote=True)}" '
             f'hash="{content_hash}" modulos="{",".join(selected)}">\n'
             + payload + f"<selo>Comece a entrega pela linha: {seal}</selo>\n</especialidade>\n")
    require(len(block.split()) <= 8000, "Bloco completo ultrapassa 8.000 palavras")
    return {"bloco": block, "selo": seal, "hash_biblioteca": entry["hash"],
            "hash_conteudo": content_hash, "hash_transporte": sha(block.encode()),
            "a_retestar": checks["a_retestar"], "palavras": len(block.split())}


def seal_check(result, delivery, received=None):
    require(isinstance(delivery, str), "Entrega deve ser texto")
    first = delivery.splitlines()[0] if delivery.splitlines() else ""
    seal_ok = first == result["selo"]
    transport_ok = None if received is None else received.startswith(result["bloco"])
    return {"selo_correto": seal_ok, "transporte_conferido": transport_ok,
            "refazer": not seal_ok or transport_ok is False,
            "limite": "Selo não prova leitura, compreensão ou isolamento; transporte compara bytes no topo do brief."}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("acao", choices=["montar", "selo"]); p.add_argument("--ficha", required=True)
    p.add_argument("--catalogo", required=True); p.add_argument("--biblioteca")
    p.add_argument("--entrega"); p.add_argument("--recebido")
    a = p.parse_args(); result = build(load(a.ficha), load(a.catalogo), a.biblioteca)
    if a.acao == "selo":
        require(a.entrega, "Conferência exige entrega")
        result = seal_check(result, safe_path(a.entrega).read_text(), safe_path(a.recebido).read_text() if a.recebido else None)
    print(dump(result), end=""); return int(result.get("refazer") is True)


if __name__ == "__main__":
    cli(main)
