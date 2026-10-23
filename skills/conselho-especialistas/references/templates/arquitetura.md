# Template Arquitetura

Base: S11 §5.3, sub-etapas 4.11–4.15. Examine coerência entre princípios,
capacidades e cenários funcionais, preservando o núcleo do conceito.

**Óticas:** construtivo, refutador de coerência e adversário. A composição por
dose segue [conselhos](../conselhos.md).

**Entrada:** cartões anônimos de famílias, arquitetura funcional, invariantes,
capacidades e cenários relevantes; propósito, restrições e critérios prévios
com `refuta_se`; parecer técnico quando exigido. “Arquitetura” aqui não autoriza
escolher stack, produto ou implementação prematura.

**Investigar:** as partes podem cumprir as funções ao mesmo tempo? Há cenário
que exige violar o núcleo ou um valor? Uma capacidade depende de uma premissa
não demonstrada? Um adversário contorna a restrição? Não complete a solução
com mecanismos que a origem não forneceu.

**Entregar:** matriz por critério com contradições e condições concretas de
refutação, fonte ou raciocínio verificável e lacunas. Não selecionar família
por total de sinais nem afirmar que a arquitetura foi aprovada.
