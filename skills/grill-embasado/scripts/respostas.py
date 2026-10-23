#!/usr/bin/env python3
"""Registro fiel, busca, auditoria e exportação de fatos. Executado pela condutora."""
from __future__ import annotations

import argparse
from datetime import datetime
import fcntl
import json
import os

from grill_core import (CLASSES, DOSES, checked_path, digest, dump, fold, identifier,
                        indexed, load, nonempty, objects, require, run_cli)


def validate_response(record: dict) -> dict:
    require(isinstance(record, dict), "Resposta deve ser objeto")
    for key in ("id", "q", "sub_etapa", "mensagem_id"):
        identifier(record.get(key))
    nonempty(record.get("texto"), "Texto original")
    try:
        stamp = datetime.fromisoformat(record.get("em", ""))
    except (ValueError, TypeError) as exc:
        from grill_core import GrillError
        raise GrillError("Data ISO-8601 obrigatória") from exc
    require(stamp.tzinfo is not None, "Data precisa de fuso horário")
    require(type(record.get("nao_sei")) is bool, "não sei deve ser explicitado")
    claims = indexed(record.get("afirmacoes"))
    for claim in claims.values():
        require(claim.get("classe") in CLASSES, "Classe de afirmação inválida")
        excerpt = nonempty(claim.get("trecho"), "Trecho da afirmação")
        require(excerpt in record["texto"], "Afirmação não é trecho literal da resposta")
        require(type(claim.get("central", False)) is bool, "Central deve ser booleano")
        refs = claim.get("fichas", [])
        require(isinstance(refs, list), "Fichas devem ser lista")
        for ref in refs:
            identifier(ref)
    for idea in objects(record.get("ideias")):
        require(nonempty(idea.get("trecho"), "Ideia") in record["texto"], "Ideia sem origem literal")
    if record.get("substitui") is not None:
        identifier(record["substitui"])
        require(isinstance(record.get("usos_anteriores"), list), "Revisão deve listar usos anteriores conhecidos")
    return record


def validate_log(records: list) -> list:
    indexed(records)
    by_id, claim_ids, replaced = {}, set(), set()
    for record in records:
        validate_response(record)
        for claim in record["afirmacoes"]:
            require(claim["id"] not in claim_ids, "ID de afirmação reutilizado")
            claim_ids.add(claim["id"])
        previous = record.get("substitui")
        if previous:
            require(previous in by_id and previous not in replaced, "Revisão sem resposta vigente anterior")
            require(by_id[previous]["q"] == record["q"] and by_id[previous]["sub_etapa"] == record["sub_etapa"],
                    "Revisão precisa manter pergunta e sub-etapa")
            replaced.add(previous)
        by_id[record["id"]] = record
    return records


def parse_log(content: str) -> list:
    require(not content or content.endswith("\n"), "Registro incompleto; preserve-o para recuperação")
    try:
        records = [json.loads(line) for line in content.splitlines()]
    except ValueError as exc:
        from grill_core import GrillError
        raise GrillError("Registro JSONL inválido") from exc
    return validate_log(records)


def read_log(path) -> list:
    p = checked_path(path)
    require(p.is_file() and p.stat().st_size <= 20_000_000, "Registro ausente ou maior que 20 MB")
    return parse_log(p.read_text(encoding="utf-8"))


def register(path, record: dict) -> dict:
    """Append sob trava, sem reescrever texto nem substituir registros existentes."""
    validate_response(record)
    p = checked_path(path)
    # O destino deve ser explícito e o diretório já deve existir.
    fd = os.open(p, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, "r+", encoding="utf-8", newline="") as stream:
        fcntl.flock(stream, fcntl.LOCK_EX)
        require(os.fstat(stream.fileno()).st_size <= 20_000_000, "Registro maior que 20 MB")
        records = parse_log(stream.read())
        previous = next((r for r in records if r["id"] == record["id"]), None)
        if previous is not None:
            require(previous == record, "ID existente tem outro conteúdo; não será sobrescrito")
            return {"gravada": False, "idempotente": True, "sha256": digest(record)}
        validate_log([*records, record])
        stream.seek(0, os.SEEK_END)
        stream.write(json.dumps(record, ensure_ascii=False, allow_nan=False) + "\n")
        stream.flush()
        os.fsync(stream.fileno())
    return {"gravada": True, "idempotente": False, "sha256": digest(record),
            "revisao": record.get("substitui"), "usos_anteriores": record.get("usos_anteriores", [])}


def active(records: list) -> list:
    validate_log(records)
    replaced = {r["substitui"] for r in records if r.get("substitui")}
    return [r for r in records if r["id"] not in replaced]


def export_facts(records: list, dose: str, sub_etapa: str | None = None) -> dict:
    require(dose in DOSES, "Dose inválida")
    facts, unverified = [], []
    for response in active(records):
        if sub_etapa and response["sub_etapa"] != sub_etapa:
            continue
        for claim in response["afirmacoes"]:
            if claim["classe"] != "fato do mundo":
                continue
            if dose == "leve" and not claim.get("central", False):
                unverified.append({"id": claim["id"], "situacao": "nao conferida", "motivo": "dose leve; não central"})
                continue
            # Não exportar resposta inteira, pergunta, autor, preferência, ideias ou classe de valor.
            facts.append({"id": claim["id"], "texto": claim["trecho"], "fichas": claim.get("fichas", [])})
    return {"modo": "conferir", "dose": dose, "afirmacoes": facts, "nao_conferidas": unverified}


def audit(records: list, transcript: list) -> dict:
    validate_log(records)
    messages = indexed(transcript)
    failures = []
    for record in records:
        message = messages.get(record["mensagem_id"])
        if message is None or message.get("papel") != "usuario" or message.get("texto") != record["texto"]:
            failures.append(record["id"])
    return {"fiel": not failures, "conferidas": len(records), "divergencias": failures,
            "limite": "Compara com a transcrição fornecida; sua autenticidade depende do hospedeiro."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument("--registrar", metavar="RESPOSTA_JSON")
    actions.add_argument("--buscar", metavar="TEXTO")
    actions.add_argument("--conferir", action="store_true")
    actions.add_argument("--auditar", metavar="TRANSCRICAO_JSON")
    parser.add_argument("--registro", required=True, help="JSONL selecionado pela condutora; só --registrar escreve")
    parser.add_argument("--dose", choices=sorted(DOSES), default="padrao")
    parser.add_argument("--sub-etapa")
    args = parser.parse_args()
    if args.registrar:
        result = register(args.registro, load(args.registrar))
    else:
        records = read_log(args.registro)
        if args.buscar is not None:
            result = {"respostas": [r for r in records if fold(args.buscar) in fold(r["texto"])]}
        elif args.conferir:
            result = export_facts(records, args.dose, args.sub_etapa)
        else:
            result = audit(records, load(args.auditar))
    print(dump(result), end="")
    return 1 if result.get("fiel") is False else 0


if __name__ == "__main__":
    run_cli(main)
