# Ensaio textual — especialistas

Uma execução por caso e condição. Revisão humana pendente.

| Condição | Assertions | Tempo médio observado |
| --- | --- | --- |
| with_skill | 12/12 | Não comparável |
| without_skill | 12/12 | Não comparável |

[Dados](benchmark.json) · [Método e limites](../README.md)

- Três casos guiados, uma execução por condição e caso; 12 assertions não são 12 execuções independentes.
- Assistentes desta sessão, com modelo exato indisponível; não é execução Claude, comparação cega ou curadoria de esp real.
- Os prompts explicitam várias regras. Resultado mede adesão textual nesta rubrica, não diversidade real, identificabilidade ou qualidade de especialistas.
- Janelas de tempo diferentes: alguns registros excluem leitura inicial. Intervalos observados são preservados, mas não há média/delta de tempo comparável. Tokens, duração nativa, chamadas e erros indisponíveis.
- Relatos execution.md não são transcrições instrumentadas. Revisão humana pendente; nenhum feedback humano foi fabricado.
