#!/usr/bin/env python3
"""Executa avaliadores externos opt-in ou aplica a regra de entrada a resultados preservados."""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import math
import subprocess
from esp_core import array, cli, dump, ident, index, load, refs, require, text


def suite(value):
    require(isinstance(value, dict), "Teste deve ser objeto")
    problems = index(value.get("problemas"))
    inside = [p for p in problems.values() if p.get("escopo") == "dentro"]
    outside = [p for p in problems.values() if p.get("escopo") == "fora"]
    require(5 <= len(inside) <= 10 and 1 <= len(outside) <= 2 and len(inside)+len(outside) == len(problems), "Exige 5–10 problemas dentro e 1–2 fora do escopo")
    require(sum(p.get("variante_nova") is True for p in inside) >= math.ceil(len(inside)/2), "Metade dos problemas internos deve ser variante nova")
    for problem in problems.values():
        text(problem.get("enunciado")); text(problem.get("fonte_gabarito"))
        require(isinstance(problem.get("gabarito"), dict), "Gabarito verificável ou rubrica obrigatória")
    models = refs(value.get("modelos_papeis"))
    require(bool(models), "Declare os modelos dos papéis")
    smaller = ident(value.get("modelo_menor"))
    require(smaller not in models, "Modelo menor deve ser comparação distinta")
    return problems, models, smaller


def gate(value):
    problems, models, smaller = suite(value)
    conditions = ("com", "sem") if value.get("tipo", "nova") == "nova" else ("nova", "anterior")
    require(value.get("tipo", "nova") in {"nova", "revisao"}, "Tipo de admissão inválido")
    scores = {}
    for result in array(value.get("resultados")):
        require(isinstance(result, dict), "Resultado deve ser objeto")
        key = (result.get("modelo"), result.get("problema"), result.get("condicao"), result.get("execucao"))
        require(key[0] in [*models, smaller] and key[1] in problems and key[2] in conditions
                and type(key[3]) is int and 1 <= key[3] <= 3, "Resultado fora da matriz de teste")
        require(key not in scores, "Resultado duplicado")
        score = result.get("acerto")
        require(type(score) in {int, float} and math.isfinite(score) and 0 <= score <= 100, "Acerto deve estar entre 0 e 100")
        if problems[key[1]]["gabarito"].get("tipo") == "rubrica":
            require(len(set(refs(result.get("avaliadores")))) == 2 and result.get("cego") is True, "Rubrica exige dois avaliadores cegos")
        scores[key] = score
    expected = {(m, p, c, r) for m in [*models, smaller] for p in problems for c in conditions for r in (1, 2, 3)}
    require(set(scores) == expected, "Teste incompleto: três execuções por condição, problema e modelo")
    reports = {}
    for model in [*models, smaller]:
        mean = {c: sum(scores[(model, p, c, r)] for p in problems for r in (1, 2, 3))/(len(problems)*3) for c in conditions}
        worse = [p for p in problems if sum(scores[(model, p, conditions[0], r)] < scores[(model, p, conditions[1], r)] for r in (1, 2, 3)) >= 2]
        gain = mean[conditions[0]] - mean[conditions[1]]
        reports[model] = {"medias": mean, "ganho": round(gain, 6), "piora_consistente": worse,
                          "passou": gain >= 10 - 1e-9 and not worse}
    return {"admitir": all(reports[m]["passou"] for m in models), "por_modelo": reports,
            "modelo_menor": smaller, "tipo": value.get("tipo", "nova"),
            "limite": "Regra numérica apenas. Fontes, licenças, revisão, sala limpa e modelo real exigem evidência externa."}


def score_answer(answer, target):
    kind = target.get("tipo")
    if kind == "igual":
        return 100 if type(answer) is type(target.get("valor")) and answer == target.get("valor") else 0
    require(kind == "numero", "Execução automática aceita só gabarito igual ou numérico; rubrica é externa")
    require(type(target.get("min")) in {int, float} and type(target.get("max")) in {int, float}
            and math.isfinite(target["min"]) and math.isfinite(target["max"]) and target["min"] <= target["max"], "Faixa do gabarito inválida")
    return 100 if type(answer) in {int, float} and math.isfinite(answer) and target["min"] <= answer <= target["max"] else 0


def execute(value, config):
    problems, models, smaller = suite(value)
    require(config.get("autorizado") is True, "Execução externa exige autorização explícita na configuração")
    command = array(config.get("comando"))
    require(bool(command) and all(isinstance(a, str) and a for a in command), "Comando deve ser lista de argumentos, sem shell")
    timeout = config.get("timeout", 30)
    require(type(timeout) is int and 1 <= timeout <= 60, "Timeout entre 1 e 60 segundos")
    require(value.get("tipo", "nova") == "nova", "Execução de revisão exige preservar blocos anterior/novo; importe resultados")
    block = text(config.get("bloco"), "Bloco de teste")
    def run(task):
        m, pid, condition, iteration = task
        # Nunca enviar gabarito, fonte do gabarito, escopo ou variante_nova ao executor.
        packet = {"modelo": m, "problema": pid, "enunciado": problems[pid]["enunciado"],
                  "material": block if condition == "com" else "", "execucao": iteration}
        proc = subprocess.run(command, input=json.dumps(packet), text=True, capture_output=True, timeout=timeout)
        require(proc.returncode == 0, "Executor falhou; execução não será convertida em acerto zero")
        require(len(proc.stdout) <= 1_000_000, "Resposta do executor excede limite")
        try:
            output = json.loads(proc.stdout)
        except ValueError as exc:
            from esp_core import EspError
            raise EspError("Executor não devolveu JSON") from exc
        require(isinstance(output, dict) and output.get("modelo") == m and output.get("modelo_verificado") is True, "Modelo efetivo não confirmado pelo adaptador")
        return {"modelo": m, "problema": pid, "condicao": condition, "execucao": iteration,
                "acerto": score_answer(output.get("resposta"), problems[pid]["gabarito"])}
    # Pares com/sem são submetidos juntos; o limite mantém os recursos proporcionais.
    tasks = [(m, p, c, r) for m in [*models, smaller] for p in problems for r in (1, 2, 3) for c in ("com", "sem")]
    try:
        with ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(run, tasks))
    except subprocess.TimeoutExpired as exc:
        from esp_core import EspError
        raise EspError("Executor excedeu timeout; teste permanece incompleto") from exc
    return {**value, "resultados": results}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("entrada"); p.add_argument("--executar", metavar="CONFIG_JSON")
    a = p.parse_args(); value = load(a.entrada)
    if a.executar:
        value = execute(value, load(a.executar))
    result = gate(value)
    print(dump({"avaliacao": result, "resultados": value["resultados"]} if a.executar else result), end="")
    return int(not result["admitir"])


if __name__ == "__main__":
    cli(main)
