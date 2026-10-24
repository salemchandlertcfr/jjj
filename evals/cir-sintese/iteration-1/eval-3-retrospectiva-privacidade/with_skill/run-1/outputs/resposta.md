# Proposta de retrospectiva

Esta minuta se baseia apenas nos registros apresentados. Não presume aprovação do CIR, verificação de commits ou realização de reuniões. Para formalizar a retrospectiva no fluxo 6.6, ainda precisam existir o “sim” da pessoa à versão identificada por commit e às ressalvas, e a avaliação dela sobre o método, registrada antes de receber o relatório. Aqui, esses elementos não foram fornecidos.

## Decisões e desfechos

| Decisão | O que se sabia quando foi tomada | Qualidade da decisão | Desfecho |
| --- | --- | --- | --- |
| D1 — opção A | O registro anterior informa evidência favorável, restrições satisfeitas e motivo da escolha registrado. | Boa decisão à luz das informações fornecidas e disponíveis naquele momento. | Falhou por uma enchente descrita como imprevisível. O resultado ruim não transforma esse processo em erro. |
| D2 — opção B | Havia uma restrição conhecida que foi ignorada. Não havia previsão registrada. | Decisão com falha no processo, pela violação da restrição conhecida. | Terminou bem por acaso. O resultado favorável não valida a decisão nem elimina a violação. |

Em D1, manter a prática de registrar evidências, restrições e motivo antes da escolha. A enchente pode motivar uma pergunta sobre a pertinência de rever a análise de riscos futura; não autoriza afirmar que era previsível ou que deveria ter sido prevista. Em D2, apurar por que a restrição foi ignorada: o enunciado não demonstra que a causa tenha sido comunicação.

## Expectativa ausente em D2

Não aceitar a reconstrução feita vendo o resultado como “previsão”. Ela pode constar como comentário retrospectivo, identificado como produzido após o desfecho, mas não sustenta uma comparação entre previsto e ocorrido.

Se for necessária uma reconstrução, a proposta é entregar apenas o material disponível na época a um reconstrutor que não conheça o desfecho. O resultado deve ser rotulado **reconstrução cega posterior**, preservando sua diferença em relação a uma previsão contemporânea. O autor que já viu o resultado não satisfaz essa condição. Nenhuma reconstrução foi realizada aqui; se não houver condições de cegamento, a expectativa de D2 permanece ausente.

Não há probabilidades numéricas anteriores informadas para D1 ou D2. Portanto, não há base para calcular Brier ou inventar uma pontuação de calibração.

## Aprendizado e privacidade

Como Lago Azul é um **projeto de teste**, a proposta é excluir integralmente sua participação no aprendizado entre projetos: nenhuma linha, métrica agregada ou versão anonimizada deve ser inserida a partir deste ensaio. O nome, o custo de domínio 780 e as 19 amostras também não devem ser transportados. As 19 amostras não equivalem a 19 projetos e não habilitam uma mediana entre projetos.

Para projetos reais aprovados, a regra futura é transportar somente métricas de método e códigos expressamente permitidos, sem conteúdo de domínio. Isso não cria uma exceção para este projeto de teste. Não há fundamento para afirmar que algo já foi exportado, excluído ou publicado.

## Melhorias propostas

“Melhorar a comunicação” ainda não define uma ação verificável. Proponho os seguintes encaminhamentos, com responsáveis por papel, sujeitos à designação:

| Ação específica | Dono proposto | Skill e seção de destino | Como conferir |
| --- | --- | --- | --- |
| Usar uma tabela de revisão com campos separados para evidências anteriores, restrições conhecidas, qualidade da decisão e desfecho; registrar a violação de D2 e a pergunta sobre sua causa sem atribuir uma causa não demonstrada. | Condutora | `cir-sintese`, 6.6; `references/retrospectiva.md` | A revisão deve preservar D1 como decisão bem fundamentada com desfecho ruim e D2 como decisão falha com desfecho bom. A apuração da restrição deve ter responsável designado e prazo acordado antes de ser encerrada. |
| Exigir em cada expectativa a indicação de origem anterior ao desfecho ou de reconstrução cega posterior; marcar como ausente quando nenhuma das duas existir. | Responsável pela retrospectiva | `cir-sintese`, 6.6; `references/retrospectiva.md` | Uma reconstrução que conhece o desfecho não pode entrar no campo de previsão nem em métricas de calibração. |
| Conferir o tipo de projeto antes de preparar qualquer registro de aprendizado; bloquear a preparação de linhas oriundas de testes e, em projetos reais, conferir cada campo contra a lista permitida. | Condutora | `cir-sintese`, “Auxiliares locais”; `references/retrospectiva.md` | Este caso deve produzir zero linhas de aprendizado, inclusive sem nome e com dados agregados. |

São propostas de procedimento, não mudanças já aplicadas às skills. A aplicação exige decisão separada, fora deste projeto. A conclusão retrospectiva proposta é preservar o mérito de D1, reconhecer a falha de D2, manter ausente a previsão que não existiu e impedir que o ensaio alimente o aprendizado entre projetos.
