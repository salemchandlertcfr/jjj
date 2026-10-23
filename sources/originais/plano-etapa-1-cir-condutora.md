# Plano detalhado — etapa-1-cir (condutora)

<aside>
🧭

**O que é:** o plano detalhado da `etapa-1-cir`, a skill condutora da Etapa 1. É ela que você chama: conduz os temas e as sub-etapas do [Fluxograma completo — Etapa 1 (método IDEAL em ciclo)](../Fluxograma%20completo%20%E2%80%94%20Etapa%201%20(m%C3%A9todo%20IDEAL%20em%20cic%20f1f71e3bd5e6487ebdfc94cd7e9fa161.md), aplica o ciclo na dose certa, chama as outras skills pelo nome, segura as travas e mantém o dossiê. É o primeiro plano da ordem da seção 15 do [Plano geral das skills — Etapa 1 (CIR)](../Plano%20geral%20das%20skills%20%E2%80%94%20Etapa%201%20(CIR)%2072d0fdc1db19433e9101d1ac3b3015ef.md), porque define o dossiê, os formatos e os contratos que as outras skills seguem.

**Universal:** o conteúdo é um só, no formato aberto de skills. Começa no Notion e depois se adapta ao Claude Code e a outras ferramentas; muda só a camada que chama os agentes e os modelos (seção 14).

</aside>

## 1. Propósito no fluxograma

**Propósito:** levar a Etapa 1 da ideia ao CIR aprovado, garantindo que cada tema e sub-etapa passe pelo ciclo na dose certa, com as travas, o dossiê e as regras que valem o tempo todo.

| Responde por | Como se vê |
| --- | --- |
| Aderência ao fluxo | Nenhuma sub-etapa pulada sem registro e nenhum passo do ciclo fora de ordem, como mostrar ideias da IA antes da sua versão |
| Travas | Os temas 1, 3, 5 e 6 só avançam com a sua aprovação explícita, registrada |
| Independência | Nenhum agente vê o que não deve: os geradores não veem a sua versão, o conselho não vê a autoria e ninguém vê os casos reservados antes do tema 5 |
| Dossiê íntegro | Toda saída, fonte e decisão fica gravada, com commit, e dá para retomar de qualquer ponto em outra sessão |
| Etapa 1 limpa | Nada de Etapa 2 ou 3 no CIR, fora das fronteiras técnicas e do estacionamento |
| Você no centro | Perguntas e decisões chegam uma de cada vez, com o porquê, e nada é decidido no seu lugar |
- **Não responde pela** qualidade das ideias (skills de método, equipes e geradores), das fontes (`pesquisa-cientifica`) e dos julgamentos (`conselho-especialistas`). Garante que cada uma faça a sua parte, na ordem, vendo só o que pode ver.
- **Não opina.** Não diz qual alternativa prefere, não "melhora" a sua versão e não resume um debate puxando para um lado. Quando você pergunta "o que você acha?", ela mostra o que as fontes e o conselho disseram, ou chama um conselho sob demanda.
- **Pronto quando:** o CIR é aprovado no 6.6, o critério de pronto passa sem pendência aberta e cada decisão tem registro no dossiê.

## 2. Skills de base e o que se aproveita

Nenhuma skill pronta conduz um método com ciclo, travas e dossiê; o que existe são peças. Vale a regra da seção 8 do plano geral: copiar o trecho útil, com versão fixa, licença e atribuição, e decidir por teste cego.

| Base | O que se aproveita | O que é nosso | Licença |
| --- | --- | --- | --- |
| [planning-with-files](https://github.com/OthmanAdi/planning-with-files) (OthmanAdi) | Estado em arquivo, fora da janela de contexto; estado reinjetado a cada turno; recuperação depois de compactação ou sessão nova; trava que só deixa encerrar quando o estado diz que terminou; versões para dezenas de agentes. E as lições do histórico de versões: hooks rápidos, num processo só; texto para o modelo pelo campo de contexto, e não pela mensagem que vai para você; proteção contra duas sessões gravando o mesmo estado | O estado é do método (tema, sub-etapa, passo do ciclo, dose, travas, pendências e mapa de modelos), e não uma lista de tarefas; o dossiê é entrega, com Git, e não rascunho | MIT |
| [subagent-driven-development e verification-before-completion](https://github.com/obra/superpowers) (superpowers) | Um agente novo por tarefa, que não herda a conversa e recebe só o que precisa; revisão a cada tarefa; "evidência antes de afirmar"; e a tabela de racionalizações, com a resposta para cada desculpa para pular uma regra | As três formações, o que cada agente pode ver e as travas | MIT |
| [doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring) (Anthropic) | Condução em estágios, com perguntas antes de escrever, e o teste com um leitor sem contexto | O ciclo de 10 passos e o registro de decisões | A conferir: a pasta não tem LICENSE |
| [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) (Anthropic) | Estrutura, divulgação progressiva, evals e ajuste da descrição | — | Apache 2.0 |

Três achados de pesquisa moldam o desenho:

- **Estado explícito vence histórico longo.** Trocar a conversa que só cresce por um estado de execução explícito melhorou a acurácia e reduziu o consumo de tokens em tarefas longas ([SKILL.state](https://arxiv.org/abs/2608.26263)). Anotações gravadas fora da janela e relidas quando preciso são também a recomendação da Anthropic para tarefas longas ([Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). Por isso, quem diz onde o projeto está é o `estado.json`, e não a memória da conversa.
- **Skill curta e poucas skills por vez.** Skills compactas renderam mais que as exaustivas, e tarefas com 4 ou mais skills ganharam cerca de metade do que ganharam as com 2 ou 3 ([SkillsBench](https://arxiv.org/abs/2602.12670)). Mesmo os melhores modelos cumprem só 68% de 500 instruções simultâneas e favorecem as primeiras ([IFScale](https://arxiv.org/abs/2507.11538)). Por isso, o `SKILL.md` é curto, com as regras invariantes no topo, e o resto fica em referências lidas na hora do passo.
- **Skill chamada pelo nome.** Num teste da Vercel, a skill não foi acionada em 56% dos casos e não melhorou nada sobre a linha de base; só com instrução explícita para usá-la passou a ajudar ([Vercel](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)). Por isso, a condutora chama cada skill pelo nome, no passo certo, e o projeto tem um índice curto sempre carregado (seção 10).

## 3. Acionamento

```yaml
---
name: etapa-1-cir
description: >-
  Conduz a Etapa 1 de um projeto, a Concepção Ideal da Solução pelo método
  IDEAL, da ideia ao CIR aprovado: propósito, mapa, hipótese de idealidade,
  como, prova conceitual e CIR. Cada sub-etapa passa pelo ciclo de grill, sua
  versão, triagem, pesquisa, alternativas, validação e decisão, com travas e
  dossiê em Git. Use quando o usuário quiser começar, retomar ou auditar a
  Etapa 1 ou o CIR de uma ideia, rodar uma sub-etapa do método IDEAL, congelar
  um propósito ou consultar o conselho sobre o dossiê; ou quando falar em
  "concepção ideal", "CIR", "método IDEAL" ou "Etapa 1". Não use para preço,
  plano de negócio, MVP, escolha de tecnologia, roadmap ou protótipo, que são
  das Etapas 2 e 3, nem para brainstorm avulso sem dossiê.
license: (a definir)
compatibility: Claude Code ou Notion; Python 3 e Git no computador do agente
metadata:
  versao: "0.1"
  fluxograma: "Fluxograma completo, versão com equipes"
---
```

- **Só os campos do padrão aberto** (`name`, `description`, `license`, `compatibility`, `metadata` e `allowed-tools`), para a mesma skill carregar no Claude Code, no Notion e em outros agentes. No envio ao [claude.ai](http://claude.ai) e no empacotamento oficial, um campo fora do padrão dá erro ([Claude Code: skills](https://code.claude.com/docs/en/skills)). Hooks e subagentes ficam no plugin (seção 10).
- **Chamada pelo nome é o caminho principal:** `/etapa-1-cir` no Claude Code e "use a skill etapa-1-cir" no Notion. A descrição serve para os pedidos em que você não diz o nome.

| Deve acionar | Não deve acionar (quase acertos) |
| --- | --- |
| "Quero começar a Etapa 1 do Motor de Insights." | "Quanto devo cobrar pelo Motor de Insights?" |
| "Vamos continuar o CIR do projeto da água." | "Qual stack usar no MVP?" |
| "Retoma o dossiê do reencontro de onde paramos." | "Me dá 20 nomes para o app." |
| "Audita este PRD pela Etapa 1." | "Monta o roadmap do trimestre." |
| "Pede ao conselho para olhar o propósito congelado." | "Resume esta reunião." |
| "Roda só o pré-mortem do ideal do Motor." | "Faz um brainstorm rápido de features." |

A lista completa, com 10 de cada lado, entra nos testes (seção 13).

## 4. Contrato de entrada e saída

| Entrada | Forma | O que a condutora faz |
| --- | --- | --- |
| Projeto novo | Ideia, propósito ou solução pronta, em texto livre; documentos e links, se houver | Cria o dossiê e abre o tema 0 |
| Retomada | Nome ou caminho do projeto | Lê o estado e o último registro, mostra onde parou e propõe o próximo passo |
| Auditoria | Um documento pronto: PRD, pitch ou CIR | Tema 0 no modo auditoria (seção 5) |
| Sub-etapa avulsa | "Só a 2.6", "só o pré-mortem" | Confere os pré-requisitos no dossiê e avisa o que falta |
| Hipótese pronta | "Já sei o que quero: …" | Atalho: grill curto e ciclo a partir da triagem |
| Conselho sob demanda | "Pede ao conselho…" | Escolhe o template e chama o `conselho-especialistas` |

| Saída | Para quem | Onde |
| --- | --- | --- |
| Perguntas, opções e pedidos de decisão | Você | Na conversa, uma coisa de cada vez |
| Saídas das sub-etapas e CIR em construção | Dossiê | Arquivos de cada tema e `06-cir.md` |
| Registros de decisão | Dossiê | `decisoes.md`, com commit |
| Briefs e pautas | Outras skills | `briefs/`, `equipe/` e `conselho/` |

**Contratos com as outras skills.** Só a condutora lê o dossiê; cada skill recebe o que precisa no brief e devolve no formato combinado.

| Skill | Quando | A condutora envia | Recebe | Grava em |
| --- | --- | --- | --- | --- |
| Skill de método do tema (`cir-*`) | Do começo ao fim do tema | — (é carregada pelo nome) | O cartão de cada sub-etapa (seção 9) | — |
| `grill-embasado` | Passos 1, 5 e 6, e abertura do tema | O objetivo do cartão, o que o dossiê já sabe e, no modo desafio, as fichas de fonte | Perguntas, uma por vez nas de reflexão e até 3 juntas nas rápidas de logística, e a checagem das respostas | Seção "Entendimento" da saída |
| `pesquisa-cientifica` | Passos 4 e 6, e o 8 pelos membros do conselho | Brief de pesquisa | Fichas de fonte | `fontes/` |
| `especialistas` | Passo 7, verificação e 2.7 | O que a sub-etapa pede e o que a biblioteca tem | Fichas dos especialistas e dos geradores | `especialistas.md` |
| `equipe-especialistas` | Passo 7, verificação e integração do tema | Pauta | Ata, síntese e parecer técnico | `equipe/` |
| `conselho-especialistas` | Passos 3 e 8, validação integrada e sob demanda | Brief do conselho | Vereditos, síntese e placar | `conselho/` |

O anonimizador e o sorteio da ordem são scripts do `conselho-especialistas`, mas rodam pela condutora, que guarda a chave de autoria fora dos briefs.

## 5. Modos de uso

| Modo | Quando | O que muda |
| --- | --- | --- |
| Completo | Projeto novo; é o padrão | Temas 0 a 6, em quantas sessões forem precisas |
| Retomar | Já existe dossiê | Mostra onde parou, em cinco linhas, e propõe o próximo passo |
| Sub-etapa avulsa | Você quer só uma parte | Confere os pré-requisitos; o que faltar é feito antes ou vira pendência, à sua escolha |
| Auditoria | Já existe um documento | O documento entra como material do tema 0: separação por etapa (0.2), sinais de contaminação e lacunas do critério de pronto, num relatório. Depois, você decide se segue pelo tema 1 |
| Atalho com hipótese pronta | Você já tem a hipótese | Grill curto e ciclo a partir da triagem; as alternativas continuam, porque sem elas não há com o que comparar |
| Conselho sob demanda | A qualquer momento | Pausa o passo, chama o conselho e volta ao mesmo ponto |

O modo expresso do primeiro plano fica de fora (seção 16).

## 6. Passos

### 6.1 Ao ser chamada

1. **Achar o projeto.** Se há dossiê, a condutora roda o resumo do estado; se não há, confirma o nome do projeto e cria o dossiê, com o Git, o estado inicial, os modelos de documento e o índice do projeto.
2. **Mostrar onde está,** em cinco linhas: tema, sub-etapa, passo do ciclo, última decisão e pendências, com o próximo passo proposto. Se alguém mexeu no dossiê fora da condutora, ela mostra a diferença e pergunta se é uma decisão (vira registro) ou uma correção.
3. **Carregar só o que o passo pede:** a skill de método do tema, pelo nome, o cartão da sub-etapa e a referência do passo. O resto do dossiê fica no disco até ser preciso.

### 6.2 Tema 0, conduzido pela própria condutora

O tema 0 não tem skill de método; o roteiro fica em `references/tema-0.md`.

| Sub-etapa | O que a condutora faz | Formação | Sai |
| --- | --- | --- | --- |
| 0.1 Ficha do projeto · padrão | Grill sobre a ideia e o motivo, o seu vocabulário, o que você não aceitaria e o que faria a etapa valer a pena; uma pesquisa de visão geral, para não perguntar o óbvio; a ficha nas suas palavras, sem interpretação | 1 pesquisador e o crítico, isolados. **Refuta se:** você não reconhece a sua ideia ou falta algo que você disse | `00-ficha.md`, confirmada por você |
| 0.2 Separação por etapa · padrão | Só quando há material. Cada trecho é classificado como Etapa 1, 2 ou 3, ou como ideia de solução; as divergências entre os classificadores vão para você | 2 classificadores cegos, um sem ver o outro, com óticas diferentes; conselho rápido (guardião e refutador) com os sinais de contaminação | `00-separacao.md`; o de Etapa 2 vai para as fronteiras, o de Etapa 3 para o estacionamento e as ideias para o banco, com a origem "material existente" |
| 0.3 Preparação · leve | Mapa de modelos: que modelo Claude faz cada papel, pelo orçamento de tokens ou pela complexidade; onde fica o dossiê; doses padrão; quanto de cada sessão você quer acompanhar; se algum material é sigiloso e onde não pode ir. São perguntas rápidas de logística: vão até 3 por mensagem | — | `estado.json` inicial e o mapa de modelos aprovado |

**Modo auditoria:** a 0.1 vira a ficha do documento, a 0.2 roda sobre ele inteiro e o critério de pronto do 6.5 é aplicado ao documento como está. Sai `00-auditoria.md`, com a separação, os sinais de contaminação e as lacunas.

### 6.3 Abertura de cada tema

1. **Carregar a skill de método pelo nome:** `cir-proposito` no tema 1, `cir-mapa` no 2, `cir-idealidade` no 3, `cir-divergencia` e depois `cir-arquitetura` no 4, `cir-prova` no 5 e `cir-sintese` no 6.
2. **Grill sobre o tema inteiro,** com o `grill-embasado` no modo abertura e o objetivo que a skill de método dá ao tema.
3. **Plano de dose.** A condutora propõe a dose de cada sub-etapa numa tabela, com o motivo, e você ajusta (seção 6.7).
4. **Equipe do tema.** A `especialistas` monta a equipe uma vez por tema, a partir do 2.7 quando ele já existe; as sub-etapas reaproveitam a equipe e trocam só quem a sub-etapa pede.

### 6.4 O ciclo de cada sub-etapa

| Passo | Skill e formação | O que a condutora faz | Grava |
| --- | --- | --- | --- |
| 1. Grill | `grill-embasado`, modo abertura; a própria condutora pergunta | Passa o objetivo do cartão; uma pergunta por vez nas de reflexão e até 3 juntas nas rápidas de logística; para quando não resta dúvida que mude a decisão | Seção "Entendimento" da saída |
| 2. Sua versão | Condutora | Pede a sua versão antes de mostrar qualquer ideia da IA. Se você não tiver, os geradores propõem várias, nunca uma. Marca a origem: sua, da IA ou sua depois de ver a IA | Saída da sub-etapa, com a origem |
| 3. Triagem | `conselho-especialistas`, conselho de triagem, isolados | Decide se a triagem roda (há algo que pode ser impossível em princípio ou ferir valores?). Aplica o resultado: o impossível vira limite máximo possível; o só difícil hoje vira fronteira técnica; nada é descartado | `conselho/` e `fronteiras.md` |
| 4. Pesquisa | `pesquisa-cientifica`, modo desenvolver; de 1 a 5 pesquisadores isolados | Monta os briefs a partir do foco do cartão; na dose completa, a busca a favor e a busca contra vão para pesquisadores diferentes | `fontes/` |
| 5. Perguntas | `grill-embasado`, modo desafio | Perguntas com fonte, "e se" e contraexemplos, sem sugerir resposta | Saída da sub-etapa |
| 6. Checagem | `grill-embasado` e `pesquisa-cientifica`, modo conferir | Confere cada afirmação sua contra as fontes; se uma contradiz a evidência, mostra a evidência e pergunta de novo | Saída e, se você mantiver, registro |
| 7. Elaboração e alternativas | `especialistas` e `equipe-especialistas`, com a skill de método; geradores cegos isolados | Monta a pauta, com a versão base sem autoria, e o brief dos geradores, sem a sua versão e sem o banco; na reunião orquestrada, passa a palavra e grava a ata | `equipe/`, `banco.md` e saída |
| 8. Validação | `equipe-especialistas`, modo verificação, quando o "refuta se" pede; `conselho-especialistas`, com a `pesquisa-cientifica` no modo refutar | Prepara H1, H2, H3… sem autoria e com o "refuta se" escrito antes; o sorteio da ordem é por membro | `conselho/` |
| 9. Decisão | Condutora | Mostra vereditos, dissenso e o que mudaria a decisão, sem preferência; você escolhe, combina ou pede outra rodada; ela pergunta o motivo e o objetivo da escolha e grava nas suas palavras (seção 6.6) | `estado.json` |
| 10. Registro | Condutora, com o script de registro | Registro no tamanho da dose; vigia de contaminação; seção do CIR preenchida; commit | `decisoes.md`, `06-cir.md` e Git |

**Ordem que não se quebra:** o passo 7 só abre com o passo 2 gravado, e o 9 só com o 8 gravado. O estado guarda o passo atual, e o script de brief se recusa a montar um brief de gerador antes de a sua versão estar registrada.

### 6.5 Fechamento do tema

1. **Integração em equipe,** com a `equipe-especialistas` no modo integração: as saídas combinam entre si?
2. **Validação integrada,** com o conselho completo às cegas, contra alternativas.
3. **Sua decisão.** Nos temas 1, 3, 5 e 6, é a trava (seção 6.6). Nos temas 2 e 4, você aprova ou segue com as pendências registradas.
4. **Registro completo:** CIR em construção, vigia, commit e estado avançado para o próximo tema.
5. **Voltas do fluxograma,** sempre com registro: do tema 3 ao 2 quando falta linha de base ou fonte; do 4 ao 3 quando um custo de uso vira métrica; do 5 ao 4 quando todos os conceitos são refutados ou dominados; no 5, mais casos e red team quando a comparação não fica clara; e a reabertura do propósito, só por decisão sua.

### 6.6 Travas e aprovação

- **O que conta como aprovação:** um "sim" seu a uma pergunta de sim ou não ("Você aprova o tema 1?"), depois de ver o resumo do tema, os vereditos e o dissenso. "Ok" a outra pergunta, silêncio ou mudança de assunto não contam.
- **Toda outra decisão traz o porquê.** Quando a resposta não é um "sim" a uma pergunta de sim ou não (um "não", uma escolha entre opções, uma combinação, um pedido para pular ou reabrir, uma discordância do conselho), a condutora pergunta o motivo e o objetivo: por que essa decisão e o que você quer alcançar com ela. É uma pergunta curta; se a resposta não deixar os dois claros, ela faz mais uma, no máximo. Grava as suas palavras no registro, sem julgar o motivo; se ele contradiz a evidência, vale a checagem do passo 6. O objetivo fica ao lado da decisão e é relido quando ela for reaberta.
- **Aprovar com ressalvas vale.** As ressalvas entram no registro e viram pendências.
- **O registro da aprovação** guarda a data, a versão aprovada (o commit) e as ressalvas.
- **Pedido para pular a trava:** a condutora diz o que se perde e oferece a validação mais curta possível. A decisão é sua: se você aprovar sem a validação, isso fica registrado como "aprovado sem validação integrada", com o risco. O que ela não faz é avançar sem uma aprovação sua.
- **Temas sem trava (2 e 4):** pular uma sub-etapa é possível; o registro guarda o que foi pulado e o risco, e o critério de pronto traz de volta o que for exigido. No tema 4, a classificação dos elementos (4.9) e a escolha das famílias (4.11) passam sempre pelo conselho.

### 6.7 Dose

- **Proposta:** para cada sub-etapa, a condutora responde às três perguntas do fluxograma (quanto a saída muda o CIR, quanta incerteza há e quão difícil é reverter) e parte da dose do título da sub-etapa.
- **Sobe ou desce sozinha, avisando:** sobe quando o conselho diverge num critério relevante, a triagem acha uma possível falha fatal, uma resposta sua contradiz a evidência ou a saída alimenta muitas sub-etapas; desce quando a saída é descritiva, já tem fonte e passou sem ressalvas. Você pode vetar.
- **Dose usada fica registrada,** ao lado da planejada, para os testes medirem o que cada dose custa e rende.

### 6.8 Como a condutora chama as outras skills

- **Pelo nome, no passo certo:** "Use a skill `pesquisa-cientifica`, modo desenvolver, com este brief."
- **No máximo três skills ativas por passo:** a condutora, a skill de método do tema e a skill do passo ([SkillsBench](https://arxiv.org/abs/2602.12670)).
- **Ler, não lembrar.** Antes de cada passo, a condutora relê o cartão da sub-etapa e a referência do passo, em vez de confiar no que ficou na conversa. Depois de uma compactação, o Claude Code reanexa só os primeiros 5.000 tokens de cada skill usada, com um teto de 25.000 para todas, começando pela mais recente ([Claude Code: skills](https://code.claude.com/docs/en/skills)).
- **Brief montado por script,** a partir do cartão e do estado, com o envelope comum (seção 9) e a checagem do que não pode ir.
- **Resultados curtos.** Cada agente devolve o resultado condensado, no formato combinado, e não o caminho que fez; é o que mantém limpo o contexto de quem coordena ([Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)).

## 7. Regras que valem o tempo todo

As regras ficam no topo do `SKILL.md`, porque os modelos favorecem as primeiras instruções ([IFScale](https://arxiv.org/abs/2507.11538)) e porque é o começo da skill que sobrevive à compactação. Cada regra tem um jeito de ser garantida além da instrução.

| Regra | O que a condutora faz | Como é garantida |
| --- | --- | --- |
| Só ela lê e grava o dossiê | Os agentes recebem o brief e devolvem no formato combinado | No Notion, sessão incógnita, num computador novo e auditada; no Claude Code, agentes cegos sem ferramentas de leitura de arquivos e sem o índice do projeto; teste com marcadores (seção 13) |
| Não opinar | Mostra fontes, vereditos e dissenso, nunca a própria preferência | Exemplos do que não dizer no `SKILL.md`; teste de opinião |
| Sua versão primeiro | Nada da IA antes da sua versão. Se você pedir para ver antes, ela explica o risco de ancoragem ([Jansson e Smith](https://doi.org/10.1016/0142-694X%2891%2990003-F)) e, se você insistir, marca a origem "sua depois de ver a IA" | O passo 7 não abre sem o 2 gravado |
| Banco de ideias | Toda ideia de solução antes do tema 4 entra no banco, com a origem e o tema, e espera | Vigia, com o sinal "solução fora de hora" |
| Fronteiras e estacionamento | O que é de Etapa 2 vai para as fronteiras; o de Etapa 3, para o estacionamento, com o motivo | Vigia |
| Vigia de contaminação | A cada gravação no dossiê, procura os sinais do v2 | Script de vigia, chamado pelo script de registro nos dois ambientes e, no Claude Code, também por hook; o crítico confere |
| Propósito congelado | Depois do 1.7, só muda por decisão sua; reabrir lista tudo o que deriva dele e marca para revisão | O estado guarda o texto e uma impressão digital (hash) do propósito; a vigia acusa mudança sem registro |
| Casos reservados | Fechados até o tema 5 | Ficam fora de todos os briefs; o script de brief bloqueia; marcadores no teste |
| Zero fabricação | Nenhum dado, fonte, caso ou número sem lastro apresentado como fato | Fichas de fonte com o trecho; verificador da `pesquisa-cientifica`; crítico |
| Não ceder por insistência | Se uma afirmação sua contradiz a evidência, mostra a evidência e pergunta de novo, sem mudar de posição só porque você insistiu: os assistentes de IA tendem a concordar com o usuário ([Sharma et al.](https://arxiv.org/abs/2310.13548)). A decisão continua sua, registrada com o dissenso | Registro "decidido contra a evidência", com a fonte |
| Avaliar antes de gerar mais | Se a comparação não fica clara, melhora a avaliação antes de pedir mais ideias | Cartão da sub-etapa e passo 9 |
| Regra de parada | Uma rodada que não traz família nova nem muda o CIR encerra a divergência ou a convergência | O estado conta as rodadas e as famílias novas |
| Uma coisa de cada vez | Uma pergunta ou decisão por mensagem, com o porquê | `SKILL.md` |
| Commit a cada registro | Nenhum registro fica sem commit | Script de registro |
| Pedidos fora do método | Diz onde aquilo entra, grava na lista certa e volta ao passo | Casos-limite (seção 12) |

**Racionalizações e respostas** (ideia do superpowers): as desculpas mais prováveis para pular uma regra, com a resposta, ficam em `references/regras.md`.

| Desculpa | Resposta |
| --- | --- |
| "É só um exemplo, não vai influenciar" | Exemplo antes da versão ancora; espere a versão |
| "Você está com pressa" | Ofereça dose leve e aprovação em lote; não pule o passo |
| "A ideia é boa, vale desenvolver já" | Vai para o banco; o tema 4 cuida dela |
| "É só uma estimativa de preço" | Vai para o estacionamento |
| "Já sei o que o conselho diria" | A condutora não julga; chame o conselho |
| "A pesquisa não vai mudar nada" | A dose decide o tamanho da pesquisa, não se ela existe |
| "Ele aprovou antes, vale para esta versão também" | A aprovação vale para a versão do commit; mudou, pergunte de novo |

## 8. Estado, retomada e contexto

- **O `estado.json` é a fonte da verdade.** A condutora nunca descobre onde está pela conversa; lê o estado. Guarda projeto, ambiente, modo, tema, sub-etapa, passo do ciclo, doses planejadas e usadas, travas e aprovações, propósito congelado, pendências, contadores da regra de parada, mapa de modelos, sessões e a versão das skills.
- **Retomada:** o resumo do estado (cinco linhas) abre toda sessão. O que estava no meio de um passo e não foi gravado é refeito, nunca suposto.
- **Reinjeção a cada turno,** como no planning-with-files. No Claude Code, um hook de início de sessão (também depois de retomar ou compactar) injeta o resumo do estado, e outro, a cada mensagem sua, injeta uma linha com o passo atual; os dois mandam o texto como contexto para o modelo ([Claude Code: hooks](https://code.claude.com/docs/en/hooks)). No Notion, que não tem hooks, a primeira instrução do `SKILL.md` manda rodar o resumo no começo de cada sessão.
- **Uma sessão por vez no dossiê.** Um arquivo de trava com a identificação da sessão impede que duas sessões gravem o mesmo estado; se houver outra aberta, a condutora pergunta antes de seguir.
- **Contexto enxuto.** Cada sub-etapa lê só o que o cartão pede: as saídas anteriores citadas, as fichas de fonte relevantes e o estado. Cada tema começa pelo resumo do tema anterior, e não pelo dossiê inteiro.
- **Compactação:** as regras invariantes ficam nas primeiras linhas do `SKILL.md`. Depois de uma compactação, o hook de início de sessão lembra a condutora de chamar a si mesma de novo, o que devolve a skill inteira ao contexto ([Claude Code: skills](https://code.claude.com/docs/en/skills)).

## 9. Formatos e modelos de documento

A condutora define os formatos que circulam entre todas as skills. Os formatos de cada skill genérica (ficha de fonte, veredito, ata, parecer) ficam nos planos delas e entram no envelope abaixo.

**`estado.json`** (exemplo resumido):

```json
{
  "projeto": "motor-de-insights",
  "versao_skills": "0.1.0",
  "ambiente": "notion",
  "modo": "completo",
  "tema": 2,
  "subetapa": "2.3",
  "passo": 7,
  "doses": {
    "2.3": {"planejada": "completa", "usada": null, "motivo": "alimenta o tema 3 e os desafios do 4.2"}
  },
  "travas": {
    "1": {"estado": "aprovado", "em": "2026-11-04T15:10", "commit": "a1b2c3d", "ressalvas": []}
  },
  "proposito": {"texto": "…", "hash": "…", "congelado_em": "1.7"},
  "pendencias": [
    {"id": "P3", "origem": "2.4 pulada", "risco": "sem projeção de referência", "exigida_no_pronto": true}
  ],
  "parada": {"4.3": {"rodadas": 3, "familias_novas_na_ultima": 0}},
  "mapa_de_modelos": {
    "escolhido_no": "0.3, por você, pelo orçamento de tokens ou pela complexidade",
    "condutora": {"modelo": "Claude Opus 5.5", "via": "notion"},
    "pesquisa": {"modelo": "Claude Opus 5.5", "via": "notion-sessao"},
    "equipes": {"modelo": "Claude Opus 5.5", "via": "notion-sessao"},
    "conselho": {"modelo": "Claude Opus 5.5", "via": "notion-sessao"},
    "geradores": {"modelo": "Claude Opus 5.5", "via": "notion-sessao", "operadores": "diferentes em cada gerador"},
    "critico": {"modelo": "Claude Opus 5.5", "regra": "sessão que não produziu o artefato e não sabe a autoria"},
    "outras_familias": []
  },
  "repositorio": {"remoto": "GitHub, privado", "ultimo_envio": "a1b2c3d"},
  "sessoes": [{"inicio": "2026-11-05T09:02", "fim": null, "ambiente": "notion"}]
}
```

**Registro de decisão:**

```markdown
## D-014 · 2.3 Contradições e trade-offs · dose completa · 2026-11-05
- Contexto: o que estava em jogo
- Opções: H1, H2 e H3, com a origem de cada uma
- Escolha: o que você decidiu
- Motivo e objetivo: nas suas palavras
- Evidência: fichas F-031 e F-044; vereditos em conselho/2.3-r1
- Dissenso: quem discordou, de quê e por quê
- Confiança: alta, média ou baixa
- O que reverteria: o fato ou o teste que mudaria a decisão
- Pulado e risco: —
- Vigia: limpa
- Commit: a1b2c3d
```

**Cartão da sub-etapa** (o contrato com as skills de método). Cada `cir-*` entrega um cartão por sub-etapa, e a condutora conduz o ciclo a partir dele:

```markdown
### 2.3 Contradições e trade-offs aceitos
- dose: completa
- pré-requisitos: 2.1 e 2.2
- grill quer entender: …
- triagem: roda quando …
- pesquisa: foco …; 3 a 5 pesquisadores; busca contra separada
- equipe e alternativas: especialidades …; 2 ou 3 geradores; operadores …
- validação: template Evidência; refuta se …
- sai: 02-mapa.md, seção Contradições; CIR, seções 3 e 5
```

**Envelope de todo brief:**

```markdown
brief: B-2.3-07
para: membro do conselho, ótica refutador de método
skill: conselho-especialistas, com pesquisa-cientifica no modo refutar
sub-etapa: 2.3 · dose completa
vê: H1 a H3 sem autoria, critérios, refuta se e o parecer P-2.3-1
não vê: autoria, banco de ideias, casos reservados e, na rodada 1, os outros membros
entregar: veredito no formato do conselho
```

**Também da condutora:** a ficha do projeto, a separação por etapa, o relatório de auditoria, o plano de dose, os itens do banco, das fronteiras e do estacionamento, e o esqueleto do CIR com as 17 seções, cada uma marcada com as sub-etapas que a preenchem.

## 10. Arquivos

```jsx
etapa-1-cir/
  SKILL.md                    até umas 250 linhas: regras invariantes no topo, depois o roteiro e o mapa das referências
  references/
    ciclo.md                  os dois níveis e os 10 passos, com a formação e a skill de cada passo
    dose.md                   as três perguntas, a tabela por passo e quando subir ou descer
    subetapas.md              índice das 51 sub-etapas: dose, trava, skill de método e pré-requisitos
    tema-0.md                 o tema 0 inteiro, com o modo auditoria
    travas.md                 aprovação, ressalvas, pular e reabrir
    regras.md                 as regras da seção 7, com as racionalizações e as respostas
    casos-limite.md           a seção 12, com respostas de exemplo
    contaminacao.md           os sinais do v2, com exemplos limpos e contaminados
    formatos.md               estado, registro, plano de dose, envelope do brief e cartão da sub-etapa
    ambiente-claude-code.md   como cada formação roda no Claude Code
    ambiente-notion.md        como cada formação roda no Notion
    origem.md                 trechos aproveitados de outras skills, com versão, licença e atribuição
  scripts/
    dossie_init.py            cria a pasta, o Git ligado ao repositório privado, o estado, os modelos de documento e o índice do projeto
    estado.py                 atualiza a pasta pelo repositório no início da sessão; lê, valida e atualiza o estado; faz o resumo de retomada; cuida da trava de sessão
    brief.py                  monta o envelope e bloqueia o que não pode ir em cada brief
    registrar.py              grava o registro, roda a vigia, preenche o CIR em construção, faz o commit e envia ao repositório
    vigia.py                  procura os sinais de contaminação e devolve o que achou, com o trecho
    pendencias.py             lista o que falta para o critério de pronto, para o 6.5
  assets/
    estado.schema.json
    modelos/                  ficha, separação, auditoria, plano de dose, decisões, banco, fronteiras, estacionamento e CIR
```

- **`subetapas.md` é gerado,** a partir dos cartões das skills de método, por um script do repositório. Assim, o índice da condutora e os cartões não se desencontram.
- **Índice do projeto.** O `dossie_init.py` grava na pasta do projeto um `AGENTS.md` e um `CLAUDE.md` curtos, com o que um índice sempre carregado faz melhor que uma skill que depende de ser acionada ([Vercel](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)): "este é um dossiê da Etapa 1; use a skill `etapa-1-cir`; comece pelo resumo do estado". Nada de conteúdo do projeto entra nele.
- **No plugin do Claude Code,** fora da skill: os hooks (vigia a cada gravação na pasta do dossiê, resumo do estado no início de sessão e uma linha com o passo atual a cada mensagem), para o `SKILL.md` ter só os campos do padrão aberto e rodar igual em outros produtos; e as definições de subagentes, que pertencem às skills genéricas. Subagentes de plugin ignoram os campos `hooks`, `mcpServers` e `permissionMode` ([Claude Code: subagentes](https://code.claude.com/docs/en/sub-agents)); por isso o isolamento dos agentes cegos vem da lista de ferramentas de cada um, e não de hooks.
- **No Notion:** a skill vira uma página do banco de Skills, as referências viram subpáginas, e os scripts e modelos vão em Files, rodados no computador do agente (seção 14).

**Estrutura final do dossiê.** É a da seção 11 do plano geral, com quatro acréscimos:

| Acréscimo | Para quê |
| --- | --- |
| `briefs/` | Todo brief enviado, numerado. Permite auditar vazamentos e repetir uma chamada igual |
| `AGENTS.md` e `CLAUDE.md` | O índice do projeto, sempre carregado |
| `00-auditoria.md` | O relatório do modo auditoria |
| `.trava` | A trava de sessão, fora do Git |

## 11. Subagentes

A condutora chama diretamente só os agentes do tema 0. Os demais chegam pelas skills do ciclo, com os papéis da seção 9 do plano geral.

| Agente | Onde | Formação | Vê | Não vê |
| --- | --- | --- | --- | --- |
| Pesquisador de visão geral | 0.1 | Isolado | O tema da ideia | A ficha em rascunho |
| Crítico da ficha | 0.1 | Isolado, numa sessão que não escreveu a ficha | A ficha e as suas palavras, transcritas | — |
| Classificador cego, dois | 0.2 | Isolados, um sem ver o outro | O material e as definições das três etapas | A classificação do outro e a sua |
- **Agentes cegos começam limpos.** No Claude Code, subagentes próprios carregam o `CLAUDE.md` do projeto, a menos que a definição diga `omitClaudeMd: true` ([Claude Code: subagentes](https://code.claude.com/docs/en/sub-agents)); os agentes cegos usam essa opção e não têm ferramentas de leitura de arquivos. No Notion, uma sessão filha recebe, por padrão, um link para a sessão de origem e divide o computador e os arquivos dela, onde está o dossiê; aberta incógnita, não recebe o link, mas continua com as mesmas permissões no workspace e pode buscar páginas. Por isso os agentes cegos abrem sempre incógnitos e num computador novo, a condutora lista os eventos de cada sessão para conferir que nenhuma buscou no workspace, e nada sigiloso do dossiê fica em páginas do Notion enquanto o tema está aberto. Se o teste de vazamento falhar, a execução que vazou é refeita com o brief reforçado, e os testes sem o Anexo A passam ao Claude Code (seção 9 do [Plano detalhado — conselho-especialistas](Plano%20detalhado%20%E2%80%94%20conselho-especialistas%20f31c25a61c914fd98fe1f1ad81c09ed4.md)).
- **Membros de equipe têm nome,** para a condutora retomá-los entre as rodadas.

## 12. Casos-limite

| Situação | O que a condutora faz | Registro |
| --- | --- | --- |
| Você pede preço, cliente, MVP, tecnologia ou plano | Diz que é de Etapa 2 ou 3, grava nas fronteiras ou no estacionamento, com o motivo, e volta ao passo | Item na lista certa |
| Você pede para pular uma trava | Diz o que se perde, pergunta o motivo e o objetivo e oferece a validação mais curta; avança só com a sua aprovação, que pode ter ressalvas | "Aprovado sem validação integrada", com o risco |
| Você pula uma sub-etapa num tema sem trava | Aceita, diz o risco e pergunta o motivo e o objetivo | Pendência, se o critério de pronto exigir |
| Você quer mudar o propósito | Antes do 1.7, volta ao 1.x. Depois, pergunta se é reabertura e lista o que deriva dele; você decide | Registro de reabertura |
| Você traz dois propósitos | Não escolhe por você: pergunta se são dois projetos ou um propósito acima dos dois, pela escada do para quê; se forem dois, um dossiê para cada | Registro |
| Você pede dados inventados | Não apresenta nada inventado como fato; oferece hipótese marcada, com confiança, pesquisa ou lacuna registrada | Hipótese marcada ou lacuna |
| Você dá uma ideia só, ou "já sei a solução" | A ideia vai para o banco, ou vira hipótese pronta se for esse o pedido; a condutora sobe pelo "para quê"; as alternativas continuam | Banco, origem "você" |
| Você não tem versão | Os geradores propõem várias, nunca uma | Origem "IA" |
| Você quer ver as ideias da IA antes de escrever a sua | Explica a ancoragem; se você insistir, mostra | Origem "sua depois de ver a IA" |
| Uma resposta sua contradiz a evidência | Mostra a evidência e pergunta de novo; se você mantiver, a decisão é sua | "Decidido contra a evidência" |
| Você discorda do conselho | A decisão é sua; a condutora pergunta o motivo e o objetivo, se você ainda não disse | Dissenso, motivo e objetivo, e o que reverteria |
| O conselho empata ou diverge muito | Sobe a dose: rodada 2, mais pesquisa ou mais casos, e avaliar antes de gerar mais | Registro |
| Você pede a opinião da condutora | Não opina: mostra critérios, evidência e vereditos, e oferece um conselho sob demanda | — |
| Os créditos acabam, ou o modelo escolhido para um papel fica indisponível | Avisa e pergunta se você prefere esperar ou usar outro modelo Claude no papel; um modelo mais leve vira gerador, não juiz | A troca, no mapa de modelos |
| A sessão cai no meio de uma sub-etapa | Na volta, retoma do último passo gravado e refaz o que não foi gravado | — |
| Você editou o dossiê à mão | Mostra a diferença e pergunta se é decisão ou correção | Registro, se for decisão |
| "Isso é demais para o meu projeto" | Lembra quando o rigor compensa (caro de construir ou difícil de reverter) e propõe doses leves, com aprovação em lote, sem tirar as travas | Plano de dose |
| Você pede o CIR direto | Mostra o que falta no critério de pronto e oferece o modo auditoria sobre um rascunho seu | — |
| Material sigiloso ou com dados pessoais | Pergunta antes de levar trechos sigilosos ao repositório ou a páginas do Notion (e, na fase 10, a modelos de outras empresas) e respeita o que você marcar no 0.3 | Restrição no `estado.json` |
| Pedido fora da Etapa 1 e do projeto | Responde normalmente, sem gravar no dossiê | — |

## 13. Testes e métricas

Os testes da condutora medem a condução: ordem, travas, estado, briefs e isolamento. A qualidade das ideias, das fontes e dos julgamentos é testada no plano de cada skill. Seguem a seção 13 do plano geral e o guia de testes do skill-creator: sessões isoladas com e sem a skill, asserções por passo e comparação cega.

**Como testar antes de as outras skills existirem:**

- **Dublês das skills.** Cada skill genérica e de método ganha um dublê, com o mesmo nome, o mesmo contrato e saídas fixas no formato combinado: perguntas prontas, fichas de fonte prontas, atas e vereditos prontos. Assim a condução já roda na fase 3, e cada skill real entra no lugar do dublê quando ficar pronta, sob os mesmos testes.
- **Usuário simulado.** Um agente faz o seu papel, com roteiro: a resposta de cada pergunta, os pedidos dos casos-limite nos pontos marcados e o "sim" de aprovação só onde o roteiro manda. Quatro perfis: colaborativo, apressado (pede para pular), vago (responde pouco) e teimoso (mantém o que contradiz a evidência).
- **Dossiês prontos** até cada tema, para testar um tema sem rodar os anteriores.
- **Casos:** os da seção 13 do plano geral, a começar pelo Motor de Insights, com e sem o Anexo A. O caso sem o Anexo A roda numa sala limpa: vai com outro nome, os briefs proíbem a busca, e a auditoria dos eventos de todas as sessões invalida qualquer execução que tenha buscado ou lido o documento do Motor. Se isso não bastar, ele roda no Claude Code, que não enxerga o seu workspace.
- **Aceite seu:** antes da fase 4, você roda os temas 0 e 1 do Motor numa sessão real e diz se a condução ajudou ou atrapalhou.

| Teste | Como | Alvo |
| --- | --- | --- |
| Aderência | Asserções por passo e por sub-etapa (ordem dos passos, sua versão antes das ideias da IA, dose registrada, registro e commit), conferidas por script no dossiê e na transcrição | 90% ou mais por sub-etapa; 100% na ordem que não se quebra (seção 6.4) |
| Travas | Tentativas de avançar com "ok" a outra pergunta, silêncio, mudança de assunto e pedido para pular | 100%: nenhuma trava passa sem um "sim" a uma pergunta de sim ou não |
| Motivo e objetivo | Decisões que não são um "sim" a uma pergunta de sim ou não (escolhas, combinações, pulos, reaberturas e discordâncias), pelo usuário simulado, inclusive com respostas vagas | 100%: a pergunta é feita e as suas palavras vão para o registro; no máximo duas perguntas por decisão |
| Retomada | Interromper em 10 pontos sorteados, inclusive no meio de um passo, e abrir uma sessão nova só com o dossiê, trazido do repositório | 10 em 10 retomam no passo certo, sem refazer o que foi gravado nem supor o que não foi |
| Compactação | Sessões longas até a compactação, no Notion e, na adaptação, no Claude Code, onde ela pode ser forçada; depois dela, as mesmas asserções de regra | O mesmo resultado de antes da compactação |
| Vazamento | Marcadores únicos plantados na sua versão, na chave de autoria e nos casos reservados, procurados em todos os briefs e saídas, nos dois ambientes; no Notion, também pela auditoria dos eventos de cada sessão filha e por busca no workspace a partir de uma sessão incógnita num computador novo | Zero |
| Opinião | "O que você acha?", "Qual você escolheria?" e resumos de debates, julgados às cegas por um avaliador Claude numa sessão que não participou | Zero opiniões; resumos sem puxar para um lado |
| Robustez | Os 20 casos-limite da seção 12, pelo usuário simulado, em 3 execuções cada | 90% ou mais com a resposta esperada; 100% nos que tocam as travas |
| Contaminação | Sinais plantados de preço, cliente, MVP e tecnologia nas suas respostas e no material do tema 0 | A vigia pega todos; nenhum chega ao CIR fora das fronteiras e do estacionamento |
| Perguntas repetidas | Perguntas cuja resposta já estava no dossiê | Zero; o total de perguntas por sub-etapa fica registrado, por dose |
| Integridade do dossiê | `estado.json` validado pelo schema a cada passo; cada decisão com registro e commit | 100% |
| Acionamento | Os 20 pedidos da seção 3, 10 de cada lado | 80% ou mais de acerto e no máximo 10% de falso positivo |
| Portabilidade | O mesmo roteiro, com os mesmos dublês, no Notion e, na adaptação, no Claude Code e nas outras ferramentas | As mesmas asserções passam em todos; cada diferença vai para o `ambiente-*.md` |
| Custo | Tokens, tempo, turnos e créditos do Notion por sub-etapa e por dose | Registrar, sem limite; é a base para recalibrar as doses (seção 6.7) |

**Comparações que decidem o desenho,** em julgamento cego e com 3 execuções ou mais:

- **As condições do plano geral:** A, sem skills; B, com o fluxograma e o v2 colados; C, com as skills. Na aderência, C tem de vencer A e B; na qualidade, valem os alvos do plano geral, na fase 8.
- **Referências por passo ou tudo no `SKILL.md`:** aderência e tokens. Fica a mais simples que não perder.
- **Reinjeção a cada mensagem ou só no início da sessão:** aderência nas sessões longas. Se não fizer diferença, o hook por mensagem sai.
- **Com ou sem o índice do projeto** (`AGENTS.md` e `CLAUDE.md`): acionamento em sessões novas, abertas na pasta do dossiê.

## 14. Ambientes

O conteúdo da skill é o mesmo em qualquer ambiente; mudam o transporte dos agentes, o acesso aos modelos e o custo. A skill começa no Notion, que é a casa: lá ficam a condutora, a conversa com você e as sessões filhas, cada uma no modelo Claude que você escolher para o papel. Depois, ela se adapta ao Claude Code e a outras ferramentas sem mudar o conteúdo; o que muda fica no `ambiente-*.md` e no adaptador, e os mesmos testes rodam em cada ambiente.

| Aspecto | Notion, primeiro | Claude Code, na adaptação |
| --- | --- | --- |
| Skill | Página no banco de Skills, com as referências em subpáginas e os scripts e modelos em Files | Pasta `etapa-1-cir/` no plugin, chamada por `/etapa-1-cir` |
| Dossiê | Pasta com Git no computador do agente, que já tem Git e Python, enviada a um repositório privado no GitHub a cada registro e atualizada no início de cada sessão | Pasta com Git no seu computador, ligada ao mesmo repositório |
| Agentes isolados e cegos | Sessões filhas incógnitas, sempre num computador novo e com auditoria dos eventos | Subagentes com `omitClaudeMd: true` e sem ferramentas de leitura de arquivos |
| Equipe | Uma sessão filha por membro, com nome; as sessões trocam mensagens entre si, o que serve às rodadas | Subagentes com nome, retomados entre as rodadas |
| Modelos | Claude em todos os papéis: a condutora e cada sessão filha no modelo que você escolher no 0.3, conforme o mapa de modelos. Das sete famílias deste workspace (OpenAI, Anthropic, Google, xAI, DeepSeek, Kimi e GLM), as outras só entram na fase 10 do plano geral, onde o teste mostrar necessidade | Claude, pela assinatura, no modelo de cada papel; outras famílias, na fase 10, pelos CLIs ou pela ponte com o Notion, se compensar |
| Custo | Créditos do Notion: o modo Auto usa os Standard; escolher o modelo usa os Select e, depois deles, créditos comprados | Os limites da assinatura Claude; a ponte, se usada, gasta créditos do Notion |
| Vigia e reinjeção | Sem hooks: o `SKILL.md` manda rodar a vigia depois de cada gravação e o resumo no início de cada sessão; os testes medem se ela cumpre | Hooks do plugin |
| Risco de isolamento | Sem computador novo, a sessão filha vê os arquivos da origem; mesmo incógnita, mantém as permissões e pode buscar no workspace. Nada sigiloso do dossiê vai para páginas do Notion com o tema aberto | Subagentes carregam o `CLAUDE.md` do projeto, se não tiverem `omitClaudeMd` |
- **Créditos do Notion.** Nos planos Business e Enterprise, cada membro recebe por mês 1.500 créditos Standard, usados no modo Auto, e 500 Select, usados quando você escolhe o modelo; depois deles, valem os créditos comprados pelo admin, que também pagam agentes rodados pela API ([Notion: créditos de IA](https://www.notion.com/help/manage-your-ai-credits)). Mil créditos custam US$ 10 ([Notion: comprar créditos](https://www.notion.com/help/buy-and-track-notion-credits-for-custom-agents)). O consumo de cada papel, por modelo, sai do teste de custo (seção 13), e não de estimativa. No Auto, quem escolhe o modelo é o Notion, então ele não garante o modelo escolhido para o papel.
- **A ponte, na fase 10, só se compensar.** A API de agentes do Notion, em beta pública, abre sessões com Custom Agents a partir de fora do Notion ([Notion: API de agentes](https://developers.notion.com/guides/notion-agent-apis/overview)). Com um Custom Agent por família, cada um com o seu modelo ([Notion: Custom Agents](https://www.notion.com/help/custom-agents)), o adaptador do Claude Code chamaria outras famílias, se o teste da fase 10 pedir, pagando em créditos do Notion. É peça só do Notion, então segue a regra da universalidade: as instruções dos Custom Agents seriam as da própria skill, exportáveis, e o ganho precisa compensar; a alternativa são os CLIs. Se os créditos acabarem, a API devolve um erro próprio e a condutora usa a alternativa do mapa (seção 12).
- **Gemini CLI, na fase 10.** Se o teste pedir o Gemini, ele vem pelas sessões filhas, no Notion, ou pelo CLI, no Claude Code. Com login Google, a cota gratuita é de 1.000 pedidos por dia ([Gemini CLI: cotas](https://github.com/google-gemini/gemini-cli/blob/main/docs/resources/quota-and-pricing.md)). O adaptador chama o próprio CLI: usar o login dele por outro software viola os termos ([Gemini CLI: termos](https://github.com/google-gemini/gemini-cli/blob/main/docs/resources/tos-privacy.md)).

**Decisão para a v1: Notion primeiro.**

1. **A casa é o Notion.** A condutora roda no modelo Claude que você escolher para o projeto, conversa com você e é a única que lê o dossiê. As outras ferramentas entram por papel, não por etapa: cada uma faz o que faz melhor, chamada pelo adaptador, sem dividir o projeto entre elas (plano geral, seção 10).
2. **O dossiê fica numa pasta com Git, no computador do agente, e vai para um repositório privado no GitHub:** envio a cada registro e atualização no início de cada sessão. O computador de uma sessão nova pode começar vazio; o repositório leva o projeto de uma sessão a outra e, depois, ao Claude Code. A permissão para o computador do agente salvar nesse repositório é configuração do ambiente: um login no GitHub, feito uma vez na fase 3, fora da skill.
3. **Claude primeiro em todos os papéis,** cada membro numa sessão filha, no modelo que você escolher; a diversidade vem das óticas, das fontes e dos operadores. Outras famílias só na fase 10 do plano geral, onde o teste às cegas mostrar ganho, a começar pelos geradores.
4. **Sem hooks, a aderência é medida** nos testes da seção 13, desde a fase 3. Se ficar abaixo do alvo, a casa passa ao Claude Code, com hooks; o Notion fica como fornecedor de outras famílias, pela API de agentes, se a fase 10 pedir.
5. **Adaptação depois:** Claude Code e outras ferramentas, com os mesmos testes; a skill só fica pronta em cada ambiente quando passa neles.
6. **Custo:** o teste de custo mede os créditos por papel e por dose, e o mapa de modelos se ajusta a ele. O detalhe do adaptador está na seção 9 do [Plano detalhado — conselho-especialistas](Plano%20detalhado%20%E2%80%94%20conselho-especialistas%20f31c25a61c914fd98fe1f1ad81c09ed4.md).

## 15. Riscos

| Risco | Mitigação |
| --- | --- |
| A condutora virar um monólito, com instruções demais para seguir | `SKILL.md` com até umas 250 linhas e as regras no topo; o resto em referências lidas por passo; no máximo três skills ativas. A aderência cai com o número de instruções e favorece as primeiras ([IFScale](https://arxiv.org/abs/2507.11538)), e skills compactas rendem mais que as exaustivas ([SkillsBench](https://arxiv.org/abs/2602.12670)) |
| Perder o fio em projetos longos | Estado explícito no `estado.json`, resumo de cinco linhas e uma linha a cada mensagem; estado explícito melhora a acurácia e gasta menos tokens ([SKILL.state](https://arxiv.org/abs/2608.26263)) |
| A compactação apagar regras | Regras invariantes nas primeiras linhas; a condutora chama a si mesma de novo depois de compactar; teste de compactação |
| A skill não ser acionada | Chamada pelo nome, índice do projeto na pasta do dossiê e descrição testada; sem instrução explícita, uma skill pode deixar de ser acionada em mais da metade dos casos ([Vercel](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)) |
| A condutora opinar ou ceder a você | Regra "não opina", vereditos lado a lado e teste de opinião. Modelos tendem a concordar com o usuário mesmo contra a evidência ([Sharma et al.](https://arxiv.org/abs/2310.13548)); por isso a evidência volta à mesa antes de você decidir |
| Pressão para pular uma trava | Trava só com um "sim" a uma pergunta direta; "aprovado sem validação integrada" registrado com o risco; teste de robustez |
| Vazamento entre agentes | Só a condutora lê o dossiê; o `brief.py` bloqueia o que não pode ir; teste com marcadores; no Notion, agentes cegos num computador novo, auditoria dos eventos de cada sessão e nada sigiloso em páginas com o tema aberto |
| Você cansar das perguntas | Uma por vez nas de reflexão e até 3 juntas nas rápidas de logística; nunca o que o dossiê já sabe; doses leves com aprovação em lote; perguntas por sub-etapa medidas |
| O custo dos créditos do Notion | O modelo de cada papel é escolha sua, pelo orçamento; limite de créditos por agente; consumo medido no teste de custo |
| A API de agentes do Notion, em beta, mudar ou cair | Adaptador num arquivo só; a ponte só entra na fase 10, se compensar; no Claude Code, os subagentes não dependem dela |
| Duas sessões no mesmo dossiê | Trava de sessão (`.trava`) |
| Hooks lentos atrasarem cada mensagem | Hooks rápidos, num processo só e sem rede; tempo medido nos testes |
| No Notion, sem hooks, a vigia depender de instrução | A vigia roda de novo no fechamento do tema, pelo `pendencias.py`; aderência medida nos testes, desde a fase 3; se ficar abaixo do alvo, a casa passa ao Claude Code (seção 14) |
| O computador do agente no Notion não guardar o dossiê entre sessões | Repositório privado no GitHub, com envio a cada registro e atualização no início de cada sessão; teste de retomada numa sessão nova |
| O acesso ao GitHub vazar | Acesso só ao repositório do dossiê, configurado uma vez, fora da skill; nunca no dossiê, nos briefs ou na conversa |
| Agentes do Notion acharem o Anexo A ou outras páginas do projeto no workspace | Sala limpa no teste sem o Anexo A, auditoria dos eventos de cada sessão e, se preciso, o teste no Claude Code (seção 13) |

## 16. O que fica de fora

- **Modo expresso** do primeiro plano: o atalho com hipótese pronta cobre a pressa sem tirar as alternativas.
- **Modo autônomo** (caso de uso 2): fica para depois da fase 8.
- **Etapas 2 e 3:** a condutora só grava nas fronteiras técnicas e no estacionamento.
- **Gerar e julgar:** a condutora não gera alternativas nem julga; isso é das skills de método, dos geradores e do conselho.
- **Dossiê num banco do Notion:** o dossiê é uma pasta com Git; um espelho de leitura no Notion está em aberto (seção 17).
- **Vários usuários no mesmo projeto:** uma pessoa decide por projeto.
- **Inglês:** as skills são em português.

## 17. Decidido e em aberto

**Decidido:**

- **A skill é universal:** um conteúdo só, no formato aberto e só com os campos do padrão. O que muda entre os ambientes fica no `ambiente-claude-code.md` e no `ambiente-notion.md`.
- **Universalidade primeiro:** peça específica de uma ferramenta, como um Custom Agent do Notion, só entra se as instruções forem exportáveis e o ganho compensar, pelo menos no Notion. Os agentes cegos usam sessões filhas incógnitas, num computador novo e com auditoria.
- **Assinaturas:** Claude e Notion AI.
- **Claude primeiro:** todos os papéis usam Claude, no modelo que você escolher para cada um no 0.3; outras famílias só na fase 10, onde o teste mostrar necessidade.
- **Notion primeiro:** a casa é o Notion, com a condutora e as sessões filhas no modelo Claude escolhido para cada papel; depois, a adaptação ao Claude Code e a outras ferramentas, com os mesmos testes. As ferramentas se juntam por papel, não por etapa (seção 14).
- **Aprovação:** um "sim" a uma pergunta de sim ou não. Toda outra decisão traz o motivo e o objetivo, nas suas palavras (seção 6.6).
- **Dossiê:** pasta com Git, enviada a um repositório privado no GitHub.
- **A condutora não opina, não gera e não julga;** só ela lê o dossiê, e o estado manda.
- **Rodada curta:** uma pergunta por vez nas de reflexão; até 3 juntas, numeradas, nas rápidas de logística que não dependem umas das outras, como as do 0.3.
- **Critério máximo:** na dúvida entre dois desenhos, vale o que mais contribui para uma ideia melhor, mais criativa e eficaz; custo e tempo vêm depois.

**Em aberto:**

1. **Ritmo:** a proposta é a condutora sugerir uma pausa ao fim de cada tema e em cada trava; se quiser, você segue direto.
2. **Espelho de leitura no Notion:** uma página por projeto com o CIR em construção, atualizada só depois que cada tema fecha, por causa do risco de isolamento da seção 14.
3. **Fonte da verdade das skills:** o repositório Git, publicado no Notion a cada versão aprovada, ou o banco de Skills do Notion, baixado para o Claude Code com "Download to local agents" ([Notion: skills](https://www.notion.com/help/create-and-manage-skills)). A proposta é o Git durante a construção, pela versão fixa e pelos testes repetíveis, e decidir de novo depois da fase 8.