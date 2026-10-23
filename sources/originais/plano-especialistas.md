# Plano detalhado — especialistas

<aside>
🎓

**O que é:** o plano detalhado da `especialistas`, a skill que recruta. Monta o mapa de especialidades do projeto, na sub-etapa 2.7 do [Fluxograma completo — Etapa 1 (método IDEAL em ciclo)](../Fluxograma%20completo%20%E2%80%94%20Etapa%201%20(m%C3%A9todo%20IDEAL%20em%20cic%20f1f71e3bd5e6487ebdfc94cd7e9fa161.md), com um mapa inicial ao fechar o tema 0; escreve a ficha de cada agente nos passos 3, 7 e 8 de cada sub-etapa; e cuida da biblioteca `esp-*`: o modelo de uma especialidade, como ela entra e é testada, e a primeira leva. É o quinto plano da ordem da seção 15 do [Plano geral das skills — Etapa 1 (CIR)](../Plano%20geral%20das%20skills%20%E2%80%94%20Etapa%201%20(CIR)%2072d0fdc1db19433e9101d1ac3b3015ef.md) e segue os formatos do [Plano detalhado — etapa-1-cir (condutora)](Plano%20detalhado%20%E2%80%94%20etapa-1-cir%20(condutora)%20fccda0c36a5d403582b433a6f2b0657f.md), do [Plano detalhado — conselho-especialistas](Plano%20detalhado%20%E2%80%94%20conselho-especialistas%20f31c25a61c914fd98fe1f1ad81c09ed4.md), do [Plano detalhado — pesquisa-cientifica](Plano%20detalhado%20%E2%80%94%20pesquisa-cientifica%20b0dde96c53b34b38aa26c8c474ce1071.md) e do [Plano detalhado — grill-embasado](Plano%20detalhado%20%E2%80%94%20grill-embasado%20ec54d7f985534c0a997926c075d97775.md).
**Universal primeiro:** recrutamento, fichas, biblioteca e scripts valem em qualquer agente com chat, e a especialidade chega a cada agente como texto, no brief (seção 9). **Claude primeiro:** quem recruta, quem escreve e revisa as `esp-*` e todo especialista são Claude, no modelo que você escolher para cada papel.

</aside>

## 1. Propósito no fluxograma

**Propósito:** ter, em cada sub-etapa, os especialistas que o problema pede, e que sejam especialistas de verdade: papel, especialidade curada e equipamento, com o que falta à vista.

| Responde por | Como se vê |
| --- | --- |
| Cobertura | Cada causa, contradição e parte do mapa tem uma especialidade na ficha de alguém; o `cobertura.py` mostra o que ficou sem |
| Especialidade de verdade | A especialidade vem de uma `esp-*` curada e testada, com versão; sem ela, a ficha diz "sem skill de especialidade" |
| Diferença real | Nenhuma formação repete especialidade e ótica; um juiz cego consegue dizer de que especialidade veio cada contribuição |
| Distância | Cada elaboração tem uma especialidade distante do problema, e só uma, com a função análoga escrita |
| Honestidade | Nenhuma ficha traz credencial, anos de experiência, instituição ou pessoa real |
| Lacunas à vista | Toda especialidade pedida e ausente da biblioteca vira lacuna, com origem e prioridade |
| Rastreio | Cada ficha registra a `esp-*`, a versão e o hash do texto que foi no brief, e a entrega do agente traz o mesmo selo |
- **Território, não roteiro.** A skill dá o objetivo, o padrão de qualidade e as regras; quais especialidades entram, em que ordem e com que escola de pensamento ficam a critério do modelo, conferidos por script.
- **Não faz:** gerar especialidade na hora; inventar credenciais; conduzir reuniões, que é da `equipe-especialistas`; escolher as óticas e os templates do conselho, que é da `conselho-especialistas` (aqui se escolhe a especialidade dos membros cuja ótica pede uma); julgar ideias; pesquisar o mérito do problema, que é da `pesquisa-cientifica`; decidir o que cada agente vê, que é regra da condutora e que a ficha só copia.
- **Pronto quando:** no mapa, o `especialistas.md` passa no `cobertura.py` e na validação do 2.7; no recrutamento, cada agente da formação tem ficha válida e bloco montado, e as lacunas estão na fila; na curadoria, a `esp-*` venceu o teste com e sem e tem a origem registrada, ou ficou registrado por que não entrou.

## 2. Skills de base e o que se aproveita

| Base | O que se aproveita | O que é nosso | Licença |
| --- | --- | --- | --- |
| [Virtual Lab](https://github.com/zou-group/virtual-lab) ([Swanson et al., Nature](https://doi.org/10.1038/s41586-025-09442-9)) | O investigador principal escolhe a equipe de cada projeto; cada agente tem título, especialidade, objetivo e papel; a seleção roda em várias discussões paralelas, e uma reunião funde os resultados; um crítico científico participa de toda reunião | A especialidade vem de uma `esp-*`, não só da descrição; o mapa sai do 2.7 e as fichas, de cada sub-etapa; a especialidade distante; o "sem skill" | MIT |
| [MDAgents](https://arxiv.org/abs/2404.15155) (Kim et al.) | A estrutura acompanha a complexidade: um agente sozinho para o simples, um grupo recrutado para o complexo; no grupo, a revisão de um moderador somada a conhecimento médico externo elevou a acurácia em 11,8% em média | O tamanho vem da dose; o conhecimento externo é a `esp-*` curada | Sem licença no repositório: só a ideia |
| [DyLAN](https://github.com/SALT-NLP/DyLAN) ([Liu et al.](https://arxiv.org/abs/2310.02170), COLM 2024) | Escolher a equipe entre candidatos, pela contribuição medida num ensaio, elevou a acurácia em até 25,0% em matérias do MMLU | A contribuição de cada `esp-*` fica no catálogo e orienta a revisão da biblioteca, não a escolha da equipe (seção 7) | MIT |
| [`skill-creator`](https://github.com/anthropics/skills/tree/main/skills/skill-creator) (Anthropic) | `SKILL.md` curto, referências lidas quando preciso e scripts; a tendência de o modelo não acionar skills; testes com e sem a skill, lançados juntos; a versão anterior como linha de base ao revisar; a comparação cega | Aplicado às `esp-*`, com gabarito verificável em vez de só preferência | Apache 2.0 |
| [`statistical-power`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/statistical-power) (K-Dense, v1.3, revista em 2026-10-01) | O desenho que o modelo de `esp-*` segue: quando usar, "a decisão que manda em tudo", receitas, ajustes esquecidos, modelo de relatório, armadilhas, scripts e 3 módulos de referência; testes ancorados em valores que se conferem fora da skill (d de Cohen de 0,5, com 80% de poder, pede 64 por grupo); a data de revisão no cabeçalho | Ponto de partida da `esp-estatistica`, com a `statistical-analysis` e a `experimental-design`; as escalas de plausibilidade da [`uncertainty-and-units`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/uncertainty-and-units) são o modelo das ordens de grandeza | MIT |
| [`scientific-problem-selection`](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research/skills/scientific-problem-selection) (Anthropic) | Conhecimento de quem é da área, a partir de Fischbach e Walsh ([Cell](https://doi.org/10.1016/j.cell.2024.03.012)): avaliação de risco, inversão do problema, planejamento para a adversidade e árvore de decisão, em 9 referências | Importar não é copiar: o roteiro de conversa sai, porque perguntar é do grill, e o conhecimento é condensado em até 3 módulos; candidata a módulo da `esp-decisao` ou da `esp-filosofia-ciencia`, e o teste decide onde rende | Apache 2.0 |
| Plano geral e fluxograma | As três partes do especialista; o híbrido; os 5 passos de entrada na biblioteca; "sem skill, roda marcado"; o 2.7; as doses; óticas não são especialidades | — | Nosso |

**Seis achados que mudam o desenho:**

1. **Conhecimento curado ajuda; o gerado na hora atrapalha.** No SkillsBench, com 87 tarefas e verificadores determinísticos, em 18 combinações de modelo e ferramenta, skills curadas elevaram a taxa de acerto de 33,9% para 50,5%. As que o próprio agente escreveu ficaram de 8,1 a 11,5 pontos abaixo de não usar skill nenhuma, inclusive no Claude Code com o Opus 4.7, e a auditoria achou conteúdo confiantemente errado ([SkillsBench](https://arxiv.org/abs/2602.12670)). Daí: a especialidade nunca é gerada na hora, e sem `esp-*` o agente roda marcado.
2. **Focada vence exaustiva, e o modelo menor com skill alcança o maior sem.** Skills compactas e padrão renderam +19,0 e +21,5 pontos; as detalhadas, +14,5; a documentação exaustiva, +0,7. Skills com até 3 módulos superaram pacotes maiores, e modelos menores com skills igualaram modelos maiores sem elas ([SkillsBench](https://arxiv.org/abs/2602.12670)). Daí: o modelo de `esp-*` tem limite de tamanho e de módulos, e o teste mede também um modelo menor com a `esp-*`, para a sua escolha no 0.3.
3. **Persona não é especialidade.** Além dos estudos da seção 4 do plano geral: várias personas finas, escolhidas para a tarefa, melhoraram o acerto e reduziram a alucinação em relação a uma persona só ou a um número fixo, mas só no GPT-4; nos modelos menores, a sinergia não apareceu ([Wang et al.](https://arxiv.org/abs/2307.05300)). Descrições de especialista sintetizadas melhoraram respostas julgadas pelo GPT-4, sem gabarito ([Xu et al.](https://arxiv.org/abs/2305.14688)). Daí: a ficha descreve o que o agente sabe e tem, não quem ele é, e o ganho de uma `esp-*` se mede contra gabarito, não só pela preferência de um juiz.
4. **Distância ajuda, na dose certa.** Em 166 desafios de ciência abertos a mais de 12.000 cientistas, a chance de dar a solução vencedora cresceu com a distância entre a área do solucionador e a área do problema ([Jeppesen e Lakhani](https://doi.org/10.1287/orsc.1090.0491)). Numa plataforma de design, conceitos que citavam fontes de inspiração tiveram mais sucesso, mas, quanto maior a distância média das fontes, menor a chance de sucesso ([Chan, Schunn e Dow](https://escholarship.org/uc/item/2bm91572)); e ideias distantes recebidas no meio de uma geração produtiva atrasaram e estreitaram a exploração, sem ganho de novidade ([Chan et al.](https://doi.org/10.1145/3059454.3059455)). Daí: uma especialidade distante por elaboração, não uma equipe de distantes; ela trabalha de preferência isolada, como gerador cego, do jeito que os solucionadores dos desafios abertos trabalharam; e o teste com e sem decide.
5. **O modelo segue o texto que recebe, mesmo errado.** Modelos aceitam evidência externa coerente e convincente mesmo quando ela contradiz o que sabem, e mostram viés de confirmação quando parte da evidência concorda com a memória ([Xie et al.](https://arxiv.org/abs/2305.13300)). Daí: um erro numa `esp-*` passa a todo especialista que a usa. Cada afirmação tem fonte e é conferida, a evidência conferida vence a `esp-*`, e a verificação confere os números centrais na pesquisa, não na `esp-*`.
6. **O mesmo modelo se repete.** Um modelo gera respostas parecidas entre si, e modelos diferentes geram respostas parecidas entre eles ([Artificial Hivemind](https://arxiv.org/abs/2510.22954)). Daí o risco principal, especialistas que são o mesmo modelo com outro nome: a diferença tem de vir do conteúdo (a `esp-*`, as fontes e os operadores), e o teste de identificabilidade mede se veio.

## 3. Acionamento

```yaml
---
name: especialistas
description: >-
  Recruta especialistas de verdade para um problema: decide que
  especialidades ele pede, inclui uma distante e o crítico, e escreve a
  ficha de cada agente (papel, especialidade, skill de especialidade ou
  "sem skill", ferramentas, modelo, o que vê e o que não vê), no tamanho da
  dose. Monta o mapa de especialidades do projeto, as fichas dos passos 3,
  7 e 8 de cada sub-etapa e cuida da biblioteca esp-*: registra as lacunas
  e guia a curadoria de uma especialidade nova, com teste com e sem. Use
  quando a condutora da Etapa 1 precisar de especialistas, equipe,
  geradores ou membros de conselho, ou quando o usuário pedir para montar
  um time de especialistas ou criar uma skill de especialidade. Não use
  para conduzir reuniões, julgar ideias, escolher as óticas do conselho ou
  responder como especialista.
license: (a definir)
compatibility: Qualquer agente com chat; Python 3 para os scripts; a curadoria usa a pesquisa-cientifica
metadata:
  versao: "0.1"
---
```

- **Só os campos do padrão aberto,** como nas outras skills.
- **Chamada pelo nome é o caminho principal:** "Use a skill `especialistas`, modo recrutar, passo 7 da 4.3, dose completa, com o `especialistas.md` do projeto." Fora da Etapa 1, a skill roda avulsa (seção 5.4).
- **As `esp-*` não dependem de acionamento.** No ciclo, elas chegam no brief (seção 9). A descrição de cada uma serve ao uso avulso e ao banco de Skills do Notion, na fase 9.

| Deve acionar | Não deve acionar (quase acertos) |
| --- | --- |
| "Monta os especialistas e os conselhos do projeto (2.7)." | "Conduz a reunião da equipe da 4.3." (é da `equipe-especialistas`) |
| "Que especialistas a equipe da 4.3 precisa, na dose completa?" | "Qual das três hipóteses é a melhor?" (julgar é do conselho) |
| "Monta os geradores cegos do passo 7, cada um de uma disciplina." | "Quantos participantes preciso para detectar esse efeito?" (é uma pergunta da área: vai à `pesquisa-cientifica` ou, avulsa, à `esp-estatistica`) |
| "Temos skill de hidráulica? Preciso de alguém dessa área na verificação." | "Que óticas entram no conselho completo?" (é da `conselho-especialistas`) |
| "Cria uma skill de especialidade em epidemiologia." (modo curar) | "Responde como se fosse o Kahneman." (imitar pessoa real fica de fora; escola de pensamento, só dentro de uma ficha) |
| "Monta um time de especialistas para avaliar o meu plano de negócios." (avulso) | "Pesquisa o que a epidemiologia diz sobre vigilância." (é da `pesquisa-cientifica`) |

A lista completa, com 10 de cada lado, entra nos testes (seção 14).

## 4. Contrato de entrada e saída

| Modo | Recebe | Entrega |
| --- | --- | --- |
| Mapa | No brief: a ficha do projeto e o material separado, no mapa inicial; no 2.7, o job map, as causas, as contradições, as partes e o espaço K; as suas respostas ao grill sobre especialidades e escolas de pensamento a ouvir ou evitar, e a sua versão, se houver; as fichas da pesquisa sobre que disciplinas estudam cada causa e contradição; o catálogo da biblioteca; o mapa de modelos | O `especialistas.md`: as especialidades e o que cada uma cobre, a distante de cada tema, as equipes-base, a composição de cada template do conselho, as suas preferências e as lacunas |
| Recrutar | O cartão da sub-etapa (o que decidir, o "refuta se" e a dose); a formação pedida; o `especialistas.md`; o catálogo; o mapa de modelos; os operadores do tema, quando há geradores | As fichas da formação, em `fichas/`; o bloco de especialidade de cada agente, para o `brief.py`; as lacunas novas |
| Curar | Uma lacuna da fila ou um pedido seu; as fontes da `pesquisa-cientifica`; a sua revisão e, se houver, a de um especialista humano | Uma `esp-*` nova ou revista, com testes, versão e origem; ou o registro de por que não entrou |
| Avulso | Um problema em texto livre | Um mapa curto e as fichas, sem dossiê; as lacunas vão para a mesma fila |

**Contratos com as outras skills:**

| Skill | Relação |
| --- | --- |
| `etapa-1-cir` | Chama a skill no mapa inicial, no 2.7 e nos passos 3, 7 e 8; põe no brief o que ela precisa ver; grava o `especialistas.md` e as `fichas/`; o `brief.py` põe o bloco de especialidade no topo do brief de cada agente, sem reescrever |
| `conselho-especialistas` | Define as óticas e os templates; recebe a ficha e o bloco de cada membro cuja ótica pede especialidade |
| `equipe-especialistas` | Recebe as fichas e os blocos e conduz a reunião; a ata marca de que especialidade veio cada contribuição, para o placar do catálogo |
| `pesquisa-cientifica` | No 2.7, diz que disciplinas estudam cada causa e contradição; na curadoria, levanta as fontes de referência da área (modo desenvolver), confere cada afirmação (modo conferir) e procura o que derruba as centrais (modo refutar) |
| `grill-embasado` | No 2.7, pergunta que especialidades e escolas de pensamento você quer ouvir ou evitar |
| `cir-*` | Dão, no cartão, a formação de cada passo e os operadores dos geradores |
- **O que cada agente vê e não vê** vem da regra do papel, na condutora. A ficha copia, e o `fichas.py` recusa mudança.

## 5. Modos e doses

### 5.1 Modos

| Modo | Quando | O que faz |
| --- | --- | --- |
| Mapa inicial | Ao fechar o tema 0, com a ficha do projeto e o material separado | Um recrutador lista as especialidades que os temas 1 e 2 vão pedir, como as disciplinas dos geradores do 1.4, e marca as lacunas. Vale até o 2.7. Você o vê no estado inicial do 0.3 e pode vetar ou pedir especialidades |
| Mapa (2.7) | Na sub-etapa 2.7 | Dois recrutadores independentes, sem ver um ao outro, e uma fusão, como a seleção em paralelo do Virtual Lab; um gerador cego propõe disciplinas distantes. O mapa passa no `cobertura.py` e no conselho rápido do 2.7, e você decide |
| Recrutar | Passos 3, 7 e 8 de cada sub-etapa | Escolhe do mapa os especialistas da formação, no tamanho da dose, escreve as fichas e manda montar os blocos. Não pede a sua aprovação a cada vez, porque o mapa já foi aprovado e as fichas ficam no registro; pede só para trazer uma especialidade de fora do mapa, com um sim ou não |
| Curar | Fora do projeto, numa sessão própria, quando você quiser | Pega a lacuna de maior prioridade e segue os passos de entrada na biblioteca (seção 6.3) |
| Avulso | Fora da Etapa 1 | Um mapa curto e as fichas para um problema qualquer (seção 5.4) |
- **Atualizar o mapa:** quando aparece uma causa, uma contradição ou uma parte nova depois do 2.7, um recrutador acrescenta o que falta, o `cobertura.py` confere, e a mudança vai a você com um sim ou não.

### 5.2 Doses

O tamanho segue a tabela de doses do fluxograma; aqui está quem entra em cada formação.

| Formação | Leve | Padrão | Completa |
| --- | --- | --- | --- |
| Mapa | 1 recrutador, só no mapa inicial | 2 recrutadores e fusão, e 1 gerador cego de disciplinas distantes: é o 2.7 | 3 recrutadores e fusão, e 2 geradores |
| Triagem, passo 3 | 1 membro e o crítico | 2 membros e o crítico | 2 ou 3 membros e o crítico |
| Elaboração, passo 7 | 1 especialista, da especialidade mais central, propõe várias variações | 3 especialistas e o crítico; 1 gerador cego, da especialidade distante | De 3 a 5 especialistas e o crítico, com a distante a partir do 4º lugar; 2 ou 3 geradores, cada um com especialidade e operadores diferentes, um deles distante |
| Verificação, passo 8 | — | — | 2 ou 3 especialistas que não elaboraram, das especialidades que o "refuta se" combina, e o crítico |
| Conselho, passos 3 e 8 | As óticas do cartão, com a `esp-*` onde a ótica pede | Idem | O template completo, com a `esp-*` onde a ótica pede |
- **Onde a ótica pede especialidade:** o especialista do domínio e os refutadores de método e de limites teóricos recebem a `esp-*` da ciência em jogo; a natureza humana, a de comportamento; o adversário, a de incentivos ou de segurança, quando houver. A composição de cada template fica no `especialistas.md`.
- **Quem entra primeiro:** as especialidades que cobrem o que a sub-etapa decide. O `cobertura.py --sugerir` propõe, por seleção gulosa, o conjunto que cobre mais itens do cartão, com peso maior para as causas centrais e as contradições de princípio; o modelo pode trocar, com o motivo na ficha.
- **Reserva:** quem não coube fica de reserva no mapa e entra na rodada seguinte, se a hipótese for refutada ou empatar.
- **Reuniões paralelas** da dose completa têm a mesma composição, como no Virtual Lab; o teste compara com composições que trocam um membro (seção 14).
- **Escola de pensamento:** a mesma especialidade só se repete numa formação com escolas diferentes, escritas na ficha, quando a divergência entre elas importa para a sub-etapa.

### 5.3 A especialidade distante

- **O que é:** uma área que resolve um problema com a mesma estrutura em outro domínio, e não uma área qualquer. A ficha escreve a função análoga: "passar um sistema em funcionamento de uma equipe a outra, em minutos, sem perder peça nem informação" liga a passagem do paciente da cirurgia para a UTI ao pit stop da Fórmula 1 e à aviação. Num hospital pediátrico, o protocolo desenhado com uma equipe de Fórmula 1 e com comandantes instrutores de aviação baixou, em média, os erros técnicos de 5,4 para 3,2 e as omissões de informação de 2,1 para 1,1 por passagem, num estudo antes e depois com 50 passagens observadas ([Catchpole et al.](https://doi.org/10.1111/j.1460-9592.2006.02239.x)).
- **De onde vem:** do gerador cego de disciplinas distantes do 2.7, que não vê a sua versão nem os mapas dos recrutadores; a fusão escolhe uma por tema.
- **Onde entra:** na dose padrão, como o gerador cego do passo 7; na completa, também com um lugar na equipe, a partir do 4º. Nunca mais de uma por formação (achado 4).
- **O que entrega:** o problema análogo da sua área, como ele é resolvido lá e o que se transfere, e não uma opinião geral.
- **Para o plano da `equipe-especialistas`:** ideias distantes atrapalharam quando chegaram no meio de uma geração produtiva, e a teoria que o estudo testou recomenda trazê-las no impasse ([Chan et al.](https://doi.org/10.1145/3059454.3059455)). Fica a sugestão de testar a fala da distante quando a reunião empaca.

### 5.4 Modo avulso

Fora da Etapa 1, sem dossiê, a skill faz uma rodada curta de até 3 perguntas (o que se quer decidir, o que entregar e que especialidades ouvir ou evitar), monta um mapa curto e as fichas e grava tudo em `especialistas/<data>-<assunto>/`, numa pasta com Git. As regras são as mesmas, e as lacunas vão para a fila da biblioteca.

## 6. Passos

### 6.1 Mapa (inicial e 2.7)

No 2.7, estes passos são o passo 7 do ciclo, a elaboração; a validação é o passo 8.

1. **Lê o problema no brief:** no mapa inicial, a ficha do projeto e o material separado; no 2.7, o mapa do tema 2, as suas respostas ao grill e a sua versão, se houver.
2. **Liga cada item a disciplinas.** Para cada causa, contradição e parte, as disciplinas que a estudam, a partir das fichas da pesquisa, e nunca a partir do catálogo (regra 1).
3. **Agrupa as disciplinas em especialidades** e só então consulta o catálogo: com `esp-*`, a versão em uso; sem, "sem skill" e uma lacuna.
4. **Escolas de pensamento:** onde a área tem escolas que divergem sobre o problema, registra quais ouvir, com as suas preferências.
5. **Monta as equipes-base de cada tema e a composição de cada template do conselho:** que especialidade e que modelo vão em cada ótica que pede especialidade.
6. **Confere** com o `cobertura.py`: cobertura de cada item, duplicatas, distante e crítico.
7. **Na dose padrão do 2.7,** dois recrutadores fazem os passos 1 a 6 sozinhos, sem ver um ao outro, e o gerador cego propõe disciplinas distantes. A condutora funde os mapas: o `cobertura.py --comparar` mostra o que só um trouxe; a diferença fica se cobre algo que o outro não cobre, e o resto vai a você.
8. **Entrega** o `especialistas.md` à validação do 2.7: conselho rápido (explorador e construtivo), que refuta se uma causa ou contradição fica sem especialidade, ou se dois membros repetem a mesma ótica. Você decide no passo 9.

### 6.2 Recrutar (passos 3, 7 e 8)

1. **Lê o cartão:** o que a sub-etapa decide, o "refuta se", a dose e a formação pedida.
2. **Escolhe do mapa** quem cobre o que a sub-etapa decide, no tamanho da dose, com a sugestão do `cobertura.py --sugerir`. Nos geradores: especialidades diferentes, uma delas distante, e operadores sorteados sem repetição, com a semente registrada.
3. **Escreve as fichas** (`fichas.py novo`): papel, especialidade, `esp-*` e módulos, escola, o que cobre e por quê, ferramentas e o modelo do papel. O que vê e não vê vem do `papeis.md`.
4. **Valida** (`fichas.py validar`): campos, credenciais, nomes de pessoas, `esp-*` no catálogo e não bloqueada, duplicatas, distante e crítico.
5. **Monta os blocos** (`brief_esp.py montar`), com versão, hash, módulos e errata, e os entrega ao `brief.py` da condutora.
6. **Registra as lacunas** (`lacunas.py novo`) de toda ficha "sem skill".
7. **Na volta,** a condutora confere o selo de cada entrega (`brief_esp.py selo`); com selo ausente ou errado, a execução é refeita.

### 6.3 Curar (fora do projeto)

1. **Escolhe** a lacuna de maior prioridade (`lacunas.py proxima`) ou a que você pedir, e escreve o escopo: o que a especialidade cobre, o que não cobre e quando chamar outra.
2. **Procura o que já existe:** skills feitas por gente da área, como as da K-Dense e da Anthropic, livros-texto, diretrizes e cursos, com a `pesquisa-cientifica` no modo desenvolver. Confere a licença e o conteúdo. Importar não é copiar: o roteiro de conversa sai, e o conhecimento é condensado no modelo da seção 8.
3. **Escreve, se não houver,** a partir das fontes de referência, numa sessão que não lê os problemas de teste nem os casos de teste do sistema, como o Motor de Insights.
4. **Confere** cada afirmação e cada ordem de grandeza no modo conferir, e as 3 a 5 afirmações centrais no modo refutar, à procura de réplicas que falharam e de revisões.
5. **Revisão sua** (escopo, clareza e serventia para os projetos) **e, quando possível, de um especialista humano** (correção). O que ele acrescentar sem fonte publicada entra como "saber de prática", marcado.
6. **Problemas de teste,** em paralelo, numa sessão que vê só o escopo e as fontes de referência: de 5 a 10 com gabarito e a fonte do gabarito, metade ou mais em variantes novas, e 1 ou 2 fora do escopo. Ficam fechados para quem escreve a `esp-*`.
7. **Teste com e sem** (`teste_esp.py`, seção 14). Só entra com ganho.
8. **Versão fixa:** tag no Git, hash, `ORIGEM.md` e catálogo. Na fase 9, a `esp-*` também vai para o banco de Skills do Notion, para o uso avulso.
9. **Validade:** a `esp-*` volta ao teste quando muda o modelo de um papel que a usa, quando acumula errata ou quando passa a data de validade, de 12 meses para começar.

### 6.4 Rever uma `esp-*`

A linha de base é a versão anterior, como no `skill-creator`, com os mesmos problemas e mais os que a errata trouxe. A versão nova só substitui a anterior se vencer; enquanto isso, a anterior segue em uso, com a errata.

### 6.5 A primeira leva

| Ordem | Especialidade | Por que entra | Pontos de partida, a conferir na curadoria | Problemas com gabarito |
| --- | --- | --- | --- | --- |
| 1 | `esp-estatistica`: estatística e inferência causal | Candidata do Motor; vai no refutador de método do template Evidência | `statistical-power`, `statistical-analysis` e `experimental-design` (K-Dense, MIT); [Hernán e Robins, *Causal Inference: What If*](https://miguelhernan.org/whatifbook) | Tamanho de amostra e poder; conjunto de ajuste num grafo causal; paradoxo de Simpson; regressão à média; comparações múltiplas |
| 2 | `esp-decisao`: ciência da decisão | Candidata do Motor; decidir bem está no centro do caso | Valor da informação ([Howard](https://doi.org/10.1109/TSSC.1966.300074)); visão de fora e classe de referência ([Kahneman e Lovallo](https://doi.org/10.1287/mnsc.39.1.17)); `scientific-problem-selection` (Anthropic, Apache 2.0) | Bayes com taxa de base; valor da informação; valor esperado; escore de Brier |
| 3 | `esp-comportamento`: comportamento humano | Transversal: a ótica natureza humana entra em vários templates e no conselho de triagem | Roda da mudança de comportamento ([Michie, van Stralen e West](https://doi.org/10.1186/1748-5908-6-42)); formação de hábitos ([Lally et al.](https://doi.org/10.1002/ejsp.674)); replicação em psicologia ([Open Science Collaboration](https://doi.org/10.1126/science.aac4716)); nudges depois da correção do viés de publicação ([Maier et al.](https://doi.org/10.1073/pnas.2200300119)) | Que efeitos replicaram e quais não; ordens de grandeza de efeitos; classificar intervenções nas funções da roda |
| 4 | `esp-filosofia-ciencia`: filosofia da ciência | Candidata do Motor; refutação e critérios de prova em todos os temas | Teste severo ([Mayo](https://doi.org/10.1017/9781107286184)); `scientific-critical-thinking` (K-Dense, MIT); `rigor-reviewer` ([Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs), MIT) | Variantes da tarefa de seleção de Wason; falseável ou não; hipótese auxiliar ad hoc; que resultado refutaria |
| 5 | `esp-computacao-ml`: computação e aprendizado de máquina | Candidata do Motor; limites do que se computa e do que se aprende | Vazamento de dados ([Kapoor e Narayanan](https://doi.org/10.1016/j.patter.2023.100804)); "não há almoço grátis" ([Wolpert e Macready](https://doi.org/10.1109/4235.585893)); conflitos entre critérios de justiça ([Kleinberg, Mullainathan e Raghavan](https://arxiv.org/abs/1609.05807)) | Achar o vazamento num processo descrito; precisão e valor preditivo com taxa de base; combinações de critérios impossíveis |
| 6 | `esp-incentivos`: economia e incentivos | Transversal: o mapa de partes (1.4) e a ótica adversário pedem | Seleção adversa ([Akerlof](https://doi.org/10.2307/1879431)); risco moral ([Holmström](https://doi.org/10.2307/3003320)) | Equilíbrio de jogos simples; leilão de segundo preço; prever como uma métrica será burlada (por rubrica) |
- **Por que estas:** as quatro candidatas do plano geral para o Motor, e duas que o próprio fluxograma pede em quase todo projeto: a ótica natureza humana, em vários templates e na triagem, e os incentivos do mapa de partes e da ótica adversário.
- **Ordem:** as três primeiras antes do fim da fase 3, para o ciclo de teste rodar com uma equipe de três especialidades de verdade; as outras três antes da fase 5, que tem o teste do impossível. A ordem segue a força da base publicada e a facilidade de montar gabarito.
- **O 2.7 confirma.** No teste ponta a ponta, o 2.7 do Motor recruta sem saber da leva; o que ele pedir fora dela roda sem skill e entra na fila (risco 8).
- **Na fila desde já:** segurança e adversários, para a ótica adversário e o red team do 5.4, e as especialidades dos outros casos de teste, como hidráulica de redes. Entram pela prioridade.
- **Pontos de partida, não conteúdo pronto:** cada um passa pelos passos de 6.3, com licença, conferência e teste. Nenhuma `esp-*` traz conteúdo dos casos de teste do sistema (regra 12).

## 7. Regras que valem o tempo todo

| Regra | Por quê | Como se garante |
| --- | --- | --- |
| 1. **Recruta pelo problema, não pelo catálogo.** | Senão a biblioteca decide o que se ouve, e a causa sem `esp-*` fica sem ninguém | O mapa parte das disciplinas que a pesquisa liga a cada item; o `cobertura.py` mostra o item sem especialidade, tenha ela skill ou não |
| 2. **Nunca gera especialidade na hora.** | Skills autogeradas ficaram abaixo de não usar skill (achado 1) | O `fichas.py` só aceita `esp-*` do catálogo, e o bloco só sai do `brief_esp.py`. Resumir ou "completar" uma `esp-*` também é gerar |
| 3. **Sem skill, roda marcado.** | A falta à vista vale mais que conhecimento inventado | Ficha "sem skill de especialidade"; bloco "sem skill", que pede fonte para as afirmações centrais; lacuna na fila |
| 4. **Sem credencial e sem pessoa real.** | Persona não melhora o acerto; credencial é invenção; imitar alguém atribui a ele opiniões que ele não deu | O `fichas.py` recusa títulos, anos de experiência, instituições, superlativos e nomes próprios nos campos de papel e especialidade; escola de pensamento entra com as obras como fonte |
| 5. **A diferença vem do conteúdo.** | O mesmo modelo se repete (achado 6) | Cada especialista tem `esp-*`, fontes e, nos geradores, operadores próprios; nenhuma formação repete especialidade e ótica, salvo escolas diferentes; o teste de identificabilidade mede |
| 6. **Uma distante por elaboração.** | A distância ajuda, e o excesso atrapalha (achado 4) | O `cobertura.py` exige uma, e só uma, nas doses padrão e completa do passo 7, com a função análoga escrita |
| 7. **Crítico em toda equipe.** | É a peça que o Virtual Lab mantém fixa, e o plano geral também | O `cobertura.py` |
| 8. **O bloco vai inteiro, no topo e sem reescrita.** | Reescrever é gerar na hora; com textos longos, o material no topo e a tarefa no fim rendem mais (seção 8) | Hash no bloco e na ficha; selo na entrega; conferência do texto que chegou (seção 9) |
| 9. **Fonte conferida vale mais que a `esp-*`, e a `esp-*`, mais que a memória.** | O modelo segue o texto que recebe, mesmo errado (achado 5) | A instrução do bloco; a errata; a `esp-*` contradita fica "em revisão" |
| 10. **O que vê e não vê vem do papel.** | O isolamento é regra da condutora, não escolha do recrutamento | O `fichas.py` copia do `papeis.md` e recusa mudança |
| 11. **Curadoria fora do projeto.** | Curadoria apressada vira geração na hora | O modo curar só roda numa sessão própria; no projeto, só se registra a lacuna |
| 12. **Sala limpa.** | Uma `esp-*` com conteúdo dos casos de teste ensinaria a resposta e invalidaria o teste | Quem escreve não lê os casos do sistema; os problemas de teste nunca saem deles; o `catalogo.py` procura os marcadores dos casos |
| 13. **Só entra com ganho.** | O teste com e sem é o "treino" possível; empate é custo sem ganho | O `teste_esp.py` e a regra de entrada (seção 14) |
| 14. **O placar orienta a revisão, não a escolha.** | Escolher pelo histórico fecharia a biblioteca nas mesmas especialidades | O recrutamento não lê o placar; o catálogo o mostra na curadoria |

**Pensamentos e realidade:**

| Pensamento | Realidade |
| --- | --- |
| "Não tem `esp-*` de hidráulica; escrevo uma rapidinha com o que eu sei." | É a skill autogerada, que piora. Roda sem skill, marcado, e vai para a fila. |
| "Chamo de engenheira com 30 anos de experiência; convence mais." | Credencial inventada não melhora e engana. A ficha diz o que o agente tem: a `esp-*` ou "sem skill". |
| "As especialidades que têm skill dão conta." | Recruta pelo problema. A causa sem especialidade aparece, com ou sem skill. |
| "Duas distantes, para ousar mais." | Uma por elaboração. Em excesso, a distância atrapalha. |
| "Resumo a `esp-*` para caber no brief." | Resumir é reescrever na hora. Vai inteira, ou só com os módulos da ficha. |
| "A pesquisa contradiz a `esp-*`, mas a `esp-*` foi revisada." | Vale a evidência conferida. Errata no bloco, e a `esp-*` vai para revisão. |
| "Dois geradores da mesma área, com temperaturas diferentes." | O mesmo modelo se repete. Especialidades e operadores diferentes. |
| "Você quer o Taleb na equipe; eu faço o Taleb." | A escola de pensamento entra, com as obras como fonte. Imitar a pessoa, não. |
| "Deu empate no teste; entra assim mesmo, mal não faz." | Só entra com ganho. O empate esconde o erro que ninguém mediu. |
| "Testo a `esp-*` com os problemas do Motor, que eu conheço bem." | Os testes nunca saem dos casos do sistema. |

## 8. Formatos e modelos de documento

Os formatos seguem os da condutora: o envelope do brief, os prefixos e os registros. Os exemplos usam um projeto de fora dos casos de teste do sistema, a passagem do paciente da cirurgia para a UTI, para não ensinar a resposta ao recrutamento.

### 8.1 Ficha

Uma por agente, em `fichas/<sub-etapa>-p<passo>.md`, com o prefixo `E-<sub-etapa>-p<passo>-<nº>`; cada rodada acrescenta as suas.

```yaml
ficha: E-4.3-p7-03
subetapa: 4.3 · passo 7 · dose completa · rodada 1
papel: especialista da equipe de elaboração
nome: estatistica-1
especialidade: estatística e inferência causal
esp: esp-estatistica@1.2 · 3f9a1c
modulos: [poder-e-amostra, eventos-raros]
escola: —
distante: não
cobre: [causa 2.2-4 · erros raros e mal registrados na passagem]
por_que: é a única da formação que diz, com poucos eventos, se uma mudança funcionou; sem ela, as variações do núcleo ficam sem teste
fontes: [F-031, F-044]
ferramentas: [busca e leitura na web, Python]
modelo: Claude Opus 5.5 · papel equipes, no mapa de modelos
ve: a pauta, a versão base sem autoria, as fichas de fonte e a ata
nao_ve: a autoria e o modelo dos outros
```

**A distante da mesma formação, sem skill** (só os campos que mudam):

```yaml
ficha: E-4.3-p7-04
nome: troca-rapida-1
especialidade: operações de troca rápida (pit stop) e aviação
esp: sem skill de especialidade · lacuna LAC-014
modulos: []
distante: sim · função análoga: passar um sistema em funcionamento de uma equipe a outra, em minutos, sem perder peça nem informação
cobre: [causa 2.2-1 · atenção dividida entre equipamento e informação, contradição 2.3-1 · rapidez × completude]
por_que: a área resolve todo dia a mesma troca sob pressa; entra no 4º lugar da dose completa
fontes: [F-052]
```

| Campo | O que guarda |
| --- | --- |
| `esp` | O nome, a versão e o começo do hash do texto que vai no bloco; ou "sem skill de especialidade", com a lacuna |
| `modulos` | Só os que a sub-etapa pede, até 3; o `SKILL.md` vai sempre inteiro |
| `cobre` e `por_que` | Os itens do mapa que o agente cobre, e por que ele e não outro. É o que o `cobertura.py` lê |
| `nome` | Funcional, da especialidade e de um número, para a condutora retomar o membro; nunca nome de pessoa (regra 4) |
| `fontes` | As fichas de fonte do dossiê que vão no brief, escolhidas pela especialidade. Para quem roda sem skill, são a base das afirmações centrais |
| `ve` e `nao_ve` | Copiados do `papeis.md` (regra 10) |
| `operadores` e `semente` | Só nos geradores: os operadores sorteados e a semente do sorteio |
| `template` e `otica` | Só no conselho |

### 8.2 `especialistas.md`

O mapa do projeto, no dossiê. O mapa inicial tem o mesmo formato, mais curto, marcado "inicial, vale até o 2.7".

```markdown
# Especialistas e conselhos · passagem-uti
mapa: 2.7 · dose padrão · recrutadores R1 e R2 e gerador G1 · aprovado no passo 9 (D-021)

## Especialidades
- fatores humanos e ergonomia · sem skill · LAC-012
  cobre: causas 2.2-1 e 2.2-2 · por quê: a passagem divide a atenção entre equipamento e informação
- medicina e enfermagem intensiva · sem skill · LAC-013
  cobre: causa 2.2-3 e partes 1.4-2 e 1.4-3 · por quê: o que a UTI precisa receber, e em que ordem
- estatística e inferência causal · esp-estatistica@1.2 · 3f9a1c
  cobre: causa 2.2-4 · por quê: medir erros raros com poucas passagens
- comportamento humano · esp-comportamento@1.0 · 8d2e47
  cobre: contradição 2.3-1 e parte 1.4-4 · por quê: protocolos que a equipe abandona sob pressa
- economia e incentivos · esp-incentivos@1.0 · c71b05
  cobre: parte 1.4-5 · por quê: quem ganha e quem perde tempo com o protocolo

## Distante por tema
- tema 4: operações de troca rápida (pit stop) e aviação · sem skill · LAC-014
  função análoga: passar um sistema em funcionamento de uma equipe a outra, em minutos, sem perder peça nem informação
- temas 3 e 5: …

## Equipes-base
- tema 4: fatores humanos, intensiva, estatística, a distante e o crítico · reserva: comportamento
- temas 3 e 5: …

## Conselhos (template → ótica → especialidade)
- Evidência: refutador de método → esp-estatistica · especialista do domínio → intensiva, sem skill
- conselho de triagem, Idealidade e Prova: natureza humana → esp-comportamento
- Elementos, Arquitetura e Prova: adversário → esp-incentivos

## Suas preferências
- ouvir: fatores humanos (entrou) · evitar: — · escolas: —

## Lacunas
- LAC-012, LAC-013 e LAC-014, na fila da biblioteca

## Como foi montado
- R1 e R2 sem ver um ao outro; G1 propôs 4 distantes por tema; na fusão, só R2 trouxe intensiva, que ficou por cobrir a causa 2.2-3
- cobertura.py: todos os itens cobertos, nenhuma duplicata, uma distante por tema e crítico em todas
- conselho rápido: nenhuma refutação
```

### 8.3 O modelo de uma `esp-*`

```jsx
esp-estatistica/
  SKILL.md                até umas 300 linhas, no esqueleto abaixo
  references/             até 3 módulos, que a ficha escolhe
    poder-e-amostra.md
    eventos-raros.md
    grafos-causais.md
  scripts/                as contas que a área faz sempre do mesmo jeito, quando houver
    poder.py
  ORIGEM.md               de onde veio cada parte, conferência, revisão, teste e licenças
```

Os problemas de teste ficam fora da pasta, num repositório fechado (seção 11).
**Esqueleto do arquivo principal** (`SKILL.md`):

```markdown
---
name: esp-estatistica
description: >-
  Estatística e inferência causal: tamanho de amostra e poder, comparação de
  grupos, eventos raros e grafos causais. Use quando uma tarefa pedir medir
  um efeito, desenhar uma comparação ou julgar uma afirmação causal. Não use
  para desenho de questionários nem para séries temporais.
license: (a definir; as licenças das fontes ficam no ORIGEM.md)
metadata:
  versao: "1.2"
  revista_em: "2026-12-01"
---
# Estatística e inferência causal
## Escopo e limites
O que cobre, o que não cobre e quando chamar outra especialidade.
## O que a área pergunta primeiro
As perguntas que alguém da área faz antes de qualquer conta.
## A decisão que manda em tudo
A escolha que mais muda o resultado, e como fazê-la.
## Receitas
Passo a passo das tarefas frequentes, com o script, quando houver.
## Critérios
Como a área julga se algo está bom, com os limiares e as fontes.
## Erros típicos
O erro, o sinal que o denuncia e a correção.
## Ordens de grandeza
Valores de referência e faixas plausíveis, cada um com fonte e data.
## Escolas de pensamento
Onde a área diverge, o que cada escola diz e as obras de cada uma.
## Fontes de referência
Livros-texto, diretrizes e revisões, com DOI ou link.
## Scripts
O que cada script faz e quando rodar.
## Saber de prática (opcional)
O que um especialista humano acrescentou sem fonte publicada, marcado.
```

- **Limites para começar:** `SKILL.md` até umas 300 linhas, até 3 módulos e o bloco inteiro, com os módulos da ficha, até umas 8.000 palavras. Vêm do achado 2, e o teste os ajusta.
- **Cada afirmação tem fonte,** e cada ordem de grandeza, fonte e data. O que não tem fonte publicada só entra no "saber de prática", marcado.
- **Conhecimento, não persona:** o texto diz o que a área sabe e faz, sem "você é"; o papel vem da ficha (achado 3).
- **Nada dos casos de teste do sistema** (regra 12).
- **Só os campos do padrão aberto** no cabeçalho, para a `esp-*` servir também avulsa e no banco de Skills.

### 8.4 `ORIGEM.md`

```yaml
esp: esp-estatistica
versao: "1.2"
tag: esp-estatistica-v1.2
hash: 3f9a1c…            # do SKILL.md e dos módulos, nesta ordem
situacao: em uso         # em teste, em uso, em revisão, bloqueada ou aposentada
entrou_em: 2026-12-01
valida_ate: 2027-12-01
escopo: estatística e inferência causal; não cobre questionários nem séries temporais
pontos_de_partida:
  - statistical-power (K-Dense, MIT, v1.3): receitas de poder e modelo de relatório, condensados
fontes:
  - Hernán e Robins, Causal Inference: What If
conferencia: 142 afirmações no modo conferir, 3 corrigidas; 5 centrais no modo refutar, nenhuma derrubada
revisao: você, em 2026-11-28 (escopo e serventia); especialista humano: —
teste:
  problemas: 8 com gabarito e 2 fora do escopo
  execucoes: 3 por condição
  resultados:
    - modelo: Claude Opus 5.5
      sem: 61
      com: 78
      fora_do_escopo: sem piora
    - modelo: o menor do teste
      com: 74
licencas: MIT da K-Dense, com o aviso de copyright
errata: []
```

### 8.5 Lacuna

Na fila da biblioteca, em `lacunas.md`:

```markdown
## LAC-014 · operações de troca rápida (pit stop) e aviação
- pedida por: passagem-uti, no 2.7 (distante do tema 4) e no passo 7 da 4.3
- para quê: função análoga, passar um sistema em funcionamento de uma equipe a outra, em minutos, sem perder peça nem informação
- rodou como: sem skill, marcado (E-4.3-p7-04)
- causa central ou contradição de princípio: não
- gabarito: parcial; o resto, por rubrica
- situação: na fila
- registrada em: 2026-11-12
```

- **Situação:** na fila, em curadoria, entrou (com a `esp-*` e a versão) ou não entrou (com o motivo, como empate no teste).
- **Prioridade** (`lacunas.py proxima`): primeiro as que cobrem causa central ou contradição de princípio; depois, as pedidas por mais projetos; depois, por mais sub-etapas; no empate, a que tem gabarito.

### 8.6 Bloco de especialidade e ordem do brief

O `brief_esp.py` monta o bloco a partir da tag do Git, sem passar pelo modelo:

```markdown
<especialidade nome="esp-estatistica" versao="1.2" hash="3f9a1c" modulos="poder-e-amostra, eventos-raros">
<instrucao>
Este é o conhecimento curado da especialidade da sua ficha, para esta tarefa. Ele vale mais que a sua memória: onde os dois divergirem, siga o texto e diga que divergiu. Uma ficha de fonte conferida, no brief, vale mais que ele: se ela o contradiz, siga a ficha e aponte o trecho. Use o que serve à tarefa. Comece a entrega pela linha: esp-estatistica@1.2 · 3f9a1c
</instrucao>
<conteudo>
… o SKILL.md inteiro, sem o cabeçalho …
</conteudo>
<modulo nome="poder-e-amostra">
… o módulo inteiro …
</modulo>
<modulo nome="eventos-raros">
… o módulo inteiro …
</modulo>
<errata>
E-1 · 2027-01-15 · onde se lê …, o certo é …; fonte: F-077
</errata>
</especialidade>
```

**Sem skill:**

```markdown
<especialidade nome="nenhuma" pedida="fatores humanos e ergonomia" lacuna="LAC-012">
<instrucao>
Não há conhecimento curado desta especialidade. Fale por ela com o que sabe, marque "conhecimento geral, sem fonte" em toda afirmação central que não venha de uma ficha de fonte do brief e diga que fonte a conferiria. Comece a entrega pela linha: sem skill · LAC-012
</instrucao>
</especialidade>
```

- **Ordem do brief:** o bloco no topo; depois, os materiais longos (fichas de fonte, pauta e versão base); no fim, o envelope, com a tarefa. Para entradas de uns 20 mil tokens ou mais, a Anthropic recomenda os documentos no topo e a pergunta no fim, o que melhorou as respostas em até 30% nos testes dela ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/long-context-tips)).
- **Errata:** entra no bloco de toda `esp-*` com correção confirmada, até sair a versão nova; enquanto isso, a `esp-*` fica "em revisão".
- **O envelope da condutora ganha dois campos,** `ficha` e `especialidade`:

```markdown
brief: B-4.3-12
para: especialista da equipe de elaboração, estatistica-1
ficha: E-4.3-p7-03
especialidade: esp-estatistica@1.2 · 3f9a1c · módulos poder-e-amostra e eventos-raros
skill: equipe-especialistas, com a cir-divergencia
sub-etapa: 4.3 · passo 7 · dose completa
vê: a pauta, a versão base sem autoria, as fichas de fonte F-031 e F-044 e a ata
não vê: a autoria e o modelo dos outros
entregar: a preparação, no formato da equipe, começando pelo selo
```

### 8.7 Problema de teste

No repositório fechado dos testes, uma pasta por `esp-*`:

```markdown
### T-decisao-03 · receita · variante nova
- enunciado: Um exame de triagem tem sensibilidade de 90% e especificidade de 95%. A condição atinge 2% de quem faz o exame. Uma pessoa teve resultado positivo. Qual a chance de ela ter a condição?
- gabarito: cerca de 27% (0,9 × 0,02 = 0,018; 0,018 + 0,05 × 0,98 = 0,067; 0,018 ÷ 0,067 ≈ 0,27)
- fonte do gabarito: teorema de Bayes; conta refeita pelo script
- aceita: de 26% a 28%
- erro que pega: ignorar a taxa de base e responder perto de 90%
- escopo: dentro
```

- **Variantes novas:** metade ou mais dos problemas muda os números e o contexto dos exemplos clássicos, para medir o raciocínio e não a memória (risco 3).
- **Fora do escopo:** 1 ou 2 por `esp-*`, de uma área vizinha, para ver se ela atrapalha onde não devia entrar.
- **Sem gabarito possível,** a área usa rubrica, julgada às cegas (seção 13).
- **Este exemplo fica fora do banco,** porque está publicado aqui.

## 9. Adaptador

O recrutamento, as fichas e os blocos são os mesmos em qualquer ferramenta; o adaptador muda só o jeito de o bloco chegar ao agente e de conferir que chegou inteiro.

| Ambiente | Como a especialidade chega | Como se confere |
| --- | --- | --- |
| Notion, primeiro | O `brief.py` da condutora põe o bloco no topo do brief da sessão filha, sem reescrever. O brief é a primeira mensagem da sessão, num computador novo, como no conselho | A condutora compara a primeira mensagem da sessão, pelos eventos, com o arquivo em `briefs/`, e confere o selo da entrega |
| Claude Code, na fase 10 | O subagente do papel, das definições das skills genéricas, recebe o bloco na mensagem de delegação, sem a ferramenta `Skill`. O teste da fase 10 compara com uma definição gerada para a sessão (`--agents`), com o campo `skills`, que injeta a skill inteira no contexto do subagente ([Claude Code: subagentes](https://code.claude.com/docs/en/sub-agents)) | O selo e a transcrição do subagente, que o Claude Code guarda num arquivo próprio, comparada com o arquivo em `briefs/` |
| Outras ferramentas e API | O mesmo brief, em texto: o bloco abre a mensagem do agente | O selo; a transcrição, quando o ambiente a dá |
- **Por que um bloco no brief, e não a skill carregada pelo agente:**
    - **Presença garantida.** Uma skill depende de o modelo acioná-la, e ele tende a não acionar ([`skill-creator`](https://github.com/anthropics/skills/tree/main/skills/skill-creator)).
    - **Isolamento.** No Notion, a `esp-*` do banco de Skills é uma página: carregá-la é ler o workspace, o que os agentes cegos não fazem e a auditoria marca.
    - **Versão fixa.** O bloco sai do Git, com tag e hash, e a ficha e o selo registram o texto exato que o agente leu.
    - **Universal.** Qualquer agente com chat recebe texto.
- **Sem definição de subagente por especialidade.** A especialidade muda a cada equipe; as definições ficam por papel, nas skills genéricas, e a especialidade chega no brief. Isso responde à pergunta da seção 9 do plano geral.
- **No Claude Code, quem escreve a mensagem de delegação é o modelo principal** ([Claude Code: subagentes](https://code.claude.com/docs/en/sub-agents)), que pode resumir o bloco sem querer. Por isso o selo e a comparação com `briefs/` valem também lá, e o teste da fase 10 decide entre o bloco na mensagem e o campo `skills`.
- **Interface:** `brief_esp.py montar --ficha E-4.3-p7-03` devolve o bloco e o hash; `brief_esp.py selo --ficha E-4.3-p7-03 --entrega <arquivo>` confere a primeira linha da entrega.

## 10. Modelos e custo

| Papel | Modelo |
| --- | --- |
| Recrutadores do mapa | O modelo da condutora, salvo outra escolha sua no 0.3 |
| Recrutar, nos passos 3, 7 e 8 | A própria condutora, com esta skill |
| Gerador cego de disciplinas distantes | O modelo dos geradores |
| Especialistas, geradores e membros de conselho com `esp-*` | O modelo do papel, no mapa de modelos; a `esp-*` não muda o modelo |
| Escritor e revisor das `esp-*`, na curadoria | Claude, o mais forte disponível: a curadoria é rara, e cada erro passa a todos que usam a `esp-*` (achado 5) |
| Autor dos problemas de teste | Claude, o mais forte, numa sessão que não vê a `esp-*` |
| Executores do teste | O modelo de cada papel que vai usar a `esp-*`, e um modelo menor (achado 2) |
| Avaliadores cegos e juízes | Claude, numa sessão que não produziu o que julga, como no conselho |
| Scripts | Sem modelo |
- **Claude primeiro:** a v1 é toda Claude. Outra família entra na fase 10, só no papel em que vencer às cegas, a começar pelos geradores, como no plano geral. A `esp-*` é texto e vai igual a qualquer modelo, mas o teste com e sem se refaz para cada modelo novo.
- **Modelo menor com a `esp-*`:** entra no teste de cada `esp-*`. Se ele alcançar o maior sem ela, a `ORIGEM.md` registra, e isso vira uma opção no 0.3, para o seu orçamento (achado 2).
- **Custo no projeto:** o recrutamento gasta pouco: no 2.7, três sessões (os dois recrutadores e o gerador) e a fusão; nos passos 3, 7 e 8, o trabalho da condutora e os scripts. O que pesa são os blocos: cada agente com `esp-*` recebe até umas 8.000 palavras a mais por brief. Daí os módulos só da ficha, o limite de tamanho, o bloco no topo, que é um começo de mensagem estável quando o ambiente tem cache de prompt, e o registro dos tokens dos blocos por sub-etapa, no `estado.json`.
- **Custo da curadoria:** cada `esp-*` custa a escrita, a conferência de cada afirmação, os problemas e 3 execuções com e sem, por modelo. É o gasto maior, e fica fora do projeto, na hora que você escolher.

## 11. Arquivos

```jsx
especialistas/
  SKILL.md                até umas 250 linhas: regras no topo, os cinco modos e o mapa das referências
  references/
    recrutamento.md       mapa inicial e do 2.7, recrutar, doses, distante, escolas e reserva
    papeis.md             o que cada papel vê e não vê, copiado da condutora (lido pelo fichas.py)
    formatos.md           ficha, especialistas.md, bloco, lacuna, ORIGEM.md e problema de teste
    modelo-esp.md         o modelo de uma esp-*, com os limites
    curadoria.md          entrar, rever e aposentar uma esp-*
    testes-esp.md         como escrever os problemas e aplicar a regra de entrada
    regras.md             as regras e os pensamentos da seção 7
    casos-limite.md       a seção 13, com respostas de exemplo
  scripts/
    catalogo.py           lê a biblioteca (versões, hashes, situação, validade e placar) e procura nas esp-* os marcadores dos casos de teste
    cobertura.py          cobertura de cada item, duplicatas, distante e crítico; --sugerir e --comparar
    fichas.py             novo e validar; sorteia os operadores dos geradores, com semente
    brief_esp.py          monta o bloco e confere o selo
    lacunas.py            novo, proxima e situacao
    teste_esp.py          roda o teste com e sem e aplica a regra de entrada
  assets/
    schemas/              ficha, catálogo, lacuna e ORIGEM, em JSON Schema
    modelos/              ficha, especialistas.md, lacuna e o esqueleto de uma esp-*
  evals/                  pedidos de acionamento e mapas e fichas plantados (seção 14)
```

**A biblioteca, à parte:**

```jsx
biblioteca-esp/           repositório próprio, com Git e uma tag por versão de cada esp-*
  catalogo.json           cada esp-*: versão em uso, hash, escopo, situação, validade e placar
  lacunas.md              a fila, com origem e prioridade
  esp-estatistica/        no modelo da seção 8.3
  esp-decisao/
  …
biblioteca-esp-testes/    repositório fechado, com os problemas e os gabaritos de cada esp-*; a sessão que escreve uma esp-* nunca o clona
```

**No dossiê:**

```jsx
cir/<projeto>/
  especialistas.md        o mapa: especialidades, distantes, equipes-base, conselhos, preferências e lacunas
  fichas/                 uma página por formação, <sub-etapa>-p<passo>.md, com as fichas de cada rodada
```

- **Os marcadores dos casos de teste** ficam no repositório de testes do sistema, fora da skill; o `catalogo.py` só os lê.
- **No Notion:** a skill vira uma página do banco de Skills, as referências viram subpáginas, e os scripts e modelos vão em Files, como nas outras. A biblioteca fica clonada no computador da condutora, na tag em uso, e o `estado.json` registra o commit.
- **No plugin do Claude Code,** a biblioteca vai junto, numa tag fixa.

## 12. Subagentes

| Agente | Formação | Vê | Não vê | Ferramentas |
| --- | --- | --- | --- | --- |
| Recrutador do mapa | Isolado, numa sessão nova; no 2.7, dois, sem ver um ao outro | O problema (a ficha do projeto e o material separado, no mapa inicial; o mapa do tema 2, no 2.7), as fichas da pesquisa sobre disciplinas, as suas preferências e a sua versão sem autoria; o catálogo, só depois de entregar as disciplinas | O outro recrutador, o banco de ideias, os casos reservados e o placar | Python, para o `cobertura.py` |
| Gerador cego de disciplinas distantes | Isolado, no 2.7 | O job, as causas e as contradições, escritos como funções | A sua versão, os mapas dos recrutadores e o catálogo | Busca e leitura na web |
| Recrutador dos passos 3, 7 e 8 | A condutora, com esta skill, porque só ela lê o dossiê | O cartão, o `especialistas.md` e o catálogo | — | Os scripts |
| Escritor da `esp-*` | Sessão nova, fora do projeto | O escopo, as fontes de referência e as skills de ponto de partida | Os problemas de teste e os casos de teste do sistema | Busca e leitura na web e Python |
| Conferentes | Os pesquisadores da `pesquisa-cientifica`, nos modos conferir e refutar | As afirmações da `esp-*`, com as fontes citadas | Os problemas de teste | Busca e leitura na web |
| Autor dos problemas | Sessão nova, em paralelo à escrita | O escopo e as fontes de referência | A `esp-*` e os casos de teste do sistema | Busca e leitura na web e Python |
| Executores do teste | Uma sessão nova por execução; as duas condições lançadas juntas | O problema e, na condição com, o bloco | O gabarito e a outra condição | As do papel |
| Avaliador cego | Sessão nova | O problema, o gabarito ou a rubrica e as respostas, sem a condição | Com ou sem, e o modelo | Python |
| Juiz de identificabilidade | Sessão nova | As contribuições de uma reunião, sem nome, e a lista das especialidades da formação | As fichas, os nomes e a ata | Nenhuma |
| Juiz de cobertura | Sessão nova, nos testes | O problema, o mapa e os itens do cartão | Quem montou o mapa e quais itens foram plantados | Nenhuma |
- **Quem recruta não fala pela especialidade,** e quem fala não recruta.
- **Quem escreve a `esp-*` não vê os problemas,** e quem escreve os problemas não vê a `esp-*` (regra 12).
- **Com e sem, juntos:** as duas condições são lançadas ao mesmo tempo, como no [`skill-creator`](https://github.com/anthropics/skills/tree/main/skills/skill-creator), para que nada mude entre elas além da `esp-*`.

## 13. Casos-limite

| Situação | O que a skill faz | Registro |
| --- | --- | --- |
| A especialidade pedida não tem `esp-*` | Roda sem skill, marcado, com o bloco "nenhuma" e as fichas de fonte da especialidade, e registra a lacuna | Ficha "sem skill"; lacuna |
| Você pede para criar a `esp-*` agora, no projeto | Explica que a especialidade gerada na hora fica abaixo de não ter skill (achado 1) e oferece duas saídas: seguir sem skill, marcado, ou pausar a sub-etapa e abrir a curadoria numa sessão própria. Quem decide é você | Registro de decisão |
| Você pede uma pessoa real ("quero o Taleb") | Oferece a escola de pensamento, com as obras como fonte; não imita a pessoa | Ficha, campo `escola` |
| Você exclui uma especialidade que cobre uma causa central | Aceita; mostra o item que fica sem cobertura e pergunta se outra especialidade o cobre | Registro de decisão, com o risco; o `cobertura.py` marca o item |
| A pesquisa contradiz uma `esp-*` | Vale a ficha conferida: errata no bloco, a `esp-*` fica "em revisão", e o especialista recebe a errata no brief seguinte | Errata; catálogo |
| O problema pede mais especialidades do que a dose comporta | Entram as do `cobertura.py --sugerir`, e o resto fica de reserva. Se uma causa central ficar sem ninguém, a condutora sobe a dose ou pergunta a você | Ficha; reserva no mapa |
| Escolas divergem sobre o problema | Se a divergência importa para a sub-etapa, duas fichas da mesma especialidade, com escolas diferentes; senão, a escola das suas preferências | Ficha, campo `escola` |
| A área não tem gabarito possível | Problemas com rubrica, julgados às cegas por dois avaliadores; a regra de entrada vale igual | `ORIGEM.md`: "teste por rubrica" |
| Domínio sensível, como saúde, direito ou segurança | A `esp-*` traz os limites e quando um profissional precisa entrar; nenhuma ficha diz que o agente é profissional; o CIR marca o que pediria revisão profissional | Ficha; CIR |
| A mesma especialidade na elaboração e na verificação | Na verificação, outro agente, numa sessão que não elaborou; a `esp-*` pode ser a mesma | Ficha da verificação |
| Muda o modelo de um papel | As `esp-*` desse papel voltam ao teste, fora do projeto; no projeto, seguem em uso, e a ficha registra o modelo | Catálogo: "a retestar" |
| Uma `esp-*` passa do limite de tamanho | Não entra assim: vira duas especialidades ou mais módulos, e o teste decide | `ORIGEM.md` |
| Selo ausente ou errado na entrega | A execução é refeita; se repetir, a condutora confere o brief e o ambiente | Registro do brief |
| A biblioteca não tem nenhuma `esp-*` para o projeto | Roda tudo marcado; o CIR avisa que as especialidades rodaram sem skill, e você decide se abre a curadoria antes de seguir | CIR; lacunas |
| Você discorda de uma afirmação com fonte numa `esp-*` | A sua posição vai como preferência ou decisão sua; a afirmação só cai com contraprova, e a que você trouxer vai à pesquisa, no modo conferir | Registro de decisão; errata, se confirmada |
| Pedem uma credencial na ficha ("põe que é PhD") | Recusa, com o motivo (regra 4); a ficha diz o que o agente tem | — |

## 14. Testes e métricas

Os testes medem o recrutamento (cobertura, distância, diferença e honestidade) e o ganho de cada `esp-*`. Seguem a seção 13 do plano geral e o guia de testes do [`skill-creator`](https://github.com/anthropics/skills/tree/main/skills/skill-creator). Os testes de recrutamento usam os casos do sistema; os de `esp-*`, nunca (regra 12).
**Banco de testes:**

- **Acionamento:** os 20 pedidos da seção 3, 10 de cada lado.
- **Mapas com itens plantados:** os problemas dos casos do sistema, cada um com uma causa que só uma especialidade sem skill cobre, uma contradição de princípio e uma parte esquecida.
- **Fichas plantadas:** 30, com credencial, nome de pessoa, `esp-*` fora do catálogo, duas distantes, sem crítico ou com o "vê" mudado; o `fichas.py` e o `cobertura.py` têm de pegar todas.
- **Erro plantado:** uma `esp-*` de teste com um erro conhecido, rodada sem errata, com errata e com uma ficha de fonte que a contradiz.
- **Problemas de cada `esp-*`:** de 5 a 10 com gabarito e 1 ou 2 fora do escopo (seção 6.3).
**Regra de entrada de uma `esp-*`:**
1. 3 execuções por condição, com e sem, no modelo de cada papel que vai usá-la.
2. Ganho de 10 pontos ou mais na média de acerto.
3. Nenhum problema, nem os de fora do escopo, piora de forma consistente, isto é, em 2 das 3 execuções.
4. Empate não entra.

| Métrica | Como | Alvo |
| --- | --- | --- |
| Cobertura | `cobertura.py` nos mapas e o juiz de cobertura nos itens plantados | Todos os itens com especialidade, com ou sem skill |
| Lacunas | Toda ficha "sem skill" tem lacuna | 100% |
| Ganho da `esp-*` | Acerto com e sem, no gabarito | A regra de entrada |
| Fora do escopo | Acerto com e sem, nos problemas de fora do escopo | Sem piora |
| Identificabilidade | O juiz diz de que especialidade veio cada contribuição | O dobro do acaso ou mais, e acima da condição só com o nome da especialidade |
| Honestidade | Credenciais, instituições e pessoas reais nas fichas e nas entregas | Zero |
| Fidelidade do bloco | O hash do bloco que chegou igual ao do catálogo; o selo certo | 100% |
| Erro plantado | O especialista segue a errata e a ficha de fonte contrária | Em todas as execuções |
| Recrutada × fixa | As saídas da sub-etapa com a equipe recrutada e com uma equipe fixa, com as mesmas especialidades em todo problema, às cegas | A recrutada vence a maioria; o número sai da linha de base |
| Distante | Elaboração com e sem a distante: famílias novas e qualidade, às cegas | Fica na dose padrão se render |
| Acionamento | Os 20 pedidos | 9 de 10 ou mais de cada lado |
| Custo | Tokens dos blocos e das sessões, por sub-etapa e dose | Registrar, sem limite |

**Comparações que decidem o desenho,** em julgamento cego:

- **Com e sem a `esp-*`,** pela regra de entrada.
- **Equipe recrutada × equipe fixa.**
- **Dois recrutadores e fusão × um.**
- **Com e sem a distante,** e a distante como gerador cego × como membro da equipe.
- **Focada × exaustiva:** a `esp-*` × a documentação completa da área, no mesmo problema (achado 2).
- **Com `esp-*` × só persona,** no acerto e na identificabilidade (achado 3).
- **Modelo menor com a `esp-*` × maior sem** (achado 2).
- **Bloco no brief × campo `skills`,** no Claude Code, na fase 10.
- **Reuniões paralelas com a mesma composição × trocando um membro.**
Fica o que vencer; no empate, o mais simples.

## 15. Riscos

| Risco | Mitigação |
| --- | --- |
| Especialistas que são o mesmo modelo com outro nome | A diferença vem do conteúdo (a `esp-*`, as fontes e os operadores); nenhuma formação repete especialidade e ótica; teste de identificabilidade (achado 6) |
| Um erro numa `esp-*` passa a todos que a usam | Fonte em cada afirmação; conferir e refutar na curadoria; errata; a ficha conferida vence; a verificação confere os números centrais na pesquisa (achado 5) |
| Teste contaminado: o modelo já viu os problemas | Metade ou mais em variantes novas, escritas para o teste por quem não vê a `esp-*`. Num banco de matemática refeito do zero, no estilo de um conhecido, alguns modelos perderam até 8% de acerto, sinal de memória; os de fronteira, quase nada ([Zhang et al.](https://arxiv.org/abs/2405.00332)) |
| Uma `esp-*` com conteúdo dos casos de teste do sistema | Sala limpa (regra 12); o `catalogo.py` procura os marcadores dos casos |
| `esp-*` desatualizada | Validade de 12 meses; reteste quando muda o modelo de um papel; errata |
| Licença | Copiar só de MIT, Apache 2.0 ou CC BY, com atribuição; o resto, só como fonte citada; tudo na `ORIGEM.md` |
| Viés de recrutamento: sempre as mesmas especialidades | Recruta pelo problema; dois recrutadores; o catálogo só depois das disciplinas; o placar fora do recrutamento; o gerador cego de distantes; o juiz de cobertura |
| A primeira leva escolhida por quem conhece o Motor | O 2.7 do Motor recruta sem saber da leva, e o que ele pedir fora dela entra na fila; os testes das `esp-*` não usam o Motor |
| Autoridade falsa: um agente sem skill falando como especialista | A ficha, o selo e a ata marcam "sem skill". Sugestão para o plano da `equipe-especialistas`: a autoridade por especialidade (regra 4 da equipe, na seção 3 do plano geral) vale só com `esp-*` ou fonte conferida |
| A fila de lacunas só cresce | Prioridade explícita; você escolhe quando curar; a lacuna que não entra fica com o motivo |
| Custo dos blocos | Módulos só os da ficha; limite de tamanho; cache de prompt, quando houver; registro por sub-etapa; teste com o modelo menor |

## 16. O que fica de fora

- **Ajuste fino de modelos por especialidade.** A especialidade vem de texto curado, que se lê, se confere e se versiona.
- **Gerar especialidade na hora,** mesmo que seja "só um resumo" (regra 2).
- **Imitar pessoas reais.** Escola de pensamento, sim, com as obras.
- **Entrevistar especialistas humanos para escrever as `esp-*`.** Na v1, o especialista humano revisa o texto.
- **Escolher a equipe pelo placar,** como no DyLAN (regra 14).
- **Uma definição de subagente por especialidade, e Custom Agents,** pela regra "Universalidade primeiro".
- **Publicar a biblioteca:** fica para depois da v1, com a licença a definir.

## 17. Decidido e em aberto

**Decidido:**

- **Universal primeiro:** recrutamento, fichas, biblioteca e scripts valem em qualquer agente com chat; a especialidade chega como um bloco de texto no topo do brief, sem depender da ferramenta de skills.
- **Claude primeiro:** recrutadores, escritores, revisores e especialistas são Claude; outra família só no papel em que vencer às cegas, na fase 10.
- **O modelo de cada papel é o que você escolhe no 0.3;** a `esp-*` não muda o modelo, e o teste mostra se um modelo menor com ela basta.
- **Recruta pelo problema,** com uma especialidade distante por elaboração, com a função análoga escrita, e o crítico em toda equipe.
- **Nunca gera especialidade na hora;** sem `esp-*`, o agente roda marcado, e a falta vira lacuna.
- **Sem credenciais e sem pessoas reais;** escolas de pensamento, sim, com as obras.
- **Uma `esp-*` só entra com ganho** no teste com e sem, e tem versão, hash e origem.
- **Mapa inicial ao fechar o tema 0 e mapa do 2.7** com dois recrutadores e fusão. Recrutar não pede a sua aprovação a cada vez; uma especialidade de fora do mapa pede um sim ou não.
- **Primeira leva de seis,** na ordem da seção 6.5; o 2.7 do Motor confirma.
- **Sem definição de subagente por especialidade.**
- **Critério máximo:** na dúvida entre dois desenhos, vale o que mais contribui para uma ideia melhor, mais criativa e eficaz; custo e tempo vêm depois.
**Em aberto:**
- **Especialista humano:** se há alguém que possa revisar alguma `esp-*` da primeira leva, e de que área.