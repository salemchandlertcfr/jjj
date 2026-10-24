# Plano detalhado — equipe-especialistas

<aside>
🤝

**O que é:** o plano detalhado da `equipe-especialistas`, a skill que conduz as reuniões de especialistas: a elaboração do passo 7 e a verificação do passo 8 de cada sub-etapa do [Fluxograma completo — Etapa 1 (método IDEAL em ciclo)](https://app.notion.com/p/Fluxograma-completo-Etapa-1-m-todo-IDEAL-em-ciclo-f1f71e3bd5e6487ebdfc94cd7e9fa161?pvs=21), a integração no fim de cada tema, as reuniões individuais e as reuniões paralelas com fusão. É o sexto plano da ordem da seção 15 do [Plano geral das skills — Etapa 1 (CIR)](https://app.notion.com/p/Plano-geral-das-skills-Etapa-1-CIR-72d0fdc1db19433e9101d1ac3b3015ef?pvs=21) e segue os formatos do [Plano detalhado — etapa-1-cir (condutora)](https://app.notion.com/p/Plano-detalhado-etapa-1-cir-condutora-fccda0c36a5d403582b433a6f2b0657f?pvs=21), do [Plano detalhado — conselho-especialistas](https://app.notion.com/p/Plano-detalhado-conselho-especialistas-f31c25a61c914fd98fe1f1ad81c09ed4?pvs=21), do [Plano detalhado — pesquisa-cientifica](https://app.notion.com/p/Plano-detalhado-pesquisa-cientifica-b0dde96c53b34b38aa26c8c474ce1071?pvs=21), do [Plano detalhado — grill-embasado](https://app.notion.com/p/Plano-detalhado-grill-embasado-ec54d7f985534c0a997926c075d97775?pvs=21) e do [Plano detalhado — especialistas](https://app.notion.com/p/Plano-detalhado-especialistas-79544cfde9c5403babc8e5cc62fe12cd?pvs=21).
**Universal primeiro:** o protocolo, os formatos e os scripts valem em qualquer agente com chat; só o transporte, o jeito de passar a palavra, muda com o ambiente (seção 9). **Claude primeiro:** líder, especialistas e crítico são Claude, no modelo que você escolher para o papel "equipes".

</aside>

## 1. Propósito no fluxograma

**Propósito:** juntar especialidades numa versão melhor que a de qualquer uma sozinha, sem fazer média e sem perder o que só um sabe.

| Responde por | Como se vê |
| --- | --- |
| Ganho da equipe | A síntese vence, às cegas, o melhor especialista sozinho e os mesmos especialistas isolados com uma síntese; onde não vence, a dose usa os isolados (seção 14) |
| Nada se perde | Toda contribuição das preparações tem um código e um destino na síntese: entrou, mudou, foi rejeitada com motivo ou ficou em aberto. O `sintese.py` acusa a que sumiu |
| Sem média | Onde as posições não combinam, a síntese escolhe pela evidência ou mantém as opções separadas, com o que decidiria entre elas; nunca um meio-termo sem motivo |
| Especialista aproveitado | Numa questão da sua área, quem fala com `esp-*` ou fonte conferida só é contrariado com contraprova, e a ata mostra qual |
| Discordância à vista | Quem discorda diz; quem muda de posição diz por quê, citando a fala que o convenceu; o dissenso que sobra vai à síntese com o melhor argumento de cada lado |
| Contas e fontes conferidas | Toda conta roda em Python e é refeita pela mesa; toda fonte nova passa pelos scripts da `pesquisa-cientifica` antes da síntese |
| Isolamento | Nenhum membro vê a autoria, o modelo dos outros, os casos reservados ou o dossiê; os marcadores plantados não aparecem em nenhuma fala |
| Rastreio | Cada fala traz o selo da especialidade, para o placar do catálogo; a ordem, a semente, as checagens e os custos ficam em `equipe/` |
- **Território, não roteiro.** A skill dá o objetivo, as regras e os formatos; o que cada especialista traz, como o líder organiza o mapa e quando a reunião para ficam a critério do modelo, conferidos por script.
- **Não faz:** julgar a versão final, que é do conselho; gerar as alternativas cegas, que trabalham isoladas; recrutar e escrever fichas, que é da `especialistas`; substituir a `pesquisa-cientifica`, que os membros usam; decidir, que é seu; ler o dossiê, que é só da condutora.
- **Pronto quando:** na elaboração, na integração e na fusão, a saída passa no script do modo e na revisão do crítico, com destino para toda contribuição; na verificação, o parecer passa no `parecer.py`, sem recomendação nem veredito; e, em todo modo, a ata, as checagens e os custos estão gravados.

## 2. Skills de base e o que se aproveita

| Base | O que se aproveita | O que é nosso | Licença |
| --- | --- | --- | --- |
| [Virtual Lab](https://github.com/zou-group/virtual-lab) ([Swanson et al., Nature](https://doi.org/10.1038/s41586-025-09442-9)) | O formato das reuniões: pauta com perguntas e regras; o investigador principal abre; cada membro fala na sua vez, pode passar e deve discordar, com educação, quando discorda; o crítico científico fala em toda reunião, por último; a cada rodada, o líder junta os pontos, decide e faz perguntas de seguimento; o resumo final pode contrariar membros, se justificado; reuniões individuais de um agente com o crítico; reuniões paralelas, com mais variação, e uma fusão, com menos, que junta as melhores partes e diz de onde veio cada uma | A preparação por escrito antes de qualquer fala; a abertura do líder com o mapa das preparações, sem a sua opinião (no Virtual Lab, ele abre com as próprias ideias); códigos e destino para cada contribuição; autoridade por especialidade; contas refeitas e fontes conferidas; posições finais | MIT |
| HiddenBench ([Li, Naito e Shirado](https://arxiv.org/abs/2505.11556), ICML 2026) | O diagnóstico e o remédio: com a informação distribuída, equipes de agentes perdem o que só um sabe e fecham cedo; revelar tudo no começo, ou um protocolo curto de troca e decisão, corrige boa parte | A preparação que chega inteira a todos; a fala com fato novo ou motivo contra; as posições finais | Só a ideia |
| [Kaesberg et al.](https://arxiv.org/abs/2502.19130) (ACL 2025 Findings) | O efeito do protocolo de decisão, do número de agentes e de rodadas; o rascunho de cada um antes da discussão e a melhoria coletiva sem conversa | Os testes de 2 contra 3 rodadas e da reunião contra a melhoria sem conversa | Só a ideia |
| Skills nossas: `conselho-especialistas`, `pesquisa-cientifica` e `especialistas` | Do conselho, o sorteio com semente, a checagem de minoria na síntese, o formato sem recomendação, o adaptador e a auditoria das sessões. Da pesquisa, os modos desenvolver e conferir e os scripts `verificar.py` e `trecho.py`. Da `especialistas`, as fichas, o bloco de especialidade, o selo, o "sem skill", a distante e os nomes funcionais | A ordem de fala sorteada por rodada; o `ata.py fontes`; o placar por especialidade, tirado da ata | Nosso |
| Plano geral e fluxograma | As 9 regras da equipe (seção 3 do plano geral); os três modos; as doses; a equipe de verificação; as duas opções de transporte | — | Nosso |

**Sete achados que mudam o desenho:**

1. **O que só um sabe se perde, a menos que vá por escrito a todos.** Em 65 tarefas de perfil oculto, em que a resposta certa só aparece juntando o que cada agente sabe, equipes de 15 modelos de ponta acertaram 30,1%, contra 80,7% de um agente único com toda a informação: convergiram cedo no que todos sabiam, e a falha piorou com equipes maiores. Quando cada um revelou tudo na primeira rodada, o acerto foi a 92,6% (GPT-4.1) e 98,2% (Gemini-2.5-Flash); um secretário que resumia a cada rodada ajudou menos. E um protocolo curto, em que cada agente traz um ou dois fatos e um motivo pelo qual a proposta à frente pode estar errada e, antes de decidir, resume a evidência mais forte e a incerteza, levou o GPT-4.1 de 3,7% a 80,0% ([Li, Naito e Shirado](https://arxiv.org/abs/2505.11556)). Em 65 estudos com grupos humanos, quem tinha a informação dividida teve oito vezes menos chance de achar a solução, e o que mais pesou foi a parte da informação única que chegou a ser dita ([Lu, Yuan e McLeod](https://doi.org/10.1177/1088868311417243)). Daí: a preparação de cada um vai inteira a todos, antes da primeira fala; a abertura lista o que só um trouxe; e a reunião fecha com posições finais.
2. **Equipes fazem média e desperdiçam o especialista.** Equipes de agentes que se organizam sozinhas ficaram abaixo do seu melhor membro mesmo sabendo quem ele era, com perdas de até 41,1% em benchmarks de ML. O gargalo foi aproveitar o especialista, não achá-lo: os agentes faziam média entre ele e os outros, e esse meio-termo cresceu com o tamanho da equipe e acompanhou a perda. A mesma busca de consenso protegeu contra agentes mal-intencionados ([Pappu et al.](https://arxiv.org/abs/2602.01011)). Daí: autoridade por especialidade, com contraprova, mas só para quem fala com `esp-*` ou fonte conferida; o `sintese.py` procura meio-termos sem motivo; de 3 a 5 especialistas.
3. **A discordância guardada derruba o ganho.** Modelos em debate trocam a resposta certa pela errada para concordar ([Wynn et al.](https://arxiv.org/abs/2509.05396)); a bajulação entre agentes leva a um consenso precoce, abaixo do agente único ([Yao et al.](https://arxiv.org/abs/2509.23055)); e o conformismo cresce com o tempo de interação e o tamanho da maioria ([Weng et al.](https://arxiv.org/abs/2501.13381)). O ganho da discussão sobre o voto cai à medida que os agentes guardam a discordância. A instrução "diga a sua resposta honesta mesmo que contradiga todos; uma discordância certa e solitária vale mais para esta equipe do que o acordo" reduziu esse silêncio, e pedir coesão o aumentou ([Mansuri et al.](https://arxiv.org/abs/2609.38324)). Daí: o objetivo dito a todos é a melhor versão, nunca o acordo; quem muda de posição diz por quê; poucas rodadas.
4. **A identidade pesa mais que o conteúdo.** Modelos seguem mais uma maioria errada quando ela é do seu grupo (a mesma família, IA ou até um grupo arbitrário), e o raciocínio passo a passo suprime a maior parte do efeito ([Soffer et al.](https://arxiv.org/abs/2609.33495)). No debate, seguir o colega é bem mais comum que se apegar à própria resposta, e tirar as marcas de identidade reduz o viés ([Choi, Zhu e Li](https://arxiv.org/abs/2510.07517)). Daí: os membros se conhecem pela especialidade, nunca pelo modelo; a versão base chega sem autoria; a fala dá o motivo antes da posição.
5. **Grupos pequenos e independentes, depois combinados, rendem mais que um grupo grande.** Numa plateia de 5.180 pessoas, cada uma respondeu sozinha e depois discutiu em grupos de cinco até um consenso; combinar só quatro desses consensos superou a média de milhares de respostas individuais ([Navajas et al.](https://doi.org/10.1038/s41562-017-0273-4)). No Virtual Lab, cada pauta importante rodou em 5 reuniões paralelas, com mais variação, e numa fusão, com menos, que juntou as melhores partes ([Swanson et al., Nature](https://doi.org/10.1038/s41586-025-09442-9)). Daí: na dose completa, 2 ou 3 reuniões paralelas e uma fusão. O que se transfere é a estrutura, não a média. E, como nem o Notion nem as definições de subagente do Claude Code dão acesso à temperatura, a diferença entre as paralelas vem da ordem de fala e da conversa; o teste compara com paralelas que trocam um membro.
6. **A conversa tem de provar que vale.** O voto da maioria explica a maior parte dos ganhos do debate entre modelos ([Choi, Zhu e Li](https://arxiv.org/abs/2508.17536)); um agente único com um bom prompt chegou perto da melhor discussão ([Wang et al.](https://arxiv.org/abs/2402.18272)); a deliberação ajudou modelos diferentes, mas não três instâncias do mesmo modelo ([Schneider e Schramm](https://arxiv.org/abs/2512.22625)); mais rodadas antes de decidir pioraram, e trabalhar sem conversa, vendo só as soluções da rodada anterior, rendeu mais que a discussão ([Kaesberg et al.](https://arxiv.org/abs/2502.19130)); falar um de cada vez rendeu mais que falar ao mesmo tempo, e agentes com o mesmo papel não superaram um agente só ([ChatEval](https://arxiv.org/abs/2308.07201)); e um protocolo de deliberação completo gastou cerca de 62 vezes os tokens de um agente e ficou abaixo dele na qualidade geral ([Prakash](https://arxiv.org/abs/2603.11781)). Quase todos usam tarefas de resposta única; elaborar com informação distribuída (cada um com a sua `esp-*` e as suas fontes) está mais perto do perfil oculto, onde a troca importa. Daí: rodadas em ordem, 2 no padrão e até 3 na completa, com parada antecipada; e a equipe fica só onde vencer, às cegas, os isolados com uma síntese (seção 14).
7. **Líder que opina cedo estreita; oposição de fachada não substitui a discordância de verdade.** Em grupos com líder diretivo, saíram menos alternativas, e os grupos aceitaram a solução do líder quando ele deu a preferência cedo ([Leana](https://doi.org/10.1177/014920638501100102)). Uma minoria autêntica rendeu mais e melhores soluções que qualquer forma de advogado do diabo ([Nemeth, Brown e Rogers](https://doi.org/10.1002/ejsp.58)); em agentes, pôr parte da equipe para discordar não ajudou de forma geral e, num modelo, derrubou o acerto de 88,9% para 30,6% ([Li, Naito e Shirado](https://arxiv.org/abs/2505.11556)). Em equipes de médicos, os líderes foram os que mais repetiram a informação e, com o tempo, cada vez mais a que só um tinha ([Larson et al.](https://doi.org/10.1037/0022-3514.71.2.315)). Daí: o líder abre com o mapa, sem preferência, devolve à mesa o que só um trouxe e decide pela evidência, no fim; o crítico confere, sem fazer oposição.

**O que muda nas regras do plano geral:** as 9 regras da seção 3 continuam, com seis acréscimos, já levados para lá: a preparação vai inteira a todos; o líder abre com um mapa, sem opinar; na rodada 1, cada fala traz fato novo e um motivo contra a proposta à frente; a autoridade por especialidade vale só com `esp-*` ou fonte conferida; cada um fecha com uma posição final, sozinho; e a síntese dá destino a toda contribuição.

## 3. Acionamento

```yaml
---
name: equipe-especialistas
description: >-
  Conduz reuniões estruturadas de especialistas para juntar especialidades
  numa versão melhor que a de qualquer uma sozinha, sem fazer média e sem
  perder o que só um sabe. Cada especialista se prepara sozinho, por
  escrito; o líder abre com o mapa das preparações, sem opinar; os membros
  falam em rodadas, discordam com motivo, só contrariam o especialista da
  área com contraprova e fazem as contas em Python; o crítico confere ao
  fim de cada rodada; o líder sintetiza com o que mudou, o dissenso e o que
  mudaria a decisão. Modos: elaboração, verificação (parecer técnico, sem
  veredito), integração do tema, reunião individual e reuniões paralelas
  com fusão. Use quando a condutora da Etapa 1 pedir uma reunião de equipe
  ou quando o usuário pedir que especialistas discutam e elaborem algo
  juntos. Não use para julgar ou votar ideias, gerar alternativas às cegas,
  recrutar especialistas ou responder como um especialista só.
license: (a definir)
compatibility: Agentes que se possam retomar, ou recriar com a ata; Python 3 para os scripts; usa a pesquisa-cientifica
metadata:
  versao: "0.1"
---
```

- **Só os campos do padrão aberto,** como nas outras skills.
- **Chamada pelo nome é o caminho principal:** "Use a skill `equipe-especialistas`, modo elaboração, passo 7 da 4.3, dose completa, reunião paralela a." Fora da Etapa 1, a skill roda avulsa (seção 5.4).
- **Três leitores.** A mesa lê o `SKILL.md` e as referências da mesa e do ambiente; o líder, o especialista e o crítico recebem, no brief, só a referência do seu papel (seção 11). Nenhum membro precisa acionar a skill.

| Deve acionar | Não deve acionar (quase acertos) |
| --- | --- |
| "Roda a reunião de elaboração da 4.3, dose completa." | "Qual das três hipóteses é a melhor?" (julgar é do conselho) |
| "Conduz a verificação do 3.5: o 'refuta se' pede estatística e fatores humanos juntos." | "Que especialistas a 4.3 precisa?" (é da `especialistas`) |
| "Fecha o tema 2 com a integração em equipe." | "Gera alternativas sem ver a minha versão." (geradores cegos, isolados) |
| "A estatística revisa essa conta sozinha, com o crítico." (individual) | "Faz os membros do conselho debaterem até concordar." (o conselho julga isolado, e a troca dele não busca acordo) |
| "Junta as duas reuniões paralelas da 4.3." (fusão) | "Pesquisa o que se sabe sobre passagem de plantão." (é da `pesquisa-cientifica`) |
| "Põe três especialistas para discutir e melhorar o meu plano de pesquisa." (avulso) | "Faz uma votação entre as opções e me diz a mais votada." (voto e média ficam de fora) |

A lista completa, com 10 de cada lado, entra nos testes (seção 14).

## 4. Contrato de entrada e saída

| Modo | Recebe | Entrega |
| --- | --- | --- |
| Elaboração (passo 7) | A pauta: a pergunta, o que decidir, o que entregar, a validação que vem depois, as restrições preservadas e a dose; a versão base, sem autoria; a ficha e o bloco de cada membro; as fichas de fonte de cada um | A ata; a síntese do líder, que vai ao passo 8 como uma das hipóteses, sem autoria; as checagens; os custos |
| Verificação (passo 8) | As afirmações técnicas a verificar, tiradas da hipótese pelo "refuta se", sem autoria; as fichas e os blocos de especialistas que não elaboraram; as fichas de fonte | O parecer técnico, afirmação por afirmação, com cálculos e fontes, sem recomendação nem veredito; a ata |
| Integração (fim do tema) | As saídas aprovadas das sub-etapas do tema, sem autoria; a equipe-base do tema | O relatório de integração: o que combina, o que conflita, com a evidência, a gravidade e o que resolveria; nenhuma decisão |
| Individual | Uma tarefa focada (uma conta, uma revisão da literatura da área, um modelo) e a ficha de um especialista | A entrega, com a revisão do crítico e a resposta a ela |
| Fusão | As sínteses das reuniões paralelas, com rótulos sorteados (A, B, C), e a pauta | A versão fundida, com a origem de cada parte, o que ficou de fora e por quê, e os conflitos mantidos como opções |
| Avulso | Um problema em texto livre e, se houver, os especialistas | A ata e a síntese, sem dossiê |

**Contratos com as outras skills:**

| Skill | Relação |
| --- | --- |
| `etapa-1-cir` | Chama a skill nos passos 7 e 8 e no fechamento do tema; monta a pauta com o `pauta.py` desta skill; é a mesa, no Notion (seção 9): abre as sessões, passa a palavra, entrega a cada um só o que ele pode ver e grava tudo em `equipe/`; leva a síntese ao passo 8 e o parecer ao conselho |
| `especialistas` | Entrega a ficha e o bloco de cada membro, com o selo; na dose completa, a distante tem lugar a partir do 4º membro; recebe da ata o placar por especialidade, para o catálogo |
| `conselho-especialistas` | Recebe a síntese como uma hipótese, sem autoria, ao lado da sua versão e das alternativas, e o parecer da verificação como evidência; o veredito é dele |
| `pesquisa-cientifica` | Os membros usam o modo desenvolver na preparação, para o que a sua especialidade pede; o crítico e a verificação, o modo conferir; o `ata.py fontes` roda o `verificar.py` e o `trecho.py` em toda fonte nova citada numa fala |
| Skill de método do tema (`cir-*`) | Dá a pergunta, o "refuta se", o formato de saída e as ferramentas da sub-etapa, que vão na pauta |
| `grill-embasado` | A equipe nunca pergunta a você. O que ela precisaria saber sai na síntese, em "Perguntas para você", e a condutora leva ao passo 9 |

## 5. Modos e doses

### 5.1 Modos

| Modo | Quando | Quem | Rodadas | Sai |
| --- | --- | --- | --- | --- |
| Elaboração | Passo 7, nas doses padrão e completa | Líder, de 3 a 5 especialistas e o crítico | 2; até 3 na completa | Síntese |
| Verificação | Passo 8 da dose completa, quando o "refuta se" exige combinar especialidades | Líder, 2 ou 3 especialistas que não elaboraram e o crítico | 1 ou 2 | Parecer técnico |
| Integração | Fechamento de cada tema, antes da validação integrada | Líder, a equipe-base do tema e o crítico | 1; a 2ª só com conflito que bloqueia | Relatório de integração |
| Individual | Uma tarefa focada, dentro de outro modo ou avulsa | 1 especialista e o crítico | 1 ou 2 revisões | Entrega revista |
| Fusão | Depois das reuniões paralelas | Um líder novo e o crítico | 1 | Versão fundida |
| Avulso | Fora da Etapa 1 | Como na elaboração | 2 | Ata e síntese |

### 5.2 Doses

| Formação | Leve | Padrão | Completa |
| --- | --- | --- | --- |
| Elaboração | Sem reunião: 1 especialista, sozinho, propõe várias variações, no formato da preparação | Líder, 3 especialistas e o crítico, em 2 rodadas | Líder, de 3 a 5 e o crítico, em até 3 rodadas; quando o plano de dose marca a saída como central, 2 ou 3 reuniões paralelas e a fusão |
| Verificação | — | — | Quando o "refuta se" pede: líder, 2 ou 3 que não elaboraram e o crítico, em 1 ou 2 rodadas |
- **Parada antecipada.** A partir da rodada 2, se todos passarem e o crítico não deixar ponto aberto, a reunião vai às posições finais.
- **Sem rodada extra.** O impasse não ganha rodada: vira dissenso ou opções na síntese, para o conselho e para você. Mais rodadas antes de decidir pioraram o resultado ([Kaesberg et al.](https://arxiv.org/abs/2502.19130)) e aumentam o conformismo (achado 3). Outra reunião, só a seu pedido, no passo 9.
- **Reuniões paralelas.** Mesma pauta e mesma composição, como no Virtual Lab e na seção 5.2 do plano da `especialistas`; cada uma com a sua ordem sorteada e em sessões próprias, sem ver as outras. O teste compara com paralelas que trocam um membro pela reserva do mapa (seção 14).
- **Fusão.** Um líder que não conduziu nenhuma das paralelas recebe as sínteses com rótulos sorteados, sem saber qual veio de qual reunião, e junta as melhores partes, dizendo de onde veio cada uma; o que conflita fica como opções. O crítico revisa.
- **A distante.** Na dose completa, entra na equipe a partir do 4º membro (seção 5.3 do plano da `especialistas`). Prepara-se e fala como os outros, e a fala dela traz o problema análogo, como ele é resolvido lá e o que se transfere. Ideias distantes atrapalharam quando chegaram no meio de uma geração produtiva ([Chan et al.](https://doi.org/10.1145/3059454.3059455)); como aqui cada um já terminou a sua preparação antes de ouvir a distante, ela entra desde o início, e o teste compara com a distante só no impasse (seção 14).

### 5.3 Reunião individual

Um especialista e o crítico, como nas reuniões individuais do Virtual Lab. O especialista entrega; o crítico aponta o que conferir ou corrigir; o especialista responde e corrige, no máximo duas vezes. Serve a uma conta, a uma revisão da literatura da área ou a um modelo, quando a condutora ou o líder pede, e a entrega vai à ata da reunião que a pediu.

### 5.4 Modo avulso

Fora da Etapa 1, a skill monta a pauta a partir do pedido, usa os especialistas que você indicar ou os que a `especialistas` montar no modo avulso, e grava a ata e a síntese numa pasta local. Quem faz a mesa é a própria sessão que chamou a skill. Sem dossiê, a versão base é o texto do pedido, e o brief diz só "versão base", sem dizer de quem é.

## 6. Passos

### 6.1 Antes da reunião

1. **Pauta** (`pauta.py montar` e `pauta.py validar`): o modo, a sub-etapa e a dose; a pergunta; o que decidir; o que entregar, no formato da `cir-*`; a validação que vem depois, com o "refuta se"; as restrições preservadas; a versão base, sem autoria; e o número de rodadas. O `validar` recusa a pauta sem pergunta ou sem formato de entrega, com marca de autoria ("a sua versão", "o usuário propôs") ou com preferência ("a melhor opção parece…").
2. **Formação** (`mesa.py iniciar`): confere a ficha e o selo de cada membro, dá a cada um uma sigla (ES, FH…) e sorteia a ordem de fala de cada rodada, com a semente. Grava o `mesa.json`.
3. **Sessões:** uma por membro, com o nome da ficha (`estatistica-1`), incógnita, num computador novo e no modelo do mapa. O brief, montado pelo `brief.py` da condutora, sem reescrever: o bloco de especialidade no topo; a referência do papel; o que a `cir-*` diz da sub-etapa; as fichas de fonte do membro, a pauta e a versão base; e o envelope no fim, com a tarefa. O líder e o crítico recebem o mesmo, sem bloco de especialidade.

### 6.2 Preparação, cada um sozinho

- **Em paralelo, sem ver as outras,** cada especialista escreve a preparação (seção 8.2): a leitura do problema pela sua especialidade; as contribuições, cada uma com um código (ES-1, ES-2) e a evidência (ficha de fonte, `esp-*`, conta ou "conhecimento geral, sem fonte"); o que pode estar errado na versão base; perguntas a outras especialidades; e o que não sabe.
- **Até umas 800 palavras,** fora o código. Contas em Python, com o código e o resultado. Fonte nova entra como "a conferir".
- **O `ata.py preparacoes`** confere o selo, os códigos e o formato. A reunião só abre com todas as preparações gravadas, ou com o tempo limite (seção 13).

### 6.3 Abertura do líder

- **O líder lê as preparações e escreve a abertura** (seção 8.3): as convergências; as divergências (D1, D2…), com quem está em cada lado; as contribuições que só um trouxe, cada uma com uma pergunta aos outros; o que a pauta pede e ninguém cobriu; e as perguntas que os especialistas fizeram uns aos outros, dirigidas por nome.
- **Sem preferência própria.** O `ata.py abertura` confere que todo código aparece no mapa e marca frases de preferência para o crítico.
- **A mesa entrega a todos** as preparações inteiras e a abertura.

### 6.4 Rodadas

1. **Falas, na ordem sorteada.** Cada especialista recebe o que foi dito desde a sua última fala e responde (seção 8.4): às divergências e às perguntas dirigidas a ele; concordo ou discordo, com o motivo e os códigos; na rodada 1, um ou dois fatos da sua especialidade que ainda não estão na mesa e um motivo pelo qual a proposta à frente pode estar errada; nas seguintes, só o que for novo, ou "passo". Para contrariar quem tem autoridade na área, a contraprova: fonte, conta ou contraexemplo. Quem muda de posição diz por quê, citando a fala. Até umas 400 palavras.
2. **O crítico, por último** (seção 8.5): pontos K1, K2… sobre método, contas, fontes e lógica; o que a pauta pede e ninguém respondeu; mudanças de posição sem motivo; meio-termos sem evidência. Diz também o que conferiu sem achar nada. Não defende posição.
3. **O líder fecha a rodada** (seção 8.6): uma decisão provisória em cada divergência, com o motivo e os códigos; o que segue aberto; e perguntas dirigidas para a rodada seguinte, inclusive as do crítico. Não traz conteúdo novo.
4. **Checagens entre as rodadas.** O `ata.py fontes` roda os scripts da `pesquisa-cientifica` nas fontes novas; o `ata.py contas` refaz cada conta num ambiente limpo e compara o resultado. O que não confere vai a todos na rodada seguinte.
5. **A reunião para** depois da última rodada da dose, ou antes, pela parada antecipada.

### 6.5 Posições finais

Em paralelo, sem ver as dos outros, cada especialista escreve (seção 8.7): o que apoia; o que mudou desde a preparação e por quê, citando a fala; a evidência mais forte e a maior incerteza; a discordância que sobra; e o que mudaria a sua posição. É a fase de decisão do protocolo do HiddenBench (achado 1). O `ata.py posicoes` compara com a preparação e marca a mudança sem motivo.

### 6.6 Síntese

1. **O líder escreve a síntese** (seção 8.8): a versão, no formato da `cir-*`; o porquê, decisão por decisão; o que mudou da versão base; o destino de cada contribuição; o que foi rejeitado, e por quê; o dissenso, com o melhor argumento de cada lado; o que mudaria a decisão; as lacunas; as perguntas para você; e o que o próprio líder acrescentou, marcado. A síntese pode contrariar a maioria, se a evidência pedir.
2. **O `sintese.py` confere:** toda contribuição tem destino; toda discordância das posições finais está no dissenso; toda divergência está decidida, no dissenso ou em opções; nenhum número sem conta ou fonte conferida. E marca meio-termos sem motivo: um valor entre duas posições, sem evidência citada.
3. **O crítico revisa a síntese, uma vez** (seção 8.9): fidelidade à ata e às posições finais, contas e fontes. O líder aceita cada ponto ou o mantém, com o motivo, e a síntese fecha.

### 6.7 Entrega

A mesa grava tudo em `equipe/<reunião>/` (seção 8.13), roda o `custos.py` e o `ata.py placar` e devolve à condutora um resumo de umas 300 palavras: o que se decidiu, o dissenso, as perguntas para você, as checagens e o custo. A síntese segue ao passo 8 sem rótulo de equipe, como as outras hipóteses.

### 6.8 Verificação

- **Pauta:** a condutora, pela `cir-*`, escreve as afirmações técnicas a verificar (A1, A2…), a partir do "refuta se" e antes de qualquer veredito. O `pauta.py validar` recusa afirmação com autoria ou com juízo sobre a hipótese.
- **Os mesmos passos,** com especialistas que não elaboraram a versão, em 1 ou 2 rodadas.
- **Sai o parecer técnico** (seção 8.10), afirmação por afirmação: os cálculos, refeitos; as fontes, conferidas; a conclusão técnica (sustenta, não sustenta ou indeterminado), a incerteza e a especialidade que responde por ela; o dissenso; e o que mudaria a conclusão.
- **Nunca recomendação nem veredito** sobre a hipótese; o `parecer.py` recusa. O conselho recebe o parecer como evidência, sem autoria, e julga sozinho.

### 6.9 Integração

As saídas aprovadas das sub-etapas do tema, sem autoria, vão à equipe-base do tema. Na preparação, cada um procura conflitos, sinergias e dependências entre as saídas, pela sua especialidade; a reunião segue os mesmos passos. Sai o relatório de integração (seção 8.11): cada conflito, com as saídas envolvidas, a evidência, a gravidade (bloqueia, pede ajuste ou menor) e o que resolveria, sem decidir. Vai à validação integrada e a você.

### 6.10 Fusão

O líder de fusão recebe as sínteses, com rótulos sorteados, e a pauta, mas não as atas. Escreve a versão fundida (seção 8.12): junta as melhores partes, diz de onde veio cada uma e o que ficou de fora, e por quê, e mantém como opções o que conflita. O `fusao.py` confere a origem de cada parte e se o dissenso de cada síntese continua à vista; o crítico revisa uma vez.

## 7. Regras que valem o tempo todo

| Regra | Por quê | Como se garante |
| --- | --- | --- |
| 1. **Cada um se prepara sozinho, por escrito, antes de ouvir os outros.** | Em grupo, o que todos sabem domina, e o que só um sabe se perde (achado 1); rascunhar antes de discutir rendeu mais ([Kaesberg et al.](https://arxiv.org/abs/2502.19130)) | A rodada 1 só abre com as preparações gravadas; `ata.py preparacoes` |
| 2. **Tudo o que foi preparado chega a todos.** | Quando cada agente revelou tudo no começo, o acerto foi a 92,6% e 98,2% (achado 1) | A mesa entrega as preparações inteiras, sem resumo |
| 3. **Nada some sem motivo.** | O que mais pesou nos grupos humanos foi a parte da informação única que chegou a ser dita (achado 1) | Código em toda contribuição; destino na síntese; `sintese.py` |
| 4. **O objetivo é a melhor versão, não o acordo.** | Pedir coesão aumenta a discordância guardada; pedir honestidade a reduz (achado 3) | A instrução de honestidade vai no brief de todos; nenhuma pauta pede consenso |
| 5. **Quem discorda diz; quem muda diz por quê.** | Modelos trocam o certo pelo errado para concordar (achado 3) | O formato da fala e da posição final; `ata.py posicoes` |
| 6. **Autoridade por especialidade, com contraprova.** | Equipes desperdiçam o especialista (achado 2). Mas a mesma deferência daria força a um especialista errado; por isso ela pede lastro | Vale só para quem fala com `esp-*` ou fonte conferida, e cai com fonte, conta ou contraexemplo. Sem skill, o especialista tem a palavra, não a autoridade: a ata o marca, e vale o argumento |
| 7. **Contas em Python, refeitas pela mesa.** | Modelos acertam mais quando escrevem o programa do que quando calculam de cabeça ([Gao et al., PAL](https://arxiv.org/abs/2211.10435)) | `ata.py contas`; número sem conta ou fonte não entra na síntese |
| 8. **Fonte nova passa pela conferência.** | Modelos aceitam evidência coerente e convincente mesmo quando ela está errada (achado 5 do plano da `especialistas`) | `ata.py fontes`; fonte que não confere não sustenta decisão |
| 9. **Identidade oculta.** | Modelos seguem mais o próprio grupo (achado 4) | Nomes funcionais; nenhum modelo nas falas; versão base sem autoria; `pauta.py validar` e a vigia |
| 10. **O líder abre sem opinar e decide pela evidência.** | Líder que dá a preferência cedo leva o grupo a ela (achado 7) | O formato da abertura; `ata.py abertura`; a revisão do crítico |
| 11. **O que não combina não se funde.** | O meio-termo entre o especialista e os outros é o que faz a equipe perder (achado 2) | Opções separadas, com o que decidiria; `sintese.py` e `fusao.py` |
| 12. **O crítico confere, sem oposição de fachada.** | Advogado do diabo rende menos que a discordância de verdade, e discordância imposta pode derrubar o acerto (achado 7) | O crítico registra o que conferiu; "nada a apontar" vale, com o que foi conferido |
| 13. **A equipe não julga nem gera às cegas.** | Julgar é do conselho isolado; gerar alternativas, dos geradores cegos (seção 2.5 do fluxograma) | Nenhuma pauta pede ranking ou voto; `parecer.py` recusa veredito |
| 14. **A mesa não opina.** | A condutora não opina (seção 3 do plano geral); a mesa só passa a palavra | As falas vão sem edição; o teste de aderência compara o que foi enviado com o que chegou |
| 15. **Ninguém lê o dossiê.** | Só a condutora lê e grava o dossiê (seção 3 do plano geral) | Sessões incógnitas, num computador novo, com auditoria dos eventos |

**Pensamentos e realidade:**

| Pensamento | Realidade |
| --- | --- |
| "Todos concordaram na rodada 1; a reunião foi ótima." | Acordo rápido é sinal de alerta. O crítico procura o que falta, e a posição final mostra se era acordo ou silêncio. |
| "Fico no meio: 3 minutos, entre os 2 e os 4." | Meio-termo sem evidência é média. Escolha pela evidência, ou mantenha as opções, com o que decidiria. |
| "Ela é a especialista; sigo sem conferir." | A autoridade pede lastro e cai com contraprova. Conferir é do crítico e dos scripts. |
| "Resumo as preparações para caber na abertura." | As preparações vão inteiras a todos. A abertura organiza, não substitui. |
| "Abro dizendo qual proposta parece melhor, para ganhar tempo." | O grupo segue a preferência que o líder dá cedo. A abertura é só o mapa. |
| "A conta é simples; faço de cabeça." | Toda conta roda em Python, e a mesa a refaz. |
| "Mais uma rodada resolve o impasse." | Mais rodadas pioram e aumentam o conformismo. O impasse vira opções. |
| "Discordo para a reunião não ficar morna." | Oposição de fachada não ajuda e pode derrubar o acerto. Sem nada novo, "passo". |
| "A maioria pensa diferente; devem saber algo." | Quem muda diz por quê, citando a fala que convenceu. Mudar sem motivo é marcado. |
| "A fonte parece certa; cito direto." | Fonte nova é "a conferir" até o `ata.py fontes` rodar. |
| "Digo ao conselho que a hipótese passa no teste do impossível." | A verificação diz se cada afirmação técnica se sustenta. O veredito é do conselho. |
| "Leio o dossiê para entender o contexto." | Só a condutora lê o dossiê. O que falta vira pergunta para você, na síntese. |

## 8. Formatos e modelos de documento

O exemplo é o da seção 8 do plano da `especialistas`: a passagem do paciente da cirurgia para a UTI, na 4.3, com a mesma formação e as mesmas fichas.

| Código | O que é |
| --- | --- |
| `ES-1` | Contribuição: a sigla do membro e o número, dados na preparação |
| `D1` | Divergência, nomeada pelo líder na abertura |
| `K1` | Ponto do crítico |
| `N1` | Fonte nova, a conferir |
| `V1` | Variação da versão |
| `A1` | Afirmação a verificar, no parecer |
| `I1` | Conflito, no relatório de integração |

### 8.1 Pauta

```markdown
# Pauta · 4.3-r1a · elaboração
sub-etapa: 4.3 · passo 7 · dose completa · paralela a, de 2 · fusão em 4.3-r1
skill de método: cir-divergencia
formação: fatores-humanos-1 (FH) · intensiva-1 (IN) · estatistica-1 (ES) · troca-rapida-1 (TR, distante) · critico-1 · lider-1
fichas: E-4.3-p7-01 a 06
rodadas: até 3, com parada antecipada a partir da 2
ordem (semente 48213): r1 ES TR FH IN · r2 IN FH ES TR · r3 TR IN ES FH

## Pergunta
Qual a melhor versão da família de conceito da versão base para o desafio 4.2-3, "como poderíamos passar o paciente da cirurgia para a UTI sem perder informação, mesmo sob pressa?"

## Decidir
1. Que passos a passagem tem, em que ordem, e quem conduz cada um
2. Como lidar com a pressa (contradição 2.3-1, rapidez × completude)
3. Como saber se funcionou, com as passagens que o serviço tem

## Entregar
A família no formato da cir-divergencia: princípio, mecanismo, variações e o que cada uma resolve do job map

## Depois
Conselho de triagem, ideia a ideia; nada é descartado

## Restrições preservadas
- do 3.5: "zero omissões" não se demonstra; a meta é uma taxa de omissão com limite superior de 95% abaixo de 1%

## Versão base · sem autoria
Antes de mover o paciente, a equipe para 2 minutos. Primeiro o equipamento passa para a UTI; depois, a informação, numa lista falada, na mesma ordem toda vez.
```

### 8.2 Preparação

```markdown
esp-estatistica@1.2 · 3f9a1c
# Preparação · estatistica-1 (ES) · 4.3-r1a

## Leitura pela especialidade
O que decide se a família funciona é medir omissões raras com as poucas passagens que um serviço tem.

## Contribuições
ES-1 · Contar as omissões por item da lista, não por passagem
- por quê: dá mais eventos por passagem e mostra que itens somem
- evidência: esp-estatistica, módulo eventos-raros; F-031
- muda na versão base: a lista ganha um registro de que itens foram ditos
ES-2 · Acompanhar com gráfico de controle, não com antes e depois
- por quê: com poucas passagens, o antes e depois confunde a mudança com a tendência do serviço
- evidência: F-044; N1
- muda na versão base: acrescenta como saber se funcionou

## O que pode estar errado na versão base
"2 minutos" não tem fonte: pode ser pouco para o paciente grave e muito para o estável.

## Perguntas a outras especialidades
- intensiva: que itens mais fazem falta quando chegam tarde?
- fatores humanos: a lista falada aguenta interrupção no meio?

## Contas
    from math import ceil, log
    # passagens seguidas sem omissão para o limite superior de 95% ficar abaixo de 1%
    print(ceil(log(0.05) / log(0.99)))
resultado: 299

## Fontes novas, a conferir
- N1 · artigo sobre gráficos de controle em serviços de saúde, com o DOI informado

## O que não sei
Quantas passagens por semana o serviço tem.
```

### 8.3 Abertura do líder

```markdown
# Abertura · lider-1 · 4.3-r1a

## Convergências
- Uma pausa antes de mover, com papéis definidos: FH-1, IN-2, TR-1
- A informação numa ordem fixa: FH-2, IN-1

## Divergências
- D1 · Quando a pausa acaba: em 2 minutos (versão base) × quando a lista acaba (TR-2) × pela gravidade do paciente (IN-3)
- D2 · Quem conduz: o anestesista (IN-1) × alguém sem tarefa de equipamento (TR-1, FH-3)

## O que só um trouxe
- ES-1 · contar por item · aos outros: a lista de IN-1 tem itens que se contem um a um?
- ES-2 · gráfico de controle · aos outros: o serviço tem passagens para ele?
- TR-3 · ensaiar a passagem, como se ensaia o pit stop · aos outros: o que se ensaia sem paciente?

## O que a pauta pede e ninguém cobriu
- o decidir 3, além de ES

## Perguntas entre especialistas
- a intensiva-1, de ES: que itens mais fazem falta quando chegam tarde?
- a fatores-humanos-1, de ES: a lista aguenta interrupção?
```

### 8.4 Fala

```markdown
troca-rapida-1 (TR) · rodada 1 · sem skill · LAC-014
- D1: fico com "quando a lista acaba" (TR-2). No pit stop, o carro sai pelo sinal de quem confere, não pelo relógio · conhecimento geral, sem fonte
- D2: mantenho TR-1 e somo FH-3: quem segura o tubo não conduz a lista
- fato novo: na aviação, a lista é lida por um e respondida em voz alta por outro; responde à pergunta de ES sobre interrupção
- contra a proposta à frente (pausa de 2 minutos): um tempo fixo vira meta, e a equipe corre para cumpri-lo
```

### 8.5 Crítica da rodada

```markdown
critico-1 · rodada 1
- K1 · ES-2: o gráfico supõe passagens independentes, e as do mesmo plantão não são. ES: como isso muda o limite?
- K2 · FH-3 cita F-052 para "quem segura o tubo não conduz a lista"; o trecho de F-052 fala de papéis definidos, não disso. FH: outro trecho, ou a marca de conhecimento geral
- K3 · decidir 3: ninguém disse quantas passagens por semana o serviço tem
- conferido, sem apontamento: a conta de ES, reproduzida pelo ata.py contas
```

### 8.6 Fechamento da rodada

```markdown
lider-1 · fecha a rodada 1
- D1 · provisório: a pausa acaba quando a lista acaba (TR-2), com teto a definir; ninguém trouxe fonte para os 2 minutos; IN-3 segue aberto
- D2 · provisório: conduz alguém sem tarefa de equipamento (TR-1, FH-3), pendente de K2; IN-1 não trouxe contraprova
- rodada 2: intensiva-1, K3 e IN-3 · estatistica-1, K1 · fatores-humanos-1, K2

checagem · entre r1 e r2
- fontes: N1 (ES) não confere: o DOI é de outro artigo (verificar.py)
- contas: ES, 1 de 1 reproduzida
```

### 8.7 Posição final

```markdown
fatores-humanos-1 (FH) · posição final · sem skill · LAC-012
- apoio: pausa até a lista acabar, com teto de 4 minutos; conduz quem não segura equipamento; lista lida e respondida
- mudou: aceitei "lida e respondida" (TR, rodada 1), porque resolve a interrupção que levantei (FH-2)
- evidência mais forte: F-052, a passagem redesenhada com a Fórmula 1 e a aviação, com menos omissões por passagem
- maior incerteza: o teto de 4 minutos não tem fonte
- discordância que sobra: com IN-3, teto fixo, e não pela gravidade
- mudaria se: uma fonte mostrar que a lista lida e respondida atrasa o paciente instável
```

### 8.8 Síntese

```markdown
# Síntese · 4.3-r1a · lider-1
checagem: sintese.py ok · contas 2 de 2 reproduzidas · fontes 3 conferidas e 1 que não confere (N1)

## Versão
Família "passagem conduzida por lista lida e respondida". Princípio: a passagem acaba quando a informação acaba, não quando o relógio manda. Mecanismo: … Variações: V1, teto fixo de 4 minutos; V2, teto pela gravidade. Resolve, no job map: …

## Por quê
- D1: … (TR-2; F-052)
- D2: … (TR-1, FH-3; K2 respondido com outro trecho de F-052)

## O que mudou da versão base
- 2 minutos fixos → até a lista acabar, com teto (D1)
- lista falada → lida e respondida (TR, rodada 1)
- acrescentado: contar as omissões por item e acompanhar por plantão (ES-1, ES-2, K1)

## Destino das contribuições
- ES-1 entrou · ES-2 mudou: limite com passagens agrupadas por plantão (K1); N1 não confere e saiu
- IN-1 rejeitada: sem contraprova a FH-3 (D2) · IN-3 em dissenso (D1)
- TR-3 em aberto: ninguém disse quem conduziria o ensaio na UTI
- …

## Dissenso
- D1, o teto: IN quer o teto pela gravidade (melhor argumento: o paciente instável não espera a lista); FH e TR, o teto fixo (melhor argumento: regra simples sob pressa). Decidiria: o tempo das passagens com paciente instável no serviço. Ficam V1 e V2

## O que mudaria a decisão
- uma fonte de que a lista lida e respondida atrasa o paciente instável

## Lacunas
- passagens por semana (K3): sem esse número, o decidir 3 fica sem tamanho de amostra

## Perguntas para você
- Quantas passagens da cirurgia para a UTI há por semana no serviço que você tem em mente?

## Do líder
- nada acrescentado
```

### 8.9 Revisão do crítico

```markdown
critico-1 · revisão da síntese
- K6 · IN-3 está em dissenso, mas a versão põe V1 antes de V2 sem dizer por quê. Dar o motivo, ou pôr as duas em pé de igualdade
- sem apontamento: o dissenso de D1 confere com as posições finais; contas e fontes conferem com o checagem.json

resposta do líder: aceito K6; V1 e V2 em pé de igualdade, com o que decidiria entre elas
```

### 8.10 Parecer técnico

```markdown
# Parecer técnico · P-3.5-1 · equipe/3.5-v1
afirmações: do "refuta se" do 3.5, sem autoria · equipe: estatistica-2 (ES), fatores-humanos-2 (FH), critico-2, lider-2 · 2 rodadas
não é veredito: o conselho julga a hipótese; aqui se diz só se cada afirmação técnica se sustenta

## A1 · Não se pode demonstrar "zero omissões" com um número finito de passagens
- cálculos: com 0 omissões em 50 passagens, o limite superior unilateral de 95% da taxa é 1 − 0,05^(1/50) ≈ 5,8%; para ficar abaixo de 1%, são precisas 299 passagens seguidas sem omissão (ata.py contas: reproduzido)
- fontes: F-031, conferida
- conclusão técnica: sustenta. Amostra finita só limita a taxa; nunca a zera
- incerteza: passagens do mesmo plantão não são independentes, o que alarga o limite
- especialidade: estatística

## A2 · Uma passagem sem nenhuma omissão é impossível em princípio
- fontes: F-052, conferida: o redesenho reduziu as omissões, e nada nela as torna inevitáveis
- conclusão técnica: não sustenta. Nenhuma lei lógica, física ou cognitiva conhecida impede a passagem sem omissão; o que existe é a fronteira de medição de A1
- incerteza: os limites da memória de trabalho sob interrupção
- especialidade: fatores humanos
- dissenso: FH acha que a interrupção torna a omissão inevitável em parte das passagens; ES, que isso diz quão rara ela é, não que seja impossível. Decidiria: estudos de omissão com lista lida e respondida sob interrupção
- mudaria se: uma prova de que algum item não pode ser transmitido em toda passagem
```

### 8.11 Relatório de integração

```markdown
# Integração · tema 2 · equipe/tema2-i1
saídas: 2.1 a 2.7, sem autoria · não decide: vai à validação integrada e a você

## Conflitos
- I1 · 2.2 × 2.6: a causa 2.2-4 (erros raros e mal registrados) não tem caso no banco que a exercite
  - evidência: nenhum caso do 2.6 tem omissão rara (ES, rodada 1)
  - gravidade: pede ajuste; sem caso, a prova do tema 5 não testa a causa
  - resolveria: (a) um caso reconstruído de um registro de omissão; (b) marcar a causa como não testável no tema 5, com o motivo
- I2 · 2.1 × 2.3: o job map põe o equipamento antes da informação, e a contradição 2.3-1 supõe os dois ao mesmo tempo
  - gravidade: menor; o 2.3 precisa dizer em que etapa do job map a contradição aparece

## Combinam
- a projeção de referência (2.4) cobre as causas 2.2-1 a 2.2-3

## Dependências
- …
```

### 8.12 Fusão

```markdown
# Fusão · 4.3-r1 · lider-3
sínteses: A e B, com rótulos sorteados (semente 77120); o líder não sabe que reunião é qual

## Versão fundida
…

## De onde veio cada parte
- lista lida e respondida: A e B
- teto pela gravidade: B, que trouxe a contraprova de IN; A deixou V1 e V2 em aberto
- contar por item e acompanhar por plantão: A

## Ficou de fora, e por quê
- o ensaio sem paciente (B): nenhuma das duas diz quem o conduz na UTI; vai como variação em aberto

## Conflitos mantidos como opções
- nenhum
```

### 8.13 Pastas e arquivos

| Pasta | Reunião |
| --- | --- |
| `equipe/<sub-etapa>-r<n>/` | Elaboração; as paralelas em `-r1a` e `-r1b`, e a fusão em `-r1` |
| `equipe/<sub-etapa>-v<n>/` | Verificação |
| `equipe/tema<k>-i<n>/` | Integração |
| `equipe/<sub-etapa>-u<n>/` | Individual |

| Arquivo | O que guarda |
| --- | --- |
| `pauta.md` | A pauta validada |
| `mesa.json` | A formação, as siglas, as sessões, o modelo de cada membro, a ordem de cada rodada, a semente e a situação de cada fala |
| `preparacoes/<sigla>.md` | As preparações, como chegaram |
| `ata.md` | A abertura, as falas, as críticas, os fechamentos e as checagens, na ordem |
| `posicoes/<sigla>.md` | As posições finais |
| `sintese.md`, `parecer.md`, `integracao.md` ou `fusao.md` | A saída do modo, com a revisão do crítico e a resposta |
| `checagem.json` | O resultado de cada script: preparações, abertura, fontes, contas, posições e saída |
| `custos.json` | Tokens, quando o ambiente dá; tempo, sessões, chamadas e créditos; e o contexto que a reunião ocupou na mesa |

## 9. Transporte

O protocolo é o mesmo em qualquer ambiente; o transporte muda só o jeito de passar a palavra e de entregar a cada um o que ele pode ver. Quem faz isso é a **mesa**: abre as sessões, entrega a cada membro só o que ele vê, recolhe as falas, roda os scripts e grava a ata. A mesa não opina, não resume e não edita fala nenhuma. No Notion, na v1, a mesa é a condutora.

| Variante | Como | Quando | Limite |
| --- | --- | --- | --- |
| 1. **Sessões que retomam** (padrão) | Uma sessão por membro, que guarda o próprio contexto: a preparação, o que ouviu e o que disse. A cada vez, a mesa manda só o que foi dito desde a última fala dele. No Notion, sessões filhas incógnitas, num computador novo, com o nome da ficha; no Claude Code, subagentes retomados pelo ID com o `SendMessage`, sem ligar as equipes de agentes ([Claude Code: subagentes](https://code.claude.com/docs/en/sub-agents)) | Sempre, na v1 | Toda fala passa pelo contexto da mesa, que no Notion é o da condutora |
| 2. **Sem estado,** como no Virtual Lab | Cada fala é uma sessão nova, com o brief, a preparação do membro e a ata até ali | Quando uma sessão se perde; para membros de outras famílias, pelo adaptador, na fase 10; e no teste | Mais tokens por fala; o membro guarda só o que está na ata |
| 3. **Mesa delegada** | Uma sessão própria faz a mesa: abre as sessões dos membros e devolve à condutora só o resumo e os arquivos | Se proteger o contexto da condutora render mais | No Claude Code, um subagente que abre subagentes, até três níveis abaixo da conversa principal, por padrão ([Claude Code: subagentes](https://code.claude.com/docs/en/sub-agents)); no Notion, uma sessão filha, se o teste da fase 3 mostrar que ela abre sessões; senão, um Custom Agent do Notion, pela regra "Universalidade primeiro"; outro harness só para as reuniões (Claude Code, Codex, agy ou outro); ou você abre as sessões à mão, com os briefs prontos (seção 17) |
| 4. **Equipes de agentes do Claude Code** | Os membros são colegas, que trocam mensagens diretas e dividem uma lista de tarefas | Só no teste da fase 10 | Experimental e desligado por padrão; só em sessão interativa; uma equipe por sessão, sem equipes aninhadas; os colegas não voltam quando a sessão é retomada; o líder da equipe é sempre a sessão principal, que conhece a autoria, então o nosso líder seria um colega; os colegas carregam o `CLAUDE.md`, os servidores MCP e as skills do projeto, e o campo `skills` da definição não vale para eles ([Claude Code: equipes de agentes](https://code.claude.com/docs/en/agent-teams)) |
- **No Notion:** os membros são disparados em paralelo na preparação e nas posições finais, com aviso de conclusão; nas rodadas, um de cada vez, na ordem do `mesa.json`, por mensagem à mesma sessão. O modelo de cada sessão é o do mapa que você aprovou no 0.3. Depois de cada reunião, a condutora lista os eventos de cada sessão: uma busca ou leitura no workspace marca a sessão, e, se ela leu algo sigiloso, a reunião se refaz com outra sessão e o brief reforçado, como no conselho (seção 9.1 do plano do conselho).
- **No Claude Code:** a sessão principal é a mesa, e cada papel tem uma definição de subagente no plugin (seção 12), com `omitClaudeMd: true` e só as ferramentas do papel, como os agentes cegos do conselho. Nomes só endereçam subagentes com as equipes de agentes ligadas; o ID funciona sem elas ([Claude Code: subagentes](https://code.claude.com/docs/en/sub-agents)).
- **O contexto da condutora é critério.** Numa reunião completa, com 5 membros e 3 rodadas, umas 30 falas passam pela mesa; com paralelas, o dobro. A mesa grava cada fala em arquivo e devolve à conversa com você só o resumo, mas, na variante 1, tudo passa pelo contexto dela. O teste mede quanto do contexto cada reunião ocupa e se isso piora o resto da sub-etapa; se piorar, entra a mesa delegada.
- **Outras famílias, na fase 10,** entram pelo adaptador do conselho, no jeito sem estado: a cada fala, recebem o brief e a ata até ali.

## 10. Modelos e custo

| Papel | Modelo |
| --- | --- |
| Especialistas | O do papel "equipes" no mapa de modelos (0.3). Se o teste da `especialistas` mostrar que um modelo menor com a `esp-*` basta, você pode escolhê-lo no 0.3 |
| Líder e líder de fusão | O do papel "equipes", nunca abaixo dos especialistas |
| Crítico | O do líder |
| Mesa | A condutora, no modelo dela |
- **Multiagente gasta muito.** No sistema de pesquisa da Anthropic, cerca de 15 vezes os tokens de uma conversa ([Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)); num protocolo de deliberação completo, cerca de 62 vezes os de um agente ([Prakash](https://arxiv.org/abs/2603.11781)).
- **Chamadas por reunião.** Na dose padrão, com 3 especialistas e 2 rodadas: 3 preparações, a abertura, 2 rodadas de 3 falas, crítica e fechamento, 3 posições finais, a síntese, a revisão e a resposta, umas 20 chamadas. Na completa, com 5 especialistas e 3 rodadas, umas 35 por reunião; com 2 paralelas e a fusão, umas 75.
- **O `custos.py` registra,** por reunião: os tokens, quando o ambiente dá; o tempo; as sessões e as chamadas; os créditos do Notion; e o contexto da mesa. O teste de custo dá o consumo por modo e por dose, e o custo só decide no empate (critério máximo).

## 11. Arquivos

```
equipe-especialistas/
  SKILL.md                  o protocolo em umas 200 linhas: modos, passos, regras e quem lê o quê
  references/
    protocolo.md            a reunião passo a passo, com o formato de cada fala
    mesa.md                 sessões, ordem, entregas a cada membro, checagens e ata
    lider.md                abertura, fechamento das rodadas, síntese e resposta ao crítico
    especialista.md         preparação, fala e posição final
    critico.md              o que conferir em cada rodada e na síntese
    modos.md                elaboração, verificação, integração, individual, fusão e avulso
    formatos.md             os modelos da seção 8
    regras.md               as 15 regras, com os pensamentos e a realidade
    ambiente-notion.md      sessões filhas, mesa, auditoria e custos no Notion
    ambiente-claude-code.md subagentes retomados, mesa delegada e equipes de agentes (fase 10)
    origem.md               trechos aproveitados, com versão, licença e atribuição
  scripts/
    pauta.py                monta e valida a pauta
    mesa.py                 formação, siglas, ordem sorteada, o que entregar a cada um e mesa.json
    ata.py                  preparacoes, abertura, fontes, contas, posicoes e placar
    sintese.py              destinos, dissenso, meio-termos sem motivo e números sem lastro
    parecer.py              parecer e integração: formato, e nada de recomendação ou veredito
    fusao.py                origem de cada parte e conflitos mantidos
    custos.py               tokens, tempo, sessões, créditos e contexto da mesa
  assets/
    schemas/                pauta, mesa, checagem e custos
    modelos/                pauta, preparação, fala, posição final, síntese, parecer, integração e fusão
  evals/                    os casos da seção 14
```

| Quem | Lê |
| --- | --- |
| Mesa | `SKILL.md`, `mesa.md`, `modos.md` e a referência do ambiente |
| Líder | `lider.md` e os modelos da saída do modo, no brief |
| Especialista | `especialista.md`, no brief, depois do bloco de especialidade |
| Crítico | `critico.md`, no brief |
- **Nenhum membro carrega a skill.** O brief leva, em texto, a referência do papel, como no conselho; assim nada depende de acionamento, e as sessões não leem o workspace.
- **No Notion,** a skill vira uma página do banco de Skills, as referências viram subpáginas, e os scripts e modelos vão em Files, como nas outras skills.
- **O `ata.py fontes`** chama o `verificar.py` e o `trecho.py` da `pesquisa-cientifica`, sem copiá-los.

## 12. Subagentes

| Agente | Formação | Vê | Não vê | Ferramentas |
| --- | --- | --- | --- | --- |
| Especialista | Uma sessão por membro, com o nome da ficha | O seu bloco de especialidade, a referência do papel, a pauta, a versão base sem autoria, as suas fichas de fonte, as preparações dos outros e a ata | A autoria, o modelo dos outros, o dossiê e os casos reservados | Busca e leitura na web, com a `pesquisa-cientifica` no modo desenvolver, e Python |
| Líder | Uma sessão própria | A pauta, a versão base sem autoria, as preparações, a ata e as checagens | A autoria, os modelos, o dossiê e os casos reservados | Busca e leitura na web, só para conferir o que foi citado, e Python |
| Crítico | Uma sessão própria, fora da equipe | O mesmo que o líder | O mesmo que o líder | Busca e leitura na web, com a `pesquisa-cientifica` no modo conferir, e Python |
| Líder de fusão | Uma sessão nova, que não conduziu nenhuma paralela | As sínteses, com rótulos sorteados, e a pauta | As atas, que reunião é qual, a autoria e os modelos | Python |
| Mesa | A condutora, ou uma sessão própria na mesa delegada | Tudo o que a reunião produz | — | Sessões, Python e os scripts |
- **No Claude Code,** os quatro primeiros têm definição no plugin (`equipe-especialista`, `equipe-lider`, `equipe-critico` e `equipe-lider-fusao`), com `omitClaudeMd: true`. A especialidade chega no brief, como no plano da `especialistas` (seção 9), e não há definição por especialidade.
- **Os especialistas veem a especialidade dos outros e se cada um tem `esp-*`,** porque a regra da autoridade depende disso; não veem as fichas inteiras.

## 13. Casos-limite

| Situação | O que a skill faz | Registro |
| --- | --- | --- |
| Membro não responde no tempo limite | A mesa tenta de novo uma vez. Na rodada, segue sem ele, e a ata marca "sem fala". Na preparação, a reunião só abre com pelo menos 2 especialistas e o crítico; senão, volta à condutora | `mesa.json` |
| Sessão perdida no meio da reunião | Retoma sem estado (variante 2): sessão nova, com o brief, a preparação dele e a ata até ali | Ata, com a troca |
| Não há versão base (você disse "não tenho") | A base são as versões que a IA propôs no passo 2, várias, marcadas "origem: IA" | Pauta |
| Uma fala cita autoria, modelo ou algo que o membro não devia ver | A mesa para a reunião e roda a vigia; a fala sai da ata, a sessão é trocada e a rodada se repete | Alerta e auditoria |
| Impasse numa divergência central | Sem rodada extra: a síntese mantém as opções, com o melhor argumento de cada uma e o que decidiria; a condutora pode levá-las ao passo 8 como hipóteses separadas | Síntese |
| Conta que não reproduz | O `ata.py contas` marca, e o autor recebe a diferença na rodada seguinte. Se continuar, o número sai da síntese ou fica "não conferido", sem sustentar decisão | `checagem.json` |
| Fonte que não confere | Marcada "não confere"; o que dependia dela perde o lastro e, com ele, a autoridade; o autor pode trazer outra | `checagem.json` |
| Especialista sem skill contrariado na sua área | Sem `esp-*` e sem fonte conferida, ele tem a palavra, não a autoridade: vale o argumento, e a síntese registra o desacordo | Ata |
| Todos concordam na rodada 1 | O crítico procura o que falta: a pauta, o que só um trouxe, a validação que vem depois. Sem ponto aberto, a reunião para na rodada 2 | Ata |
| O crítico não acha nada | Diz o que conferiu e por que não aponta nada; não inventa objeção | Ata |
| Alguém pede veredito, ranking ou voto | Recusa: julgar é do conselho. Na verificação, o parecer diz só se cada afirmação se sustenta | Ata |
| Uma fala traz preço, cliente, MVP ou tecnologia | A mesa marca para a vigia; a condutora leva o assunto às fronteiras ou ao estacionamento; a síntese não o usa | Vigia |
| O líder acrescenta conteúdo próprio | Vai marcado em "Do líder"; o crítico confere; sem lastro, sai | Síntese |
| Mudança de posição sem motivo | O `ata.py posicoes` marca; na síntese, a mudança não conta como convencimento | `checagem.json` |
| As paralelas chegam a versões quase iguais | A fusão registra; o dado entra no teste das paralelas | `fusao.md` |

## 14. Testes e métricas

**Comparações que decidem o desenho,** todas em julgamento cego:

1. **A conversa vale?** A síntese da equipe contra o melhor especialista sozinho e contra os mesmos especialistas isolados, cada um com a sua preparação, com uma síntese do líder, como o agregador do [MoA](https://arxiv.org/abs/2406.04692). Onde a equipe não vencer, a dose usa os isolados com síntese. É a comparação da seção 13 do plano geral.
2. **Transporte.** No Notion, as sessões que retomam contra o jeito sem estado, e a mesa delegada, pelo caminho que a fase 3 indicar; na fase 10, também as equipes de agentes do Claude Code. Medem-se a qualidade às cegas, a aderência, o isolamento, a estabilidade em 3 execuções, o custo e o contexto da condutora.
3. **Rodadas contra melhoria sem conversa.** Cada um vê as preparações dos outros e reescreve a sua, sem rodadas, e o líder sintetiza, como na melhoria coletiva de [Kaesberg et al.](https://arxiv.org/abs/2502.19130).
4. **Com e sem as posições finais.**
5. **2 contra 3 rodadas,** na dose completa.
6. **Paralelas:** a mesma composição contra a troca de um membro pela reserva; e 2 paralelas com fusão contra uma reunião só.
7. **A distante desde o início contra só no impasse,** como sugere a seção 5.3 do plano da `especialistas`.
8. **A regra da autoridade, com e sem,** em dois tipos de caso: um especialista certo, com a peça que decide (perfil oculto), e um errado, com uma `esp-*` adulterada. A regra fica se ajudar no primeiro sem piorar o segundo; é o dilema que [Pappu et al.](https://arxiv.org/abs/2602.01011) acharam.
9. **Ordem sorteada contra a palavra dada pelo líder** a quem pode resolver o ponto aberto; controlar quem fala melhorou tarefas de perfil oculto ([Babu et al.](https://arxiv.org/abs/2608.20564)).

**Casos de teste,** fora dos projetos reais:

- **Perfil oculto adaptado:** a melhor versão precisa de uma peça que só um membro tem, na sua `esp-*` ou nas suas fontes, e o gabarito diz qual; parte dos casos põe a peça contra a maioria.
- **Elaboração aberta,** julgada às cegas por rubrica (eficácia, criatividade, lastro e o que cada especialidade acrescentou), por 3 juízes em sessões isoladas e, numa amostra, por você.
- **Verificação com gabarito:** afirmações técnicas de resposta conhecida, com afirmações falsas plantadas.
- **Vazamento:** marcadores na sua versão, na autoria e nos casos reservados, procurados em todas as falas e nos eventos das sessões.

| Métrica | Como se mede | Alvo |
| --- | --- | --- |
| Ganho da equipe | Vitórias às cegas sobre o melhor sozinho e sobre os isolados com síntese | Vencer os dois; senão, a dose usa os isolados |
| Informação única | Nos casos de perfil oculto, a parte das peças plantadas que chega à síntese | 90% ou mais |
| Média escondida | Meio-termos sem motivo, pelo `sintese.py` e por um juiz cego | Nenhum |
| Contribuições perdidas | Códigos sem destino | Nenhuma |
| Mudança sem motivo | Posições que mudam sem citar a fala | 5% ou menos |
| Fabricação | Fontes que não conferem e contas que não reproduzem chegando à saída | Nenhuma |
| Aderência | Passos do protocolo cumpridos, pelos scripts e pelo `mesa.json` | Todos |
| Isolamento | Marcadores nas falas e buscas no workspace | Nenhum |
| Estabilidade | As decisões centrais em 3 execuções da mesma pauta | Registrar; a variação alimenta o teste das paralelas |
| Acionamento | Os 10 casos de cada lado da tabela da seção 3 | 9 de 10 de cada lado |
| Custo | Tokens, tempo, créditos e contexto da mesa, por reunião e por dose | Registrar; decide só no empate |

Fica o que vencer; no empate, o mais simples.

## 15. Riscos

| Risco | Mitigação |
| --- | --- |
| A equipe fazer média e ficar abaixo do melhor especialista | Autoridade com contraprova; opções em vez de meio-termo; `sintese.py`; o teste 1 decide onde a equipe entra |
| Conformismo e acordo precoce | Preparação por escrito; o objetivo é a melhor versão; fato novo e motivo contra na rodada 1; posições finais sozinho; poucas rodadas; mudança sem motivo marcada |
| Autoridade dada a um especialista errado | Só com `esp-*` ou fonte conferida; a contraprova sempre derruba; o crítico confere; o teste 8, com a `esp-*` adulterada |
| O mesmo modelo com nomes diferentes | Especialidades de `esp-*`, fontes diferentes por membro, o teste de identificabilidade da `especialistas` e a fase 10 |
| O líder puxar para a própria ideia | Abertura sem preferência; o que ele acrescenta vai marcado; o crítico revisa a síntese |
| Crítico de fachada, ou que não confere | Registra o que conferiu; "nada a apontar" vale; os scripts conferem contas e fontes de qualquer jeito |
| A conta certa do modelo errado | O `ata.py contas` refaz a conta, e o crítico confere o que ela modela |
| O contexto da condutora encher | Resumo de 300 palavras; falas em arquivo; a mesa delegada, se o teste pedir |
| Custo alto | Doses; parada antecipada; equipe só onde vence; registro por reunião |
| Vazamento entre sessões | Sessões incógnitas, num computador novo, auditoria e marcadores |
| Paralelas iguais, sem acesso à temperatura | Ordem sorteada em cada uma; o teste com a troca de um membro |
| As equipes de agentes do Claude Code mudarem | São experimentais e ficam para a fase 10; o protocolo não depende do transporte |

## 16. O que fica de fora

- **Debate livre,** sem pauta, sem ordem e sem formato.
- **Voto ou média como decisão.**
- **A equipe julgar ou dar veredito.**
- **Especialistas humanos na reunião.** Eles revisam as `esp-*`, num plano próprio, depois das skills.
- **Temperatura como fonte de diversidade.**
- **Perguntas a você no meio da reunião:** saem na síntese.
- **Equipes de agentes do Claude Code na v1,** e Custom Agents, pela regra "Universalidade primeiro".

## 17. Decidido e em aberto

**Decidido:**

- **Universal primeiro:** o protocolo, os formatos e os scripts valem em qualquer agente com chat; só o transporte muda com o ambiente.
- **Claude primeiro:** líder, especialistas e crítico são Claude, no modelo do papel "equipes"; outras famílias só na fase 10, onde vencerem às cegas.
- **O protocolo:** preparação por escrito que chega inteira a todos; abertura do líder sem opinião; rodadas na ordem sorteada, com fato novo e motivo contra na rodada 1; o crítico ao fim de cada rodada; posições finais, cada um sozinho; síntese com o destino de cada contribuição; uma revisão do crítico.
- **Autoridade por especialidade, com contraprova,** só para quem fala com `esp-*` ou fonte conferida.
- **Doses:** a leve, sem reunião; a padrão, com 3 especialistas e o crítico, em 2 rodadas; a completa, com 3 a 5, em até 3 rodadas, com paralelas e fusão quando a saída é central. Parada antecipada, sem rodada extra.
- **No Notion, a reunião orquestrada,** com a condutora na mesa e sessões filhas que retomam; o jeito sem estado fica de reserva e é a via das outras famílias.
- **Equipes de agentes do Claude Code só no teste da fase 10.**
- **A equipe nunca julga:** a verificação entrega um parecer técnico, e o veredito é do conselho.
- **Critério máximo:** na dúvida entre dois desenhos, vale o que mais contribui para uma ideia melhor, mais criativa e eficaz; custo e tempo vêm depois.
- **Mesa delegada, se o contexto da condutora pedir:** no Notion, uma sessão filha, se o teste da fase 3 mostrar que ela abre sessões; senão, um Custom Agent do Notion, pela regra "Universalidade primeiro"; outro harness só para as reuniões (Claude Code, Codex, agy ou outro); ou você abre as sessões à mão, com os briefs prontos. Até lá, a mesa é a condutora.

**Em aberto:**

- Nada, por enquanto.