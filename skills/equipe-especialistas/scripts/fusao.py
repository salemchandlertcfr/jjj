#!/usr/bin/env python3
"""Anonimiza paralelas e valida origem das partes, omissões e conflitos."""
from __future__ import annotations
import argparse
import copy
import random
from equipe_core import array, cli, digest, dump, ident, index, load, no_verdict, refs, require, text, visible
import pauta


def prepare(packet):
    p=pauta.validate(packet.get("pauta"));require(p["modo"]=="fusao","Pauta de fusão obrigatória")
    parallel=list(index(packet.get("sinteses")).values());require(2<=len(parallel)<=3,"Fusão recebe duas ou três paralelas")
    leader=ident(packet.get("sessao_lider"));producer=refs(packet.get("sessoes_lideres"))
    require(leader not in producer and bool(producer),"Líder de fusão precisa ser novo")
    seed=packet.get("semente");require(type(seed) is int,"Semente obrigatória")
    parallel=sorted(parallel,key=lambda s:s["id"]);random.Random(seed).shuffle(parallel)
    public={};private={}
    for i,s in enumerate(parallel):
        label=chr(65+i);private[label]=s["id"]
        parts=list(index(s.get("partes")).values())
        require(bool(parts),"Síntese paralela sem partes")
        for part in parts:
            text(part.get("texto"));require(not visible(part["texto"],p.get("marcadores",[])),"Parte contém autoria/modelo/marcador")
        dissent=[]
        for d in index(s.get("dissenso",[])).values():
            text(d.get("argumento"));item={k:d[k] for k in ("id","argumento","mudaria_se") if k in d}
            require(not visible(dump(item),p.get("marcadores",[])),"Dissenso contém autoria/modelo/marcador")
            dissent.append(item)
        public[label]={"partes":[{"id":part["id"],"texto":part["texto"]} for part in parts],"dissenso":dissent}
    return {"brief":{"pauta":pauta.public(p),"sinteses":public,"entregar":"Origem de cada parte; fora com motivo; conflitos como opções ou contraprova."},
            "privado":{"rotulos":private,"semente":seed,"sessao_lider":leader},
            "limite":"Separar chave do brief não restringe permissões; a mesa retém a chave."}


def validate(value,public):
    require(isinstance(value,dict),"Fusão deve ser objeto");no_verdict(dump(value))
    sources=public["sinteses"];parts={(label,p["id"]):p["texto"] for label,s in sources.items() for p in s["partes"]}
    used=set()
    for part in index(value.get("partes")).values():
        text(part.get("texto"));origins=array(part.get("origens"));require(bool(origins),"Parte fundida sem origem")
        for origin in origins:
            key=(origin.get("sintese"),origin.get("parte"));require(key in parts,"Origem inexistente")
            require(origin.get("trecho") in parts[key] if isinstance(origin.get("trecho"),str) and origin["trecho"] else False,"Trecho de origem inventado")
            used.add(key)
        require(part.get("leitura") is True or len(origins)==1 and part["texto"]==origins[0]["trecho"],"Paráfrase da fusão precisa estar marcada como leitura")
    omitted=set()
    for part in array(value.get("fora")):
        key=(part.get("sintese"),part.get("parte"));require(key in parts,"Omissão sem origem")
        text(part.get("motivo"));omitted.add(key)
    require(used|omitted==set(parts),"Parte das paralelas desapareceu")
    expected={(label,d["id"],d["argumento"]) for label,s in sources.items() for d in s["dissenso"]}
    actual={(d.get("sintese"),d.get("id"),d.get("argumento")) for d in array(value.get("dissenso"))}
    require(expected<=actual,"Dissenso das paralelas desapareceu")
    for conflict in array(value.get("conflitos")):
        text(conflict.get("texto"));text(conflict.get("decidiria"))
        require(conflict.get("situacao") in {"opcoes","contraprova"},"Não fundir incompatíveis por média")
        if conflict["situacao"]=="contraprova":text(conflict.get("evidencia"))
    review=value.get("revisao",{});answers=index(value.get("respostas_critico"))
    require(review.get("conferido") and set(answers)==set(index(review.get("pontos"))),"Revisão do crítico e resposta a todos os pontos são obrigatórias")
    require(review.get("hash_saida")==digest({k:v for k,v in value.items() if k not in {"revisao","respostas_critico"}}),"Crítico precisa revisar a versão atual da fusão")
    for answer in answers.values():text(answer.get("motivo"))
    return {"valida":True,"limite":"Origem textual não comprova que a fusão é melhor ou que contraprova é suficiente."}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("acao",choices=["preparar","validar"]);p.add_argument("entrada");p.add_argument("--brief")
    a=p.parse_args();value=load(a.entrada)
    if a.acao=="preparar":result=prepare(value)
    else:require(a.brief,"Selecione brief público");result=validate(value,load(a.brief))
    print(dump(result),end="");return 0


if __name__=="__main__":cli(main)
