# Execução — caso 1, com skill, run 1

- Caso executado: `id: 1`, `abertura-sem-solucao`. Foi extraído apenas esse caso de `evals.json`; os demais casos não foram exibidos nem utilizados.
- Skill lida: `/workspace/jjj/skills/grill-embasado/SKILL.md`.
- Referências lidas: `origem.md`, `modos.md`, `formatos.md`, `adaptador.md`, `tipos.md`, `casos.md`, `qualidade.md` e `indutoras.md`. Também foi lido `modelos/pergunta.json`.
- Foi consultado `python3 -B scripts/perguntas.py --help`. Após um alerta, foram lidos trechos de `scripts/perguntas.py` e localizada a regra correspondente em arquivos locais da skill.
- Foi criado um envelope JSON temporário em `/tmp`, com modo abertura, dose padrão, cartão e mensagem originais, mapa de lacunas e uma pergunta do tipo `evidencia`. O prompt do caso não foi reescrito.
- Primeira validação: `python3 -B scripts/perguntas.py <entrada temporária>`, a partir da pasta da skill; código de saída 1, `aprovada: false`, `erros: []`, `suspeitas: ["pergunta-dupla"]`, `pendentes: ["pergunta-dupla"]`. Essa reprovação foi preservada neste registro.
- A suspeita veio da expressão literal `e quando` do cartão reproduzido na base da mensagem. Foi registrada a justificativa: O padrão foi acionado por "e quando" no trecho literal do cartão citado em Base. A única pergunta dirigida à pessoa pede o relato de uma situação vivida; a citação da base não acrescenta uma segunda pergunta.
- Segunda validação, com a mesma pergunta e uma tentativa reprovada declarada: código de saída 0, `aprovada: true`, `erros: []`, `suspeitas: ["pergunta-dupla"]`, `pendentes: []`. A suspeita permaneceu explícita e justificada.
- A mensagem renderizada pelo validador foi salva integralmente em `outputs/mensagem.md` e relida para conferir a gravação.
- Não foram realizadas perguntas reais ao usuário, pesquisas externas, simulação de resposta da pessoa, alterações de código, registro no dossiê ou ações de Git. Os diretórios temporários foram removidos automaticamente.

## Limitações

A validação é estrutural e lexical. O caso cobre somente a próxima mensagem de abertura; não demonstra a qualidade de uma entrevista real nem o entendimento completo do job. Não houve pesquisa, leitor independente ou encerramento da entrevista. Tokens, duração de ferramenta e modelo não foram inventados; `timing.json` usa somente a diferença entre leituras de relógio UTC observadas para a duração total.
