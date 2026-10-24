# Cartões operacionais do tema 2

Base: S15 §5, detalhamento de S08 tema 2. Sem trava formal; decisão continua humana.

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
