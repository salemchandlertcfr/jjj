# Cartões do tema 6

S16 §5, transcrição do contrato selecionado.

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
