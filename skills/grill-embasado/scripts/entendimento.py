#!/usr/bin/env python3
"""Monta Entendimento rastreável, brief filtrado e verifica parada/contradição."""
from __future__ import annotations

import argparse

from grill_core import (DOSES, VALUES, digest, dump, identifier, indexed, load,
                        nonempty, objects, require, run_cli)
from perguntas import frontier
from respostas import active, read_log


def understanding(packet: dict, responses: list) -> dict:
    require(isinstance(packet, dict), "Entendimento deve ser objeto")
    identifier(packet.get("sub_etapa"))
    by_id = indexed(active(responses))
    excerpts = indexed(packet.get("trechos_dossie", []))
    items = objects(packet.get("itens"))
    require(bool(items), "Entendimento precisa de itens")
    lines = [f"## Entendimento · {packet['sub_etapa']}"]
    for item in items:
        label = nonempty(item.get("rotulo"), "Rótulo")
        text = nonempty(item.get("texto"), "Texto do entendimento")
        require(type(item.get("leitura")) is bool, "Cada item deve declarar se é leitura")
        origins = objects(item.get("origens"))
        require(bool(origins), "Frase sem origem")
        quotes, citations = [], []
        for origin in origins:
            excerpt = nonempty(origin.get("trecho"), "Trecho de origem")
            key = origin.get("id")
            kind = origin.get("tipo")
            if kind == "resposta":
                require(key in by_id, "Origem não é resposta vigente")
                source = by_id[key]
                require(source["sub_etapa"] == packet["sub_etapa"], "Resposta de outra sub-etapa exige trecho explícito do dossiê")
                require(excerpt in source["texto"], "Origem diverge da resposta")
                citations.append(source["q"] + "/" + key)
            elif kind == "dossie":
                require(key in excerpts, "Trecho do dossiê não fornecido")
                require(excerpt in nonempty(excerpts[key].get("texto"), "Texto do dossiê"), "Origem diverge do dossiê")
                citations.append(key)
            else:
                require(False, "Tipo de origem inválido")
            quotes.append(excerpt)
        require(item["leitura"] or (len(quotes) == 1 and text == quotes[0]),
                "Paráfrase ou ligação precisa da marca leitura")
        prefix = "leitura da condutora · " if item["leitura"] else ""
        lines.append(f"- {prefix}{label}: {text} ({', '.join(citations)})")
    for entry in objects(packet.get("nao_perguntado", [])):
        require(entry.get("valor") in VALUES, "Valor de lacuna inválido")
        nonempty(entry.get("risco"), "Risco de não perguntar")
        nonempty(entry.get("motivo"), "Motivo de não perguntar")
        lines.append(f"- não perguntado: {nonempty(entry.get('texto'), 'Lacuna')} · valor {entry['valor']}; "
                     f"risco: {entry['risco']}; motivo: {entry['motivo']}")
    markdown = "\n".join(lines) + "\n"
    return {"markdown": markdown, "sha256": digest(markdown), "confirmacao": "pendente"}


def reader_brief(card: dict, result: dict, dose: str) -> dict:
    require(dose in DOSES, "Dose inválida")
    # Lista explícita: nenhuma outra chave do cartão ou envelope é transmitida.
    public_card = {"sub_etapa": identifier(card.get("sub_etapa")),
                   "objetivo": nonempty(card.get("objetivo"), "Objetivo do cartão"),
                   "grill_quer_entender": nonempty(card.get("grill_quer_entender"), "Objetivo do grill"),
                   "saida": nonempty(card.get("saida"), "Saída do cartão")}
    return {"papel": "leitor do entendimento", "dose": dose, "cartao": public_card,
            "entendimento": result["markdown"], "entendimento_sha256": result["sha256"],
            "entregar": "Só perguntas em que um palpite errado mudaria a saída, com classe, impacto e importância; ou nada importante faltando.",
            "restricoes": {"sessao_nova": True, "ferramentas": [], "sem_conversa_dossie_fichas_autoria": True},
            "limite": "Filtragem não é sandbox. O hospedeiro deve verificar contexto e permissões."}


def stop(packet: dict) -> dict:
    require(isinstance(packet, dict), "Parada deve ser objeto")
    require(packet.get("dose") in DOSES, "Dose inválida")
    reason = packet.get("motivo")
    require(reason in {"sem valor", "chega"}, "Motivo de parada inválido")
    nodes = objects(packet.get("mapa"))
    available = frontier(nodes)
    pending = [n for n in nodes if n["estado"] == "pendente" and VALUES[n["valor"]] > 0]
    gaps = indexed(packet.get("nao_perguntado", []))
    require(all(n["id"] in gaps for n in pending), "Pendência sem registro de não perguntado")
    for gap in gaps.values():
        nonempty(gap.get("risco"), "Risco da pendência")
        nonempty(gap.get("motivo"), "Motivo da pendência")
    sha = nonempty(packet.get("entendimento_sha256"), "Hash do entendimento")
    nonempty(packet.get("sessao_condutora"), "Sessão da condutora")
    confirmed = packet.get("confirmacao", {})
    require(isinstance(confirmed, dict), "Confirmação inválida")
    confirmation_ok = (confirmed.get("entendimento_sha256") == sha
                       and confirmed.get("confirmado") is True and bool(confirmed.get("resposta_id")))
    reader = packet.get("leitor", {})
    require(isinstance(reader, dict), "Resultado do leitor inválido")
    reader_ok = (reader.get("concluido") is True and reader.get("entendimento_sha256") == sha
                 and bool(reader.get("sessao")) and reader.get("sessao") != packet.get("sessao_condutora")
                 and reader.get("modelo_verificado") is True)
    questions = objects(reader.get("perguntas", []))
    for question in questions:
        require(question.get("classe") in {"fato do mundo", "fato pessoal", "decisao", "valor"}, "Classe do leitor inválida")
        nonempty(question.get("impacto"), "Impacto da lacuna encontrada pelo leitor")
        nonempty(question.get("texto"), "Pergunta do leitor")
    unresolved_personal = [q for q in questions if q["classe"] != "fato do mundo" and q.get("resolvida") is not True]
    research = [q for q in questions if q["classe"] == "fato do mundo"]
    if reason == "chega":
        return {"parar_conversa": True, "pronto": False, "situacao": "interrompido pelo usuario",
                "pulado_e_risco": list(gaps.values()), "leitor_pendente": not reader_ok,
                "confirmacao_pendente": not confirmation_ok, "para_pesquisa": research}
    blockers = []
    if available or unresolved_personal:
        blockers.append("perguntas ainda mudam a decisão")
    if any(n["classe"] != "fato do mundo" for n in pending):
        blockers.append("dependências ou perguntas pendentes")
    if not confirmation_ok:
        blockers.append("entendimento atual sem confirmação")
    if not reader_ok:
        blockers.append("leitor independente pendente para o entendimento atual")
    if research and not packet.get("pesquisa_encaminhada"):
        blockers.append("fatos do leitor ainda não encaminhados")
    if any(n["classe"] == "fato do mundo" for n in pending) and not packet.get("pesquisa_encaminhada"):
        blockers.append("fatos do mapa ainda não encaminhados")
    return {"parar_conversa": not available and not unresolved_personal, "pronto": not blockers,
            "bloqueios": blockers, "para_pesquisa": research, "pulado_e_risco": list(gaps.values())}


def check_contradictions(records: list, conferences: list, events: list, dose: str) -> dict:
    """Conferências externas; o grill não cria evidência nem resolve o desacordo."""
    require(dose in DOSES, "Dose inválida")
    claims = {c["id"]: c for r in active(records) for c in r["afirmacoes"] if c["classe"] == "fato do mundo"}
    by_id = indexed(conferences)
    for key, conf in by_id.items():
        require(key in claims, "Conferência sem afirmação factual vigente")
        require(conf.get("resultado") in {"sustenta", "sustenta em parte", "nao sustenta", "contradiz", "sem fonte"}, "Resultado de conferência inválido")
        if conf["resultado"] != "sem fonte":
            require(bool(objects(conf.get("evidencias"))), "Conferência sem evidência")
            for evidence in conf["evidencias"]:
                identifier(evidence.get("ficha"))
                nonempty(evidence.get("trecho"), "Trecho da evidência")
                require(type(evidence.get("forca")) is int and 1 <= evidence["forca"] <= 5, "Força inválida")
    indexed(events)
    challenged = set()
    for event in events:
        claim_id = event.get("afirmacao")
        require(claim_id in by_id and by_id[claim_id]["resultado"] == "contradiz", "Evento sem contradição conferida")
        require(claim_id not in challenged, "Contradição já foi perguntada; não insistir")
        challenged.add(claim_id)
        require(event.get("suas_palavras") == claims[claim_id]["trecho"], "Contradição deve mostrar palavras originais")
        require(event.get("evidencias_mostradas") == by_id[claim_id]["evidencias"], "Evidência ou força foi omitida ou alterada")
        require(event.get("depois") in {"mudou", "manteve", "manteve sem motivo", "aguardando"}, "Desfecho inválido")
        if event["depois"] in {"mudou", "manteve"}:
            nonempty(event.get("motivo"), "Motivo do usuário")
    contradictions = [k for k, v in by_id.items() if v["resultado"] == "contradiz"]
    return {"sinal_dose": bool(contradictions), "dose_sugerida": {"leve": "padrao", "padrao": "completa", "completa": "completa"}[dose] if contradictions else dose,
            "mostrar_uma_vez": [k for k in contradictions if k not in challenged],
            "nao_conferidas": [k for k in claims if k not in by_id],
            "situacoes": [{"id": k, "resultado": by_id[k]["resultado"] if k in by_id else "nao conferida"} for k in claims]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entrada", help="Entendimento ou pacote de parada/checagem JSON")
    parser.add_argument("--registro", help="Respostas JSONL explicitamente selecionadas")
    parser.add_argument("--cartao", help="Devolve brief filtrado em vez do Markdown")
    parser.add_argument("--dose", choices=sorted(DOSES), default="padrao")
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument("--parada", action="store_true")
    actions.add_argument("--checagem", action="store_true")
    args = parser.parse_args()
    packet = load(args.entrada)
    if args.parada:
        result = stop(packet)
    else:
        require(bool(args.registro), "Selecione --registro")
        records = read_log(args.registro)
        if args.checagem:
            result = check_contradictions(records, packet.get("conferencias", []), packet.get("eventos", []), args.dose)
        else:
            result = understanding(packet, records)
            if args.cartao:
                result = reader_brief(load(args.cartao), result, args.dose)
    print(dump(result), end="")
    return 1 if args.parada and not result["pronto"] else 0


if __name__ == "__main__":
    run_cli(main)
