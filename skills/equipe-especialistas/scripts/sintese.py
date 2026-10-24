#!/usr/bin/env python3
"""Valida destinos, dissenso e lastro; não julga se uma versão é melhor."""
from __future__ import annotations
import argparse
import re
from equipe_core import array, cli, contributions, dump, index, load, no_verdict, refs, require, supported, text


def provenance(value,state):
    cs=contributions(state);destinations=index(value.get("destinos"))
    require(set(destinations)==set(cs),"Contribuição perdida ou destino inventado")
    for dest in destinations.values():
        require(dest.get("destino") in {"entrou","mudou","rejeitada","aberto"},"Destino inválido")
        text(dest.get("motivo"),"Motivo do destino")
        if dest.get("lastro"):
            supported(dest["lastro"],state)
    expected={(e["ator"],d["id"],d["argumento"]) for e in state["eventos"] if e["tipo"]=="posicao" for d in e["dissenso"]}
    preserved=set()
    for dissent in array(value.get("dissenso")):
        text(dissent.get("mudaria_se"))
        for side in array(dissent.get("argumentos")):
            preserved.add((side.get("ator"),dissent.get("id"),side.get("argumento")))
    require(expected<=preserved,"Dissenso final ou melhor argumento desapareceu")
    return destinations


def numbers(value,state):
    body=text(value.get("versao"),"Versão")
    declared=[]
    for number in array(value.get("numeros",[])):
        require(type(number.get("valor")) in {int,float},"Número deve ser explícito")
        supported(number.get("lastro"),state)
        text(number.get("motivo"))
        positions=number.get("entre_posicoes",[])
        if positions:
            require(all(type(v) in {int,float} for v in positions),"Posições numéricas inválidas")
            require(number.get("justificacao") in {"evidencia","opcoes"},"Meio-termo sem justificativa de evidência")
        declared.append(float(number["valor"]))
    # Exclui códigos; números factuais no corpo precisam de declaração/lastro.
    scrubbed=re.sub(r"\b[A-Z]+-?\d+(?:[.-]\d+)*\b","",body)
    for token in re.findall(r"(?<![\w])[-+]?\d+(?:[.,]\d+)?",scrubbed):
        require(float(token.replace(",",".")) in declared,"Número na versão sem lastro declarado")


def validate(value,state):
    require(isinstance(value,dict),"Síntese deve ser objeto")
    body=text(value.get("versao"));no_verdict(dump(value))
    provenance(value,state);numbers(value,state)
    for field in ("por_que","mudancas","lacunas","perguntas_usuario","do_lider"):
        array(value.get(field))
    opening=next((e for e in state["eventos"] if e["tipo"]=="abertura"),None)
    if opening:
        decisions=index(value.get("divergencias"))
        require(set(decisions)==set(index(opening["divergencias"])),"Divergência sem destino")
        for decision in decisions.values():
            require(decision.get("situacao") in {"resolvida","dissenso","opcoes"},"Divergência não encerrada")
            text(decision.get("motivo"))
            if decision["situacao"]=="resolvida":supported(decision.get("lastro"),state)
            else:text(decision.get("decidiria"))
    for addition in value["do_lider"]:
        require(addition.get("marcado") is True,"Conteúdo do líder precisa estar marcado")
        text(addition.get("texto"));supported(addition.get("lastro"),state)
    return {"valida":True,"destinos":len(value["destinos"]),"limite":"Rastreabilidade não comprova neutralidade, adequação do modelo científico ou ganho da reunião."}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("entrada");p.add_argument("--estado",required=True)
    a=p.parse_args();print(dump(validate(load(a.entrada),load(a.estado))),end="");return 0


if __name__=="__main__":cli(main)
