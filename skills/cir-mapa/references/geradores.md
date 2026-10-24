## 11. Subagentes

A skill não chama agentes: a condutora monta os briefs pelos cartões, e o grill, os pesquisadores, as equipes e o conselho chegam pelas skills genéricas. Aqui ficam os geradores cegos do tema, a sonda e o que o crítico da equipe procura.

| Agente | Quantos | Vê | Não vê | Entrega |
| --- | --- | --- | --- | --- |
| Gerador de decomposição · 2.1 | 1 | O job, as variações e o seu operador | O job map, a sua versão e as fichas | Uma decomposição em etapas de verbo e objeto, com as passagens e o que não sabe |
| Gerador de causas rivais · 2.2 | 2 ou 3, um por disciplina | O job, o job map sem as fontes, a falha e o seu operador | As árvores, a sua versão, as causas da equipe e as dos outros geradores | Várias causas, cada uma como cadeia, com a probabilidade e o que se deveria observar (8.9) |
| Gerador de contradições · 2.3 | 2 | O job, o job map, as falhas e causas, os conflitos do 1.5 e o seu operador | A sua lista, a da equipe e a do outro gerador | Contradições em par de parâmetros, com a forma física, a classe que propõe e a probabilidade |
| Gerador da visão de fora · 2.4 | 1 | O fenômeno, o job e as partes centrais | A sua projeção, a ideia e o resto do mapa | A classe de referência, as taxas-base com fonte e a projeção só pela classe, em faixas |
| Sonda de memória · 2.6 | 1, no modelo dos geradores do tema 4 | O antes de cada caso, com os nomes e as datas | O desfecho e o resto do banco | A continuação de cada caso e os detalhes que acertou (8.7) |
| Gerador de diagnóstico de contraste · validação integrada | 1 ou 2 | O job, o fenômeno e as partes centrais | Tudo do tema 2 | Um diagnóstico com as linhas do pacote (8.8) |
| Crítico da equipe | 1 por reunião | A saída da reunião, o cartão, as regras, os exemplos e as saídas do `sinais.py` e do `mapa.py` | A autoria | As falhas do tema: mercado, solução no mapa, causa sem mecanismo, rival que é só o oposto, "erro humano" no fim, árvore sem "outras causas", "de princípio" sem premissas, limite de hoje como impossível, analogia como solução, caso com o desfecho no antes |

O gerador de disciplinas distantes do 2.7 é da `especialistas`.

**Operadores,** sorteados sem repetição, com a semente registrada:

| Sub-etapa | Operador | O que pede |
| --- | --- | --- |
| 2.1 | De trás para a frente | Começa pelo concluir e pergunta o que tinha de estar pronto antes de cada etapa |
| 2.1 | Pela variação mais difícil | Decompõe o job na variação mais dura do 1.3 |
| 2.1 | Pelo erro | Começa pelo que costuma dar errado e reconstrói as etapas em volta |
| 2.1 | Executor novato | Decompõe como quem faz o job pela primeira vez, sem os atalhos de quem já sabe |
| 2.2 | Outra disciplina | Explica a falha pela ótica de uma disciplina do mapa, diferente da de quem elaborou as árvores |
| 2.2 | Caso desviante | Parte de onde a falha não acontece, nas mesmas condições, e pergunta o que é diferente |
| 2.2 | Inversão | Pergunta o que alguém teria de fazer para produzir esta falha de propósito |
| 2.2 | Nível do sistema | Sobe um nível: regras, contratos, incentivos e fluxos de informação, em vez de pessoas |
| 2.3 | Parâmetros | Percorre os parâmetros genéricos de `assets/parametros.md`, dois a dois |
| 2.3 | Valores | Parte dos conflitos do 1.5 e procura outros, parte a parte |
| 2.3 | Extremo | Leva um parâmetro ao limite e vê o que quebra |
| 2.3 | Melhor de hoje | Parte da melhor abordagem atual e pergunta onde ela para de melhorar, e por quê |
| 2.4 | Classe de referência | Escolhe a classe e projeta só por ela, antes de olhar o caso |
| Integrada | Do zero | Monta o diagnóstico sem ver o mapa, a partir do job e do fenômeno |
- **Várias opções por gerador,** cada uma com a probabilidade, inclusive as improváveis: pedir a distribuição verbalizada aumenta a diversidade ([Verbalized Sampling](https://arxiv.org/abs/2510.01171)), e modelos diferentes tendem a respostas parecidas ([Artificial Hivemind](https://arxiv.org/abs/2510.22954)).
- **A sua versão primeiro, e os geradores separados:** a ajuda da IA melhora ideias individuais e reduz a diversidade do conjunto ([Doshi e Hauser](https://doi.org/10.1126/sciadv.adn5290); [Anderson, Shah e Kreminski](https://doi.org/10.1145/3635636.3656204)).

**Modelos e custo:**

- **Modelos:** cada agente usa o modelo do seu papel no mapa de modelos (0.3). A sonda usa, de propósito, o modelo dos geradores do tema 4: é a memória deles que ela mede.
- **Ordem de grandeza:** com as doses dos cartões, o tema abre perto de 120 sessões filhas, somando pesquisadores, equipes, verificações, geradores, a sonda e os conselhos das 7 sub-etapas e da validação integrada. O teste de custo da fase 5 mede o consumo real, e o custo só decide no empate (critério máximo, seção 16).

Base: S15. Operadores não são executores; só a condutora despacha agentes.
