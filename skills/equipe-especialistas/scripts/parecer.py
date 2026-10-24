#!/usr/bin/env python3
"""Valida parecer técnico e integração, sem decisão sobre hipótese."""
from __future__ import annotations
import argparse
from equipe_core import array, cli, dump, index, load, no_verdict, refs, require, supported, text
from sintese import provenance


def validate(value,state):
    require(isinstance(value,dict),"Relatório deve ser objeto")
    # Examina toda a saída técnica, inclusive campos paralelos à conclusão.
    no_verdict(dump(value));provenance(value,state)
    mode=state["pauta"]["modo"]
    if mode=="verificacao":
        expected=index(state["pauta"]["afirmacoes"]);actual=index(value.get("afirmacoes"))
        require(set(expected)==set(actual),"Parecer deve cobrir todas as afirmações prévias")
        for claim in actual.values():
            require(claim.get("conclusao") in {"sustenta","nao_sustenta","indeterminado"},"Conclusão é técnica, sem veredito")
            for field in ("justificativa","incerteza","especialidade","mudaria_se"):text(claim.get(field))
            if claim["conclusao"]!="indeterminado":supported(claim.get("lastro"),state)
            else:array(claim.get("lastro",[]))
    elif mode=="integracao":
        outputs=index(state["pauta"]["saidas_aprovadas"])
        for conflict in index(value.get("conflitos")).values():
            require(conflict.get("gravidade") in {"bloqueia","pede_ajuste","menor"},"Gravidade inválida")
            require(len(refs(conflict.get("saidas")))>=2 and set(conflict["saidas"])<=set(outputs),"Conflito sem saídas de origem")
            text(conflict.get("texto"));text(conflict.get("resolveria"));supported(conflict.get("lastro"),state)
            require("decisao" not in conflict,"Integração relata; não decide pelo usuário")
        array(value.get("combinam"));array(value.get("dependencias"))
    else:require(False,"Estado não é verificação ou integração")
    return {"valida":True,"veredito":False,"limite":"Valida formato e vínculo de lastro; o conselho julga e a pessoa decide."}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("entrada");p.add_argument("--estado",required=True)
    a=p.parse_args();print(dump(validate(load(a.entrada),load(a.estado))),end="");return 0


if __name__=="__main__":cli(main)
