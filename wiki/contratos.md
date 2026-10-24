# Contratos dos entregáveis

**Estado:** formatos do desenho, com persistência e modelos iniciais na [condutora alpha](implementacao-condutora.md). A produção e avaliação conceitual completas dependem das outras skills. **Revisão:** 2026-10-23.

Esta página define o conteúdo esperado dos artefatos de um projeto conduzido pelo [método IDEAL](metodo-ideal.md). O [fluxo](fluxo-etapa1.md) define quando produzi-los; a [arquitetura](arquitetura.md) define os papéis responsáveis.

## Dossiê: estado e memória do projeto

O plano atual prevê uma pasta `cir/<projeto>/`, versionada com Git. **A condutora lê e grava o dossiê**; os trabalhadores recebem briefs com apenas o conteúdo permitido e devolvem resultados estruturados. Essa é uma responsabilidade planejada, que depende de isolamento real na implementação: remover dados do brief não revoga acesso ao sistema de arquivos. ([S02, §2 e §11](../sources/originais/plano-geral-skills-cir.md))

| Grupo | Conteúdo esperado |
| --- | --- |
| Estado | `estado.json`: tema, sub-etapa, doses, travas, pendências e mapa de modelos. A definição formal do schema ainda depende de implementação. |
| Trabalho por tema | Ficha/separação inicial, propósito, mapa, idealidade, desafios, famílias, esboço, triagem, arquitetura e prova; conservar origem das conclusões. |
| Casos | Banco de trabalho e reservados separados; preservar o conjunto que geradores não podem consultar antes da prova. |
| Memória transversal | Banco de ideias com origem; fronteiras técnicas; estacionamento com motivos; decisões; fichas de fonte e mapa de especialistas. |
| Interações | Perguntas e respostas; pautas, atas, sínteses e pareceres; briefs, vereditos, chaves de autoria e placar do conselho. |
| Consolidação | `06-cir.md`, `06-pacote-etapa-2.md`, `06-estacionamento-etapa-3.md` e `06-pronto.md`. |

Decisão: contexto, opções, escolha, evidência, dissenso, confiança e condição de reversão. Ficha de fonte: referência, link, trecho de apoio, o que demonstra, força da evidência, data e verificação realizada. Campo vazio não significa aprovação. Estrutura completa em [S02, §11](../sources/originais/plano-geral-skills-cir.md).

O grill acrescenta perguntas, checagem e não perguntado em `grill/<sub-etapa>.md`, respostas literais em `grill/respostas.jsonl` e fatos sem autoria em `grill/conferir/<sub-etapa>.json`. Entendimento vai na saída da sub-etapa; paráfrases são leituras marcadas, e confirmação/leitura vinculam-se à versão atual. A condutora continua como única escritora. Contratos locais e limites em [implementação do grill](implementacao-grill.md); fonte: [S12, §§4, 8 e 11](../sources/originais/plano-grill-embasado.md).

Especialistas devolve `especialistas.md` e fichas por formação/rodada para `fichas/<sub-etapa>-p<passo>.md`. Cada ficha transporta papel, especialidade, versão/hash da `esp-*` ou lacuna, módulos, cobertura/motivo, escola, equipamentos, modelo e visibilidade. O bloco inteiro abre o brief; o envelope acrescenta ficha/especialidade, e a entrega começa pelo selo. Hash da versão, do conteúdo selecionado e do transporte são distintos. Biblioteca e testes fechados não integram o dossiê. Veja [interfaces e limites](implementacao-especialistas.md); fonte: [S13, §§4 e 8–11](../sources/originais/plano-especialistas.md).

Equipe devolve `equipe/<reuniao>/` com pauta, preparações, ata literal, posições finais, síntese/parecer/integração, checagem, custos e placar contribuição→especialidade→destino. Estado privado contém sessões, modelos, auditoria e quarentena; não distribuir o pacote inteiro aos membros ou ao conselho. A síntese destina cada código e conserva o melhor argumento do dissenso. Parecer cobre afirmações prévias sem veredito; integração relata conflitos sem decidir. Fusão preserva origem A/B/C, exclusões e incompatíveis como opções ou contraprova. Só a condutora persiste; protocolo concluído não implica aprovação humana. Veja [implementação e formatos](implementacao-equipe.md); fonte: [S14, §§4 e 6–10](../sources/originais/plano-equipe-especialistas.md).

## CIR: conteúdo em 17 seções

O CIR consolida a referência conceitual. Cada seção precisa ter origem no dossiê e ser compatível com as decisões; pode referenciar evidências detalhadas. ([S09, §8](../sources/originais/concepcao-ideal-solucao.md); [S08, sub-etapa 6.1](../sources/originais/fluxograma-completo-ideal.md))

| # | Seção | Conteúdo mínimo |
| --- | --- | --- |
| 1 | Essência | Conceito em uma frase. |
| 2 | Propósito, job e estado ideal | Escolha congelada, formulações descartadas e motivos. |
| 3 | Fenômeno e contradições | Problema compreendido e contradições relevantes. |
| 4 | Métricas e RFI | Linha de base, limite ideal, custo de uso e dano. |
| 5 | Limites | Impossibilidades reformuladas e fronteiras suspensas. |
| 6 | Famílias exploradas | Alternativas consideradas e razão da escolha. |
| 7 | Princípios invariantes | O que define a identidade do conceito. |
| 8 | Capacidades | Essenciais, complementares e exploratórias; experiência como função. |
| 9 | Restrições anti-ideais | Comportamentos que prejudicam o propósito, mesmo agradando. |
| 10 | Funcionamento | Cenários de operação ideal sem escolher telas ou stack. |
| 11 | Diferenciais | Contradições quebradas e salto qualitativo, como hipóteses com confiança. |
| 12 | Casos canônicos | Situações reais, fontes, desfechos conhecidos e saídas ideais. |
| 13 | Pré-mortem | Falhas intrínsecas, danos e uso duplo. |
| 14 | Limite de identidade | O que este conceito não é. |
| 15 | Passagem à Etapa 2 | Perguntas abertas e referência ao pacote técnico futuro. |
| 16 | Estacionamento Etapa 3 | Apelo e necessidades vizinhas, com motivos de exclusão. |
| 17 | Decisões | Histórico das escolhas e taxa de surpresa. |

## Critério de pronto: 14 verificações

Checklist do método completo. Quantidades não substituem revisão de conteúdo. Item pendente volta à origem ou fica registrado como ressalva por decisão explícita; não apresentar um CIR com ressalvas como plenamente conforme. ([S09, §9](../sources/originais/concepcao-ideal-solucao.md); [S08, sub-etapa 6.5](../sources/originais/fluxograma-completo-ideal.md))

- [ ] Propósito único, no nível do “para quê”, sem produto ou tecnologia; formulações descartadas registradas e escolha congelada.
- [ ] Métricas com linha de base e limite ideal, incluindo custo de uso e dano.
- [ ] RFI aprovado no teste do impossível.
- [ ] Pelo menos três famílias com princípios realmente diferentes, exploradas e registradas.
- [ ] Tangentes registradas no banco, com taxa de surpresa.
- [ ] Esboço integrado com conflitos, sinergias e dependências.
- [ ] Todos os elementos triados nos cinco tipos; experiência que entra descrita como função.
- [ ] Restrições anti-ideais explícitas e estacionamento com motivo para cada exclusão.
- [ ] Capacidades sem tecnologia e núcleo invariante definido.
- [ ] Pelo menos três cenários de operação ideal.
- [ ] Pelo menos dez casos canônicos com saídas ideais escritas.
- [ ] Pré-mortem do ideal e red team realizados.
- [ ] Decisões registradas com confiança.
- [ ] Pacote de passagem à Etapa 2 pronto.

A fonte operacional admite linha de base “a medir”, desde que acompanhada do método de medição. Registrar essa condição, sem inventar valor ou esconder a pendência. Termos como preço, stack e MVP indicam possível contaminação quando orientam o CIR; podem aparecer legitimamente nas fronteiras, no estacionamento ou na explicação de exclusões. ([S08, sub-etapa 3.3](../sources/originais/fluxograma-completo-ideal.md))

## Passagem às Etapas 2 e 3

O pacote da **Etapa 2** deve relacionar capacidades às métricas de idealidade, incluir os casos canônicos como bancada futura, fronteiras técnicas e perguntas científicas abertas, princípios invariantes, restrições anti-ideais e alternativas vivas. Isso permite procurar mecanismos sem reabrir silenciosamente decisões conceituais.

O estacionamento da **Etapa 3** conserva ideias de apelo e necessidades vizinhas com o motivo de cada exclusão. Um item que muda o resultado do propósito exige rever sua classificação. Estacionar não significa priorizar comercialmente nem prometer implementação. ([S09, passo 9](../sources/originais/concepcao-ideal-solucao.md); [S08, sub-etapas 6.2–6.3](../sources/originais/fluxograma-completo-ideal.md))

No teste de passagem planejado, um leitor em sessão nova recebe somente CIR e pacote. Corrigir ambiguidades e perguntas centrais até que propósito e núcleo sejam entendidos sem a conversa original. O relatório de pronto registra verificações, ressalvas e fontes conferidas. O [exemplo](exemplo.md) ilustra um trecho de raciocínio; não representa um dossiê completo aprovado.

Os antigos nomes `dossie.md`, `cir.md` e pacotes sem prefixo pertencem à proposta histórica substituída de [S05, §4.2–4.8](../sources/originais/plano-skill-etapa1-ideal.md). Lacunas de schemas, isolamento e compatibilidade devem continuar visíveis em [pendências](pendencias.md).
