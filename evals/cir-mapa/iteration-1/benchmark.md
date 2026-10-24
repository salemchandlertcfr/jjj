# Ensaio textual — cir-mapa

Uma execução por caso e condição. Revisão humana pendente.

| Condição | Assertions | Tempo |
| --- | --- | --- |
| with_skill | 11/12 | Desconhecido |
| without_skill | 6/12 | Desconhecido |

[Dados](benchmark.json) · [Método e limites](../README.md)

- Três casos guiados, uma execução por condição e caso; 12 assertions não são 12 execuções independentes.
- Assistentes desta sessão, com modelo exato indisponível; não é execução Claude ou comparação cega.
- Os prompts explicitam várias regras. Resultado mede adesão textual nesta rubrica, sem demonstrar qualidade causal, pesquisa ou isolamento.
- Tokens, tempo, duração nativa, chamadas e erros indisponíveis; nenhum valor foi estimado. Zeros necessários ao auxiliar upstream existem só na cópia temporária e são removidos antes de salvar.
- Relatos execution.md não são transcrições instrumentadas. Revisão humana pendente; nenhum feedback humano foi fabricado.
- A condição com skill ocorreu enquanto formatos.md ainda era escrito; não é avaliação da interface CLI final.
- Expectativas compostas são rígidas: o 0/4 da baseline no caso 2 não significa quatro conclusões falsas. A falha com skill no caso 3 é a ausência de pedido explícito de casos não expostos; o texto preserva a cronologia do congelamento.
