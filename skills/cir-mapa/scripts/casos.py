#!/usr/bin/env python3
"""Valida candidatos, prepara sonda, sorteia uma vez e audita vazamento sem revelar trechos."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import math
from pathlib import Path
import random
import re

from mapa_core import array, cited, cli, document, dump, index, iso, load, require, sources, text

TYPES = {"comum", "falha", "sucesso", "simetria", "evidencia_contraria", "nada_relevante"}


def validate(bank):
    document(bank); fs = sources(bank); cases = index(bank.get("casos"))
    require(15 <= len(cases) <= 30, "Banco exige 15 a 30 casos")
    counts = Counter(); markers = set(); pairs = defaultdict(list)
    require(text(bank.get("modelo_sonda")) == text(bank.get("modelo_geradores")), "Sonda deve usar modelo dos geradores do tema 4")
    for c in cases.values():
        require(c.get("tipo") in TYPES, "Tipo de caso inválido")
        counts[c["tipo"]] += 1
        marker = c.get("marcador")
        require(isinstance(marker, str) and re.fullmatch(r"⟦[A-Za-z0-9_-]{6,64}⟧", marker), "Marcador único obrigatório")
        require(marker not in markers, "Marcador duplicado"); markers.add(marker)
        cutoff = iso(c.get("data_corte"))
        text(c.get("origem")); text(c.get("dificuldade"))
        require(c.get("lado") in {"bom", "ruim", "neutro"}, "Desfecho exige lado")
        require(type(c.get("visto")) is bool and type(c.get("depois_solucao")) is bool
                and type(c.get("construido")) is bool, "Flags de exposição/construção devem ser booleanas")
        require(c.get("conhecido_modelo") is None or type(c.get("conhecido_modelo")) is bool, "Sonda deve ser booleano ou null pendente")
        # Null impede reserva; uma declaração false exige registro da sonda.
        if c.get("conhecido_modelo") is not None:
            probe = c.get("sonda")
            require(isinstance(probe, dict), "Falta registro da sonda")
            require(probe.get("modelo") == bank["modelo_geradores"], "Modelo divergente na sonda")
            text(probe.get("continuacao")); array(probe.get("acertos_nao_no_antes"))
            require(c["conhecido_modelo"] == bool(probe["acertos_nao_no_antes"]), "Marca de memória diverge dos acertos")
        before = array(c.get("antes")); require(bool(before), "Antes obrigatório")
        outcome = c.get("desfecho")
        require(isinstance(outcome, dict), "Desfecho separado obrigatório")
        text(outcome.get("texto")); cited(outcome.get("fontes"), fs); iso(outcome.get("data"))
        require(outcome["data"] > cutoff, "Desfecho deve ser posterior ao corte")
        for fact in before:
            text(fact.get("texto")); cited(fact.get("fontes"), fs)
            require(iso(fact.get("disponivel_em")) <= cutoff, "Informação posterior ao corte no antes")
            require(outcome["texto"].casefold() not in fact["texto"].casefold(), "Desfecho copiado no antes")
        if c["tipo"] == "simetria":
            text(c.get("par")); text(c.get("relacao_esperada")); pairs[c["par"]].append(c)
        else:
            require(not c.get("construido"), "Só espelho de simetria pode ser construído")
    require(counts["falha"] >= 3 and counts["sucesso"] >= 3, "Faltam falhas/sucessos")
    require(counts["evidencia_contraria"] >= 2 and counts["nada_relevante"] >= 2, "Faltam evidência contrária/nada relevante")
    require(len(pairs) >= 2, "Exige dois pares de simetria")
    for members in pairs.values():
        require(len(members) == 2 and not all(c["construido"] for c in members), "Par exige dois casos e ao menos um real")
        require(members[0]["relacao_esperada"] == members[1]["relacao_esperada"], "Par com relações conflitantes")
    require({"bom", "ruim"} <= {c["lado"] for c in cases.values()}, "Banco não pode ter desfechos de um lado só")
    return {"valido": True, "total": len(cases), "contagem": dict(sorted(counts.items())),
            "pares_simetria": len(pairs), "sondas_pendentes": sum(c["conhecido_modelo"] is None for c in cases.values()),
            "limite": "Datas e cópia literal são verificadas; retrospectiva semântica, fatos e dificuldade exigem crítico."}


def fingerprint(bank):
    # Ordem física não muda o sorteio ou a impressão digital.
    from mapa_core import dump
    normalized = {**bank, "casos": sorted(bank["casos"], key=lambda c: c["id"])}
    normalized.pop("sorteio", None)
    return hashlib.sha256(dump(normalized).encode()).hexdigest()


def draw(bank, seed, etapa):
    validate(bank)
    require(etapa == "3.6", "Sorteio só no 3.6")
    require(type(seed) is int, "Semente inteira obrigatória")
    require(not bank.get("sorteio"), "Banco já congelado: não sortear de novo; novos casos são depois da solução")
    cases = index(bank["casos"])
    # Pares são unidades indivisíveis, para não revelar o reservado pelo espelho.
    groups = defaultdict(list)
    for c in sorted(cases.values(), key=lambda c: c["id"]):
        groups[("par", c.get("par")) if c["tipo"] == "simetria" else ("caso", c["id"])].append(c)
    eligible = defaultdict(list)
    for group in groups.values():
        if all(not c["visto"] and c["conhecido_modelo"] is False and not c["depois_solucao"] for c in group):
            eligible[group[0]["tipo"]].append(group)
    rng = random.Random(seed)
    required_types = {c["tipo"] for c in cases.values()}
    require(required_types <= set(eligible), "Faltam candidatos elegíveis em um tipo: peça mais casos; não relaxe exclusões")
    reserved = []; remainder = []
    for kind in sorted(required_types):
        choices = eligible[kind]; rng.shuffle(choices)
        reserved.extend(c["id"] for c in choices[0])
        remainder.extend(choices[1:])
    rng.shuffle(remainder)
    target = max(math.ceil(len(cases) / 4), len(cases) - 20, len(reserved))
    for group in remainder:
        if len(reserved) >= target:
            break
        reserved.extend(c["id"] for c in group)
    working = sorted(set(cases) - set(reserved))
    require(10 <= len(working) <= 20 and len(reserved) >= math.ceil(len(working) / 3),
            "Casos insuficientes para trabalho e reserva por tipo; ampliar banco")
    return {"schema_version": 1, "etapa": etapa, "semente": seed, "banco_sha256": fingerprint(bank),
            "trabalho": working, "reservados": sorted(reserved),
            "regra": "estratificado por tipo; pares juntos; mínimo um grupo por tipo; exclui exposição, memória e pós-solução",
            "privado": True, "persistir": "Só a condutora registra uma vez; não distribuir esta relação nem os reservados aos geradores."}


def probe(bank):
    validate(bank)
    return {"modelo": bank["modelo_geradores"], "casos": [
        {"id": c["id"], "data_corte": c["data_corte"], "antes": [f["texto"] for f in c["antes"]]}
        for c in bank["casos"]], "entregar": "continuação; acertos não contidos no antes, conferidos externamente"}


def leakage(bank, root):
    validate(bank); root = Path(root).resolve()
    require(root.is_dir(), "Raiz para auditoria ausente")
    patterns = []
    for c in bank["casos"]:
        patterns.append((c["id"], "marcador", c["marcador"]))
        for raw in [f["texto"] for f in c["antes"]] + [c["desfecho"]["texto"]]:
            if len(raw.split()) >= 8:
                patterns.append((c["id"], "trecho_literal", raw))
    findings = []
    # Falha de leitura não é um resultado limpo. Não segue symlinks para fora.
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if any(p in {".git", "__pycache__"} for p in rel.parts):
            continue
        require(not path.is_symlink(), "Auditoria incompleta: link simbólico em " + str(rel))
        if not path.is_file() or rel.parts[0] == "casos":
            continue
        raw = path.read_bytes()
        try:
            content = raw.decode("utf-8")
        except UnicodeDecodeError:
            require(not any(p.encode() in raw for _, _, p in patterns), "Marcador/trecho em arquivo binário: " + str(rel))
            continue
        normalized = " ".join(content.split()).casefold()
        for case, kind, pat in patterns:
            if " ".join(pat.split()).casefold() in normalized:
                findings.append({"arquivo": str(rel), "caso": case, "tipo": kind})
    return {"limpo": not findings, "achados": findings, "limite": "Busca literal, não detecta paráfrases; não substitui permissões do hospedeiro."}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("operacao", choices=["validar", "sonda", "sortear"]); p.add_argument("entrada")
    p.add_argument("--semente", type=int); p.add_argument("--etapa")
    p.add_argument("--vazamento", type=Path)
    a = p.parse_args(); bank = load(a.entrada)
    if a.vazamento:
        result = leakage(bank, a.vazamento)
    elif a.operacao == "sortear":
        result = draw(bank, a.semente, a.etapa)
    else:
        result = probe(bank) if a.operacao == "sonda" else validate(bank)
    print(dump(result), end="")
    return int(result.get("limpo") is False)


if __name__ == "__main__":
    raise SystemExit(cli(main))
