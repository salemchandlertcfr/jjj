# Plano detalhado — cir-sintese

<aside>
📜

**O que é:** o plano detalhado da `cir-sintese`, a skill de método das sub-etapas 6.1 a 6.6 do tema 6 do [Fluxograma completo — Etapa 1 (método IDEAL em ciclo)](https://app.notion.com/p/Fluxograma-completo-Etapa-1-m-todo-IDEAL-em-ciclo-f1f71e3bd5e6487ebdfc94cd7e9fa161?pvs=21), que é o passo 9 do IDEAL. Ela transforma o dossiê no CIR e o entrega às etapas seguintes sem perder nem inventar nada no caminho: monta as 17 seções a partir do que cada tema gravou, com a origem de cada frase à vista e os trechos que obrigam ou prometem copiados por script; escreve só as ligações, conferidas afirmação por afirmação por quem não as escreveu; gera das mesmas fontes o pacote da Etapa 2 e o estacionamento da Etapa 3; põe leitores sem contexto para dizer com as próprias palavras o que entenderam, antes de perguntar; checa o critério de pronto pela evidência de cada item, e não por tique; e fecha o projeto com a sua aprovação e uma retrospectiva que compara o que se previu com o que aconteceu. É a sétima e última skill de método do item 7 da ordem da seção 15 do [Plano geral das skills — Etapa 1 (CIR)](https://app.notion.com/p/Plano-geral-das-skills-Etapa-1-CIR-72d0fdc1db19433e9101d1ac3b3015ef?pvs=21), depois da [Plano detalhado — cir-prova](https://app.notion.com/p/Plano-detalhado-cir-prova-d9314866db864324bca0e773fc6553a7?pvs=21), e entrega à [Plano detalhado — etapa-1-cir (condutora)](https://app.notion.com/p/Plano-detalhado-etapa-1-cir-condutora-fccda0c36a5d403582b433a6f2b0657f?pvs=21) o cartão do tema 6 e os do 6.1 ao 6.6, no formato combinado; o 6.6 é a trava. Os agentes chegam pelas skills genéricas, nos formatos do [Plano detalhado — conselho-especialistas](https://app.notion.com/p/Plano-detalhado-conselho-especialistas-f31c25a61c914fd98fe1f1ad81c09ed4?pvs=21), do [Plano detalhado — pesquisa-cientifica](https://app.notion.com/p/Plano-detalhado-pesquisa-cientifica-b0dde96c53b34b38aa26c8c474ce1071?pvs=21), do [Plano detalhado — grill-embasado](https://app.notion.com/p/Plano-detalhado-grill-embasado-ec54d7f985534c0a997926c075d97775?pvs=21), do [Plano detalhado — especialistas](https://app.notion.com/p/Plano-detalhado-especialistas-79544cfde9c5403babc8e5cc62fe12cd?pvs=21) e do [Plano detalhado — equipe-especialistas](https://app.notion.com/p/Plano-detalhado-equipe-especialistas-184104fa869f40b6a3589890879df668?pvs=21).
**Universal primeiro:** o método, os cartões, os formatos e os scripts valem em qualquer agente com chat; quem conduz é a condutora, no ambiente dela; o CIR é um arquivo markdown no dossiê, e o espelho no Notion é só leitura. **Claude primeiro:** redator, decompositor, verificador, leitores, crítico e conselho são Claude, nos modelos que você escolheu no 0.3; a independência do leitor vem da sessão nova e do que ele não vê, e não de trocar de modelo; verificador, leitores e juízes usam o modelo de juiz do mapa de modelos. **Para qualquer projeto:** startups, produtos, pesquisa ou projetos públicos; os exemplos de dentro da skill variam de domínio e nenhum usa os casos de teste.

</aside>

## 1. Propósito no fluxograma

**Propósito:** consolidar o dossiê no CIR e entregá-lo às etapas seguintes sem perder nem inventar nada: cada frase com a origem à vista, os trechos que obrigam ou prometem copiados sem mudança, o pacote e o estacionamento gerados das mesmas fontes, a clareza testada por quem não participou e o pronto mostrado por evidência, até a sua aprovação.

| Responde por | Como se vê |
| --- | --- |
| Nada inventado | O CIR não nasce de uma redação livre: o `cir.py montar` junta as 17 seções a partir dos blocos que o `registrar.py` gravou em cada tema e dos arquivos de origem. O redator escreve só as ligações; cada frase leva o ID de onde veio, e o `cir.py conferir` acusa a frase sem origem ou com uma origem que não existe |
| Nada promovido | Propósito, linhas vermelhas, restrições anti-ideais, princípios invariantes, métricas com os números, confianças e killer conditions entram como cópia literal, travada por hash. O `cir.py conferir` acusa número diferente da origem, qualificador retirado, confiança promovida e escopo alargado ("sempre", "todas", "garante"); cada ligação é decomposta em afirmações atômicas, conferidas uma a uma contra as fontes que ela cita, por quem não a escreveu |
| Nada perdido | Cobertura por script: toda linha vermelha, restrição, princípio, killer condition, alternativa viva, refutado com o desafio, dissenso e pendência aparece, com pelo menos 10 casos canônicos e o que você disse temer perder. O dissenso não é resumido, é copiado. A distribuição das ligações por tema vai ao crítico, para o último tema não tomar o lugar dos primeiros |
| Entendido sem você | No 6.4, três leitores novos, que só veem o CIR e o pacote, primeiro dizem com as próprias palavras o propósito, o núcleo, o que o conceito não é e a primeira tarefa da Etapa 2; só depois perguntam. Onde as reformulações divergem, há ambiguidade. Corrige-se a partir do dossiê ou de uma resposta sua, com registro, até não sobrar pergunta central e as reformulações baterem |
| Passagem que serve | O pacote da Etapa 2 diz o que fazer primeiro, liga cada capacidade às métricas que ela move, leva a bancada, as fronteiras com o que respeitar, os princípios e as restrições com o "refuta se" e o que fazer em vez disso, as alternativas vivas, o que não reintroduzir sem prova e o que reverteria a escolha |
| Estacionamento com motivo | Tudo o que os temas estacionaram, sem repetição, cada item com a origem e o motivo; o guardião confere que nada do que muda o resultado do propósito ficou ali |
| Pronto por evidência | O `pronto.py` confere os 14 itens pela evidência de cada um (arquivo, seção, ID e hash); item sem evidência é "não verificado", e não "passa". A vigia final, as pendências e a conferência das fontes rodam de novo no 6.5, e não são lembradas |
| Aprender com o projeto | A retrospectiva compara o que se previu, gravado antes, com o que aconteceu: o placar do conselho, as perguntas previstas do 6.4, o plano de dose, as voltas e a taxa de surpresa. Cada melhoria tem dono, uma skill e uma seção; os números de método vão ao `aprendizado.jsonl`, que a condutora lê no projeto seguinte |
| Seu | Você escreve a sua essência e o seu "o que não é" antes de ver os do redator; diz o que teme perder na passagem e o que a Etapa 2 não pode perder; prevê as perguntas do leitor antes de vê-las; responde o que só você sabe, e cada resposta vira registro; decide cada pendência, voltar ou ressalva; e aprova o CIR na trava |
- **Entra em:** 6.1 a 6.6, carregada pela condutora no 6.1, no lugar da `cir-prova`. Antes disso, só o formato dela: o esqueleto do `06-blocos.md`, o CIR em construção, que o `dossie_init.py` cria, e o formato do bloco, que o `registrar.py` grava a cada registro desde o tema 1, saem do `assets/` desta skill. No modo auditoria do tema 0, a condutora roda o `pronto.py --auditoria`.
- **Entrega:** `06-cir.md`, com as 17 seções e a origem de cada frase, montado a partir do `06-blocos.md`; `06-conferencia.md`, com as afirmações conferidas; `06-pacote-etapa-2.md` e o `pacote.json`; `06-estacionamento-etapa-3.md`; `06-passagem.md`, com as rodadas do teste; `06-pronto.md`; `06-retrospectiva.md`; os registros no `decisoes.md`; os desfechos no `conselho/placar.jsonl`; a chave "sintese" do `estado.json`; e, num projeto real, uma linha no `aprendizado.jsonl` e a oferta do espelho de leitura no Notion.
- **Alimenta:** a Etapa 2 (o pacote, a bancada, as fronteiras, as perguntas e o que reverteria a escolha); a Etapa 3 (o estacionamento e as saídas ideais como régua do MVP); o placar do conselho, com os desfechos; as skills, com as melhorias com dono; e a condutora dos projetos seguintes, pelo `aprendizado.jsonl`, que traz a fração de tangentes do 4.4 e o acerto das perguntas previstas.

## 2. Skills de base e o que se aproveita

| Base | O que se aproveita | O que é nosso | Licença |
| --- | --- | --- | --- |
| [`doc-coauthoring`](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring) (Anthropic, `skills`) | O teste de leitor: um sub-agente novo, só com o documento, responde às perguntas que um leitor faria, e o que ele erra mostra a lacuna; as checagens de ambiguidade, de suposição falsa, de contradição e do contexto que o texto supõe; corrigir e repetir até o leitor responder certo, de forma consistente, sem achar lacuna nova; prever de 5 a 10 perguntas de leitor antes do teste; começar pela seção com mais incógnitas e deixar o resumo para o fim; reler o todo por fluxo, repetição e contradição | O leitor reformula antes de perguntar; três leitores por rodada, e a divergência entre as reformulações como sinal de ambiguidade; as suas perguntas previstas, gravadas antes e comparadas com as reais; a classificação central ou secundária, e quem responde (o dossiê, só você ou ninguém); a correção só na origem, com a remontagem; o leitor no modelo de juiz | Não declarada, nem na pasta nem no repositório: só a ideia, citada, sem copiar texto |
| [`verification-before-completion`](https://github.com/obra/superpowers/tree/main/skills/verification-before-completion) (obra, `superpowers`) | Nenhuma afirmação de pronto sem evidência nova: identificar o que prova, rodar, ler a saída e só então afirmar; os pensamentos que pedem parada, como "deve estar certo", "estou confiante" e "só desta vez" | O `pronto.py`, que pede a evidência de cada um dos 14 itens (arquivo, seção, ID e hash) e marca "não verificado" o que não a tem; a vigia, as pendências e as fontes, rodadas de novo no 6.5, e não lembradas | MIT |
| [`discovery-agents-handoff`](https://github.com/klausners/discovery-agents-handoff) (klausners) | As citações travadas por hash; a métrica sem número na fonte marcada "precisa validar"; uma seção para a evidência que discorda; o núcleo determinístico num script; o teto de 3 rodadas | Os trechos fixos, copiados com o hash da origem; o dissenso copiado para a seção 17; o `cir.py`, que monta e confere; as 3 rodadas do 6.4, e a quarta só com o seu "sim" | MIT |
| [`handoff`](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff) e [`writing-for-agents`](https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents) (Matt Pocock, `skills`) | Escrever para que um agente novo continue o trabalho, sob medida para o que a próxima sessão vai fazer; não repetir o que já está em outro artefato, e apontar para ele pelo caminho; uma fonte única para cada sentido; o critério de conclusão verificável e exaustivo; dizer o comportamento esperado ao lado da proibição, porque a proibição sozinha puxa o que proíbe | O pacote abre com o que fazer primeiro; o que se entende vai no texto, e o que se confere, no ID e no caminho; o CIR e o pacote saem dos mesmos registros; cada princípio e cada restrição levam o "em vez disso" | MIT |
| [`think-after-action-review`](https://github.com/product-on-purpose/thinking-framework-skills/tree/main/skills/think-after-action-review) e [`think-pyramid-principle`](https://github.com/product-on-purpose/thinking-framework-skills/tree/main/skills/think-pyramid-principle) (product-on-purpose, `thinking-framework-skills`) | Comparar o esperado com o que aconteceu, nos dois sentidos, sem culpa, com o que manter e o que mudar, específico e com dono; reconstruir a expectativa que não foi gravada num sub-agente que não viu o resultado. A conclusão primeiro, com 3 a 5 argumentos sem sobreposição e sem lacuna, e a ressalva de que uma estrutura clara não prova o caso | A retrospectiva sobre o que foi gravado antes (o placar, as suas previsões, as perguntas previstas, o plano de dose e a taxa de surpresa), com a reconstrução cega marcada; cada melhoria com dono numa skill e numa seção; a primeira frase de cada seção do CIR como a conclusão dela, e a seção 1 como a essência | Apache 2.0 |
| [`create-prd`](https://github.com/phuryn/pm-skills/tree/main/pm-execution/skills/create-prd) (Paweł Huryn, `pm-skills`) | Completo é não ter lacuna que bloqueie a decisão; o que não se sabe vai a perguntas marcadas, e não a suposições; dizer o que ficou de fora | O "completo" do pacote: nenhuma lacuna que bloqueie a primeira decisão da Etapa 2; as perguntas da seção 15, cada uma com quem responde; o estacionamento, com o motivo de cada item | MIT |
| Métodos públicos | A passagem de plantão do I-PASS, que termina com a síntese de quem recebe e traz o plano de contingência, e o teach-back, em que quem recebe diz com as próprias palavras o que entendeu ([AHRQ](https://www.ahrq.gov/teamstepps-program/curriculum/communication/tools/ipass.html)); a rastreabilidade desde a origem; o registro de decisões de arquitetura; o checklist cirúrgico; a revisão depois da ação | A reformulação antes das perguntas, no 6.4; o "o que reverteria" e as killer conditions no pacote; o ID visível em cada frase; o "não reintroduzir sem prova"; o pronto por evidência; a retrospectiva com melhorias com dono | Métodos, sem licença; fontes nos achados abaixo |
| Plano geral, fluxograma, v2 e os planos prontos | O modelo das 17 seções do CIR e a origem de cada uma; os 14 itens do critério de pronto e os sinais de contaminação; o registro, as travas, o `registrar.py`, o `vigia.py` e o `pendencias.py`, da condutora; o conselho Passagem e o placar, do conselho; a conferência final das fichas, da pesquisa; o leitor do entendimento, do grill; o aviso das especialidades sem skill e do que pede revisão profissional, da `especialistas`; o dissenso, a confiança contada e o "o que reverteria", da `cir-prova`; a taxa de surpresa, da `cir-arquitetura` | O tema 6 inteiro, que nenhum plano anterior desenhou: como o CIR se monta, quem confere cada frase, quem lê sem contexto, o que se passa à Etapa 2 e como se aprende com o projeto | Nossos |
| Olhadas e deixadas de fora | O resto da `create-prd`: é de produto (personas, priorização, lançamento e métricas de negócio), o que o CIR deixa às etapas seguintes; avaliadores de resumo que dão uma nota ao texto todo: juízes de IA não pegam a infidelidade sutil (achado 6); reescrever o CIR inteiro a cada correção: é o telefone sem fio (achado 9) | — | — |

**Dezessete achados que mudam o desenho:**

1. **Quem escreve acha que foi entendido.** Falantes que diziam frases ambíguas com uma intenção esperaram ser entendidos mais vezes do que foram, e subestimaram a ambiguidade das próprias frases; quem ouvia de fora, sabendo a intenção, não superestimou ([Keysar e Henly, 2002](https://doi.org/10.1111/1467-9280.00439)). E quem sabe mais não consegue deixar de lado o que sabe ao prever o que outros, que sabem menos, vão fazer, mesmo com dinheiro em jogo ([Camerer, Loewenstein e Weber, 1989](https://doi.org/10.1086/261651)). **Daí:** nem o redator nem você julgam se o CIR está claro; quem julga são leitores em sessões novas, que só veem o CIR e o pacote, e a condutora não explica nada a eles. Conta o que eles entenderam, e não o que acham que entenderam.
2. **A passagem que funciona termina com a síntese de quem recebe.** Com o I-PASS, que tem a lista de ações, o plano de contingência e a síntese feita por quem recebe, os erros médicos caíram 23% e os eventos adversos evitáveis, 30%, em 10.740 internações de 9 hospitais ([Starmer et al., 2014](https://doi.org/10.1056/NEJMsa1405556); [AHRQ](https://www.ahrq.gov/teamstepps-program/curriculum/communication/tools/ipass.html)); pedir que quem recebe explique com as próprias palavras, e corrigir até acertar, funcionou em 19 de 20 estudos ([Talevski et al., 2020](https://doi.org/10.1371/journal.pone.0231350)). **Daí:** o 6.4 começa pela reformulação, antes de qualquer pergunta; o pacote abre com o que fazer primeiro e traz o que reverteria a escolha, que é o plano de contingência da Etapa 2.
3. **Prever as perguntas do leitor se aprende vendo leitores de verdade.** Escritores que previram os problemas de leitores e depois leram as transcrições de leitores reais pensando em voz alta passaram a prever mais problemas, e a achar os que vinham de omissões, do que os que aprenderam com técnicas de análise de público ([Schriver, 1992](https://doi.org/10.1177/0741088392009002001)); a `doc-coauthoring` também pede de 5 a 10 perguntas previstas antes do teste. **Daí:** as suas perguntas previstas são gravadas, com hash, antes da primeira rodada e comparadas com as reais; o acerto vai à retrospectiva e ao `aprendizado.jsonl`; e o leitor procura também o que falta, e não só o que está confuso.
4. **Modelos não reconhecem bem a própria ambiguidade.** Num conjunto de frases ambíguas, as desambiguações que o GPT-4 escreveu foram julgadas corretas em 32% das vezes, contra 90% das escritas por pessoas ([Liu et al., 2023](https://arxiv.org/abs/2304.14399)). **Daí:** a ambiguidade não se pergunta ao leitor; ela aparece quando três reformulações independentes divergem. E o leitor marca, em cada resposta, se deduziu ou chutou, com a frase em que se apoiou.
5. **Resumo inventa, e o erro se esconde numa frase.** Modelos de resumo puseram nos resumos conteúdo que não estava no documento, e as medidas de sobreposição de palavras não mediram a fidelidade; a checagem de implicação mediu melhor ([Maynez et al., 2020](https://arxiv.org/abs/2005.00661)); quebrar o texto em afirmações atômicas mostrou que só 58% das afirmações de biografias do ChatGPT tinham apoio ([Min et al., 2023](https://arxiv.org/abs/2305.14251)). **Daí:** o CIR é montado por script, a partir dos registros; o redator só escreve as ligações; e cada ligação é quebrada em afirmações atômicas, conferidas uma a uma contra as fontes.
6. **A infidelidade sutil, as omissões e a ênfase no fim passam pelos juízes.** Em resumos de livros inteiros, a maior parte das afirmações infiéis tratava de eventos e de estados de personagens e só caía com raciocínio indireto sobre a narrativa; avaliadores automáticos não as pegaram com segurança; e os resumos omitiam muito e davam peso demais ao fim do livro ([Kim et al., 2024](https://arxiv.org/abs/2404.01261)). **Daí:** a conferência é por afirmação, com a fonte de cada uma, e por script onde dá (números, hashes, IDs); a cobertura é item a item, contra a lista dos registros; e a distribuição das afirmações por tema vai ao crítico, para o tema 5 não engolir os outros.
7. **Resumir generaliza, e pedir precisão piora.** Em 4.900 resumos de artigos científicos, feitos por 10 modelos, os resumos tiveram cerca de cinco vezes mais generalizações amplas que os escritos por pessoas; pedir precisão quase dobrou a chance de generalizar; os modelos mais novos foram piores; e os Claude, os mais fiéis ([Peters e Chin-Yee, 2025](https://doi.org/10.1098/rsos.241776)). **Daí:** os qualificadores, o escopo e a confiança vêm da origem e são conferidos pelo `cir.py`, que acusa "sempre", "todas" e "garante", o presente genérico no lugar do passado de um caso e o qualificador retirado. "Seja preciso" no brief não substitui a conferência, e a regra vale mesmo com o Claude.
8. **Resumos apagam vozes.** Resumos de textos com perspectivas diversas deixaram parte delas de fora, de forma desigual ([Zhang et al., 2024](https://arxiv.org/abs/2311.07884)); a `discovery-agents-handoff` guarda uma seção só para a evidência que discorda. **Daí:** o dissenso entra por cópia na seção 17, nunca resumido, e as alternativas vivas e as refutadas aparecem com o motivo, com o que as refutou e com o desafio guardado.
9. **Texto reescrito por modelos, de mão em mão, deriva.** Em cadeias de transmissão em que cada modelo reescreve o texto do anterior, os textos derivaram para formas que os modelos preferem, e perderam diversidade ([Perez et al., 2024](https://arxiv.org/abs/2407.04503)). **Daí:** o CIR se remonta a partir dos registros, e nunca se reescreve sobre a versão anterior; o pacote e o estacionamento saem das mesmas fontes, e não do CIR.
10. **O que fica no meio se perde, e quem lê procura a conclusão.** Modelos usaram melhor a informação no começo e no fim de um contexto longo do que no meio ([Liu et al., 2024](https://arxiv.org/abs/2307.03172)); o princípio da pirâmide põe a conclusão primeiro, e lembra que uma estrutura clara não prova o caso (`think-pyramid-principle`). **Daí:** o redator escreve uma seção por vez, em sessão própria, com só as fontes dela; a essência abre o CIR; a primeira frase de cada seção é a conclusão; e os leitores marcam onde se perderam.
11. **A rastreabilidade que falha é a da origem.** Numa pesquisa com mais de cem profissionais, os problemas de rastreabilidade de requisitos vinham, sobretudo, de não se saber de onde um requisito veio e por quê, e não de segui-lo dali em diante ([Gotel e Finkelstein, 1994](https://doi.org/10.1109/ICRE.1994.292398)). **Daí:** cada frase do CIR leva o ID da origem, visível; o `cir.py` acusa a frase sem origem ou com ID que não existe; e o CIR abre com o "Como ler", que explica os prefixos.
12. **Sem o motivo, a decisão evapora.** A arquitetura de um sistema é um conjunto de decisões, e, quando o motivo delas se perde, quem vem depois as desfaz sem saber, e o sistema se degrada ([Jansen e Bosch, 2005](https://doi.org/10.1109/WICSA.2005.61)). **Daí:** o pacote traz o que não reintroduzir sem prova, com o que refutou cada ideia; e a seção 17 guarda, para cada decisão, o contexto, as opções, o motivo nas suas palavras e o que a reverteria.
13. **Um checklist ajuda quando é feito, e não quando é marcado.** Com a lista de verificação cirúrgica, as mortes caíram de 1,5% para 0,8% e as complicações, de 11,0% para 7,0%, em 8 hospitais ([Haynes et al., 2009](https://doi.org/10.1056/NEJMsa0810119)); tornada obrigatória em 101 hospitais de Ontário, não reduziu de forma significativa nem as mortes nem as complicações ([Urbach et al., 2014](https://doi.org/10.1056/NEJMsa1308261)); e a `verification-before-completion` proíbe dizer "pronto" sem evidência nova. **Daí:** o `pronto.py` pede a evidência de cada item (arquivo, seção, ID e hash), e o que não tem é "não verificado"; a vigia, as pendências e a conferência das fontes rodam de novo no 6.5.
14. **Palavras de probabilidade se leem de jeitos diferentes, e só o número no texto ajuda.** Com 924 participantes, a leitura de expressões como "muito provável" bateu com a intenção do autor em 66% quando o número vinha entre parênteses no texto, contra 32% sem ele; tabela à parte e dica ao passar o mouse quase não ajudaram ([Wintle et al., 2019](https://doi.org/10.1371/journal.pone.0213522)). **Daí:** toda confiança e toda palavra de probabilidade do CIR vêm com a base em números, entre parênteses, no próprio texto, como em "confiança média (6 de 7 condições)".
15. **A retrospectiva rende quando tem estrutura e registro.** Reuniões de revisão (debriefs), de equipes e de indivíduos, melhoraram o desempenho em cerca de 25% sobre o controle, em 46 amostras, com d = 0,67 ([Tannenbaum e Cerasoli, 2013](https://doi.org/10.1177/0018720812448394)); a revisão depois da ação, em 61 estudos, teve d = 0,79, e rende mais com registro objetivo do que com a memória de quem participou ([Keiser e Arthur, 2021](https://doi.org/10.1037/apl0000821)); e ela compara o esperado com o que aconteceu, sem culpa, com mudanças específicas e com dono (`think-after-action-review`). **Daí:** o 6.6 trabalha sobre os registros objetivos do dossiê, e não sobre a lembrança; cada melhoria tem dono, uma skill e uma seção.
16. **Depois do desfecho, tudo parece previsível, e a decisão é julgada pelo resultado.** Quem sabia o desfecho achou que ele era mais provável do que achava quem não sabia, e não percebeu a diferença ([Fischhoff, 1975](https://doi.org/10.1037/0096-1523.1.3.288)); a mesma decisão foi julgada pior quando o resultado foi ruim ([Baron e Hershey, 1988](https://doi.org/10.1037/0022-3514.54.4.569)). **Daí:** a retrospectiva compara com as previsões gravadas antes; a expectativa que não foi gravada é reconstruída por um agente que não vê o desfecho, e vai marcada; e uma decisão boa com desfecho ruim não é contada como erro.
17. **Quem escreveu não deve conferir, e o juiz prefere o próprio texto.** Sem informação de fora, modelos que revisaram as próprias respostas não melhoraram, e às vezes pioraram ([Huang et al., 2023](https://arxiv.org/abs/2310.01798)); juízes de IA reconheceram e favoreceram o que eles mesmos geraram ([Panickssery, Bowman e Feng, 2024](https://arxiv.org/abs/2404.13076)). **Daí:** o redator não confere o que escreveu; o verificador, os leitores e os juízes rodam no modelo de juiz do mapa de modelos, em sessões que não escreveram nada.

**O que muda no fluxograma:** no 6.1, o CIR é montado pelo `cir.py` a partir do CIR em construção, com os trechos fixos copiados e a origem em cada frase; o redator só escreve as ligações, uma seção por vez; a sua essência e o seu "o que não é" vêm antes dos do redator; e o verificador e o crítico conferem afirmação por afirmação. No 6.2, o pacote sai das mesmas fontes, pelo `pacote.py`, abre com o que fazer primeiro, e o conselho Passagem ensaia a primeira decisão da Etapa 2. No 6.3, o estacionamento junta o que os temas 0 a 5 estacionaram, sem repetição, com a origem e o motivo de cada item, e vira a régua do MVP. No 6.4, três leitores por rodada, sem contexto, reformulam antes de perguntar; as suas perguntas previstas são gravadas antes; a divergência entre as reformulações marca a ambiguidade; e a correção muda a origem, com registro, e remonta, em no máximo 3 rodadas. No 6.5, o `pronto.py` confere os 14 itens pela evidência, e a vigia, as pendências e as fontes rodam de novo. No 6.6, depois do "sim" na trava, a retrospectiva compara o previsto com o que aconteceu: o placar, a taxa de surpresa final, as melhorias com dono e, num projeto real, o `aprendizado.jsonl` e a oferta do espelho de leitura.

## 3. Acionamento

```yaml
---
name: cir-sintese
description: >-
  Método das sub-etapas 6.1 a 6.6 do tema 6 da Etapa 1 do IDEAL (passo
  9): monta o CIR a partir dos registros do dossiê, com a origem de cada
  frase e os trechos fixos copiados; confere o CIR afirmação por
  afirmação; gera o pacote da Etapa 2 e o estacionamento da Etapa 3 das
  mesmas fontes; testa a passagem com leitores sem contexto; checa o
  critério de pronto pela evidência; e, depois da aprovação, faz a
  retrospectiva do projeto. Carregada pela condutora no 6.1, no lugar da
  cir-prova. Use para redigir ou remontar o CIR, saber de onde veio uma
  frase, montar o pacote ou o estacionamento, testar se alguém de fora
  entende o CIR, checar se ele está pronto, auditar um documento contra
  o critério de pronto ou fazer a retrospectiva. Não use para escolher
  o conceito (cir-prova), mudar o propósito, as métricas ou o conceito
  (temas 1 a 5, por uma volta), escolher tecnologia (Etapa 2) nem tratar
  de mercado e preço (Etapa 3), a não ser no modo avulso.
---
```

- **Quem carrega:** a condutora, no 6.1, quando descarrega a `cir-prova`, pelo limite de 3 skills ativas. As skills dos temas 1 a 5 só voltam numa volta (seção 6.11), com o que a pede, e saem de novo quando ela fecha. Antes do tema 6, a skill não é carregada: o `dossie_init.py` e o `registrar.py` da condutora só usam o formato dela, que fica em `assets/` (seção 4). No modo auditoria do tema 0, a condutora carrega a skill só para rodar o `pronto.py --auditoria` e o `cir.py conferir --sem-dossie` (seção 6.12).
- **Modo avulso:** sem o dossiê, para quem quer saber se um documento de conceito está pronto ou se alguém de fora o entende. Grava em `sintese/<data>-<assunto>/`, numa pasta com Git, e roda dois passos: a auditoria, que aplica os 14 itens como perguntas e aponta a lacuna de cada um, e o teste de passagem, com as perguntas previstas pedidas antes, três leitores, reformulação e perguntas. Sem registros não há montagem: a skill não reescreve o documento, e o relatório diz isso no topo.
- **Reuso:** o teste de passagem serve a qualquer documento que outra pessoa ou outro agente vai usar sem quem o escreveu por perto, como um plano de projeto, uma especificação ou o brief de uma equipe; a montagem com origem, a qualquer síntese de um processo com registros, como o relatório final de uma pesquisa; a retrospectiva contra o que se gravou antes, a qualquer projeto com previsões registradas. Na Etapa 2 e na Etapa 3, o método é o mesmo, e o cartão muda.

| Deve acionar | Não deve acionar |
| --- | --- |
| "Fecha o CIR com o que já decidimos" | "Escolhe entre os dois conceitos que sobraram" (5.7, `cir-prova`) |
| "De onde veio esta frase do CIR?" | "Muda a métrica M1; ela ficou dura demais" (tema 3, `cir-idealidade`, pela volta 6→3) |
| "Monta o pacote para a Etapa 2" | "Que tecnologia usamos para avisar as famílias?" (Etapa 2, por `fronteiras.md`) |
| "Alguém de fora entenderia este CIR?" | "Quanto a prefeitura pagaria por isso?" (Etapa 3, por `estacionamento.md`) |
| "Já está pronto? O que falta?" | "Escreve o pitch para os investidores" (fora do IDEAL) |
| "Audita este documento contra o critério de pronto" | "Resume o dossiê numa página para o prefeito" (resumo sem origem, para terceiros: fora, seção 15) |
| "Faz a retrospectiva do projeto" | "Acrescenta uma capacidade nova ao CIR" (tema 4, `cir-arquitetura`, pela volta 6→4.9 ou 6→4.12) |

## 4. Contrato de entrada e saída

**Entradas:**

| Entrada | De quem | Forma |
| --- | --- | --- |
| O CIR em construção: um bloco por item registrado, com a seção do CIR, a sub-etapa, o registro, o tipo, o trecho e o hash da origem | A condutora, pelo `registrar.py`, desde o tema 1, no formato do `assets/cir-bloco.md` desta skill | `06-blocos.md`, que o `dossie_init.py` cria vazio, com as 17 seções do `assets/cir-modelo.md` |
| Propósito congelado, com as formulações descartadas e o motivo; job e estado ideal; partes; valores e linhas vermelhas | Tema 1, pela `cir-proposito` | `01-proposito.md`, com o hash do 1.7 no estado |
| O fenômeno, as contradições, as falhas e como se resolve hoje; os casos | Tema 2, pela `cir-mapa` | `02-mapa.md`; `casos/trabalho.md` e `casos/reservados.md`, com os hashes |
| Métricas selecionadas, com a linha de base, a fonte e o limite ideal; o RFI; o critério de refutação | Tema 3, pela `cir-idealidade` | `03-idealidade.md` e `03-criterio.md`, abertos desde o tema 5 |
| Desafios, famílias, esboço, banco classificado, restrições anti-ideais, RFI por função e taxa de surpresa; as famílias que seguem, com as capacidades, os cenários, o núcleo e os princípios invariantes | Tema 4, pela `cir-divergencia` e pela `cir-arquitetura` | `04-desafios.md`, `04-familias.md`, `04-esboco.md`, `04-triagem.md` e `04-arquitetura.md` |
| Saídas ideais, vereditos, R, R5, pré-mortem, red team, matriz e a decisão do 5.7, com a confiança, as killer conditions e o que reverteria | Tema 5, pela `cir-prova` | `05-saidas.md` e `05-prova.md`, seção Decisão; a chave "prova" do `estado.json` |
| Os registros, com o motivo nas suas palavras, o dissenso e a confiança | Todas as sub-etapas | `decisoes.md` |
| O banco de ideias, as fronteiras e o estacionamento, com a origem de cada item | Todos os temas, desde o 0.2 | `banco.md`, `fronteiras.md` e `estacionamento.md` |
| As fichas de fonte e as conferências | `pesquisa-cientifica` | `fontes/` e `fontes/conferencias/` |
| O Entendimento e as checagens de cada sub-etapa | `grill-embasado` | `grill/` e a seção Entendimento de cada arquivo de tema |
| Os vereditos e o placar, com a probabilidade de resistir de cada um | `conselho-especialistas` | `conselho/` e `conselho/placar.jsonl` |
| Pendências, doses planejadas e usadas, voltas, travas, mapa de modelos e as chaves de cada tema | A condutora | `estado.json` |
| Os números de método dos projetos reais anteriores | Esta skill, nos projetos anteriores | `aprendizado/aprendizado.jsonl`, no repositório das skills, só para leitura, no 6.6 |

**Saídas:**

| Saída | Conteúdo | Para quem |
| --- | --- | --- |
| `06-cir.md` | O CIR montado: o "Como ler", as 17 seções, cada frase com a origem, os trechos fixos entre «», as ligações conferidas e a versão (commit); gerado pelo `cir.py`, e nunca editado à mão | Você, a Etapa 2, a Etapa 3 e o espelho de leitura |
| `06-blocos.md` | Os blocos de origem, acrescidos das ligações, das suas versões da essência e do "o que não é" e do histórico de cada bloco; é a fonte única do `06-cir.md` e do pacote | O `cir.py`, o `pacote.py` e a vigia |
| `06-conferencia.md` | A cada montagem: o que o `cir.py conferir` acusou, as afirmações de cada ligação com o veredito do verificador, a cobertura item a item, a distribuição por tema e o parecer do crítico | Você; o `pronto.py`; o CIR, seção 17 |
| `06-pacote-etapa-2.md` e `pacote.json` | As 9 partes do pacote (seção 6.6), com os IDs; o `pacote.json` traz o mesmo em campos, para os agentes da Etapa 2 | A Etapa 2 |
| `06-estacionamento-etapa-3.md` | O que os temas estacionaram, sem repetição, por tipo, com todas as origens e o motivo de cada item; as saídas ideais como régua do MVP | A Etapa 3 |
| `06-passagem.md` | As suas perguntas previstas, com o hash; cada rodada, com as reformulações, as perguntas, os vereditos dos juízes, a classificação e a correção de cada pergunta; o previsto × o real | A retrospectiva; o CIR, seção 17 |
| `06-pronto.md` | Os 14 itens, cada um com a evidência e o estado (passa, falha ou não verificado); as pendências; a vigia final; a conferência das fontes; as ressalvas, com o motivo e o objetivo nas suas palavras | Você, na trava; o CIR, seção 17 |
| `06-retrospectiva.md` | O esperado × o acontecido, nos dois sentidos; o placar com os desfechos e a calibração; a dose; as voltas; a taxa de surpresa final; o que manter e o que mudar, com dono | Você e as skills; o `aprendizado/melhorias.md` |
| `decisoes.md` e `estado.json` | Um registro por sub-etapa e por volta, de D-051 em diante no exemplo; a chave "sintese", com os hashes; a trava do tema 6 em "travas" | A condutora e a vigia |
| `conselho/placar.jsonl` | Os desfechos que o tema 6 conhece: os conceitos que resistiram e os que caíram no 5.7, os controles do 5.1 e as perguntas centrais do 6.2, com o desfecho da correção | O `placar.py` do conselho |
| `aprendizado/aprendizado.jsonl` e `aprendizado/melhorias.md`, no repositório das skills | Só num projeto real: uma linha de números e notas de método, sem nada do conteúdo do projeto; e as melhorias, com dono | A condutora do próximo projeto, no 4.4; você, quando decidir mudar uma skill |
| Pedidos de volta | Ao tema 1, 2, 3, 4 ou 5, com a falta que os pede e o lugar onde ela nasceu | A skill de quem a volta é (seção 6.11) |

**Com as outras skills:**

- **Condutora:** cria o `06-blocos.md` pelo `dossie_init.py`, com o esqueleto do `assets/cir-modelo.md`; o modelo "CIR" da pasta `assets/modelos/` dela é gerado desse arquivo pelo mesmo script do repositório que gera o `subetapas.md`, e assim os dois não divergem. O `registrar.py` grava, a cada registro, os blocos no formato do `assets/cir-bloco.md`, e roda a vigia em cada um. A condutora lê os cartões, monta os briefs com o `brief.py`, roda os scripts da skill, grava os registros, cuida da trava do 6.6, oferece o espelho de leitura depois do "sim" e lê o `aprendizado.jsonl` no 4.4. O `pendencias.py` dela entra no 6.5.
- **`grill-embasado`:** o "grill quer entender" de cada cartão, uma pergunta por vez: no 6.1, a sua essência e o seu "o que não é", antes de ver as do redator, e o que você teme que se perca; no 6.2, o que a Etapa 2 não pode perder; no 6.4, as suas perguntas previstas, antes da rodada, e as respostas que só você tem, cada uma com registro; no 6.5, a decisão de cada pendência. O Entendimento e as checagens de cada sub-etapa entram na seção 17 pelo caminho, e as checagens que discordaram de você, por cópia.
- **`pesquisa-cientifica`:** o modo conferir. No 6.1, as fichas que uma ligação usa de um jeito novo; no 6.2, as perguntas científicas ainda abertas, com a data da busca; no 6.3, os motivos que citam fonte; no 6.5, todas as fichas citadas no CIR e no pacote, em `fontes/conferencias/C-6.5.md`.
- **`especialistas` e `equipe-especialistas`:** a equipe-base do tema, com as especialidades da tabela da seção 5; o redator de cada seção recebe a `esp-*` do tema dela; o crítico da equipe confere no 6.1 e no 6.5. Não há reunião de equipe no tema 6, como na tabela do plano geral: o trabalho aqui é montar, conferir e testar, e não elaborar.
- **`conselho-especialistas`:** o rápido Passagem no 6.2 (leitor da Etapa 2 sem contexto e guardião do propósito), no formato "perguntas centrais sem resposta no CIR"; o rápido do 6.3 (guardião e refutador); e, no 6.6, os desfechos, que o `placar.py` dele grava. Os critérios e o "refuta se" vêm do cartão, escritos antes.
- **`cir-proposito`, `cir-mapa`, `cir-idealidade`, `cir-divergencia`, `cir-arquitetura` e `cir-prova`:** entregam as saídas da tabela de entradas e recebem as voltas, cada uma com o que a pede. A `cir-sintese` nunca muda a saída de outro tema: pede a volta, e a skill dona executa.
- **Taxa de surpresa:** a final usa a regra do `surpresa.py` da `cir-arquitetura`, copiada no `retrospectiva.py` com a origem, sem depender da outra skill.

## 5. Cartões das sub-etapas

No formato da condutora: os campos que ela lê, na ordem do ciclo. O `cartoes.py` confere os cartões contra o índice de sub-etapas da condutora. O cartão do tema fica aqui, porque é esta skill que abre o tema 6; o 6.5 é a validação integrada, e o 6.6, a trava.

```markdown
### Tema 6 · CIR · com trava · 6.1 a 6.6 nesta skill
- abertura: o que a Etapa 2 precisa saber e o que você teme que se perca na passagem
- plano de dose: 6.1 padrão; 6.2 completa; 6.3 leve; 6.4 completa; 6.5 completa, integrada; 6.6 trava
- conselho: rápido Passagem no 6.2 (leitor da Etapa 2 sem contexto e guardião do propósito); rápido no 6.3 (guardião e refutador); no 6.1, o verificador e o crítico; no 6.4, os leitores e os juízes; no 6.5, os scripts e o crítico
- equipe-base: escrita técnica e passagem de trabalho, do domínio e engenharia de sistemas, do especialistas.md; quem escreve uma ligação não a confere, e nenhum leitor do 6.4 trabalhou no projeto
- integração: o 6.5 é a validação integrada, sem conselho completo: não há alternativas a comparar, e o olhar de fora vem dos leitores do 6.4 e do conselho Passagem
- trava: no 6.6, antes da retrospectiva; aprovação é "sim" a "Aprova o CIR ___ (commit ___), com as ressalvas ___?"
- fechados: dos leitores e dos juízes do 6.4, o dossiê, a conversa, o grill, os registros e as suas perguntas previstas; do verificador, tudo menos a afirmação e as fontes que ela cita; do redator, as suas versões da essência e do "o que não é"; do reconstrutor do 6.6, os desfechos
- sai: 06-blocos.md, com as ligações; 06-cir.md; 06-conferencia.md; 06-pacote-etapa-2.md e pacote.json; 06-estacionamento-etapa-3.md; 06-passagem.md; 06-pronto.md; 06-retrospectiva.md; os registros do tema; "sintese" no estado.json, com os hashes; e, num projeto real, a linha do aprendizado.jsonl e a oferta do espelho de leitura

### 6.1 Redação do CIR
- dose: padrão
- pré-requisitos: tema 5, com o 05-prova.md fechado, a decisão do 5.7 aprovada e os hashes no estado
- grill quer entender: a essência em uma frase e o que o conceito não é, nas suas palavras, gravadas com hash antes de você ver as do redator; e o que você teme que se perca na passagem
- triagem: não roda; ideia nova vai ao banco, e só volta ao 4.9 se puder mudar o resultado (seção 6.11)
- pesquisa: conferir as fichas que uma ligação usa de um jeito novo
- equipe e alternativas: o cir.py monta o CIR a partir do 06-blocos.md, relendo cada origem no commit; um redator por seção, em sessão própria, com só as fontes dela e a esp-* do tema, escreve as ligações; nas seções 1 e 14, o redator vê o CIR montado, e não as suas versões; a condutora mostra as duas lado a lado, e você escolhe, combina ou reescreve; o decompositor quebra cada ligação em afirmações
- validação: o cir.py conferir, o verificador em todas as afirmações e o crítico da equipe; refuta se uma frase não tem origem ou cita um ID que não existe; se um trecho fixo difere da origem; se um número, um escopo ou uma confiança não são os da origem, ou se uma confiança vem sem a base em números; se uma afirmação não é sustentada, exagera ou contradiz um registro; se falta um item da cobertura, o temor da abertura ou o dissenso de um registro; ou se uma seção contradiz outra
- sai: 06-blocos.md, com as ligações e as suas versões; 06-cir.md; 06-conferencia.md; CIR, seções 1 a 17

### 6.2 Pacote de passagem para a Etapa 2
- dose: completa
- pré-requisitos: 6.1, com o CIR montado e nenhuma afirmação pendente
- grill quer entender: o que você não quer que a Etapa 2 perca, e qual a primeira decisão que você espera que ela tome
- triagem: não roda
- pesquisa: conferir as perguntas científicas ainda abertas, com a data da busca; a que já tem resposta sai da lista, com a ficha
- equipe e alternativas: o pacote.py gera o pacote das mesmas fontes do CIR, no commit da montagem em vigor; o redator escreve só o "em vez disso" de cada princípio e de cada restrição, e o verificador o confere
- validação: conselho rápido Passagem (leitor da Etapa 2 sem contexto e guardião do propósito); o leitor ensaia a primeira decisão da Etapa 2 (o que prototiparia primeiro, com que bancada e o que não pode violar) e lista as perguntas centrais sem resposta, cada uma com a probabilidade de proceder, que vai ao placar; o guardião confere que nada desvia do propósito; refuta se a Etapa 2 precisaria perguntar algo central que o pacote não responde; se uma capacidade não aponta para métricas com a linha de base e o limite; se um princípio ou uma restrição vêm sem o "refuta se" ou sem o "em vez disso"; se falta o que reverteria a escolha, com as killer conditions; ou se o pacote escolhe meio ou tecnologia
- sai: 06-pacote-etapa-2.md e pacote.json; as perguntas do conselho ao placar; CIR, seção 15

### 6.3 Estacionamento para a Etapa 3
- dose: leve
- pré-requisitos: 6.1
- grill quer entender: se algo que foi estacionado deveria voltar ao conceito, e por quê
- triagem: não roda; o item estacionado sem motivo volta à sua origem
- pesquisa: conferir os motivos que citam fonte
- equipe e alternativas: o pacote.py etapa3 junta o que o 0.2 e os temas 1 a 5 estacionaram, sem repetição, com todas as origens de cada item, por tipo; as saídas ideais entram como régua do MVP
- validação: conselho rápido (guardião e refutador); refuta se um item não tem motivo ou origem; se algo que muda o resultado do propósito foi estacionado; ou se um item repetido perdeu uma das origens
- sai: 06-estacionamento-etapa-3.md; CIR, seção 16, remontada

### 6.4 Teste de passagem
- dose: completa
- pré-requisitos: 6.2 e 6.3, com o CIR remontado e conferido
- grill quer entender: as perguntas que você prevê que um leitor de fora fará, gravadas com hash antes da rodada; depois, as respostas que só você tem, uma por vez
- triagem: não roda
- pesquisa: conferir a ficha que uma correção cita
- equipe e alternativas: 3 leitores por rodada (engenharia de sistemas, do domínio e um generalista), em sessões novas, no modelo de juiz, só com o CIR e o pacote; cada um reformula primeiro e só depois pergunta, marcando o que deduziu e o que chutou, com a frase; 2 juízes comparam as reformulações com o gabarito tirado do CIR; a condutora classifica cada pergunta com o crítico; cada correção muda a origem e remonta
- validação: os leitores, os juízes e o leitor.py; refuta se um leitor entende errado o propósito, o núcleo, um princípio ou o que o conceito não é; se as reformulações divergem; se sobra uma pergunta central; se uma correção mudou o CIR sem mudar a origem; se uma resposta mudou o propósito, o núcleo, um princípio, uma restrição ou a escolha sem a volta; ou se passou de 3 rodadas sem o seu "sim"
- sai: 06-passagem.md; o CIR e o pacote remontados; os registros das suas respostas; CIR, seções 15 e 17

### 6.5 Critério de pronto e vigia final · validação integrada
- dose: completa
- pré-requisitos: 6.4, sem pergunta central
- grill quer entender: para cada pendência, se você quer voltar ou aceitar com ressalva, com o motivo e o objetivo
- triagem: não roda
- pesquisa: conferir todas as fichas citadas no CIR e no pacote, em fontes/conferencias/C-6.5.md
- equipe e alternativas: o pronto.py confere os 14 itens pela evidência; o pendencias.py lista o que falta; o vigia.py roda no CIR, no pacote e no estacionamento; o crítico da equipe procura o item marcado sem evidência
- validação: o conjunto do tema: a conferência, o pacote, o estacionamento, a passagem e as fontes; refuta se um item passa sem evidência, ou com a evidência de outra coisa; se um "não verificado" foi contado como passa; se uma pendência ficou sem decisão sua; se a vigia acusou algo sem destino; ou se uma ficha que não confere segue sustentando uma frase
- sai: 06-pronto.md; as voltas ou as ressalvas, com registro; C-6.5; CIR, seções 15 e 17

### 6.6 Aprovação e retrospectiva · trava
- dose: trava
- pré-requisitos: 6.5, com cada item passado ou com ressalva sua
- grill quer entender: antes do "sim", se há algo no CIR que você não assinaria; depois do "sim" e antes de ver a retrospectiva, o que você acha que funcionou e o que não funcionou no método, gravado
- triagem: não roda
- pesquisa: não roda
- equipe e alternativas: o retrospectiva.py junta o placar, as previsões gravadas, as doses, as voltas e a taxa de surpresa; o reconstrutor, que não vê os desfechos, reconstrói a expectativa que não foi gravada; a equipe-base escreve o que manter e o que mudar, com dono
- validação: o crítico da equipe; refuta se uma comparação usa expectativa que não foi gravada antes nem reconstruída às cegas; se uma decisão boa com desfecho ruim conta como erro; se uma melhoria não tem dono, skill e seção, ou é genérica; ou se o aprendizado.jsonl recebe conteúdo do projeto ou uma linha de projeto de teste
- trava: antes da retrospectiva; "sim" a "Aprova o CIR ___ (commit ___), com as ressalvas ___?"
- sai: o CIR aprovado, com o commit; o registro da trava; 06-retrospectiva.md; os desfechos no placar; num projeto real, a linha do aprendizado.jsonl, as melhorias e a oferta do espelho de leitura
```

**Critérios do conselho,** escritos antes, um por linha da matriz; o "refuta se" é a falha que derruba:

| Sub-etapa | Critérios |
| --- | --- |
| 6.1 | Cada frase tem origem, e todo ID existe; cada trecho fixo tem o hash da origem; números, escopos e confianças são os da origem, com a base em números; cada ligação foi decomposta, e cada afirmação foi conferida por quem não a escreveu; a cobertura tem todos os itens da lista, o temor da abertura e pelo menos 10 casos canônicos; o dissenso está copiado; a primeira frase de cada seção é a conclusão dela; a sua essência e o seu "o que não é" foram gravados antes dos do redator |
| 6.2 | Cada uma das 9 partes do pacote tem conteúdo ou "nenhum", com o motivo; cada capacidade aponta para métricas com a linha de base e o limite; a bancada tem os caminhos e a nota dos casos nunca vistos; cada fronteira é uma pergunta, sem meio escolhido; cada princípio e cada restrição têm o "refuta se" e o "em vez disso" conferido; o "não reintroduzir" tem o que refutou cada ideia e o desafio guardado; o que reverteria tem as killer conditions e o teste mais barato; o leitor do conselho ensaiou a primeira decisão sem pergunta central |
| 6.3 | Cada item tem a origem e o motivo; os repetidos foram juntados sem perder origem; nada do que muda o resultado do propósito está ali; as saídas ideais estão como régua do MVP, com os caminhos |
| 6.4 | As perguntas previstas foram gravadas antes da rodada; os leitores não viram nada além do CIR e do pacote; cada reformulação foi julgada por 2 juízes contra o gabarito; cada pergunta tem a classificação e quem responde; cada correção mudou a origem e remontou, com registro quando veio de você; nenhuma resposta mudou o rumo sem volta; no máximo 3 rodadas |
| 6.5 | Cada um dos 14 itens tem a evidência que o `pronto.py` conferiu; "não verificado" é falha; cada pendência tem volta ou ressalva sua, com o motivo e o objetivo; a vigia final está limpa, ou cada sinal tem destino; cada ficha citada foi conferida, e a que não confere mudou a origem, com registro, ou virou ressalva |
| 6.6 | A trava tem o "sim", o commit e as ressalvas; cada comparação da retrospectiva usa o que foi gravado antes, ou a reconstrução cega, marcada; os desfechos foram ao placar; cada melhoria tem dono, skill e seção; o `aprendizado.jsonl` só recebe números e notas de método, e só de projeto real |

**Especialidades por sub-etapa,** da tabela do `especialistas.md`:

| Sub-etapa | Especialidades | Por quê |
| --- | --- | --- |
| 6.1 | Escrita técnica e passagem de trabalho; do domínio; a do tema de cada seção, no redator dela | Ligar sem trair a origem, e saber o que cada seção precisa dizer |
| 6.2 | Engenharia de sistemas; do domínio | Ensaiar a primeira decisão da Etapa 2 e ver o que falta para ela |
| 6.3 | Do domínio; economia e incentivos | Separar o que é de mercado do que muda o resultado do propósito |
| 6.4 | Nos leitores: engenharia de sistemas, do domínio e um generalista | Três leituras diferentes, de quem não participou |
| 6.5 | Métodos e verificação | Ver o tique sem evidência |
| 6.6 | Avaliação de programas, no reconstrutor e na equipe | Comparar o esperado com o acontecido sem julgar pelo desfecho |

## 6. Método

Nesta seção, "seção 6.x" é um passo do método, e "o 6.x" é a sub-etapa do fluxograma.

### 6.1 Passagem e abertura (6.1)

1. **Passagem:** a condutora fecha o tema 5, com os hashes do `05-saidas.md` e do `05-prova.md` no estado, descarrega a `cir-prova` e carrega a `cir-sintese`. O `cir.py` confere o hash de cada arquivo de origem contra o estado; se um mudou sem registro, a skill para, e a vigia acusa.
2. **Abertura:** a condutora pergunta o que a Etapa 2 precisa saber e o que você teme que se perca na passagem. A resposta é gravada com hash; o temor vira item da cobertura do `cir.py` (seção 6.5) e pergunta ao conselho Passagem (seção 6.6).
3. **Dose:** a do cartão. A condutora propõe subir o 6.1 para completa quando houve volta no tema 4 ou no 5, porque aí há blocos superados a separar, e o 6.3 para padrão quando o estacionamento passa de 30 itens.
4. **Numeração:** os registros continuam a sequência do `decisoes.md` (no exemplo, de D-051 em diante), e as fichas, a das fontes (de F-094 em diante); as ligações, lig-3.1, lig-3.2…, pela seção e pela ordem; as afirmações, A-001…; as perguntas do 6.4, 6.4-01…, e as suas previstas, 6.4-P1…; os leitores, L1, L2…; os itens do pronto, I1 a I14; as melhorias, 6.6-M1…; e os agentes, RD (redator), DC (decompositor), VR (verificador), JR (juiz das reformulações) e RE (reconstrutor), com o número.

### 6.2 O CIR em construção (temas 1 a 5)

1. **Esqueleto:** o `dossie_init.py` cria o `06-blocos.md` com as 17 seções do `assets/cir-modelo.md`, cada uma com as sub-etapas de origem da seção 4 do fluxograma.
2. **Bloco:** a cada registro, o `registrar.py` grava, na seção do CIR de onde a sub-etapa vem, um bloco por item: o ID, a sub-etapa, o registro, o commit, o tipo, o trecho, o caminho da origem e o hash. O formato é o do `assets/cir-bloco.md` (seção 8.1), e o `registrar.py` só precisa dele, e não da skill.
3. **Trechos fixos:** o que obriga ou promete entra por cópia, entre «», e nenhuma ligação o reescreve: o propósito congelado e as formulações descartadas, com o motivo; os valores e as linhas vermelhas; as métricas, com a linha de base, a fonte e o limite; o RFI; as impossibilidades reformuladas e as fronteiras suspensas; as restrições anti-ideais, com onde moram e o "refuta se"; os princípios invariantes, com o "refuta se"; as capacidades; os cenários; os casos canônicos e as saídas ideais; as falhas reais do pré-mortem e os ataques que procederam; a confiança, o que reverteria e as killer conditions; o seu motivo, nas suas palavras; e o dissenso.
4. **Itens:** o que não obriga nem promete entra pelo ID e pelo rótulo da origem (uma família explorada, uma tangente, uma pergunta aberta), e as ligações podem juntá-los.
5. **Superados:** quando um registro supera outro (no exemplo, D-036 sobre D-025, no critério, e D-041 sobre o 4.13 da 4.5-C), o bloco antigo fica marcado "superado por", com o ID; o corpo do CIR usa o vigente, e o histórico vai à seção 17.
6. **Vigia:** cada bloco passa pela vigia quando é gravado; o que ela acusa fica no bloco e volta à sub-etapa, como em qualquer registro.

### 6.3 Montagem (6.1)

1. **`cir.py montar`:** lê o `06-blocos.md`, relê cada origem no commit do bloco e confere o hash. Se a origem mudou com registro, o bloco ganha a versão nova, e a antiga vai ao histórico; se mudou sem registro, a montagem para, e a vigia acusa.
2. **Ordem de cada seção:** a primeira frase, vazia, para a conclusão; os trechos fixos e os itens, na ordem dos IDs; e, entre eles, os espaços de ligação, marcados.
3. **Famílias que não venceram:** os itens delas (capacidades, cenários, princípios) ficam fora das seções 7 a 10, que são do conceito de referência; vão à seção 6, com o motivo e o desafio guardado, e ao "não reintroduzir sem prova" do pacote.
4. **Como ler:** o topo do CIR diz como lê-lo: os prefixos dos IDs, com a sub-etapa e o arquivo de cada um; «…» é cópia travada, conferida pelo hash; o que está fora das aspas é ligação, conferida afirmação por afirmação; toda confiança vem com a base em números; e os avisos de método, como pede a `especialistas`: as especialidades que rodaram sem `esp-*` e o que pede revisão profissional, em domínio sensível.
5. **Seção 15:** junta as perguntas do 2.5, do 4.12, do 4.13, do 5.6 e do 5.7 e, depois do 6.4, as que ninguém sabe responder, cada uma com quem responde e quando; e, depois do 6.5, as suas ressalvas, com o motivo.
6. **Seção 16:** junta os blocos do estacionamento; depois do 6.3, é remontada a partir do consolidado.
7. **Seção 17:** os registros, por tema, com o dissenso por cópia; o caminho do Entendimento e das checagens de cada sub-etapa, e, por cópia, as checagens que discordaram de você; o histórico dos blocos superados; e a taxa de surpresa do 4.10.
8. **Remontar, nunca reescrever:** toda correção, em qualquer sub-etapa, muda a origem ou a ligação, que também é bloco, e roda o `cir.py montar` de novo; o `06-cir.md` nunca é editado à mão (achado 9).

### 6.4 Ligações (6.1)

1. **Você primeiro:** antes de qualquer redator, o grill pede a sua essência em uma frase e o seu "o que não é"; o `cir.py` grava as duas no `06-blocos.md`, com hash, como "suas versões" (achado 1).
2. **Redator:** um por seção, numa sessão própria, no modelo de trabalho, com só os blocos e as fontes da seção e a `esp-*` do tema dela. Escreve a primeira frase, que é a conclusão da seção, e as ligações entre os trechos, cada uma com os IDs que ela liga. A ordem é a da `doc-coauthoring`: primeiro as seções com mais ligação a fazer (no exemplo, a 3, a 6 e a 11), e as seções 1 e 14, que resumem o resto, por último (achado 10).
3. **Seções 1 e 14:** o redator vê o CIR montado, e não as suas versões, e escreve a essência e o "o que não é". O "o que não é" só aponta para o que o dossiê excluiu (formulações descartadas, famílias refutadas, itens estacionados e fronteiras), com o ID de cada exclusão. A condutora mostra as duas versões, a sua e a do redator, lado a lado; você escolhe, combina ou reescreve. A escolhida passa pelo verificador, venha de quem vier; se a sua tem afirmação sem sustentação, a condutora mostra, e você decide, com registro.
4. **O que o redator não faz:** não reescreve trecho fixo, não resume dissenso, não arredonda número, não troca o passado de um caso pelo presente genérico e não cita meio nem tecnologia. O que precisaria disso é pergunta à condutora, e não ligação.
5. **Decompositor:** um por seção, numa sessão própria, quebra cada ligação em afirmações atômicas, cada uma com as origens que a ligação cita (achado 5).

### 6.5 Conferência (6.1, e em cada remontagem)

1. **`cir.py conferir`** acusa: (a) frase sem origem, ou com ID que não existe (achado 11); (b) trecho fixo com hash diferente do da origem; (c) número que não está na origem, ou que difere dela; (d) confiança ou palavra de probabilidade sem a base em números ao lado (achado 14); (e) generalização, pela lista do `assets/generalizacao.txt`: "sempre", "todas", "nunca" e "garante", o presente genérico no lugar do passado de um caso e o qualificador da origem que sumiu (achado 7); (f) cobertura, contra a lista que sai dos registros: cada métrica, restrição, princípio, capacidade, cenário, caso canônico, falha real, ataque que procedeu, alternativa viva, killer condition, dissenso e pergunta aberta, mais o temor da abertura e pelo menos 10 casos canônicos (achado 6); (g) a distribuição das afirmações por tema, que vai ao crítico, sem limite fixo até haver linha de base; (h) a vigia, frase por frase.
2. **Verificador:** no modelo de juiz, em lotes de até 20 afirmações de seções diferentes, em ordem sorteada; vê só a afirmação e os trechos das fontes que ela cita; e dá um de quatro vereditos: sustentada, não sustentada, exagerada ou contradiz. Todas as afirmações das ligações são conferidas, e não uma amostra; os trechos fixos, pelo hash (achados 5, 6 e 17).
3. **Crítico da equipe:** lê o CIR montado e a conferência, e procura contradição entre seções, distribuição torta, conclusão de seção sem apoio nela e os pensamentos da seção 7.
4. **Destinos:** a afirmação não sustentada ou exagerada volta ao redator, que reescreve a ligação, e passa de novo pelo verificador; a que contradiz um registro sai, e a condutora mostra o conflito a você; o item que falta volta à montagem; e, se a falta é da origem (um registro sem um campo), vira pendência do 6.5.

### 6.6 Pacote da Etapa 2 (6.2)

1. **`pacote.py etapa2`:** gera o pacote das mesmas fontes do CIR, no commit da montagem em vigor, e não a partir do CIR (achado 9); cada remontagem gera o pacote de novo. O que se precisa entender vai no texto; o que se confere vai no ID e no caminho, sem repetir o que já está num arquivo (`handoff`).
2. **As 9 partes,** na ordem da tabela abaixo; parte sem conteúdo diz "nenhuma", com o motivo.
3. **"Em vez disso":** é a única parte escrita, pelo redator, e conferida pelo verificador. Para cada princípio e cada restrição, diz o comportamento esperado ao lado da proibição, porque a proibição sozinha puxa o que proíbe (`writing-for-agents`).
4. **Completo:** o pacote está completo quando nenhuma lacuna bloqueia a primeira decisão da Etapa 2 (`create-prd`). O que não se sabe vai à parte 5 ou à seção 15, marcado, e não vira suposição.
5. **Conselho rápido Passagem:** o leitor da Etapa 2, sem contexto, ensaia a primeira decisão (o que prototiparia primeiro, com que bancada e o que não pode violar) e lista as perguntas centrais sem resposta, cada uma com a probabilidade de proceder, que vai ao placar; o desfecho sai da correção: procede se o pacote precisou mudar, e não procede se a resposta já estava lá. O guardião confere se algo no pacote desvia do propósito.
6. **Pesquisa:** confere as perguntas científicas abertas, com a data; a que já tem resposta sai da lista, com a ficha.

| Parte | O que traz | De onde |
| --- | --- | --- |
| 1. O que fazer primeiro | De 3 a 5 ações, cada uma com o ID que a pede; é a lista de ações do I-PASS (achado 2) | O que reverteria, as perguntas abertas e as fronteiras |
| 2. Capacidades e métricas | Cada capacidade do conceito de referência, com as métricas que ela move, a linha de base e o limite ideal | 4.13 e 4.15; tema 3 |
| 3. A bancada | Os casos canônicos e as saídas ideais, com os caminhos em `casos/` e no `05-saidas.md`, e a nota de que a bancada precisa também de casos que ninguém viu | 2.6, 3.6, 5.1 e 5.2 |
| 4. As fronteiras | Cada uma como pergunta, com o que tem de respeitar; nenhuma resposta escolhida | `fronteiras.md` |
| 5. Perguntas científicas abertas | Cada uma com a data da última busca e quem pode responder | 2.5, 4.12, 4.13, 5.6 e 5.7; a pesquisa do 6.2 |
| 6. Princípios e restrições | Os princípios invariantes e as restrições anti-ideais, com o "refuta se", onde moram e o "em vez disso" | 4.9 e 4.15; o redator, só no "em vez disso" |
| 7. Alternativas vivas | As vivas, com o que a prova mostrou de cada uma, ou "nenhuma", com o motivo | 5.7 |
| 8. Não reintroduzir sem prova | Cada ideia refutada ou excluída, com o que a refutou e o desafio guardado, para não ser desfeita sem saber (achado 12) | 5.4, 5.7, 4.9 e o tema 1 |
| 9. O que reverteria a escolha | As condições, com as killer conditions e o teste mais barato de cada uma; é o plano de contingência da Etapa 2 | 5.7; a vigia |

### 6.7 Estacionamento da Etapa 3 (6.3)

1. **`pacote.py etapa3`:** junta o que o 0.2 e os temas 1 a 5 estacionaram, sem repetição; o item que aparece em mais de um tema fica uma vez, com todas as origens.
2. **Por tipo:** ideias de apelo; necessidades vizinhas; mercado, preço e canal; e as falhas de mercado do pré-mortem.
3. **Motivo:** cada item traz o motivo da exclusão, copiado da origem; o que não tem motivo volta à origem, e não entra.
4. **Régua do MVP:** as saídas ideais dos casos canônicos entram como a régua com que a Etapa 3 vai medir quanto do ideal o MVP entrega.
5. **Conselho rápido (guardião e refutador):** o guardião procura o que muda o resultado do propósito e foi estacionado; se acha, é volta ao 4.9, por decisão sua; o refutador procura motivo fraco e origem perdida na junção.

### 6.8 Teste de passagem (6.4)

1. **Previsão:** antes da rodada, o grill pede as perguntas que você prevê que um leitor de fora fará; o `leitor.py` grava com hash, e elas não vão a nenhum leitor (achado 3).
2. **Leitores:** 3 por rodada, em sessões novas, no modelo de juiz, cada um com uma especialidade (engenharia de sistemas, do domínio e um generalista). Recebem só o CIR e o pacote, com o hash, e a tarefa: "você começa a Etapa 2 amanhã, sem poder falar com ninguém do projeto". A condutora não explica nada (achado 1).
3. **Reformular primeiro:** cada leitor escreve, com as próprias palavras, o propósito, o núcleo e os princípios, o que o conceito não é, a primeira tarefa da Etapa 2 e a bancada (achado 2).
4. **Perguntar depois:** só então, as perguntas que faria a quem escreveu e, para cada resposta que deu a si mesmo, se deduziu ou chutou, com a frase em que se apoiou; marca as perguntas cuja resposta mudaria o que faria primeiro (achado 4).
5. **Juízes das reformulações:** 2, no modelo de juiz, comparam cada reformulação com o gabarito tirado do próprio CIR (o propósito, os princípios, a seção 14 e a parte 1 do pacote): bate, diverge ou incompleta; se os juízes discordam, conta "diverge". O `leitor.py` marca ambiguidade onde duas reformulações divergem entre si, mesmo que cada uma bata em parte com o gabarito.
6. **Classificação:** a condutora, com o crítico, classifica cada pergunta: central, se a resposta mudaria a primeira decisão da Etapa 2 ou o entendimento do propósito, do núcleo ou de um princípio, ou secundária; e quem responde: o dossiê, só você, ou ninguém sabe.
7. **Correção:** se o dossiê responde, a resposta entra na origem, como bloco novo ou ligação, e o CIR é remontado; se só você responde, o grill pergunta, e a resposta vira registro e, depois, bloco; se ninguém sabe, vai à seção 15, com quem responde e quando. O leitor nunca preenche a lacuna: ele mostra onde ela está.
8. **Volta disfarçada:** uma resposta que muda o propósito, o núcleo, um princípio, uma restrição ou a escolha é volta (seção 6.11), e não esclarecimento. A definição de um termo de um "refuta se" que o tema 5 já usou passa pelo `cir.py usos`, que lista os blocos, os casos e os vereditos que dependem dele; se algum mudaria, é volta 6→5 só para eles.
9. **Parada:** abre outra rodada, com 3 leitores novos, se sobrou pergunta central ou se uma reformulação divergiu; para quando não há pergunta central e as 3 reformulações batem. No máximo 3 rodadas; a quarta, só com o seu "sim" (`discovery-agents-handoff`).
10. **Previsto × real:** o `leitor.py` compara as suas previstas com as reais (quantas apareceram e quantas centrais você não previu) e grava no `06-passagem.md`, para a retrospectiva e o `aprendizado.jsonl`.

### 6.9 Critério de pronto (6.5)

1. **`pronto.py`:** aplica o `assets/pronto.yaml`, que diz a evidência de cada item (tabela abaixo). O estado é passa, falha ou não verificado, e "não verificado" conta como falha (achado 13).
2. **Pendências:** o `pendencias.py` da condutora lista o que falta e o que ficou como "pulado e risco".
3. **De novo, e não lembrado:** a vigia roda no CIR, no pacote e no estacionamento inteiros; a pesquisa confere todas as fichas citadas, em `fontes/conferencias/C-6.5.md`. A ficha que não confere muda a origem, com registro, pela skill dona (seção 6.11), ou vira ressalva sua.
4. **Pendente:** para cada item que falha, a condutora mostra a origem, o que falta e o custo da volta; você decide voltar ou aceitar com ressalva, com o motivo e o objetivo. A ressalva vai ao registro, à seção 15 e à pergunta da trava.
5. **Crítico:** procura o item marcado sem evidência, ou com a evidência de outra coisa.

**Evidência que o `pronto.py` pede, item por item,** do critério de pronto do v2:

| Item | Evidência |
| --- | --- |
| I1 · Propósito único, sem produto nem tecnologia, com as descartadas, congelado | `01-proposito.md`, com o hash igual ao do estado; congelado no 1.7; as formulações descartadas, com o motivo; a vigia limpa; o mesmo texto na seção 2 do CIR |
| I2 · Métricas com linha de base e limite, com custo de uso e dano | Cada métrica com a linha de base, a fonte e o limite; pelo menos uma de custo de uso (no exemplo, M4, M5, M10 e M13) e uma de dano (M3, M6, M7 e M9) |
| I3 · RFI aprovado no teste do impossível | O registro do teste do impossível e o RFI, na seção 4 do CIR |
| I4 · 3 famílias realmente diferentes | 3 famílias ou mais, do 4.5 e do 4.11, com a checagem de distância da `cir-divergencia` |
| I5 · Tangentes, com a taxa de surpresa | As tangentes no banco, com o tipo; a taxa do 4.10 no estado e na seção 17 |
| I6 · Esboço integrado | `04-esboco.md`, com os conflitos, as sinergias e as dependências |
| I7 · Tudo classificado, e experiência como função | Cada elemento do banco e do esboço com um dos cinco tipos, no `04-triagem.md`, inclusive os que entraram no banco depois do 4.9; nenhuma tela no CIR, pela vigia |
| I8 · Restrições e estacionamento com motivo | Cada restrição com a origem, onde mora e o "refuta se"; cada item do estacionamento com a origem e o motivo |
| I9 · Capacidades sem tecnologia, com o núcleo | As capacidades e o núcleo, do 4.13 ao 4.15, com a vigia limpa |
| I10 · 3 cenários | 3 cenários ou mais, do 4.14 |
| I11 · 10 casos canônicos com a saída ideal | 10 casos ou mais, com os caminhos e os hashes das saídas |
| I12 · Pré-mortem e red team | As seções do `05-prova.md`, com os registros |
| I13 · Decisões com confiança | Todo registro com o campo Confiança preenchido |
| I14 · Pacote da Etapa 2 pronto | O pacote existe; o conselho Passagem do 6.2 está gravado; o 6.4 fechou com zero centrais; os hashes do pacote batem com o commit do CIR |

### 6.10 Aprovação e retrospectiva (6.6)

1. **Trava:** a condutora mostra o resumo (o commit do CIR, os 14 itens, as ressalvas, as perguntas abertas da seção 15 e o que reverteria) e pergunta: "Aprova o CIR  ***(commit*** ), com as ressalvas ___?". Só "sim" aprova. O registro leva a data, o commit e as ressalvas, e a trava fica em "travas", no estado. A retrospectiva vem depois do "sim", porque mede o projeto fechado, e não muda o CIR.
2. **Você primeiro:** depois do "sim" e antes da retrospectiva, o grill pergunta o que você acha que funcionou e o que não funcionou no método, e grava.
3. **`retrospectiva.py`** junta: o placar, com os desfechos que o projeto conhece (os conceitos que resistiram e os que caíram no 5.7, os controles do 5.1 e as perguntas do 6.2) e a pontuação de Brier, pelo `placar.py` do conselho; as suas previsões gravadas (a escolha antes do quadro do 5.7, a falha temida do 5.3, as decisões dos reservados do 5.2 e as perguntas previstas do 6.4), como a sua calibração, ao lado da do conselho; a dose planejada e a usada, por sub-etapa; as voltas, com o tipo e o lugar onde nasceu a falta; e a taxa de surpresa final, as tangentes com função no CIR aprovado sobre as classificadas, ao lado da do 4.10.
4. **Expectativa sem registro:** o reconstrutor, numa sessão própria, recebe só o cartão e o que se sabia antes, sem os desfechos, e reconstrói o que se esperava; a reconstrução vai marcada, e nunca no lugar de uma previsão gravada (`think-after-action-review`; achado 16).
5. **Decisão × desfecho:** cada comparação separa a qualidade da decisão, com o que se sabia, do desfecho; uma decisão boa com desfecho ruim não é erro, e uma ruim com desfecho bom não é acerto (achado 16).
6. **Manter e mudar:** a equipe-base escreve o que manter e o que mudar, nos dois sentidos (o que foi melhor que o esperado também conta), sem culpa; cada mudança é específica, com dono, a skill e a seção do plano dela, e vai ao `06-retrospectiva.md` e ao `aprendizado/melhorias.md`. Você decide se e quando mudar uma skill, fora do projeto (achado 15).
7. **`aprendizado.jsonl`:** só num projeto real, uma linha no repositório das skills, com números e notas de método: a fração de tangentes usada no 4.4, a taxa do 4.10 e a final, o número de tangentes, as doses, as rodadas do 6.4, o acerto das perguntas previstas e as voltas por tipo; nunca o conteúdo do projeto. Projeto de teste não grava. No 4.4 do projeto seguinte, a condutora mostra a mediana de cada número, com o n; com menos de 3 projetos, mostra os valores e pergunta. É a resposta ao ponto em aberto da [Plano detalhado — cir-divergencia](https://app.notion.com/p/Plano-detalhado-cir-divergencia-aa452eebec8044cb9c016a345ce0f1ff?pvs=21) sobre a taxa de surpresa entre projetos.
8. **Espelho de leitura:** só num projeto real, depois do "sim", a condutora oferece uma página no Notion com o CIR aprovado, gerada do commit, só de leitura e com o link para ele; nunca o CIR em construção, pelo risco de isolamento da seção 14 da condutora. É a resposta ao ponto em aberto da [Plano detalhado — etapa-1-cir (condutora)](https://app.notion.com/p/Plano-detalhado-etapa-1-cir-condutora-fccda0c36a5d403582b433a6f2b0657f?pvs=21) sobre o espelho de leitura.

### 6.11 Voltas

| Volta | Quando | O que leva | Quem executa |
| --- | --- | --- | --- |
| 6 → 1 | Uma resposta sua, ou a passagem, mostra que o propósito precisa dizer outra coisa | O que mostrou; o propósito é congelado de novo no 1.7, e tudo o que dependia dele é revisto | `cir-proposito`, só com a sua decisão |
| 6 → 2 ou 3 | Uma ficha que sustenta o mapa ou uma métrica não confere, ou falta uma linha de base | A ficha nova e a linha em questão; só ela muda | `cir-mapa` ou `cir-idealidade` |
| 6 → 4.9 | Um elemento do banco ou do esboço está sem tipo; algo que muda o resultado foi estacionado; ou uma ideia nova do tema 6 pode mudar o resultado | Os elementos, com a origem | `cir-arquitetura` |
| 6 → 4.12 a 4.15 | Uma resposta sua muda o núcleo, um princípio ou uma capacidade | O que muda e por quê; a prova refaz o que dependia | `cir-arquitetura`, e depois a `cir-prova` |
| 6 → 5 | A definição de um termo muda um veredito, ou uma ficha que sustenta a escolha foi retratada | Só os vereditos que dependem, ou a decisão do 5.7 | `cir-prova` |
| 6.x → 6.1 | Qualquer correção dentro do tema 6 | A origem corrigida; o CIR é remontado e conferido | Esta skill |

**Em toda volta,** o CIR e o pacote são remontados e conferidos; o 6.4 roda de novo, com leitores novos, se a volta mudou o propósito, o núcleo, um princípio, uma restrição, a escolha ou o pacote, e, se só mudou um número sem mudar decisão, o estacionamento, o histórico ou uma ficha, bastam a remontagem e a conferência; cada volta tem o seu registro; e o mesmo tipo de volta não se repete sem o seu "sim".

### 6.12 Auditoria, modo avulso e reuso

- **Auditoria, no tema 0:** o `pronto.py --auditoria` transforma cada item em pergunta, com o lugar do documento como evidência, e marca "lacuna" onde não acha; a vigia roda no documento inteiro; o `cir.py conferir --sem-dossie` lista os números e as garantias sem fonte. O resultado entra no `00-auditoria.md` da condutora, e as lacunas viram o plano do projeto.
- **Avulso:** em `sintese/<data>-<assunto>/`, com a auditoria e o teste de passagem (seção 3). Sem registros, não há montagem nem correção pela origem: a skill aponta a lacuna, e quem trouxe o documento decide.
- **Reuso:** na Etapa 2 e na Etapa 3, o mesmo método monta e testa a passagem de cada uma; o cartão muda, e o critério de pronto é o da etapa.

## 7. Regras que valem o tempo todo

1. **O CIR é montado, e não escrito.** O `cir.py` monta a partir dos blocos; o redator só escreve as ligações; o `06-cir.md` nunca é editado à mão (achados 5 e 9).
2. **Toda frase tem origem, à vista.** O trecho fixo vai entre «», com o hash; a ligação, com os IDs que liga; frase sem origem não entra (achado 11).
3. **O número, o escopo e a confiança são os da origem.** Nada se arredonda nem se generaliza, e toda confiança vem com a base em números, entre parênteses, no próprio texto (achados 7 e 14).
4. **Quem escreve não confere.** O verificador, os leitores e os juízes são outros, em sessões novas, no modelo de juiz (achados 1 e 17).
5. **O dissenso é copiado, e não resumido.** Vai inteiro à seção 17, com quem discordou, de quê e por quê (achado 8).
6. **Corrigir é mudar a origem e remontar.** Nunca se corrige o CIR por cima, nem se faz o pacote a partir do CIR (achado 9).
7. **Você primeiro.** A sua essência, o seu "o que não é", o seu temor, as suas perguntas previstas e a sua avaliação do método são gravados antes de você ver os dos agentes (achados 1 e 3).
8. **O leitor mostra a lacuna, e não a preenche.** Quem responde é o dossiê ou você; se ninguém sabe, a seção 15 diz, com quem pode responder.
9. **Resposta que muda o rumo é volta.** O que muda o propósito, o núcleo, um princípio, uma restrição ou a escolha passa pela skill dona, e não entra como esclarecimento.
10. **Pronto é evidência.** Cada item tem o arquivo, a seção, o ID e o hash; sem evidência, é "não verificado", que conta como falha (achado 13).
11. **Pendência fecha ou vira ressalva sua,** com o motivo e o objetivo nas suas palavras, no registro, na seção 15 e na pergunta da trava.
12. **Sem tecnologia, sem mercado e sem produto.** O meio vai a `fronteiras.md`, e o mercado, ao estacionamento; a vigia acusa.
13. **A retrospectiva compara com o que foi gravado antes,** e separa a decisão do desfecho (achados 15 e 16).
14. **Os números saem dos scripts:** as contagens, os hashes, a cobertura, a distribuição, os estados do pronto, a taxa de surpresa e o acerto das previsões, e nunca de estimativa do modelo.

**Pensamentos que pedem parada:**

| Pensamento | Realidade |
| --- | --- |
| "Vou reescrever este trecho para ficar mais fluido" | Trecho fixo não se reescreve; a fluidez é das ligações, e o texto reescrito deriva (achado 9) |
| "'Quase todas' é praticamente 'todas'" | O qualificador é da origem, e o `cir.py` acusa a generalização (achado 7) |
| "Resumo o dissenso numa linha" | O dissenso vai por cópia; resumir apaga vozes (achado 8) |
| "Eu escrevi; está claro" | Quem escreve superestima o quanto foi entendido; quem diz são os leitores (achado 1) |
| "Respondo esta pergunta do leitor pelo Luan; é óbvio" | Só você responde o que só você sabe, com registro; o óbvio para quem escreveu é a maldição do conhecimento (achado 1) |
| "Os três leitores disseram que entenderam" | Conta a reformulação, julgada contra o gabarito, e não o "entendi" (achados 2 e 4) |
| "É só um esclarecimento" | Se muda o propósito, o núcleo, um princípio, uma restrição ou a escolha, é volta; o `cir.py usos` mostra o que depende |
| "Todos os itens estão marcados" | Marcado não é feito; o `pronto.py` pede a evidência de cada um (achado 13) |
| "A vigia já rodou no tema 4" | Roda de novo no 6.5, no CIR, no pacote e no estacionamento inteiros |
| "A pendência é pequena; a Etapa 2 resolve" | A pendência fecha com uma volta ou vira ressalva sua, com o motivo, na pergunta da trava |
| "Deu errado; foi erro nosso" | Uma decisão boa com desfecho ruim não é erro; compara-se com o que se sabia (achado 16) |
| "A gente lembra o que esperava" | Lembrar depois do desfecho é viés de retrospectiva; vale o que foi gravado, ou a reconstrução cega, marcada (achado 16) |
| "Melhorar a comunicação entre as skills" | Melhoria sem dono, skill e seção não muda nada (achado 15) |
| "Cito a tecnologia para ajudar a Etapa 2" | O meio é pergunta, em `fronteiras.md`; escolher é da Etapa 2 |
| "Copio o texto do teste de leitor da `doc-coauthoring`" | A licença não está declarada: entra só a ideia, citada |

## 8. Formatos e modelos de documento

O exemplo corre pelo mesmo caso dos planos anteriores: o transporte escolar na zona rural, com o propósito "Que as crianças da zona rural cheguem à escola todo dia, a tempo e em segurança" (D-011). O tema 5 fechou na D-050: o conceito de referência é a 4.5-C (separar quem viaja pela distância, no tempo ou em veículos), sem alternativa viva e com confiança média. Os registros desta skill começam em D-051, e as fichas, em F-094. O CIR passa por quatro montagens: a 1 (commit 52be9d3), a primeira conferida; a 2 (a8d4e10), que gera o pacote e o estacionamento e vai à rodada 1 do teste de passagem; a 3 (c41f7b2), corrigida pela rodada 1, que vai à rodada 2 e ao pronto; e a 4 (7f21c0a), depois das voltas do pronto, que é a aprovada.

### 8.1 Bloco, ligação e as suas versões, no `06-blocos.md`

O bloco da 4.9-R3 foi gravado pelo `registrar.py` quando a D-035 fechou o 4.9; a ligação, pelo redator da seção 9, no 6.1; as suas versões, pelo grill, antes de qualquer redator.

```markdown
# CIR em construção · transporte escolar rural · 06-blocos.md
## 9. Restrições anti-ideais · origens: 1.5 e 4.9
### 4.9-R3 · restrição anti-ideal · 4.9 · D-035 · commit 3c9a1f0
- tipo: trecho fixo
- trecho: «O conceito não faz a criança pequena sair de casa antes das 6h, mesmo que isso encurte a rota»
- onde mora: «a ordem das ondas e a hora dos pontos»
- refuta se: «com a escola a 40 km, a primeira criança pequena sai antes das 6h»
- de onde vem: 4.7-C1, o conflito entre 4.6-01 e V4
- origem: 04-triagem.md#4.9-R3 · hash 5e1b…
- vigia: limpa
### lig-9.1 · redator RD-09 · montagem 1 · liga 4.9-R1, 4.9-R2, 4.9-R3, 4.9-R4, V2, V3, V4 e M7
- texto: Cada restrição impede que o conceito fira um valor ou aumente um dano: 4.9-R1 protege V2; 4.9-R2, M7; 4.9-R3, V4; e 4.9-R4, V3.
- afirmações, pelo decompositor DC-09: A-041 "4.9-R1 protege V2" · A-042 "4.9-R2 protege M7" · A-043 "4.9-R3 protege V4" · A-044 "4.9-R4 protege V3"
- vereditos: as quatro sustentadas (verificador VR-03)
## Suas versões · 6.1 · gravadas antes de qualquer redator
- abertura (hash 0c3e…): a Etapa 2 precisa saber "que a ordem das ondas muda quando a estrada fecha"; você teme que se perca "a criança pequena" → item da cobertura e pergunta ao conselho Passagem
- essência (hash 2b7d…): "Cada criança viaja só o seu pedaço do caminho e sempre chega a tempo"
- o que não é (hash 2b7d…): "não é um app que mostra onde está o ônibus, nem a guarda dos pontos pelas famílias"
```

### 8.2 O CIR montado, no `06-cir.md`

Trechos da montagem 4, a aprovada. A essência saiu da comparação lado a lado, que fica na seção 17.

```markdown
# CIR · transporte escolar rural · montagem 4 · commit 7f21c0a · gerado pelo cir.py; não editar
## Como ler
- «…» é cópia da origem, travada pelo hash; o que está fora das aspas é ligação, conferida afirmação por afirmação no 06-conferencia.md
- cada frase termina com a origem: D- registro (decisoes.md) · F- ficha (fontes/) · P e V, propósito e valores (01-proposito.md) · M métrica (03-idealidade.md) · 2.6- caso (casos/) · B- banco e 4.x- tema 4 (04-*.md) · 5.x- prova (05-prova.md) · lig- ligação (06-blocos.md)
- toda confiança vem com a base em números ao lado
- avisos de método: nenhuma especialidade rodou sem esp-*; nada aqui pede revisão profissional
## 1. Essência em uma frase
Cada criança da zona rural viaja só o trecho da sua distância, numa onda com hora certa, e nunca espera sem um adulto que responde por ela. (lig-1.1 · 4.15-I4, 4.15-I5, 4.13-11, P1 · D-051)
## 9. Restrições anti-ideais
Cada restrição impede que o conceito fira um valor ou aumente um dano: 4.9-R1 protege V2; 4.9-R2, M7; 4.9-R3, V4; e 4.9-R4, V3. (lig-9.1)
- 4.9-R3 · «O conceito não faz a criança pequena sair de casa antes das 6h, mesmo que isso encurte a rota» · onde mora: «a ordem das ondas e a hora dos pontos» · refuta se: «com a escola a 40 km, a primeira criança pequena sai antes das 6h» · criança pequena, aqui e em V4: até os 8 anos (D-054) · D-035 · 04-triagem.md · 5e1b…
## 11. Diferenciais, como hipóteses com confiança
- A 4.5-C supera a de hoje na chegada a tempo, na chuva (M1), e nas faltas causadas pelo transporte (M2): «R1: M1 8–1, M2 7–2» · confiança «média», pelo decisao.py: falta uma condição, o R5 válido sem os espelhos (com eles, 5 de 8; sem eles, fraco, 2 de 5) · «nenhuma criança sem adulto (V1) em 35 casos → até cerca de 1 em 12 casos parecidos ainda pode ter» · D-050 · 05-prova.md
## 14. O que este conceito não é
Não é um jeito de ver onde está o ônibus (B-001 e 4.8-06, estacionada como apelo); não é a guarda dos pontos pelas famílias, em rodízio (4.5-B, refutada na D-050, por M13); não é a aula levada até a criança (4.5-A, refutada pelo 5.4-07); e não é gastar menos pelo município (P4, descartada na D-005). (lig-14.1 · D-051)
## 17. Registro de decisões e taxa de surpresa
- D-050 · 5.7 · a 4.5-C, sem vivas · motivo, nas suas palavras: «eu queria a 4.5-B, mas três horas a mais por mês, todo mês, é o que faz a família desistir; fico com a que não pede isso» · dissenso: «o explorador defende a 4.5-B como a de mais salto, refutada só pela D-036; o refutador de método lembra que o R5 da 4.5-C só ficou válido com os espelhos»
- D-051 · 6.1 · essência, lado a lado: a sua, "Cada criança viaja só o seu pedaço do caminho e sempre chega a tempo" (o cir.py acusou "sempre", e o verificador a deu como exagerada: a origem é «M1 8–1», e o limite de 100% não foi atingido; e ela não diz o adulto da 4.15-I5) · a do redator RD-01, "Na 4.5-C, as crianças viajam em ondas pela distância, e nenhuma espera sem um adulto que responde por ela" (sustentada; diz o nome da família, e não o que muda para a criança) · a combinada, por você, acima, sustentada; o "nunca" que o cir.py acusou é o «nenhuma» do princípio, e não a generalização de um caso
- taxa de surpresa do 4.10: «3 de 36 = 8,3%» (B-044, B-051 e B-058)
```

### 8.3 A conferência da montagem 1, no `06-conferencia.md`

```markdown
# Conferência · 6.1 · CIR montagem 1 · commit 52be9d3
## cir.py conferir
- a · frase sem origem: 0
- b · trecho fixo com hash diferente: 0
- c · número fora da origem: 1 · seção 6: "as famílias dariam 4 horas a mais por mês à guarda" · a origem diz «cerca de 3 h a mais por mês por família»
- d · confiança sem base: 1 · seção 11: "confiança média", sem as condições do decisao.py ao lado
- e · generalização: 2 · seção 10: "as ondas garantem a chegada a tempo" (a origem é «M1 8–1») · seção 4: "a rota dividida chega a 90%" (sumiu o qualificador «a rota 3, depois de dividida»)
- f · cobertura: falta 1 · a falha real 5.3-05: o registro do 5.3 a traz, e o 06-blocos.md não tem o bloco
- g · distribuição das afirmações: tema 1, 9% · tema 2, 6% · tema 3, 14% · tema 4, 30% · tema 5, 41% → ao crítico
- h · vigia: 1 · seção 6: "a 4.5-B foi descartada por ser cara" · sinal de mercado
## Verificador · 96 afirmações · 5 lotes, de VR-01 a VR-05 · ordem sorteada
- A-017 "a 4.5-B foi refutada só pela versão do critério que decide (D-036), por M13" · D-050 e 05-prova.md · sustentada
- A-018 "a 4.5-B piorou M13 em todos os casos de trabalho" · a origem diz «− em 11 de 18» · exagerada
- totais: 88 sustentadas · 5 exageradas · 1 não sustentada · 2 contradizem ("a 4.5-B foi descartada por ser cara", contra o motivo da D-050; "a 4.5-C venceu sem dissenso", contra o dissenso da D-050)
## Crítico
- a conclusão da seção 6 diz que a 4.5-C venceu sem dissenso, e a seção 17 copia o dissenso da D-050: contradição entre seções
- o tema 5 tem 41% das afirmações, e o tema 2, 6%: a conclusão da seção 3 não se apoia nos casos do 2.6
## Destinos
- c, d, e, as 5 exageradas e a não sustentada → redatores das seções 3, 4, 6, 10 e 11; verificador de novo, só nas afirmações novas
- as 2 que contradizem → saem; a condutora mostra o conflito, e você confirma o motivo e o dissenso da D-050, que ficam por cópia
- f → pendência à origem: o registrar.py grava o bloco da 5.3-05 a partir do registro do 5.3
- montagem 2 · commit a8d4e10 · conferir limpo · 19 afirmações novas, todas sustentadas
```

### 8.4 O pacote da Etapa 2, no `06-pacote-etapa-2.md`

Trechos da versão da montagem 4. O `pacote.json` tem as mesmas partes, com os IDs e os caminhos.

```markdown
# Pacote da Etapa 2 · transporte escolar rural · pacote.py etapa2 · das fontes, no commit 7f21c0a
## 1. O que fazer primeiro
1. Prototipar a ordem das ondas da ponta norte e conferi-la contra 4.9-R3 no 2.6-12 (leitura dividida no 5.1) e nos 5.6-08 a 5.6-11 (a estrada fecha às 5h50) · pedem: 4.9-R3, 5.3-01 e a primeira killer da D-050
2. Responder como se registra a chegada de cada onda, e não só a da primeira · pedem: 5.3-02 e a seção 15
3. Decidir, com a bancada, se uma onda é outra viagem do mesmo veículo ou outro veículo · pede: 6.4-01
4. Medir quantas crianças cabem numa onda · pede: 6.4-03
## 2. Capacidades e métricas
- 4.13-11 · levar cada criança só o trecho da sua distância, numa onda com hora certa · M1 (60% hoje, F-039 · limite 100%), M4 e M8
- 4.13-12 · um adulto que responde pelas crianças que esperam a sua onda (D-041) · M3
- 4.13-13 · a passagem anterior avisa a seguinte quando atrasa · M1 e M11
## 3. A bancada
- os 12 casos canônicos da seção 12, com as saídas ideais: casos/ e 05-saidas.md, com os hashes
- os 5.6-08 a 5.6-11 nunca foram vistos por quem escreveu o conceito; mesmo assim, a bancada precisa de casos que ninguém do projeto viu: a Etapa 2 guarda os dela, fechados, antes de prototipar
## 4. As fronteiras
- que meio faz a passagem anterior avisar a seguinte, respeitando 4.9-R1? (4.13)
- onde ficam os pontos, respeitando 4.9-R3? (4.13)
- como o segundo veículo sabe que a primeira onda atrasou onde não há sinal de celular? (5.3-11)
- como a lista de quem embarcou chega à escola num dia sem sinal? (5.4-12)
## 6. Princípios e restrições
- 4.9-R3 · «O conceito não faz a criança pequena sair de casa antes das 6h, mesmo que isso encurte a rota» · criança pequena: até os 8 anos (D-054) · onde mora: «a ordem das ondas e a hora dos pontos» · refuta se: «com a escola a 40 km, a primeira criança pequena sai antes das 6h» · em vez disso: a ordem das ondas e a hora dos pontos se ajustam para que a primeira criança pequena saia às 6h ou depois, mesmo que a rota fique mais longa
- 4.15-I5 · «nenhuma criança espera a sua onda sem um adulto que responde por ela» · … · em vez disso: a criança só sai para esperar a onda quando há, no ponto, um adulto que responde por ela, da chegada ao embarque
## 7. Alternativas vivas
nenhuma: a D-050 escolheu a 4.5-C sem vivas
## 8. Não reintroduzir sem prova
- 4.5-B · a guarda nos pontos pelas famílias, em rodízio · refutada pela D-036, por M13 (cerca de 3 h a mais por mês por família) · desafio: "como poderíamos ter um adulto que responde pela criança em cada ponto de espera sem que as famílias deem mais horas por mês?"
- 4.5-A · levar a aula até a criança · refutada pelo 5.4-07 (4.9-R4) · desafio: "como poderíamos levar a aula até a criança sem que declarar o caminho fechado dê vantagem a quem declara?"
## 9. O que reverteria a escolha
- uma criança pequena sair antes das 6h quando a estrada fecha cedo · killer · teste mais barato: a ordem das ondas nos 5.6-08 a 5.6-11, no papel, antes de qualquer protótipo em campo
- um ponto sem adulto na segunda viagem · killer · teste mais barato: contar, nos 12 casos, os pontos da segunda viagem e quem responde em cada um
- a chegada registrada ser só a da primeira onda · irmãos em ondas diferentes sem adulto para o menor (5.3-05) · as outras condições do quadro, com o teste de cada uma
```

### 8.5 O estacionamento da Etapa 3, no `06-estacionamento-etapa-3.md`

Trechos da versão final, com 19 itens; no 6.3, eram 17, e o B-206 e o B-207 entraram pela volta do pronto (seção 8.7).

```markdown
# Estacionamento da Etapa 3 · pacote.py etapa3 · do 0.2 e dos temas 1 a 5 · commit 7f21c0a
## Mercado, preço e canal
- o custo por criança transportada · origens: D-005 (P4: «dois propósitos; o custo vai ao estacionamento») e 03-idealidade.md (estacionamento do tema 3) · juntado: aparecia nos dois temas
## Falhas de mercado do pré-mortem
- prefeituras sem verba para o segundo motorista · origem: 5.3-12
## Ideias de apelo
- 4.8-06 · ver o transporte se aproximar · de B-001 · origem: 04-triagem.md (D-035) · motivo: «nenhum: fora do propósito»
- B-206 · um nome e uma música para cada onda · origem: 5.6, classificada na D-056 · motivo: apelo, sem função no propósito
## Necessidades vizinhas
- B-207 · café da manhã na escola para quem chega na primeira onda · origem: 5.6, classificada na D-056 · motivo: necessidade vizinha; não muda a chegada nem a segurança
## Régua do MVP
- os 12 casos canônicos, com as saídas ideais (caminhos e hashes): a Etapa 3 mede, em cada um, quanto do ideal o MVP entrega
## Conselho rápido · conselho/6.3-r1 · guardião e refutador
- guardião: ver o transporte se aproximar (4.8-06) poderia baixar M3, os minutos no ponto sem adulto? → você decide que não: a espera já é coberta pela 4.15-I5 e pela 4.13-13, e fica estacionada (D-053, com o seu motivo)
- refutador: nenhum motivo fraco; nenhuma origem perdida na junção (as duas do custo estão lá)
```

### 8.6 O teste de passagem, no `06-passagem.md`

O brief do leitor é o mesmo para os três; muda só a especialidade.

```markdown
# Brief · 6.4 · leitor L2 · rodada 1 · domínio: transporte e educação · sessão nova · modelo de juiz
## Você recebe
- 06-cir.md, montagem 2, commit a8d4e10 · 06-pacote-etapa-2.md, hash 41aa…
## Você não recebe
- o dossiê; as conversas; as perguntas previstas; o que os outros leitores escreveram
## Tarefa
Você começa a Etapa 2 amanhã, sem poder falar com ninguém do projeto.
1. Escreva, com as suas palavras: o propósito; o núcleo e os princípios; o que o conceito não é; a primeira tarefa que você faria; a bancada com que testaria.
2. Só depois: as perguntas que faria a quem escreveu. Para cada resposta que você deu a si mesmo, diga se deduziu ou chutou, e a frase em que se apoiou. Marque as perguntas cuja resposta mudaria o que você faria primeiro.
## Limites
- só os dois arquivos; o que faltar é pergunta, e não suposição
```

```markdown
# Passagem · 6.4 · leitor.py · transporte escolar rural
## Previstas · gravadas antes da rodada 1 · hash 61f0…
- 6.4-P1 quem é o adulto que espera com a criança no ponto · 6.4-P2 o que acontece quando a estrada fecha cedo · 6.4-P3 por que não a 4.5-B · 6.4-P4 como a escola sabe quem chegou · 6.4-P5 quanto custa · 6.4-P6 o que é a bancada
## Rodada 1 · CIR montagem 2 · L1 sistemas · L2 domínio · L3 generalista · juízes JR-1 e JR-2
### Reformulações, contra o gabarito tirado do CIR
- L1: as 5 batem
- L2: o núcleo diverge ("dois ônibus, um para quem mora longe e outro para quem mora perto"); a primeira tarefa, incompleta (sem a 4.9-R3); as outras 3 batem
- L3: o que não é, incompleta (sem a 4.5-A); as outras 4 batem
- ambiguidade, pelo leitor.py: L1 leu as ondas como horários do mesmo veículo, e L2, como veículos diferentes
### Perguntas
- 6.4-01 · L1 e L2 · "uma onda é um veículo diferente ou outra viagem do mesmo?" · L2 deduziu de «no tempo ou em veículos» · central · o dossiê responde: a 4.5-C deixa os dois abertos, e escolher é da Etapa 2 → ligação nova na seção 8 e item 3 da parte 1 do pacote
- 6.4-02 · L2 e L3 · "o que é 'criança pequena' em 4.9-R3 e em V4?" · L3 chutou "até 6 anos" · central · só você → D-054
- 6.4-03 · L1 · "quantas crianças cabem numa onda?" · secundária · ninguém sabe → seção 15: a Etapa 2 mede no protótipo; item 4 da parte 1
- 6.4-04 a 6.4-07 · são as suas P1 a P4 · secundárias · o dossiê responde → ligações nas seções 6, 7, 10 e 15
- previsto × real: 4 das 6 previstas apareceram (P1 a P4); 2 centrais que você não previu (6.4-01 e 6.4-02)
## Rodada 2 · CIR montagem 3 · L4 a L6, novos · juízes JR-3 e JR-4
- reformulações: as 15 batem · perguntas: 1, secundária, cuja resposta já estava na parte 3 do pacote → falso alarme; nada muda
- parada: nenhuma central, e as reformulações batem → fecha na rodada 2 (D-055)
```

A resposta à 6.4-02 é sua, e o `cir.py usos` decide se é esclarecimento ou volta:

```markdown
## D-054 · 6.4 Teste de passagem · esclarecimento · completa · 2027-03-01
- Contexto: 6.4-02, central, de L2 e L3: "o que é 'criança pequena' em 4.9-R3 e em V4?"; L3 chutou "até 6 anos"
- Opções: definir o termo agora; deixá-lo à Etapa 2, na seção 15
- Escolha: criança pequena é a que tem até 8 anos, em V4 e em 4.9-R3
- Motivo e objetivo: nas suas palavras, «é a idade até a qual as famílias daqui não deixam a criança ir sozinha ao ponto»
- Evidência: cir.py usos: V4 (1.5, D-008), 4.9-R3 (D-035) e os vereditos do 2.6-12 e dos 5.6-08 a 5.6-11 · o verificador releu os cinco com a definição ao lado: nenhum muda
- Dissenso: —
- Confiança: alta: 5 de 5 vereditos iguais com a definição
- O que reverteria: um veredito do tema 5 que mude com a definição (volta 6→5, só para ele)
- Pulado e risco: —
- Vigia: limpa
- Commit: c41f7b2
```

O termo vira bloco ao lado de V4 e de 4.9-R3, com a D-054; o `01-proposito.md` não muda, porque V4 não mudou: ganhou a definição de um termo.

### 8.7 O pronto e a conferência das fichas, no `06-pronto.md`

```markdown
# Pronto · 6.5 · pronto.py · CIR montagem 3 · commit c41f7b2
- I1 passa · 01-proposito.md, hash igual ao do estado (7c41e2a9b0d3) · congelado no 1.7 (D-011) · P2 a P4 descartadas, com o motivo · a seção 2 igual
- I2 passa · M1 a M13, cada uma com a linha de base, a fonte e o limite · custo de uso: M4, M5, M10 e M13 · dano: M3, M6, M7 e M9
- I3 a I6 passam · …
- I7 falha · B-206 e B-207 entraram no banco no 5.6, na leitura dos casos novos, e estão sem tipo no 04-triagem.md
- I8 a I14 passam · … · I14: o pacote no commit c41f7b2 · conselho/6.2-r1 gravado · o 6.4 fechou na rodada 2, com 0 centrais
- vigia, no CIR, no pacote e no estacionamento inteiros: 0
- crítico: nenhum item marcado sem evidência, ou com a evidência de outra coisa
## C-6.5 · conferência final do CIR · 52 afirmações com ficha · 50 conferem
- "a rota 3, depois de dividida, chegou a 90% na chuva" (CIR, seção 4) · F-060, T1 · scripts ✓ · não sustenta: a fonte diz 88%; o 1h20 de M4 confere · não confere → ficha nova F-094
- "a divisão pela distância separa irmãos de idades diferentes, e o mais velho falta para acompanhar o menor" (CIR, seção 13) · F-090, T2 · link morto, sem cópia no Wayback · o trecho está guardado na ficha · marcada
## Pendências · pendencias.py · e destinos
- I7 → volta 6→4.9, pela cir-arquitetura (D-056): B-206 é apelo, e B-207, necessidade vizinha; os dois vão ao estacionamento; só ele muda, e não há novo 6.4
- F-060 → volta 6→3, pela cir-idealidade (D-057): o melhor de hoje em M1 passa a 88% (F-094); o cir.py usos mostra que nada do tema 5 dependia do número, porque o R1 conta por caso; bastam a remontagem e a conferência
- F-090 → nenhuma volta resolve: ressalva sua (D-058), com o motivo, «o trecho guardado diz qual é a falha, e ela já está no que reverteria», na seção 15 e na pergunta da trava
- montagem 4 · commit 7f21c0a · conferir limpo · pronto.py: 14 de 14, com a ressalva da F-090
```

### 8.8 A trava e a retrospectiva, no `06-retrospectiva.md`

```markdown
## D-059 · 6.6 Aprovação · trava · 2027-03-05
- Contexto: CIR montagem 4, commit 7f21c0a · pronto 14 de 14, com a ressalva da F-090 (D-058) · seção 15: 4 perguntas abertas · o que reverteria: as 2 killers da D-050 e as outras condições
- Opções: aprovar; voltar a uma sub-etapa
- Escolha: aprovado, com a ressalva da F-090
- Commit: 7f21c0a
```

Trava: "sim" a "Aprova o CIR do transporte escolar rural (commit 7f21c0a), com a ressalva da F-090 (fonte fora do ar; o trecho está guardado na ficha)?"

```markdown
# Retrospectiva · 6.6 · retrospectiva.py · CIR aprovado na D-059, commit 7f21c0a · equipe-base
## A sua avaliação, gravada antes · hash 77e0…
- funcionou: "os casos de época do tema 5; largar a 4.5-B foi difícil, mas o quadro mostrou por quê"
- não funcionou: "o tema 4 foi longo; e eu não sabia dizer o que era uma onda até os leitores perguntarem"
## Placar · placar.py · com os desfechos que o projeto conhece
- 5.7: resistiu a 4.5-C; caíram a 4.5-B e a 4.5-A · Brier do conselho nessas previsões: 0,19
- 5.1, controles: os três como deviam, depois da segunda execução do negativo
- 6.2, conselho Passagem: 5 perguntas, 3 procederam · Brier 0,15
## Suas previsões, ao lado das do conselho
- antes do quadro do 5.7: C1, a 4.5-B · a escolhida foi a 4.5-C
- reservados do 5.2: o ganho sobre você foi 0 na 4.5-C, +2 na 4.5-B e +1 na 4.5-A
- falha temida do 5.3: a 5.3-03, achada como real
- perguntas do 6.4: 4 das 6 apareceram; as 2 centrais que você não previu eram de termo (a onda e a criança pequena)
## Doses · planejada × usada
- nos temas 1 a 6: 41 iguais, 5 subiram e 2 desceram · o 6.1 subiu para completa (voltas no tema 4) · o 6.3 ficou leve (17 itens)
## Voltas · onde nasceu a falta
- 4→3 (D-036): M13 só apareceu no tema 4 · nasceu no 3.2, que não perguntou a cada parte quanto tempo ela dá ao funcionamento
- 4.14→4.13 (D-041): às 6h10, crianças da ponta norte esperavam sem adulto · achada pelo cenário degradado, como devia
- 6→4.9 (D-056): B-206 e B-207 sem tipo · nasceu na condutora, que não manda à triagem as ideias que entram no banco depois do 4.9
- 6→3 (D-057): a F-060 não conferia · nasceu na transcrição da ficha, no tema 3
## Taxa de surpresa
- no 4.10: 3 de 36 (8,3%) · no CIR aprovado: 1 de 36 (2,8%): só a B-044 chegou, como 4.8-09, capacidade exploratória, com a pergunta da adesão; a B-051 e a B-058 serviam às famílias que caíram
## Decisão × desfecho
- o 3.2 sem M13: com o que se sabia, nenhuma parte tinha falado do próprio tempo; a decisão foi boa, e o desfecho, a volta 4→3 · a falta é do cartão (6.6-M1), e não de quem decidiu
- a sua C1 antes do quadro: seguia o que você mais valoriza, um adulto em cada ponto; o quadro mostrou o custo (M13), e você mudou, com registro · o quadro fez o que devia
- o 6.1 em dose completa: achou as 2 contradições da montagem 1 · decisão e desfecho bons
## Expectativa sem registro · reconstrutor RE-1, cego aos desfechos · marcada
- o que se esperava do 4.14, pelo cartão e pelo que se sabia antes: "o cenário degradado acha uma espera sem adulto" · é reconstrução, e não previsão
## Manter
- os casos de época e as suas previsões gravadas antes · a reformulação dos leitores, que achou a ambiguidade da onda sem que ninguém perguntasse por ela
## Mudar · com dono · também no aprendizado/melhorias.md
- 6.6-M1 · cir-idealidade · cartão do 3.2: perguntar a cada parte quanto tempo ela dá ao funcionamento (D-036)
- 6.6-M2 · cir-arquitetura · seção 6.3 do plano (4.9): definir os termos de cada "refuta se" ao escrever a restrição (D-054)
- 6.6-M3 · condutora · seção 6.5 do plano: as ideias que entram no banco depois do 4.9 voltam à triagem antes do 6.1 (D-056)
- 6.6-M4 · condutora · seção 6.4 do plano (o registro): o registrar.py confere, a cada registro, se cada item listado ganhou o seu bloco (a 5.3-05 só apareceu no 6.1)
```

### 8.9 A linha do `aprendizado.jsonl`

Como seria num projeto real; o exemplo é de teste e não grava. Só números e notas de método, sem o conteúdo do projeto.

```json
{"projeto": "h:3f8a…", "data": "2027-03-05", "fracao_tangentes_4_4": 0.30, "fracao_seguinte": 0.40, "tangentes": 36, "taxa_4_10": 0.083, "taxa_final": 0.028, "doses": {"iguais": 41, "subiram": 5, "desceram": 2}, "passagem": {"rodadas": 2, "previstas": 6, "apareceram": 4, "centrais_nao_previstas": 2, "falsos_alarmes": 1}, "voltas": {"4→3": 1, "4.14→4.13": 1, "6→4.9": 1, "6→3": 1}, "pronto": {"itens": 14, "ressalvas": 1}, "notas": ["um termo de 'refuta se' sem definição chegou ao 6.4", "ideias que entraram no banco no 5.6 chegaram ao 6.5 sem tipo", "um custo de uso de uma parte só apareceu no tema 4"]}
```

### 8.10 A chave "sintese" no `estado.json`

```json
"sintese": {
  "registros": "D-051 a D-059",
  "abertura": {"hash": "0c3e…", "temor": "na cobertura e no conselho Passagem"},
  "suas_versoes": {"hash": "2b7d…", "essencia": "combinada", "o_que_nao_e": "combinada"},
  "blocos": {"arquivo": "06-blocos.md", "secoes": 17, "superados": ["D-025 → D-036", "4.13 da 4.5-C → D-041"]},
  "montagens": [
    {"n": 1, "commit": "52be9d3", "afirmacoes": 96, "sustentadas": 88, "exageradas": 5, "nao_sustentadas": 1, "contradizem": 2, "cobertura_faltou": ["5.3-05"]},
    {"n": 2, "commit": "a8d4e10", "conferir": "limpo"},
    {"n": 3, "commit": "c41f7b2", "conferir": "limpo"},
    {"n": 4, "commit": "7f21c0a", "conferir": "limpo", "aprovada": true}
  ],
  "distribuicao_por_tema": {"1": 0.09, "2": 0.06, "3": 0.14, "4": 0.30, "5": 0.41},
  "pacote": {"arquivos": ["06-pacote-etapa-2.md", "pacote.json"], "commit": "7f21c0a", "conselho": "conselho/6.2-r1", "perguntas": 5, "procederam": 3},
  "estacionamento": {"itens": 19, "juntados": 1, "conselho": "conselho/6.3-r1"},
  "passagem": {"rodadas": 2, "leitores": 6, "previstas": 6, "apareceram": 4, "centrais_nao_previstas": 2, "secao_15": ["6.4-03"], "falsos_alarmes": 1, "registro": "D-055"},
  "pronto": {"itens": "14 de 14", "ressalvas": ["F-090 · D-058"], "voltas": ["D-056", "D-057"], "vigia": 0, "C-6.5": {"conferidas": 52, "conferem": 50}},
  "trava": "D-059, em travas",
  "retrospectiva": {"arquivo": "06-retrospectiva.md", "melhorias": ["6.6-M1", "6.6-M2", "6.6-M3", "6.6-M4"], "brier_6_2": 0.15},
  "aprendizado": "não: projeto de teste",
  "espelho": "não: projeto de teste",
  "hashes": {"06-blocos.md": "…", "06-cir.md": "…", "06-pacote-etapa-2.md": "…", "pacote.json": "…", "previstas": "61f0…", "avaliacao": "77e0…"}
}
```

## 9. Exemplos limpos e contaminados

De fora dos casos de teste, para o `exemplos.md`. O crítico da equipe e o conselho usam a coluna do meio como sinal.

| Contaminado | Limpo | O que muda |
| --- | --- | --- |
| Ligação num CIR de um programa de leitura: "O programa garante que todas as crianças leiam até o fim do 2º ano" | "No piloto, 41 de 50 crianças leram com fluência no fim do 2º ano (F-21); o limite ideal é 100% (M1)" | O número e o escopo do caso, no passado; o `cir.py` acusa "garante" e "todas" (achado 7) |
| Restrição num CIR de coleta seletiva, nas palavras do redator: "evitar que os catadores percam renda" | «O conceito não tira dos catadores a renda que eles têm hoje com o reciclável» · 4.9-R1 · hash 8d2f… | O que obriga vai por cópia; reescrito, muda o que obriga, e ninguém percebe (achados 5 e 9) |
| Seção 6: "A coleta porta a porta foi descartada por ser cara" | "A coleta porta a porta foi refutada na D-022: «a separação em casa caiu quando o caminhão passou a vir uma vez por semana» (M2 6–1)" | O motivo é o do registro, por cópia; "cara" é sinal de mercado para a vigia (achado 12) |
| Seção 17: "Houve ressalvas, superadas na discussão" | D-030, dissenso: «o refutador de método lembra que o ganho veio só dos bairros com associação de moradores» | O dissenso vai inteiro, com quem discordou e de quê (achado 8) |
| Seção 11: "Confiança: provável" | "Confiança média, pelo `decisao.py`: falta uma condição, o R5 válido sem os espelhos (5 de 8 com eles; 2 de 5 sem eles)" | A palavra de probabilidade só vale com a base em números ao lado (achado 14) |
| "Nenhuma falha nos 30 casos: o conceito é seguro" | "Nenhuma falha em 30 casos → até cerca de 1 em 10 casos parecidos ainda pode ter (regra de três)" | Zero em 30 não é zero; a regra de três dá o teto |
| Pacote de um CIR de coleta seletiva: "Instalar sensores de nível nas lixeiras para avisar a coleta" | Parte 4: "que meio avisa a coleta de que a lixeira encheu, respeitando 4.9-R2?" (4.13) | O meio é pergunta; escolher é da Etapa 2 |
| Leitor do 6.4: "Está claro; eu começaria pelo protótipo" | "O núcleo, nas minhas palavras: …; deduzi de «…»; chutei que 'bairro' é o setor do censo; esta pergunta mudaria o que faço primeiro" | A reformulação e o "deduzi ou chutei" mostram o que o "está claro" esconde (achados 1, 2 e 4) |
| Correção depois do 6.4, num CIR de vacinação: a condutora edita o `06-cir.md` e escreve que "vacina em dia" são as do calendário até os 5 anos | A pergunta vai ao grill; a sua resposta vira registro e bloco, e o CIR é remontado | A correção sem origem some na montagem seguinte; o `06-cir.md` nunca é editado à mão (achado 9) |
| Pronto: "[x] I11 · 10 casos canônicos" | "I11 passa · 12 casos, com os caminhos em `casos/` e os hashes das saídas" | Marcado não é feito; o item vale pela evidência (achado 13) |
| Retrospectiva num CIR de hortas comunitárias: "Erramos: o piloto falhou" | "A D-018, com o que se sabia (F-30: 2 de 3 bairros com água encanada), foi uma boa decisão; o desfecho foi ruim porque a seca de março cortou a água; a falta não nasceu no método" | A decisão é julgada pelo que se sabia, e não pelo desfecho (achado 16) |
| Retrospectiva: "Melhorar a comunicação entre as equipes" | "6.6-M1 · `cir-mapa` · cartão do 2.3: perguntar quem mais decide o horário da coleta (D-012)" | Com dono, skill e seção; a genérica não muda nada (achado 15) |
| Estacionamento: "Gamificação — fora" | "B-077 · pontos para quem separa o lixo · apelo · origem: `04-triagem.md` (D-024) · motivo: «a separação não mudou depois do primeiro mês (F-41)»" | Cada item com a origem e o motivo copiado; a Etapa 3 sabe o que está decidindo |
| Seção 1, num CIR de vacinação: "Uma plataforma de agendamento que reduz as filas do posto" | "Quem precisa de vacina sai protegido no mesmo dia em que procura o posto" (lig-1.1 · 4.15-I2, P1) | A essência diz o que muda para quem usa, sem produto, e com a origem (achado 10) |

## 10. Arquivos

```jsx
cir-sintese/
  SKILL.md                 o tema em umas 200 linhas: cartões, passos, regras e quem lê o quê
  references/
    cartoes.md             o cartão do tema e os do 6.1 ao 6.6 (seção 5)
    construcao.md          o esqueleto, o bloco, os trechos fixos, os itens, os superados
                           e a vigia por bloco, desde o tema 1 (6.2)
    montagem.md            a passagem, a abertura, a numeração e a montagem: a ordem das seções,
                           as famílias que não venceram, o "Como ler" e as seções 15 a 17 (6.1 e 6.3)
    ligacoes.md            você primeiro, o redator, as seções 1 e 14, o que o redator não faz
                           e o decompositor (6.4)
    conferencia.md         o cir.py conferir, de a a h, o verificador, o crítico e os destinos (6.5)
    pacote.md              as 9 partes, o "em vez disso", o completo e o conselho Passagem (6.6)
    etapa3.md              o estacionamento, os tipos, o motivo, a régua do MVP e o conselho (6.7)
    passagem.md            a previsão, os leitores, reformular e perguntar, os juízes, a classificação,
                           a correção, a volta disfarçada e a parada (6.8)
    pronto.md              os 14 itens e a evidência, as pendências, as fichas e as ressalvas (6.9)
    retrospectiva.md       a trava, a sua avaliação, o retrospectiva.py, o reconstrutor,
                           decisão × desfecho, manter e mudar, o aprendizado e o espelho (6.10)
    voltas.md              as voltas, a auditoria, o modo avulso e o reuso (6.11 e 6.12)
    agentes.md             quem vê o quê e os formatos das entregas (seção 11)
    grill.md               perguntas boas e ruins, por sub-etapa
    exemplos.md            limpos e contaminados (seção 9)
    regras.md              as 14 regras, com os pensamentos e a realidade (seção 7)
    formatos.md            os modelos da seção 8
  assets/
    cir-modelo.md          as 17 seções, com as sub-etapas de origem e o "Como ler"; dele saem
                           o esqueleto do 06-blocos.md e o modelo "CIR" da condutora
    cir-bloco.md           o formato do bloco e da ligação, que o registrar.py segue
    pronto.yaml            os 14 itens, com a evidência que cada um pede
    generalizacao.txt      "sempre", "todas", "nunca", "garante" e as outras marcas de generalização;
                           o presente genérico e os qualificadores que não podem sumir
    briefs/                os modelos de brief da seção 11: redator, decompositor, verificador,
                           crítico, leitor, juiz das reformulações e reconstrutor
    modelos/               os modelos vazios do tema, com as seções na ordem: 06-conferencia.md,
                           06-pacote-etapa-2.md, 06-estacionamento-etapa-3.md, 06-passagem.md,
                           06-pronto.md e 06-retrospectiva.md
  scripts/
    cir.py                 montar: os blocos e as origens, os hashes, os superados e a ordem;
                           conferir: de a a h, e --sem-dossie na auditoria; afirmacoes: os lotes
                           sorteados, com os trechos das fontes; usos: o que depende de um ID ou termo
    pacote.py              etapa2: as 9 partes das fontes, no commit da montagem, e o pacote.json;
                           etapa3: junta, tira a repetição, guarda as origens e confere o motivo
    leitor.py              as previstas com hash; o que cada leitor recebe; a ambiguidade entre
                           reformulações; o previsto × real; a regra de parada
    pronto.py              o pronto.yaml: passa, falha ou não verificado; --auditoria, no tema 0
    retrospectiva.py       o placar, as previsões, as doses, as voltas e a taxa de surpresa, com a regra
                           copiada do surpresa.py; a linha do aprendizado.jsonl, só em projeto real;
                           --mediana, que a condutora chama no 4.4 do projeto seguinte
    cartoes.py             confere os cartões contra o índice da condutora
  tests/                   casos dos scripts e as falhas plantadas (seção 13)
```

**Fora da skill, no repositório das skills:** `aprendizado/aprendizado.jsonl`, uma linha por projeto real, só com números e notas de método; e `aprendizado/melhorias.md`, as melhorias com dono, que você decide se e quando aplicar.

**Quem lê o quê:** os agentes recebem só o brief, montado pelo `brief.py`; nenhum lê a skill, e nenhum lê o dossiê inteiro.

| Arquivo | Quem lê | Quando |
| --- | --- | --- |
| `SKILL.md` | A condutora | Na abertura do 6.1 e em cada volta |
| `references/cartoes.md` | A condutora e o `cartoes.py` | Em cada sub-etapa |
| `references/construcao.md`, `assets/cir-modelo.md` e `cir-bloco.md` | O `dossie_init.py` e o `registrar.py` da condutora | Na abertura do projeto e a cada registro, desde o tema 1 |
| `references/montagem.md` e `ligacoes.md` | A condutora e o `cir.py`; o redator e o decompositor recebem só o brief | No 6.1 e em cada remontagem |
| `references/conferencia.md` e `assets/generalizacao.txt` | O `cir.py`, a condutora e o crítico da equipe; o verificador recebe só o brief | No 6.1, no "em vez disso" do 6.2 e em cada remontagem |
| `references/pacote.md` e `etapa3.md` | O `pacote.py`, a condutora e os conselhos rápidos do 6.2 e do 6.3 | No 6.2, no 6.3 e em cada remontagem |
| `references/passagem.md` | A condutora e o `leitor.py`; leitores e juízes recebem só o brief | No 6.4 |
| `references/pronto.md` e `assets/pronto.yaml` | O `pronto.py`, a condutora e o crítico da equipe | No 6.5 e na auditoria do tema 0 |
| `references/retrospectiva.md` | A condutora, o `retrospectiva.py` e a equipe-base; o reconstrutor recebe só o brief | No 6.6, depois do "sim" |
| `references/voltas.md` | A condutora | Nas voltas, na auditoria e no modo avulso |
| `references/agentes.md` e `assets/briefs/` | O `brief.py` da condutora | Em cada brief |
| `references/regras.md` e `exemplos.md` | O crítico da equipe e o conselho | Nas validações |
| `references/grill.md` | O `grill-embasado` | No passo 1 de cada sub-etapa |
| `aprendizado/aprendizado.jsonl` | A condutora, pelo `retrospectiva.py --mediana`; nenhum agente | No 4.4 dos projetos seguintes |

## 11. Subagentes

A skill não chama agentes: a condutora monta cada sessão com o `brief.py`, pelos cartões, e o grill, os pesquisadores, as equipes e o conselho chegam pelas skills genéricas. Aqui ficam os agentes próprios do tema, o que cada um vê e o que entrega. Nenhum deles lê o dossiê inteiro; nenhum vê as suas versões nem as suas perguntas previstas; e quem confere nunca sabe quem escreveu.

| Agente | Quantos | Vê | Não vê | Entrega |
| --- | --- | --- | --- | --- |
| Redator · 6.1, 6.2 e correções | 1 por seção, numa sessão própria; no 6.2, 1 para o "em vez disso" | Os blocos e as fontes da seção, a `esp-*` do tema dela e o formato da ligação; nas seções 1 e 14, o CIR montado | As outras seções em construção, as suas versões, as conversas e os vereditos | A primeira frase da seção e as ligações, cada uma com os IDs que liga; no 6.2, o "em vez disso" de cada princípio e restrição |
| Decompositor · 6.1 e correções | 1 por seção, que não é o redator | As ligações da seção e os IDs que cada uma cita | O que o redator pensou e os vereditos | As afirmações atômicas, cada uma com as origens que a ligação cita |
| Verificador · 6.1, 6.2 e remontagens | 1 por lote de até 20 afirmações, de seções diferentes, em ordem sorteada | A afirmação e os trechos das fontes que ela cita | A seção, a ligação inteira, quem escreveu e os outros vereditos | Sustentada, não sustentada, exagerada ou contradiz, com o trecho que decide |
| Crítico da equipe · 6.1 e 6.5 | 1 | O CIR montado, a conferência, a saída do `pronto.py`, o `regras.md` e o `exemplos.md` | As conversas e quem escreveu cada ligação | Contradições entre seções, distribuição torta, conclusão sem apoio, item marcado sem evidência e os pensamentos da seção 7 |
| Conselho rápido Passagem · 6.2 | 2: o leitor da Etapa 2, sem contexto, e o guardião do propósito; e o crítico | O pacote e o CIR, com o hash; o guardião, também o propósito congelado | O dossiê, as conversas e as suas versões | O ensaio da primeira decisão e as perguntas centrais sem resposta, cada uma com a probabilidade de proceder, ao placar |
| Conselho rápido · 6.3 | 2: o guardião do propósito e o refutador | O estacionamento consolidado, com as origens e os motivos, e o propósito | O pacote e as conversas | O que muda o resultado e foi estacionado; o motivo fraco; a origem perdida na junção |
| Leitor · 6.4 | 3 por rodada, novos a cada rodada: engenharia de sistemas, o domínio e um generalista | O CIR e o pacote, com o hash | O dossiê, as conversas, as suas previstas e os outros leitores | As reformulações e, só depois, as perguntas, com o "deduzi ou chutei" e a frase de apoio |
| Juiz das reformulações · 6.4 | 2 por rodada | As reformulações, sem o nome do leitor, e o gabarito tirado do próprio CIR | As perguntas dos leitores e as suas previstas | Bate, diverge ou incompleta, item por item, com o trecho do gabarito |
| Pesquisador · 6.1 a 6.5 | Os da `pesquisa-cientifica`, no modo conferir | A ficha e a afirmação que a cita | O resto do CIR e os vereditos | Confere, não confere ou marcada, em `fontes/conferencias/`; no 6.5, a C-6.5 |
| Reconstrutor · 6.6 | 1 por expectativa sem registro | O cartão da sub-etapa e o que se sabia antes dela | Os desfechos, as saídas seguintes e a sua avaliação | A expectativa reconstruída, marcada como reconstrução |

**O que o crítico da equipe procura:** frase sem origem que passou; ligação que reescreve trecho fixo, resume dissenso, arredonda número ou troca o passado de um caso pelo presente genérico; conclusão de seção sem apoio na seção; contradição entre seções; um tema que domina a distribuição; item de família que perdeu nas seções 7 a 10; "o que não é" sem o ID da exclusão; meio ou tecnologia no pacote; "em vez disso" que contradiz a proibição; item estacionado sem motivo, ou com a origem perdida; leitor que recebeu algo além do CIR e do pacote; resposta que muda o propósito, o núcleo, um princípio, uma restrição ou a escolha tratada como esclarecimento; item do pronto marcado sem evidência, ou com a de outra coisa; comparação da retrospectiva com uma expectativa que não foi gravada nem reconstruída às cegas; melhoria sem dono; e os pensamentos da seção 7.

**Sessões:** cada agente roda numa sessão própria, como subagente, sem memória das outras; a condutora não repassa conversa, só o brief. Os redatores rodam em paralelo, primeiro os das seções com mais ligação e, por último, os das seções 1 e 14, que veem o CIR montado; cada decompositor, depois do seu redator; os verificadores, em lotes paralelos, quando todas as ligações estão decompostas; o crítico, depois dos vereditos. No 6.4, os 3 leitores rodam em paralelo, depois das suas previstas, e os juízes, depois das 3 reformulações. O reconstrutor roda só depois do "sim" e da sua avaliação.

**Modelos e custo:** redatores, decompositores e o reconstrutor usam o modelo de trabalho do mapa de modelos do 0.3; verificadores, leitores e juízes das reformulações, o modelo de juiz, porque juízes de IA favorecem o que eles mesmos geraram (achado 17), e um leitor do mesmo modelo do redator tende a completar as lacunas do mesmo jeito que ele (seção 14). Um tema com 17 seções, perto de 100 afirmações e 2 rodadas do 6.4 fica entre 60 e 80 sessões filhas, a maioria pequenas: uma seção, um lote, uma reformulação. A métrica de custo da seção 13 registra os tokens, o tempo e as sessões; o custo só desempata.

## 12. Casos-limite

| Caso | O que a skill faz |
| --- | --- |
| Uma seção do CIR fica sem bloco | O `cir.py montar` não inventa: a seção sai com "sem bloco", com a sub-etapa de origem; se ela foi pulada com registro, vem o "pulado e risco"; senão, é pendência do 6.5, e a falta volta à skill dona |
| Uma origem mudou sem registro | A montagem para, e a vigia acusa; a condutora mostra o que mudou e pergunta se a mudança se registra, pela skill dona, ou se a origem volta ao que estava. Nada segue antes |
| Dois registros se contradizem, e nenhum supera o outro | O `cir.py` não escolhe: mostra os dois, com as origens; você decide qual vale, com registro, e o outro fica marcado "superado por" |
| Você escolheu no 5.7 um conceito refutado | O CIR diz que ele foi refutado, pelo quê, e traz o seu motivo por cópia; a parte 9 do pacote abre com a refutação; nenhuma ligação diz que ele passou |
| Abstenção no 5.7 | Não há conceito de referência: o CIR documenta o que se tentou, o que se provou e onde cada conceito quebrou, sem as seções 7 a 10; não há pacote da Etapa 2, e vai uma nota do que reabriria (o tema 1, o 3 ou o 4); a trava aprova o encerramento, e não um conceito |
| Você discorda de uma ligação | Você a reescreve, com registro; a sua versão passa pelo decompositor e pelo verificador, como qualquer outra; se uma afirmação sua não tem sustentação, a condutora mostra, e você decide |
| Surge uma ideia nova no tema 6 | Entra no banco, com a origem, e nunca direto no CIR; se pode mudar o resultado, é volta ao 4.9; se não, vai à triagem e ao estacionamento |
| Os leitores ainda divergem depois de 3 rodadas | Sem o seu "sim" para a quarta, você reescreve o trecho que divide, com registro, e a montagem passa pela conferência; ou a ambiguidade vai à seção 15, com as leituras e quem decide, e o I14 fica com ressalva |
| Um leitor acusa uma lacuna que não existe | Falso alarme: a condutora mostra onde está a resposta, e o CIR não muda; se o mesmo falso alarme vem de 2 leitores, a resposta existe, mas não se acha, e a ligação ganha o caminho |
| O pacote fica enorme | O pacote não resume: o que está num arquivo vai pelo ID e pelo caminho; se a parte 1 passa de 5 ações, você escolhe as 5 primeiras, com registro, e o resto vai à seção 15 |
| Há menos de 10 casos canônicos | O I11 falha; a volta vai ao 2.6 ou ao 5.6, por mais casos, ou vira ressalva sua, com o número e o motivo, na pergunta da trava |
| O documento auditado no tema 0 é de produto | A auditoria roda igual; telas, tecnologia e preço saem como lacuna, pela vigia; o `00-auditoria.md` diz que o documento descreve um produto, e não um conceito, e o plano do projeto começa pelo tema 1 |
| Uma ficha que sustenta a escolha foi retratada | Volta 6→5, pela `cir-prova`, para o que dependia dela; vira ressalva só se o `cir.py usos` mostra que nenhum veredito dependia |
| Você quer pular o 6.4 | Pode, com registro e o risco; o I14 fica com ressalva, e o topo do CIR e do pacote diz "aprovado sem teste de passagem" |
| Um leitor recebeu algo além do CIR e do pacote | A rodada é refeita, com leitores novos; a anterior fica no `06-passagem.md`, marcada, e não conta |
| Projeto de teste | Tudo roda igual, menos a linha do `aprendizado.jsonl` e o espelho; o estado diz "projeto de teste" |
| A Etapa 2 pede o pacote antes do 6.6 | Sai com "não aprovado" no topo, com o commit e o que falta; nunca como versão final |
| A Etapa 2 acha um erro no CIR aprovado | A correção vai à origem, pela skill dona, e sai uma versão nova, com conferência e trava; a aprovada continua no histórico, e o espelho só muda depois do novo "sim" |

## 13. Testes e métricas

| Teste | Como | Passa se |
| --- | --- | --- |
| Infidelidade plantada | 40 ligações de um CIR de teste, de outro domínio: 20 com uma infidelidade plantada (número trocado, escopo perdido, qualificador que sumiu, causa inventada, dissenso resumido) e 20 fiéis, misturadas | O `cir.py conferir` e o verificador pegam pelo menos 18 das 20 e acusam no máximo 2 das fiéis (achados 5 e 6) |
| Omissão plantada | Um dossiê de teste sem 6 blocos: uma restrição, uma killer condition, um dissenso, uma falha real, uma pergunta aberta e um caso canônico | A cobertura do `cir.py` acusa os 6 (achado 6) |
| Telefone | 5 correções seguidas no mesmo CIR, cada uma por uma volta diferente, com a remontagem | Os trechos fixos ficam iguais aos da origem, pelo hash, nas 5; nenhuma ligação muda sem que a origem dela tenha mudado (achado 9) |
| Lacunas plantadas | Um CIR de outro domínio com 5 lacunas: um termo sem definição num "refuta se", uma ambiguidade no núcleo, um princípio que se lê de dois jeitos, a primeira tarefa que falta e uma bancada sem caminho | Os leitores acham pelo menos 4 em até 2 rodadas (achados 1 a 4) |
| CIR limpo | O mesmo CIR, sem as lacunas, com 2 rodadas de leitores | No máximo 1 falso alarme central |
| Pronto plantado | Um dossiê de teste com 3 itens marcados sem evidência e 1 com a evidência de outra coisa | O `pronto.py` falha os 4, e o crítico aponta o da evidência errada (achado 13) |
| Vigia plantada | 8 sinais no CIR, no pacote e no estacionamento: tela, tecnologia, preço, canal, nome de produto, marca, "plataforma" e um meio na parte 1 do pacote | A vigia do 6.5 acusa os 8 |
| Fontes plantadas | 3 problemas nas fichas citadas: um número que mudou na fonte, um link morto sem cópia e uma retratação | A C-6.5 acusa os 3, e cada um vai ao seu destino: a volta à skill dona, a ressalva e a volta 6→5 |
| Decisão × desfecho plantados | 4 decisões de um projeto de teste, com o que se sabia gravado: boa com desfecho ruim, ruim com desfecho bom, boa com bom e ruim com ruim | A equipe classifica as 4 pela decisão, e não pelo desfecho, e a melhoria das 2 ruins tem dono, skill e seção (achados 15 e 16) |
| Aprendizado, teste × real | Um projeto marcado de teste e outro real, com nomes e números do domínio no dossiê | Só o real grava uma linha, e nenhum campo traz nome, número do domínio ou frase do CIR; no 4.4 seguinte, a condutora mostra os valores e pergunta, porque há menos de 3 projetos |
| Auditoria do Motor | O documento do Motor de Insights, como versão 1 de um CIR, no `pronto.py --auditoria`, no `cir.py conferir --sem-dossie` e na vigia | Pela sua regra de correspondência, as lacunas acusadas batem com o seu gabarito, escrito antes |
| Motor ponta a ponta | O tema 6 do Motor, com o seu gabarito escrito antes | O CIR, o pacote e o estacionamento batem com o gabarito; nenhuma afirmação sem sustentação; o 6.4 fecha em até 3 rodadas |
| Outros casos do plano geral | Informar eleitores sobre candidatos, com ligações em pares em que só o candidato muda; o hábito de exercício, com a isca que melhorou a métrica; a água tratada, com o adversário que desvia; o reencontro de amigos, com desfechos qualitativos e a abstenção | Nenhuma ligação favorece um candidato; a isca aparece no "não reintroduzir sem prova"; o desvio está na parte 9 do pacote; e, no reencontro, a abstenção vira CIR sem pacote, com a nota do que reabriria |
| Usuário simulado teimoso | Um usuário que quer editar o `06-cir.md` à mão, pular o 6.4, aceitar "não verificado" como passa, resumir o dissenso e citar uma tecnologia no pacote | A skill remonta da origem, e a edição some, com o aviso; pula o 6.4 só com registro e a marca "aprovado sem teste de passagem"; não aceita "não verificado"; mantém o dissenso por cópia; e a tecnologia vira fronteira |
| Condições A, B e C | O mesmo tema 6 sem skills, com o fluxograma e o v2 colados no prompt, e com a skill, pelo menos 3 execuções de cada | Com a skill, menos afirmações sem sustentação, mais cobertura, menos centrais na última rodada e o pacote mais estável entre execuções, no julgamento cego |

**Comparações que decidem o desenho,** todas às cegas: fica a que levar ao CIR mais fiel e ao pacote mais usável, pelo seu julgamento cego e pelos gabaritos; o custo só desempata.

- **Montagem:** o CIR montado de blocos contra o CIR redigido de uma vez a partir do dossiê, contando as afirmações sem sustentação e as omissões (achados 5 e 9).
- **Conferência:** as afirmações atômicas contra um juiz do todo, contando as infidelidades plantadas que passam (achado 6).
- **Leitores:** 3 contra 1, e a reformulação primeiro contra só perguntas, contando as lacunas plantadas achadas por rodada (achados 2 e 4).
- **Modelo do leitor:** o modelo de juiz contra o do redator, contando o que cada um completa sem perguntar.
- **Previsão:** com e sem as suas previstas, contando as rodadas e as centrais, e o acerto delas de um projeto ao seguinte (achado 3).
- **Pacote:** gerado das fontes contra gerado do CIR, contando as diferenças que a conferência acusa (achado 9).

**Métricas acompanhadas:**

| Métrica | Como mede | Alvo |
| --- | --- | --- |
| Afirmações sem sustentação no CIR aprovado | O verificador e o `cir.py` | 0 |
| Trechos fixos alterados | O hash, contra a origem | 0 |
| Cobertura | O `cir.py conferir` (f) | 100% |
| Centrais na última rodada do 6.4 | O `leitor.py` | 0 |
| Rodadas do 6.4 | O `leitor.py` | Até 3 |
| Acerto das suas previstas | As que apareceram e as centrais que você não previu | Registrado; acompanhado de um projeto ao seguinte |
| Falsos alarmes dos leitores | O `06-passagem.md` | Registrado; alvo depois da linha de base da fase 2 |
| Distribuição das afirmações por tema | O `cir.py conferir` (g) | Registrado; alvo depois da linha de base da fase 2 |
| Pronto | O `pronto.py` | 14 de 14, ou com ressalva sua |
| Vigia no 6.5 | O `vigia.py`, no CIR, no pacote e no estacionamento | 0 |
| Fichas que não conferem no 6.5 | A C-6.5 | Registrado; cada uma com destino |
| Calibração do conselho e a sua | A pontuação de Brier, pelo `placar.py` | Registrado; alvo depois da linha de base da fase 2 |
| Taxa de surpresa final × a do 4.10 | O `retrospectiva.py` | Registrado |
| Melhorias com dono | O `06-retrospectiva.md` | Todas |
| Custo | Tokens, tempo e sessões filhas, por sub-etapa | Registrado, sem alvo, pelo critério máximo |

**Aceite:** os cartões passam no `cartoes.py`; os scripts passam nos testes de `tests/`; passam a infidelidade plantada, a omissão plantada, o telefone, as lacunas plantadas, o CIR limpo, o pronto plantado, a vigia plantada, as fontes plantadas, a decisão × desfecho plantados, o aprendizado teste × real e a auditoria do Motor. **Aceite seu:** o tema 6 do Motor numa sessão real, com você.

## 14. Riscos

| Risco | Sinal | O que a skill faz |
| --- | --- | --- |
| Invenção no CIR | Frase sem origem, ou com uma origem que não diz aquilo | O `cir.py` (a) e o verificador, afirmação por afirmação (achados 5 e 11) |
| Generalização | "Sempre", "todas", "garante"; o presente genérico no lugar do passado de um caso | O `generalizacao.txt` no (e), e o verificador dá "exagerada" (achado 7) |
| Infidelidade sutil | Número arredondado, escopo perdido, uma causa que a origem não diz | Os trechos fixos por cópia, com hash; o (c) nos números; as afirmações atômicas (achados 5 e 6) |
| Omissão | Um item dos registros que não chega ao CIR | A cobertura (f), contra a lista que sai dos registros, com o temor da abertura (achado 6) |
| O último tema domina | Muitas afirmações do tema 5 e poucas dos primeiros temas | A distribuição (g), ao crítico; um redator por seção, com só os blocos dela (achado 6) |
| Conclusão escondida | A seção começa pelo contexto, e a conclusão fica no meio | A primeira frase de cada seção é a conclusão; as seções 1 e 14, por último (achado 10) |
| Dissenso apagado | "Houve ressalvas", "foi superado" | O dissenso por cópia, na seção 17; a cobertura conta cada dissenso (achado 8) |
| Confiança sem número | "Provável", "alta", sem a base | O (d), e a confiança que vem do `decisao.py`, com a base ao lado (achado 14) |
| Telefone | O CIR muda um pouco a cada correção | Remontar, nunca reescrever; os trechos fixos pelo hash; o pacote gerado das fontes (achado 9) |
| Maldição do conhecimento | Quem escreveu acha claro o que só ele entende | Os leitores sem contexto, em sessões novas, e as suas previstas, gravadas antes, para medir o quanto você acerta (achados 1 e 3) |
| Leitor que preenche | A reformulação bate, mas por chute | O "deduzi ou chutei", com a frase de apoio; os juízes das reformulações; os leitores no modelo de juiz (achados 2 e 4) |
| Volta disfarçada | Uma resposta que muda o núcleo entra como esclarecimento | A regra da seção 6.8 e o `cir.py usos`; o crítico procura |
| Checklist de fachada | Item marcado sem evidência | O `pronto.py`, com a evidência de cada item; "não verificado" conta como falha (achado 13) |
| Fontes que mudaram | Um número que não bate mais com a fonte; link morto | A C-6.5, refeita, e não lembrada; a ficha nova pela skill dona, ou a ressalva sua |
| Retrospectiva pelo desfecho | "Erramos" ou "acertamos", pelo resultado | Decisão × desfecho, contra o que se sabia; o que foi gravado antes, ou a reconstrução cega, marcada (achado 16) |
| Melhoria genérica | "Melhorar a comunicação" | Cada melhoria com dono, skill e seção; a genérica não entra (achado 15) |
| Vazamento entre projetos | O conteúdo de um projeto chega a outro | O `aprendizado.jsonl` só com números e notas de método, pela lista de campos; projeto de teste não grava |
| Espelho lido por quem devia estar cego | Um agente lê o CIR no Notion | O espelho é só do CIR aprovado, depois do "sim", e nenhum brief tem o link |
| Autopreferência | O verificador aprova o que o seu modelo escreveu | Verificador, leitores e juízes no modelo de juiz; quem confere não sabe quem escreveu (achado 17) |
| Pacote que escolhe a tecnologia | Um meio, uma marca ou uma ferramenta no pacote | As fronteiras como pergunta; a vigia no pacote; o "em vez disso" diz o comportamento, e não o meio |
| Cansaço no fim | Você aprova sem ler, no último tema | A trava com um resumo curto (o commit, os 14 itens, as ressalvas, as perguntas abertas e o que reverteria), e só "sim" aprova; cada pendência fecha ou vira ressalva sua, nas suas palavras |

## 15. O que fica de fora

- **Decidir ou mudar o conceito:** é do tema 5; aqui, a escolha é documentada, e a correção que muda o núcleo é volta, pela skill dona.
- **Tecnologia, viabilidade técnica e implementação:** Etapa 2, pelas fronteiras do pacote.
- **Mercado, preço, canal e quem pagaria:** Etapa 3, pelo estacionamento.
- **Resumo para terceiros sem a origem:** uma página para o prefeito ou para quem financia não é o CIR; se você quiser uma, ela sai do CIR aprovado, com o link para ele, e fora do dossiê.
- **Copiar o texto da `doc-coauthoring`:** a licença não está declarada; entra só a ideia do teste de leitor, citada.
- **Espelho do CIR em construção:** só o aprovado, depois do "sim".
- **Reescrever por estilo:** o redator escreve as ligações, e ninguém reescreve um trecho fixo para soar melhor.
- **O documento de produto:** é da Etapa 2 em diante, com a `create-prd` ou outra; o pacote só diz o que o produto não pode perder.
- **Guardar entre projetos o conteúdo de um projeto:** só o `aprendizado.jsonl`, com números e notas de método.
- **Aplicar as melhorias nas skills:** a retrospectiva propõe, com dono; você decide se e quando, fora do projeto.

## 16. Decidido e em aberto

**Decidido:**

- **Universal primeiro e Claude primeiro,** como no callout do topo.
- **Os cartões do tema 6 e do 6.1 ao 6.6 são o contrato com a condutora,** e o `cartoes.py` confere; o cartão do tema fica aqui, porque é esta skill que abre o tema.
- **O CIR é montado por script, a partir dos blocos que o `registrar.py` grava desde o tema 1; o `06-blocos.md` é a fonte única, e o `06-cir.md`, gerado, nunca é editado à mão.** Motivo: texto reescrito por modelos, de mão em mão, deriva ([Perez et al., 2024](https://arxiv.org/abs/2407.04503)), e o que mais falha na rastreabilidade é saber de onde um requisito veio ([Gotel e Finkelstein, 1994](https://doi.org/10.1109/ICRE.1994.292398)).
- **O que obriga ou promete entra por cópia, entre «», com o hash da origem; o redator só escreve as ligações.** Motivo: modelos de resumo põem no texto o que não está no documento ([Maynez et al., 2020](https://arxiv.org/abs/2005.00661)), e a infidelidade sutil passa pelos juízes ([Kim et al., 2024](https://arxiv.org/abs/2404.01261)).
- **Cada ligação é quebrada em afirmações atômicas, e todas são conferidas por um verificador que vê só a afirmação e as fontes dela; os trechos fixos, pelo hash.** Motivo: a conferência por afirmação atômica mostra o que o juízo do todo esconde ([Min et al., 2023](https://arxiv.org/abs/2305.14251); [Kim et al., 2024](https://arxiv.org/abs/2404.01261)).
- **O `cir.py conferir` acusa generalização, número fora da origem e confiança sem a base em números.** Motivo: resumir generaliza, e pedir precisão piora ([Peters e Chin-Yee, 2025](https://doi.org/10.1098/rsos.241776)); palavras de probabilidade se leem de jeitos diferentes, e só o número ao lado ajuda ([Wintle et al., 2019](https://doi.org/10.1371/journal.pone.0213522)); e modelos verbalizam confiança alta demais ([Xiong et al., 2024](https://arxiv.org/abs/2306.13063)).
- **A cobertura é item a item, contra a lista que sai dos registros, e a distribuição das afirmações por tema vai ao crítico.** Motivo: os resumos omitem muito e dão peso demais ao fim ([Kim et al., 2024](https://arxiv.org/abs/2404.01261)), e o que fica no meio de um contexto longo se perde ([Liu et al., 2024](https://arxiv.org/abs/2307.03172)).
- **O dissenso vai por cópia à seção 17, nunca resumido.** Motivo: resumos apagam vozes, de forma desigual ([Zhang et al., 2024](https://arxiv.org/abs/2311.07884)); a [`discovery-agents-handoff`](https://github.com/klausners/discovery-agents-handoff) guarda uma seção só para a evidência que discorda.
- **A primeira frase de cada seção é a conclusão, e as seções 1 e 14 se escrevem por último, sobre o CIR montado.** Motivo: quem lê procura a conclusão, e o meio se perde ([Liu et al., 2024](https://arxiv.org/abs/2307.03172)); é a ordem da [`doc-coauthoring`](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring) e a pirâmide da [`think-pyramid-principle`](https://github.com/product-on-purpose/thinking-framework-skills/tree/main/skills/think-pyramid-principle).
- **A sua essência e o seu "o que não é" vêm antes dos do redator, com hash, e a escolhida passa pelo verificador, venha de quem vier.** Motivo: quem já conhece uma versão não consegue imaginar o que pensaria sem ela ([Camerer, Loewenstein e Weber, 1989](https://doi.org/10.1086/261651)); e as duas, lado a lado, mostram onde você e o CIR divergem.
- **Verificador, leitores e juízes das reformulações rodam no modelo de juiz, e quem confere não sabe quem escreveu.** Motivo: juízes de IA favorecem o que eles mesmos geraram ([Panickssery, Bowman e Feng, 2024](https://arxiv.org/abs/2404.13076)), e um modelo que revisa o próprio texto sem informação de fora não melhora ([Huang et al., 2023](https://arxiv.org/abs/2310.01798)).
- **O teste de passagem tem 3 leitores sem contexto por rodada, que reformulam antes de perguntar e dizem se deduziram ou chutaram, com juízes contra o gabarito tirado do CIR; no máximo 3 rodadas, e a quarta só com o seu "sim".** Motivo: quem escreve acha que foi entendido mais vezes do que é ([Keysar e Henly, 2002](https://doi.org/10.1111/1467-9280.00439)); a síntese de quem recebe é parte do que fez o I-PASS reduzir erros ([Starmer et al., 2014](https://doi.org/10.1056/NEJMsa1405556)), e explicar com as próprias palavras funcionou em 19 de 20 estudos ([Talevski et al., 2020](https://doi.org/10.1371/journal.pone.0231350)); modelos não reconhecem bem a própria ambiguidade ([Liu et al., 2023](https://arxiv.org/abs/2304.14399)); o teste de leitor é ideia da `doc-coauthoring`, e o limite de rodadas, da `discovery-agents-handoff`.
- **As suas perguntas previstas são gravadas com hash antes da rodada e comparadas com as reais.** Motivo: prever os problemas do leitor melhora com a comparação com leitores de verdade ([Schriver, 1992](https://doi.org/10.1177/0741088392009002001)).
- **Toda correção entra pela origem, e a resposta que muda o propósito, o núcleo, um princípio, uma restrição ou a escolha é volta, e não esclarecimento; o `cir.py usos` mostra o que depende de um termo.** Motivo: quando o motivo de uma decisão se perde, quem vem depois a desfaz sem saber ([Jansen e Bosch, 2005](https://doi.org/10.1109/WICSA.2005.61)).
- **O pacote da Etapa 2 é gerado das fontes, no commit da montagem, com as 9 partes; só o "em vez disso" é escrito, e conferido.** Motivo: gerado do CIR, o pacote copiaria a deriva dele ([Perez et al., 2024](https://arxiv.org/abs/2407.04503)); a proibição sozinha puxa o que proíbe ([`writing-for-agents`](https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents)); a lista de ações e o plano de contingência vêm do I-PASS ([AHRQ](https://www.ahrq.gov/teamstepps-program/curriculum/communication/tools/ipass.html)); o que se confere vai pelo caminho, como na [`handoff`](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff); e o "completo" é o da [`create-prd`](https://github.com/phuryn/pm-skills/tree/main/pm-execution/skills/create-prd).
- **O estacionamento da Etapa 3 é consolidado sem repetição, com todas as origens e o motivo copiado, e as saídas ideais viram a régua do MVP.** Motivo: o item sem motivo é desfeito sem saber ([Jansen e Bosch, 2005](https://doi.org/10.1109/WICSA.2005.61)), e a Etapa 3 mede o MVP contra o ideal, e não contra o que for mais fácil.
- **O pronto é por evidência, item por item, e "não verificado" conta como falha; a vigia e a conferência das fichas rodam de novo no 6.5.** Motivo: o checklist cirúrgico reduziu as mortes quando foi feito ([Haynes et al., 2009](https://doi.org/10.1056/NEJMsa0810119)), e não quando só foi adotado ([Urbach et al., 2014](https://doi.org/10.1056/NEJMsa1308261)); evidência antes de afirmar, como na [`verification-before-completion`](https://github.com/obra/superpowers/tree/main/skills/verification-before-completion).
- **O 6.5 é a validação integrada do tema, sem conselho completo.** Motivo: o conselho completo já julgou o conceito no 5.5; o que o tema 6 valida é a fidelidade e a passagem, que o verificador, os leitores e o `pronto.py` medem item a item.
- **A trava vem antes da retrospectiva, e a retrospectiva não muda o CIR.** Motivo: ela mede o projeto fechado; se pudesse mudar o CIR, seria mais uma rodada, sem trava.
- **A retrospectiva usa só o que foi gravado antes, ou a reconstrução cega, marcada; separa a decisão do desfecho; e cada melhoria tem dono, skill e seção.** Motivo: depois do desfecho, tudo parece previsível ([Fischhoff, 1975](https://doi.org/10.1037/0096-1523.1.3.288)), e a decisão é julgada pelo resultado ([Baron e Hershey, 1988](https://doi.org/10.1037/0022-3514.54.4.569)); revisões com estrutura e registro melhoram o desempenho ([Tannenbaum e Cerasoli, 2013](https://doi.org/10.1177/0018720812448394); [Keiser e Arthur, 2021](https://doi.org/10.1037/apl0000821)); é o formato da [`think-after-action-review`](https://github.com/product-on-purpose/thinking-framework-skills/tree/main/skills/think-after-action-review).
- **O script é o `retrospectiva.py`, e não `retro.py`,** porque `retro.py` já é o detector de retrospectiva da `cir-prova`.
- **O `aprendizado.jsonl` guarda, de cada projeto real, só números e notas de método, e a condutora mostra no 4.4 a mediana, com o n; com menos de 3 projetos, os valores, e pergunta.** É a resposta ao ponto em aberto da [Plano detalhado — cir-divergencia](https://app.notion.com/p/Plano-detalhado-cir-divergencia-aa452eebec8044cb9c016a345ce0f1ff?pvs=21) sobre a taxa de surpresa entre projetos.
- **O espelho de leitura no Notion é só do CIR aprovado, só de leitura e só em projeto real.** É a resposta ao ponto em aberto da [Plano detalhado — etapa-1-cir (condutora)](https://app.notion.com/p/Plano-detalhado-etapa-1-cir-condutora-fccda0c36a5d403582b433a6f2b0657f?pvs=21) sobre o espelho de leitura; o CIR em construção fica fora, pelo risco de isolamento.
- **O `06-blocos.md` é separado do `06-cir.md`:** um é a fonte, e o outro é gerado; assim, nenhuma correção se perde na montagem seguinte.
- **Pelo critério máximo do [Plano geral das skills — Etapa 1 (CIR)](https://app.notion.com/p/Plano-geral-das-skills-Etapa-1-CIR-72d0fdc1db19433e9101d1ac3b3015ef?pvs=21), o custo é registrado e só desempata.**

**Em aberto:**

- **O gabarito do Motor para o tema 6 e a regra de correspondência:** são seus, escritos antes de qualquer execução: o que o CIR do Motor tem de dizer, o que o pacote tem de trazer e quais lacunas a auditoria do documento tem de achar.
- **Os alvos que dependem da linha de base da fase 2:** a distribuição das afirmações por tema, os falsos alarmes dos leitores e a calibração, pela pontuação de Brier.