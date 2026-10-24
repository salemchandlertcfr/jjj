#!/usr/bin/env python3
"""Uniformiza pacote e contrastes sem truncar, escolher vencedor ou transportar o banco."""
from __future__ import annotations

import argparse
import re
from mapa_core import cli, dump, load, require, text

FIELDS = ("job", "falhas_centrais", "causas", "contradicoes", "projecao", "espaco_k", "banco")
AUTHOR = re.compile(r"\b(autoria|autor|usuário|usuario|user|equipe|gerador|claude|anthropic|openai|gpt|opus|sonnet)\b|[\w.+-]+@[\w.-]+", re.I)


def validate(value):
    from mapa_core import document
    document(value)
    require(set(value) == {"schema_version", *FIELDS}, "Pacote e contraste exigem somente as mesmas sete linhas")
    for k in FIELDS:
        text(value[k], k)
        require("\n" not in value[k], "Uma linha por campo")
        require(not AUTHOR.search(value[k]), "Possível autoria: normalize e revise o campo " + k)
        require(not re.search(r"⟦[^⟧]+⟧|casos/|desfecho:", value[k], re.I), "Banco deve aparecer somente como contagem")
    require(re.fullmatch(r"[\d\s:;,./()=+\-\wáéíóúâêôãõç]+", value["banco"], re.I) is not None, "Contagem inválida")
    # Banco é objeto numérico normalizado em texto; títulos/conteúdo de casos não cabem.
    require(re.fullmatch(r"\d+ total; \d+ falha; \d+ sucesso; \d+ simetria; \d+ evidencia_contraria; \d+ nada_relevante; \d+ comum", value["banco"]) is not None, "Use apenas a contagem padronizada do banco")
    numbers = list(map(int, re.findall(r"\d+", value["banco"])))
    require(numbers[0] == sum(numbers[1:]), "Total do banco diverge das contagens")
    require(sum(len(value[k].split()) for k in FIELDS) <= 600, "Pacote excede 600 palavras: redija de novo sem truncamento automático")
    return value


def build(value):
    from mapa import validate as validate_map
    validate_map(value)
    counts = value.get("contagem_casos")
    require(isinstance(counts, dict), "Contagem pública de casos obrigatória")
    kinds = ("falha", "sucesso", "simetria", "evidencia_contraria", "nada_relevante", "comum")
    require(set(counts) == set(kinds) and all(type(v) is int and v >= 0 for v in counts.values()), "Contagem inválida")
    bank = str(sum(counts.values())) + " total; " + "; ".join(f"{counts[k]} {k}" for k in kinds)
    descriptions = [c["id"] + " " + c["texto"] + " (" + c["forca"] + ", " + c["situacao"] + ")" for c in value["causas"]]
    descriptions.extend(f["id"] + ": causa desconhecida; resolveria: " + f["excecao_rivais"]["observacao_que_resolveria"]
                        for f in value["falhas"] if f.get("causa_desconhecida"))
    result = {"schema_version": 1, "job": value["job"],
              "falhas_centrais": "; ".join(f["id"] + " " + f["texto"] for f in value["falhas"] if f["central"]),
              "causas": "; ".join(descriptions) or "Nenhuma causa admitida",
              "contradicoes": "; ".join(c["id"] + " " + " × ".join(c["parametros"]) + " (" + c["classe"] + ")" for c in value["contradicoes"]) or "Nenhuma contradição identificada",
              "projecao": "; ".join(h["prazo"] + ": " + h["faixa"] for h in value["projecao"]["horizontes"]),
              "espaco_k": "; ".join(k["id"] + " " + k["texto"] + " (" + k["classe"] + ")" for k in value["conhecimento"]) or "Sem conhecimento admitido",
              "banco": bank}
    # Texto livre ainda exige revisão humana de anonimato e fidelidade.
    return validate(result)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("operacao", choices=["montar", "conferir"]); p.add_argument("entrada")
    a = p.parse_args(); v = load(a.entrada)
    print(dump(build(v) if a.operacao == "montar" else validate(v)), end="")


if __name__ == "__main__":
    raise SystemExit(cli(main))
