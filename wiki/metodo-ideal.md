# Método IDEAL

**Estado:** método proposto; documentação do desenho, sem execução automatizada implementada. **Revisão:** 2026-10-22.

O IDEAL organiza a Etapa 1: definir o que deveria existir para realizar plenamente um propósito, antes de escolher tecnologia, produto e mercado. Seu resultado é o **Conceito Ideal de Referência (CIR)**, usado como referência nas etapas seguintes. A definição identifica-se como v2 para revisão; IDEAL, CIR e suas métricas são nomes propostos no projeto. ([S09, §1 e abertura](../sources/originais/concepcao-ideal-solucao.md))

## Onde começa e termina

A Etapa 1 descreve propósito, funções, comportamentos e princípios conceituais. A Etapa 2 procura mecanismos técnicos; a Etapa 3 acrescenta mercado, produto e MVP. Uma descoberta posterior pode reabrir o CIR, com registro da mudança.

O método explica **o que elaborar**. O [fluxo da Etapa 1](fluxo-etapa1.md) transforma seus nove passos em temas e sub-etapas, aplicando um ciclo de entendimento, pesquisa, elaboração e validação. As skills previstas para conduzir esse trabalho estão na [arquitetura](arquitetura.md). O plano antigo de uma skill única `metodo-ideal` foi explicitamente substituído; permanece como histórico. ([S05, abertura](../sources/originais/plano-skill-etapa1-ideal.md))

## Princípios que delimitam o ideal

Um CIR tem **um propósito**, formulado como resultado na vida de alguém. “Analisar dados” ainda é um meio; “decidir melhor, no momento certo” se aproxima do resultado pretendido. No início, explorar formulações e escolher uma; depois, mudar o propósito exige reabrir e registrar as decisões afetadas.

O desenho suspende filtros comerciais, orçamento e organização. Limitações da tecnologia atual viram **fronteiras técnicas** para a Etapa 2. Lógica, ciência, natureza humana, propósito e valores continuam valendo. Conflitos regulatórios devem ser registrados; a abstração conceitual não autoriza ações ilegais ou danos durante a execução. O teste decisivo é: impossível em princípio ou apenas difícil hoje? O primeiro exige reformular o alvo pelo máximo possível; o segundo exige registrar uma fronteira. ([S09, §3–4](../sources/originais/concepcao-ideal-solucao.md))

“Processo amplo, CIR estreito” significa explorar livremente e conservar no CIR o que altera o resultado do propósito. Registrar o restante preserva repertório. Diferenciais permanecem hipóteses com confiança; decisões precisam de razões e de uma condição que as faria mudar.

## Cinco fases e nove passos

A tabela resume o método; os [contratos dos entregáveis](contratos.md) definem o que consolidar. As quantidades orientam o método completo e não comprovam, sozinhas, qualidade. ([S06, passos 1–9](../sources/originais/metodo-ideal-passo-a-passo.md); [S09, §5](../sources/originais/concepcao-ideal-solucao.md))

| Fase | Passo | Trabalho e resultado |
| --- | --- | --- |
| **I — Intenção** | 1. Propósito, job e estado ideal | Explorar 3–5 formulações; escolher um propósito; descrever o job sem solução, quem participa e o estado ideal. Congelar a escolha. |
| **D — Diagnóstico** | 2. Anatomia e conhecimento | Mapear etapas do job, falhas, causas, contradições e o que ocorre se nada mudar. Separar sabido, incerto e impossível de saber. |
| D | 3. Métricas e Resultado Final Ideal | Propor 5–12 métricas com linha de base e limite ideal, incluindo esforço e dano; testar impossibilidades do resultado pretendido. |
| **E — Exploração** | 4. Divergência ampla | Gerar pelo menos três famílias com princípios diferentes. Registrar ideias, origem e tangentes; evitar encerrar na primeira lista. |
| E | 5. Esboço integrado | Reunir o conceito amplo num rascunho de 1–2 páginas para expor conflitos, sinergias e dependências. O esboço não é compromisso final. |
| **A — Arquitetura** | 6. Abstração e triagem | Perguntar “para que serve?” até chegar à função. Classificar cada elemento e registrar seu destino. |
| A | 7. Arquitetura funcional | Elaborar capacidades e 3–5 cenários sem telas para as famílias sobreviventes. Distinguir núcleo invariante e capacidades amplificadoras. |
| **L — Lapidação** | 8. Prova conceitual | Confrontar conceitos com 10–20 casos reais de desfecho conhecido, saídas ideais, pré-mortem e red team; comparar com a melhor abordagem atual. |
| L | 9. Síntese | Consolidar CIR, passagem à Etapa 2 e estacionamento da Etapa 3; conferir rastreabilidade e critério de pronto. |

A comparação usa critérios explícitos e sinais `+`, `0`, `−` e `?`, sem somá-los numa nota geral. Eliminar apenas alternativas claramente dominadas; se a comparação continuar fraca, melhorar a avaliação antes de gerar mais ideias. Uma rodada termina quando não traz família nova nem altera o CIR.

## Como a exploração vira escopo

A triagem usa o efeito no propósito, inclusive para ideias de experiência. ([S09, §3.4 e passo 6](../sources/originais/concepcao-ideal-solucao.md))

| Classificação | Destino |
| --- | --- |
| Parte da eficácia: sem ela o propósito falha | Função do CIR |
| Custo de uso: altera esforço, tempo ou atenção | Métrica de idealidade |
| Anti-ideal: agrada e prejudica o propósito | Restrição explícita |
| Apelo: não altera resultado nem esforço | Estacionamento da Etapa 3 |
| Necessidade vizinha: resolve outro job | Estacionamento ou outro CIR |

O [exemplo](exemplo.md) mostra essa passagem da forma à função. A **taxa de surpresa**, fração das tangentes que viram função após abstração, serve para ajustar exploração futura.

## Termos e limites da evidência

**Job** é o que alguém procura realizar, sem nomear solução. **RFI**, chamado também IFR nas fontes, é o Resultado Final Ideal: benefícios sem custo de uso ou dano, sujeito aos limites de princípio. **Espaço K** é o conhecimento disponível; a teoria C–K relaciona conhecimento e exploração de conceitos. **Gap de idealidade** é a distância entre uma solução real e a referência ideal.

A simulação usa `Q` como pontuação artificial que combina núcleo e cadeia até o resultado. Essa fórmula pertence ao modelo de brinquedo, sem validação como medida universal do CIR. Proporções como 70/30 e 20–30 ideias por rodada são heurísticas, não parâmetros empiricamente ótimos. A própria fonte afirma que hipóteses, simulação e literatura não provam o método. ([S09, §10](../sources/originais/concepcao-ideal-solucao.md))

Questões de aprovação, implementação e divergências entre planos permanecem em [pendências](pendencias.md).
