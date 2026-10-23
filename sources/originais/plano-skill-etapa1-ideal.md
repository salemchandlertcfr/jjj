# Plano da skill — Etapa 1 (método IDEAL)

<aside>
⚠️

Esta versão (uma skill só, no Codex) foi substituída pelo [Plano geral das skills — Etapa 1 (CIR)](Plano%20da%20skill%20%E2%80%94%20Etapa%201%20(m%C3%A9todo%20IDEAL)/Plano%20geral%20das%20skills%20%E2%80%94%20Etapa%201%20(CIR)%2072d0fdc1db19433e9101d1ac3b3015ef.md) e pelo [Fluxograma completo — Etapa 1 (método IDEAL em ciclo)](Plano%20da%20skill%20%E2%80%94%20Etapa%201%20(m%C3%A9todo%20IDEAL)/Fluxograma%20completo%20%E2%80%94%20Etapa%201%20(m%C3%A9todo%20IDEAL%20em%20cic%20f1f71e3bd5e6487ebdfc94cd7e9fa161.md). Fica como histórico.

</aside>

Planejamento do desenvolvimento da skill para a Etapa 1 do fluxograma de criação de startups, com base em [Método IDEAL — passo a passo](M%C3%A9todo%20IDEAL%20%E2%80%94%20passo%20a%20passo%200a6e02fec42e47e09d4a10981b12849b.md) e [Etapa 1 — Concepção Ideal da Solução: método IDEAL (v2)](../Etapa%201%20%E2%80%94%20Concep%C3%A7%C3%A3o%20Ideal%20da%20Solu%C3%A7%C3%A3o%20m%C3%A9todo%20IDEAL%20%20629394b6e12b49c792805775c07e27d3.md). Define ferramenta, arquitetura, conteúdo, testes e roadmap; a skill em si vem depois.

## 1. Resumo das decisões

- **Ferramenta:** criar a versão universal (master) no **Codex**, seguindo o processo do **skill-creator original da Anthropic**, do qual o seu [skill-creator](https://app.notion.com/p/skill-creator-3d16b1ab777b4d31a8f2302ed9ee976e?pvs=21) é a adaptação para o Notion. O seu entra na etapa de adaptação. O Notion AI fica com o planejamento (este documento), a adaptação e os testes no Notion. O Claude agent do Notion não é indicado para criar.
- **Quantas skills:** **uma agora**, `metodo-ideal`, que conduz os 9 passos e carrega uma referência por fase. Dois módulos internos, divergência e revisão adversarial, já nascem com interface própria e viram skills separadas quando as Etapas 2 e 3 precisarem deles.
- **Papel da IA:** facilitadora e coautora. Quem decide nos gates é você. A skill é chamada de forma explícita (`/metodo-ideal` ou `$metodo-ideal`).
- **Memória:** um dossiê por CIR guarda estado, banco de ideias e decisões entre sessões.
- **Qualidade:** proteções contra ideias homogêneas e contra bajulação. Você gera antes da IA, a IA gera em paralelo com princípios diferentes e a avaliação acontece em contexto novo.
- **Prova:** só vira v1 depois de testes com e sem a skill (e com o método apenas colado no prompt), em pelo menos dois ambientes (Codex e Notion).

## 2. Qual ferramenta usar

| Opção | A favor | Contra, para criar o master | Papel recomendado |
| --- | --- | --- | --- |
| Notion AI + seu skill-creator | Web, computador com arquivos e scripts, sessões paralelas com escolha de modelo; o seu skill-creator já cobre importação, testes e otimização da description | A skill nasce como página do banco de Skills, no formato do Notion; o skill-creator adaptado não tem scripts nem visualizador; testar a versão universal exige importá-la, o que já é a adaptação | Planejamento (agora), adaptação e testes no Notion |
| Claude agent no Notion + skill-creator | Bom com código e arquivos; conecta ao GitHub | Beta, só em Business e Enterprise; [não navega na web nem chama outros agentes](https://www.notion.com/help/use-claude-agents-in-notion) durante a sessão, então não roda as versões com e sem skill em paralelo, que são o centro do skill-creator | Não usar para criar; no máximo, ambiente testado depois |
| Codex + skill-creator | [Lê pastas com SKILL.md](https://developers.openai.com/codex/skills) de forma nativa (`.agents/skills`), com Git, scripts, subagentes e `codex exec` para rodar baterias de testes; linha de base simples (rodar sem a pasta ou com `enabled = false`) | O skill-creator do Codex não tem ciclo de avaliação; o da Anthropic funciona, exceto a otimização automática da description, que usa `claude -p` e precisa ser adaptada para `codex exec` ou feita à mão | **Criar e testar o master** |
| Extra: Claude Code ou Cowork | Ambiente de referência do skill-creator da Anthropic: tudo funciona, inclusive o visualizador e a otimização da description | Exige plano do Claude | Equivalente ao Codex, se você já usa |

**Na prática:**

1. Um repositório Git (sugestão: `startup-skills/`) com `skills/metodo-ideal/` e `evals/` é a fonte única do master, no formato da [especificação Agent Skills](https://agentskills.io/specification).
2. No Codex, instalar o [skill-creator da Anthropic](https://github.com/anthropics/skills/tree/HEAD/skills/skill-creator) em `.agents/skills/` (os subagentes do Codex fazem o papel dos do Claude) e usar o skill-creator do próprio Codex para gerar o esqueleto e validar o formato.
3. Rodar os testes com e sem a skill por subagentes ou `codex exec` e revisar os resultados no visualizador do skill-creator.
4. Importar a v1 no Notion com [Importar e adaptar skills de outras ferramentas](https://app.notion.com/p/Importar-e-adaptar-skills-de-outras-ferramentas-e0a07d1397954bf09ac8dd799d705b1a?pvs=21) e repetir os testes com [Testes e avaliação de skills](https://app.notion.com/p/Testes-e-avalia-o-de-skills-624c31b477db4437a74907b335df9810?pvs=21).
5. Sincronização: mudança no método → v2 no Notion → master → adaptações. O "Download for local agents" do Notion leva a versão do Notion para agentes locais, mas não serve como master, porque exporta a versão adaptada.

## 3. Quantas skills

| Alternativa | A favor | Contra | Veredito |
| --- | --- | --- | --- |
| Uma skill com todo o v2 no SKILL.md | Simples | Muito acima do tamanho recomendado (corpo abaixo de ~5 mil tokens); documentação exaustiva quase não melhora resultados | Não |
| Uma skill por passo (9) | Passos isolados | Acionamento frágil; com 4 ou mais skills o ganho cai; o estado se fragmenta; uma skill não chama outra de forma confiável | Não |
| **Uma skill principal + uma referência por fase + módulos com interface própria** | Corpo compacto, leitura por fase, passos testáveis isoladamente, funciona em qualquer ambiente | Exige interfaces bem definidas entre os módulos | **Sim, na v1** |
| Três skills desde já (principal + divergência + revisão adversarial) | Reuso imediato nas Etapas 2 e 3 | Nem todo ambiente encadeia skills; mais manutenção antes de provar valor | Na v2, quando houver um segundo uso |

**Por quê:**

- [SkillsBench](https://arxiv.org/abs/2602.12670): skills curadas elevaram a taxa de acerto de 33,9% para 50,5%. Skills de tamanho padrão renderam mais (+21,5 pp) que as detalhadas (+14,5) ou as abrangentes (+0,7); 2 a 3 skills por tarefa renderam mais (+19,0) que 4 ou mais (+10,1); skills geradas pelo próprio modelo, sem curadoria, não ajudaram. Por isso a skill nasce do seu método, curada e testada.
- [Vercel](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals): a skill não foi acionada em 56% dos casos e, sem instrução, rendeu o mesmo que não ter skill; com instrução explícita, chegou a 79%; com um índice no AGENTS.md, a 100%. Por isso a invocação é explícita e, nos repositórios de projeto, uma linha no AGENTS.md aponta para a skill.
- Os dois estudos medem tarefas de código com verificação objetiva, não ideação. Servem de direção; os testes desta skill confirmam ou não.

## 4. Plano da skill principal: `metodo-ideal`

### 4.1 Identidade

- **Nome:** `metodo-ideal` (minúsculas e hífen, igual ao nome da pasta, como pede a especificação).
- **Objetivo:** levar um propósito até o CIR, com o pacote da Etapa 2 e o estacionamento da Etapa 3, seguindo o IDEAL sem contaminação comercial ou tecnológica.
- **Usar quando:** idealizar a solução, o app, a ferramenta ou o estado ideal para um propósito, seja um problema ou uma aspiração; rodar, retomar ou revisar um passo; montar ou auditar um CIR; separar a ideia central do que já é produto.
- **Não usar para:** validar mercado, preço, MVP, roadmap, stack, PRD ou entrevistas de validação.
- **Compatibilidade** (campo `compatibility`): funciona melhor com subagentes e busca na web; sem eles, usa as alternativas da seção 4.6.
- **Rascunho da description** (até 1.024 caracteres; será otimizada nos testes de acionamento):

```
Conduz a concepção ideal de uma solução (Etapa 1 do fluxograma de criação de startups) pelo método IDEAL (Intenção, Diagnóstico, Exploração, Arquitetura, Lapidação), do propósito até o Conceito Ideal de Referência (CIR). Use quando a pessoa quiser idealizar a solução, o app, a ferramenta ou o estado ideal para um propósito (um problema ou uma aspiração) sem limitações comerciais, de mercado ou de tecnologia atual; quando pedir para rodar, retomar ou revisar um passo do IDEAL; montar ou auditar um CIR; ou separar a ideia central do que já é produto ou MVP. Também para pedidos em inglês como "ideal solution", "blue-sky concept", "idealized design" ou "design without constraints". Não use para validar mercado, definir preço, MVP, roadmap, stack ou PRD (Etapas 2 e 3).
```

### 4.2 Entradas e saídas

- **Entradas:** a ideia ou o propósito, em texto livre (pode chegar como solução pronta; a skill sobe pelo "para quê?"); documentos do projeto, se houver; o dossiê, para retomar; o prazo.
- **Saídas:** `dossie.md` (estado vivo); `cir.md` (as 17 seções do modelo); `pacote-etapa-2.md` (funções com métricas, casos canônicos, fronteiras técnicas, perguntas em aberto, princípios invariantes, restrições anti-ideais e alternativas vivas); `estacionamento-etapa-3.md` (com o motivo de cada exclusão).

### 4.3 Modos

| Modo | Quando | O que muda |
| --- | --- | --- |
| Completo (padrão) | Algo caro de construir ou difícil de reverter | Os 9 passos com gates, em várias sessões, com prazo definido no início |
| Retomar | Já existe dossiê | Lê o estado, mostra onde parou e propõe o próximo passo |
| Passo avulso | "Só a divergência", "só os casos canônicos" | Confere os pré-requisitos mínimos (propósito congelado, métricas) e avisa o que falta |
| Expresso | Experimento barato de testar no mercado | CIR v0 em uma sessão, tudo marcado como hipótese de baixa confiança, com a lista do que o rigor completo acrescentaria |
| Auditoria | Já existe um documento (PRD, pitch, CIR) | Separa trechos de Etapa 1, 2 e 3, aponta contaminação e lacunas do critério de pronto, como a seção 11 do v2 fez com o Motor de Insights |

O modo expresso segue o próprio v2: o rigor completo compensa quando a solução é cara de construir ou difícil de reverter, e não num experimento barato.

### 4.4 Fluxo por fase

| Fase e passos | A IA faz | Você faz | Gate: só avança com | Referência |
| --- | --- | --- | --- | --- |
| I — 1. Propósito, job e estado ideal | Entrevista com uma pergunta por vez; sobe pelo "para quê?"; propõe versões só depois das suas; procura palavras de produto ou tecnologia; mapeia quem executa, quem é afetado e quem tenta distorcer | Escreve as primeiras versões, escolhe uma e congela | Propósito único, sem palavra de produto, versões descartadas com motivo, sua aprovação | `fase-1-intencao.md` |
| D — 2. Anatomia e mapa de conhecimento; 3. Métricas e IFR | Monta o mapa do job com falhas e causas, contradições e o cenário "nada muda"; pesquisa o fenômeno com fontes; rotula fato, inferência e hipótese; propõe métricas; aplica o teste do impossível | Corrige o diagnóstico; valida métricas e linhas de base | 5 a 12 métricas com linha de base e limite ideal, incluindo custo de uso e dano; IFR aprovado no teste do impossível | `fase-2-diagnostico.md`, `fronteiras.md` |
| E — 4. Divergência; 5. Esboço integrado | Pede as suas ideias primeiro; gera famílias em paralelo com princípios diferentes; 70% meios e 30% tangentes; 20 a 30 ideias por rodada; registra tudo com a origem; escreve o esboço de 1 a 2 páginas com conflitos, sinergias e dependências | Gera ideias antes de ver as da IA; marca as que surpreendem | Pelo menos 3 famílias realmente diferentes; banco completo; esboço com conflitos | `fase-3-exploracao.md`, `divergencia.md` |
| A — 6. Abstração e triagem; 7. Arquitetura funcional | Pergunta "para que serve isso?" até chegar à função; propõe a classificação nos 5 tipos; calcula a taxa de surpresa e ajusta a fração de tangentes; decompõe as 2 ou 3 famílias em capacidades; escreve 3 a 5 cenários sem telas; manda o que for tecnologia para as fronteiras | Confirma ou corrige a triagem | Tudo classificado; anti-ideais e estacionamento com motivo; núcleo invariante; pelo menos 3 cenários | `fase-4-arquitetura.md` |
| L — 8. Prova conceitual; 9. Síntese | Ajuda a achar 10 a 20 casos reais com fonte, sem nunca inventar; faz pré-mortem e red team em contexto novo; monta a matriz +, 0, −, ? contra a melhor abordagem atual, sem somar; registra decisões com confiança; monta o CIR e os pacotes; roda o teste de passagem | Escreve a saída ideal dos casos (a IA sugere depois); decide o conceito de referência | Critério de pronto completo; nenhuma pergunta que só você responde pendente no teste de passagem | `fase-5-lapidacao.md`, `revisao-adversarial.md` |

### 4.5 Regras que valem em todos os passos

1. **Fronteiras do v2 (seção 3):** restrições comerciais e organizacionais ficam suspensas; tecnologia atual não filtra, vira fronteira técnica; regulação registra o conflito; lógica, ciência, natureza humana e valores são preservados.
2. **Função, não tela nem tecnologia; papéis, não personas.** Pedidos de produto são acolhidos e mandados para fronteiras ou estacionamento, sem discussão, e o passo continua. Redirecionar sem recusar mantém o ritmo e não perde a ideia.
3. **Rótulos de evidência:** fato (com fonte), inferência ou hipótese, e nível de confiança em toda decisão e diferencial. Nunca inventar dado, caso, estudo ou número: o CIR é a régua das próximas etapas, e um erro aqui se propaga.
4. **Você gera antes da IA** no propósito, na primeira rodada de ideias e nos casos canônicos. Pular é permitido e fica registrado. Motivo: ver ideias da IA antes aumenta a fixação e reduz a diversidade.
5. **Diversidade por construção:** gerações independentes com princípios e lentes diferentes, analogias próximas e distantes, ideias improváveis pedidas de forma explícita e a origem de cada ideia registrada. Motivo: modelos repetem a si mesmos e uns aos outros.
6. **Gerar e avaliar em contextos separados:** critérios antes da pontuação, avaliador sem saber quem gerou cada ideia e nenhuma escolha automática de vencedor: você decide. Motivo: modelos favorecem as próprias gerações.
7. **Sem bajulação:** apontar o que está fraco, manter discordâncias registradas, aceitar "aprovado" como resultado válido sem fabricar dúvida e declarar o que não foi possível avaliar.
8. **Entrevista:** uma pergunta por vez, perguntas abertas antes de opções e, a cada bloco, um resumo curto do entendimento, com os palpites marcados.
9. **Gates com aprovação explícita:** nenhuma fase avança sem a sua aprovação ou sem registrar que foi pulada.
10. **Tudo deixa rastro:** cada decisão registra contexto, opções, escolha, confiança e o que a reverteria. Nada se perde: o que sai vai para o estacionamento com motivo.
11. **Prazo e parada:** prazo de cada fase definido no início; uma rodada termina quando não traz família nova nem muda o CIR.
12. **Gate ético:** danos a terceiros, manipulação e uso duplo entram na conta da idealidade e no pré-mortem. Temas sensíveis, como saúde, eleições, crianças e finanças, recebem checagem extra.

### 4.6 Subagentes e alternativas

| Tarefa | Com subagentes (Codex, Claude Code, Notion AI) | Sem subagentes |
| --- | --- | --- |
| Divergência | 3 a 5 geradores em paralelo, cada um com um princípio ou lente e sem ver os outros; outro modelo, quando houver | Rodadas em sequência com lentes diferentes, sem reler as anteriores, avisando que a independência é menor |
| Red team e pré-mortem | Revisor novo com um brief autossuficiente (artefato, fronteiras e lentes), sem a conversa e sem a opinião da IA que gerou | Mensagem separada com papel explícito e a recomendação de repetir depois em outro modelo |
| Comparação de conceitos | Avaliador cego, sem saber a origem, com critérios fixados antes | Critérios fixados antes, matriz preenchida depois, e você revisa |
| Teste de passagem para a Etapa 2 | Agente novo lê só o pacote e tenta especificar a Etapa 2; cada pergunta dele vira "já respondida", "menor" ou "só você responde" | Checklist do pacote e as perguntas que um engenheiro faria |
| Pesquisa do fenômeno e de casos | Pesquisador com web, que entrega as fontes | Pede material a você e marca o que não foi verificado |

### 4.7 Dossiê entre sessões

- Toda sessão começa lendo o dossiê e termina atualizando-o com o que mudou, as decisões e o próximo passo.
- **Conteúdo:** propósito congelado (com as versões descartadas), prazo, fase atual e próxima ação; job, papéis e estado ideal; anatomia e mapa de conhecimento; métricas (direção, métrica, objeto, contexto, linha de base, limite ideal, tipo e confiança); IFR e teste do impossível; banco de ideias (família ou princípio, meio ou tangente, origem, rodada, tipo na triagem, destino e motivo); famílias vivas e eliminadas; capacidades e cenários; casos canônicos (fonte, desfecho, saída ideal, lados trocados); matriz de comparação; achados do pré-mortem e do red team; registro de decisões; fronteiras técnicas, estacionamento e perguntas em aberto; números do processo (ideias por rodada, famílias, taxa de surpresa, fração de tangentes).
- **No Codex:** pasta `ideal/<slug>/` no repositório do projeto. **No Notion:** uma página por CIR; banco de ideias e registro de decisões podem virar bancos de dados.

### 4.8 Estrutura de arquivos

```
metodo-ideal/
├── SKILL.md                    # até ~300 linhas: modos, regras, gates e quando ler cada referência
├── agents/openai.yaml          # opcional: metadados para o Codex
├── references/
│   ├── fronteiras.md           # restrições, teste do impossível, 5 tipos, sinais de contaminação
│   ├── fase-1-intencao.md      # passo 1
│   ├── fase-2-diagnostico.md   # passos 2 e 3
│   ├── fase-3-exploracao.md    # passos 4 e 5
│   ├── fase-4-arquitetura.md   # passos 6 e 7
│   ├── fase-5-lapidacao.md     # passos 8 e 9
│   ├── divergencia.md          # módulo: protocolo contra homogeneização e técnicas
│   ├── revisao-adversarial.md  # módulo: red team, pré-mortem e teste de passagem
│   └── exemplos.md             # trechos limpos × contaminados (Motor de Insights, JEV)
├── assets/
│   ├── dossie.md
│   ├── cir.md                  # as 17 seções
│   ├── pacote-etapa-2.md
│   ├── estacionamento-etapa-3.md
│   └── briefs/                 # gerador, red team, pré-mortem, teste de passagem
├── scripts/                    # opcionais e determinísticos
│   ├── check_pronto.py         # contagens do critério de pronto
│   └── lint_contaminacao.py    # sinaliza termos de produto, mercado e tecnologia para revisão
└── evals/                      # fica no Git; não vai para o Notion
    ├── evals.json
    ├── gatilhos.json
    └── fixtures/               # dossiês prontos até o passo N
```

Cada referência abre com a interface (o que recebe, o que devolve e quando parar) e fecha com anti-padrões no formato "erro → correção". Os scripts só sinalizam; a skill funciona sem eles.

**De onde sai cada parte:**

| No v2 | Vai para |
| --- | --- |
| §4 Princípios; Esforço, prazo e parada | `SKILL.md` (regras, modos e parada) |
| §3 Fronteiras; sinais de contaminação (§9) | `references/fronteiras.md` |
| §5 Passos 1 a 9 e o passo a passo | `references/fase-*.md` |
| §8 Modelo do CIR | `assets/cir.md` |
| §9 Critério de pronto | Gates no `SKILL.md` e `scripts/check_pronto.py` |
| §11 Motor de Insights e JEV | `references/exemplos.md` e fixtures dos testes |
| §2, §6, §7, §10 e §12 a §14 (fundamentos, simulação, evidências, referências) | Ficam no Notion como documentação; não são carregados durante o uso |

### 4.9 Casos-limite

- **Chega com a solução pronta** ("quero um app que…"): subir pelo "para quê?" até o propósito; a solução vira a primeira ideia do banco.
- **Propósito que é aspiração, não problema** (ex.: tornar um reencontro inesquecível): a anatomia olha o que separa o hoje do estado ideal, e as falhas viram lacunas para o ideal.
- **Dois propósitos:** separar em dois CIRs e escolher por qual começar.
- **O propósito muda no meio:** registrar, avaliar o impacto e decidir com você de qual passo recomeçar.
- **Não há casos canônicos reais** (algo inédito): usar casos análogos reais, rotulados e com confiança menor. Caso inventado nunca é apresentado como real.
- **Pedido de preço, stack ou MVP:** acolher, registrar no estacionamento ou nas fronteiras e voltar ao passo.
- **Pedido para pular um gate:** permitido, registrado como decisão, com o risco.
- **Tema sensível:** gate ético reforçado e o papel "quem tenta distorcer" obrigatório.
- **Sessão interrompida:** o dossiê é salvo ao fim de cada bloco, não só no fim da sessão.

### 4.10 Fora do escopo

Etapa 2 (tecnologia, arquitetura técnica, MOPs e TPMs), Etapa 3 (mercado, cliente, preço, MVP, roadmap, PRD), validação com usuários e código.

### 4.11 Adaptação para o Notion

| No master | No Notion |
| --- | --- |
| `name` e `description` | Propriedades Skill name e Description no banco de Skills |
| Corpo do `SKILL.md` | Corpo da página da skill |
| `references/*.md` | Subpáginas, com um nível de profundidade |
| `assets/` e `scripts/` | Files (e modelos como subpáginas, se preferir) |
| Pasta do dossiê | Uma página por CIR; banco de ideias e decisões como bancos de dados, se quiser |
| Subagentes | Sessões do Notion AI, inclusive com modelos diferentes para o red team e o avaliador cego |
| `evals/` | Ficam no Git e são rodados com o guia de testes do skill-creator |

## 5. Módulos que viram skills na v2

| Módulo → skill futura | O que faz | Entradas | Saída | Reuso |
| --- | --- | --- | --- | --- |
| `divergencia` → `ideacao-divergente` | Gera alternativas realmente diferentes para um "como poderíamos…" e mostra a diversidade; não julga valor | Alvo (propósito, função ou contradição), fronteiras da etapa, número de famílias, ideias suas | Banco de ideias por família, com origem e relatório de diversidade | Etapa 1, passo 4; Etapa 2 (alternativas técnicas); Etapa 3 (modelos de negócio, canais) |
| `revisao-adversarial` → `revisao-adversarial` | Ataca um artefato em contexto novo: afirmações que sustentam tudo, steelman antes do ataque, "falha se…", tigres, tigres de papel e elefantes, ranking por impacto × probabilidade × custo de checar, o que está sólido e o que não foi possível avaliar | Artefato, lentes da etapa, modo (red team, pré-mortem, teste de passagem) | Relatório padronizado e itens para o registro de decisões | Todas as etapas (na 1: fenômeno, lógica, natureza humana e danos; na 3: mercado) |

**Quando promover:** quando a skill da Etapa 2 ou 3 for planejada e os testes da v1 mostrarem que o módulo funciona. A skill principal passa a usar a skill separada quando ela existir e mantém a referência como alternativa. O texto continua com uma fonte só, copiada por script.

## 6. Pesquisa: skills avaliadas

<aside>
🔎

Como foi avaliado: leitura do conteúdo (não só do nome e da descrição), autoria, manutenção, testes e licença. Nenhuma skill encontrada tem eficácia comprovada de forma independente; estrelas medem popularidade. A evidência que existe é a dos métodos por trás delas (pré-mortem, geração individual antes da coletiva, analogias, templates) e a dos estudos gerais sobre skills. Por isso o plano aproveita mecanismos em vez de instalar skills prontas, e reescreve em vez de copiar.

</aside>

### 6.1 Úteis nesta etapa, para qualquer projeto

| Skill | O que aproveitar | Fonte e evidência | Veredito |
| --- | --- | --- | --- |
| [brainstorming](https://github.com/obra/superpowers/tree/HEAD/skills/brainstorming) (superpowers) | Uma pergunta por mensagem; perguntas abertas antes de opções, porque opções direcionam; pensar amplo antes de perguntar; resumos curtos com palpites marcados; documento revisado por um subagente novo que separa as perguntas em "já respondida", "menor" e "do usuário"; bloqueio duro antes de construir; tabela de sinais de alerta | Jesse Vincent, MIT, ~302 mil ★; testes de comportamento por ambiente, mas nenhum estudo de eficácia | **Adaptar o processo** (o conteúdo é de software) |
| [writing-skills](https://github.com/obra/superpowers/tree/HEAD/skills/writing-skills) (superpowers) | TDD para skills: ver o agente falhar sem a skill antes de escrevê-la | Idem | **Usar na criação**, junto com o skill-creator |
| [scientific-brainstorming](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/scientific-brainstorming) (K-Dense) | Rótulos (ideia, suposição, previsão, evidência, decisão); geração humana independente antes de mostrar ideias de IA; preservar opinião minoritária; critérios antes da pontuação; pesquisa depois da 1ª rodada, reabrindo a ideação; nada de vencedor automático; revisão por quem não gerou; gates de ética e uso duplo; lista de vieses (homogeneização, fixação, convergência prematura, falsa precisão) | K-Dense, MIT, v1.4 revisada em out/2026, com scripts de validação; regras coerentes com a pesquisa sobre criatividade em grupo; sem avaliação publicada da skill | **Principal referência de rigor** |
| [product-brainstorming](https://github.com/anthropics/knowledge-work-plugins/tree/HEAD/product-management/skills/product-brainstorming) (Anthropic) | Sessão enquadrar → divergir → provocar → convergir → registrar (inclusive o que ficou de fora); HMW, primeiros princípios, SCAMPER, brainstorming reverso; anti-padrões | Oficial, Apache 2.0; sem avaliação publicada; mistura viabilidade e negócio | **Adaptar a estrutura**, sem os critérios de viabilidade |
| [creative-thinking-for-research](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/21-research-ideation/creative-thinking-for-research) (Orchestra Research) | 8 operadores: bisociação, reformulação, analogia estrutural, manipulação de restrições, inversão, escada de abstração, adjacente possível, pensamento janusiano | MIT, ~13,8 mil ★; operadores da ciência cognitiva (Koestler, Gentner, Boden); a skill não foi testada | **Adaptar** para o catálogo do passo 4 |
| [strategy-red-team](https://github.com/phuryn/pm-skills/tree/HEAD/pm-execution/skills/strategy-red-team) e [pre-mortem](https://github.com/phuryn/pm-skills/tree/HEAD/pm-execution/skills/pre-mortem) (pm-skills) | Extrair as afirmações que sustentam tudo; steelman antes do ataque; "falha se…"; ranking; não fabricar dúvida; dizer o que não deu para avaliar; modo com outro modelo; tigres, tigres de papel e elefantes | Paweł Huryn, MIT, ~27 mil ★; testes só de estrutura; o pré-mortem tem base empírica | **Adaptar** para o passo 8, trocando mercado por fenômeno, casos e idealidade |
| [grill-me](https://github.com/mattpocock/skills/tree/HEAD/skills/productivity/grill-me) (Matt Pocock) | Entrevista insistente que resolve cada ramo da árvore de decisões | MIT, 7 linhas; sem avaliação | **Adotar a ideia** nos passos 1 a 3 |
| [doc-coauthoring](https://github.com/anthropics/skills/tree/HEAD/skills/doc-coauthoring) (Anthropic) | Teste de leitor: uma instância nova lê o documento sem contexto | Oficial; sem avaliação publicada | **Adotar** no teste de passagem |
| [founder-skill](https://github.com/Jakeschincariol/founder-skill) | Arquivo de estado compartilhado; brief autossuficiente para subagentes ("eles não veem a conversa; não inclua sua opinião"); lentes em paralelo; discordâncias mantidas; "sem fatos inventados"; "PASS é resultado" | MIT, criado em out/2026; testes só dos scripts; conteúdo de mercado (conselho, painel de 100 compradores sintéticos, preço), e respondentes sintéticos têm validade limitada | **Padrões sim, conteúdo não**: contamina a Etapa 1 |
| [wondelai/skills](https://github.com/wondelai/skills) (metaskills e [good-strategy-bad-strategy](https://github.com/wondelai/skills/tree/HEAD/good-strategy-bad-strategy)) | Estado salvo em `docs/` entre sessões; o núcleo de Rumelt (diagnóstico → política → ações) como checagem do diagnóstico | MIT; 51 skills baseadas em livros; sem avaliação | **Padrão de estado**; Rumelt opcional no passo 2 |
| [problem-framing-canvas](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/problem-framing-canvas) e [autonomous-investigation](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/autonomous-investigation) (Dean Peters) | Enquadramento do problema (MITRE); rótulos fato, inferência e suposição, com confiança | Licença CC BY-NC-SA 4.0 (não comercial) | **Só inspiração**, sem copiar texto |
| [product-skills](https://github.com/wdavidturner/product-skills) (David Turner) | Formato "erro → correção" nas referências; alerta contra JTBD "de sala de reunião" (job imaginado, sem observação) | MIT, 21 ★, parado desde jan/2026 | **Formato** para os anti-padrões |
| [office-hours](https://github.com/garrytan/gstack/tree/HEAD/office-hours) e [plan-ceo-review](https://github.com/garrytan/gstack/tree/HEAD/plan-ceo-review) (gstack) | Experiência de 10 ou 11 estrelas e expansão de escopo | MIT; ~1.300 linhas cada, muito acima do recomendado; viés de software e YC | **Só a ideia** do 11 estrelas |

### 6.2 Úteis conforme o tipo de projeto

| Tipo de projeto | Skills | Como usar sem limitar a criatividade |
| --- | --- | --- |
| Software e plataformas | wondelai [architecture-optimization](https://github.com/wondelai/skills/tree/HEAD/architecture-optimization), [system-design](https://github.com/wondelai/skills/tree/HEAD/system-design), [ddia-systems](https://github.com/wondelai/skills/tree/HEAD/ddia-systems), [clean-architecture](https://github.com/wondelai/skills/tree/HEAD/clean-architecture); Anthropic [system-design](https://github.com/anthropics/knowledge-work-plugins/tree/HEAD/engineering/skills/system-design) | Etapa 2. Na Etapa 1, só os limites de princípio (ex.: teorema CAP, complexidade computacional) entram como restrições preservadas no teste do impossível; padrões de arquitetura nunca filtram ideias |
| Sites, apps e interfaces | Anthropic [frontend-design](https://github.com/anthropics/skills/tree/HEAD/skills/frontend-design); wondelai [top-design](https://github.com/wondelai/skills/tree/HEAD/top-design), [refactoring-ui](https://github.com/wondelai/skills/tree/HEAD/refactoring-ui), [ux-heuristics](https://github.com/wondelai/skills/tree/HEAD/ux-heuristics), [web-typography](https://github.com/wondelai/skills/tree/HEAD/web-typography) | Etapa 3 em diante. Na Etapa 1 a experiência entra como função; [design-everyday-things](https://github.com/wondelai/skills/tree/HEAD/design-everyday-things) ajuda na parte de natureza humana (lacunas de execução e de avaliação), sem desenhar interface |
| Ciência, saúde e deep tech | K-Dense [hypothesis-generation](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/hypothesis-generation), [scientific-critical-thinking](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/scientific-critical-thinking), [literature-review](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/literature-review) | Etapa 1, passos 2, 3 e 8: mapa de conhecimento, hipóteses falsificáveis e limites físicos ou biológicos |
| Produtos de IA e apoio à decisão | Lenny [ai-evals](https://github.com/refoundai/lenny-skills/tree/HEAD/skills/ai-evals) | Os casos canônicos já funcionam como evals; a escolha de modelo fica para a Etapa 2 |
| Hábito, saúde e educação (a parte humana pesa muito) | David Turner [hooked-model](https://github.com/wdavidturner/product-skills/tree/HEAD/skills/hooked-model); wondelai [drive-motivation](https://github.com/wondelai/skills/tree/HEAD/drive-motivation) e design-everyday-things | Na Etapa 1, só como mecanismos de comportamento avaliados contra os valores (manipulação é restrição preservada); táticas de engajamento ficam para a Etapa 3, com gate ético |
| Físico, hardware e operações | Nenhuma skill madura encontrada; usar o TRIZ do próprio método (contradições, recursos, efeitos) | Etapa 1 com TRIZ; fabricação e custos na Etapa 2 |
| Cívico, regulado ou sensível | Gates de ética e uso duplo do scientific-brainstorming; Value Sensitive Design e consequence scanning (seção 7) | Etapa 1, passos 1 e 8 |
| Negócio e mercado (qualquer projeto) | founder-*, lean canvas, pricing e market sizing (pm-skills), evaluating-startup-ideas e idea-validation (Lenny), lean-startup, mom-test, monetizing-innovation e blue-ocean-strategy (wondelai) | **Etapa 3.** Na Etapa 1, contaminam |

**Descartadas para esta etapa:** brainstorm-ideas-new (pm-skills) e product-vision (pm-skills e Lenny), porque priorizam o que é rápido de validar ou "alcançável"; [claude-skills](https://github.com/alirezarezvani/claude-skills) (854 skills, maioria de negócio e C-level); [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills), que é um diretório útil para descobrir skills, não para usar.

## 7. Conceitos renomados que complementam o método

Já estão no v2: idealized design, TRIZ, JTBD e ODI, OST, Working Backwards, mapa de premissas, pré-mortem, teoria C–K, Pahl & Beitz, Axiomatic Design, ConOps, matriz morfológica, matriz de Pugh, set-based design e ADR. Estes complementam:

| Conceito (origem) | O que acrescenta | Onde entra | Evidência |
| --- | --- | --- | --- |
| Pensamento Inventivo Sistemático, SIT (Goldenberg, Mazursky e Solomon) | 5 operadores (subtração, multiplicação, divisão, unificação de tarefa, dependência de atributo) e o "mundo fechado" | Passo 4, como gerador, nunca como filtro | Média: [estudo na Science (1999)](https://www.science.org/doi/10.1126/science.285.5433.1495) com padrões recorrentes em produtos de sucesso e ideias por template mais bem avaliadas que as de livre associação |
| Geração individual antes da coletiva (brainwriting, grupo nominal; Diehl e Stroebe) | Ideias independentes antes de juntar | Regra 4 e geração paralela | Alta: a perda de produtividade dos grupos interativos se repete em meta-análises |
| Analogia por propósito e mecanismo (Kittur et al.; Chan, Dow e Schunn; Fu et al.) | Buscar analogias pela função e misturar distâncias | Passo 4 | Média: em experimentos, [fontes próximas renderam mais que as distantes](https://www.sciencedirect.com/science/article/abs/pii/S0142694X14000611) |
| Dissenso autêntico e inquérito dialético (Nemeth; Schweiger) | Crítica de quem parte de outras premissas vale mais que advogado do diabo encenado | Red team em contexto novo ou com outro modelo | Média: [experimentos](https://onlinelibrary.wiley.com/doi/10.1002/ejsp.58) de laboratório |
| Retrospectiva prospectiva (Mitchell, Russo e Pennington) | Base do pré-mortem que o método já usa | Passo 8 | Média: [imaginar que o evento já aconteceu gerou mais explicações](https://onlinelibrary.wiley.com/doi/10.1002/bdm.3960020103) |
| Experiência de 11 estrelas (Brian Chesky) | Escalar o estado ideal até o absurdo e voltar | Passos 1 e 4 | Baixa: relato de prática |
| Análise funcional FAST e engenharia de valor (Miles; Bytheway) | Funções em verbo + substantivo, com a lógica "como?" e "por quê?" nos dois sentidos | Passos 6 e 7 | Média-baixa: prática industrial consolidada, poucos estudos controlados |
| Teoria da mudança e impact mapping (Weiss; Adzic) | Cadeia explícita do propósito até as mudanças de comportamento, com premissas | Passo 2, quando a parte humana pesa (H1 do v2) | Baixa a média: muito usada em avaliação de programas |
| Pontos de alavancagem (Meadows) | Níveis de intervenção (parâmetros, fluxos, regras, metas, paradigma) para gerar famílias em níveis diferentes | Passo 4 | Baixa: conceitual |
| Value Sensitive Design (Friedman) e consequence scanning (Doteveryone) | Partes afetadas diretas e indiretas, valores em conflito, consequências não intencionais | Passos 1 e 8 | Média-baixa: literatura de método ampla |
| Provocação "Po" e Seis Chapéus (de Bono) | Operadores de provocação; separar modos de pensar | Passo 4, nas tangentes | Baixa: evidência fraca e mista |
| Cynefin (Snowden) | Classifica o fenômeno (claro, complicado, complexo, caótico) e o que dá para saber | Passo 2, no mapa de conhecimento | Baixa: conceitual |

**Ficam para outras etapas:** Kano, Blue Ocean (ERRC), Value Proposition Canvas, Lean Canvas e os testes com usuário do Design Sprint (Etapa 3); Wardley, QFD e DSM (Etapa 2).

## 8. O que a pesquisa diz sobre IA na ideação

| Achado | Fonte | Implicação na skill |
| --- | --- | --- |
| Ideias do GPT-4 foram menos diversas que as de grupos humanos; cadeia de raciocínio e personas reduziram a diferença | [Meincke, Mollick e Terwiesch, 2024](https://arxiv.org/abs/2402.01727) | Gerar com raciocínio explícito e lentes diferentes |
| Modelos repetem a si mesmos e se parecem entre si | [Artificial Hivemind, NeurIPS 2025](https://arxiv.org/abs/2510.22954) | Geradores independentes, outro modelo quando houver e diversidade medida |
| Pedir várias respostas com probabilidades aumentou a diversidade de 1,6 a 2,1 vezes em escrita criativa | [Verbalized Sampling, 2025](https://arxiv.org/abs/2510.01171) | Pedir N ideias com probabilidade e incluir as improváveis |
| IA aumenta a criatividade individual e reduz a diversidade coletiva | [Doshi e Hauser, Science Advances, 2024](https://www.science.org/doi/10.1126/sciadv.adn5290) | Você gera primeiro; o banco registra a origem |
| Ver imagens geradas por IA aumentou a fixação em ideação visual | [Wadinambiarachchi et al., CHI 2024](https://arxiv.org/abs/2403.11164) | Idem |
| Ideias de LLM foram julgadas mais novas e um pouco menos factíveis que as de especialistas; a autoavaliação do modelo falhou | [Si, Yang e Hashimoto, ICLR 2025](https://arxiv.org/abs/2409.04109) | Novidade é o ponto forte da IA na Etapa 1; o gerador nunca avalia a si mesmo |
| Avaliadores LLM preferem as próprias gerações | [Panickssery et al., NeurIPS 2024](https://arxiv.org/abs/2404.13076) | Avaliação cega, em contexto novo, de preferência com outro modelo |

## 9. Plano de testes

**Condições** (pelo menos 3 execuções de cada, porque o resultado varia):

- **A — sem skill**, como linha de base.
- **B — método colado no prompt** (passo a passo + v2), para saber se a skill acrescenta algo além do conteúdo.
- **C — com a skill.**

**Ambientes:** Codex (principal) e Notion AI (adaptação); Claude Code ou ChatGPT, se quiser. Os resultados são revisados no visualizador do skill-creator e numa leitura cega sua.

**Ordem:** primeiro rodar A e B e anotar as falhas típicas (a fase "vermelha" do TDD); depois escrever a skill para corrigir essas falhas.

### 9.1 Casos

| Caso | Tipo | O que testa |
| --- | --- | --- |
| Motor de Insights | Apoio à decisão (parte humana pesa ~40%) | Caso real, com gabarito parcial no v2 (§11 e JEV) |
| Manter um hábito de exercício | Hábito e saúde (~70%) | Natureza humana, anti-ideais de engajamento, gate ético |
| Água tratada chegando sem perdas a uma cidade | Físico, máquina para máquina (~5%) | Fora de software, TRIZ, leis físicas no teste do impossível |
| Tornar um reencontro de amigos inesquecível | Aspiração, não problema | Propósito sem "dor" |
| Informar eleitores sobre candidatos | Cívico e sensível | Uso duplo, quem tenta distorcer, manipulação |
| Auditoria do documento do Motor de Insights v1 | Modo auditoria | Concordância com a separação por etapa feita no §11 do v2 |

**Testes de robustez** (falas suas durante a sessão): pedir preço, stack ou MVP; mudar o propósito; pedir dados inventados; dar uma ideia só; pedir para pular um gate; trazer dois propósitos.

**Testes por passo:** dossiês prontos até o passo N (fixtures) para testar o passo seguinte isoladamente.

### 9.2 Métricas e alvos (proposta para a v1)

| Métrica | Como medir | Alvo |
| --- | --- | --- |
| Aderência ao método | Asserções por passo + `check_pronto.py` | ≥ 90% das asserções |
| Contaminação | Lint + revisão: termos e decisões de Etapa 2 ou 3 no CIR, fora das fronteiras e do estacionamento | Zero no CIR final |
| Fabricação | Fatos, casos e números sem fonte apresentados como fato | Zero |
| Diversidade | Famílias com princípio distinto; ideias ausentes nas condições A e B; julgamento cego de "princípio diferente?" | ≥ 3 famílias e mais variedade que A e B |
| Triagem | Concordância com a sua classificação nos 5 tipos | ≥ 80% |
| Qualidade | Comparação cega C × A e C × B, por você e por um avaliador de outro modelo | C vence A em ≥ 70% e vence B |
| Passagem | Perguntas "só você responde" no teste de passagem | Caem a cada versão |
| Custo | Tokens, tempo e turnos | Registrar; expresso em 1 sessão |
| Acionamento | ~20 consultas por ambiente: metade deve acionar, metade são quase-acertos que não devem | ≥ 80% de acerto e ≤ 10% de falso positivo |

## 10. Roadmap

| Fase | Entrega | Onde | Pronto quando |
| --- | --- | --- | --- |
| 0. Decisões | Respostas da seção 13 | Notion | Você aprova |
| 1. Linha de base | Casos rodados nas condições A e B, com as falhas típicas anotadas | Codex | 6 casos × 2 condições |
| 2. v0.1 | `SKILL.md`, referências, modelos e briefs | Codex, com os skill-creators da Anthropic e do Codex | Formato validado e texto revisado por você |
| 3. Testes 1 | Testes por passo e casos completos | Codex | Relatório no visualizador |
| 4. v1.0 | Iterações até os alvos; description otimizada | Codex | Alvos da seção 9 atingidos |
| 5. Adaptação | Página no banco de Skills, subpáginas, Files, dossiê como página | Notion AI + seu skill-creator | Testes repetidos no Notion |
| 6. Testes cruzados | Mesmos testes no Codex e no Notion (opcional: Claude Code e ChatGPT) | Ambos | Diferenças registradas no campo `compatibility` |
| 7. Uso real | Um CIR novo, de ponta a ponta | Notion ou Codex | Retrospectiva vira a v1.1 |
| 8. Skills separadas | `ideacao-divergente` e `revisao-adversarial` | Codex | Quando a Etapa 2 ou 3 for planejada |

## 11. Riscos

| Risco | Mitigação |
| --- | --- |
| Processo pesado demais, abandono no meio | Modos expresso e passo avulso; parada por rodada |
| IA homogênea ou bajuladora | Regras 4 a 7, outro modelo no red team, diversidade medida |
| Contaminação pela tendência da IA de falar de MVP e stack | Fronteiras, lint, exemplos limpos × contaminados, testes de robustez |
| Casos canônicos inventados | Regra de fonte; você fornece ou aprova; o que não foi verificado é marcado |
| Skill não acionada | Invocação explícita, linha no AGENTS.md, description otimizada |
| Diferenças entre ambientes | Alternativas sem subagentes e sem web; campo `compatibility`; testes cruzados |
| Master e versão do Notion divergirem | Fonte única no Git, CHANGELOG, checklist de adaptação |
| Perda de estado entre sessões | Dossiê lido no início e salvo ao fim de cada bloco |
| Criatividade é difícil de medir | Comparação cega, sua avaliação e métricas objetivas parciais |
| Números da simulação do v2 tomados como fatos | Tratar como heurística, como o próprio v2 avisa, e ajustar com os dados dos testes |

## 12. Ajustes sugeridos ao método

1. **Passo 4:** trocar "analogias distantes" por analogias próximas, moderadas e distantes, buscadas pela função (Chan; Fu; Kittur).
2. **Passo 4:** incluir os operadores do SIT e os níveis de Meadows como geradores de famílias.
3. **Passos 1, 4 e 8:** você gera antes da IA, e o banco de ideias registra a origem de cada ideia.
4. **Passo 8:** red team em contexto novo e, se possível, com outro modelo.
5. **Passo 3:** deixar explícitas no teste do impossível as leis do domínio (físicas, lógicas e cognitivas).
6. **Passos 1 e 8:** incluir partes afetadas indiretamente e consequências não intencionais (Value Sensitive Design, consequence scanning).

## 13. Decisões em aberto

- [ ]  Construir no Codex (recomendado) ou você já usa Claude Code ou Cowork?
- [ ]  O nome `metodo-ideal` está bom?
- [ ]  v1 com uma skill e módulos internos (recomendado) ou três skills desde já?
- [ ]  Papel padrão da IA: facilitadora que pergunta e rascunha, com você decidindo nos gates (recomendado), ou coautora que entrega rascunhos completos para revisão?
- [ ]  "Você gera antes da IA" fica obrigatório, com opção de pular registrada (recomendado), ou opcional?
- [ ]  Onde fica o dossiê: `ideal/<slug>/` no repositório do projeto e, no Notion, uma página por CIR ou bancos de dados?
- [ ]  O modo expresso deve existir?
- [ ]  Os casos de teste da seção 9 servem? Dá para montar um gabarito de triagem do Motor de Insights (cerca de 30 elementos)?
- [ ]  Incorporar ao v2 os ajustes da seção 12?
- [ ]  Precisa de versão em inglês?

[Fluxograma aperfeiçoado — Etapa 1 (CIR)](Plano%20da%20skill%20%E2%80%94%20Etapa%201%20(m%C3%A9todo%20IDEAL)/Fluxograma%20aperfei%C3%A7oado%20%E2%80%94%20Etapa%201%20(CIR)%20fb9015a39bb1406481763a2903aca006.md)

[Fluxograma completo — Etapa 1 (método IDEAL em ciclo)](Plano%20da%20skill%20%E2%80%94%20Etapa%201%20(m%C3%A9todo%20IDEAL)/Fluxograma%20completo%20%E2%80%94%20Etapa%201%20(m%C3%A9todo%20IDEAL%20em%20cic%20f1f71e3bd5e6487ebdfc94cd7e9fa161.md)

[Plano geral das skills — Etapa 1 (CIR)](Plano%20da%20skill%20%E2%80%94%20Etapa%201%20(m%C3%A9todo%20IDEAL)/Plano%20geral%20das%20skills%20%E2%80%94%20Etapa%201%20(CIR)%2072d0fdc1db19433e9101d1ac3b3015ef.md)