# Pendências e próximos passos

Estado: lacunas do sistema e próximos passos após os alphas de condutora e conselho. Revisão: 2026-10-23.

## Decisões aplicadas e verificações pendentes

| ID | Evidência e impacto | Como encerrar |
| --- | --- | --- |
| P01 — Famílias de modelos | Resolvido para a v1: o usuário selecionou [S11, §§9–10](../sources/originais/plano-conselho-especialistas-revisado.md), revisão de S04. Claude-first, mesmo modelo de juiz escolhido e verificado, sessões não produtoras e óticas distintas. S04 permanece histórico. | Validar operacionalmente a separação de papéis. Diversidade de famílias fica para uma fase posterior; não é bloqueio herdado de S04 para esta v1. |
| P02 — Garantia de acesso e independência | S11 prevê Notion e adaptação para Claude Code. O alpha inclui transporte CLI para rodada 1, mas um diretório temporário e declarações de capacidade não restringem permissões nem demonstram isolamento. | Verificar modelo efetivo, contexto, memória, arquivos, ferramentas e autenticação por ambiente; auditar vazamentos e retomada da segunda rodada. |
| P03 — Critérios numéricos | [S08, §§2–3](../sources/originais/fluxograma-completo-ideal.md) e [S09, §§5 e 10](../sources/originais/concepcao-ideal-solucao.md) incluem doses, distribuição aproximada de esforço, contagens e regras de parada. São escolhas do desenho; a simulação não as calibra empiricamente. | Selecionar parâmetros iniciais e avaliar em casos reais com comparação e registro de mudanças. Não anunciar números como ótimos. |
| P04 — Placar e calibração | Formato local definido: JSONL por hipótese e critério, probabilidade opcional, evento factual explicitado e desfecho com referência. O conselho entrega `conselho/<id>/placar.jsonl`; não sincroniza Markdown. | Obter previsões e desfechos reais para avaliar calibração. Brier exclui falta de probabilidade/desfecho e não transforma escolha de valor em fato. Ajuste automático de templates continua fora da v1. |
| P05 — Responsável por persistir | Resolvido pelo contrato S10/S11: somente a condutora lê/grava o dossiê. O conselho alpha devolve um pacote externo `arquivos`; o registro permanece transação da condutora. | Verificar essa fronteira nas permissões de cada hospedeiro. O recebimento do pacote não aprova hipótese nem avança uma trava. |
| P06 — Independência operacional | S08, §2 distingue crítico da elaboração, verificação técnica e conselho. A dose leve reduz a geração independente; retirar autoria não impede acesso ao contexto. | Especificar separação de contextos por papel e dose, proteção dos casos reservados e critério para invalidar uma avaliação contaminada. |

## Material e implementação ausentes

- A [condutora alpha](implementacao-condutora.md) e o [conselho alpha](implementacao-conselho.md) foram criados a partir de S10/S11. As outras 11 skills continuam planejadas; integrações de plataforma e isolamento real precisam de validação. [S03](../sources/originais/simulacao_etapa1.py) permanece o experimento original, distinto do código dessas skills.
- [S02, §15](../sources/originais/plano-geral-skills-cir.md) referencia planos detalhados de pesquisa, grill e especialistas ainda não fornecidos. O plano da condutora chegou como S10. Links de Notion nos originais não equivalem a conteúdo analisado.
- A origem de [skill-creator, S01](../sources/originais/skill-creator.md) foi confirmada byte a byte com o arquivo oficial da Anthropic em revisão fixa, sob Apache-2.0. Seus auxiliares foram obtidos no workspace para avaliar o conselho, sem vendorização. Procedência no [inventário](../sources/README.md); isso não define a licença do projeto inteiro.
- Há testes locais e avaliações limitadas da [condutora](avaliacao-condutora.md) e do [conselho](avaliacao-conselho.md). Estudo comparativo repetido, avaliação de plataformas e passagem independente para a Etapa 2 seguem pendentes.

## Ordem de trabalho recomendada

1. Desenvolver pesquisa, grill e o tema de propósito, registrando primeiro o propósito geral de cada skill. Preservar os contratos de condutora e conselho e verificar P02 antes de prometer isolamento real.
2. Executar a primeira fatia completa com um caso novo, um caso enviesado por uma solução pronta e uma retomada entre sessões; obter o aceite humano dos temas 0 e 1.
3. Medir aderência, falhas, custo e qualidade; substituir dublês por dependências reais sob os mesmos testes.
4. Expandir os temas e a prova conceitual; exercitar conselho, crítica, relatoria e retomada das sessões num hospedeiro real.
5. Repetir avaliações comparativas e revisar interfaces e documentação a partir de falhas observadas.

Essa sequência é uma proposta desta análise, não uma substituição silenciosa do roadmap de [S02, §14](../sources/originais/plano-geral-skills-cir.md). Os critérios do método continuam em [contratos](contratos.md); o escopo das verificações já realizadas está em [simulação](simulacao.md) e no [log](log.md).
