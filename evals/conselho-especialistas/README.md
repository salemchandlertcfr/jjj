# Avaliação textual do conselho

A [iteração 1](iteration-1/) preserva três casos fictícios, cada um executado uma vez com a skill e uma vez sem ela. A avaliação usa a metodologia de [S01, skill-creator](../../sources/originais/skill-creator.md), com grader, agregador e viewer oficiais de `anthropics/skills` na revisão `dbd4588f9e1033efb41dad4bef2f7947c8993d44`. Os auxiliares de terceiros foram usados externamente, sem instalação global nem inclusão no repositório.

Abra o [viewer oficial estático](avaliacao.html) para comparar as seis respostas, os julgamentos e o benchmark. O resultado e seus limites estão na [avaliação do conselho](../../wiki/avaliacao-conselho.md). A revisão humana permanece pendente; no viewer, `Submit All Reviews` baixa um `feedback.json`, que deve ser guardado na pasta da iteração antes de iniciar outra rodada. Nenhum feedback humano foi presumido ou fabricado.

## Resultado e limites

| Caso | Com skill | Sem skill |
| --- | ---: | ---: |
| Falha fatal | 4/4 | 4/4 |
| Dissenso minoritário | 4/4 | 4/4 |
| Troca sem evidência | 4/4 | 3/4 |
| Total | 12/12 | 11/12 |

A diferença é restrita à primeira assertion do terceiro caso: o baseline registra o `+` declarado por M2 como voto final, enquanto a regra avaliada exige registrar a tentativa e preservar seu `−` anterior por falta de evidência nova. Ambas as respostas mantêm F-21 e recusam consenso favorável. Os votos não determinam a validade do contraexemplo de doze minutos.

São três respostas por configuração, **uma execução por caso**, e não três repetições de cada caso. As duas condições usaram a mesma família de assistentes disponível; os identificadores específicos não foram fornecidos. Não foi execução Claude em produção nem teste de provedores, pesquisa ou sessões reais do conselho. As premissas já explicitam boa parte das objeções; o ensaio 1 com skill admite triagem parcial. Não há evidência de superioridade geral.

Tokens, duração nativa, chamadas de ferramentas e erros não estão disponíveis e permanecem `null`. Os segundos apresentados em `time_seconds` e no viewer são apenas tempo de parede observado localmente. Os desvios padrão descrevem variação entre casos diferentes, sem confiança estatística. Caracteres foram contados somente como caracteres, sem estimar tokens.

## Dados preservados

Os [prompts e assertions](evals.json) não foram alterados após as respostas. Cada diretório `iteration-1/eval-*/{with_skill,without_skill}/run-1/` contém `prompt.txt`, `eval_metadata.json`, `outputs/resposta.md`, `grading.json` e `timing.json`. Há também metadata no nível do caso para o agregador. Os três arquivos de timing originalmente produzidos em `outputs/` foram preservados e copiados, byte a byte, para o nível do run. As seis respostas são as saídas originais.

O [manifesto SHA-256](iteration-1/artifacts.sha256) permite conferir os 36 arquivos selecionados. O [benchmark JSON](iteration-1/benchmark.json) e seu [resumo legível](iteration-1/benchmark.md) são derivados. Os casos de [fixtures](fixtures/README.md) exercitam mecanismos determinísticos separados; não são as respostas desta comparação textual. Não há transcripts instrumentados para verificar independentemente claims de processo.

## Reproduzir benchmark e viewer

Com Python 3.10+ e uma cópia externa da pasta `skills/skill-creator` na revisão fixa acima, execute na raiz:

```bash
python3 scripts/reproduzir_avaliacao_conselho.py \
  --skill-creator /caminho/anthropics-skills/skills/skill-creator
python3 scripts/reproduzir_avaliacao_conselho.py \
  --skill-creator /caminho/anthropics-skills/skills/skill-creator --check
python3 scripts/verificar_documentacao.py
```

O [script local](../../scripts/reproduzir_avaliacao_conselho.py) confere os hashes dos três auxiliares oficiais utilizados e dos dados preservados. Invoca `generate_benchmark` oficial em cópia temporária: apenas nessa cópia, mapeia segundos observados ao campo numérico esperado pelo agregador, que não aceita `null` nas estatísticas. O fallback upstream que usa caracteres como tokens é removido antes de gravar os resultados; tokens desconhecidos ficam `null` por run, em ambos os resumos e no delta. Também corrige `runs_per_configuration` para `1` e os modelos desconhecidos para `null`.

O viewer é gerado pelo `generate_review.py` oficial, com a pasta da iteração deste repositório e o benchmark sanitizado; não contém links absolutos da sessão. `--check` regenera em diretório temporário e compara os três artefatos derivados sem alterá-los. O comando não chama modelos, não refaz as respostas nem demonstra que mudanças posteriores na skill conservam esses resultados. As lacunas identificadas devem orientar novos casos depois da revisão humana, sem editar retroativamente assertions ou respostas desta rodada.
