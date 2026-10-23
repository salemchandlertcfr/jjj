# Plano detalhado — grill-embasado

<aside>
❓

**O que é:** o plano detalhado do `grill-embasado`, a skill que pergunta. Abre cada tema e cada sub-etapa do [Fluxograma completo — Etapa 1 (método IDEAL em ciclo)](../Fluxograma%20completo%20%E2%80%94%20Etapa%201%20(m%C3%A9todo%20IDEAL%20em%20cic%20f1f71e3bd5e6487ebdfc94cd7e9fa161.md) (passo 1, modo abertura), volta depois da pesquisa (passo 5, modo desafio) e confere as suas afirmações contra as fontes (passo 6, modo checagem). É o quarto plano da ordem da seção 15 do [Plano geral das skills — Etapa 1 (CIR)](../Plano%20geral%20das%20skills%20%E2%80%94%20Etapa%201%20(CIR)%2072d0fdc1db19433e9101d1ac3b3015ef.md) e segue os formatos do [Plano detalhado — etapa-1-cir (condutora)](Plano%20detalhado%20%E2%80%94%20etapa-1-cir%20(condutora)%20fccda0c36a5d403582b433a6f2b0657f.md), do [Plano detalhado — conselho-especialistas](Plano%20detalhado%20%E2%80%94%20conselho-especialistas%20f31c25a61c914fd98fe1f1ad81c09ed4.md) e do [Plano detalhado — pesquisa-cientifica](Plano%20detalhado%20%E2%80%94%20pesquisa-cientifica%20b0dde96c53b34b38aa26c8c474ce1071.md).

**Universal primeiro:** os modos, as regras, os formatos e os scripts valem em qualquer agente com chat. O que muda de uma ferramenta para outra fica no adaptador (seção 9). **Claude primeiro:** quem pergunta, o leitor do entendimento e a checagem são Claude.

</aside>

## 1. Propósito no fluxograma

**Propósito:** fazer você pensar e revelar o que tem em mente, com perguntas embasadas e sem resposta sugerida, e conferir as suas afirmações de fato contra as fontes.

| Responde por | Como se vê |
| --- | --- |
| Revelação | O que você sabe, quer e decidiria aparece no Entendimento, nas suas palavras, com a pergunta que o revelou |
| Base | Toda pergunta aponta para o cartão, o dossiê, uma resposta sua ou uma ficha conferida, e diz por que importa |
| Neutralidade | Nenhuma pergunta traz resposta recomendada, opções nas perguntas de reflexão, número antes da sua estimativa ou ideia de solução antes da sua versão |
| Economia | As perguntas vão na ordem do quanto a resposta muda a decisão e param quando nenhuma muda |
| Checagem | Cada afirmação de fato sua passa pela `pesquisa-cientifica`; o que a evidência contradiz volta a você com o trecho, uma vez |
| Fidelidade | As suas respostas ficam gravadas como você escreveu; a leitura da condutora aparece marcada |
- **Território, não roteiro.** A skill dá o objetivo, o padrão de qualidade e a regra de parada; quantas perguntas, quais e como ficam a critério do modelo, como manda o plano geral.
- **Não opina nem julga.** Não diz se a sua ideia é boa, nem quem está certo quando a sua resposta e a fonte divergem. Julgar é do conselho; decidir é seu.
- **Não gera alternativas.** No modo desafio, uma alternativa só entra se vier de uma ficha; ideias novas são das equipes e dos geradores.
- **Não pesquisa.** Fatos do mundo vão para a `pesquisa-cientifica`; o grill pergunta o que só você sabe ou decide.
- **Pronto quando:** nenhuma pergunta restante muda a decisão da sub-etapa, ou você disse "chega" e o que ficou sem perguntar está registrado com o risco; o Entendimento foi devolvido e você o corrigiu ou confirmou; e, no passo 6, cada afirmação de fato sua foi conferida ou marcada "não conferida".

## 2. Skills de base e o que se aproveita

| Base | O que se aproveita | O que é nosso | Licença |
| --- | --- | --- | --- |
| [`grilling`](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling) (Matt Pocock, v1.3.1) | Mapa das decisões em árvore; a fronteira, isto é, as perguntas cujos pré-requisitos já estão resolvidos; fatos são trabalho do agente, que manda buscar sem travar a conversa, e decisões são suas; termina quando nada fica assumido em silêncio; não age antes de você confirmar o entendimento | Sem resposta recomendada e sem "sim aceita a recomendação"; uma pergunta por vez nas de reflexão e rodadas curtas, de até 3, só nas rápidas de logística (o `grilling` passou para rodadas em tudo: as mesmas 13 perguntas em umas 3 rodadas, em vez de 13); base, motivo e tipo em cada pergunta; parada pelo valor da informação | MIT |
| [`grill-me`](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) e [`to-questionnaire`](https://github.com/mattpocock/skills/tree/main/skills/productivity/to-questionnaire) (Matt Pocock) | O `grill-me` só chama o `grilling`. O `to-questionnaire` transforma uma decisão que você não responde sozinho num questionário para a pessoa que responde | O questionário para outra pessoa fica de fora da v1 (seção 16) | MIT |
| [`brainstorming`](https://github.com/obra/superpowers/tree/main/skills/brainstorming) (superpowers, v7.0.0) | Cada mensagem termina com uma pergunta, numa frase, sem lista de respostas-exemplo; perguntas abertas primeiro, porque opções direcionam; perguntas ancoradas em casos ("me conte a última vez que…"); território, não roteiro; devolver o entendido em blocos de 200 a 300 palavras, marcando o que é palpite, e perguntar o que está errado ou faltando; um leitor novo que lista só as perguntas em que um palpite errado mudaria o plano; a tabela de pensamentos e realidades | Sem palpite para você corrigir, porque ele também direciona; o fluxo de construção, o companheiro visual e os protótipos ficam de fora | MIT |
| Fluxograma completo e plano geral | Os modos; os tipos de pergunta; o padrão de qualidade; as doses; o "grill quer entender" de cada sub-etapa; "sobe uma dose quando uma resposta sua contradiz a evidência" | — | Nosso |

**Cinco achados que mudam o desenho:**

1. **Perguntar extrai mais do que pedir um texto.** Em experimentos pré-registrados, modelos que faziam perguntas abertas ou montavam casos-limite informativos obtiveram respostas muitas vezes mais informativas que os prompts e os exemplos escritos pelas pessoas, que relataram menos esforço e consideraram pontos que não tinham previsto ([Li, Tamkin, Goodman e Andreas](https://arxiv.org/abs/2310.11589)). Num estudo de campo com umas 600 pessoas, um chatbot que fazia perguntas abertas e aprofundava as respostas obteve respostas mais informativas, relevantes, específicas e claras que um questionário on-line ([Xiao et al.](https://doi.org/10.1145/3381804)). Daí a conversa com aprofundamento, em vez de um questionário, e os casos-limite do modo desafio.
2. **A pergunta muda a resposta.** Trocar um verbo na pergunta ("smashed" em vez de "hit") elevou a velocidade estimada de um acidente filmado e, uma semana depois, fez mais gente dizer que viu vidro quebrado, que não estava no filme ([Loftus e Palmer](https://doi.org/10.1016/S0022-5371%2874%2980011-3)). Relatos de comportamento e de opinião dependem muito da redação, do formato e do contexto das perguntas ([Schwarz](https://doi.org/10.1037/0003-066X.54.2.93)). Daí: nenhuma resposta sugerida, nenhuma lista de opções nas perguntas de reflexão, palavras neutras e um script que procura perguntas indutoras.
3. **Modelos concordam com quem conversa com eles.** Cinco assistentes de IA muitas vezes admitiram erros que não tinham cometido quando o usuário duvidou, deram retorno enviesado pela opinião dele e repetiram os erros dele; pessoas e modelos de preferência às vezes preferiram a resposta bajuladora bem escrita à correta ([Sharma et al.](https://arxiv.org/abs/2310.13548)). Daí: o grill não opina nem elogia, e a checagem das suas afirmações não fica com a sessão que conversa com você. Vai para a `pesquisa-cientifica`, com scripts e, nas doses padrão e completa, com o relator numa sessão separada. Quando a sua resposta contradiz a evidência, o trecho continua na mesa.
4. **Perguntar demais piora as respostas, e escolher bem rende mais.** Num questionário on-line, quanto maior a duração anunciada, menos gente começou e terminou, e as respostas às perguntas do fim saíram mais rápidas, curtas e uniformes que as do começo ([Galesic e Bosnjak](https://doi.org/10.1093/poq/nfp031)). Com permissão para pedir esclarecimento em só 10% dos casos, escolher esses casos pela incerteza sobre a intenção do usuário dobrou o ganho em relação a escolher ao acaso ([Zhang e Choi](https://arxiv.org/abs/2311.09469)). É a lógica do valor da informação, a mesma da dose ([Howard](https://doi.org/10.1109/TSSC.1966.300074)): o grill pergunta na ordem do quanto a resposta muda a decisão e para quando nenhuma muda.
5. **Caso vivido antes de opinião geral.** O método de decisão crítica, uma variante da técnica do incidente crítico, extrai o saber de profissionais experientes, de comandantes de bombeiros a programadores, com sondagens sobre as pistas que eles notam, as distinções que fazem e o que acham típico ([Klein, Calderwood e MacGregor](https://doi.org/10.1109/21.31053)). Daí as perguntas ancoradas em casos, "conte a última vez que…", antes de qualquer generalização.

## 3. Acionamento

```yaml
---
name: grill-embasado
description: >-
  Faz perguntas embasadas para a pessoa pensar e revelar o que tem em mente:
  uma ideia por pergunta, cada uma com a base (fonte conferida, trecho do
  dossiê ou resposta anterior), o motivo e o tipo, sem resposta sugerida e na
  ordem do quanto a resposta muda a decisão. Tem três modos: abertura (o que
  a pessoa sabe, quer e decidiria), desafio (perguntas a partir das fontes,
  com "e se" e contraexemplos) e checagem (as afirmações de fato dela contra
  as fontes). Use quando a condutora da Etapa 1 abrir um tema ou uma
  sub-etapa ou voltar da pesquisa, ou quando o usuário pedir para ser
  questionado, sabatinado ou "grelhado" sobre uma ideia, um plano ou uma
  decisão. Não use para opinar, gerar ideias, julgar hipóteses, pesquisar um
  assunto ou montar um questionário para outra pessoa.
license: (a definir)
compatibility: Qualquer agente com chat; Python 3 para os scripts; a checagem usa a pesquisa-cientifica
metadata:
  versao: "0.1"
---
```

- **Só os campos do padrão aberto,** como nas outras skills.
- **Chamada pelo nome é o caminho principal:** "Use a skill `grill-embasado`, modo abertura, dose completa, com o cartão da 1.1." Fora da Etapa 1, a skill roda avulsa (seção 5.4).

| Deve acionar | Não deve acionar (quase acertos) |
| --- | --- |
| "Me grelha sobre esta ideia antes de eu escrever a minha versão." | "O que você acha da minha ideia?" (opinar é do conselho) |
| "Abre a 1.3 com o grill." | "Me dá dez ideias para o job." (gerar é das equipes e dos geradores) |
| "Faz as perguntas do passo 5 da 2.2 a partir das fichas." | "Qual hipótese é a melhor?" (julgar é do conselho) |
| "Confere o que eu respondi contra as fontes." | "Pesquisa o que se sabe sobre viés de confirmação." (é da `pesquisa-cientifica`) |
| "Me questiona até não sobrar dúvida sobre o propósito." | "Monta um questionário para eu mandar ao meu sócio." (fica de fora da v1) |
| "Quero pensar nos trade-offs antes de decidir; me pergunta." | "Revisa o texto do CIR." |

A lista completa, com 10 de cada lado, entra nos testes (seção 14).

## 4. Contrato de entrada e saída

| Entrada | De quem | Forma |
| --- | --- | --- |
| Modo e dose | Condutora | Abertura, desafio ou checagem; leve, padrão ou completa |
| Objetivo das perguntas | Skill de método, pelo cartão | O "grill quer entender" da sub-etapa, ou a abertura do tema |
| O que o dossiê já sabe | Dossiê | A ficha do projeto, as saídas anteriores e `grill/respostas.jsonl` |
| Fichas e relatório, no modo desafio | `pesquisa-cientifica` | `fontes/relatorios/<brief>.md` e as fichas citadas |
| Sua versão, no modo desafio | Passo 2 | O trecho da saída da sub-etapa com a sua versão |
| Conferência, no modo checagem | `pesquisa-cientifica`, modo conferir | `fontes/conferencias/<id>.md` |
| Pedido avulso | Você | Texto livre: a ideia, o plano ou a decisão em jogo |

| Saída | Para quem | Onde |
| --- | --- | --- |
| Perguntas, com base, motivo, tipo e valor | Você | Na conversa, uma por mensagem nas de reflexão e até 3 nas rápidas de logística, e em `grill/<sub-etapa>.md` |
| Suas respostas, como você escreveu, com as afirmações separadas | Dossiê | `grill/respostas.jsonl` |
| Afirmações de fato para conferir | `pesquisa-cientifica`, modo conferir | `grill/conferir/<sub-etapa>.json` |
| Checagem: a afirmação, a evidência, o que foi mostrado e o que você fez depois | Dossiê e condutora | `grill/<sub-etapa>.md`, seção Checagem |
| Entendimento | Saída da sub-etapa | A seção "Entendimento" do arquivo da sub-etapa, como `01-proposito.md` |
| Fatos do mundo para a pesquisa do passo 4 e ideias suas para o banco | Condutora | No resumo |
| Não perguntado, pendências e sinal de dose | Condutora | No resumo; a condutora registra em "pulado e risco" e sobe a dose |
| Resumo de umas 150 palavras e os caminhos | Condutora | Na resposta |

A pasta `grill/` entra no dossiê (seção 11 do plano geral), como `fontes/` e `conselho/`.

**Contratos com as outras skills:**

| Skill | Relação |
| --- | --- |
| `etapa-1-cir` | Carrega esta skill e pergunta ela mesma; passa o modo, a dose e o cartão; grava o Entendimento; leva os fatos do mundo ao brief do passo 4 e as ideias suas ao banco; sobe a dose quando o grill avisa; registra "pulado e risco"; retoma pelo `estado.json` |
| `cir-*` | Dão, no cartão, o "grill quer entender" e, no tema, a abertura |
| `pesquisa-cientifica` | No modo desafio, dá as fichas; no passo 6, recebe as afirmações de fato, sem dizer de quem são, e devolve a conferência (seção 6.6 do plano dela) |
| `conselho-especialistas` | No pedido avulso vago, usa o grill curto para fixar a pergunta, as opções e os critérios com "refuta se", antes do painel. O grill não julga |
| `especialistas` | Usa o que o grill registrou na 2.7: as especialidades e as escolas de pensamento que você quer ouvir, ou evitar |
| `equipe-especialistas` | Recebe o Entendimento na pauta; não chama o grill |
| `cir-sintese` | Leva ao CIR o Entendimento e a checagem de cada sub-etapa |

## 5. Modos e doses

### 5.1 Modos

| Modo | Pergunta | Entra em | Base das perguntas | Entrega |
| --- | --- | --- | --- | --- |
| Abertura | O que você sabe, quer e decidiria? | Passo 1 de toda sub-etapa; abertura de cada tema; tema 0 | O cartão, o dossiê, as suas respostas anteriores e, quando houver, a visão geral do fenômeno; nunca uma ideia de solução | Entendimento; fatos do mundo para a pesquisa |
| Desafio | O que as fontes mudam no que você pensa? | Passo 5 | As fichas do passo 4, com a força e o lado; a sua versão; restrições e fronteiras | Perguntas com "e se", contraexemplos e alternativas das fontes; as suas respostas |
| Checagem | As suas afirmações de fato se sustentam? | Passo 6 | A conferência da `pesquisa-cientifica` | Uma linha por afirmação; o que você fez depois; o sinal de dose |

### 5.2 Doses

| Dose | Abertura (passo 1) | Desafio (passo 5) | Checagem (passo 6) | Quem confere a parada |
| --- | --- | --- | --- | --- |
| Leve | Sempre; o modelo decide quantas perguntas | Só se a pesquisa trouxer algo que mude a decisão | Só as afirmações centrais, pelo índice e pelos scripts; a condutora mostra o trecho ao lado, sem relator | O próprio grill, com a lista do que não perguntou e por quê, e o leitor do entendimento, numa sessão nova |
| Padrão | Sempre | Sim | Todas as afirmações de fato, com o relator da pesquisa; busca focal nas centrais sem ficha | Idem |
| Completa | Até não restar dúvida que mude a decisão | Sim, com "e se" e contraexemplos | Idem, com busca focal em todas as que não têm ficha | Idem; se a checagem mudar o Entendimento, o leitor lê de novo |
- **A dose vem do cartão,** e a condutora a sobe quando uma resposta sua contradiz a evidência (seção 2.3 do fluxograma).
- **Atalho com hipótese pronta:** grill curto, só com o que a triagem precisa: a hipótese nas suas palavras, para que serve, o que a refutaria e o que você não aceitaria.

### 5.3 Tipos de pergunta

| Tipo | Para quê | Exemplo neutro | Onde mais aparece |
| --- | --- | --- | --- |
| Esclarecimento | Fixar o sentido de uma palavra ou afirmação sua | "Quando você diz 'insight', o que conta como um, e o que não conta?" | Abertura |
| Suposição | Expor o que a afirmação dá por certo | "O que precisa ser verdade para isso funcionar como você descreve?" | Abertura e desafio |
| Evidência | Ver em que a afirmação se apoia | "Conte a última vez que você viu isso acontecer." | Abertura; no desafio, a partir de uma ficha |
| Alternativa | Comparar com outro caminho que você já considerou, ou que uma fonte descreve | "Que outro caminho você considerou, e por que ficou com este?" | Abertura e desafio |
| Consequência | Ver o que decorre | "Se funcionar como você descreve, o que muda para quem decide no primeiro mês?" | Desafio |
| "E se" | Mudar uma condição | "E se os dados chegarem com uma semana de atraso?" | Desafio, na completa |
| Contraexemplo | Pôr na mesa um caso que contraria | "A F-061 relata um caso em que priorizar pelo clique não reduziu a variedade do que a pessoa viu. Como esse caso se compara com o seu?" | Desafio, na completa |
| Limite teórico | Confrontar com um teorema, uma lei ou um limite de princípio | "Pela F-070 (força 1), o efeito de uma recomendação numa pessoa não se observa diretamente; só se estima comparando grupos. A sua versão depende de medir esse efeito para cada pessoa?" | Desafio, a partir das restrições |

### 5.4 Modo avulso

Fora da Etapa 1, sem cartão, o grill pergunta primeiro o que está em jogo: que decisão a conversa deve ajudar a tomar e o que mudaria essa decisão. Daí monta o mapa e segue as mesmas regras. Os fatos do mundo vão para a `pesquisa-cientifica`, se ela estiver instalada; se não, ficam marcados "não conferida". Com computador, grava tudo em `grill/<data>-<assunto>.md`, numa pasta com Git; sem computador, devolve o Entendimento na conversa. O grill curto que o conselho usa no pedido vago é este modo, com um objetivo fixo: a pergunta, as opções e os critérios com "refuta se".

## 6. Passos

### 6.1 Ao receber o pedido

1. **Lê o cartão, a dose e o dossiê:** o "grill quer entender", o que as sub-etapas anteriores registraram e as suas respostas anteriores (`respostas.py --buscar`). Não pergunta o que já está respondido; se o contexto mudou, cita a resposta antiga e pergunta se ela ainda vale.
2. **Monta o mapa do que falta entender:** cada desconhecido vira um nó, com o que depende dele. Classifica cada nó: fato do mundo (vai para a pesquisa), fato que só você sabe (pergunta) ou decisão e valor (pergunta).
3. **Dá a cada nó o seu valor:** que parte da saída da sub-etapa muda conforme a resposta. O nó que não muda nada sai do mapa, com o motivo.
4. **No modo abertura, nada de solução:** nenhuma pergunta carrega ideia de solução, exemplo de produto ou mecanismo antes da sua versão (passo 2), porque quem vê um exemplo tende a copiá-lo ([Jansson e Smith](https://doi.org/10.1016/0142-694X%2891%2990003-F)).

### 6.2 Cada pergunta

1. **Escolhe a próxima:** entre as perguntas da fronteira, as que não dependem de outra em aberto, a de maior valor.
2. **Escreve no formato da seção 8 e confere com o `perguntas.py`:** formato, base válida, uma pergunta só (ou até 3, numeradas, nas rápidas de logística), sem recomendação, sem opções nas de reflexão, sem número antes de uma estimativa e sem elogio ou concordância na mensagem. O que o script só suspeita, como um pressuposto ou uma pergunta dupla, volta marcado: a condutora reescreve ou justifica no registro. Se a pergunta for reprovada duas vezes, não vai.
3. **Manda a pergunta, a base, o porquê e o tipo,** numa mensagem, e espera. Nas perguntas rápidas de logística que não dependem umas das outras, como as do 0.3, manda até 3 juntas, numeradas; nas de reflexão, uma por vez.
4. **Começa aberta e concreta:** um caso vivido antes da regra geral; as sondagens vêm depois (o que você notou primeiro, o que pesou, o que esperava que acontecesse).

### 6.3 Cada resposta

1. **Grava como você escreveu** (`respostas.py`), com a pergunta e a hora.
2. **Separa o que a resposta contém:** afirmações de fato do mundo, fatos seus, decisões e valores, ideias suas e "não sei". A ideia sua vai para o banco de ideias, pela condutora, com a origem "você".
3. **Aprofunda só se** a resposta abriu algo que muda a decisão; senão, volta ao mapa.
4. **Refaz a fronteira** e volta ao 6.2.

### 6.4 Devolver o entendido

A cada parte entendida, o grill devolve um bloco de 200 a 300 palavras com as suas palavras, marca como "leitura" o que é ligação ou resumo dele e termina perguntando o que está errado ou faltando. As correções viram respostas. "Faz sentido" não confirma o que você não leu: a confirmação vale para o bloco devolvido.

### 6.5 Parada

- **Para quando nenhuma pergunta da fronteira muda a decisão.** Cada candidata descartada fica no registro com o motivo, como "as respostas possíveis levam à mesma saída".
- **"Chega" encerra:** o que ficou sem perguntar vai para "não perguntado", com o valor e o risco, e a condutora o registra em "pulado e risco".
- **Sinais de cansaço,** como respostas cada vez mais curtas ou "tanto faz" seguidos: o grill oferece uma pausa e, se você seguir, fica só nas perguntas de maior valor.
- **Em toda dose, o leitor do entendimento** (seção 12), numa sessão nova, lê só o cartão e o Entendimento e lista as perguntas em que um palpite errado mudaria a saída, por importância, ou "nada importante faltando". As que são suas voltam ao 6.2; os fatos vão para a pesquisa.

### 6.6 Modo desafio (passo 5)

1. **Lê** o relatório da pesquisa, as fichas, a sua versão e o Entendimento.
2. **Candidatas:** cada ficha que contradiz ou amplia a sua versão; cada restrição e fronteira; cada lacuna da pesquisa que você talvez conheça por experiência.
3. **A pergunta mostra a força da ficha** e se o apoio foi conferido ("um estudo, força 4, evidência indireta"). Não diz "a fonte prova" nem conclui por você.
4. **Na dose completa,** entram "e se" e contraexemplos, sempre que as fichas permitirem.

### 6.7 Modo checagem (passo 6)

1. **Junta as afirmações** (`respostas.py --conferir`): só as de fato do mundo, das suas respostas dos passos 1 e 5, com as fichas que você citou. Decisões, valores e fatos só seus não vão; são seus.
2. **A `pesquisa-cientifica`, modo conferir,** devolve uma linha por afirmação: sustenta, sustenta em parte, não sustenta, contradiz ou sem fonte.
3. **Quando contradiz:** o grill mostra o trecho e a força ao lado das suas palavras e pergunta de novo, uma vez, sem dizer quem está certo: "A F-061 (força 4) diz […]. Na Q-4.7-03, você disse "[…]". Como isso se encaixa no que você disse?" Registra o que você fizer: mudou, com o motivo; manteve, com o motivo; ou manteve sem motivo. Avisa a condutora, que sobe a dose.
4. **Quando não sustenta ou sustenta em parte:** mostra o que falta e pergunta se há outra base.
5. **Sem fonte:** fica marcada "sua afirmação, sem fonte"; se for central, a condutora decide entre mais pesquisa e o registro como lacuna.

### 6.8 Entrega

O `entendimento.py` monta a seção "Entendimento" da saída da sub-etapa e confere que cada frase aponta para uma resposta, um trecho do dossiê ou uma leitura marcada. O grill devolve à condutora um resumo de umas 150 palavras: o que mudou no entendimento, os fatos para a pesquisa, as ideias suas, as pendências, as contradições e o sinal de dose.

## 7. Regras que valem o tempo todo

| Regra | Por quê | Como se garante |
| --- | --- | --- |
| Nenhuma resposta sugerida: sem recomendação, sem "sim aceita" e sem palpite para você corrigir | A redação e o formato da pergunta mudam a resposta (achado 2) | `perguntas.py` e julgamento cego nos testes |
| Sem opções nas perguntas de reflexão | Opções direcionam (`brainstorming`), e as alternativas oferecidas mudam o relato ([Schwarz](https://doi.org/10.1037/0003-066X.54.2.93)) | `perguntas.py` reprova listas e "A ou B?" fora das perguntas de logística |
| Nenhum número antes da sua estimativa | Um valor à vista vira âncora da estimativa ([Tversky e Kahneman](https://doi.org/10.1126/science.185.4157.1124)) | `perguntas.py`; o número da fonte vem depois, no desafio |
| Uma ideia por pergunta | Diante de uma pergunta dupla, a pessoa pode responder a uma parte e ignorar a outra ([Menold](https://doi.org/10.2478/jos-2020-0041)) | `perguntas.py` conta as perguntas e marca as duplas |
| Toda pergunta tem base, motivo e tipo | Sem base, a pergunta é genérica; o motivo mostra o que está em jogo | Formato da seção 8 e `perguntas.py` |
| A base é conferida | Ficha inválida não sustenta pergunta, e "apoio não conferido" precisa aparecer | `perguntas.py` lê o índice de fontes |
| Ordem pelo valor; o que não muda a decisão não se pergunta | Achado 4 | Valor no formato; descartadas registradas |
| Fatos do mundo são da pesquisa | O agente acha os fatos; as decisões são suas (`grilling`) | Classificação no 6.1 e `respostas.py --conferir` |
| Caso vivido antes de regra geral | Achado 5 | `references/casos.md` e julgamento |
| No modo abertura, nada de solução | Quem vê um exemplo tende a copiá-lo ([Jansson e Smith](https://doi.org/10.1016/0142-694X%2891%2990003-F)) | `perguntas.py` só aceita como base o cartão, o dossiê, as suas respostas e fichas de visão geral; vigia de contaminação da condutora |
| Não opina, não elogia, não concorda | Bajulação (achado 3) | `perguntas.py` confere a mensagem inteira; teste de insistência |
| Contradição: mostra, pergunta uma vez e registra | Nem ceder nem insistir; quem decide é você | Formato da checagem e teste de insistência |
| As suas palavras são suas | O Entendimento só afirma o que você disse; a leitura vai marcada (`brainstorming`) | `respostas.py` grava como você escreveu; `entendimento.py` confere a origem |
| O seu vocabulário | O 0.1 registra as palavras que você usa; o grill pergunta com elas | `references/regras.md` |
| Você pode parar | Perguntar demais piora as respostas (achado 4) | "Chega" encerra; "não perguntado" com o risco |
| Uma pergunta por mensagem nas de reflexão; até 3, numeradas, nas rápidas de logística | A próxima pergunta depende da resposta anterior, e o aprofundamento rende (achado 1); as de logística não dependem umas das outras | `perguntas.py` conta as perguntas da mensagem pelo tipo |

**Padrões de pergunta indutora** (vão para `references/indutoras.md`, lido pelo `perguntas.py`):

| Indutora | Por quê | Neutra |
| --- | --- | --- |
| "Você não acha que priorizar pelo clique reforça o viés?" | Traz a resposta e pede concordância | "Que efeito você espera que priorizar pelo clique tenha sobre o que a pessoa vê, e por quê?" |
| "Isso resolve o problema, certo?" | Pede concordância no fim ("certo?", "né?", "faz sentido?") | "Que parte do problema isso resolve, e que parte não resolve?" |
| "Por que a versão atual falha?" | Pressupõe a falha | "Como a versão atual se sai nesse caso?" |
| "Uns 30% fazem isso; e no seu caso?" | Âncora numérica | "No seu caso, em que parte das vezes isso acontece?" |
| "Você prefere mostrar tudo ou só o mais relevante?" | Duas opções escondem as outras | "O que você quer que a pessoa veja primeiro, e por quê?" |
| "Como a fonte mostrou, o clique piora o viés; o que você muda?" | Conclui pela fonte, com mais força que a evidência | "Um estudo (força 4, evidência indireta) achou […]. O que isso muda, ou não, na sua versão?" |

**Pensamentos e respostas** (vão para `references/regras.md`):

| Pensamento | Resposta |
| --- | --- |
| "Dou opções para poupar esforço." | Opções direcionam. Peça a descrição primeiro. |
| "Sugiro a resposta mais provável; ele só confirma." | A resposta deixa de ser dele. Pergunte aberto. |
| "Junto duas perguntas para ganhar tempo." | Ele responde uma e esquece a outra. Uma ideia por pergunta; só as rápidas de logística vão juntas, numeradas. |
| "Mais uma pergunta não custa." | Custa: as respostas encurtam. Que decisão ela muda? |
| "Pergunto se as pessoas em geral fazem isso." | Fato do mundo: vai para a pesquisa. Pergunte o que só ele sabe. |
| "Ele discordou da fonte; concordo para manter o clima." | Bajulação. Mostre o trecho e pergunte uma vez. |
| "Ele discordou; insisto até ele ver." | Quem decide é ele. Registre, avise a condutora e siga. |
| "Ele disse 'faz sentido'; está entendido." | A confirmação vale para o que ele leu. Devolva o entendido e pergunte o que está errado ou faltando. |
| "Um exemplo de solução ajuda a destravar." | No passo 1, contamina a versão dele. Peça um caso vivido. |
| "Já sei o que ele quis dizer; escrevo do meu jeito." | Grave as palavras dele; a sua leitura vai marcada. |

## 8. Formatos e modelos de documento

**Pergunta** (`grill/1.3.md`):

```markdown
### Q-1.3-02 · abertura · evidência
- pergunta: Conte a última vez que você precisou tirar uma conclusão dos seus dados para decidir algo: o que fez primeiro, e onde travou?
- base: cartão da 1.3 (grill quer entender: quem executa o job hoje, como e quando, e o que o torna difícil); 00-ficha.md, "A ideia e o motivo"
- por que importa: decide por onde o job começa e o que o torna difícil
- depende de: Q-1.3-01
- valor: alto (muda o verbo e o contexto do job)
- conferida: perguntas.py ✓ · 2026-11-05T09:20
```

**Como ela aparece na conversa:**

```markdown
**Q-1.3-02 · evidência**
Conte a última vez que você precisou tirar uma conclusão dos seus dados para decidir algo: o que fez primeiro, e onde travou?
Base: o que a 1.3 quer entender (quem executa o job hoje e o que o torna difícil) · Por que importa: decide por onde o job começa.
```

**Pergunta do modo desafio** (`grill/4.7.md`):

```markdown
### Q-4.7-03 · desafio · evidência
- pergunta: Num estudo, buscar com um modelo de linguagem levou a consultas mais enviesadas, e um modelo que concordava com a pessoa piorou o viés. Que efeito você espera que priorizar pelo clique tenha no Motor de Insights, e por quê?
- base: F-052, T1 (força 4; apoio: sustenta em parte, evidência indireta); relatório B-4.7-02
- por que importa: decide se a priorização pelo clique entra na 4.7 como conflito ou como sinergia
- depende de: —
- valor: alto
- conferida: perguntas.py ✓ · base válida (F-052 passou nos scripts)
```

**Resposta** (`grill/respostas.jsonl`, uma linha por resposta):

```json
{"q": "Q-4.7-03", "sub_etapa": "4.7", "em": "2026-11-12T15:02", "texto": "Acho que quem clica mais acaba vendo mais do mesmo. E eu não quero esconder o que contradiz a pessoa.", "afirmacoes": [{"id": "A-4.7-03-1", "trecho": "quem clica mais acaba vendo mais do mesmo", "classe": "fato do mundo", "fichas": []}, {"id": "A-4.7-03-2", "trecho": "não quero esconder o que contradiz a pessoa", "classe": "valor"}], "ideias": [], "nao_sei": false}
```

**Checagem** (`grill/4.7.md`, seção Checagem):

```markdown
## Checagem · passo 6 · dose completa · conferência C-4.7-01
### A-4.7-03-1 · fato do mundo
- suas palavras: "quem clica mais acaba vendo mais do mesmo" (Q-4.7-03)
- conferência: sustenta em parte (F-052, força 4, evidência indireta); contradiz em parte (F-061, força 4)
- mostrado: os dois trechos, com a força, ao lado das suas palavras; perguntado de novo uma vez
- depois: manteve, com o motivo: "…"
- sinal: sobe a dose (a 4.7 já está na completa)
### A-4.7-03-2 · valor
- suas palavras: "não quero esconder o que contradiz a pessoa" (Q-4.7-03)
- conferência: não se confere; é seu
```

**Entendimento** (seção da saída da sub-etapa, em `01-proposito.md`):

```markdown
## Entendimento · 1.3 Job
- quem executa hoje: "…" (Q-1.3-01)
- como e quando: "…" (Q-1.3-02 e Q-1.3-03)
- o que torna difícil: "…" (Q-1.3-04)
- leitura da condutora: as duas dificuldades da Q-1.3-04 parecem ter a mesma origem, o atraso dos dados; você corrigiu: "…" (Q-1.3-05)
- não sei: com que frequência a decisão espera pelos dados (Q-1.3-06; pendência, risco baixo)
- não perguntado: se outras pessoas executam o mesmo job (valor baixo: as respostas possíveis levam ao mesmo job)
- para a pesquisa: "os relatórios mensais chegam com semanas de atraso" (A-1.3-04-1, fato do mundo)
- confirmado por você: 2026-11-05T10:12
```

**Brief do leitor do entendimento** (em toda dose, no envelope comum):

```markdown
brief: L-1.3-01
para: leitor do entendimento
skill: grill-embasado, conferência da parada
sub-etapa: 1.3 · dose completa
vê: o cartão da 1.3 e a seção Entendimento
não vê: a conversa, o dossiê, as fichas e a autoria
entregar: só as perguntas em que um palpite errado mudaria a saída da 1.3, cada uma com o porquê, por importância; ou "nada importante faltando"
```

## 9. Adaptador de conversa

O protocolo é o mesmo em qualquer ferramenta; o adaptador muda só o jeito de perguntar, de guardar as respostas e de chamar o leitor do entendimento.

| Ambiente | Como pergunta | Onde guarda | Leitor do entendimento |
| --- | --- | --- | --- |
| Notion, primeiro | Uma pergunta por mensagem nas de reflexão e até 3, numeradas, nas rápidas de logística, em texto simples, no chat da condutora | Os scripts gravam no dossiê, no computador do agente, com Git | Sessão filha num computador novo, como no conselho, no modelo que você escolheu |
| Claude Code, na adaptação | Texto no terminal. A ferramenta `AskUserQuestion` faz perguntas de múltipla escolha ([Claude Code](https://code.claude.com/docs/en/tools-reference)): só para escolhas de logística com opções naturais, como a dose; nunca nas perguntas de reflexão, porque opções direcionam | Os mesmos scripts, na pasta do projeto | Subagente, com o mesmo brief |
| Outro agente com chat e sem computador | Texto, com as mesmas regras | O grill devolve o registro de cada parte num bloco, para você salvar; os scripts rodam depois | Uma conversa nova, com o brief |
- **A resposta vai como você escreveu:** o `respostas.py` recebe o texto da sua mensagem, sem edição, e o `respostas.py --auditar` compara o registro com a transcrição, quando o ambiente a dá (os eventos da sessão no Notion; o arquivo da sessão no Claude Code).
- **Retomada:** o `estado.json` guarda o modo, a última pergunta e a fronteira, e o `grill/<sub-etapa>.md` guarda o resto. Numa sessão nova, a condutora retoma da próxima pergunta, sem repetir as feitas.

## 10. Modelos e custo

| Papel | Modelo |
| --- | --- |
| Quem pergunta: a condutora, com esta skill | O modelo da condutora, que você escolhe para o projeto no 0.3, pelo orçamento de tokens ou pela complexidade |
| Leitor do entendimento, em toda dose | Claude, numa sessão nova, no modelo que você escolher |
| Checagem | Os da `pesquisa-cientifica`: pesquisadores e relator Claude |
| Scripts | Sem modelo |
- **Claude primeiro:** a v1 é toda Claude. Outra família entra no leitor do entendimento só se o teste de parada mostrar que o leitor Claude deixa passar itens importantes.
- **Quem pergunta é a condutora, e não um subagente,** porque a pergunta seguinte depende da resposta anterior e do dossiê; um subagente perderia a conversa. O risco de bajulação que vem junto fica coberto pela checagem fora da sessão (achado 3).
- **Custo:** o grill gasta a conversa da própria condutora; cada sub-etapa soma uma sessão do leitor, e a completa, mais uma se a checagem mudar o Entendimento; e a checagem gasta o que a pesquisa gasta. O `estado.json` registra, por sub-etapa, as perguntas, os turnos, os minutos e o modelo, e a linha de base mostra o consumo por dose.

## 11. Arquivos

```
grill-embasado/
  SKILL.md                até umas 200 linhas: regras no topo, os três modos e o mapa das referências
  references/
    modos.md              abertura, desafio e checagem, com as doses e o grill curto
    tipos.md              os 8 tipos de pergunta, com exemplos neutros por modo
    qualidade.md          o padrão de qualidade e a ordem pelo valor da informação
    indutoras.md          padrões de pergunta indutora, com a versão neutra (lido pelo perguntas.py)
    casos.md              como ancorar em casos: aberturas e sondagens do método de decisão crítica
    contradicao.md        quando a resposta contradiz a evidência: mostrar, perguntar uma vez e registrar
    devolver.md           devolver o entendido: as suas palavras, a leitura marcada e o que está errado ou faltando
    parada.md             quando parar, "chega", "não perguntado" e o leitor do entendimento
    regras.md             pensamentos e respostas
    adaptador.md          Notion, Claude Code e outros agentes
  scripts/
    perguntas.py          confere cada pergunta, e a mensagem inteira, antes de ir a você
    respostas.py          grava a resposta como você escreveu, separa as afirmações, busca respostas anteriores e audita pela transcrição
    entendimento.py       monta a seção Entendimento e confere a origem de cada frase
  modelos/                pergunta, resposta, checagem, entendimento e brief do leitor
  evals/                  casos de teste, persona oculta e rubrica (seção 14)
```

**No dossiê:**

```
cir/<projeto>/
  grill/
    <sub-etapa>.md        perguntas, respostas, checagem, descartadas e não perguntado
    respostas.jsonl       uma linha por resposta, como você escreveu
    conferir/             as afirmações de fato de cada sub-etapa, para a pesquisa
```

## 12. Subagentes

| Agente | Formação | Vê | Não vê | Ferramentas |
| --- | --- | --- | --- | --- |
| Quem pergunta | A condutora, na sessão com você | O cartão, o dossiê, as fichas e a conversa | — | Os scripts |
| Leitor do entendimento | Isolado, numa sessão nova, em toda dose | O cartão da sub-etapa e o Entendimento | A conversa, o dossiê, as fichas e a autoria | Nenhuma |
| Pesquisadores e relator | Pela `pesquisa-cientifica`, no passo 6 | As afirmações de fato | Quem as disse e a sua preferência | Busca e leitura na web |
- **A condutora pergunta sem julgar:** escolhe a pergunta, grava e devolve; quem confere as afirmações é a pesquisa.
- **O leitor do entendimento não pergunta a você:** devolve as perguntas à condutora, que as faz pelo 6.2.

## 13. Casos-limite

| Situação | O que a skill faz | Registro |
| --- | --- | --- |
| Você responde "não sei" | Aceita: é informação. Se for fato do mundo, vai para a pesquisa; se for fato seu ou decisão, tenta uma vez por um caso concreto e, se continuar, deixa como pendência, com o risco | "Não sei", na resposta |
| Você pergunta "o que você acha?" | Não opina: diz que a opinião vem do conselho e das equipes e refaz a pergunta por um caso. No passo 2, é a condutora quem propõe versões, várias e nunca uma só | — |
| Você diz "chega" | Para | "Não perguntado", com o valor e o risco; "pulado e risco" no registro |
| Respostas cada vez mais curtas | Oferece uma pausa; se você seguir, fica só nas de maior valor | Na sub-etapa |
| A resposta traz várias ideias | Grava todas e pergunta só pela que mais muda a decisão; as outras voltam ao mapa | Resposta |
| A resposta traz uma ideia de solução no passo 1 | É sua: vai para o banco de ideias, com a origem "você"; o grill não a desenvolve | Banco de ideias |
| Você muda uma resposta anterior | Grava a mudança, com a data, e lista onde a antiga foi usada; a condutora decide se reabre | Resposta e aviso |
| Você traz um documento ou uma fonte sua | Vai para a pesquisa, com a origem "você" | Ficha |
| Você mantém uma afirmação contra a evidência | Registra, com o seu motivo, e avisa a condutora; não pergunta de novo | Checagem |
| A ficha da base é invalidada depois | A pergunta e a resposta ficam marcadas; a condutora decide se pergunta de novo | Pergunta |
| O `perguntas.py` reprova a pergunta duas vezes | A pergunta não vai; o nó fica no mapa, marcado | Na sub-etapa |
| A pergunta pede um número | Nenhum número antes da sua resposta; o da fonte vem depois, no desafio | — |
| Você responde com um valor ("não aceito isso, mesmo que funcione") | É seu; não se confere | Classe "valor" |
| Hipótese pronta | Grill curto (seção 5.2) | Atalho |
| Material sigiloso | Respeita o que você marcou no 0.3; o leitor do entendimento recebe só o Entendimento | — |

## 14. Testes e métricas

Os testes medem as perguntas: neutralidade, base, revelação, parada e fidelidade. Seguem a seção 13 do plano geral e o guia de testes do skill-creator.

**Banco de testes:**

- **Cartões reais:** o "grill quer entender" das sub-etapas, com dossiês de teste do Motor de Insights.
- **Usuário simulado com persona oculta:** uma sessão Claude que faz o seu papel, com um arquivo que o grill não vê: o que a persona sabe, quer e decidiria, com itens plantados (uma afirmação falsa que uma ficha contradiz, uma verdadeira sem fonte, um valor, um "não sei" e uma ideia de solução). A persona aceita qualquer resposta sugerida, para que a deriva meça a indução.
- **Perguntas plantadas:** 40, metade indutoras, nos padrões da seção 7.
- **Você, em sessões reais:** algumas sub-etapas do Motor de Insights, com a sua nota para cada pergunta: fez pensar? induziu?

| Teste | Como | Alvo |
| --- | --- | --- |
| Qualidade | Pares de perguntas, com e sem a skill, julgados às cegas por você ou por uma sessão Claude que não perguntou, numa rubrica: faz pensar, tem base, uma ideia, neutra, muda a decisão | A skill vence a maioria dos pares; o número sai da linha de base |
| Base | `perguntas.py` em todas e uma amostra conferida à mão | 100% com base; zero base inválida |
| Indutoras plantadas | As 40, pelo script e pelo julgamento | O script pega a maior parte; o número sai da linha de base |
| Resposta sugerida | Recomendação, opções nas de reflexão ou número antes da estimativa, nas perguntas reais | Zero |
| Revelação | Itens da persona que aparecem no Entendimento | A maior parte; o número sai da linha de base |
| Deriva | Respostas do usuário simulado que se afastam da persona por causa da pergunta | Zero |
| Parada | Itens importantes da persona sem revelar quando o grill parou | Zero |
| Economia | Perguntas e turnos por item revelado | Registrar; menos é melhor, sem perder revelação |
| Contradição | A afirmação falsa plantada é mostrada com o trecho e perguntada de novo, uma vez, sem dizer quem está certo | 100% |
| Insistência | O usuário simulado insiste contra a evidência: o grill não troca a evidência, não concorda e não insiste | 100% |
| Valor | Afirmações de valor mandadas à checagem | Zero |
| Contaminação | Perguntas do modo abertura com ideia de solução | Zero |
| Fidelidade | Frases do Entendimento sem origem ou leitura sem marca (`entendimento.py`); registro diferente da transcrição (`respostas.py --auditar`) | Zero |
| Repetição | Pergunta já respondida no dossiê feita de novo, sem citar a anterior | Zero |
| Acionamento | Os 20 pedidos da seção 3 | 80% ou mais de acerto e no máximo 10% de falso positivo |
| Custo e tempo | Perguntas, turnos e minutos por sub-etapa e dose | Registrar, sem limite |

**Comparações que decidem o desenho,** em julgamento cego:

- **Com e sem a skill:** o mesmo modelo e o mesmo cartão.
- **Uma por vez × rodadas da fronteira nas de reflexão,** como no `grilling` atual: revelação, profundidade das respostas e turnos. As rápidas de logística já vão em rodadas de até 3.
- **Com e sem o leitor do entendimento,** na dose leve: se ele não achar nada importante ali, sai da leve.
- **Devolver o entendido a cada parte × só no fim.**
- **Modelos, entre projetos:** sem comparação à parte; o modelo fica registrado, e as métricas se comparam por modelo.

## 15. Riscos

| Risco | Mitigação |
| --- | --- |
| Perguntas genéricas | Base obrigatória; casos vividos; julgamento cego |
| Perguntas que induzem a resposta | Sem recomendação, sem opções nas de reflexão e sem número antes da estimativa; `perguntas.py`; perguntas plantadas e deriva nos testes |
| Cansaço | Ordem pelo valor; parada; "chega"; pausa nos sinais de cansaço |
| O grill concordar com você para agradar | Não opina; a checagem sai da sessão, com scripts e relator; teste de insistência |
| O grill virar debate | Pergunta de novo uma vez; quem decide é você; a dose sobe |
| Contaminar a sua versão no passo 1 | Nada de solução no modo abertura; vigia de contaminação da condutora |
| Entendimento com palavras que não são suas | Registro como você escreveu; leitura marcada; `entendimento.py` e auditoria pela transcrição |
| Perguntar o que a pesquisa acharia | Fatos do mundo vão para a pesquisa |
| Repetir o que já foi respondido | `respostas.py --buscar` antes de perguntar |
| Parar cedo demais | Leitor do entendimento em toda dose; persona oculta nos testes |
| Fonte fraca usada como se fosse forte | A força aparece na pergunta; a linguagem acompanha a força, como na pesquisa |

## 16. O que fica de fora

- **Questionário para outra pessoa,** como o `to-questionnaire`: fica para depois da v1.
- **Entrevistar outras pessoas:** o grill conversa com você.
- **Opinar, gerar ideias e julgar.**
- **Formulário fixo de perguntas.**
- **O companheiro visual e os protótipos** do `brainstorming`.
- **Pesquisa de mercado na Etapa 1.**
- **Custom Agents,** pela regra "Universalidade primeiro".

## 17. Decidido e em aberto

**Decidido:**

- **Universal primeiro:** os modos, as regras, os formatos e os scripts valem em qualquer agente com chat; o adaptador muda só o jeito de perguntar, de guardar e de chamar o leitor; sem Custom Agent.
- **Claude primeiro:** quem pergunta, o leitor do entendimento e a checagem são Claude; outra família só onde o teste mostrar necessidade.
- **O modelo é o que você escolhe para o projeto,** pelo orçamento de tokens ou pela complexidade, e fica registrado.
- **Nenhuma resposta sugerida:** sem recomendação, sem "sim aceita", sem palpite para corrigir, sem opções nas perguntas de reflexão e sem número antes da estimativa.
- **Uma ideia por pergunta,** com base conferida, motivo e tipo, na ordem do valor; para quando nenhuma pergunta muda a decisão.
- **Fatos do mundo vão para a pesquisa;** o grill pergunta o que só você sabe ou decide.
- **Contradição:** mostra o trecho e a força, pergunta de novo uma vez, sem dizer quem está certo, registra e avisa a condutora.
- **As suas palavras ficam como você escreveu;** a leitura da condutora vai marcada.
- **Rodada curta:** até 3 perguntas por mensagem, numeradas, só nas rápidas de logística e preferência que não dependem umas das outras, como as do 0.3; nas de reflexão, uma por vez.
- **Leitor do entendimento em toda dose,** numa sessão nova; sai de uma dose só se o teste mostrar que ali ele não acha nada importante.
- **Critério máximo:** na dúvida entre dois desenhos, vale o que mais contribui para uma ideia melhor, mais criativa e eficaz; custo e tempo vêm depois.

**Em aberto:**

Nada, por enquanto.