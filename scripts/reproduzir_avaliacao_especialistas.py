#!/usr/bin/env python3
"""Reproduz agregação oficial dos seis ensaios preservados de recrutamento."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals/especialistas"
ITERATION = EVALS / "iteration-1"
REVISION = "dbd4588f9e1033efb41dad4bef2f7947c8993d44"
HASHES = {
    "scripts/aggregate_benchmark.py": "123ef128ea5ccc01a4b1ac212ef5567f21e9c13d3d240609780beeb3200c49aa",
    "eval-viewer/generate_review.py": "fc9d1b9243fe5ab6012ebd579bd76d0035de1b79fd3b969de114defab26478fb",
    "eval-viewer/viewer.html": "a53213426ee1100441d701a3a0d49cda7a842f992d2c36463f4d3cc0258575fa",
}


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def raw(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+"\n").encode()


def generate(upstream):
    for name, expected in HASHES.items():
        if hashlib.sha256((upstream/name).read_bytes()).hexdigest() != expected:
            raise ValueError("Auxiliar oficial diverge da revisão fixada")
    for line in (ITERATION/"artifacts.sha256").read_text().splitlines():
        expected, name = line.split("  ",1); path = (ITERATION/name).resolve()
        if not path.is_relative_to(ITERATION) or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError("Artefato de avaliação divergente")
    runs = sorted(ITERATION.glob("eval-*/*/run-1"))
    if len(runs) != 6:
        raise ValueError("Esperadas seis execuções")
    spec = importlib.util.spec_from_file_location("official_esp_aggregate",upstream/"scripts/aggregate_benchmark.py")
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    with tempfile.TemporaryDirectory(prefix="especialistas-aggregate-") as d:
        stage = Path(d)
        for run in runs:
            target = stage/run.relative_to(ITERATION); target.mkdir(parents=True)
            meta = read(run/"eval_metadata.json"); grading = read(run/"grading.json")
            passed = sum(e["passed"] is True for e in grading["expectations"]); total = len(grading["expectations"])
            if [e["text"] for e in grading["expectations"]] != meta["assertions"] or grading["summary"] != {"passed":passed,"failed":total-passed,"total":total,"pass_rate":passed/total}:
                raise ValueError("Assertions/contagens divergentes")
            (target.parents[1]/"eval_metadata.json").write_bytes(raw(meta))
            # Compatibilidade só na cópia temporária: upstream não admite null.
            grading["timing"] = {"total_duration_seconds":read(run/"timing.json")["total_duration_seconds"]}
            grading["execution_metrics"] = {}
            (target/"grading.json").write_bytes(raw(grading))
        benchmark = module.generate_benchmark(stage,"especialistas","skills/especialistas")
    benchmark["metadata"].update(executor_model=None,analyzer_model=None,timestamp="2026-10-23",
        timestamp_kind="data do ensaio; hora nativa indisponível",runs_per_configuration=1,cases_per_configuration=3,
        human_review_status="pending",upstream_commit=REVISION,time_seconds_kind="observed_wall_clock")
    for run in benchmark["runs"]:
        run["result"].update(observed_interval_seconds=run["result"]["time_seconds"],
                             time_seconds=None,tokens=None,tool_calls=None,errors=None,native_duration_ms=None)
    benchmark["runs"].sort(key=lambda r:(r["eval_id"],r["configuration"]!="with_skill"))
    for condition in ("with_skill","without_skill"):
        benchmark["run_summary"][condition]["tokens"] = None
        benchmark["run_summary"][condition]["time_seconds"] = None
    benchmark["run_summary"]["delta"]["tokens"] = None
    benchmark["run_summary"]["delta"]["time_seconds"] = None
    benchmark["notes"] = [
        "Três casos guiados, uma execução por condição e caso; 12 assertions não são 12 execuções independentes.",
        "Assistentes desta sessão, com modelo exato indisponível; não é execução Claude, comparação cega ou curadoria de esp real.",
        "Os prompts explicitam várias regras. Resultado mede adesão textual nesta rubrica, não diversidade real, identificabilidade ou qualidade de especialistas.",
        "Janelas de tempo diferentes: alguns registros excluem leitura inicial. Intervalos observados são preservados, mas não há média/delta de tempo comparável. Tokens, duração nativa, chamadas e erros indisponíveis.",
        "Relatos execution.md não são transcrições instrumentadas. Revisão humana pendente; nenhum feedback humano foi fabricado."]
    return benchmark


def markdown(value):
    lines=["# Ensaio textual — especialistas","","Uma execução por caso e condição. Revisão humana pendente.","",
           "| Condição | Assertions | Tempo médio observado |","| --- | --- | --- |"]
    for condition in ("with_skill","without_skill"):
        runs=[r for r in value["runs"] if r["configuration"]==condition]
        lines.append(f"| {condition} | {sum(r['result']['passed'] for r in runs)}/{sum(r['result']['total'] for r in runs)} | Não comparável |")
    lines += ["","[Dados](benchmark.json) · [Método e limites](../README.md)",""]
    lines += ["- "+n for n in value["notes"]]
    return ("\n".join(lines)+"\n").encode()


def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("--skill-creator",type=Path,required=True); p.add_argument("--check",action="store_true")
    a=p.parse_args()
    try:
        value=generate(a.skill_creator.resolve())
        with tempfile.TemporaryDirectory(prefix="especialistas-viewer-") as d:
            stage=Path(d); (stage/"benchmark.json").write_bytes(raw(value))
            subprocess.run([sys.executable,str(a.skill_creator/"eval-viewer/generate_review.py"),str(ITERATION),"--skill-name","especialistas","--benchmark",str(stage/"benchmark.json"),"--static",str(stage/"avaliacao.html")],check=True,capture_output=True)
            outputs={ITERATION/"benchmark.json":raw(value),ITERATION/"benchmark.md":markdown(value),EVALS/"avaliacao.html":(stage/"avaliacao.html").read_bytes()}
            for path, content in outputs.items():
                if a.check:
                    if path.read_bytes()!=content: raise ValueError("Resultado não reproduzido")
                else: path.write_bytes(content)
        print("OK: seis execuções íntegras; agregação e viewer "+("reproduzidos." if a.check else "gerados."));return 0
    except (ValueError,OSError,KeyError,TypeError,subprocess.CalledProcessError) as e:
        print("ERRO: "+str(e),file=sys.stderr);return 1


if __name__=="__main__":
    raise SystemExit(main())
