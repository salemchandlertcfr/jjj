#!/usr/bin/env python3
"""Consolida apenas métricas fornecidas, mantendo ausência como desconhecida."""
from __future__ import annotations
import argparse
import math
from equipe_core import cli, dump, load, require


def summarize(state):
    events=state["eventos"];result={"reuniao":state["pauta"]["id"],"chamadas_registradas":len(events),
                                  "sessoes_declaradas":len({m["sessao"] for m in state["membros"]}),
                                  "limite":"Eventos não são chamadas de API; não inferir tokens por caracteres ou créditos por chamadas."}
    for event in events:
        require(isinstance(event.get("metricas",{}),dict),"Métricas devem ser objeto")
    for field in ("tokens","segundos","creditos","contexto_mesa_tokens"):
        values=[];missing=0
        for event in events:
            value=event.get("metricas",{}).get(field)
            if value is None:missing+=1
            else:
                require(type(value) in {int,float} and math.isfinite(value) and value>=0,"Métrica negativa, booleana ou não finita")
                values.append(value)
        result[field]={"total":sum(values) if not missing else None,"conhecido":sum(values) if values else None,"eventos_sem_dado":missing}
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("entrada");a=p.parse_args()
    print(dump(summarize(load(a.entrada))),end="");return 0


if __name__=="__main__":cli(main)
