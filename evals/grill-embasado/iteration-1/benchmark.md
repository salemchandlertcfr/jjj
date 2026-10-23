# Ensaio textual — grill-embasado

Uma execução por caso e condição; revisão humana pendente.

| Condição | Assertions | Tempo médio de parede observado |
| --- | --- | --- |
| with_skill | 12/12 | 83.0 s |
| without_skill | 9/12 | 34.3 s |

Tokens e duração nativa: indisponíveis.

Dados: [benchmark.json](benchmark.json). Procedimento: [README](../README.md).

- Ensaio textual exploratório: três prompts por condição, uma execução por prompt. As 12 assertions não são 12 execuções independentes.
- Execução e avaliação usaram assistentes desta sessão; modelo exato indisponível. Isto não é validação em Claude, avaliação cega, persona oculta ou conversa real com usuário.
- Tempo é parede observada pelo executor, incluindo leitura e ferramentas; duração nativa, tokens, chamadas e erros são desconhecidos. Caracteres não são tokens.
- O caso 2 empata. As diferenças dos casos 1 e 3 são unicidade da pergunta, identificação do cartão como base e sinal de dose. A rubrica de identificação da base admite revisão humana.
- Os prompts tornam várias regras explícitas. Assertions conjuntas, como valor e dose, reduzem a precisão da atribuição; veja eval_feedback de cada execução.
- A skill passou em 12/12 e o baseline em 9/12 nesta rubrica; a amostra não demonstra benefício geral, revelação, ausência de deriva ou parada adequada numa entrevista completa.
- O desvio padrão é entre três casos diferentes, sem repetições. Revisão humana pendente; feedback não foi fabricado.
