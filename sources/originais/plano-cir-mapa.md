# Plano detalhado — cir-mapa

<aside>
🗺️

**O que é:** o plano detalhado da `cir-mapa`, a skill de método do tema 2 do [Fluxograma completo — Etapa 1 (método IDEAL em ciclo)](https://app.notion.com/p/Fluxograma-completo-Etapa-1-m-todo-IDEAL-em-ciclo-f1f71e3bd5e6487ebdfc94cd7e9fa161?pvs=21). Ela entende o fenômeno e por que o job falha: o job map; as falhas e as causas, com causas rivais; as contradições, separadas em de princípio e quebráveis; a projeção de referência; o espaço K, com o que se sabe, o que é incerto e o que é impossível de saber; o banco de casos, juntado antes de existir solução e guardado; e, com a `especialistas`, os especialistas e os conselhos do projeto. É a segunda skill de método do item 7 da ordem da seção 15 do [Plano geral das skills — Etapa 1 (CIR)](https://app.notion.com/p/Plano-geral-das-skills-Etapa-1-CIR-72d0fdc1db19433e9101d1ac3b3015ef?pvs=21), depois da [Plano detalhado — cir-proposito](https://app.notion.com/p/Plano-detalhado-cir-proposito-71d3eb40508e4f08a048aea8216c6a33?pvs=21), e entrega à [Plano detalhado — etapa-1-cir (condutora)](https://app.notion.com/p/Plano-detalhado-etapa-1-cir-condutora-fccda0c36a5d403582b433a6f2b0657f?pvs=21) os cartões das sub-etapas 2.1 a 2.7, no formato combinado. Os agentes chegam pelas skills genéricas, nos formatos do [Plano detalhado — conselho-especialistas](https://app.notion.com/p/Plano-detalhado-conselho-especialistas-f31c25a61c914fd98fe1f1ad81c09ed4?pvs=21), do [Plano detalhado — pesquisa-cientifica](https://app.notion.com/p/Plano-detalhado-pesquisa-cientifica-b0dde96c53b34b38aa26c8c474ce1071?pvs=21), do [Plano detalhado — grill-embasado](https://app.notion.com/p/Plano-detalhado-grill-embasado-ec54d7f985534c0a997926c075d97775?pvs=21), do [Plano detalhado — especialistas](https://app.notion.com/p/Plano-detalhado-especialistas-79544cfde9c5403babc8e5cc62fe12cd?pvs=21) e do [Plano detalhado — equipe-especialistas](https://app.notion.com/p/Plano-detalhado-equipe-especialistas-184104fa869f40b6a3589890879df668?pvs=21).
**Universal primeiro:** o método, os cartões, os formatos e os scripts valem em qualquer agente com chat; quem conduz é a condutora, no ambiente dela. **Claude primeiro:** geradores, equipe e conselho do tema são Claude, nos modelos que você escolheu no 0.3. **Para qualquer projeto:** startups, produtos, pesquisa ou projetos públicos; os exemplos de dentro da skill variam de domínio e nenhum usa os casos de teste.

</aside>

## 1. Propósito no fluxograma

**Propósito:** entender o fenômeno e por que o job falha, separar o que se sabe do que não se pode saber, juntar os casos antes de existir solução e definir os especialistas.

| Responde por | Como se vê |
| --- | --- |
| Fenômeno, e não mercado | Nenhuma peça fala de preço, disposição a pagar, tamanho de mercado ou concorrência. Produtos que já existem aparecem só como modo de fazer o job hoje, descritos pelo mecanismo e pelo lugar onde falham. O `sinais.py` acusa, e o crítico confere |
| Job inteiro | Cada etapa do job diz como é feita hoje, com a fonte; uma decomposição alternativa cega procura as etapas escondidas |
| Causas com evidência | Cada causa é uma cadeia de mecanismo, com a dependência medida: a falha muda quando a causa muda. O que só tem correlação, ou não tem fonte, fica marcado como hipótese |
| Causas rivais | Toda falha central tem pelo menos duas explicações, de origens diferentes, testadas contra o que cada uma faria esperar, escrito antes da busca |
| Contradições classificadas | Cada contradição é um par de parâmetros. "De princípio" só com teorema ou lei e as premissas; sem prova, é limite de hoje ou quebrável, e vira desafio do tema 4 |
| Futuro sem intervenção | A projeção do que acontece se nada mudar parte da visão de fora, com fonte, sem preço nem adoção e sem número inventado |
| Saber e não saber | Cada afirmação do espaço K está como sabida, incerta (com o que a resolveria) ou impossível de saber (com o porquê), e o trecho da fonte a sustenta |
| Casos antes da solução | De 15 a 30 casos reais, com desfecho verificável, desfechos dos dois lados e os tipos difíceis, guardados longe dos geradores; quem vai para os reservados é o sorteio, no 3.6 |
| Quem pensa o projeto | Cada causa, contradição e parte tem uma especialidade; os conselhos têm óticas distintas; o que não tem skill vira lacuna |
| Seu | Cada peça começa pela sua versão; o que a IA propõe vem marcado; quem decide é você |
- **Entra em:** 2.1 a 2.7 e na validação integrada do tema, carregada pela condutora na abertura do tema 2.
- **Entrega:** `02-mapa.md`, `casos/` e, com a `especialistas`, o `especialistas.md`.
- **Alimenta:** o tema 3 (as etapas, nos resultados desejados do 3.1 e nos RFIs do 3.4; a frequência e a gravidade das falhas, como candidatas a linha de base no 3.3; os limites, no teste do impossível do 3.5; os casos, no 3.6); o tema 4 (as contradições quebráveis e as causas, nos desafios do 4.2; as restrições preservadas, em toda geração; as analogias, no 4.3); o tema 5 (os casos de trabalho e os reservados); e as seções 3, 5, 12 e 15 do CIR.

## 2. Skills de base e o que se aproveita

| Base | O que se aproveita | O que é nosso | Licença |
| --- | --- | --- | --- |
| [`synthesize-research`](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management/skills/synthesize-research) e [`research-synthesis`](https://github.com/anthropics/knowledge-work-plugins/tree/main/design/skills/research-synthesis) (Anthropic) | A análise temática e o affinity mapping; a triangulação por método, por fonte e no tempo; o comportamento vale mais que a preferência declarada; gambiarras revelam necessidade não atendida; os sinais de intensidade (frequência, gravidade e emoção); "citação é evidência, não achado"; o que fazer quando as fontes discordam | Entram só quando há dados de usuários (entrevistas, registros, chamados, respostas abertas), como evidência para o 2.1 e o 2.2. Ficam de fora personas, segmentos, dimensionamento de oportunidade e roadmap | Apache 2.0 |
| [thinking-framework-skills](https://github.com/product-on-purpose/thinking-framework-skills) (product-on-purpose), 63 frameworks, cada um com o seu nível de evidência | `think-process-tracing`: causas rivais como cadeias de mecanismo, o que se deveria observar escrito antes, os testes de aro, arma fumegante, palha ao vento e duplamente decisivo, a evidência não diagnóstica e a observação mais decisiva que falta. `think-five-whys`: marcar cada passo como causa única ou ramo. `think-analysis-of-competing-hypotheses`: o próprio nível de evidência dela é baixo, porque a matriz dá confiança sem acurácia e a contagem trata as evidências como independentes e de mesmo peso. `think-contradiction-resolution`: contradição técnica e física. `think-reference-class-forecasting`: classe de referência, taxas-base reais, um subagente que não viu o plano e ajuste conservador. `think-consider-the-unknowns`: o registro do que não se sabe, resolvível ou inobservável. `think-far-analogy-ideation`: estrutura profunda, de mecanismo para mecanismo | A árvore com ramos e "outras causas"; os cartões de causa em linhas, sem matriz nem contagem; a força pela dependência e pelo mecanismo; as três classes das contradições, com as premissas; os três estados do espaço K. A resolução das contradições fica para o tema 4 | Apache 2.0 |
| [`mom-test`, da wondelai](https://github.com/wondelai/skills/tree/main/mom-test) | Falar da vida das pessoas, e não da ideia; perguntar por fatos específicos do passado; falar menos; elogio e opinião sobre o futuro não são dado | As regras viram perguntas do grill, critério do crítico na pesquisa do fenômeno e o roteiro de observação (6.11). Compromisso, venda e validação da ideia ficam de fora | MIT |
| [Bettencourt e Ulwick](https://hbr.org/2008/05/the-customer-centered-innovation-map) (HBR, 2008) | As 8 etapas universais do job map: definir, localizar, preparar, confirmar, executar, monitorar, modificar e concluir | As perguntas de cada etapa sem meio; como cada etapa é feita hoje, com a fonte; as passagens entre papéis; a decomposição alternativa cega | Artigo; só a ideia |
| Plano geral, fluxograma e as skills genéricas | As sub-etapas, as doses, as validações e os "refuta se" do tema 2; o formato do cartão; os modos refutar e conferir e a data de corte da pesquisa; a verificação da equipe; o 2.7 da `especialistas`, com o `cobertura.py` | — | Nosso |
| Olhadas e deixadas de fora | As skills de causa raiz e de job map sem licença declarada e as de Dean Peters (CC BY-NC-SA), só pelas ideias; `customer-journey-map`, `pre-mortem` e `pestle` (phuryn, MIT), que tratam da jornada de compra, do pré-mortem (que é do tema 5) e do ambiente de negócio; skills de jobs-to-be-done de outras coleções, sem job map | — | — |

**Dez achados que mudam o desenho:**

1. **Árvores parecem completas mesmo quando falta um ramo, e o ramo dividido parece maior.** Diante de árvores de falhas com ramos retirados, as pessoas quase não aumentaram o peso de "todas as outras causas", e dividir um ramo em partes aumentou a importância dada a ele ([Fischhoff, Slovic e Lichtenstein](https://doi.org/10.1037/0096-1523.4.2.330)); descrever um evento em partes faz o todo parecer mais provável ([Tversky e Koehler](https://doi.org/10.1037/0033-295X.101.4.547)). Os 5 porquês levam a uma cadeia única e dependem de quem pergunta ([Card](https://doi.org/10.1136/bmjqs-2016-005849)), e as análises de causa raiz na saúde costumam parar numa causa só e em correções fracas ([Peerally et al.](https://doi.org/10.1136/bmjqs-2016-005511)). **Daí:** árvore de causas com ramos e um ramo "outras causas" à vista em cada nó; os 5 porquês só dentro de um ramo, com cada passo marcado como causa única ou ramo; o peso de uma causa vem da evidência, e nunca do número de subdivisões; decomposição alternativa cega no 2.1 e causas rivais cegas no 2.2.
2. **Pensar numa explicação rival reduz o viés; a matriz de hipóteses concorrentes, não.** Explicar uma alternativa qualquer, e não só o oposto, reduziu o viés de explicação ([Hirt e Markman](https://doi.org/10.1037/0022-3514.69.6.1069)); pedir para considerar o oposto corrigiu a leitura enviesada da evidência melhor do que pedir imparcialidade ([Lord, Lepper e Preston](https://doi.org/10.1037/0022-3514.47.6.1231)). Já a análise de hipóteses concorrentes, de Heuer, com a matriz e a contagem de inconsistências, falhou nos testes: analistas treinados não seguiram os passos, o efeito sobre o viés foi misto, e o método pode aumentar a inconsistência e o erro ([Dhami, Belton e Mandel](https://doi.org/10.1002/acp.3550)); com 227 participantes, não melhorou a coerência dos julgamentos e trouxe peso pseudodiagnóstico às evidências ([Karvetski e Mandel](https://doi.org/10.1017/s1930297500008159)). A forma conta: hipóteses em linhas, com as evidências nas colunas, reduziram o viés de confirmação; a matriz no estilo da técnica, com as hipóteses nas colunas, não ([Dhami et al.](https://doi.org/10.1186/s41235-024-00560-y)). **Daí:** causas rivais para toda falha central, de origens diferentes (você, a equipe e geradores cegos); cada causa é uma linha, com as suas evidências ao lado; nada de matriz de contagem nem de soma.
3. **Causa pede mecanismo e dependência, e os modelos confundem correlação com causa.** Nas ciências da saúde, afirmar uma causa pede dois tipos de evidência: de que a causa faz diferença no efeito e de um mecanismo que liga os dois ([Russo e Williamson](https://doi.org/10.1080/02698590701498084)). Modelos de linguagem ficaram perto do acaso ao decidir se uma correlação permite concluir causa, e o ajuste fino não generalizou ([Jin et al.](https://arxiv.org/abs/2306.05836)). **Daí:** cada causa é uma cadeia de mecanismo, com a dependência (a falha muda quando a causa muda) e o mecanismo, cada um com fonte; só correlação é hipótese; o crítico e a verificação conferem o tipo de cada evidência.
4. **Evidência que combina com todas as causas não decide nada.** O process tracing classifica os testes pela força: palha ao vento, aro (a causa precisa passar), arma fumegante (se aparecer, confirma) e duplamente decisivo ([Collier](https://doi.org/10.1017/S1049096511001429)); e a evidência compatível com todas as hipóteses não é diagnóstica, o ponto central de Heuer. **Daí:** para cada causa, o que se deveria observar se ela for verdadeira e se for falsa, escrito antes da busca; cada evidência entra com o tipo de teste; a busca procura a observação mais decisiva, e a que falta vira pergunta.
5. **Quem busca acha o que procura, e a IA reforça.** Numa meta-análise, as pessoas preferiram a informação que confirmava o que já pensavam ([Hart et al.](https://doi.org/10.1037/a0015701)); buscar com um modelo de linguagem levou a consultas mais enviesadas, e um modelo que concordava com a pessoa piorou o viés ([Sharma, Liao e Xiao](https://arxiv.org/abs/2402.05880)). **Daí:** busca a favor e busca contra em pesquisadores separados, com a pergunta contra escrita no cartão: "onde a falha acontece sem esta causa?" e "onde a causa está presente e a falha não?".
6. **A visão de fora corrige o otimismo da visão de dentro.** Previsões feitas pelos detalhes do próprio caso tendem ao otimismo, e olhar o que aconteceu com casos parecidos corrige ([Kahneman e Lovallo](https://doi.org/10.1287/mnsc.39.1.17)); a previsão por classe de referência foi levada à prática do planejamento para conter esse otimismo ([Flyvbjerg](https://doi.org/10.1080/09654310701747936)); num torneio de previsões, o treino em raciocínio probabilístico, com classes de referência, melhorou a acurácia ([Mellers et al.](https://doi.org/10.1177/0956797614524255)). **Daí:** a projeção de referência começa pela classe de referência, montada por um gerador cego que não viu a sua projeção nem a ideia, com taxas-base de fontes e nenhum número inventado; o ajuste ao caso vem depois, com o motivo.
7. **Listar o que não se sabe reduz o excesso de confiança, e a incerteza tem dois tipos.** Pedir que as pessoas considerassem o que não sabiam reduziu o excesso de confiança, e mais onde ele era maior ([Walters et al.](https://doi.org/10.1287/mnsc.2016.2580)); as pessoas distinguem a incerteza do que se pode vir a saber da incerteza do acaso, e a linguagem mostra qual é ([Ülkümen, Fox e Malle](https://doi.org/10.1037/xge0000202)). **Daí:** o espaço K separa o sabido, o incerto (com o estudo, o dado ou o teste que o resolveria) e o impossível de saber (inobservável ou aleatório, com o porquê); cada afirmação diz o que mudaria no CIR se fosse falsa; o incerto que se resolve vira pergunta científica.
8. **Analogias valem pela estrutura, e a distância tem dose.** Buscar inspiração pelo propósito e pelo mecanismo, e não pela aparência, rendeu ideias mais úteis e mais novas ([Kittur et al.](https://doi.org/10.1073/pnas.1807185116)); exemplos de áreas distantes e pouco comuns renderam soluções mais novas ([Chan et al.](https://doi.org/10.1115/1.4004396)), mas analogias distantes demais pioraram a novidade e a qualidade ([Fu et al.](https://doi.org/10.1115/1.4023158)). **Daí:** no espaço K, as analogias são buscadas pela função, com a pergunta sem as palavras do domínio, e marcadas pela distância (próxima, moderada ou distante); entram como conhecimento, com o mecanismo mapeado; a ideia de solução que surgir vai ao banco.
9. **Casos escolhidos depois enganam, e saber o desfecho muda o que parecia previsível.** Escolher casos pelo resultado distorce a conclusão ([Geddes](https://doi.org/10.1093/pan/2.1.131)); o pré-registro fixa as escolhas antes de ver os dados ([Nosek et al.](https://doi.org/10.1073/pnas.1708274114)); quem conhece o desfecho acha que ele era mais previsível do que era ([Fischhoff](https://doi.org/10.1037/0096-1523.1.3.288)); o vazamento entre o que ajusta e o que testa infla resultados em muitas áreas ([Kapoor e Narayanan](https://doi.org/10.1016/j.patter.2023.100804)), inclusive em modelos de linguagem que já viram os testes no treino ([Sainz et al.](https://doi.org/10.18653/v1/2023.findings-emnlp.722)). **Daí:** casos juntados antes de qualquer solução, com desfechos dos dois lados; em cada caso, o que se sabia até a data de corte, separado do desfecho; uma sonda de memória marca os casos que o modelo já conhece, que ficam fora dos reservados; e a divisão entre trabalho e reservados é por sorteio, no 3.6.
10. **O que as pessoas dizem que fariam é pouco confiável; o que fizeram, e as gambiarras, sim.** Em perguntas hipotéticas, o valor declarado costuma passar do que as pessoas de fato pagam ([Murphy et al.](https://doi.org/10.1007/s10640-004-3332-z)); a [`mom-test`, da wondelai](https://github.com/wondelai/skills/tree/main/mom-test) pede fatos específicos do passado, e não opiniões sobre o futuro; a [`synthesize-research`](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management/skills/synthesize-research) põe o comportamento acima da preferência declarada e lê as gambiarras como necessidade não atendida. **Daí:** a pesquisa é sobre o fenômeno e a execução observada; nada de disposição a pagar, tamanho de mercado ou concorrência; gambiarras entram como evidência de falha; com dados de usuários, síntese temática com triangulação.

**O que muda no fluxograma:** no 2.1, a etapa que não se aplica fica marcada, com o motivo; no 2.2, "árvore de causas ou 5 porquês" vira árvore com ramos, com os 5 porquês só dentro de um ramo, e a matriz de Heuer dá lugar a causas rivais como cadeias de mecanismo, com o que se deveria observar escrito antes; o "refuta se" do 2.2 passa a dizer "persiste igual" e "sem mecanismo"; no 2.3, cada "de princípio" leva as premissas, e a validação passa a ser o parecer de verificação e o conselho completo Evidência, com um refutador de limites teóricos, como pede a dose completa, com a triagem no passo 3; no 2.4, a sua projeção primeiro e um gerador cego da visão de fora; no 2.5, o incerto diz o que o resolveria, e as analogias levam a distância; no 2.6, desfechos dos dois lados, o antes separado do desfecho, a sonda de memória e o sorteio no 3.6; na validação integrada, 1 ou 2 diagnósticos de contraste, e "causa desconhecida" vale como resposta. O exemplo do Motor no 2.3 fica no fluxograma; os da skill vêm de fora dos casos de teste (seção 9).

## 3. Acionamento

```yaml
---
name: cir-mapa
description: >-
  Método do tema 2 (Mapa) da Etapa 1 do IDEAL: entende o fenômeno e por
  que o job falha. Traz os cartões das sub-etapas 2.1 a 2.7 (job map;
  falhas e causas, com causas rivais; contradições de princípio e
  quebráveis; projeção de referência; espaço K; banco de casos, com a
  guarda; especialistas do projeto), os briefs dos geradores e os
  formatos do 02-mapa.md e de casos/. Use quando a condutora abrir o
  tema 2 ou uma das sub-etapas, ou quando o usuário pedir, fora da Etapa
  1, um job map, as causas de uma falha com evidência ou a classificação
  de uma contradição. Não use para pesquisa de mercado, concorrência ou
  preço, para depurar um incidente técnico, para revisão de literatura
  avulsa, nem para gerar soluções.
license: (a definir)
compatibility: Carregada pela etapa-1-cir; Python 3 para os scripts
metadata:
  versao: "0.1"
---
```

- **Só os campos do padrão aberto,** como nas outras skills.
- **Chamada pelo nome é o caminho principal:** "Use a skill `cir-mapa`, cartão do 2.2, dose completa." A condutora carrega a skill na abertura do tema 2 e relê o cartão antes de cada passo.
- **Quem lê.** A condutora lê o `SKILL.md`, os cartões e a referência do passo; grill, pesquisadores, equipe, geradores, sonda e conselho recebem, no brief, só o trecho do papel (seções 10 e 11). Nenhum deles precisa acionar a skill.

| Deve acionar | Não deve acionar (quase acertos) |
| --- | --- |
| "Abre o tema 2." | "Quero começar a Etapa 1 do meu projeto." (é da condutora, que depois carrega esta skill) |
| "Monta o job map do 2.1, dose padrão." | "Qual é o tamanho do mercado e quem são os concorrentes?" (mercado; fica de fora) |
| "Essa causa tem evidência ou é só correlação?" | "Escreve um roteiro de entrevista para validar a minha ideia com clientes." (validação da ideia; fica de fora) |
| "Monta os briefs dos geradores de causas rivais do 2.2." | "Por que o deploy de ontem derrubou o servidor?" (depuração de um incidente técnico) |
| "Por que pequenos restaurantes ficam sem ingrediente na hora do pico? Quero as causas, com evidência." (avulso) | "Faz uma revisão de literatura sobre sono e aprendizagem." (é da `pesquisa-cientifica`, no modo avulso) |
| "Esse trade-off entre rapidez e segurança é de princípio ou só das abordagens de hoje?" (avulso) | "Gera ideias para resolver essa contradição." (solução, tema 4; vai para o banco) |

A lista completa, com 10 de cada lado, entra nos testes (seção 13).

## 4. Contrato de entrada e saída

**Entradas:**

| Entrada | De quem | Forma |
| --- | --- | --- |
| Propósito congelado; job e variações por contexto; partes; valores e os conflitos em que nenhum valor cede | Tema 1, pela `cir-proposito` | `01-proposito.md`: a Declaração e as seções Job, Partes e Valores, com os conflitos marcados "vai ao 2.3" |
| Ficha do projeto, separação do material e mapa inicial de especialidades | Tema 0, pela condutora | `00-ficha.md`, `00-separacao.md` e `especialistas.md`, marcado "inicial" |
| O que você sabe do fenômeno, onde acha que o job falha, em que fontes confia e que casos conhece | Grill da abertura e de cada sub-etapa | `grill/respostas.jsonl` |
| Sua versão de cada peça | Passo 2 de cada sub-etapa | Trecho da saída da sub-etapa, com a origem "sua" ou "sua depois de ver a IA" |
| Dados de usuários, quando houver: entrevistas, registros, chamados, respostas abertas | Você, ou o material separado no 0.2 | Fichas de fonte marcadas "dados seus", sintetizadas pelo método da seção 6.11 |
| Fichas de fonte | `pesquisa-cientifica` | `fontes/` e os relatórios de cada brief |
| Atas e sínteses; parecer de verificação; relatório de integração | `equipe-especialistas` | `equipe/2.x-…`, `equipe/2.2-v1`, `equipe/2.3-v1` e `equipe/tema2-i1` |
| Alternativas e a sonda de memória | Geradores cegos e a sonda | No formato do gerador e no da sonda (seções 8.9 e 8.7) |
| Vereditos | `conselho-especialistas` | `conselho/2.x-…` |
| Sua decisão | Passo 9 | Registro D-xxx, gravado pela condutora |

**Saídas:**

| Saída | Para quem | Onde |
| --- | --- | --- |
| Os cartões das sub-etapas 2.1 a 2.7 e o do tema | Condutora | `references/cartoes.md` (seção 5) |
| Job map, falhas e causas, contradições, projeção e espaço K | Dossiê, gravado pela condutora; temas 3 e 4 | `02-mapa.md`, uma seção por sub-etapa (seção 8.1); CIR, seção 3 |
| Banco de casos candidatos | 3.6, que sorteia os de trabalho e os reservados; tema 5 | `casos/candidatos.md`, fechado. O `02-mapa.md` guarda só a contagem por tipo |
| Restrições preservadas: contradições de princípio, teoremas e leis, sempre com as premissas | Tema 3: limite ideal, RFI e teste do impossível | `02-mapa.md`, seções Contradições e Espaço K; CIR, seção 5 |
| Contradições quebráveis | 4.2, como desafios de geração | `02-mapa.md`, seção Contradições, marcadas "desafio" |
| Limites da tecnologia de hoje | Fronteiras técnicas, com a data | `fronteiras.md`, com a origem "tema 2" |
| Lacunas: perguntas científicas em aberto | CIR, seção 15; o grill dos temas seguintes | `02-mapa.md`, seção Espaço K |
| Números de como o job é feito hoje | 3.3, como candidatos a linha de base | `02-mapa.md`, seções Job map e Falhas, marcados "linha de base?" |
| Os especialistas e os conselhos do projeto | Todas as sub-etapas seguintes | `especialistas.md` (2.7) |
| Ideias de solução e assuntos de Etapa 2 e de Etapa 3 que aparecerem | Banco, fronteiras e estacionamento | `banco.md`, `fronteiras.md` e `estacionamento.md`, com a origem "tema 2" |
| Parte nova, ou um job que não bate com o que se observou | Você, que decide se reabre o tema 1 | Registro, pela condutora (seção 6.10) |

**Com as outras skills:**

| Skill | Relação |
| --- | --- |
| `etapa-1-cir` | Carrega esta skill pelo nome na abertura do tema 2; conduz o ciclo pelos cartões e relê o cartão antes de cada passo; monta os briefs por script, e o `brief.py` bloqueia `casos/candidatos.md` em todo brief fora do 2.6 e do sorteio do 3.6; grava o dossiê, os registros e o estado; roda a vigia, que ganha os sinais do tema 2 (seção 10) |
| `cir-proposito` | Entrega o propósito congelado, o job, as variações, as partes e os conflitos de valores. Se o mapa mostrar uma parte nova, ou um job que não bate com o que se observou, reabrir o tema 1 é decisão sua (seção 6.10) |
| `grill-embasado` | Recebe a abertura do tema e o "grill quer entender" de cada cartão, mais as perguntas boas e ruins do tema (`grill.md`, seção 10): casos vividos e fatos do passado, e não opiniões sobre o futuro |
| `pesquisa-cientifica` | Recebe o foco de cada cartão. No 2.2, a busca a favor e a busca contra vão a pesquisadores separados; no 2.3, a busca da prova e a do contraexemplo também, no modo refutar; no 2.5, os modos desenvolver e conferir, com a busca pela função; no 2.6, cada caso tem data de corte |
| `especialistas` | O mapa inicial parte das especialidades do tema (seção 5), inclusive as disciplinas dos geradores. No 2.7, roda o 6.1 dela; o `inventario.py` desta skill lista os itens do mapa que o `cobertura.py` dela confere |
| `equipe-especialistas` | Elabora no passo 7 de cada sub-etapa, com a pauta tirada do cartão; no 2.2 e no 2.3, uma equipe de verificação, com quem não elaborou, entrega o parecer; faz a integração do tema depois do 2.6 |
| `conselho-especialistas` | Template Evidência: rápido no 2.1, no 2.4, no 2.6 e no 2.7; completo no 2.2, no 2.3, no 2.5 e na validação integrada. Os critérios e o "refuta se" vêm do cartão, escritos antes de ver as hipóteses |
| `cir-idealidade` | Recebe os candidatos a linha de base e a projeção (3.3), as restrições preservadas (3.4 e 3.5) e o banco de casos, que ela sorteia no 3.6 com o `casos.py` |
| `cir-divergencia`, `cir-prova` e `cir-sintese` | As quebráveis viram desafios do 4.2; o tema 5 abre os reservados; a síntese leva o mapa às seções 3, 5, 12 e 15 do CIR |

## 5. Cartões das sub-etapas

No formato do cartão da condutora (seção 9 do plano dela). Os cartões repetem o fluxograma e só acrescentam o que este plano decide; se o fluxograma mudar, os cartões mudam junto, e um teste confere (seção 13). A condutora relê o cartão antes de cada passo, e o `brief.py` tira dele o foco da pesquisa, a pauta da equipe, os briefs dos geradores e os critérios do conselho. O tema 2 não tem trava: as peças seguem abertas para os temas seguintes, e reabrir uma delas segue a seção 6.10.

```markdown
### Tema 2 · Mapa · sem trava
- abertura: o que você já sabe do fenômeno, onde acha que o job falha, em que fontes confia e que casos conhece; pesquisa do fenômeno, e não do mercado
- plano de dose: 2.2, 2.3, 2.5 e 2.6 completas; 2.1, 2.4 e 2.7 padrão
- equipe-base: as especialidades do mapa inicial marcadas para o tema 2, e a distante; o mapa do 2.7 vale dali em diante
- integração: equipe-especialistas, modo integração, depois do 2.6
- validação integrada: conselho completo Evidência sobre o mapa inteiro, no fim do tema, com 1 ou 2 diagnósticos de contraste
- sai: 02-mapa.md; casos/candidatos.md, fechado; especialistas.md; "mapa" no estado.json

### 2.1 Job map
- dose: padrão
- pré-requisitos: tema 1
- grill quer entender: como você executa, ou vê executarem, cada etapa; onde o job passa de uma pessoa para outra; o que as pessoas improvisam
- triagem: não roda
- pesquisa: foco em como pessoas, instituições e ferramentas executam cada etapa hoje (estudos de observação, relatos de prática e dados de uso); 2 ou 3 pesquisadores
- equipe e alternativas: equipe-base, a partir da sua versão; cada etapa vira verbo e objeto, com o modo de hoje e a fonte, e a etapa que não se aplica fica marcada, com o motivo; 1 gerador cego monta outra decomposição, só a partir do job e das variações; operador sorteado: de trás para a frente, pela variação mais difícil, pelo erro ou pelo executor novato
- validação: conselho rápido Evidência (refutador de método e especialista do domínio); refuta se uma etapa não tem evidência de como é feita hoje, ou a decomposição esconde uma etapa com falha conhecida
- sai: 02-mapa.md, seção Job map, com as passagens, as variações e as gambiarras; CIR, seção 3

### 2.2 Falhas e causas
- dose: completa
- pré-requisitos: 2.1
- grill quer entender: onde você vê falhas, um caso vivido de cada uma, o que você acha que causa cada falha e o que faria você mudar de ideia
- triagem: não roda
- pesquisa: foco no mecanismo e na dependência de cada causa (estudos em que a causa muda e a falha é medida) e nos lugares onde a falha acontece sem a causa; 3 a 5 pesquisadores, um por especialidade; busca a favor e busca contra em pesquisadores separados, com a pergunta contra do cartão de causa
- equipe e alternativas: equipe-base elabora as árvores, com ramos e um ramo "outras causas", a partir da sua versão; 2 ou 3 geradores cegos propõem causas rivais, cada uma como cadeia de mecanismo, com o que se deveria observar; operadores: outra disciplina, caso desviante, inversão e nível do sistema; uma equipe de verificação, com especialistas que não elaboraram as árvores, testa as causas contra a evidência e entrega o parecer P-2.2-1
- validação: conselho completo Evidência sobre os cartões de causa, até 12 por conselho, a começar pelas falhas centrais; refuta se a falha persiste, igual, onde a causa está ausente, ou a causa só tem correlação, sem mecanismo
- sai: 02-mapa.md, seção Falhas e causas: as falhas, as árvores, os cartões de causa com a força da evidência e as rivais que ficaram de pé; o que não tem fonte fica marcado como hipótese; CIR, seção 3

### 2.3 Contradições e trade-offs aceitos
- dose: completa
- pré-requisitos: 2.1 e 2.2
- grill quer entender: que trade-offs você considera inevitáveis, por quê, e o que mostraria que não são
- triagem: roda sempre, sobre cada candidata a "de princípio": que teorema ou lei estaria por trás, e com que premissas?
- pesquisa: modo refutar; para cada contradição, a busca da prova (teorema ou lei, com as premissas) e a busca do contraexemplo (um caso em que os dois parâmetros melhoraram juntos) em pesquisadores separados; 2 ou 3 pesquisadores
- equipe e alternativas: listas independentes: a sua, a da equipe-base e as de 2 geradores cegos; operadores: parâmetros, valores, extremo e melhor de hoje; a equipe junta as listas e escreve cada contradição como par de parâmetros, com a forma física e a classe proposta; a equipe de verificação confere cada "de princípio" e entrega o parecer P-2.3-1
- validação: conselho completo Evidência, com um refutador de limites teóricos, sobre as contradições e o parecer; refuta se uma "de princípio" tem contraexemplo ou depende de uma premissa não escrita, ou uma "quebrável" tem prova de impossibilidade
- sai: 02-mapa.md, seção Contradições: as de princípio, com as premissas, viram restrições preservadas; os limites de hoje vão às fronteiras, com a data; as quebráveis viram desafios do 4.2; CIR, seções 3 e 5

### 2.4 Projeção de referência
- dose: padrão
- pré-requisitos: 2.1
- grill quer entender: o que você acha que vai acontecer se nada mudar, em quanto tempo e com base em quê
- triagem: não roda
- pesquisa: foco nas tendências do fenômeno e nas taxas-base da classe de referência, e não do mercado; 1 ou 2 pesquisadores
- equipe e alternativas: a sua projeção primeiro; 1 gerador cego monta a visão de fora, pela classe de referência, sem ver a sua projeção nem a ideia; a equipe-base ajusta a visão de fora ao caso, com o motivo de cada ajuste
- validação: conselho rápido (refutador e especialista do domínio); refuta se a tendência não tem fonte ou depende de preço e adoção
- sai: 02-mapa.md, seção Projeção, com dois horizontes e faixas; CIR, seção 3

### 2.5 Espaço K
- dose: completa
- pré-requisitos: 2.2 e 2.3
- grill quer entender: o que você toma como sabido, em que fontes confia e o que você acha que ninguém sabe
- triagem: não roda
- pesquisa: 3 a 5 pesquisadores em paralelo, um por especialidade e um de área distante, nos modos desenvolver e conferir; analogias buscadas pela função, com a pergunta sem as palavras do domínio
- equipe e alternativas: equipe-base junta as fichas e classifica cada afirmação em sabido, incerto e impossível de saber, com a distância de cada analogia; sem geradores
- validação: conselho completo Evidência, com o crítico conferindo cada ficha; refuta se o trecho da fonte não sustenta a afirmação, ou um limite da tecnologia atual foi registrado como impossibilidade
- sai: 02-mapa.md, seção Espaço K: teoremas e leis viram restrições preservadas; limites da tecnologia atual, fronteiras técnicas; lacunas, perguntas em aberto; CIR, seções 3, 5 e 15

### 2.6 Banco de casos
- dose: completa
- pré-requisitos: 2.1 e 2.2
- grill quer entender: que casos você conhece, com o desfecho, e quais seriam os mais difíceis para qualquer solução
- triagem: não roda
- pesquisa: casos documentados, com fonte e desfecho; 3 pesquisadores independentes, com cotas de tipo diferentes (falhas; sucessos e "nada relevante"; simetria e evidência contrária); em cada caso, o que se sabia antes, separado do desfecho, pela data de corte
- equipe e alternativas: sem geradores; os seus casos entram com a origem "sua"; a sonda de memória, no mesmo modelo dos geradores do tema 4, diz que casos ele já conhece
- validação: conselho rápido Evidência, com o crítico conferindo fatos e desfechos; refuta se o desfecho não é verificável, faltam casos de simetria, de evidência contrária ou de "nada relevante", ou só há desfechos de um lado
- sai: casos/candidatos.md, fechado, com 15 a 30 casos, cada um com fonte, desfecho, o que se sabia antes, por que é difícil e o marcador; no 02-mapa.md, só a contagem por tipo; o sorteio é no 3.6

### 2.7 Especialistas e conselhos do projeto
- dose: padrão
- pré-requisitos: 2.1 a 2.6 e a integração em equipe
- grill quer entender: que especialidades e escolas de pensamento você quer ouvir, ou evitar
- triagem: não roda
- pesquisa: foco em que disciplinas estudam cada causa e cada contradição; 1 pesquisador
- equipe e alternativas: pela `especialistas` (6.1 dela): 2 recrutadores independentes e a fusão; 1 gerador cego de disciplinas distantes; o inventario.py lista os itens do mapa, e o cobertura.py confere
- validação: conselho rápido (explorador e construtivo); refuta se uma causa ou contradição fica sem especialidade, ou dois membros repetem a mesma ótica
- sai: especialistas.md: as equipes de cada tema, com uma distante por tema, e a composição de cada template do conselho; especialidade sem skill fica marcada e vira lacuna

### Validação integrada do tema 2
- dose: integrada
- pré-requisitos: 2.1 a 2.7
- grill quer entender: se o mapa diz o que você vê no fenômeno e o que faria você reabrir uma causa
- pesquisa: dentro do conselho, cada membro no modo refutar
- equipe e alternativas: a integração em equipe vem antes; 1 ou 2 geradores cegos montam diagnósticos de contraste do zero, a partir do job e do fenômeno, sem ver nada do tema 2
- validação: conselho completo Evidência sobre o pacote do mapa e os contrastes, sem vencedor; refuta se uma falha central fica sem causa e sem a marca "causa desconhecida", uma causa sem evidência ou uma contradição sem classe, ou se um contraste traz uma falha central que o mapa não tem nem explica
- sai: o mapa validado; o que o contraste trouxe volta à sub-etapa, com registro
```

**Critérios do conselho,** escritos antes, um por linha da matriz; o "refuta se" é a falha que derruba:

| Sub-etapa | Critérios |
| --- | --- |
| 2.1 | Cada etapa é verbo e objeto, sem meio; cada etapa diz como é feita hoje, com fonte; as passagens entre papéis aparecem; as variações do 1.3 estão cobertas; a etapa que não se aplica tem o motivo; a decomposição cega não trouxe etapa com falha conhecida que falte no mapa |
| 2.2 | Toda falha central tem pelo menos duas causas, de origens diferentes; cada causa é uma cadeia de mecanismo; a dependência e o mecanismo têm fonte; o que se deveria observar foi escrito antes da busca; cada evidência tem o tipo de teste; a busca contra rodou; a força bate com a evidência; "erro humano" não fecha cadeia; toda árvore tem o ramo "outras causas" |
| 2.3 | Cada contradição é um par de parâmetros, com a forma física; toda "de princípio" traz o teorema ou a lei e as premissas; a busca do contraexemplo rodou em separado; "ninguém conseguiu" ficou como limite de hoje; nenhuma solução no texto; os conflitos de valores do 1.5 estão lá |
| 2.4 | Parte da classe de referência, com taxas-base e fonte; cada ajuste ao caso tem motivo; sem preço, adoção nem mercado; dois horizontes, com faixas; diz o que acontece com as partes centrais |
| 2.5 | Cada afirmação tem ficha, e o trecho a sustenta; o incerto diz o que o resolveria; o impossível de saber diz por quê; nenhum limite de hoje aparece como impossibilidade; cada analogia tem a função e a distância; cada afirmação diz o que mudaria no CIR se fosse falsa |
| 2.6 | Cada caso tem fonte e desfecho verificável; o que se sabia antes está separado do desfecho; as cotas de tipo estão cumpridas; há desfechos dos dois lados; cada caso diz por que é difícil para qualquer solução; os casos conhecidos do modelo estão marcados |
| 2.7 | Cada causa, contradição e parte tem especialidade; uma distante por tema; nenhuma ótica repetida; "sem skill" marcado; respeita as escolas que você pediu ou vetou |
| Integrada | Cada falha central tem causa, cada causa tem evidência e cada contradição tem classe; as peças não se contradizem; os casos exercitam as causas centrais; o contraste não traz falha central que o mapa não tenha nem explique |

**Especialidades que o tema costuma pedir,** ponto de partida do mapa inicial; quem decide é a `especialistas`, e o que faltar na biblioteca roda marcado, pela regra "sem skill":

| Sub-etapa | Especialidades |
| --- | --- |
| 2.1 | A do domínio; fatores humanos e análise de tarefas, pela execução observada |
| 2.2 | A do domínio; fatores humanos; ciência da segurança, pela análise de acidentes; economia e incentivos; estatística e inferência causal, pela dependência. São também as disciplinas dos geradores de causas rivais |
| 2.3 | Engenharia de sistemas, com TRIZ; matemática, física, estatística ou computação, conforme o teorema em jogo; ética aplicada, pelos conflitos de valores |
| 2.4 | Estudos de futuros e previsão; demografia, quando a tendência for de população |
| 2.5 | A do domínio; ciência da informação, pela busca; a distante, pelas analogias |
| 2.6 | A do domínio; história ou jornalismo investigativo, pela reconstrução dos casos; método de estudo de caso |

## 6. Método

O ciclo de 10 passos é o da condutora; aqui fica só o que é do tema 2. Os exemplos desta seção usam casos de fora dos testes (seção 9).

### 6.1 Abertura do tema

1. **Grill do tema,** com a abertura do cartão: o que você já sabe do fenômeno, onde acha que o job falha, em que fontes confia e que casos conhece. Pede casos vividos: a última vez que a falha aconteceu e o que se fez. Não pede opinião sobre o futuro, pelas regras da [`mom-test`, da wondelai](https://github.com/wondelai/skills/tree/main/mom-test), nem o porquê do comportamento de alguém, que as pessoas costumam explicar mal ([Nisbett e Wilson](https://doi.org/10.1037/0033-295X.84.3.231)).
2. **Fenômeno, e não mercado:** a condutora diz, na abertura, o que fica de fora: preço, disposição a pagar, tamanho de mercado e concorrência. Produto que já existe entra só como um modo de fazer o job hoje, pelo mecanismo e pelo lugar onde falha.
3. **Plano de dose:** o do cartão, que você ajusta. Descer pede o registro "pulado e risco". O 2.1 sobe para completa quando o job tem muitas passagens entre papéis; o 2.4 pode descer para leve quando o fenômeno é estável e a projeção não muda nada nos temas seguintes.
4. **Equipe-base:** as especialidades do mapa inicial marcadas para o tema 2 (seção 5), com as fichas escritas pela `especialistas`. O mapa do 2.7 substitui o inicial dali em diante.
5. **Sinais e guarda ligados desde a abertura:** a vigia passa a procurar os sinais do `sinais.py` (seção 10). Caso que você contar no grill vira candidato no `casos/candidatos.md`, com a origem "sua"; se ele também servir de evidência no 2.2, fica marcado "visto" e nunca vai para os reservados (seção 6.7).
6. **Dados de usuários,** se houver, entram aqui, pelo método da seção 6.11.

### 6.2 Job map (2.1)

As 8 etapas universais de [Bettencourt e Ulwick](https://hbr.org/2008/05/the-customer-centered-innovation-map), cada uma com uma pergunta que não cita meio:

| Etapa | Pergunta, sem meio | Onde costuma esconder falha |
| --- | --- | --- |
| Definir | O que quem executa precisa decidir ou planejar antes de começar? | Objetivos e critérios que ninguém escreve |
| Localizar | O que precisa ser reunido, como informação, coisas e pessoas, e de onde vem? | Insumos que dependem de outro papel |
| Preparar | O que precisa ser arrumado ou ajustado antes de executar? | Preparação feita de memória |
| Confirmar | O que precisa ser verificado para ter certeza de que está tudo pronto? | Conferência pulada na pressa |
| Executar | Qual é o centro do job, e o que pode dar errado enquanto ele acontece? | Atrasos e interrupções |
| Monitorar | Como quem executa sabe, durante o job, se está dando certo? | Sinal que chega tarde ou a quem não pode agir |
| Modificar | O que se ajusta quando algo sai do plano, e quem decide? | Exceção sem dono |
| Concluir | Como se sabe que terminou, e o que se faz ao terminar? | Passagem final e registro |
1. **Sua versão primeiro,** nas suas etapas, sem ver a lista. Depois, a lista entra como desafio de completude, por categoria: "que etapa sua corresponde a confirmar?". Nenhum exemplo de job map aparece antes da sua versão.
2. **Verbo e objeto, sem meio:** "confirmar que todas as crianças embarcaram", e não "conferir a lista no app". A etapa diz o quê, nunca com quê.
3. **Etapa que não se aplica fica marcada,** com o motivo ("não há o que modificar: a rota é fixa por contrato"). O crítico confere se o motivo não esconde uma falha.
4. **Como é feita hoje, com fonte:** quem executa, com quê, em quanto tempo e com que frequência falha, cada número com a ficha. Sem fonte, a linha fica marcada "hipótese"; os números que podem servir de linha de base ganham a marca "linha de base?", para o 3.3.
5. **Passagens:** onde o job passa de um papel a outro, numa linha própria, com o que passa e o que se perde. Passagens costumam esconder falhas.
6. **Variações:** cada variação do 1.3 percorre o mapa, e a etapa que muda ganha uma linha.
7. **Gambiarras:** o que as pessoas improvisam para dar conta. Como na [`synthesize-research`](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management/skills/synthesize-research), cada gambiarra é sinal de necessidade não atendida e vai ao 2.2 como evidência de falha.
8. **Decomposição cega:** o gerador vê só o job e as variações, nunca o mapa nem a sua versão, com um operador sorteado (seção 11). Etapa ou passagem que só a decomposição cega tem vira uma pergunta ao mapa: "o que acontece entre X e Y?". Entra no mapa se você e a equipe aceitarem, com a origem "G1".

### 6.3 Falhas e causas (2.2)

1. **O que é falha:** uma etapa ou passagem do job em que o resultado sai pior que o pretendido, para uma parte, com a frequência e a gravidade: "a criança chega depois do início da aula". "Falta de solução" não é falha: "não existe um aplicativo que…" vai para o banco.
2. **Falhas centrais:** as que mais pesam pelo propósito e pelas partes centrais, pelos sinais de intensidade da [`synthesize-research`](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management/skills/synthesize-research) (frequência, gravidade e emoção). A equipe sugere, e você escolhe; as outras ficam listadas, com o motivo de não serem centrais.
3. **Árvore com ramos:** cada falha central ganha uma árvore de causas, com ramos e um ramo "outras causas", que diz quanto acha que pesa. Árvores com ramos retirados pareceram completas a quem as leu ([Fischhoff, Slovic e Lichtenstein](https://doi.org/10.1037/0096-1523.4.2.330)); o ramo "outras causas" e a decomposição cega são a defesa. Ramo dividido em muitas partes parece pesar mais ([Tversky e Koehler](https://doi.org/10.1037/0033-295X.101.4.547)); a equipe confere se a árvore não dividiu demais o ramo favorito.
4. **Cinco porquês só dentro de um ramo,** para descer até onde dá para agir, com cada passo marcado como causa única ou ramo, como pede a `think-five-whys` da [thinking-framework-skills](https://github.com/product-on-purpose/thinking-framework-skills). Sozinhos, eles levam a uma cadeia única e dependem de quem pergunta ([Card](https://doi.org/10.1136/bmjqs-2016-005849)).
5. **Onde parar:** quando a próxima causa já não muda o que uma solução teria de fazer, quando sai do alcance do propósito, ou quando nenhuma evidência separa os próximos passos, e aí vira pergunta. As análises de causa raiz costumam parar cedo, numa causa só e em correções fracas ([Peerally et al.](https://doi.org/10.1136/bmjqs-2016-005511)).
6. **"Erro humano" não fecha cadeia:** pergunta-se o que tornou o erro provável: carga, desenho, informação, incentivo ou treino.
7. **Laços:** quando a falha alimenta a própria causa ("o ônibus atrasa, as famílias desistem, a rota perde crianças, a rota é cortada, o ônibus atrasa mais"), o laço fica desenhado, com o sentido de cada elo.
8. **Causas rivais:** toda falha central tem pelo menos duas causas, de origens diferentes: a sua, a da equipe e a dos geradores cegos. A rival é uma alternativa qualquer, e não só o oposto ([Hirt e Markman](https://doi.org/10.1037/0022-3514.69.6.1069)).
9. **Cadeia de mecanismo e o que se deveria observar, escritos antes:** cada causa é uma cadeia, "A leva a B, que leva à falha", com cada elo. Antes da busca, o cartão diz o que se deveria observar se a causa for verdadeira e se for falsa, como no process tracing da [thinking-framework-skills](https://github.com/product-on-purpose/thinking-framework-skills) ([Collier](https://doi.org/10.1017/S1049096511001429)).
10. **Busca a favor e busca contra, separadas,** em pesquisadores diferentes, com as perguntas contra escritas no cartão: "onde a falha acontece sem esta causa?" e "onde a causa está presente e a falha não?" ([Hart et al.](https://doi.org/10.1037/a0015701); [Sharma, Liao e Xiao](https://arxiv.org/abs/2402.05880)).

**Evidência tipada:** cada evidência entra com o tipo de teste:

| Teste | Se passar | Se falhar |
| --- | --- | --- |
| Palha ao vento | Aumenta um pouco a confiança | Diminui um pouco |
| Aro | A causa continua viva, sem ser confirmada | A causa cai |
| Arma fumegante | A causa fica confirmada | A causa não cai |
| Duplamente decisivo | Confirma esta causa e derruba as rivais | A causa cai |
| Não diagnóstica | Combina com todas as rivais: fica registrada e não pesa | — |

**Força da evidência,** que exige dependência e mecanismo, como nas ciências da saúde ([Russo e Williamson](https://doi.org/10.1080/02698590701498084)); os modelos confundem correlação com causa ([Jin et al.](https://arxiv.org/abs/2306.05836)), e o crítico e a verificação conferem:

| Força | Quando |
| --- | --- |
| Forte | A dependência foi medida (a falha muda quando a causa muda, por experimento, experimento natural ou comparação com controle), o mecanismo tem fonte, a causa passou num teste de aro ou de arma fumegante, e a busca contra não achou a falha, igual, sem ela |
| Média | Dependência e mecanismo têm fonte, mas a dependência vem de comparação sem controle ou de um contexto parecido, e não do mesmo |
| Fraca | Mecanismo com fonte e dependência só por relatos ou casos |
| Hipótese | Sem fonte, ou só correlação, sem mecanismo |

**Depois da busca:**

1. **Linhas, e não matriz:** cada causa é uma linha, com as suas evidências e os tipos ao lado. Nada de contar inconsistências nem de somar pesos: a matriz de hipóteses concorrentes não melhorou os julgamentos e deu peso a evidências pseudodiagnósticas ([Karvetski e Mandel](https://doi.org/10.1017/s1930297500008159); [Dhami, Belton e Mandel](https://doi.org/10.1002/acp.3550)), enquanto as hipóteses em linhas reduziram o viés de confirmação ([Dhami et al.](https://doi.org/10.1186/s41235-024-00560-y)).
2. **A observação que falta:** cada cartão diz qual seria a observação mais decisiva que ainda não se tem. Se for barata, vira pesquisa agora; se não, pergunta em aberto (CIR, seção 15).
3. **Verificação:** depois da elaboração, a equipe de verificação, com especialistas que não elaboraram as árvores e sem saber a autoria, recebe as afirmações técnicas dos cartões (a dependência, o mecanismo e o tipo de cada teste) e entrega o parecer P-2.2-1, afirmação por afirmação: sustenta, não sustenta ou incerto, com as contas e as fontes. O parecer não julga as causas; isso é do conselho.
4. **Conselho:** completo Evidência, às cegas, sobre os cartões de causa, com o parecer. Até 12 cartões por conselho, a começar pelas falhas centrais; com mais, outro conselho, e o que sobrar desce para rápido, com registro.
5. **Decisão:** por falha central, você decide que causas ficam como principais, que rivais ficam vivas (marcadas "rival viva", para os temas seguintes) e o que vira pergunta. "Causa desconhecida", com a observação que a resolveria, é uma resposta válida.

### 6.4 Contradições (2.3)

**Três classes,** e para onde vai cada uma:

| Classe | O que pede | Vai para |
| --- | --- | --- |
| De princípio | O teorema ou a lei, as premissas escritas, uma a uma, e a conta que liga os dois parâmetros | Restrição preservada, válida enquanto as premissas valerem (CIR, seção 5); candidata a limite ideal no 3.3 |
| Limite de hoje | Ninguém conseguiu melhorar os dois juntos, com as fontes do melhor de hoje e a data; nenhuma prova de impossibilidade | Fronteira técnica, com a data, e desafio do 4.2 |
| Quebrável | Um contraexemplo, ou seja, um caso em que os dois melhoraram juntos; ou nenhuma prova e nenhum limite conhecido | Desafio do 4.2 |
1. **De onde vêm:** os conflitos de valores do 1.5 em que nenhum cede; as causas do 2.2 que aparecem como "para melhorar A, piora B"; os trade-offs que a área dá como inevitáveis; e a sua lista.
2. **Listas independentes:** a sua (passo 2), a da equipe-base e as de 2 geradores cegos, com operadores diferentes: parâmetros (percorre uma lista de parâmetros genéricos, como tempo, quantidade, confiabilidade, segurança, esforço e informação, à maneira dos parâmetros da TRIZ), valores (parte dos conflitos do 1.5 e procura outros, parte a parte), extremo (leva um parâmetro ao limite e vê o que quebra) e melhor de hoje (parte da melhor abordagem atual e pergunta onde ela para de melhorar, e por quê).
3. **A forma:** cada contradição é um par de parâmetros ("quando A melhora, B piora"), com a forma física: o que liga os dois, como a mesma grandeza, o mesmo recurso ou o mesmo intervalo de tempo. Quando houver, também a contradição física: "o mesmo X precisa ser P e não P".
4. **Nada de resolver:** o "dá para resolver assim" que aparecer vai para o banco. O mapa é lido pelos geradores do tema 4, e uma solução escrita aqui vira o exemplo que eles copiam ([Jansson e Smith](https://doi.org/10.1016/0142-694X%2891%2990003-F)). Pelo mesmo motivo, o contraexemplo de uma quebrável fica na ficha, citado pelo número, e o desafio do 4.2 vai sem ele.
5. **Triagem, no passo 3:** sobre cada candidata a "de princípio", pergunta que teorema ou lei estaria por trás, e com que premissas. Se ninguém nomeia um, a candidata desce para limite de hoje ou quebrável antes da pesquisa.
6. **Prova e contraexemplo, em pesquisadores separados,** no modo refutar: um procura a prova, com as premissas; outro, sem ver o primeiro, procura o contraexemplo.
7. **Forma limite:** muitas vezes o teorema vale só no limite, como um mínimo ou um máximo, e o conflito de hoje está longe dele. A conta mostra a folga: o limite vira restrição, e o que fica entre o limite e o hoje é quebrável (exemplo na seção 8.4).
8. **Premissas visíveis:** cada premissa fica escrita, com a fonte; a restrição só vale enquanto ela valer. Premissa que uma solução poderia mudar é marcada "premissa móvel" e vai ao 4.2, sem resolver nada aqui.
9. **"Ninguém conseguiu" é limite de hoje,** nunca de princípio; e "todo mundo aceita" não é prova.
10. **Verificação e conselho:** a equipe de verificação confere cada "de princípio" (o teorema existe e diz o que se afirma, as premissas valem no caso, a conta fecha) e entrega o parecer P-2.3-1. O conselho completo Evidência, com um refutador de limites teóricos, julga a classificação.

### 6.5 Projeção de referência (2.4)

1. **Sua projeção primeiro,** no passo 2: o que acontece se nada mudar, em dois horizontes (por exemplo, 5 e 20 anos), e com base em quê.
2. **Visão de fora, cega:** um gerador que não viu a sua projeção nem a ideia escolhe a classe de referência (casos parecidos, de outros lugares ou épocas), com as taxas-base e as fontes, e projeta só por ela. A visão de dentro tende ao otimismo, e olhar casos parecidos corrige ([Kahneman e Lovallo](https://doi.org/10.1287/mnsc.39.1.17); [Flyvbjerg](https://doi.org/10.1080/09654310701747936)); o treino em raciocínio por classes de referência melhorou previsões num torneio ([Mellers et al.](https://doi.org/10.1177/0956797614524255)).
3. **Tendências do fenômeno:** população, clima, regras, infraestrutura e tecnologias de uso geral; nunca preço, adoção, mercado ou concorrência.
4. **Ajuste ao caso:** a equipe-base parte da visão de fora e ajusta, com o motivo de cada ajuste e quanto ele move. A distância entre a sua projeção e a de fora fica à vista.
5. **Dois horizontes, com faixas:** para cada parte central, o que acontece em cada horizonte, numa faixa (do mais provável ao pior razoável), nunca num número só.
6. **Para quê:** é a projeção de referência de Ackoff, o futuro que se teria se nada mudasse ([Ackoff, Magidson e Addison](https://archive.org/details/idealizeddesignc00acko)). No tema 3, ela é a base para dizer quanto uma solução precisa mudar.

### 6.6 Espaço K (2.5)

Na teoria C–K ([Hatchuel e Weil](https://doi.org/10.1007/s00163-008-0043-4)), o espaço K é o que se sabe; os conceitos, o espaço C, só aparecem no tema 4. Aqui, nenhum conceito.

| Classe | O que é | O que leva | Vai para |
| --- | --- | --- | --- |
| Sabido | Afirmação com ficha, e o trecho a sustenta | A ficha, o trecho, a força e o que mudaria no CIR se fosse falsa | CIR, seção 3; teoremas e leis viram restrições preservadas (seção 5) |
| Incerto | Ainda não se sabe, mas pode vir a se saber | O estudo, o dado ou o teste que resolveria, e quanto custaria | Pergunta em aberto (CIR, seção 15); se for barato, vira pesquisa agora |
| Impossível de saber | Inobservável, aleatório ou dependente de escolhas futuras | O porquê | CIR, seção 3: a solução terá de funcionar sem saber |
1. **Listar o que não se sabe:** considerar o que se desconhece reduziu o excesso de confiança ([Walters et al.](https://doi.org/10.1287/mnsc.2016.2580)); e as pessoas distinguem a incerteza do que se pode vir a saber da incerteza do acaso ([Ülkümen, Fox e Malle](https://doi.org/10.1037/xge0000202)). Daí a separação entre incerto e impossível de saber, cada um com o seu motivo.
2. **Suas crenças entram como as outras:** o que você toma como sabido, no grill, entra com a origem "sua" e passa pela mesma conferência; se a fonte não sustentar, vai para o incerto, com uma pergunta do grill.
3. **Limite de hoje não é impossibilidade:** o que ninguém conseguiu ainda vai às fronteiras, com a data. É o "refuta se" do cartão.
4. **Analogias pela função:** o pesquisador de área distante busca com a pergunta reescrita sem as palavras do domínio ("como levar itens frágeis de muitos pontos dispersos a um só lugar, num horário fixo?"). Buscar pelo propósito e pelo mecanismo rendeu ideias mais úteis e mais novas ([Kittur et al.](https://doi.org/10.1073/pnas.1807185116)); em problemas abertos a quem quisesse resolver, quem vinha de áreas mais distantes do problema teve mais chance de resolvê-lo ([Jeppesen e Lakhani](https://doi.org/10.1287/orsc.1090.0491)).
5. **Distância marcada:** cada analogia é próxima, moderada ou distante. Exemplos distantes renderam soluções mais novas ([Chan et al.](https://doi.org/10.1115/1.4004396)), mas distantes demais pioraram ([Fu et al.](https://doi.org/10.1115/1.4023158)); o tema 4 escolhe a dose.
6. **Analogia é conhecimento, e não solução:** entra com o mecanismo mapeado (o que corresponde ao quê); "dá para fazer como X" vai para o banco.
7. **Crítico em cada ficha:** modelos inventam e erram referências ([Walters e Wilder](https://doi.org/10.1038/s41598-023-41032-5)); o crítico confere se a fonte existe e se o trecho sustenta a afirmação.
8. **A equipe junta,** sem geradores: lê as fichas dos pesquisadores, tira as repetições, classifica cada afirmação e marca as contradições entre fontes, como na [`synthesize-research`](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management/skills/synthesize-research): quando as fontes discordam, as duas ficam, com o motivo provável.

### 6.7 Banco de casos (2.6)

Os casos são situações reais passadas, com desfecho conhecido, juntadas antes de existir qualquer solução, para que a prova do tema 5 não possa ser escolhida a dedo. Escolher casos pelo resultado distorce a conclusão ([Geddes](https://doi.org/10.1093/pan/2.1.131)); fixar as escolhas antes de ver os dados é a lógica do pré-registro ([Nosek et al.](https://doi.org/10.1073/pnas.1708274114)).

| Tipo | O que é | Cota mínima |
| --- | --- | --- |
| Comum | Uma situação típica do job | O resto, até fechar de 15 a 30 |
| Falha | O job falhou, com o desfecho registrado | 3 |
| Sucesso | O job deu certo em condições difíceis | 3 |
| Simetria | Dois casos com os mesmos dados e os lados trocados, em que o desfecho certo deveria trocar junto ou ficar igual, como nos testes de invariância e de direção da CheckList ([Ribeiro et al.](https://doi.org/10.18653/v1/2020.acl-main.442)) | 2 pares; um pode ser espelho construído a partir de um caso real, marcado "construído" |
| Evidência contrária | A evidência mais importante ia contra a leitura óbvia | 2 |
| Nada relevante | O certo era dizer que não havia o que fazer ou o que achar; sistemas treinados só com perguntas que têm resposta dão palpites onde não há ([Rajpurkar, Jia e Liang](https://doi.org/10.18653/v1/p18-2124)) | 2 |
| Seus | Os que você trouxe | Todos, com a origem "sua" |
1. **Antes de qualquer solução:** o banco fecha no tema 2. Caso que aparecer depois do tema 3 entra marcado "depois da solução" e nunca vai para os reservados.
2. **O antes separado do desfecho:** cada caso tem o que se sabia até a data de corte, escrito sem o desfecho, e o desfecho, à parte. Quem conhece o desfecho acha que ele era mais previsível do que era ([Fischhoff](https://doi.org/10.1037/0096-1523.1.3.288)); a pesquisa respeita a data de corte.
3. **Os dois lados:** desfechos bons e ruins. Banco só de falhas, ou só de sucessos, é o "refuta se".
4. **Por que é difícil:** cada caso diz por que seria difícil para qualquer solução, e não para uma em particular.
5. **Três pesquisadores independentes,** cada um com uma cota diferente: falhas; sucessos e "nada relevante"; simetria e evidência contrária. Nenhum vê o banco dos outros.
6. **Sonda de memória:** no mesmo modelo dos geradores do tema 4, a sonda recebe só o começo de cada caso, sem o desfecho, e tenta completá-lo. Se acerta detalhes que não estavam no começo, o caso fica marcado "conhecido do modelo". Modelos já viram muitos testes no treino ([Sainz et al.](https://doi.org/10.18653/v1/2023.findings-emnlp.722)), e o vazamento entre o que ajusta e o que testa infla resultados ([Kapoor e Narayanan](https://doi.org/10.1016/j.patter.2023.100804)).
7. **Guarda:** o `casos/candidatos.md` fica fechado. Cada caso tem um marcador único (⟦…⟧), procurado pela vigia em todos os briefs e saídas; o `brief.py` bloqueia o arquivo fora do 2.6 e do 3.6. No `02-mapa.md`, só a contagem por tipo.
8. **Sorteio no 3.6:** estratificado por tipo, com a semente registrada, pelo `casos.py sortear`. Os casos "vistos", "conhecidos do modelo" ou "depois da solução" só podem ir para os de trabalho; se faltar caso para os reservados de um tipo, a condutora pede mais, ou um espelho construído.

### 6.8 Especialistas e conselhos do projeto (2.7)

Roda o 6.1 do [Plano detalhado — especialistas](https://app.notion.com/p/Plano-detalhado-especialistas-79544cfde9c5403babc8e5cc62fe12cd?pvs=21), sem reescrever. Esta skill acrescenta só o `inventario.py`, que lista os itens que o mapa pede cobrir: as falhas centrais, as causas, as rivais vivas, as contradições, as partes do 1.4 e as lacunas do espaço K, com peso maior para as causas centrais e as contradições de princípio. O `cobertura.py` da `especialistas` confere o mapa contra essa lista; o resto (os dois recrutadores, a fusão, o gerador de distantes e a validação) é dela.

### 6.9 Integração e validação integrada

1. **Integração em equipe,** depois do 2.6 (`equipe/tema2-i1`): os conflitos entre as peças, como uma causa central sem caso que a exercite, uma premissa de contradição que a projeção desmente ou um item do espaço K que contradiz uma causa. Cada conflito volta à sub-etapa, com o que resolveria.
2. **Pacote do mapa,** montado pelo `pacote.py`, com até 600 palavras e sem autoria: as falhas centrais, as causas principais e as rivais vivas, as contradições por classe, a projeção, o essencial do espaço K e a contagem do banco.
3. **Diagnósticos de contraste:** 1 ou 2 geradores cegos montam, do zero, um diagnóstico do mesmo tamanho, a partir do job e do fenômeno, sem ver nada do tema 2. Não há vencedor: o conselho procura o que o contraste tem e o mapa não, e cada diferença volta à sub-etapa como pergunta, com registro.
4. **Causa desconhecida** vale como resposta, com a observação que a resolveria.
5. **Você decide** e fecha o tema; "mapa" entra no `estado.json`.

### 6.10 Reabrir

Reabrir é decisão sua, com registro. A condutora lista o que deriva da peça que muda e marca para revisão; onde nada muda, a revisão pode descer de dose, com registro.

| Se mudar | Revisar |
| --- | --- |
| Uma etapa do job map | As falhas e as causas daquela etapa; os casos que a exercitam |
| Uma causa central | As contradições que vêm dela; o espaço K ligado a ela; o mapa de especialidades (2.7); as métricas do tema 3 que dependem dela |
| A classe de uma contradição | As restrições preservadas e as fronteiras; os desafios do 4.2; o RFI e o teste do impossível (3.4 e 3.5) |
| A projeção | As linhas de base (3.3) |
| Um item do espaço K | As restrições e as fronteiras que vêm dele; as perguntas em aberto (CIR, seção 15) |
| O banco, antes do 3.6 | Só o banco |
| O banco, depois do 3.6 | Nada se sorteia de novo: o caso novo entra "depois da solução" |
| Uma parte nova, ou um job que não bate com o que se observou | Você decide se reabre o tema 1, pelo 6.9 do plano da `cir-proposito` |

### 6.11 Dados de usuários

1. **Quando houver dados** (entrevistas, registros, chamados, respostas abertas), a síntese segue a [`synthesize-research`](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management/skills/synthesize-research) e a [`research-synthesis`](https://github.com/anthropics/knowledge-work-plugins/tree/main/design/skills/research-synthesis): análise temática e affinity mapping; triangulação por método, por fonte e no tempo; comportamento acima da preferência declarada; gambiarras como necessidade não atendida; sinais de intensidade; "citação é evidência, não achado"; e as duas leituras à vista quando as fontes discordam.
2. **Cada dado vira ficha** "dados seus", com o trecho, e entra no 2.1 e no 2.2 como evidência. Nada de personas, segmentos ou dimensionamento.
3. **Roteiro de observação,** quando não há dados e você pode falar com quem executa o job: a última vez que fez, o que fez, o que já tentou, quanto tempo e esforço gasta hoje. Nunca "você usaria?" nem "quanto pagaria?": em perguntas hipotéticas, o valor declarado costuma passar do que as pessoas de fato pagam ([Murphy et al.](https://doi.org/10.1007/s10640-004-3332-z)).
4. **Nada de usuário simulado como dado:** um agente no papel de usuário não vira evidência; modelos que substituem participantes humanos distorcem e achatam os grupos que imitam ([Wang, Morgenstern e Dickerson](https://doi.org/10.1038/s42256-025-00986-z)).

### 6.12 Modo avulso

Fora da Etapa 1, a skill roda o job map, as falhas e causas e a classificação de contradições (2.1 a 2.3), em dose leve ou padrão: grill curto, a sua versão, o mapa, os cartões de causa com as rivais, as contradições com as premissas e o `sinais.py`. O conselho entra só se você pedir, no modo avulso dele. Tudo vai para `mapas/<data>-<assunto>/`, numa pasta com Git. O banco de casos e os especialistas só rodam pela condutora.

## 7. Regras que valem o tempo todo

1. **Fenômeno, e não mercado.** Nenhuma peça fala de preço, disposição a pagar, tamanho de mercado ou concorrência; produto que já existe entra só como um modo de fazer o job hoje.
2. **Nada de solução no mapa.** Ideia de solução vai para o banco, com a origem "tema 2"; assunto de Etapa 2 vai às fronteiras, e de Etapa 3, ao estacionamento.
3. **Causa pede mecanismo e dependência.** Só correlação, ou sem fonte, fica marcada como hipótese.
4. **Rivais antes de conclusão.** Toda falha central tem pelo menos duas causas, de origens diferentes, com o que se deveria observar escrito antes da busca.
5. **Busca contra separada,** sempre em outro pesquisador.
6. **Linhas, e não contagem.** Nada de somar pesos nem contar inconsistências.
7. **"De princípio" só com teorema ou lei e as premissas.** "Ninguém conseguiu" é limite de hoje.
8. **O incerto diz o que o resolveria; o impossível de saber diz por quê.**
9. **Visão de fora antes do ajuste,** na projeção.
10. **Casos antes da solução, com os dois lados,** e o que se sabia antes separado do desfecho.
11. **Casos fechados.** Nenhum brief fora do 2.6 e do 3.6 vê o `casos/candidatos.md`, e a vigia procura os marcadores.
12. **Sua versão primeiro, e categorias em vez de exemplos.** Nenhum exemplo de job map, causa, contradição ou projeção aparece para você antes da sua versão.
13. **O que as pessoas fizeram, e não o que dizem que fariam;** e nenhum agente no papel de usuário vira dado.
14. **Exemplos limpos.** Os exemplos de dentro da skill não usam os casos de teste.

**Pensamentos que pedem parada:**

| Pensamento | Realidade |
| --- | --- |
| "A causa é óbvia; não precisa de rival." | Pensar numa explicação alternativa reduz o viés de explicação ([Hirt e Markman](https://doi.org/10.1037/0022-3514.69.6.1069)). A causa óbvia passa pelo mesmo cartão, e passa rápido, se for mesmo óbvia |
| "Cinco porquês bastam." | Levam a uma cadeia só e dependem de quem pergunta ([Card](https://doi.org/10.1136/bmjqs-2016-005849)); use-os dentro de um ramo |
| "A árvore está completa." | Árvores com ramos faltando parecem completas ([Fischhoff, Slovic e Lichtenstein](https://doi.org/10.1037/0096-1523.4.2.330)); o ramo "outras causas" fica, com o peso |
| "A correlação é forte; é a causa." | Os modelos confundem correlação com causa ([Jin et al.](https://arxiv.org/abs/2306.05836)); sem mecanismo e dependência, é hipótese |
| "Achei três estudos a favor; está confirmado." | Quem busca acha o que procura ([Hart et al.](https://doi.org/10.1037/a0015701)); falta a busca contra, em outro pesquisador |
| "Vamos montar a matriz e somar." | A matriz com contagem não melhorou os julgamentos e deu peso a evidências pseudodiagnósticas ([Karvetski e Mandel](https://doi.org/10.1017/s1930297500008159)); cada causa é uma linha |
| "Você disse que a causa é X; você conhece o assunto." | Modelos tendem a concordar com quem fala ([Sharma et al.](https://arxiv.org/abs/2310.13548)). A sua causa passa pelo mesmo cartão, com a busca contra |
| "É de princípio; todo mundo da área sabe." | Sem teorema ou lei e as premissas, é limite de hoje ou quebrável |
| "Ninguém conseguiu; logo, é impossível." | É limite de hoje, com a data; vai às fronteiras |
| "Já que estamos aqui, vale anotar a solução." | Solução escrita no mapa vira o exemplo que os geradores copiam ([Jansson e Smith](https://doi.org/10.1016/0142-694X%2891%2990003-F)); vai para o banco |
| "O mercado vai crescer; a tendência é boa." | Mercado fica de fora; a projeção é do fenômeno, pela classe de referência |
| "Esses casos mostram bem o problema." | Escolher casos pelo resultado distorce a conclusão ([Geddes](https://doi.org/10.1093/pan/2.1.131)); valem as cotas de tipo e os dois lados |
| "O modelo conhece bem esse caso famoso; é ótimo para testar." | O que o modelo já viu no treino infla o teste ([Sainz et al.](https://doi.org/10.18653/v1/2023.findings-emnlp.722)); o caso fica marcado e só vai para os de trabalho |
| "Sabendo o desfecho, dá para ver que era previsível." | Quem conhece o desfecho superestima o que dava para prever ([Fischhoff](https://doi.org/10.1037/0096-1523.1.3.288)); o antes fica escrito sem o desfecho |
| "Pergunto ao agente como um usuário reagiria." | Agente no papel de usuário não é dado ([Wang, Morgenstern e Dickerson](https://doi.org/10.1038/s42256-025-00986-z)); valem os dados reais ou o roteiro de observação |
| "A fonte parece boa." | Modelos inventam e erram referências ([Walters e Wilder](https://doi.org/10.1038/s41598-023-41032-5)); o crítico confere cada ficha |

## 8. Formatos e modelos de documento

Os exemplos continuam o caso inventado do plano da `cir-proposito`, o transporte escolar na zona rural, de fora dos casos de teste. Números e fichas são fictícios.

### 8.1 O `02-mapa.md`

Uma seção por sub-etapa, cada uma aberta pelo registro e pela origem; o banco aparece só pela contagem.

```markdown
# Mapa · tema 2 · <projeto>
validação integrada: D-019 · conselho/tema2-r1 · contrastes C1 e C2, sem autoria
## Job map · 2.1
## Falhas e causas · 2.2
## Contradições · 2.3
## Projeção de referência · 2.4
## Espaço K · 2.5
## Banco de casos · 2.6 · só a contagem por tipo
## Especialistas · 2.7 · ver especialistas.md
## Pendências
```

### 8.2 Job map

Uma linha por etapa, com o modo de hoje e a fonte; depois, as passagens, as variações, as gambiarras e o que a decomposição cega trouxe.

```markdown
## Job map · 2.1
registro: D-012 · origem: sua, elaborada pela equipe (equipe/2.1-r1a) · decomposição G1 (de trás para a frente), sem autoria
job: levar uma criança de casa até a escola e de volta, todo dia letivo, quando a escola fica longe e não há transporte perto
| ID | Etapa | O quê | Quem executa | Como é feita hoje | Fonte | Falha conhecida |
|---|---|---|---|---|---|---|
| 2.1-1 | Definir | decidir por onde a rota passa e a que horas | quem decide o transporte | rota fixa no contrato, revista uma vez por ano | F-031 | a rota não acompanha as matrículas |
| 2.1-2 | Localizar | saber que crianças vão em cada dia | quem opera o transporte | lista do início do ano | F-032 | 18% dos nomes errados no meio do ano · linha de base? |
| 2.1-3 | Preparar | deixar a criança pronta no ponto, na hora | quem leva a criança | a família acorda a criança às 4h40 | F-014 | — |
| 2.1-4 | Confirmar | confirmar que todas as crianças embarcaram | o motorista | de memória | hipótese | ninguém sabe se faltou alguém |
| 2.1-5 | Executar | percorrer o caminho até a escola | o motorista | 1 veículo, 62 km de rota, de 20 a 35 crianças | F-033 | atraso, mais na chuva |
| 2.1-6 | Monitorar | saber, no caminho, se vai chegar a tempo | ninguém | não é feito | F-034 | a escola só sabe do atraso quando ele acontece |
| 2.1-7 | Modificar | mudar o plano quando a estrada fecha | quem decide o transporte | ligações, no mesmo dia | F-034 | exceção sem dono |
| 2.1-8 | Concluir | entregar a criança à escola e registrar a chegada | a professora da primeira aula | chamada em papel | F-035 | a hora real de chegada se perde |
| 2.1-9 | Concluir | devolver a criança a um adulto em casa | o motorista e quem leva a criança | deixa no ponto | F-057 | criança em casa sem adulto · trazida por G1 |
passagens:
- 2.1-3 → 2.1-5 · da família ao motorista, no ponto: passa a criança; perde-se quem não vai hoje
- 2.1-5 → 2.1-8 · do motorista à escola: passa a criança; perde-se a hora real de chegada
variações:
- a chuva fecha a estrada: mudam 2.1-5 e 2.1-7 (F-036)
- criança com deficiência: mudam 2.1-3 e 2.1-5, e entra uma etapa, confirmar o acompanhante (F-037)
gambiarras: o grupo de mensagens das mães para avisar do atraso (F-038) → 2.2
não se aplica: —
G1: "o que acontece entre 2.1-8 e a chegada em casa?" → aceito, 2.1-9
```

### 8.3 Falhas e causas

A falha, com a árvore; depois, um cartão por causa, com as evidências em linhas e o tipo de cada teste.

```markdown
## Falhas e causas · 2.2
registro: D-013 · árvores: equipe/2.2-r1a · rivais: G1 (economia), G2 (caso desviante) · parecer: P-2.2-1 · conselho/2.2-r1
### Falha 2.2-A · a criança chega depois do início da aula · central
onde: 2.1-5 · quem perde: a criança; a professora da primeira aula · frequência: 2 dias em cada 5, na época de chuvas (F-039) · gravidade: perde a primeira aula
- 2.2-1 · a rota é longa demais para o horário · principal
  - a rota soma crianças de três comunidades, para caber num contrato só · causa única
  - o contrato paga por quilômetro, e não por criança entregue a tempo · ramo → 2.2-3
- 2.2-2 · a estrada fica intransitável na chuva · principal
- 2.2-3 · o contrato não cobra pontualidade · rival viva (G1)
- outras causas · peso estimado: médio · descartada: quebra do veículo (F-040: 1 em cada 40 atrasos)
laço: atraso → famílias levam por conta própria → lista menor → rota refeita, mais longa → mais atraso (F-041)

### Cartão de causa 2.2-1 · a rota é longa demais para o horário
falha: 2.2-A · origem: sua, elaborada pela equipe
cadeia: rota de 62 km → 1h50 de viagem para quem embarca primeiro → saída às 5h10 → qualquer parada a mais estoura as 7h
deveria observar, escrito antes da busca:
- se verdadeira: o atraso cresce com o comprimento da rota; rotas curtas da mesma estrada atrasam menos
- se falsa: rotas curtas e longas atrasam igual; o atraso acompanha a chuva, e não a distância
perguntas contra: onde as rotas são curtas e o atraso é igual? onde a rota é longa e não há atraso?
| Evidência | Teste | Lado | Ficha |
|---|---|---|---|
| Em 14 rotas da região, o atraso cresce com o comprimento, na mesma estrada | aro | a favor | F-042 |
| Quando a rota 3 foi dividida em duas, os atrasos caíram de 38% para 9% dos dias | arma fumegante | a favor | F-043 |
| Na época de chuvas, as rotas curtas também atrasam | palha ao vento | contra | F-039 |
| Os motoristas dizem que "a rota é puxada" | não diagnóstica | — | F-044 |
dependência: medida na divisão da rota 3 (F-043), sem controle · mecanismo: tempo por quilômetro na estrada de terra (F-033)
força: média · por quê: a dependência vem de uma mudança só, sem comparação com controle
verificação: P-2.2-1, A3 sustenta; A4 incerto (a divisão coincidiu com a melhora de um trecho da estrada)
observação que falta: o atraso de rotas divididas sem mudança na estrada → pesquisa agora
rivais: 2.2-2 e 2.2-3
mudaria se: rotas curtas e longas, na mesma estrada, atrasassem igual
```

### 8.4 Contradições

Cada contradição com o par, a forma física, a classe e o destino; a de princípio leva as premissas e a conta.

```markdown
## Contradições · 2.3
registro: D-014 · listas: sua, equipe/2.3-r1a, G1 (parâmetros) e G2 (extremo) · parecer: P-2.3-1 · conselho/2.3-r1
2.3-1 · hora de chegada × hora de saída de casa · de princípio, só na forma limite
  origem: o conflito V4 × chegar a tempo, do 1.5
  forma física: o mesmo intervalo de tempo; t ≥ d / v máx.
  premissas: a criança percorre a estrada até a escola (móvel); a escola fica a 40 km (móvel); a velocidade segura na estrada é de até 60 km/h (F-045); a aula começa às 7h (móvel)
  conta: 40 km a 60 km/h dão 40 min, no mínimo; com a aula às 7h, sair entre 6h e 6h20 respeita V4 e chega a tempo
  restrição preservada: nenhuma criança a 40 km chega em menos de 40 min, enquanto as premissas valerem · candidata a limite ideal no 3.3
  entre o limite e o hoje (sair às 5h10): quebrável → 2.3-2
2.3-2 · crianças por viagem × tempo de viagem de quem embarca primeiro · quebrável
  forma física: a mesma viagem; cada criança a mais acrescenta paradas para todas as que já embarcaram
  prova: nenhuma · contraexemplo: F-046, na ficha
  → desafio do 4.2: levar mais crianças por viagem sem que quem embarca primeiro viaje mais
2.3-3 · adulto responsável em todo trecho (V1) × tempo de trabalho da família · quebrável
  prova: nenhuma · contraexemplo: F-047, na ficha
  → desafio do 4.2
2.3-4 · estrada transitável × época de chuvas · limite de hoje · 2026-11
  ninguém conseguiu manter a estrada de terra transitável em toda chuva, com os recursos de hoje (F-048 e F-049); nenhuma prova de impossibilidade
  → fronteiras.md, com a data; desafio do 4.2
```

### 8.5 Projeção de referência

A visão de fora primeiro, com a classe e as taxas-base; depois, o ajuste ao caso e a sua projeção, lado a lado.

```markdown
## Projeção de referência · 2.4
registro: D-015 · sua projeção; visão de fora: G1, cega · ajuste: equipe/2.4-r1a
classe de referência: municípios rurais que fecharam escolas pequenas e levaram os alunos para escolas maiores, de 2000 a 2020 (F-050)
taxas-base: o tempo de viagem subiu em 7 de cada 10; a frequência caiu de 2 a 6 pontos (F-050 e F-051)
| Parte | Em 5 anos | Em 20 anos | Ajuste ao caso e motivo |
|---|---|---|---|
| A criança | viagem de 1h30 a 2h; frequência de −2 a −5 pontos | de −4 a −10 pontos | para pior: mais duas escolas com fechamento previsto (F-052) |
| Quem leva a criança | mais famílias levando por conta própria | menos famílias com filhos na zona rural | para menos: saída das famílias jovens (F-053) |
| Quem decide o transporte | rotas mais longas a cada ano | — | sem ajuste |
sua projeção: "vai piorar devagar" · diferença para a visão de fora: a sua não contava com os fechamentos
```

### 8.6 Espaço K

Uma linha por afirmação, com a classe, a ficha ou o porquê, o que mudaria no CIR e o destino.

```markdown
## Espaço K · 2.5
registro: D-016 · pesquisadores: domínio, ciência da informação e distante · equipe/2.5-r1a · conselho/2.5-r1
| ID | Afirmação | Classe | Ficha ou porquê | Se fosse falsa | Destino |
|---|---|---|---|---|---|
| 2.5-1 | Na estrada de terra, a velocidade segura com o veículo cheio fica entre 40 e 60 km/h | sabido | F-045 | muda o limite do 2.3-1 | restrição preservada |
| 2.5-2 | Chegar depois do início da aula prejudica o aprendizado da primeira aula | incerto · resolveria: comparar notas por aula com a hora de chegada, num semestre | — | muda o peso da falha 2.2-A | PA-2.5-01 (CIR, seção 15) |
| 2.5-3 | Que criança vai adoecer em que dia | impossível de saber · aleatório | — | — | CIR, seção 3: a solução tem de funcionar sem saber quem falta |
| 2.5-4 | Coleta de leite nas propriedades: muitos pontos dispersos e hora fixa de chegada à usina | analogia · moderada | F-054 · pontos dispersos ↔ casas; hora da usina ↔ início da aula; leite que estraga ↔ criança que cansa | — | conhecimento; nenhuma solução |
```

### 8.7 Caso do banco

No `casos/candidatos.md`, fechado. O antes e o desfecho ficam separados, e o marcador vai em cada caso.

```markdown
### Caso 2.6-07 · ⟦c-41f9a2⟧
tipo: evidência contrária · origem: pesquisador 3 · sonda: não conhecido · visto: não · estado: candidato
o que se sabia até a data de corte (2019-03-01): um município dividiu a rota mais longa em duas; as famílias reclamavam dos atrasos
desfecho: a pontualidade melhorou e a frequência caiu, porque o novo ponto de embarque ficou a 3 km a pé de 11 crianças (F-055 e F-056)
evidência contrária: a que mais importava era a distância a pé até o ponto, contra a leitura óbvia de que o problema era só o atraso
por que é difícil: qualquer solução que melhore a pontualidade pode piorar o caminho até o ponto
fonte: F-055 (relatório da secretaria) e F-056 (reportagem)
```

A sonda de memória entrega uma linha por caso:

```markdown
sonda · modelo dos geradores do tema 4 · caso 2.6-07
recebeu: o antes, com os nomes e as datas, sem o desfecho
completou: "a pontualidade melhorou e a frequência subiu"
acertos que não estavam no antes: nenhum · conhecido do modelo: não
```

### 8.8 Pacote do mapa

O pacote e os diagnósticos de contraste têm as mesmas linhas e o mesmo limite de palavras, para que o tamanho e a forma não pesem no julgamento.

```markdown
# Pacote · tema 2 · até 600 palavras, sem autoria
job: levar uma criança de casa até a escola e de volta, todo dia letivo…
falhas centrais: 2.2-A a criança chega depois do início da aula; 2.2-B a criança espera sozinha no ponto
causas: 2.2-1 rota longa demais (média); 2.2-2 estrada na chuva (forte) · rival viva: 2.2-3 contrato sem pontualidade · 2.2-B: causa desconhecida, com a observação que resolveria
contradições: de princípio, só na forma limite: 2.3-1; quebráveis: 2.3-2 e 2.3-3; limite de hoje: 2.3-4
projeção: em 5 anos, viagem de 1h30 a 2h e frequência de −2 a −5 pontos
espaço K: 12 sabidos, 5 incertos e 2 impossíveis de saber; 3 analogias, 1 distante
banco: 24 casos · falha 4 · sucesso 3 · simetria 2 pares · evidência contrária 2 · nada relevante 2 · seus 3 · comuns 6
```

### 8.9 Entrega do gerador

Várias opções por gerador, cada uma com a probabilidade, incluindo as improváveis, e o que ele não sabe.

```markdown
gerador: G1 · 2.2 · operador: outra disciplina (economia e incentivos)
vê: o job, o job map sem as fontes e a falha 2.2-A · não vê: as árvores, a sua versão e as causas da equipe
R1 · probabilidade 0,40 · o contrato paga por quilômetro, e não por criança entregue a tempo
  cadeia: pagamento por quilômetro → rota longa rende mais → ninguém divide a rota → atraso
  deveria observar, se verdadeira: rotas pagas por criança entregue atrasam menos, na mesma estrada
  deveria observar, se falsa: o atraso não muda quando o contrato muda
R2 · probabilidade 0,25 · …
R3 · probabilidade 0,07 · improvável · …
não sei: como são os contratos da região
```

### 8.10 Registro de decisão

No formato da condutora; o campo "o que reverteria" vem do "mudaria se" dos cartões.

```markdown
### D-013 · 2.2 Falhas e causas · dose completa
- Contexto: as falhas 2.2-A e 2.2-B, com 7 cartões de causa; parecer P-2.2-1; conselho/2.2-r1, às cegas
- Opções: 2.2-1 e 2.2-2 como principais, com 2.2-3 viva; 2.2-3 como principal; "causa desconhecida" para 2.2-B
- Escolha: 2.2-1 e 2.2-2 principais; 2.2-3 rival viva; 2.2-B com causa desconhecida
- Motivo e objetivo: nas suas palavras
- Evidência: conselho/2.2-r1; P-2.2-1; fichas F-039, F-042 e F-043
- Dissenso: o refutador de método achou que a divisão da rota 3 (F-043) não separa 2.2-1 de 2.2-2, porque a estrada mudou junto
- Confiança: média
- O que reverteria: rotas curtas e longas, na mesma estrada, atrasarem igual
- Pulado e risco: —
- Vigia: limpa
- Commit: 4b7d2e9
```

## 9. Exemplos limpos e contaminados

Os exemplos que a skill mostra aos agentes, no `exemplos.md`, nos briefs do crítico e no `grill.md`. A você, nenhum aparece antes da sua versão (regra 12). Todos vêm de casos de fora dos testes: o transporte escolar na zona rural, o estoque de um pequeno restaurante e um sistema distribuído.

| Peça | Contaminado | Sinal | Limpo |
| --- | --- | --- | --- |
| Etapa do job | "Conferir a lista no app" | Meio e produto | "Confirmar que todas as crianças embarcaram" |
| Etapa do job | "Fazer o pedido no sistema do fornecedor" | Meio e produto | "Repor o que vai faltar antes que falte" |
| Falha | "Falta um aplicativo que avise o atraso" | Falta de solução no lugar da falha | "A escola só sabe do atraso quando ele acontece" (2.1-6) |
| Falha | "O restaurante não usa um sistema de estoque" | Falta de solução | "O ingrediente acaba no meio do pico de sexta-feira, 3 vezes por mês" |
| Causa | "Os motoristas são irresponsáveis" | "Erro humano" fecha a cadeia; sem mecanismo | "O contrato paga por quilômetro, e rota longa rende mais" (2.2-3), com o que se deveria observar |
| Causa | "Nas semanas de mais falta de ingrediente, as vendas foram maiores; logo, o volume causa a falta" | Só correlação, sem mecanismo | "O pedido sai na segunda, pela média do mês, e o pico de sexta não entra na conta" (mecanismo, com ficha); "quando o pedido passou para quinta, a falta caiu" (dependência, com ficha) |
| Rival | "A rival é: não é a rota" | O oposto, e não uma alternativa | Outra cadeia: "o contrato não cobra pontualidade" |
| Contradição | "Consistência × disponibilidade: a equipe nunca conseguiu as duas; é de princípio" | "Ninguém conseguiu" como prova | De princípio só com o teorema: numa rede assíncrona em que mensagens se perdem, nenhum sistema garante ao mesmo tempo consistência atômica e resposta a toda requisição ([Gilbert e Lynch](https://doi.org/10.1145/564585.564601)). Com as premissas escritas, sem partição de rede o conflito pode ser quebrável |
| Contradição | "Chegar a tempo × sair mais tarde de casa: é física, não tem jeito" | "De princípio" sem premissas nem conta; a lei vale só no limite | O 2.3-1: t ≥ d / v máx., com as premissas, a conta e a folga entre o limite e o hoje marcada como quebrável (seção 8.4) |
| Contradição | "Estoque × desperdício: o jeito é pedir na quinta" | Solução no mapa | O par de parâmetros, com a forma física; a ideia vai para o banco |
| Projeção | "O mercado de transporte escolar vai crescer 8% ao ano" | Mercado; número sem faixa | A visão de fora, pela classe de referência, com as taxas-base e as faixas (seção 8.5) |
| Projeção | "Em 5 anos, veículos autônomos resolvem isso" | Tecnologia e adoção | O que acontece se nada mudar; tecnologia de uso geral só como tendência com fonte |
| Espaço K | "Ninguém sabe se chegar atrasado atrapalha o aprendizado" | Incerto sem o que o resolveria | O 2.5-2, com o estudo que resolveria e quanto custaria |
| Espaço K | "É impossível manter a estrada transitável na chuva" | Limite de hoje como impossibilidade | Limite de hoje, com a data (2.3-4), nas fronteiras |
| Analogia | "Dá para fazer como a coleta de leite e criar pontos de encontro" | Analogia como solução | O 2.5-4, com a função e o que corresponde ao quê; a ideia vai para o banco |
| Caso | "O município que resolveu tudo com rastreio por GPS" | Escolhido pelo resultado; solução no caso | Um caso com o antes, o desfecho e o porquê de ser difícil para qualquer solução (seção 8.7) |
| Caso | "Em 2021, a rota 5 atrasou porque o motorista dormiu, e ninguém percebeu a tempo" | O desfecho misturado ao antes | O que se sabia até a data de corte, sem o desfecho; o desfecho à parte |
- **O `sinais.py` pega o que tem marca no texto:** preço, mercado, concorrente, disposição a pagar; produto e tecnologia fora do "como é feita hoje"; "de princípio" sem premissas e "impossível" sem teorema; causa sem ficha; "erro humano" no fim de uma cadeia; palavras de correlação ("associado a", "quanto mais… mais") num cartão sem mecanismo; "dá para" e "basta" no mapa. Rival que é só o oposto, árvore sem ramo e caso escolhido a dedo quase nunca têm marca; quem os pega são o crítico, a verificação e o conselho.
- **Os exemplos do Motor de Insights ficam no plano geral, no fluxograma e nos testes,** inclusive o de critérios de justiça que não valem juntos, no 2.3 do fluxograma. Dentro da skill, nenhum exemplo usa os casos de teste do plano geral (seção 13 dele), para que um teste não acerte por ter lido a resposta; uma busca confere (seção 13).

## 10. Arquivos

```
cir-mapa/
  SKILL.md                 o tema em umas 200 linhas: cartões, passos, regras e quem lê o quê
  references/
    cartoes.md             os cartões do tema, das sub-etapas 2.1 a 2.7 e da validação integrada (seção 5)
    fenomeno.md            fenômeno, e não mercado; o que fica de fora; produto como modo de hoje (6.1)
    job-map.md             as 8 etapas, as perguntas sem meio, as passagens, as variações,
                           as gambiarras e a decomposição cega (6.2)
    causas.md              falha, árvore, cinco porquês, onde parar, rivais, o que se deveria
                           observar, testes, força, verificação e decisão (6.3)
    contradicoes.md        listas, par de parâmetros, forma física, três classes, premissas
                           e forma limite (6.4)
    projecao.md            visão de fora, classe de referência, ajuste, horizontes e faixas (6.5)
    espaco-k.md            sabido, incerto e impossível de saber; analogias pela função (6.6)
    casos.md               tipos e cotas, o antes e o desfecho, sonda, guarda e sorteio (6.7)
    integracao.md          integração, pacote, contrastes e reabrir (6.9 e 6.10)
    dados-de-usuarios.md   síntese e roteiro de observação (6.11)
    geradores.md           os operadores de cada sub-etapa e o formato da entrega (seção 11)
    grill.md               perguntas boas e ruins, por sub-etapa
    exemplos.md            limpos e contaminados (seção 9)
    regras.md              as 14 regras, com os pensamentos e a realidade (seção 7)
    formatos.md            os modelos da seção 8
    origem.md              trechos aproveitados, com versão, licença e atribuição
  scripts/
    sinais.py              marca mercado, preço, solução, "de princípio" sem premissas, causa sem
                           ficha, "erro humano" no fim da cadeia e correlação sem mecanismo, por
                           peça; nunca bloqueia
    mapa.py                confere o 02-mapa.md: IDs; etapa com fonte ou "hipótese"; falha central
                           com 2 causas de origens diferentes; o "deveria observar" gravado antes
                           das fichas da busca, pelo histórico do Git; tipo em cada evidência;
                           força coerente; classe e premissas em cada contradição;
                           --mermaid desenha as árvores e os laços
    casos.py               confere o banco: cotas, dois lados, o antes sem desfecho, data de corte,
                           fonte e marcador único; sortear --semente separa trabalho e reservados
                           no 3.6, por tipo; --vazamento procura marcadores e trechos fora de casos/
    pacote.py              monta o pacote do mapa e confere os contrastes: as mesmas linhas,
                           até 600 palavras e sem autoria
    inventario.py          lista os itens do mapa, com o peso, no formato que o cobertura.py lê
    cartoes.py             confere os cartões contra o índice de sub-etapas da condutora
  assets/
    modelos/               os modelos da seção 8
    lexicos/               os termos do sinais.py, em português e em inglês, com as exceções
    parametros.md          os parâmetros genéricos do operador "parâmetros" (2.3)
  evals/                   os casos da seção 13
```

| Quem | Lê |
| --- | --- |
| Condutora | `SKILL.md`, `cartoes.md` e a referência do passo; roda os scripts |
| Grill | A abertura e o "grill quer entender" do cartão, com o trecho do `grill.md` da sub-etapa |
| Pesquisadores | O foco do cartão: no 2.2, a pergunta a favor ou a contra; no 2.3, a prova ou o contraexemplo; no 2.6, a cota de tipos e o formato do caso |
| Equipe | A pauta, com o trecho da referência da sub-etapa |
| Equipe de verificação | As afirmações técnicas dos cartões, sem autoria |
| Crítico da equipe | `regras.md`, `exemplos.md` e as saídas do `sinais.py` e do `mapa.py` |
| Geradores | O trecho do `geradores.md` com os seus operadores e o formato da entrega |
| Sonda de memória | O antes de cada caso, sem o desfecho |
| Conselho | Os critérios do cartão, o parecer, quando houver, e a saída do `sinais.py` |
- **Nenhum agente carrega a skill.** Cada um recebe, no brief, só o trecho do seu papel, montado pelo `brief.py` da condutora a partir dos cartões.
- **O `sinais.py` roda na vigia da condutora,** com `--peca job|falha|causa|contradicao|projecao|k|caso`. Os termos e as exceções ficam em `assets/lexicos/`, para crescer sem mexer no código; cada falso positivo vira uma exceção, com um caso de teste.
- **No Notion,** a skill vira uma página do banco de Skills, as referências viram subpáginas, e os scripts e modelos vão em Files, como nas outras skills.

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

## 12. Casos-limite

| Situação | Resposta | Registro |
| --- | --- | --- |
| Você pede o tamanho do mercado ou os concorrentes | Diz que fica fora da Etapa 1 e por quê; oferece o estacionamento; produto concorrente entra só como modo de fazer o job hoje | Estacionamento, com a origem "tema 2" |
| Você já sabe a causa e quer pular as rivais | Mostra o achado das rivais e roda o cartão rápido; a sua causa entra com a origem "sua" e passa pela busca contra | "Pulado e risco", se você insistir |
| Uma causa central não tem fonte | Fica "hipótese", com a observação que resolveria; vira pergunta a você e pergunta em aberto | Pendência |
| Toda a evidência de uma causa é correlação | Hipótese; pesquisa nova atrás do mecanismo; sem ele, "causa desconhecida" | Registro |
| Só uma causa parece plausível | Os geradores rodam mesmo assim; se nenhuma rival se sustentar, a falha fica com uma causa, e o registro diz por quê | Registro, com o dissenso |
| As fontes discordam | As duas leituras ficam, com o motivo provável (método, contexto ou época) | Ficha e registro |
| Você diz que uma contradição é de princípio, sem lei | Pergunta que lei estaria por trás; sem lei, fica limite de hoje ou quebrável; você pode discordar, e a pesquisa refuta | Registro |
| Há um teorema, mas as premissas não valem no caso | Fica quebrável, com a premissa que falha escrita | Parecer e registro |
| Uma contradição tem prova e contraexemplo | Uma das duas está errada, ou as premissas diferem; a verificação confere as premissas do contraexemplo | Parecer |
| Aparece uma solução no meio do mapa | Vai para o banco, e o texto volta sem ela | Banco, com a origem "tema 2" |
| Você não tem dados de usuários | O mapa roda com a pesquisa, e o roteiro de observação fica à disposição | — |
| Você quer que um agente simule os usuários | Explica por que não vira dado e oferece o roteiro de observação | Registro |
| Faltam casos de "nada relevante" ou de simetria | Um pesquisador só com essa cota; se ainda faltar, espelho construído, marcado | Pendência, com o risco no 3.6 |
| Quase todos os casos são conhecidos do modelo | Pede casos menos famosos (locais, recentes, de documentos) ou espelhos construídos; o 3.6 só reserva os não conhecidos | Registro |
| Você conta um caso depois do 2.6 | Antes do 3.6, entra no banco; depois, entra "depois da solução" | Registro |
| Você quer ver os reservados depois do sorteio | Mostra, com o aviso: quem conhece os reservados pode puxar a solução para eles | Registro |
| Aparece uma parte nova no meio do tema | Entra marcada "nova", e você decide se reabre o tema 1 (6.10) | Registro |
| O job não bate com o que se observou | Mostra a diferença; reabrir o 1.3 é decisão sua | Registro |
| Você quer pular o 2.4 | Pode, com o risco: o 3.3 fica sem o "se nada mudar" | "Pulado e risco"; pendência exigida no pronto |
| Há mais de 12 cartões de causa | Outro conselho, pelas falhas centrais; o resto desce para rápido | Registro |
| Um gerador traz só o oposto da causa da equipe | O crítico marca, e o gerador recebe o pedido de outra cadeia | Registro |
| Você pede, fora da Etapa 1, o mapa de um problema | Modo avulso (6.12) | Pasta `mapas/<data>-<assunto>/` |

## 13. Testes e métricas

**Casos com gabarito,** escritos por você antes de qualquer execução, como no plano da `cir-proposito`:

1. **Motor de Insights, sem o Anexo A,** na sala limpa da condutora: quantos dos 18 pontos fracos e dos 20 modos de falha o mapa reencontra, e o que ele traz que o Anexo A não tem. O gabarito é o próprio Anexo A, com uma regra de correspondência escrita por você antes (o que conta como "reencontrado"); um juiz cego, que não sabe de que execução vem cada mapa, aplica a regra.
2. **Motor de Insights, com o Anexo A:** o Anexo entra como material seu. Os casos dele vão ao banco com a origem "sua", e as falhas dele passam pelos mesmos cartões, com rivais e busca contra; o teste confere que nada do Anexo vira causa sem evidência.
3. **Água tratada chegando sem perdas a uma cidade:** causas técnicas e de incentivo misturadas; contradições com lei física e quebráveis; projeção com tendência de população.
4. **Hábito de exercício:** quem executa e quem vive o resultado são a mesma pessoa; nenhuma causa termina em "falta de força de vontade" sem mecanismo; os seus registros de treino, se houver, como dados seus.
5. **Reencontro de amigos:** um job de aspiração, com poucos dados, muitos "impossíveis de saber" e casos pessoais no banco.
6. **Mapas plantados:** 30 mapas, com as falhas do crítico (mercado, solução, causa só com correlação, rival que é o oposto, árvore sem "outras causas", "de princípio" sem premissas, limite de hoje como impossível, incerto sem o que resolveria, analogia como solução, caso com o desfecho no antes, banco de um lado só, marcador ausente), e 15 limpos parecidos. O `mapa.py`, o `casos.py` e o crítico têm de pegar todas, e os limpos têm de passar.
7. **Frases plantadas:** 40 contaminadas e 20 limpas parecidas, em português e em inglês, para o `sinais.py`.
8. **Guarda:** marcadores plantados nos casos, procurados em todos os briefs e saídas fora do 2.6 e do 3.6, nos dois ambientes.
9. **Sonda:** 10 casos famosos e 10 documentados depois do corte de treino do modelo; a sonda tem de marcar os primeiros e não marcar os outros.
10. **Usuário simulado,** o da condutora, com os quatro perfis; o teimoso insiste que a causa é uma só e que uma contradição é de princípio sem lei.
11. **Robustez, do plano geral:** pedir preço, tecnologia ou MVP; pedir dados inventados; dar uma ideia só; mudar o propósito no meio, quando o mapa para e a condutora pergunta se reabre o tema 1.

**Comparações que decidem o desenho,** todas às cegas:

1. **Causas rivais em linhas** contra a matriz de hipóteses concorrentes com contagem e contra nenhuma rival, no recall das causas do gabarito e na calibração da força.
2. **Árvore com ramos e "outras causas"** contra cinco porquês sozinhos.
3. **O "deveria observar" escrito antes** contra escrito depois da busca, na força dos testes.
4. **Busca contra em outro pesquisador** contra o mesmo pesquisador buscando os dois lados.
5. **Visão de fora cega primeiro** contra a projeção da equipe sozinha, em casos passados: projetar a partir do antes e comparar com o que aconteceu.
6. **Decomposição cega e diagnósticos de contraste** contra nenhum: se nunca trazem nada que fique, saem da dose padrão.

**Métricas:**

| Métrica | Como se mede | Alvo |
| --- | --- | --- |
| Recall do Anexo A | Pontos fracos e modos de falha reencontrados, pela sua regra de correspondência, pelo juiz cego | A definir com você depois da linha de base da fase 2; proposta: 2 em cada 3 |
| Além do Anexo A | Itens do mapa sem correspondência que você julga úteis | 3 ou mais |
| Rivais | Falhas centrais com duas causas de origens diferentes | Todas |
| Causas com mecanismo e dependência | Cartões "forte" e "média" com as duas fontes, pela verificação | Todos |
| "De princípio" | Contra o gabarito e o parecer: teorema, premissas e conta | Nenhuma sem os três |
| Mercado e solução no mapa | `sinais.py` e crítico | Nenhum no texto final |
| Cotas do banco | `casos.py` | Todas cumpridas |
| Vazamento de casos | Marcadores fora de `casos/` | Zero |
| Sonda | Famosos marcados e recentes sem marca | 9 de 10 em cada grupo |
| Aderência | Passos dos cartões cumpridos, pelos registros e pelo `estado.json` | 90% ou mais |
| Insistência | No usuário simulado: mostra a evidência, pergunta de novo e registra, sem ceder nem forçar | Em todos os casos |
| Exemplos limpos | Busca dos termos dos casos de teste em toda a skill | Nenhum |
| Cartões | `cartoes.py` contra o índice da condutora e o fluxograma | Nenhuma divergência |

**Aceite seu:** os temas 2 e 3 do Motor de Insights numa sessão real, com você, na fase 5. A skill está pronta quando você reconhece o mapa como fiel ao fenômeno e o recall do Anexo A, na sala limpa, chega ao alvo.

Fica o que vencer; no empate, o mais simples.

## 14. Riscos

| Risco | Sinal | O que fazemos |
| --- | --- | --- |
| Virar pesquisa de mercado | Preço, concorrência ou tamanho no texto | Regra 1, `sinais.py` e crítico; o assunto vai para o estacionamento |
| Causas sem evidência | Muitas causas centrais marcadas "hipótese" | Força tipada, verificação e conselho; "causa desconhecida" em vez de inventar |
| Casos escolhidos a dedo | Banco de um lado só, ou com tipos faltando | Cotas, três pesquisadores independentes e sorteio no 3.6 |
| Vazamento dos casos | Marcador fora de `casos/` | O `brief.py` bloqueia; a vigia e o `casos.py --vazamento` procuram |
| Memória do modelo | Caso famoso entre os reservados | Sonda; só casos não conhecidos vão para os reservados |
| Viés de confirmação na busca | Só fichas a favor | Busca contra em outro pesquisador; o "deveria observar" gravado antes da busca |
| Árvore incompleta | Sem "outras causas", ou etapa que só a decomposição cega viu | Ramo "outras causas", decomposição cega e diagnósticos de contraste |
| Rivais de fachada | Rival que é o oposto ou uma variação da principal | Crítico; operadores de outra disciplina e de caso desviante |
| Falsa impossibilidade | "De princípio" sem teorema | Triagem, verificação e refutador de limites teóricos |
| Falsa possibilidade | Quebrável que tinha prova de impossibilidade | Busca da prova em pesquisador separado; o "refuta se" do 2.3 |
| Solução infiltrada no mapa | "Dá para", "basta", mecanismo de solução no texto | Regra 2 e `sinais.py`; o contraexemplo fica na ficha |
| Projeção otimista ou de mercado | Sem classe de referência, ou com adoção | Visão de fora cega primeiro; o "refuta se" do 2.4 |
| Concordar com você | A sua causa passa sem busca contra ([Sharma et al.](https://arxiv.org/abs/2310.13548)) | A sua causa no mesmo cartão; conselho às cegas |
| Fontes inventadas | Referência que não existe ou trecho que não sustenta | O crítico em cada ficha e o `verificar.py` da pesquisa |
| Geradores parecidos | Rivais quase iguais entre geradores | Operadores sorteados, disciplinas diferentes e várias opções com probabilidade |
| Custo alto | Sessões acima do previsto no teste da fase 5 | Doses; até 12 cartões por conselho; o que não muda nada sai, pelas comparações |
| Método demais para um projeto pequeno | O tema demora mais do que vale | Plano de dose ajustado por você e o modo avulso |

## 15. O que fica de fora

- **Pesquisa de mercado:** concorrência, preço, disposição a pagar e tamanho de mercado.
- **Personas, segmentos, jornada de compra e roadmap.**
- **Soluções, conceitos e analogias como solução,** que vão para o banco e são do tema 4.
- **Métricas, linhas de base e limites,** que são do tema 3; daqui saem só os candidatos.
- **Pré-mortem e red team,** que são do tema 5.
- **Depuração de incidentes e análise de um evento só,** fora da Etapa 1.
- **Revisão de literatura avulsa,** que é da `pesquisa-cientifica`.
- **A matriz de hipóteses concorrentes com contagem,** pelos achados da seção 2.
- **Agentes que simulam usuários ou partes** ([Wang, Morgenstern e Dickerson](https://doi.org/10.1038/s42256-025-00986-z)).

## 16. Decidido e em aberto

**Decidido:**

- **Universal primeiro e Claude primeiro,** como no callout do topo.
- **Os cartões são o contrato com a condutora,** e o `cartoes.py` confere.
- **Fenômeno, e não mercado;** produto que já existe entra só como modo de fazer o job hoje.
- **O job map** tem as 8 etapas, com perguntas sem meio, a etapa que não se aplica marcada, as passagens, as gambiarras e a decomposição cega.
- **As causas** saem em árvore com ramos e "outras causas", com os cinco porquês só dentro de um ramo; as rivais são cadeias de mecanismo, com o que se deveria observar escrito antes; a evidência é tipada e fica em linhas, sem contagem; a verificação e o conselho completo julgam; "causa desconhecida" vale.
- **As contradições** são pares de parâmetros, com a forma física e três classes; "de princípio" pede teorema ou lei, premissas e conta; a triagem roda no passo 3; prova e contraexemplo vão a pesquisadores separados; a validação junta verificação e conselho completo, com um refutador de limites teóricos.
- **A projeção** começa pela sua e pela visão de fora cega, com dois horizontes e faixas.
- **O espaço K** tem três classes, cada uma com o que leva; as analogias são buscadas pela função, com a distância; o crítico confere cada ficha.
- **O banco** tem tipos e cotas, o antes separado do desfecho, os dois lados, a sonda e os marcadores; o sorteio é no 3.6, com semente, e caso "depois da solução" nunca vai para os reservados.
- **O 2.7** roda pela `especialistas`, com o `inventario.py` desta skill.
- **A validação integrada** tem 1 ou 2 diagnósticos de contraste, sem vencedor.
- **Os exemplos** vêm de fora dos casos de teste.
- **O modo avulso** roda só do 2.1 ao 2.3.
- **Critério máximo:** na dúvida entre dois desenhos, vale o que mais contribui para uma ideia melhor, mais criativa e eficaz; custo e tempo vêm depois.

**Em aberto:**

- **A regra de correspondência do Anexo A** (o que conta como "reencontrado") e o alvo de recall: são seus, escritos antes de qualquer execução.
- **Sonda e reservados:** se a sonda marcar quase todos os casos de um projeto, o que vale: espelhos construídos ou reservados conhecidos, com o risco? Proposta: espelhos construídos, marcados, e o tema 5 compara os dois grupos.
- **O limite de 12 cartões por conselho** só se confirma no teste de custo da fase 5.