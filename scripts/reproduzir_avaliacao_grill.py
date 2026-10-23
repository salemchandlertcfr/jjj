#!/usr/bin/env python3
"""Reproduz agregação e viewer de seis saídas preservadas; não chama modelos."""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals/grill-embasado"
ITERATION = EVALS / "iteration-1"
REVISION = "dbd4588f9e1033efb41dad4bef2f7947c8993d44"
HASHES = {
    "scripts/aggregate_benchmark.py": "123ef128ea5ccc01a4b1ac212ef5567f21e9c13d3d240609780beeb3200c49aa",
    "eval-viewer/generate_review.py": "fc9d1b9243fe5ab6012ebd579bd76d0035de1b79fd3b969de114defab26478fb",
    "eval-viewer/viewer.html": "a53213426ee1100441d701a3a0d49cda7a842f992d2c36463f4d3cc0258575fa",
}
NOTES = [
    "Ensaio textual exploratório: três prompts por condição, uma execução por prompt. As 12 assertions não são 12 execuções independentes.",
    "Execução e avaliação usaram assistentes desta sessão; modelo exato indisponível. Isto não é validação em Claude, avaliação cega, persona oculta ou conversa real com usuário.",
    "Tempo é parede observada pelo executor, incluindo leitura e ferramentas; duração nativa, tokens, chamadas e erros são desconhecidos. Caracteres não são tokens.",
    "O caso 2 empata. As diferenças dos casos 1 e 3 são unicidade da pergunta, identificação do cartão como base e sinal de dose. A rubrica de identificação da base admite revisão humana.",
    "Os prompts tornam várias regras explícitas. Assertions conjuntas, como valor e dose, reduzem a precisão da atribuição; veja eval_feedback de cada execução.",
    "A skill passou em 12/12 e o baseline em 9/12 nesta rubrica; a amostra não demonstra benefício geral, revelação, ausência de deriva ou parada adequada numa entrevista completa.",
    "O desvio padrão é entre três casos diferentes, sem repetições. Revisão humana pendente; feedback não foi fabricado.",
]


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode()


def verify(upstream):
    for name, expected in HASHES.items():
        if hashlib.sha256((upstream / name).read_bytes()).hexdigest() != expected:
            raise ValueError("Auxiliar não corresponde à revisão oficial fixada")
    for line in (ITERATION / "artifacts.sha256").read_text().splitlines():
        expected, name = line.split("  ", 1)
        path = (ITERATION / name).resolve()
        if not path.is_relative_to(ITERATION) or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError("Artefato de avaliação ausente ou divergente")
    runs = sorted(ITERATION.glob("eval-*/*/run-1"))
    if len(runs) != 6:
        raise ValueError("Esperadas seis execuções preservadas")
    for run in runs:
        grading = read(run / "grading.json")
        expectations = grading["expectations"]
        passed = sum(item["passed"] is True for item in expectations)
        if [e["text"] for e in expectations] != read(run / "eval_metadata.json")["assertions"]:
            raise ValueError("Assertions divergentes")
        if grading["summary"] != {"passed": passed, "failed": len(expectations)-passed,
                                  "total": len(expectations), "pass_rate": passed/len(expectations)}:
            raise ValueError("Contagens divergentes")
    return runs


def aggregate(upstream, runs):
    spec = importlib.util.spec_from_file_location("grill_official_aggregate", upstream / "scripts/aggregate_benchmark.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # Compatibilidade apenas na cópia: upstream não admite métricas null.
    # Removemos todos os substitutos numéricos do resultado antes de salvar.
    with tempfile.TemporaryDirectory(prefix="grill-aggregate-") as d:
        stage = Path(d)
        for run in runs:
            target = stage / run.relative_to(ITERATION)
            target.mkdir(parents=True)
            meta = read(run / "eval_metadata.json")
            (target.parents[1] / "eval_metadata.json").write_bytes(encoded(meta))
            grading = read(run / "grading.json")
            grading["timing"] = {"total_duration_seconds": read(run / "timing.json")["total_duration_seconds"]}
            grading["execution_metrics"] = {}
            (target / "grading.json").write_bytes(encoded(grading))
        benchmark = module.generate_benchmark(stage, "grill-embasado", "skills/grill-embasado")
    benchmark["metadata"].update(executor_model=None, analyzer_model=None, timestamp="2026-10-23",
                                 timestamp_kind="data da avaliação; hora nativa indisponível",
                                 runs_per_configuration=1, cases_per_configuration=3,
                                 time_seconds_kind="observed_wall_clock", human_review_status="pending",
                                 upstream_commit=REVISION)
    for run in benchmark["runs"]:
        run["result"].update(tokens=None, tool_calls=None, errors=None, native_duration_ms=None)
    benchmark["runs"].sort(key=lambda r: (r["eval_id"], r["configuration"] != "with_skill"))
    for condition in ("with_skill", "without_skill"):
        benchmark["run_summary"][condition]["tokens"] = None
    benchmark["run_summary"]["delta"]["tokens"] = None
    benchmark["notes"] = NOTES
    return benchmark


def markdown(benchmark):
    summary = benchmark["run_summary"]
    lines = ["# Ensaio textual — grill-embasado", "", "Uma execução por caso e condição; revisão humana pendente.", "",
             "| Condição | Assertions | Tempo médio de parede observado |", "| --- | --- | --- |"]
    for condition in ("with_skill", "without_skill"):
        runs = [r for r in benchmark["runs"] if r["configuration"] == condition]
        passed = sum(r["result"]["passed"] for r in runs)
        total = sum(r["result"]["total"] for r in runs)
        lines.append(f"| {condition} | {passed}/{total} | {summary[condition]['time_seconds']['mean']:.1f} s |")
    lines.extend(["", "Tokens e duração nativa: indisponíveis.", "",
                  "Dados: [benchmark.json](benchmark.json). Procedimento: [README](../README.md).", ""])
    lines.extend("- " + note for note in NOTES)
    return ("\n".join(lines) + "\n").encode()


def triage():
    sys.path.insert(0, str(ROOT / "skills/grill-embasado/scripts"))
    from perguntas import validate
    base = read(ROOT / "skills/grill-embasado/modelos/pergunta.json")
    results = []
    for case in read(EVALS / "perguntas-plantadas.json"):
        packet = copy.deepcopy(base)
        packet["perguntas"][0]["texto"] = case["texto"]
        result = validate(packet)
        results.append({"id": case["id"], "indutora_rotulada": case["indutora"],
                        "sinalizada": not result["aprovada"], "erros": result["erros"],
                        "suspeitas": result["suspeitas"]})
    return {"indutoras_sinalizadas": sum(c["indutora_rotulada"] and c["sinalizada"] for c in results),
            "indutoras_total": sum(c["indutora_rotulada"] for c in results),
            "neutras_sinalizadas": sum(not c["indutora_rotulada"] and c["sinalizada"] for c in results),
            "neutras_total": sum(not c["indutora_rotulada"] for c in results),
            "limite": "Corpus escrito junto ao validador; não é teste cego ou medida de generalização.",
            "resultados": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-creator", required=True, type=Path)
    parser.add_argument("--check", action="store_true", help="Compara sem alterar artefatos")
    args = parser.parse_args()
    upstream = args.skill_creator.resolve()
    try:
        benchmark = aggregate(upstream, verify(upstream))
        with tempfile.TemporaryDirectory(prefix="grill-viewer-") as d:
            stage = Path(d)
            (stage / "benchmark.json").write_bytes(encoded(benchmark))
            subprocess.run([sys.executable, str(upstream / "eval-viewer/generate_review.py"), str(ITERATION),
                            "--skill-name", "grill-embasado", "--benchmark", str(stage / "benchmark.json"),
                            "--static", str(stage / "avaliacao.html")], check=True, capture_output=True)
            outputs = {ITERATION / "benchmark.json": encoded(benchmark),
                       ITERATION / "benchmark.md": markdown(benchmark),
                       EVALS / "triagem.json": encoded(triage()),
                       EVALS / "avaliacao.html": (stage / "avaliacao.html").read_bytes()}
            for target, content in outputs.items():
                if args.check:
                    if target.read_bytes() != content:
                        raise ValueError("Resultado não reproduzido")
                else:
                    target.write_bytes(content)
        print("OK: seis execuções íntegras; benchmark e viewer " + ("reproduzidos." if args.check else "gerados."))
        return 0
    except (ValueError, OSError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
        print("ERRO: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
