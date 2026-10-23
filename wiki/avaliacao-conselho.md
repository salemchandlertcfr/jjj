# Avaliação do conselho

Estado: verificação local do alpha e comparação textual exploratória; revisão humana pendente. Revisão: 2026-10-23. Para instalar ou executar o pacote, consulte a [implementação do conselho](implementacao-conselho.md).

## Método e artefatos

A avaliação segue [S01 — skill-creator, seção “Running and evaluating test cases”](../sources/originais/skill-creator.md#running-and-evaluating-test-cases): casos com e sem skill, critérios verificáveis, julgamento por evidência, agregação e apresentação das respostas para revisão. A fonte original foi preservada; sua proveniência está no [inventário](../sources/README.md). Os auxiliares oficiais de julgamento, agregação e visualização foram obtidos na revisão fixa [`dbd4588f9e1033efb41dad4bef2f7947c8993d44`](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator), sem incorporar esses arquivos upstream ao repositório.

A iteração 1 reúne três casos fictícios por configuração, com uma execução por caso: **N = 3 com skill e N = 3 sem skill**, seis respostas ao todo. Os mesmos enunciados e quatro verificações por caso foram aplicados às duas condições. As fichas mencionadas são dados fornecidos nos exercícios; não representam pesquisa externa. O julgamento considera as respostas produzidas e cita evidência para cada resultado.

As duas condições usaram a mesma família do assistente disponível; o modelo específico não foi registrado. Esta comparação não executou Claude em produção, provedores reais ou um conselho completo de sessões independentes. Os resultados, critérios e limites estão no [README da avaliação](../evals/conselho-especialistas/README.md); o [visualizador oficial](../evals/conselho-especialistas/avaliacao.html) permite examinar as respostas antes de aceitar as notas. A revisão humana permanece pendente.

## Resultado observado

| Caso | Com skill | Sem skill | Observação |
| --- | --- | --- | --- |
| Falha fatal | 4/4 | 4/4 | Ambas identificam a impossibilidade de receber evento novo sem canal e preservam a hipótese condicionada à conexão. |
| Dissenso minoritário | 4/4 | 4/4 | Ambas preservam o dissenso e seus fundamentos, sem converter maioria em prova. |
| Troca sem evidência | 4/4 | 3/4 | A diferença está no sinal consolidado de M2 após uma mudança motivada por concordância. |
| Total | **12/12** | **11/12** | Uma diferença em doze verificações por configuração. |

No terceiro caso, os sinais originais eram `+, −, +`. M2 declarou depois `+`, sem medição nova ou correção de F-21. A resposta sem skill registra a sequência final `+, +, +`; a resposta com skill registra a tentativa de mudança, mas preserva `−` na consolidação. Ambas mantêm F-21, o pedido de doze minutos diante do limite decisivo de dez, e recusam registrar consenso favorável. A razão substantiva é esse contraexemplo, não a contagem de votos.

O [benchmark JSON](../evals/conselho-especialistas/iteration-1/benchmark.json) e o [relatório Markdown](../evals/conselho-especialistas/iteration-1/benchmark.md) guardam a agregação. Tokens e duração nativos estão indisponíveis, representados por `null`; há somente tempo de parede observado e identificado como tal. Esses registros não permitem concluir vantagem de custo ou velocidade.

## Cobertura e próximos exames

Os casos são guiados e tornam explícitas as premissas relevantes. O empate nos dois primeiros limita o poder de distinguir as condições. No primeiro, a resposta com skill também declara triagem parcial: não executou crítico separado nem segundo refutador independente. A nota verifica o conteúdo pedido pelas quatro assertions; não certifica uma triagem padrão concluída. São necessários casos menos direcionados, repetições e revisão humana antes de qualquer conclusão geral sobre benefício da skill.

Os testes determinísticos em [entrada](../tests/test_conselho_entrada.py), [resultados](../tests/test_conselho_resultados.py), [revisão](../tests/test_conselho_revisao.py), [placar](../tests/test_conselho_placar.py) e [integração](../tests/test_conselho_integracao.py) verificam contratos, preservação de dissenso, rejeição de mudanças sem evidência, limites do transporte e recebimento pela condutora. Esse escopo é separado da comparação textual; não demonstra pesquisa correta, isolamento real, qualidade científica ou integração de plataforma.

A verificação final passou **143 testes**: 77 do conselho e 66 já existentes. O pacote extraído executou a preparação fora do repositório. Permanecem sem medir os alvos de S11 §14 para detecção/falso alarme, lastro científico, cegueira, autopreferência, viés de posição, estabilidade em três repetições, neutralidade cega e acionamento. O caso Motor de Insights também depende do documento e do Anexo A, ausentes dos anexos recebidos. As metas não são resultados deste alpha.

Consulte o [procedimento de reprodução](../scripts/reproduzir_avaliacao_conselho.py) e execute, na raiz, `python3 -m unittest discover -s tests -v` e `python3 scripts/verificar_documentacao.py`. Os artefatos permitem auditar o observado; esta iteração não demonstra superioridade geral nem encerra a avaliação do método.
