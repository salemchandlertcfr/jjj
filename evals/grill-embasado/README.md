# Avaliação do grill embasado

Estado: primeira avaliação local e ensaio textual guiado, em 23/10/2026.
Requisitos: [S12, §14](../../sources/originais/plano-grill-embasado.md).
Metodologia: [S01, skill-creator](../../sources/originais/skill-creator.md).

## O que foi executado

Três casos de [evals.json](evals.json): abertura sem solução, desafio com
evidência indireta e checagem com insistência seguida de “chega”. Cada caso
rodou uma vez em sessão separada com a skill e outra sem ela, sem histórico
do autor. O avaliador foi outra sessão, usando o grader oficial. Os nomes
exatos dos modelos não foram disponibilizados: isso não é execução Claude,
comparação cega ou diálogo com um usuário real. Fontes nos prompts são
fictícias/controladas; não se fez pesquisa científica.

| Caso | Com skill | Sem skill |
| --- | --- | --- |
| Abertura | 4/4 | 2/4 |
| Desafio | 4/4 | 4/4 |
| Checagem e parada | 4/4 | 3/4 |

As diferenças observadas foram uma pergunta com várias demandas no baseline,
identificação explícita do cartão como base e sinal de aumento de dose. O
caso 2 empata. A avaliação de base é discutível: o baseline identifica a fala
da pessoa, mas não o cartão exigido pela assertion. O avaliador registrou isso
em `eval_feedback`, além do limite de assertions conjuntas como valor/dose.
Esses juízos aguardam revisão humana; não demonstram superioridade geral.

Veja as saídas no [viewer oficial estático](avaliacao.html) e os dados no
[benchmark](iteration-1/benchmark.json). O viewer permite baixar
`feedback.json`; nenhum feedback humano foi criado pelo agente. Os relatos
em `execution.md` são resumos de ações, não transcrições instrumentadas;
claims de uso de scripts não são auditáveis só por esses relatos. A validação
dos scripts tem evidência separada nos testes locais.

## Métricas e reprodução

`timing.json` registra apenas tempo de parede observado pelos executores,
incluindo leitura e ferramentas; tokens, duração nativa, contagem de chamadas,
erros e identificadores de modelo ficam desconhecidos. Não converter
caracteres em tokens. Uma execução por caso não mede variabilidade.

Os 41 arquivos selecionados estão protegidos pelo [manifesto de hashes](iteration-1/artifacts.sha256).
Com auxiliares externos oficiais de `anthropics/skills`, pasta `skills/skill-creator`,
revisão `dbd4588f9e1033efb41dad4bef2f7947c8993d44`:

```bash
python3 -B scripts/reproduzir_avaliacao_grill.py --skill-creator /caminho/skills/skill-creator
python3 -B scripts/reproduzir_avaliacao_grill.py --skill-creator /caminho/skills/skill-creator --check
```

O script confere os hashes oficiais de agregador/viewer/template, agrega numa
cópia temporária compatível e elimina todas as métricas substitutas antes de
salvar. Também reproduz a triagem lexical das 40 perguntas. Não modifica os seis registros nem chama modelos. O relatório fixa
uma execução por caso, remove nomes de modelo fictícios e preserva tempos
como parede observada. Os auxiliares externos não integram o pacote da skill.

## Triagem lexical e avaliações futuras

As [40 perguntas plantadas](perguntas-plantadas.json) têm 20 indutoras e 20
neutras rotuladas pelo autor. Resultado em [triagem.json](triagem.json): 18
indutoras sinalizadas, duas não detectadas e nenhuma neutra sinalizada. É um
corpus escrito junto ao script, sem separação treino/teste ou julgamento cego;
não estima a taxa de erro em uso real. Julgamento semântico continua necessário.

Os [20 pedidos de acionamento](acionamento.json) e a [persona oculta](persona-oculta.json)
estão preparados, **não executados**. Os testes de avaliação ficam fora do
pacote distribuído para evitar que o grill leia a persona. No ensaio futuro,
só o simulador pode recebê-la; não a inclua em briefs, catálogo ou skill.

Próximas verificações de S12 §14: entrevista completa com persona oculta e
Claude escolhido; revelação/deriva/parada/economia; pares cegos com/sem skill;
uma reflexão por vez versus rodadas; leitor na leve; devolução por partes;
acionamento real e sessões humanas do Motor de Insights. Custos e métricas
serão observados, não inferidos dos alvos do plano.
