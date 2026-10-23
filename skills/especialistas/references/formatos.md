# Formatos e interface local

Entradas JSON explícitas, sem varrer dossiê ou salvar arquivos implicitamente.
Comandos devolvem JSON em stdout; a condutora ou curador persiste a saída.
Os [schemas](../assets/schemas/ficha.schema.json) documentam a estrutura;
as verificações entre arquivos e formações são feitas pelas CLIs.

## Mapa, catálogo e modelos

Veja [mapa](../assets/modelos/mapa.json), [catálogo vazio](../assets/modelos/catalogo.json)
e [modelos não configurados](../assets/modelos/modelos.json).

Mapa versão 1 tem itens (ID, tipo causa/contradicao/parte/job, texto, central e
principio), especialidades (ID, descrição funcional, cobre, por_que, fontes,
esp ou lacuna). `esp: null` não exclui a disciplina da cobertura. Fontes são
referências fornecidas, cuja pertinência e verificação são externas.

No mapa 2.7, declare etapa, dose, recrutadores, geradores_distantes, fusao e
temas com equipe_base/reserva por IDs, critico e uma distante com função
análoga. `aprovacao: {aprovada, decisao}` registra a decisão da pessoa; sem
ela a formação pode estar estruturalmente válida, mas não executável.
Preferências, propostas independentes e composição de conselhos são
conteúdo do mapa humano; as contagens não demonstram que essas sessões ocorreram.

Catálogo: schema_version e especialidades com ID `esp-*`, versao, tag,
commit completo, hash SHA-256, escopo, modulos, situacao, valida_ate,
modelos_testados e errata. Situações: em_teste/em_uso/em_revisao/bloqueada/
aposentada. Só em_uso e em_revisao geram blocos; em_revisao exige errata com
ID, texto, fonte e data. O placar pode ficar no catálogo completo, mas a
projeção de recrutamento não o transmite nem o usa.

Modelo por papel tem id, nome escolhido, familia anthropic e verificado
booleano. Falso permite preparar fichas, mantendo `executavel: false`.
Nunca transforme exemplos de nomes em disponibilidade de provedor.

## Fichas e formações

Veja [rascunho de ficha](../assets/modelos/ficha.json). `novo` copia ve/nao_ve
e modelo; não aceita alterá-los. `validar` recebe objeto com formacao,
fichas e itens_exigidos do cartão. Ficha: contexto, papel, nome funcional,
especialidade, esp `{id,versao,hash}` ou null com lacuna, modulos, escola
opcional `{nome,obras}`, distante, funcao_analoga, cobre, por_que, fontes,
ferramentas, sessao e campos copiados. Geradores têm operadores/semente;
conselheiros, template/otica dados pelo conselho. Campos desconhecidos são erro.

Repetição de especialidade requer escolas diferentes e motivo_escola;
geradores nunca repetem especialidade. Fora do mapa requer excecao_mapa com
aprovada e decisao. Verificação exige sessoes_produtoras e recusa qualquer
coincidência. Conselho recebe oticas esperadas; esta skill não as inventa.

`sortear` recebe fichas de geradores, operadores e semente inteira. Ordena
o conjunto antes do sorteio, sem repetição, e devolve fichas atualizadas.
A semente torna a distribuição repetível; não é prova de cegueira.

## Biblioteca Git e hashes

A tag precisa resolver ao commit declarado. Leitura usa objetos do commit,
não o arquivo de trabalho. Hash da biblioteca é SHA-256 da concatenação,
na ordem SKILL e módulos do catálogo, de cada `caminho + NUL + tamanho em
bytes decimal + NUL + bytes`. Inclui o cabeçalho original do SKILL. O curador
calcula esse hash ao registrar a versão; auditoria recusa qualquer divergência.

O bloco usa o corpo inteiro sem cabeçalho e os módulos selecionados na ordem
do catálogo, sem reescrever, mais errata. Hash_conteudo sela nome/versão e
payload exato, sem incluir a própria linha de selo; hash_transporte sela os
bytes finais do bloco. São hashes distintos da biblioteca e aparecem na saída.
A ficha aponta para o hash da biblioteca; a entrega começa pelo selo do bloco.

`selo` reconstrói o bloco esperado, confere a primeira linha literal da
entrega e, com recebido, compara o bloco inteiro no topo da mensagem. Não
compara só a presença do hash; texto reescrito com hash copiado é detectado.
Errata muda o hash do bloco; tag movida ou conteúdo adulterado bloqueiam.

## Lacunas e admissão

Fila é lista JSON; modelos em [primeira leva](../assets/modelos/primeira-leva.json).
Cada lacuna tem ID estável, especialidade, para_que, pedidos por projeto/
subetapa/ficha, central_ou_principio, gabarito, situacao e registrada_em.
`novo` agrega pedidos sem duplicar; `situacao` atualiza com motivo e, se
entrou, esp/versao/teste. Isso registra decisão externa, não publica a esp.

Teste recebe problemas (ID, enunciado, escopo dentro/fora, variante_nova,
fonte_gabarito, gabarito), modelos_papeis, modelo_menor, tipo nova/revisao e
resultados por modelo/problema/condicao/execucao/acerto. Acerto é percentual
0–100. Rubrica exige dois IDs de avaliadores e `cego: true` por resultado.

Execução opt-in recebe config com comando em lista, autorizado, timeout e
bloco. Adaptador lê JSON pelo stdin (modelo, problema, enunciado, material,
execucao) e devolve `{modelo, modelo_verificado: true, resposta}`. Nunca
recebe gabarito. Só gabaritos `igual` com valor ou `numero` com min/max rodam
automaticamente; rubricas e revisão de versões usam resultados externos.
O pacote não implementa autenticação, seleção de provedor ou sessões Claude.

## Persistência e adaptação

Mapa humano: `especialistas.md`; fichas: `fichas/<subetapa>-p<passo>.md`.
O [modelo Markdown](../assets/modelos/especialistas.md) tem equipes-base,
conselhos, preferências, lacunas e registro da fusão/decisão. O protocolo
exige essas seções; o mapa JSON é só a projeção usada pelas verificações.
Biblioteca e testes fechados ficam em repositórios separados do projeto.
Notion recebe o brief como primeira mensagem de sessão filha isolada;
Claude Code recebe texto na delegação. Esses adaptadores precisam de teste
de transporte, contexto, ferramentas e permissões antes de uso real.
