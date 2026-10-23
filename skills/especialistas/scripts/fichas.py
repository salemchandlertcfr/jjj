#!/usr/bin/env python3
"""Cria fichas copiando permissões do papel e valida formações e doses."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import random
import re
from catalogo import catalog
from cobertura import mapping
from esp_core import DOSES, array, cli, dump, functional, ident, index, load, refs, require, text

FIELDS = {"id", "subetapa", "passo", "dose", "rodada", "grupo", "papel", "nome", "especialidade",
          "esp", "modulos", "escola", "distante", "funcao_analoga", "cobre", "por_que", "fontes",
          "ferramentas", "modelo", "ve", "nao_ve", "sessao", "lacuna", "operadores", "semente",
          "template", "otica", "excecao_mapa", "motivo_escola"}


def policies():
    raw = (Path(__file__).resolve().parents[1] / "references/papeis.md").read_text()
    match = re.search(r"```json\n(.*?)\n```", raw, re.S)
    require(match, "Política de papéis ausente")
    return json.loads(match.group(1))


def model_for(models, role):
    require(isinstance(models, dict) and isinstance(models.get(role), dict), "Modelo do papel ausente")
    model = models[role]
    ident(model.get("id")); text(model.get("nome"))
    require(model.get("familia") == "anthropic", "Perfil v1 exige modelo Claude escolhido pelo usuário")
    require(type(model.get("verificado")) is bool, "Presença/verificação do modelo deve ser explícita")
    return {k: model[k] for k in ("id", "nome", "familia", "verificado")}


def new(draft, models):
    require(isinstance(draft, dict), "Ficha deve ser objeto")
    result = dict(draft)
    role = draft.get("papel")
    require(role in policies(), "Papel não definido pela política")
    rule = policies()[role]
    for field in ("ve", "nao_ve"):
        require(field not in draft or draft[field] == rule[field], "Tentativa de mudar visibilidade do papel")
        result[field] = rule[field]
    expected = model_for(models, role)
    require("modelo" not in draft or draft["modelo"] == expected, "Especialidade não pode trocar o modelo do papel")
    result["modelo"] = expected
    return result


def validate(ficha, cat, models, mapa):
    require(isinstance(ficha, dict) and set(ficha) <= FIELDS, "Ficha contém campos desconhecidos ou credenciais")
    ident(ficha.get("id")); ident(ficha.get("subetapa")); ident(ficha.get("sessao"))
    require(ficha.get("papel") in policies(), "Papel inválido")
    role = ficha["papel"]
    for field in ("ve", "nao_ve"):
        require(ficha.get(field) == policies()[role][field], "Visibilidade alterada; copie a regra do papel")
    require(ficha.get("modelo") == model_for(models, role), "Modelo diverge do papel")
    require(ficha.get("dose") in DOSES and ficha.get("passo") in {3, 7, 8}, "Passo ou dose inválido")
    require(type(ficha.get("rodada")) is int and ficha["rodada"] > 0, "Rodada inválida")
    require(isinstance(ficha.get("nome"), str) and re.fullmatch(r"[a-z][a-z0-9-]*-\d+", ficha["nome"]), "Nome deve ser funcional com número")
    functional(ficha["nome"])
    functional(ficha.get("especialidade")); text(ficha.get("por_que"))
    items, specialties = mapping(mapa)
    require(bool(refs(ficha.get("cobre"))) and set(ficha["cobre"]) <= set(items), "Ficha não cobre itens conhecidos")
    matching = [s for s in specialties.values() if s["especialidade"] == ficha["especialidade"]]
    if not matching and role != "critico":
        exception = ficha.get("excecao_mapa", {})
        require(isinstance(exception, dict) and exception.get("aprovada") is True and bool(exception.get("decisao")),
                "Especialidade fora do mapa exige decisão explícita")
    elif matching:
        require(set(ficha["cobre"]) <= {i for s in matching for i in s["cobre"]}, "Ficha amplia cobertura sem atualizar mapa")
    refs(ficha.get("fontes")); refs(ficha.get("ferramentas"))
    require(type(ficha.get("distante")) is bool, "Distância deve ser explícita")
    if ficha["distante"]:
        text(ficha.get("funcao_analoga"), "Função análoga da distante")
    school = ficha.get("escola")
    if school is not None:
        require(isinstance(school, dict), "Escola deve ter nome e obras")
        text(school.get("nome")); require(bool(array(school.get("obras"))), "Escola sem obras")
        for work in school["obras"]:
            text(work)
    entries = catalog(cat)
    esp = ficha.get("esp")
    if esp is None:
        ident(ficha.get("lacuna")); require(ficha.get("modulos") == [], "Sem skill não pode ter módulos")
    else:
        require(isinstance(esp, dict) and esp.get("id") in entries, "esp fora do catálogo")
        entry = entries[esp["id"]]
        require(entry["situacao"] in {"em_uso", "em_revisao"}, "esp não está disponível para uso")
        require(esp == {k: entry[k] for k in ("id", "versao", "hash")}, "Versão/hash diverge do catálogo")
        require(set(refs(ficha.get("modulos"))) <= set(entry["modulos"]), "Módulo fora da versão selecionada")
    if role == "gerador":
        require(bool(refs(ficha.get("operadores"))) and type(ficha.get("semente")) is int, "Gerador exige operadores e semente")
    if role == "conselheiro":
        ident(ficha.get("template")); ident(ficha.get("otica"))
    return ficha


def formation(packet, cat, models, mapa):
    require(isinstance(packet, dict), "Formação deve ser objeto")
    cards = list(index(packet.get("fichas")).values())
    require(bool(cards), "Formação vazia")
    for card in cards:
        validate(card, cat, models, mapa)
    require(len({f["sessao"] for f in cards}) == len(cards), "Agentes devem usar sessões diferentes")
    require(len({f["nome"] for f in cards}) == len(cards), "Nome funcional duplicado")
    require(len({(f["subetapa"], f["passo"], f["dose"], f["rodada"]) for f in cards}) == 1, "Fichas de contextos diferentes")
    dose, step = cards[0]["dose"], cards[0]["passo"]
    kind = packet.get("formacao")
    require(kind in {"triagem", "equipe", "geradores", "verificacao", "conselho"}, "Formação inválida")
    require(step == {"triagem": 3, "equipe": 7, "geradores": 7, "verificacao": 8}.get(kind, step), "Passo diverge da formação")
    members = [f for f in cards if f["papel"] != "critico"]
    critics = [f for f in cards if f["papel"] == "critico"]
    require(len(critics) == (0 if kind == "geradores" else 1), "Formação exige um crítico separado; geradores são isolados")
    if kind == "conselho":
        expected = refs(packet.get("oticas"))
        require(set(expected) == {f.get("otica") for f in members} and len(expected) == len(members), "Composição do conselho diverge das óticas fornecidas")
        require(all(f["papel"] == "conselheiro" for f in members), "Papel divergente do conselho")
    else:
        sizes = {"triagem": {"leve": (1, 1), "padrao": (2, 2), "completa": (2, 3)},
                 "equipe": {"leve": (1, 1), "padrao": (3, 3), "completa": (4, 5)},
                 "geradores": {"leve": (0, 0), "padrao": (1, 1), "completa": (2, 3)},
                 "verificacao": {"leve": (0, 0), "padrao": (0, 0), "completa": (2, 3)}}
        lo, hi = sizes[kind][dose]
        require(lo <= len(members) <= hi and hi > 0, "Tamanho incompatível com dose/formação")
        expected_role = {"triagem": "especialista", "equipe": "especialista", "geradores": "gerador", "verificacao": "verificador"}[kind]
        require(all(f["papel"] == expected_role for f in members), "Papel incompatível com formação")
    distant = [f for f in members if f["distante"]]
    expected_distant = 1 if kind == "geradores" or kind == "equipe" and dose == "completa" else 0
    require(len(distant) == expected_distant, "Quantidade de distantes incompatível com formação")
    if kind == "equipe" and dose == "completa":
        require(members.index(distant[0]) >= 3, "Distante só entra a partir do quarto lugar")
    for i, member in enumerate(members):
        for other in members[:i]:
            same = member["especialidade"] == other["especialidade"]
            if same:
                require(kind != "geradores" and member.get("escola") and other.get("escola")
                        and member["escola"]["nome"] != other["escola"]["nome"]
                        and bool(member.get("motivo_escola")), "Especialidade/ótica repetida sem divergência de escolas justificada")
    if kind == "geradores":
        operators = [o for f in members for o in f["operadores"]]
        require(len(set(operators)) == len(operators), "Geradores repetem operadores")
        require(len({f["semente"] for f in members}) == 1, "Semente deve ser comum ao sorteio da formação")
    if kind == "verificacao":
        producers = refs(packet.get("sessoes_produtoras"))
        require(bool(producers), "Verificação exige lista de sessões produtoras")
        require(not {f["sessao"] for f in cards} & set(producers), "Quem elaborou não verifica")
    selected = {i for f in members for i in f["cobre"]}
    required_items = refs(packet.get("itens_exigidos"))
    require(set(required_items) <= set(mapping(mapa)[0]), "Item exigido fora do problema")
    missing = sorted(set(required_items)-selected)
    return {"valida": not missing, "sem_cobertura": missing,
            "executavel": not missing and all(f["modelo"]["verificado"] for f in cards)
                          and mapa.get("aprovacao", {}).get("aprovada") is True
                          and bool(mapa.get("aprovacao", {}).get("decisao")),
            "lacunas": sorted({f["lacuna"] for f in cards if f["esp"] is None}),
            "limite": "Sessões, modelos e permissões declarados exigem auditoria no hospedeiro."}


def operators(cards, pool, seed):
    require(type(seed) is int, "Semente inteira obrigatória")
    choices = refs(pool)
    require(len(choices) >= len(cards), "Operadores insuficientes sem repetição")
    choices = sorted(choices); random.Random(seed).shuffle(choices)
    result = []
    for i, card in enumerate(cards):
        require(card.get("papel") == "gerador", "Sorteio só para geradores")
        result.append({**card, "operadores": [choices[i]], "semente": seed})
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("acao", choices=["novo", "validar", "sortear"]); p.add_argument("entrada")
    p.add_argument("--catalogo"); p.add_argument("--modelos"); p.add_argument("--mapa")
    a = p.parse_args(); value = load(a.entrada)
    if a.acao == "sortear":
        result = operators(value["fichas"], value["operadores"], value["semente"])
    else:
        require(a.catalogo and a.modelos and a.mapa, "Selecione catálogo, modelos e mapa")
        cat, models, mapa = load(a.catalogo), load(a.modelos), load(a.mapa)
        if a.acao == "novo":
            result = new(value, models); validate(result, cat, models, mapa)
        else:
            result = formation(value, cat, models, mapa)
    print(dump(result), end="")
    return int(result.get("valida") is False) if isinstance(result, dict) else 0


if __name__ == "__main__":
    cli(main)
