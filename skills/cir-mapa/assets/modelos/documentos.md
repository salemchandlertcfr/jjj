# Modelos editoriais (fictícios)

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
