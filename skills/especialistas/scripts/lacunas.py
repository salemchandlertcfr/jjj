#!/usr/bin/env python3
"""Fila declarativa de curadoria. Devolve atualização; não grava na biblioteca."""
from __future__ import annotations
import argparse
import copy
from esp_core import array, cli, dump, functional, ident, index, iso_date, load, require, text

STATES = {"na_fila", "em_curadoria", "entrou", "nao_entrou"}


def validate(queue):
    entries = index(queue)
    for entry in entries.values():
        functional(entry.get("especialidade")); text(entry.get("para_que"))
        require(entry.get("situacao") in STATES, "Situação de lacuna inválida")
        require(type(entry.get("central_ou_principio")) is bool and type(entry.get("gabarito")) is bool, "Prioridade deve ser explícita")
        iso_date(entry.get("registrada_em"))
        require(bool(array(entry.get("pedidos"))), "Lacuna deve ter origem")
        for request in entry["pedidos"]:
            require(isinstance(request, dict), "Pedido de lacuna inválido")
            ident(request.get("projeto")); ident(request.get("subetapa")); ident(request.get("ficha"))
        if entry["situacao"] in {"entrou", "nao_entrou"}:
            text(entry.get("motivo"))
        if entry["situacao"] == "entrou":
            text(entry.get("esp")); text(entry.get("versao")); text(entry.get("teste"))
    return entries


def add(queue, incoming):
    validate([incoming]); current = validate(queue)
    result = copy.deepcopy(queue)
    previous = next((e for e in result if e["especialidade"] == incoming["especialidade"]), None)
    if previous:
        require(previous["id"] == incoming["id"], "Mesma especialidade deve manter ID estável")
        for request in incoming["pedidos"]:
            if request not in previous["pedidos"]:
                previous["pedidos"].append(copy.deepcopy(request))
        previous["central_ou_principio"] |= incoming["central_ou_principio"]
        previous["gabarito"] |= incoming["gabarito"]
    else:
        require(incoming["id"] not in current, "ID de lacuna já usado por outra especialidade")
        result.append(copy.deepcopy(incoming))
    return result


def next_gap(queue):
    values = list(validate(queue).values())
    def priority(e):
        return (-e["central_ou_principio"], -len({p["projeto"] for p in e["pedidos"]}),
                -len({(p["projeto"], p["subetapa"]) for p in e["pedidos"]}), -e["gabarito"], e["id"])
    waiting = sorted((e for e in values if e["situacao"] == "na_fila"), key=priority)
    return {"proxima": waiting[0] if waiting else None, "ordem": [e["id"] for e in waiting]}


def update(queue, change):
    result = copy.deepcopy(queue); entries = validate(result)
    require(change.get("id") in entries and change.get("situacao") in STATES, "Atualização inválida")
    entry = entries[change["id"]]
    require(set(change) <= {"id", "situacao", "motivo", "esp", "versao", "teste"}, "Atualização contém campos desconhecidos")
    entry.update(change); validate(result)
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("acao", choices=["novo", "proxima", "situacao"]); p.add_argument("fila"); p.add_argument("--entrada")
    a = p.parse_args(); queue = load(a.fila)
    if a.acao == "proxima":
        result = next_gap(queue)
    else:
        require(a.entrada, "Operação exige entrada")
        result = (add if a.acao == "novo" else update)(queue, load(a.entrada))
    print(dump(result), end=""); return 0


if __name__ == "__main__":
    cli(main)
