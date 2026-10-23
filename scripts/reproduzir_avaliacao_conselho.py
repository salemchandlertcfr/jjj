#!/usr/bin/env python3
"""Reagrega respostas preservadas com os auxiliares oficiais, sem executar modelos."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / 'evals' / 'conselho-especialistas'
ITERATION = EVALS / 'iteration-1'
REVISION = 'dbd4588f9e1033efb41dad4bef2f7947c8993d44'
UPSTREAM_HASHES = {
    'scripts/aggregate_benchmark.py': '123ef128ea5ccc01a4b1ac212ef5567f21e9c13d3d240609780beeb3200c49aa',
    'eval-viewer/generate_review.py': 'fc9d1b9243fe5ab6012ebd579bd76d0035de1b79fd3b969de114defab26478fb',
    'eval-viewer/viewer.html': 'a53213426ee1100441d701a3a0d49cda7a842f992d2c36463f4d3cc0258575fa',
}
NOTES = [
    'Ensaio textual exploratório: três prompts por configuração, uma execução por prompt; 12 assertions por configuração, não 12 execuções independentes.',
    'As duas condições usaram a mesma família de assistentes disponível nesta sessão. Identificadores específicos do executor e do avaliador não foram fornecidos e são null; não é execução Claude em produção.',
    'Time/time_seconds é somente tempo de parede observado localmente. Duração nativa, tokens, chamadas de ferramentas e erros não estão disponíveis e permanecem null. Caracteres não estimam tokens.',
    'Com skill: 12/12; baseline: 11/12. Há empate nos casos 1 e 2. A única diferença é preservar o sinal anterior de M2 na consolidação do caso 3; ambas as condições preservam F-21 e recusam consenso favorável.',
    'O contraexemplo é sustentado por F-21 e pelo critério 12 > 10, independentemente dos votos. O baseline registra a declaração final positiva de M2, mas falha a convenção de consolidação exigida pela primeira assertion.',
    'As premissas e objeções são muito explícitas; o caso 1 com skill declara triagem parcial. Os resultados não demonstram superioridade geral, processo completo, isolamento ou integração com provedores reais.',
    'Os desvios padrão descrevem variação entre os três casos, não repetições ou confiança estatística. Não há transcripts de execução nem métricas nativas.',
    'Revisão humana pendente. O viewer oficial permite baixar feedback.json; ele não foi fabricado nem preenchido pelo avaliador.',
]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8'))


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def verify_inputs(upstream: Path) -> list[Path]:
    for name, expected in UPSTREAM_HASHES.items():
        path = upstream / name
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError(f'Auxiliar oficial ausente ou divergente da revisão {REVISION}: {name}')
    for line in (ITERATION / 'artifacts.sha256').read_text().splitlines():
        expected, name = line.split('  ', 1)
        path = ITERATION / name
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError(f'Artefato de avaliação ausente ou alterado: {name}')
    runs = sorted(ITERATION.glob('eval-*/*/run-1'))
    if len(runs) != 6:
        raise ValueError('Esta iteração exige seis runs preservados: três casos e duas condições.')
    for run in runs:
        metadata = load_json(run / 'eval_metadata.json')
        grading = load_json(run / 'grading.json')
        if [item['text'] for item in grading['expectations']] != metadata['assertions']:
            raise ValueError(f'Assertions diferentes da metadata em {run.name}')
        passed = sum(item['passed'] for item in grading['expectations'])
        total = len(metadata['assertions'])
        if grading['summary'] != dict(passed=passed, failed=total-passed, total=total, pass_rate=passed/total):
            raise ValueError('Contagens de grading inconsistentes.')
    return runs


def aggregate(upstream: Path, runs: list[Path]) -> dict:
    spec = importlib.util.spec_from_file_location('official_aggregate_benchmark', upstream / 'scripts/aggregate_benchmark.py')
    if spec is None or spec.loader is None:
        raise ValueError('Não foi possível carregar o agregador oficial.')
    official = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(official)
    # O upstream não aceita null nas estatísticas. Só na cópia temporária,
    # mapeamos o tempo observado ao campo numérico que ele espera. Não alteramos
    # os registros originais nem alegamos duração nativa. Seu fallback de tokens
    # por caracteres é removido por inteiro antes de gravar o benchmark final.
    with tempfile.TemporaryDirectory(prefix='conselho-aggregate-') as temp:
        stage = Path(temp)
        for run in runs:
            target = stage / run.relative_to(ITERATION)
            target.mkdir(parents=True)
            metadata = load_json(run / 'eval_metadata.json')
            write_json(target / 'eval_metadata.json', metadata)
            write_json(target.parents[1] / 'eval_metadata.json', metadata)
            grading = load_json(run / 'grading.json')
            grading['timing']['total_duration_seconds'] = load_json(run / 'timing.json')['observed_wall_seconds']
            write_json(target / 'grading.json', grading)
        benchmark = official.generate_benchmark(stage, 'conselho-especialistas', 'skills/conselho-especialistas')
    last_finish = max(datetime.fromisoformat(load_json(run / 'timing.json')['observed_finished_at'].replace('Z', '+00:00')) for run in runs)
    benchmark['metadata'].update({
        'executor_model': None,
        'analyzer_model': None,
        'timestamp': last_finish.astimezone(timezone.utc).isoformat().replace('+00:00', 'Z'),
        'timestamp_kind': 'último término de execução observado localmente',
        'runs_per_configuration': 1,
        'cases_per_configuration': 3,
        'time_seconds_kind': 'observed_local_wall_time',
        'native_duration_ms': None,
        'human_review_status': 'pending',
        'upstream_commit': REVISION,
        'aggregation_method': 'generate_benchmark oficial em cópia temporária compatível; sanitização local explícita de métricas indisponíveis',
    })
    for run in benchmark['runs']:
        run['result'].update(tokens=None, tool_calls=None, errors=None, native_duration_ms=None)
    benchmark['runs'].sort(key=lambda run: (run['eval_id'], run['configuration'] != 'with_skill', run['run_number']))
    for config in ('with_skill', 'without_skill'):
        benchmark['run_summary'][config]['tokens'] = None
    benchmark['run_summary']['delta']['tokens'] = None
    benchmark['notes'] = NOTES
    return benchmark


def markdown(benchmark: dict) -> str:
    summary = benchmark['run_summary']
    a, b = summary['with_skill'], summary['without_skill']
    def stat(value: dict, percentage: bool = False) -> str:
        factor = 100 if percentage else 1
        return f"{value['mean']*factor:.2f} ± {value['stddev']*factor:.2f}" + ('%' if percentage else ' s')
    lines = [
        '# Benchmark textual — conselho-especialistas', '',
        'Três casos por configuração; uma execução por caso. Revisão humana pendente.', '',
        '| Métrica | Com skill | Sem skill | Diferença |',
        '| --- | --- | --- | --- |',
        f"| Assertions | 12/12 | 11/12 | 1 assertion |",
        f"| Aprovação média por caso | {stat(a['pass_rate'], True)} | {stat(b['pass_rate'], True)} | +8,33 pontos percentuais |",
        f"| Tempo de parede observado | {stat(a['time_seconds'])} | {stat(b['time_seconds'])} | {summary['delta']['time_seconds']} s |",
        '| Duração nativa | Não disponível | Não disponível | Não disponível |',
        '| Tokens | Não disponível | Não disponível | Não disponível |', '',
        'O desvio padrão é entre casos diferentes. Não representa replicações nem intervalo de confiança.', '',
        'Dados: [benchmark.json](benchmark.json). Método, evidências e reprodução: [README](../README.md).', '',
    ]
    lines.extend('- ' + note for note in NOTES)
    return '\n'.join(lines) + '\n'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skill-creator', type=Path, required=True, help='Pasta skills/skill-creator da revisão oficial fixada; sem instalação global.')
    parser.add_argument('--check', action='store_true', help='Regenera em pasta temporária e compara; não altera os artefatos.')
    args = parser.parse_args()
    upstream = args.skill_creator.resolve()
    try:
        runs = verify_inputs(upstream)
        benchmark = aggregate(upstream, runs)
        with tempfile.TemporaryDirectory(prefix='conselho-review-') as temp:
            generated = Path(temp)
            write_json(generated / 'benchmark.json', benchmark)
            (generated / 'benchmark.md').write_text(markdown(benchmark), encoding='utf-8')
            subprocess.run([
                sys.executable, str(upstream / 'eval-viewer/generate_review.py'), str(ITERATION),
                '--skill-name', 'conselho-especialistas', '--benchmark', str(generated / 'benchmark.json'),
                '--static', str(generated / 'avaliacao.html'),
            ], check=True, capture_output=True, text=True)
            if '/workspace/' in (generated / 'avaliacao.html').read_text():
                raise ValueError('O viewer contém caminho absoluto da sessão.')
            for name, target in [('benchmark.json', ITERATION / 'benchmark.json'), ('benchmark.md', ITERATION / 'benchmark.md'), ('avaliacao.html', EVALS / 'avaliacao.html')]:
                content = (generated / name).read_bytes()
                if args.check:
                    if not target.exists() or target.read_bytes() != content:
                        raise ValueError(f'Artefato não reproduzido: {target.relative_to(ROOT)}')
                else:
                    target.write_bytes(content)
        print('OK: seis runs íntegros; agregação oficial sanitizada e viewer ' + ('reproduzidos.' if args.check else 'gerados.'))
        return 0
    except (OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError) as error:
        print(f'ERRO: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
