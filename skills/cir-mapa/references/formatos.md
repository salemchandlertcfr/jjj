# Formatos locais v1 e contrato de retorno

Os auxiliares recebem um objeto JSON `schema_version: 1`, ou Markdown com
exatamente um bloco iniciado por ` ```json cir-mapa-v1 ` (sem os espaços externos).
O bloco é a representação canônica verificável do documento. A prosa editorial,
inclusive discordâncias e comentários fora dele, exige revisão: não se afirma
que uma validação do JSON abrange todo o Markdown. Nenhum comando grava no dossiê.
O modelo editorial da seção 8 de S15 está em
[documentos](../assets/modelos/documentos.md); o modelo de dados preenchível está
em [mapa](../assets/modelos/mapa.json) e o banco em [casos](../assets/modelos/casos.json).
Ambos são exercícios fictícios de interface, nunca evidência científica.

## Fontes comuns aos objetos de mapa e banco

`fontes` é lista de `{id, referencia, trecho, afirmacao, data, conferida}`.
Data usa `YYYY-MM-DD`, `conferida` é booleano. IDs são únicos, com letras,
dígitos, ponto, hífen ou underscore. Uma citação admitida precisa apontar para
ficha conferida; a conferência ainda depende de pesquisa e crítico reais.
Não há consulta automática de URL/DOI nem juízo automático de suporte semântico.

## Mapa

`job` é texto; os demais campos abaixo são listas, salvo projeção/contagens.
IDs de etapas, falhas, causas, contradições, K e partes não podem colidir.

| Campo | Conteúdo |
| --- | --- |
| `etapas` | `{id, categoria, texto, aplica, motivo?, executor, hoje, fontes, hipotese?}`. Oito categorias minúsculas: definir, localizar, preparar, confirmar, executar, monitorar, modificar, concluir. Não aplicável exige motivo. Sem fonte exige hipótese. |
| `passagens` | `{de, para, o_que_passa, o_que_se_perde}` com IDs das etapas. |
| `variacoes`, `gambiarras` | Listas editoriais preservadas; cobertura e pertinência são revisão semântica. |
| `falhas` | `{id, texto, central, etapas, partes, frequencia, gravidade, arvore}`. Frequência desconhecida é texto com plano de medição, sem valor inventado. |
| `arvore` | `{outras_causas, ramos:[{causa, tipo, outras_causas?, ramos?}]}`. `tipo` é unica/ramo. Todo nó interno tem outras_causas, com peso estimado ou desconhecimento. Sem ciclos; laços são separados. |
| `causas` | Cartão abaixo; duas origens diferentes por falha central. |
| `lacos` | `{nos:[IDs de falha/causa], sentido:reforco/equilibrio, fontes}`. |
| `contradicoes` | `{id, parametros:[A,B], forma_fisica, classe, busca_prova, busca_contraexemplo}`. Classes: principio, limite_hoje, quebravel. Buscas têm pesquisadores distintos. |
| `projecao` | `{sua_versao, classe_referencia, taxas_base, fontes, horizontes}`; exatamente dois prazos distintos. Cada horizonte: `{prazo, faixa, partes, ajuste_motivo}`. Faixas numéricas exigem fontes; o script só verifica estrutura. |
| `conhecimento` | `{id, texto, classe, se_falsa}`; sabido exige fontes e trecho literal presente na ficha; incerto exige resolveria e custo_investigar; impossivel_saber exige por_que e natureza aleatorio/inobservavel/escolhas_futuras. |
| `analogias` | `{id, funcao, mapeamento, distancia, fontes}`; próxima/moderada/distante sem acentos no JSON. |
| `partes` | `{id, texto}` recebidos do propósito; novos atores voltam à decisão humana. |
| `contagem_casos` | Objeto só com inteiros por tipo: comum, falha, sucesso, simetria, evidencia_contraria, nada_relevante. Nenhum conteúdo de caso. Simetria conta casos; pares são informados no relatório privado. |

Cartão de causa: `{id, texto, origem, falha, cadeia:[elos], previsoes:{se_verdadeira,
se_falsa}, pergunta_contra, busca:{favor,contra}, evidencias, forca, motivo_forca,
fontes_mecanismo, fontes_dependencia, tipo_dependencia, falha_igual_sem_causa,
observacao_faltante, mudaria_se, situacao, historico?}`. `situacao` é principal,
rival_viva ou pergunta. `origem` é privada, removida na projeção pública.

Evidência: `{texto, teste, lado, resultado, fontes}`. Testes: palha_ao_vento,
aro, arma_fumegante, duplamente_decisivo, nao_diagnostica. Lado: favor/contra/neutra;
resultado: passou/falhou/incerto. Força: forte/media/fraca/hipotese. Dependência:
controle/sem_controle/contexto_parecido/relatos; correlação isolada fica hipótese.
Nenhum cálculo de força por soma. `mapa.py` bloqueia força sem requisitos mínimos,
mas a avaliação real é da verificação e do conselho. Fraca pode ser classificação
conservadora; ter campos fortes não obriga a promovê-la.

Exceção de rivais é objeto na falha com registro, motivo, busca_rivais, dissenso
e observacao_que_resolveria; só vale para uma causa sustentada ou
`causa_desconhecida:true`. Esta última permite árvore sem ramos, mantendo
outras_causas à vista. Não invente árvore ou rivais para obter validação.

Contradição de princípio acrescenta lei, conta, fontes, parecer, conselho,
contraexemplo_valido:false e premissas não vazias `{texto,fontes,movel}`.
Limite de hoje acrescenta data e fontes. Quebrável com lei exige
premissa_que_falha; um contraexemplo fica na ficha, sem receita no desafio.

### Anterioridade auditável

Em cada causa, `historico:{pre_registro:<SHA completo>, busca:<SHA completo>,
arquivo:<caminho relativo no Git>}` aponta para dois commits distintos.
`mapa.py --git PASTA` exige ancestralidade, as mesmas previsões/cadeia/pergunta
contra nos dois snapshots e no cartão atual, evidências ausentes antes e iguais
depois, fichas da busca novas e presentes no segundo commit. Sem `--git`, o
relatório deixa a cronologia pendente. Isso verifica o histórico disponibilizado,
não prova que alguém desconhecia o desfecho nem autentica a origem de um commit.
Não reescreva história para fazer o teste passar.

## Banco privado

Campos: fontes, modelo_sonda, modelo_geradores e casos. Modelos precisam coincidir.
Cada caso: `{id,tipo,marcador,origem,data_corte,antes,desfecho,lado,dificuldade,
visto,depois_solucao,construido,conhecido_modelo,sonda,par?,relacao_esperada?}`.
Tipos e cotas estão em [casos](casos.md). Flags são booleanos; conhecido_modelo
aceita null para sonda pendente, impedindo reserva. Marcador único: `⟦c-123abc⟧`.
Antes é lista de `{texto,disponivel_em,fontes}`; desfecho é `{texto,data,fontes}`.
Data do desfecho posterior ao corte; fatos do antes não podem ser posteriores.
Detecção de cópia literal não detecta toda retrospectiva: crítico continua necessário.
Lado: bom/ruim/neutro. Simetria tem par e relação esperada; pelo menos um membro
do par é real. Um espelho construído nunca se apresenta como evento observado.

Sonda registra modelo, continuacao e acertos_nao_no_antes. Marca conhecido_modelo
deve corresponder aos acertos conferidos externamente; uma resposta errada não
prova ausência de memória. `sonda` produz apenas os fatos anteriores, sem fichas,
desfechos ou marcadores. O relatório da sonda e o banco são privados.

`sortear` retorna uma relação privada com semente e hash do banco. Pares ficam
juntos; reserva ao menos um grupo elegível por tipo, com alvo de aproximadamente
um terço adicional aos 10–20 de trabalho. Com banco pequeno ou já exposto, as
cotas podem ser incompatíveis: o comando bloqueia e pede mais casos em vez de
relaxar sigilo ou memória. Um banco válido na coleta não implica sorteio possível.
A condutora persiste uma vez em 3.6 e anexa a relação em `sorteio` ao banco;
o comando recusa banco já congelado. O script não autentica que a condutora
anexou o registro: controle de estado e acesso é responsabilidade da integração.

`--vazamento RAIZ` procura marcadores e trechos literais com pelo menos oito
palavras fora da pasta casos/ dessa raiz. Não imprime os trechos, só IDs/caminhos.
Audite todas as raízes de briefs e saídas; pasta não auditada não está verificada.
Symlinks/erros de leitura impedem um resultado limpo; paráfrases pedem auditoria humana.

## Pacote, inventário e cartões

Pacote e contraste usam exatamente schema_version mais sete campos de texto de
uma linha: job, falhas_centrais, causas, contradicoes, projecao, espaco_k, banco.
Limite 600 palavras no total; acima dele, redigir novamente sem truncamento.
O campo banco usa contagens normalizadas, nunca casos. `montar` projeta o mapa;
`conferir` aplica a mesma forma ao contraste, sem decidir vencedor. Revisar
anonimato semântico, informação omitida e causa desconhecida antes do envio.

Inventário devolve itens aceitos por cobertura.py (job/causa/contradicao/parte),
incluindo falhas centrais como causa com ID próprio, e peso por central/princípio.
Os incertos K ficam em lacunas_espaco_k: o contrato atual não tem tipo lacuna;
ligue-os aos itens e verifique que cada um recebeu especialidade. Não afirmar
cobertura total dessas perguntas pela mera aprovação do contrato antigo.

`cartoes.py` recebe uma lista (ou objeto subetapas) com id, titulo e dose.
Confere 2.1–2.7, campos, títulos e doses. O teste de desenvolvimento compara
também os cartões literais de S15 e IDs/títulos/doses de S08. O índice real da
condutora não está neste checkout: não substituí-lo por um índice inventado
para alegar integração. As mudanças deliberadas de S15 estão em origem.md.

Retorno à condutora: mapa, banco privado separado, inventário e relatórios de
validação, sinais, limites e pendências. Ela prepara o mapa `arquivos` de seu
envelope transacional. Estes auxiliares não implementam essa transação nem
escrevem `estado.json`; não se inventa o schema de um brief.py ausente.
