# Plano detalhado — conselho-especialistas

<aside>
⚖️

**O que é:** o plano detalhado do `conselho-especialistas`, a skill que julga. Entra na triagem (passo 3) e na validação (passo 8) de cada sub-etapa do [Fluxograma completo — Etapa 1 (método IDEAL em ciclo)](https://app.notion.com/p/Fluxograma-completo-Etapa-1-m-todo-IDEAL-em-ciclo-f1f71e3bd5e6487ebdfc94cd7e9fa161?pvs=21), nas validações integradas e sempre que você pedir um conselho. É o segundo plano da ordem da seção 15 do [Plano geral das skills — Etapa 1 (CIR)](https://app.notion.com/p/Plano-geral-das-skills-Etapa-1-CIR-72d0fdc1db19433e9101d1ac3b3015ef?pvs=21) e inclui o adaptador e o mapa de modelos. Segue os formatos definidos no [Plano detalhado — etapa-1-cir (condutora)](https://app.notion.com/p/Plano-detalhado-etapa-1-cir-condutora-fccda0c36a5d403582b433a6f2b0657f?pvs=21).

**Notion primeiro, conteúdo universal:** o protocolo, as óticas, os templates e os formatos valem em qualquer agente. O que muda de uma ferramenta para outra fica no adaptador (seção 9).

</aside>

## 1. Propósito no fluxograma

**Propósito:** validar qualquer coisa, antes ou depois de definida, com julgamento independente, às cegas e apoiado em pesquisa de refutação, preservando o dissenso.

| Responde por | Como se vê |
| --- | --- |
| Independência | Na rodada 1, nenhum membro vê os outros, a autoria nem a preferência de ninguém; a ordem das hipóteses é sorteada para cada membro |
| Diversidade | Membros de famílias de modelos diferentes, de qualidade parecida, cada um com uma ótica |
| Refutação com lastro | Cada veredito vem critério a critério, com fonte ou raciocínio verificável e o que o mudaria |
| Dissenso preservado | Matriz sem soma e sem vencedor; a posição minoritária aparece com o seu melhor argumento |
| Rastreabilidade | Painel, briefs, vereditos, crítica, matriz e custos ficam gravados no dossiê |
| Aprendizado | O placar guarda cada veredito, para conferir depois quais óticas, especialidades e modelos acertam mais |
- **Não decide.** Quem decide é você; o conselho mostra onde cada hipótese resiste e onde cai.
- **Não elabora nem gera alternativas,** e não conversa antes do veredito. O que exige combinar especialidades chega pelo parecer da equipe de verificação.
- **Não faz a pesquisa do zero:** cada membro usa a `pesquisa-cientifica` no modo refutar.
- **Pronto quando:** todos os membros previstos entregaram, ou a falta ficou registrada; o crítico revisou; a matriz e a síntese estão gravadas; a chave de autoria continua fora dos briefs; e o placar foi atualizado.

## 2. Skills de base e o que se aproveita

| Base | O que se aproveita | O que é nosso | Licença |
| --- | --- | --- | --- |
| [llm-council](https://github.com/karpathy/llm-council) (Karpathy) | Três estágios: opiniões independentes, revisão anônima entre os modelos e um presidente que compila a resposta | Critérios com "refuta se" no lugar do ranking por "acerto e insight"; revisão só com divergência, mudando de posição só com evidência nova; um relator que não decide, no lugar do presidente | Sem licença: só a ideia |
| [claude-council](https://github.com/hex/claude-council) (hex) | Chamadas em paralelo a vários CLIs, com nova tentativa por assento; papéis de especialista; conselho só com subagentes Claude quando não há outro provedor; síntese que nomeia a premissa que mudaria a resposta | Adaptador do Notion, protocolo às cegas, matriz por critério, templates e placar | MIT; ativo em outubro de 2026 |
| Fluxograma completo (2.4) e v2 (seção 6) | Conselhos, templates, óticas, rodadas e placar | — | Nosso |

**Três achados que mudam o desenho:**

1. **Nenhuma base julga às cegas, por critério escrito antes, com pesquisa para refutar.** Todas comparam respostas a uma pergunta aberta. O protocolo é nosso; das bases vêm o transporte e o formato da síntese.
2. **Concordância não é verificação.** Os modelos partem da mesma descrição e das mesmas premissas, como o próprio claude-council avisa, e modelos diferentes já respondem parecido ([Artificial Hivemind](https://arxiv.org/abs/2510.22954)). Por isso cada membro pesquisa para derrubar, e um "+" precisa de lastro.
3. **O ganho vem das opiniões independentes.** O debate rende pouco além do voto ([Choi, Zhu e Li](https://arxiv.org/abs/2508.17536)) e pode fazer modelos trocarem a resposta certa pela errada para concordar ([Talk Isn't Always Cheap](https://arxiv.org/abs/2509.05396)). Daí uma troca só, sem autoria, e só quando há divergência.

## 3. Acionamento

```yaml
---
name: conselho-especialistas
description: >-
  Reúne um conselho de modelos de famílias diferentes para julgar hipóteses,
  decisões ou documentos às cegas, critério a critério, com pesquisa para
  refutar, crítico de outra família e dissenso preservado, sem média nem
  vencedor. Use quando a condutora da Etapa 1 pedir triagem, validação ou
  validação integrada, ou quando o usuário pedir que um conselho avalie,
  teste ou tente derrubar uma ideia, hipótese, decisão ou documento. Não use
  para gerar ideias, elaborar uma versão, fazer brainstorm, resumir opiniões
  ou decidir pelo usuário.
license: (a definir)
compatibility: Notion ou Claude Code; Python 3 no computador do agente
metadata:
  versao: "0.1"
---
```

- **Só os campos do padrão aberto,** como na condutora.
- **Chamada pelo nome é o caminho principal:** "Use a skill `conselho-especialistas`, conselho rápido, template Evidência, com este brief." Fora da Etapa 1, a skill roda avulsa (seção 5.4).

| Deve acionar | Não deve acionar (quase acertos) |
| --- | --- |
| "Pede ao conselho para tentar derrubar o propósito congelado." | "Me dá 10 ideias para o propósito." |
| "Quero que modelos diferentes julguem estas três arquiteturas." | "Resume o que os especialistas disseram na reunião." |
| "Valida às cegas H1, H2 e H3 com o template Evidência." | "Melhora o texto desta hipótese." |
| "Faz a triagem de falha fatal destas ideias." | "Faz uma pesquisa sobre o estado da arte de X." |
| "Monta um conselho sobre esta decisão." | "Qual dessas você prefere?" (a condutora não opina e oferece o conselho) |
| "O conselho concorda com a minha classificação dos elementos?" | "Conversa com o GPT sobre isso." |

A lista completa, com 10 de cada lado, entra nos testes (seção 14).

## 4. Contrato de entrada e saída

| Entrada | De quem | Forma |
| --- | --- | --- |
| Brief do conselho | Condutora | O envelope comum do plano da condutora (seção 9), com os campos da seção 8 deste plano |
| Hipóteses sem autoria | Condutora, já anonimizadas | Cartões de hipótese num formato fixo, com rótulos aleatórios |
| Critérios e "refuta se" | Cartão da sub-etapa | Escritos antes de o conselho ver as hipóteses |
| Parecer de verificação | `equipe-especialistas` | Afirmação verificada, cálculos, fontes, conclusão e incerteza, sem autoria |
| Fichas de fonte já conferidas | Dossiê, pela condutora | Só as relevantes |
| Mapa de modelos e restrições | `estado.json` | Famílias autorizadas, modelos e o que não pode sair para cada uma |
| Pedido avulso | Você | Pergunta em texto livre; a skill monta o brief com você |

| Saída | Para quem | Onde |
| --- | --- | --- |
| Pacote: matriz, síntese, vereditos, crítica e alertas | Condutora, que mostra a você | `conselho/<id>/` |
| Resumo curto, de umas 300 palavras, e os caminhos | Condutora | Na resposta |
| Fichas de fonte novas | Dossiê | `fontes/`, sem duplicar |
| Placar | Dossiê | `conselho/placar.jsonl` |
| Custos e falhas por modelo | Dossiê | `conselho/<id>/custos.json` |

**Contratos com as outras skills:**

| Skill | Relação |
| --- | --- |
| `etapa-1-cir` | Manda o brief, guarda a chave de autoria, roda o anonimizador e o sorteio, recebe o pacote e leva a decisão a você |
| `pesquisa-cientifica` | Cada membro a usa no modo refutar; o crítico, no modo conferir |
| `especialistas` | Dá a ficha e a `esp-*` quando a ótica pede uma especialidade, como a do especialista do domínio |
| `equipe-especialistas` | Entrega o parecer de verificação antes do veredito |

## 5. Conselhos, óticas e templates

### 5.1 Tipos de conselho

| Conselho | Quando | Composição | Rodadas |
| --- | --- | --- | --- |
| Triagem | Passo 3 | Refutador de limites teóricos e guardião, mais natureza humana quando há pessoas no centro, e o crítico. Um membro na dose leve, dois na padrão, dois ou três na completa | Uma; só procura falha fatal |
| Triagem reforçada | 3.5, o teste do impossível | O parecer da equipe de verificação e refutadores de duas famílias | Uma, e a troca se houver divergência |
| Rápido | Passo 8, nas doses leve e padrão | 2 membros com as óticas do cartão e o crítico | Troca só na dose padrão, se houver divergência |
| Completo | Passo 8 na dose completa e validações integradas | De 3 a 5 membros de famílias diferentes e o crítico | Troca se houver divergência |
| Sob demanda | Quando você pedir | 2 ou 3 óticas escolhidas conforme a dúvida, e o crítico | Troca se houver divergência |

### 5.2 Óticas

| Ótica | Procura | Barra de evidência | Não faz |
| --- | --- | --- | --- |
| Refutador (de método, de limites teóricos ou de coerência) | A falha fatal e o contraexemplo | Alta: fonte, cálculo ou prova | Ser do contra sem critério; o advogado do diabo designado tende a reforçar a posição inicial do grupo ([Nemeth, Brown e Rogers](https://doi.org/10.1002/ejsp.58)) |
| Construtivo | A melhor versão da hipótese e o que falta para ela ficar de pé | Média | Reescrever a hipótese |
| Explorador | Uma alternativa melhor ou uma analogia de outro campo | Baixa para levantar, alta para afirmar | Votar na própria alternativa |
| Adversário | Como manipular, enganar ou contornar o conceito | Média, com cenário concreto | Atacar sem cenário |
| Guardião | Danos, valores e fidelidade ao propósito | Alta nos valores do 1.5 | Trazer valores que não estão no dossiê como se estivessem |
| Natureza humana | Como pessoas reais vão entender mal, usar mal ou confiar demais | Média, com estudos de comportamento | Supor o usuário ideal |
| Especialista do domínio | O que a área sabe e a hipótese ignora | Alta, com a `esp-*` | Julgar fora da área |
| Juiz de diversidade | Se duas famílias de ideias têm o mesmo princípio central | — | Julgar a qualidade |
| Leitor da Etapa 2 | O que não dá para entender sem contexto | — | Completar as lacunas por conta própria |
- **Papéis diferentes é que fazem a diferença;** repetir o mesmo papel piora a avaliação ([ChatEval](https://arxiv.org/abs/2308.07201)). Uma persona sozinha não melhora o acerto ([Zheng et al.](https://arxiv.org/abs/2311.10054)); por isso cada ótica vem com método e perguntas-guia, e a especialidade vem de uma `esp-*`.
- **"Personalidade" é postura de julgamento:** a barra de evidência, quão longe o membro explora e quanto risco aceita. Traços sociais, como excesso de confiança, trazem conformismo ([Zhang et al.](https://arxiv.org/abs/2310.02124)) e ficam de fora.

### 5.3 Templates

| Template | Usado em | Óticas | Formato da resposta |
| --- | --- | --- | --- |
| Propósito | Tema 1 | Guardião, natureza humana, refutador e explorador | Matriz por critério |
| Evidência | Tema 2 e linhas de base | Refutador de método, especialista do domínio e construtivo | Matriz por critério |
| Idealidade | Tema 3 e RFI na função | Refutador de limites teóricos, construtivo, natureza humana e explorador | Matriz por critério |
| Diversidade | 4.5 | Juiz de diversidade e explorador | Pares de famílias: o princípio central é o mesmo? |
| Elementos | 4.7 e 4.9 | Construtivo, adversário e guardião | Elemento a elemento, nos que dividem opiniões |
| Arquitetura | 4.11 a 4.15 | Construtivo, refutador de coerência e adversário | Matriz por critério |
| Prova | Tema 5 | Adversário, refutador, natureza humana, construtivo e explorador | Matriz por critério |
| Passagem | Tema 6 | Leitor da Etapa 2 sem contexto e guardião do propósito | Perguntas centrais sem resposta no CIR |
| Sob demanda | Quando você pedir | Escolhidas conforme a dúvida | Matriz por critério |

No conselho rápido, o cartão da sub-etapa diz quais duas óticas entram, como em "conselho rápido (guardião e refutador)". No completo, entram as óticas do template, e as que sobrarem são sorteadas.

### 5.4 Modo avulso

Fora da Etapa 1, sem dossiê, a skill faz um grill curto para fixar a pergunta, as opções e os critérios com "refuta se", antes de qualquer opinião. Depois monta o painel com o mapa padrão e grava tudo em `conselhos/<data>-<assunto>/`, numa pasta com Git. As regras são as mesmas.

## 6. Passos

### 6.1 Ao receber o brief

1. **Confere o brief** (`valida_brief.py`): critérios com "refuta se", hipóteses no formato fixo e sem marcas de autoria, template e dose. Se faltar algo, devolve à condutora dizendo o quê. Nunca cria critério depois de ver as hipóteses.
2. **Monta o painel** (`painel.py`): as óticas do template; uma família por membro, todas no nível de juiz; o crítico de uma família que não produziu o artefato principal e, se der, fora do painel; no máximo um membro da família do produtor; e as restrições do mapa. Grava `painel.json`.
3. **Prepara um brief por membro** (`briefs_membros.py`): rótulos aleatórios, ordem sorteada para cada membro, com a semente registrada, as instruções da ótica e o formato de entrega. O brief vai como texto, e o membro não lê arquivos do dossiê.
4. **Normaliza a redação** na dose completa: um modelo que não vota reescreve as hipóteses na mesma estrutura e no mesmo tom, sem mudar o conteúdo, para que o estilo não denuncie a origem. A sua versão, escrita por você, ao lado de textos de IA, é o caso típico. A condutora confere a fidelidade, e o teste da seção 14 mede se ainda dá para adivinhar a origem.

### 6.2 Rodada 1, em paralelo

| Quem | Faz | Entrega |
| --- | --- | --- |
| Cada membro | Lê o brief; carrega a `esp-*`, se houver; para cada hipótese e critério, procura o que a derrubaria, com a `pesquisa-cientifica` no modo refutar; julga sozinho | Veredito no formato da seção 8 |
| Adaptador | Dispara todos os membros ao mesmo tempo e espera; chama de novo, uma vez, quem falhar; depois, troca pela alternativa do mapa | `custos.json` e alertas |
| `valida_veredito.py` | Confere o formato, os sinais e as fichas citadas, e marca o que o membro citou sem estar no brief nem numa fonte da web (possível vazamento) | Um pedido de correção; se não vier, veredito inválido, com registro |

### 6.3 Crítico

Lê os vereditos, identificados só pelo rótulo do membro, e confere o método, a lógica, se o trecho de cada ficha sustenta a afirmação (com a `pesquisa-cientifica` no modo conferir) e os sinais de contaminação. Marca o que está sem lastro. Não vota nas hipóteses. Entrega `critica.md`.

### 6.4 Divergência

O `divergencia.py` marca divergência relevante quando, num critério que o cartão chama de decisivo, um membro dá "+" e outro "−"; quando um membro aponta falha fatal; quando a maioria responde "?"; ou quando o crítico derruba o lastro de um veredito decisivo.

### 6.5 Troca de argumentos

Só com divergência relevante e se a dose permitir. Cada membro recebe, na mesma sessão da rodada 1, os argumentos dos outros sobre os pontos divergentes, sem autoria e em ordem sorteada, e as notas do crítico. Muda de posição só citando a evidência nova que o fez mudar; sem ela, mantém. É uma troca só, como no método Delphi ([Rowe e Wright](https://doi.org/10.1016/S0169-2070%2899%2900018-7)).

### 6.6 Matriz e síntese

- **Matriz** (`matriz.py`): hipóteses por critérios, com o sinal de cada membro na célula (por exemplo, "+ + − ?"), sem soma. Marca as divergências e as falhas fatais.
- **No conselho rápido,** a síntese é a própria matriz com a lista das divergências e os argumentos copiados dos vereditos, sem paráfrase.
- **No completo,** um relator, que não vota e é de uma família que não produziu o artefato, escreve o que convergiu, o que divergiu, com o melhor argumento de cada lado, as falhas fatais apontadas, o que mudaria cada veredito e as lacunas. Não recomenda nada. O `sintese_check.py` confere se toda posição minoritária da matriz aparece na síntese.

### 6.7 Entrega

Grava o pacote, atualiza o placar e devolve à condutora um resumo curto e os caminhos; o resultado condensado é o que mantém limpo o contexto de quem coordena ([Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). A condutora mostra a matriz e a síntese a você. Qual modelo fez o papel de cada membro fica na chave e só aparece depois da sua decisão, se você quiser, para que a marca do modelo não pese na escolha.

### 6.8 Triagem

Uma rodada. Cada item sai como "sem falha fatal", "impossível em princípio" (vira limite máximo possível), "difícil hoje" (vira fronteira técnica) ou "fere um valor" (vai para você), com o motivo e a fonte. Nada é descartado. Uma falha fatal apontada por um membro só passa pelo crítico e, nas doses padrão e completa, por um refutador de outra família antes de chegar a você.

### 6.9 Placar

- **Cada veredito vira uma linha:** o membro (ótica, especialidade, família e modelo), a hipótese, o critério, o sinal, a probabilidade que o membro dá de a hipótese resistir ao "refuta se" e o que o mudaria.
- **Quando um desfecho aparece** (a prova conceitual do tema 5, o critério de pronto, as Etapas 2 e 3 ou um fato novo), a condutora o registra, e o placar calcula o acerto por ótica, especialidade e família, com a pontuação de Brier. Acompanhar o acerto ao longo do tempo é parte do que melhorou previsores humanos ([Mellers et al.](https://doi.org/10.1177/0956797614524255)).
- **Sua decisão entra ao lado do veredito:** a escolha, o motivo e o objetivo que a condutora grava (seção 6.6 do plano dela). Assim, quando você decide contra a síntese por um valor ou por um objetivo, o placar não conta isso como erro do conselho.
- **Rodízio:** as famílias giram entre as óticas, de um conselho para outro, para o placar separar o efeito da ótica do efeito do modelo.
- **Na v1, o placar só registra.** Os ajustes nos templates vêm quando houver desfechos suficientes.

## 7. Regras que valem o tempo todo

| Regra | Por quê | Como se garante |
| --- | --- | --- |
| A rodada 1 é cega e independente | A influência social reduz a sabedoria das multidões ([Lorenz et al.](https://doi.org/10.1073/pnas.1008636108)) | Briefs individuais, rótulos aleatórios e nada do dossiê; no Notion, sessão incógnita num computador novo, ou um Custom Agent sem acesso às páginas (seção 9); teste com marcadores |
| Critérios e "refuta se" vêm antes das hipóteses | Critério escrito depois vira critério sob medida | O `valida_brief.py` recusa o brief sem eles |
| Sem soma, sem média e sem vencedor | O dissenso fica visível, e quem decide é você | Matriz com o sinal de cada membro |
| Mudar de posição só com evidência nova | No debate, modelos trocam a resposta certa pela errada para concordar ([Talk Isn't Always Cheap](https://arxiv.org/abs/2509.05396)) | O formato da troca pede a evidência nova; sem ela, a mudança não vale |
| Concordância não é verificação | Os modelos partem das mesmas premissas | "+" e "−" com fonte ou raciocínio verificável; "?" é resposta legítima |
| Identidade dos modelos oculta | Modelos seguem mais a maioria quando ela é da mesma família ([Soffer et al.](https://arxiv.org/abs/2609.33495)) | Os membros se conhecem pela ótica |
| Famílias diferentes, de qualidade parecida | Um painel de modelos diferentes avalia melhor que um modelo só ([PoLL](https://arxiv.org/abs/2404.18796)), mas misturar modelos desiguais baixa a média ([Self-MoA](https://arxiv.org/abs/2502.00674)) | O `painel.py` só usa modelos do nível de juiz (seção 10) |
| Crítico de outra família que a do produtor, e no máximo um membro da família do produtor | Avaliadores de IA favorecem as próprias gerações ([Panickssery, Bowman e Feng](https://arxiv.org/abs/2404.13076)) | O `painel.py` e o teste de autopreferência |
| Ordem sorteada para cada membro | Juízes de IA têm viés de posição ([Zheng et al.](https://arxiv.org/abs/2306.05685)) | O `sorteio.py`, com a semente registrada |
| Quem gerou não julga o que gerou | Modelos se mostraram avaliadores pouco confiáveis de ideias ([Si, Yang e Hashimoto](https://arxiv.org/abs/2409.04109)) | Sessões de geração e de julgamento sempre separadas |
| A síntese não recomenda | A decisão é sua | Formato fixo e o teste de opinião |
| Sem diversidade, avisa | Você precisa saber quando o conselho é só Claude | Claude com óticas e fontes diferentes, e o registro "sem diversidade de modelos" |
| O membro usa só o brief e a web | Sem isso, não há julgamento às cegas | Instrução no brief, auditoria das sessões no Notion e ferramentas mínimas no Claude Code |

**Racionalizações e respostas** (vão para `references/regras.md`):

| Pensamento | Resposta |
| --- | --- |
| "Todos concordaram; não precisa pesquisar." | Concordância não é verificação. Pesquisar para derrubar é o trabalho. |
| "Só um membro discorda; é ruído." | O dissenso fica. A maioria pode estar errada. |
| "Somo os sinais para facilitar." | Sem soma. Um "−" num critério decisivo não se compensa com dois "+". |
| "O brief não tem critério; crio um razoável." | Critério criado depois de ver as hipóteses é sob medida. Devolve à condutora. |
| "O modelo caiu; ponho outro Claude e sigo." | Pode, pela alternativa do mapa, mas registra "sem diversidade de modelos". |
| "Faço a troca em tudo, por garantia." | Só com divergência relevante. Debate sem motivo puxa para o consenso. |
| "O usuário prefere H2; vale avisar o conselho." | Preferência não entra no brief. |
| "A síntese fica mais útil com uma recomendação." | Recomendação é decisão. A síntese mostra, e você decide. |

## 8. Formatos e modelos de documento

**Brief do conselho** (os campos que se somam ao envelope comum):

```markdown
brief: B-2.3-07
conselho: completo · template Evidência · dose completa
sub-etapa: 2.3 Contradições e trade-offs aceitos
pergunta: quais destas formulações das contradições do mapa resistem aos critérios?
hipóteses: K, Q e T (cartões abaixo, sem autoria)
critérios:
  - C1 (decisivo): cada contradição tem evidência de que existe hoje. Refuta se: uma contradição não tem caso nem fonte
  - C2: a classificação "de princípio" ou "quebrável" se sustenta. Refuta se: uma "de princípio" tem contraexemplo
parecer: P-2.3-1 (equipe de verificação), sem autoria
fichas: F-031, F-044
troca: permitida se houver divergência
restrições: nenhum trecho sigiloso; famílias autorizadas pelo mapa
```

**Veredito de um membro:**

```markdown
veredito: B-2.3-07 · membro M3 · ótica refutador de método · rodada 1
## Q
- C1: − · a contradição 2 não tem caso nem fonte; busquei casos de "custo de uso alto com adoção alta" e não achei (buscas anotadas) · mudaria: um caso documentado
- C2: + · F-044, trecho 3, sustenta "de princípio" · mudaria: um contraexemplo publicado
- probabilidade de resistir ao "refuta se": 35%
## K
- …
falha fatal: nenhuma
fontes novas: F-M3-1 (DOI 10.…, trecho anotado)
```

**Matriz:**

| Hipótese | C1 (decisivo) | C2 | Falha fatal |
| --- | --- | --- | --- |
| K | `+ + ?` | `+ + 0` | — |
| Q | `+ + −` | `+ + +` | — |
| T | `− − ?` | `0 + ?` | M2: "a contradição 1 não existe fora do caso citado" |

Cada célula traz o sinal de cada membro, na ordem M1 a M3, sem total. No documento, as divergências aparecem destacadas.

**Painel** (`painel.json`, resumido):

```json
{
  "conselho": "B-2.3-07",
  "tipo": "completo",
  "template": "evidencia",
  "via": "notion-sessao",
  "familia_do_produtor": "anthropic",
  "membros": [
    {"rotulo": "M1", "otica": "especialista do domínio", "esp": "esp-economia-comportamental", "familia": "openai", "modelo": "GPT-5.5"},
    {"rotulo": "M2", "otica": "construtivo", "familia": "xai", "modelo": "Grok 4.6"},
    {"rotulo": "M3", "otica": "refutador de método", "familia": "deepseek", "modelo": "DeepSeek V4 Pro"}
  ],
  "critico": {"familia": "zhipu", "modelo": "GLM 5.2"},
  "relator": {"familia": "google", "modelo": "Gemini 3.1 Pro"},
  "semente_sorteio": 48213,
  "sem_diversidade": false
}
```

O crítico e o relator também seguem as regras: são de famílias que não produziram o artefato e ficam fora do painel. Quando não houver famílias suficientes, o crítico pode ser de uma família do painel, nunca da família do produtor.

**Linha do placar** (`placar.jsonl`):

```json
{"conselho": "B-2.3-07", "membro": "M3", "otica": "refutador de método", "familia": "deepseek", "modelo": "DeepSeek V4 Pro", "hipotese": "Q", "origem": "na chave", "criterio": "C1", "sinal": "-", "prob_resistir": 0.35, "mudaria": "um caso documentado", "desfecho": null}
```

A origem da hipótese fica só na chave, com a condutora, e entra no placar depois da decisão, para o teste de autopreferência.

## 9. Adaptador de modelos

O protocolo é o mesmo em qualquer ferramenta; o adaptador só muda o jeito de chamar cada membro. Ele dispara, espera, valida e registra o custo. A interface é uma só: recebe o rótulo do membro, a família, o modelo, a via, o brief em texto e o tempo limite; devolve o texto do veredito, a situação (ok, falhou, inválido ou substituído), o modelo usado de fato, o tempo e o custo.

### 9.1 Notion, primeiro

No Notion, quem chama é o próprio agente, pelas ferramentas de sessão; os scripts preparam, sorteiam, validam e consolidam.

| Via | Como | Isolamento | Quando |
| --- | --- | --- | --- |
| A. Sessão filha | Uma sessão por membro, com o modelo do mapa, incógnita e num computador novo; a troca vai por mensagem à mesma sessão, que guarda o contexto da rodada 1 | Não recebe o link da sessão de origem nem os arquivos do dossiê. Mas continua com as suas permissões no workspace, então pode buscar páginas e sessões antigas: o isolamento depende da instrução e da auditoria | Padrão, se passar no teste de vazamento |
| B. Custom Agent de privilégio mínimo | Um agente "Conselheiro", sem acesso às páginas do workspace e com a skill anexada, chamado pela URL, com o modelo do mapa | Isolado por permissão. Não aceita as opções de incógnito nem de computador novo; falta confirmar se tem computador para cálculos e se enxerga a sessão de origem | Papéis cegos, se a via A vazar; e a ponte para o Claude Code, pela API de agentes |
- **Por que computador novo sempre:** por padrão, a sessão filha divide o computador e os arquivos da sessão de origem, onde está o dossiê. Num computador novo, ela não os vê.
- **Escolha do modelo:** a documentação das sessões pede que o modelo só seja escolhido a pedido seu. O mapa que você aprova no 0.3 é esse pedido.
- **Em paralelo:** os membros são disparados juntos, com aviso de conclusão; a condutora espera todos, ou o tempo limite, antes de seguir.
- **Auditoria:** depois de cada conselho, a condutora lista os eventos de cada sessão de membro. Uma busca ou leitura no workspace invalida o veredito e vira alerta. Nos testes, sempre; em uso, sempre no conselho completo e por amostragem nos outros.
- **Cálculos:** na via A, o membro tem Python no computador novo. Na via B, se o Custom Agent não tiver computador, os cálculos ficam com a equipe de verificação, e o membro recebe o parecer.

### 9.2 Claude Code, na adaptação

| Família | Como |
| --- | --- |
| Claude | Subagentes só com busca e leitura na web e Python, sem o `CLAUDE.md` do projeto ([Claude Code: subagentes](https://code.claude.com/docs/en/sub-agents)) |
| Gemini | Gemini CLI em modo não interativo, com saída em JSON, na cota gratuita do login Google ([Gemini CLI](https://github.com/google-gemini/gemini-cli)) |
| As demais | A API de agentes do Notion, em beta, chamando o Custom Agent "Conselheiro" com o modelo do mapa e pagando em créditos do Notion ([Notion: API de agentes](https://developers.notion.com/guides/notion-agent-apis/overview)) |

Um script dispara os membros em paralelo, com tempo limite e nova tentativa por assento, a partir do claude-council (MIT, com atribuição em `origem.md`).

## 10. Mapa de modelos

**Modelos de juiz** são os do nível mais alto de inteligência relativa na lista do Notion. A lista abaixo é a deste workspace, consultada em outubro de 2026; o 0.3 confere de novo a cada projeto, porque os modelos mudam.

| Família | Juiz | Só gerador ou tarefa simples |
| --- | --- | --- |
| Anthropic | Opus 5.5 (a condutora) e Sonnet 5.5 | Haiku 5.5 |
| OpenAI | GPT-5.5 e GPT-5.4 | GPT-5.6 Luna |
| xAI | Grok 4.6 | — |
| DeepSeek | DeepSeek V4 Pro | DeepSeek V4 Flash |
| Zhipu | GLM 5.2 | GLM 5.3 Flash |
| Google | Gemini 3.1 Pro, se a linha de base confirmar o nível | Gemini 3.7 Flash |
| Moonshot | — | Kimi K3 (nível intermediário) |

| Papel | Proposta inicial |
| --- | --- |
| Conselho rápido | 2 membros, de famílias diferentes, entre GPT-5.5, Grok 4.6, DeepSeek V4 Pro e GLM 5.2 |
| Conselho completo | De 3 a 5 entre GPT-5.5, Grok 4.6, DeepSeek V4 Pro, GLM 5.2, Gemini 3.1 Pro e Sonnet 5.5, com no máximo um da família do produtor |
| Crítico | O de nível mais alto de uma família que não produziu o artefato, de preferência fora do painel |
| Relator e normalizador | Nível mais alto, fora do painel e de uma família que não produziu o artefato |
| Sem diversidade | Sonnet 5.5 e Opus 5.5 com óticas e fontes diferentes, com o registro |
- **As equipes são quase sempre Claude,** então a versão elaborada costuma ser da família Anthropic. Por isso o crítico e o relator padrão vêm de outras famílias, e no máximo um membro é Claude.
- **Custo:** cada membro é uma sessão. Um conselho vai de umas 3 chamadas, no rápido, a umas 13, no completo com troca, contando crítico, relator e normalizador. O custo em créditos vai para o `custos.json`, e a linha de base mede o consumo real por tipo de conselho.

## 11. Arquivos

```
conselho-especialistas/
  SKILL.md                  até umas 200 linhas: regras no topo, o roteiro e o mapa das referências
  references/
    protocolo.md            rodadas, divergência, troca e entrega
    conselhos.md            tipos e composição por dose
    oticas.md               as óticas, com método, perguntas-guia, barra de evidência e o que não fazem
    templates/              propósito, evidência, idealidade, diversidade, elementos, arquitetura, prova, passagem e sob demanda
    membro.md               o texto que vai no brief de todo membro: o que fazer, o formato e o que não fazer
    critico.md
    relator.md
    regras.md               a seção 7, com as racionalizações
    formatos.md
    placar.md
    modelos.md              como montar o mapa, os níveis e as regras de qualidade parecida
    adaptador-notion.md
    adaptador-claude-code.md
    origem.md               ideias e trechos aproveitados, com licença e atribuição
  scripts/
    valida_brief.py         critérios, "refuta se", formato e marcas de autoria
    anonimiza.py            rótulos aleatórios e chave de autoria fora dos briefs
    sorteio.py              ordem por membro, com semente
    painel.py               monta o painel a partir do template, do mapa e das restrições
    briefs_membros.py       um brief por membro
    valida_veredito.py      formato, sinais, fichas citadas e sinais de vazamento
    divergencia.py
    matriz.py
    sintese_check.py        toda posição minoritária aparece na síntese
    placar.py               registro e, com desfechos, a pontuação de Brier
    custos.py
    paralelo_cli.py         no Claude Code: chamadas em paralelo, com tempo limite e nova tentativa
  assets/
    schemas/                brief, veredito, painel e placar
```

- **No Notion,** a skill vira uma página do banco de Skills; as referências viram subpáginas; os scripts vão em Files; e `membro.md`, `critico.md` e `relator.md` viram as instruções das sessões filhas e do Custom Agent "Conselheiro".
- **No Claude Code,** as definições dos subagentes ficam no plugin, como na condutora.

## 12. Subagentes

| Agente | Formação | Vê | Não vê | Ferramentas |
| --- | --- | --- | --- | --- |
| Membro | Isolado, de uma família do painel | O brief, com as hipóteses em ordem sorteada, os critérios, o parecer e as fichas | A autoria, os outros membros na rodada 1, o modelo dos outros, a sua preferência e o dossiê | Busca e leitura na web e Python; a `pesquisa-cientifica` e, se houver, a `esp-*` |
| Crítico | Isolado, de outra família que a do produtor | Os vereditos, pelos rótulos | A autoria e os modelos | Busca e leitura na web e Python; a `pesquisa-cientifica` |
| Relator | Isolado, fora do painel; só no completo | A matriz, os vereditos e a crítica | A autoria e os modelos | Nenhuma |
| Normalizador | Isolado, fora do painel; só na dose completa | As hipóteses | A autoria | Nenhuma |
| Juiz de diversidade | Isolado, sem ter gerado nada | As famílias de ideias, duas a duas | A autoria | Nenhuma |
| Leitor da Etapa 2 | Isolado | Só o CIR e o pacote | O dossiê e a conversa | Nenhuma |

## 13. Casos-limite

| Situação | O que o conselho faz | Registro |
| --- | --- | --- |
| Brief sem critério ou sem "refuta se" | Devolve à condutora, dizendo o que falta | — |
| Hipótese com marca de autoria ("minha versão", "a da IA") | O anonimizador tira a marca; se não der sem mudar o sentido, devolve | Alerta |
| Uma hipótese só | Julga contra os critérios e avisa que, sem alternativa, não há comparação | "Sem alternativa" |
| Mais de 6 hipóteses | Cada membro julga um subconjunto sorteado, com sobreposição, e a matriz mostra quem viu o quê | No painel |
| Um modelo falha ou estoura o tempo | Nova tentativa; depois, a alternativa do mapa, no mesmo nível e de outra família | "Substituído" |
| Nenhuma alternativa de outra família | Claude com óticas e fontes diferentes | "Sem diversidade de modelos" |
| Os créditos acabam no meio | Guarda o que já chegou e pergunta se você quer esperar, trocar de modelo ou seguir só com Claude | Registro |
| Veredito fora do formato | Um pedido de correção; depois, veredito inválido, fora da matriz | "Inválido" |
| Um membro cita algo que só existe no workspace ou no dossiê | Invalida o veredito, audita a sessão e avisa a condutora | "Possível vazamento" |
| Todos concordam rápido, sem fontes | O crítico marca "concordância sem lastro", e a condutora pode pedir mais pesquisa | Alerta |
| A divergência continua depois da troca | Não força consenso; a matriz mostra o empate, e a condutora sobe a dose (mais pesquisa ou mais casos) antes de gerar mais | Registro |
| Só um membro aponta falha fatal | Passa pelo crítico e, nas doses padrão e completa, por um refutador de outra família, antes de chegar a você | Registro |
| Um membro propõe uma alternativa em vez de julgar | Ela vai para o banco de ideias, com origem "conselho", e não conta como voto | Banco |
| Você quer saber qual modelo disse o quê | Depois da sua decisão, sim; antes, a condutora explica por que espera | — |
| Você quer participar como membro | A sua opinião entra como a sua versão ou a sua decisão, e não como voto, para não pesar sobre os membros | — |
| Pedido sob demanda vago ("o que o conselho acha?") | Grill curto: a pergunta, as opções e os critérios, antes de montar o painel | — |
| Material sigiloso marcado no 0.3 | Só vai para as famílias autorizadas; se faltarem famílias, avisa | Restrição no painel |
| Hipóteses longas demais | Pede à skill de origem o cartão no tamanho máximo, em vez de resumir por conta própria | — |

## 14. Testes e métricas

Os testes medem o julgamento: independência, lastro, dissenso e acerto. Seguem a seção 13 do plano geral e o guia de testes do skill-creator.

**Como testar antes de as outras skills existirem:**

- **Dublê da `pesquisa-cientifica`,** com fichas fixas, para separar a qualidade do julgamento da qualidade da busca. Depois, os mesmos testes com a skill real.
- **Banco de calibração,** com resposta conhecida: hipóteses com falha fatal plantada (violar um limite de princípio, prometer "eliminar todo viés", contradição lógica), hipóteses sólidas e armadilhas (uma fonte que parece sustentar e não sustenta; uma afirmação verdadeira sem fonte).
- **Motor de Insights:** as decisões do documento v1 vão ao conselho, que deve reencontrar os pontos fracos e os modos de falha do Anexo A sem acesso a ele.
- **Sala limpa para o teste sem o Anexo A.** No Notion, os agentes conseguem buscar o Anexo no seu workspace. Nesse teste, o caso vai com outro nome, os briefs proíbem a busca, e a auditoria das sessões invalida qualquer execução que tenha buscado no workspace. Se isso não bastar, o teste roda pela via B ou no Claude Code.

| Teste | Como | Alvo |
| --- | --- | --- |
| Falha fatal | Banco de calibração | 90% ou mais das falhas plantadas achadas; no máximo 10% de falso alarme |
| Lastro | "+" e "−" com fonte ou raciocínio verificável; fichas cujo trecho sustenta a afirmação, conferidas pelo crítico e por amostragem sua | 90% ou mais com lastro; 95% ou mais das fichas sustentam |
| Recuperação do gabarito | Pontos fracos e modos de falha do Anexo A reencontrados sem acesso a ele | A maior parte; o número sai da linha de base |
| Independência | Justificativas da rodada 1 parecidas demais, comparadas com execuções separadas de propósito | Nenhum sinal de cópia |
| Vazamento | Marcadores únicos na autoria, na sua versão e no dossiê; auditoria dos eventos das sessões | Zero, nas vias A e B |
| Cegueira de autoria | Um juiz tenta adivinhar a origem de cada hipótese (sua ou de qual família), com e sem a normalização | Perto do acaso, com a normalização |
| Viés de posição | O mesmo brief com a ordem invertida | 90% ou mais das células com o mesmo sinal |
| Autopreferência | Sinais de cada família para hipóteses da própria família e das outras, pela chave, depois das decisões | Diferença medida; se for relevante, a regra do painel endurece |
| Estabilidade | O mesmo brief 3 vezes | 80% ou mais de sinais iguais nos critérios decisivos |
| Troca de argumentos | Mudanças de posição com evidência nova citada; e, no banco de calibração, as que trocaram o certo pelo errado | 100% com evidência nova; trocas para o errado medidas |
| Dissenso | Posições minoritárias da matriz que aparecem na síntese | 100% |
| Neutralidade | Sínteses julgadas às cegas por um avaliador de outra família | Nenhuma recomendação |
| Acionamento | Os 20 pedidos da seção 3 | 80% ou mais de acerto e no máximo 10% de falso positivo |
| Custo e tempo | Chamadas, créditos e minutos por tipo de conselho; falhas por modelo | Registrar, sem limite |

**Comparações que decidem o desenho,** em julgamento cego:

- **Famílias diferentes ou só Claude** com óticas diferentes, no banco de calibração e no Motor.
- **Com e sem a troca de argumentos,** nos casos com divergência.
- **3 ou 5 membros** no conselho completo: se 5 não acharem mais falhas que 3, ficam 3.
- **Via A ou via B** no Notion: vazamento, custo e tempo.
- **Com e sem a normalização da redação:** cegueira de autoria e fidelidade ao conteúdo.
- **Gemini 3.1 Pro e Kimi K3 como juízes:** entram no nível de juiz só se igualarem os outros no banco de calibração.

## 15. Riscos

| Risco | Mitigação |
| --- | --- |
| Conformismo e bajulação | Rodada 1 cega, troca só com divergência, mudança só com evidência nova e identidade dos modelos oculta |
| Modelos que pensam igual | Famílias, óticas e buscas diferentes por membro; o teste com só Claude mede o ganho real |
| Vazamento pela busca no workspace do Notion | Computador novo, instrução no brief e auditoria das sessões; se vazar, via B |
| A redação denunciar a autoria | Cartão de formato fixo e normalização; teste de cegueira |
| Viés de posição e autopreferência | Sorteio por membro, crítico de outra família e no máximo um membro da família do produtor; testes |
| A síntese decidir no seu lugar | Relator que não vota, formato sem recomendação, `sintese_check.py` e teste de neutralidade |
| Fontes inventadas ou que não sustentam a afirmação | Fichas com o trecho, crítico no modo conferir e verificação de DOI |
| Os modelos mudarem de nome, preço ou qualidade | Mapa conferido a cada projeto, modelo gravado em cada veredito e linha de base refeita quando o mapa mudar |
| Muitas sessões ao mesmo tempo | Medir o limite na fase 3; se houver, disparar em lotes |
| A API de agentes, em beta, mudar | Só na ponte do Claude Code; alternativa no mapa |
| Custo em créditos | Conselho rápido onde basta, completo onde a decisão pesa; custo por conselho medido |
| Placar sem desfechos por muito tempo | Na v1, só registra; os desfechos vêm do tema 5, do critério de pronto e das Etapas 2 e 3 |

## 16. O que fica de fora

- **Debate livre ou com várias rodadas.**
- **Voto, média, ranking geral ou nota única.**
- **Conselho que decide ou recomenda.**
- **Pessoas como membros.** O especialista humano revisa as `esp-*`, no plano da `especialistas`.
- **Ajuste automático dos templates pelo placar,** que vem quando houver desfechos.
- **Conversa entre membros antes do veredito,** que é da equipe de verificação.

## 17. Decidido e em aberto

**Decidido:**

- **Notion primeiro,** com o conteúdo universal e o adaptador por ferramenta.
- **Conselhos, óticas e templates do fluxograma;** uma troca só, e só com divergência; sem média; crítico de outra família; ordem sorteada; síntese sem recomendação.
- **Modelos de juiz:** o nível mais alto de cada família no Notion, conferido a cada projeto.

**Em aberto:**

1. **Via A ou via B para os papéis cegos no Notion:** o teste de vazamento decide. Criar o Custom Agent "Conselheiro" para o teste precisa da sua autorização, e talvez da do admin, porque ele gasta créditos do Notion.
2. **Probabilidade em cada veredito:** dá calibração ao placar, mas pesa no formato. A proposta é pedir só nos critérios decisivos.
3. **Mostrar qual modelo fez cada papel depois da sua decisão:** a proposta é sim, se você quiser.
4. **Normalização da redação:** a proposta é usar sempre que a sua versão estiver entre as hipóteses e na dose completa; o teste de cegueira decide.