# Benchmark textual — conselho-especialistas

Três casos por configuração; uma execução por caso. Revisão humana pendente.

| Métrica | Com skill | Sem skill | Diferença |
| --- | --- | --- | --- |
| Assertions | 12/12 | 11/12 | 1 assertion |
| Aprovação média por caso | 100.00 ± 0.00% | 91.67 ± 14.43% | +8,33 pontos percentuais |
| Tempo de parede observado | 46.39 ± 6.83 s | 25.42 ± 5.56 s | +21.0 s |
| Duração nativa | Não disponível | Não disponível | Não disponível |
| Tokens | Não disponível | Não disponível | Não disponível |

O desvio padrão é entre casos diferentes. Não representa replicações nem intervalo de confiança.

Dados: [benchmark.json](benchmark.json). Método, evidências e reprodução: [README](../README.md).

- Ensaio textual exploratório: três prompts por configuração, uma execução por prompt; 12 assertions por configuração, não 12 execuções independentes.
- As duas condições usaram a mesma família de assistentes disponível nesta sessão. Identificadores específicos do executor e do avaliador não foram fornecidos e são null; não é execução Claude em produção.
- Time/time_seconds é somente tempo de parede observado localmente. Duração nativa, tokens, chamadas de ferramentas e erros não estão disponíveis e permanecem null. Caracteres não estimam tokens.
- Com skill: 12/12; baseline: 11/12. Há empate nos casos 1 e 2. A única diferença é preservar o sinal anterior de M2 na consolidação do caso 3; ambas as condições preservam F-21 e recusam consenso favorável.
- O contraexemplo é sustentado por F-21 e pelo critério 12 > 10, independentemente dos votos. O baseline registra a declaração final positiva de M2, mas falha a convenção de consolidação exigida pela primeira assertion.
- As premissas e objeções são muito explícitas; o caso 1 com skill declara triagem parcial. Os resultados não demonstram superioridade geral, processo completo, isolamento ou integração com provedores reais.
- Os desvios padrão descrevem variação entre os três casos, não repetições ou confiança estatística. Não há transcripts de execução nem métricas nativas.
- Revisão humana pendente. O viewer oficial permite baixar feedback.json; ele não foi fabricado nem preenchido pelo avaliador.
