# Exemplo curto de aplicação

Estado: exemplo didático criado para esta documentação; não é uma execução das skills nem um CIR completo. Revisão: 2026-10-22.

## Entrada

“Quero um aplicativo com notificações para estudantes entregarem trabalhos no prazo.”

O aplicativo e as notificações são formas propostas. O propósito a investigar é permitir que estudantes concluam e entreguem trabalhos no prazo, sem sobrecarga evitável. Prazo, contexto de estudo e necessidades de acessibilidade precisam ser esclarecidos com as pessoas envolvidas; o exemplo não os considera fatos conhecidos.

## Percurso resumido

| Tema | Trabalho ilustrativo |
| --- | --- |
| Entendimento | Separar necessidade, solução sugerida e restrições de implementação. |
| Propósito | Formular o resultado desejado, os beneficiários e as linhas vermelhas; confirmar antes de divergir. |
| Mapa | Mapear compreender a tarefa, planejar, começar, acompanhar e entregar; investigar onde ocorrem falhas. |
| Idealidade | Propor métricas de entrega efetiva, esforço e interrupções; definir o que refutaria a hipótese de melhoria. |
| Como | Explorar famílias de solução, inclusive reduzir a necessidade de lembrar; abstrair notificações para a função “tornar o próximo passo perceptível no momento útil”. |
| Prova | Comparar conceitos em casos de trabalho e reservados, como prazos simultâneos e informação de prazo alterada. |
| CIR | Registrar funções selecionadas, evidências, incertezas e o que a próxima etapa precisa testar. |

## Saída parcial esperada

**Função candidata:** tornar a próxima ação necessária compreensível e perceptível a tempo de executá-la.

**Rastreabilidade:** essa função contribui para concluir o trabalho no prazo. “Enviar uma notificação por aplicativo” permanece uma possibilidade de implementação, sem se tornar obrigação do conceito.

**Hipótese:** a função ajuda sem aumentar interrupções além do aceitável. Continua pendente de evidência; nenhum número de melhoria é atribuído neste exemplo.

**Passagem:** a Etapa 2 investigará quais componentes podem realizar a função; a Etapa 3 poderá escolher aplicativo, integração ou outro produto viável. Uma plataforma sugerida pelo usuário pode ser registrada para esse momento.

Para produzir o artefato completo, siga o [fluxo](fluxo-etapa1.md) e o [contrato do CIR](contratos.md). O exemplo aplica a distinção entre função e forma descrita em [S06, passos 4–7](../sources/originais/metodo-ideal-passo-a-passo.md) e [S09, §§3–5](../sources/originais/concepcao-ideal-solucao.md).
