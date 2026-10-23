# Método IDEAL — passo a passo

Resumo operacional da Etapa 1: os 9 passos para chegar ao Conceito Ideal de Referência (CIR). Fundamentos, exemplos e evidências estão em [Etapa 1 — Concepção Ideal da Solução: método IDEAL (v2)](../Etapa%201%20%E2%80%94%20Concep%C3%A7%C3%A3o%20Ideal%20da%20Solu%C3%A7%C3%A3o%20m%C3%A9todo%20IDEAL%20%20629394b6e12b49c792805775c07e27d3.md).

## I — Intenção

### 1. Propósito, job e estado ideal

- **O quê:** definir um único propósito, no nível do *para quê*, e o estado ideal em que ele se realiza por completo.
- **Como:** partir da ideia e perguntar "para quê?" até chegar a um resultado na vida de alguém. Escrever de 3 a 5 versões do propósito, escolher uma e registrar o motivo. Descrever o job (verbo + objeto + contexto) sem citar solução, e quem o executa, quem é afetado e quem tenta distorcê-lo. Escrever como é o mundo quando o job é realizado com perfeição. Congelar o propósito até o fim da etapa.
- **Por quê:** "ideal" só existe em relação a um objetivo. Dois propósitos geram trocas que só critérios de mercado resolveriam, e um propósito no nível do mecanismo deixa de fora o que faz o resultado acontecer.

## D — Diagnóstico

### 2. Anatomia do problema e mapa de conhecimento

- **O quê:** entender onde e por que o job falha hoje e o que já se sabe sobre o fenômeno.
- **Como:** dividir o job em etapas (definir, localizar, preparar, confirmar, executar, monitorar, modificar, concluir). Para cada falha, buscar a causa. Listar as contradições ("para melhorar A, piora B"). Descrever o que acontece se nada mudar. Separar o que se sabe, o que é incerto e o que não se pode saber.
- **Por quê:** o diferencial nasce de falhas e contradições que ninguém resolveu. Sem esse mapa, a divergência produz variações do que já existe.

### 3. Métricas de idealidade e Resultado Final Ideal

- **O quê:** tornar o ideal extremo e mensurável.
- **Como:** escrever de 5 a 12 métricas (direção + métrica + objeto + contexto), cada uma com linha de base e limite ideal, incluindo custo de uso (esforço, tempo, atenção) e dano. Escrever o Resultado Final Ideal (o job se realiza sozinho, com todos os benefícios e nenhum custo ou dano) para o todo e para cada etapa do job. Passar cada exigência pelo teste do impossível: se for impossível em princípio, trocar pelo limite máximo possível.
- **Por quê:** sem métrica, "ideal" vira opinião, e a escolha volta a ser guiada pelo que parece viável. Com ela, a distância entre o MVP e o ideal fica mensurável.

## E — Exploração

### 4. Divergência ampla

- **O quê:** gerar possibilidades antes de escolher, inclusive fora do núcleo do propósito.
- **Como:** gerar pelo menos 3 famílias de conceito com princípios de solução diferentes (atributos inesperados, quebra de contradições, combinação de princípios por função, analogias distantes, inversão, 10×). Dedicar cerca de 70% do esforço aos meios do propósito e 30% a tangentes: experiência, enfeites, necessidades vizinhas, analogias abstratas e provocações. Não parar na primeira lista; mirar de 20 a 30 ideias por rodada. Registrar tudo no banco de ideias, inclusive o descartado.
- **Por quê:** as primeiras ideias são as óbvias, tangentes às vezes escondem funções valiosas, e o que não é registrado não pode ser reaproveitado depois.

### 5. Esboço integrado

- **O quê:** juntar o conceito amplo num único rascunho.
- **Como:** em 1 a 2 páginas e poucas horas, descrever o conceito como se tudo do banco de ideias coubesse nele. Listar os conflitos (um elemento piora outro ou o propósito), as sinergias e as dependências.
- **Por quê:** conflitos só aparecem quando os elementos estão juntos. A versão curta é a que mais rende por hora de trabalho.

## A — Arquitetura

### 6. Abstração e triagem

- **O quê:** decidir o que entra no CIR pelo efeito no propósito, sem perder o resto.
- **Como:** para cada elemento, perguntar "para que serve isso?" até chegar a uma função e classificá-la: parte da eficácia (sem ela, o propósito não se realiza) → função do CIR; custo de uso (muda o esforço) → meta nas métricas; anti-ideal (melhora a experiência e piora o propósito) → restrição do CIR; apelo ou necessidade vizinha → estacionamento, com o motivo. Aplicar o Resultado Final Ideal à função ("e se acontecesse sem sistema nenhum?"). Contar quantas tangentes viraram função (taxa de surpresa) e ajustar a fração de tangentes da próxima rodada.
- **Por quê:** impede que o CIR cresça por atração, pega elementos anti-ideais antes que virem produto e transforma ideias de interface em funções que podem ser cumpridas de um jeito melhor.

### 7. Arquitetura funcional

- **O quê:** descrever como o conceito funciona, sem tecnologia, para as 2 ou 3 famílias que sobreviveram.
- **Como:** decompor cada conceito em capacidades independentes, descendo de propósito para função, comportamento e princípio de solução. Escrever de 3 a 5 cenários de operação num dia real, sem telas. Separar o núcleo invariante das capacidades amplificadoras e classificar as capacidades em essenciais, complementares e exploratórias. Quando especificar exigir escolher tecnologia, registrar para a Etapa 2 e seguir.
- **Por quê:** capacidades independentes permitem recortar o MVP sem quebrar o conceito, e os cenários revelam lacunas que uma lista de funções esconde.

## L — Lapidação

### 8. Prova conceitual

- **O quê:** testar os conceitos contra a realidade e escolher (ou combinar) o de referência.
- **Como:** escrever à mão a saída ideal para 10 a 20 casos reais passados, com desfecho conhecido, incluindo casos com os lados trocados. Fazer o pré-mortem ("foi construído com perfeição e falhou: por quê?") e pedir a um red team que derrube cada conceito. Comparar cada conceito com a melhor abordagem atual, critério a critério (+, 0, − ou ?), sem somar numa nota. Eliminar só o que é claramente inferior e registrar cada decisão com o nível de confiança. Se a comparação não ficar clara, melhorar a avaliação antes de gerar mais ideias. Parar quando uma rodada nova não trouxer família nova nem mudar o CIR.
- **Por quê:** a escolha é o gargalo. Avaliar melhor rende mais do que gerar mais, e sem critérios explícitos a escolha volta para o viável, justamente o filtro que a etapa suspendeu.

### 9. Síntese do CIR

- **O quê:** consolidar o conceito num documento único e preparar a passagem para as próximas etapas.
- **Como:** preencher o modelo do CIR. Montar o pacote da Etapa 2: funções com métricas, casos canônicos, fronteiras técnicas, perguntas em aberto, princípios invariantes, restrições anti-ideais e alternativas vivas. Entregar o estacionamento à Etapa 3, com o motivo de cada exclusão. Conferir o critério de pronto.
- **Por quê:** o CIR é a régua das etapas seguintes. Sem o pacote, a Etapa 2 reabre decisões já tomadas; sem o estacionamento, o repertório da exploração se perde.