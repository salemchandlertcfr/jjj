# Contratos JSON e persistência

Todos os arquivos de trabalho são explícitos; nenhuma CLI percorre o dossiê
ou grava nele. Use Python 3.10+. Schemas documentais em
[assets/schemas](../assets/schemas/pauta.schema.json); validações entre eventos
e arquivos são feitas pelos scripts, não só pelo schema.

## Inicialização

[inicio.json](../assets/modelos/inicio.json) contém pauta, membros, semente,
fontes autorizadas e, na verificação, sessoes_produtoras. Dados do exemplo
são fictícios; modelo não configurado mantém `executavel: false`.

Pauta: schema_version 1, id/subetapa/modo/dose, pergunta, decidir (lista),
formato_entrega, validacao_depois, refuta_se, restricoes, versao_base sem
autoria e rodadas. Completa central declara paralelas 2 ou 3; integração tem
saidas_aprovadas com ID/texto/aprovada/decisao; verificação tem afirmações
com ID/texto. Marcadores de auditoria são privados, omitidos do brief.

Membro é um recorte da ficha já validada em `especialistas`, com ID, nome,
sigla, ficha, papel (especialista/lider/critico), sessão e modelo. Modelo tem
id, familia anthropic, nivel ordinal escolhido e verificado booleano. Esse
nível compara o mapa escolhido; não é ranking de qualidade inferido pelo código.
Especialista traz especialidade, esp ou null, bloco/selo/hash_transporte,
fontes (IDs) e distante/funcao_analoga quando aplicável. Líder/crítico não
recebem bloco de especialidade. A mesa não revalida a biblioteca Git ou as
fichas completas: essa etapa continua com `especialistas`.

## Eventos e sequência

`mesa.py registrar` recebe estado e evento e devolve estado novo. Com
`--revisao N`, recusa versão obsoleta. Campos comuns: ID único, tipo, ator,
rodada (null fora das rodadas), texto original e métricas opcionais.
`tarefas` informa ator/tipo/rodada esperados; não os invente para pular passos.

- Preparação: leitura, posicao_inicial, critica_base, contribuicoes com
  ID da sigla, texto literal no original, por_que, muda e evidencias.
  Tipos: fonte/conta/esp com ID, ou geral com marca “conhecimento geral,
  sem fonte”. Perguntas, fontes_novas e nao_sei podem ser listas.
- Abertura: mapa com todos os códigos, divergencias por ID/texto/contribuicoes,
  unicas e o mapa em texto, sem preferência.
- Fala: selo na primeira linha, passo booleano; se não passar, motivo,
  posicao, referencias. Rodada inicial: fatos_novos (um/dois), contra_proposta.
  Mudança: porque/cita_fala. Contraria: contribuição e contraprova com
  tipo fonte/conta e ID conferido, ou contraexemplo textual.
  Depois da primeira rodada, fala sem passo declara fatos_novos não vazios;
  pertinência e novidade real exigem revisão semântica. Não redefinir
  contribuicoes fora da preparação: os códigos originais são preservados.
- Crítica: pontos com ID/texto, conferido (lista não vazia), abertos (IDs).
  “Nada a apontar” permite pontos vazios, com o que foi conferido.
- Fechamento: decisoes de todas as divergências com ID/situacao
  resolvida|aberta|opcoes, motivo e referencias anteriores. Parar antecipado
  exige rodada ≥2, todos passando e nenhum ponto aberto do crítico.
- Checagem: ator mesa e resultados com ID/confere booleano; vêm dos scripts
  ou da pesquisa real. Não são certificados assinados de execução.
- Posição: selo, apoio literal, evidencia_mais_forte, incerteza, mudaria_se,
  dissenso por ID/argumento/mudaria_se; mudança também tem porque/cita_fala.
- Saída: campo saida no formato do modo. Revisão: hash_saida da saída
  atual, pontos, conferido e abertos. Resposta: saída final e respostas por
  ID do ponto, acao aceito|mantido e motivo.

Individual: preparacao → critica_individual → checagem → replica_individual,
uma ou duas vezes. Réplica contém saída/destinos, respostas e encerrar
booleano. Não simular abertura/rodadas/posições de uma equipe inexistente.

## Saídas

Síntese: versao, por_que, mudancas, destinos por contribuição
(entrou/mudou/rejeitada/aberto e motivo), divergencias com situação e lastro
ou decidiria, dissenso com argumentos por ator, lacunas, perguntas_usuario,
do_lider (texto/marcado/lastro) e numeros quando houver.

Número: valor, lastro (IDs de fonte/conta conferidos) e motivo; se está entre
posições, entre_posicoes e justificacao evidencia|opcoes. Dígitos no corpo
da versão precisam dessa declaração. Valores por extenso e pertinência do
lastro exigem revisão semântica; regex não detecta toda média escondida.

Parecer: destinos/dissenso e afirmacoes cobrindo IDs prévios; cada uma tem
conclusao sustenta|nao_sustenta|indeterminado, justificativa, lastro, incerteza,
especialidade e mudaria_se. Integração: destinos/dissenso, conflitos por ID,
saidas de origem, texto, lastro, gravidade bloqueia|pede_ajuste|menor e
resolveria, mais combinam/dependencias. Sem decisão ou veredito da hipótese.

Fusão: `preparar` recebe pauta, duas/três sínteses com ID/partes/dissenso,
sessao_lider nova, sessoes_lideres e semente. Separe brief público e chave
privada. `validar` recebe brief público e saída: partes com texto/origens
(sintese A/B/C, parte e trecho literal), leitura marcada se parafraseou,
fora com motivos, dissenso e conflitos como opções/contraprova. Revisão tem
hash da saída sem campos revisao/respostas_critico; respostas a todos os
pontos precisam de motivo. Não envia atas ou modelos ao líder de fusão.

## Contas, fontes e custos

`ata.py contas` recebe lista de ID/codigo/resultado. Subconjunto: constantes
finitas, atribuições simples, + − × ÷ potência limitada, funções
ceil/floor/log/log10/sqrt/exp/sin/cos/abs/min/max/round, importações dessas
funções de math e um print final. Sem laços, strings, arquivos, rede,
atributos, imports reais ou execução irrestrita. Código não suportado ou
resultado divergente fica não conferido. Worker usa Python isolado, com
limites de tamanho/AST/magnitude/tempo.

`ata.py fontes` recebe lista ID/texto. Sem pesquisa, retorna não conferida.
Adaptador opcional autorizado tem comandos verificar e trecho por argumentos,
sem shell; cada wrapper chama os scripts reais da pesquisa, recebe a fonte
JSON via stdin e devolve ID/confere booleano. A interface nativa daqueles
scripts ainda precisa ser verificada; este pacote não os copia ou emula.

Métricas opcionais por evento: tokens, segundos, creditos, contexto_mesa_tokens.
Somar somente quando comparáveis. Campo ausente deixa total desconhecido,
com parcela conhecida separada. Contagem de eventos não é chamada de API;
não estimar tokens por caracteres ou créditos por sessão.

`entregar` gera mapa `arquivos` com pauta, estado, ata literal, preparações,
posições, saída, checagem, custos e placar. As projeções Markdown de pauta e
saída usam JSON legível; a condutora pode apresentá-las sem reescrever conteúdo.
Quarentena e modelos no estado são privados; nunca mandar o pacote inteiro
aos membros ou ao conselho. Só a síntese/parecer filtrado segue para julgamento.
