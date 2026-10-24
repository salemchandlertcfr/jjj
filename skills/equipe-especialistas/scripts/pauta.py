#!/usr/bin/env python3
"""Monta/valida pauta sem autoria, preferência, voto ou formato de entrega ausente."""
from __future__ import annotations
import argparse
import copy
import re
from equipe_core import MODES, array, cli, dump, fold, ident, index, load, no_verdict, require, text, visible


def validate(value):
    require(isinstance(value,dict) and value.get("schema_version")==1,"Pauta versão 1 obrigatória")
    ident(value.get("id")); ident(value.get("subetapa"))
    mode,dose=value.get("modo"),value.get("dose")
    require(mode in MODES and dose in {"leve","padrao","completa"},"Modo/dose inválido")
    for field in ("pergunta","formato_entrega","validacao_depois","refuta_se","versao_base"):
        text(value.get(field),field)
    require(bool(array(value.get("decidir"))),"Pauta precisa definir o que decidir")
    for part in value["decidir"]+array(value.get("restricoes")):
        text(part)
    public="\n".join([value["pergunta"],value["versao_base"],value["formato_entrega"],value["validacao_depois"],value["refuta_se"],*value["decidir"],*value["restricoes"]])
    require(not visible(public,value.get("marcadores",[])),"Pauta contém autoria, modelo ou marcador reservado")
    no_verdict(public)
    require(not re.search(r"melhor opcao parece|minha preferencia|buscar consenso|chegar a um acordo|votacao|media das propostas",fold(public)),"Pauta induz preferência, consenso, voto ou média")
    rounds=value.get("rodadas")
    require(type(rounds) is int and rounds>0,"Número de rodadas obrigatório")
    if mode in {"elaboracao","avulso"}:
        require(dose!="leve","Dose leve é preparação individual sem reunião; não iniciar mesa")
        require(rounds==2 if dose=="padrao" or mode=="avulso" else 2<=rounds<=3,"Rodadas fora da dose")
    elif mode=="verificacao":
        require(dose=="completa" and 1<=rounds<=2,"Verificação: completa, uma ou duas rodadas")
        require(bool(index(value.get("afirmacoes"))),"Verificação precisa de afirmações prévias")
        for c in value["afirmacoes"]:
            text(c.get("texto")); require(not visible(c["texto"]),"Afirmação traz autoria")
            no_verdict(c["texto"])
    elif mode=="integracao":
        require(1<=rounds<=2 and (rounds==1 or value.get("conflito_bloqueia") is True),"Segunda rodada de integração exige conflito bloqueante")
        require(bool(index(value.get("saidas_aprovadas"))),"Integração precisa de saídas aprovadas")
        for output in value["saidas_aprovadas"]:
            require(output.get("aprovada") is True and bool(output.get("decisao")),"Saída sem decisão anterior")
            text(output.get("texto"));require(not visible(output["texto"]),"Saída traz autoria")
    elif mode=="individual":
        require(1<=rounds<=2,"Individual tem uma ou duas revisões")
    else:
        require(rounds==1,"Fusão tem uma rodada de revisão")
    require(type(value.get("central",False)) is bool,"Central deve ser booleano")
    if value.get("central") and dose=="completa" and mode=="elaboracao":
        require(value.get("paralelas") in {2,3},"Saída central completa exige duas ou três paralelas e fusão")
    return value


def build(value):
    result=copy.deepcopy(value);result.setdefault("schema_version",1);result.setdefault("restricoes",[])
    result.setdefault("rodadas",3 if result.get("modo")=="elaboracao" and result.get("dose")=="completa" else 2 if result.get("modo") in {"elaboracao","avulso"} else 1)
    return validate(result)


def public(value):
    validate(value)
    keys=("id","subetapa","modo","dose","pergunta","decidir","formato_entrega","validacao_depois",
          "refuta_se","restricoes","versao_base","rodadas","afirmacoes","saidas_aprovadas")
    return {k:value[k] for k in keys if k in value}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("acao",choices=["montar","validar"]);p.add_argument("entrada")
    a=p.parse_args();print(dump((build if a.acao=="montar" else validate)(load(a.entrada))),end="");return 0


if __name__=="__main__":cli(main)
