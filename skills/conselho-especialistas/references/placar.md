# Placar de previsões e desfechos

Base: S11 §§6.9, 8, 14 e 16. O placar registra para aprender com desfechos;
não ajusta automaticamente templates nem decide quem venceu um conselho.

Registre por célula: conselho, membro, ótica/especialidade, modelo efetivo no
registro privado, hipótese anônima, critério, sinal, probabilidade opcional de
resistir ao `refuta_se` e o que mudaria o julgamento. A origem só se vincula pela
chave depois da decisão humana, quando necessário para avaliar autopreferência.
Antes disso, o placar apresentado não revela origem nem modelo.

Defina o evento como resistência ao `refuta_se` daquele critério, sem trocar sua
definição depois de observar o resultado. Registre probabilidade de 0 a 1 ou
`null`; ela é opcional, especialmente fora dos critérios decisivos. Não converta
`+`, `0`, `-` ou `?` em probabilidades inventadas.

Um desfecho exige fato observável, booleano explícito, fonte e referência de
conferência. Pode vir do tema 5, critério de pronto, Etapas 2 e 3 ou fato novo.
Escolha do usuário por valor, objetivo ou preferência é um registro separado;
discordar da matriz não demonstra erro factual do conselho. A condutora registra
essa decisão, motivo e objetivo sem transformá-la em `desfecho:true/false`.

Calcule Brier somente quando probabilidade e desfecho observado estiverem
presentes: `(prob_resistir - resultado)^2`, com resultado 1 para resistiu e 0
para não resistiu. Informe quantidade de eventos válidos e excluídos. Ausência
de desfecho não é acerto, erro nem zero. Compare óticas/modelos somente com
contexto e cobertura, sem fazer ranking geral das hipóteses em avaliação.

Consulte `python3 <raiz-da-skill>/scripts/placar.py --help` para registro e
cálculo efetivos. A condutora incorpora as linhas em `conselho/placar.jsonl`;
o conselho devolve dados em seu pacote externo, sem escrever no dossiê.
