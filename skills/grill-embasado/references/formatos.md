# Contratos locais e comandos

Todos os caminhos de entrada são explícitos. A condutora prepara os arquivos;
nenhum script percorre o dossiê. Saída JSON em stdout; código 1 em reprovação.
Python 3.10+ e biblioteca padrão. JSON usa códigos sem acento; texto fica intacto.

## Perguntas e mapa

Veja [pergunta.json](../modelos/pergunta.json). Envelope: `schema_version: 1`,
`modo`, `dose`, `objetivo`, `bases`, `perguntas` e `mapa`. Modos: abertura,
desafio, checagem. Doses: leve, padrao, completa.

Base tem `id`, `tipo`, `origem` e `texto` autorizado. Tipos: cartao, dossie,
resposta, ficha, pedido. Tipo ficha exige índice separado: objeto por ID,
`valida: true`, `trecho` que contém a base, `forca` inteira de 1–5,
`apoio: conferido|nao conferido`, `visao_geral: true` para abertura. Isso
confere consistência com o índice recebido, não verifica a fonte na web.

Pergunta tem ID, `texto`, `tipo` (oito códigos), `genero: reflexao|logistica`,
`base` (IDs), `motivo`, `valor: alto|medio|baixo`, `no` e `estimativa` booleana.
`tentativas_reprovadas` registra o número anterior. `anteriores` traz IDs e
textos de perguntas já respondidas; repetição exige `retoma` e `motivo_retomada`.
O histórico depende da seleção honesta pela condutora, não de detecção semântica.

Mapa: lista de nós com ID, `classe: fato do mundo|fato pessoal|decisao|valor`,
`estado: pendente|respondido|descartado`, `valor`, `impacto`, `depende_de` e,
no descarte, `motivo`. `valor: nulo` não entra na fronteira. Não omita nós
importantes para passar na parada. Rode `perguntas.py mapa.json --fronteira`.

A saída contém `aprovada`, `erros`, `suspeitas`, `pendentes` e `mensagem`.
Envie só a mensagem aprovada; `mensagem` fornecida na entrada deve ser idêntica
à renderizada. Suspeitas podem ser justificadas por ID em `justificativas`.

## Respostas

Veja [resposta.json](../modelos/resposta.json). ID de resposta é diferente do
ID da pergunta e do ID estável da mensagem na transcrição. Timestamp ISO com
fuso obrigatório. `texto` não é limpo nem reescrito. `afirmacoes` têm ID,
`trecho` literal, `classe`, `central` opcional e `fichas` opcionais. `ideias`
têm trecho literal. `nao_sei` é explícito. O agente faz a classificação;
o script não infere intenção por palavras-chave.

Correção: novo ID, `substitui` apontando para resposta vigente anterior da
mesma pergunta/sub-etapa e `usos_anteriores` listando onde a antiga foi usada.
Os IDs de afirmação também são novos. Histórico não é removido. Exportação
e Entendimento usam versões vigentes; busca inclui o histórico.

`--registrar` faz append com trava de arquivo em Unix e permissão inicial 0600;
repetir o mesmo ID e conteúdo não duplica. Conteúdo diferente com o mesmo ID
é erro. O diretório precisa existir; nenhuma pasta de dossiê é criada.

`--auditar` recebe lista JSON de `{id, papel: usuario, texto}` e compara texto
exato por `mensagem_id`. O resultado lista IDs divergentes sem imprimir as
mensagens da transcrição. A autenticidade da exportação é externa ao script.

`--conferir` exporta só fatos vigentes da sub-etapa selecionada: ID da
afirmação, texto e fichas, sem resposta inteira ou autoria. Leve seleciona
centrais e marca o restante não conferido. Padrão/completa incluem todos.

## Entendimento, leitor e parada

Veja [entendimento.json](../modelos/entendimento.json). Cada item tem
`rotulo`, `texto`, `leitura` booleana e `origens`: tipo resposta/dossie, ID e
trecho. Fonte de dossiê precisa estar em `trechos_dossie` (ID e texto), já
filtrada. Paráfrases só com `leitura: true`. Saída: Markdown e hash canônico.

Com `--cartao`, gera brief só com os quatro campos do cartão de
[cartao.json](../modelos/cartao.json), Entendimento e instrução de leitura.
Não inclui respostas nem chaves extras do cartão. O conteúdo textual ainda
precisa de revisão de sigilo, pelo agente.

Veja [parada.json](../modelos/parada.json). Requer dose, mapa, `nao_perguntado`
(IDs, motivo e risco), `motivo: sem valor|chega`, hash atual, confirmação da
pessoa (`confirmado`, hash, `resposta_id`) e resultado do leitor (`concluido`,
hash, `sessao`, `modelo_verificado`, perguntas com texto/classe/impacto).
Declare `sessao_condutora`; perguntas do leitor já resolvidas trazem
`resolvida: true`. Encaminhamento factual usa `pesquisa_encaminhada: true`.
São evidências fornecidas pelo hospedeiro, não autenticação ou auditoria real.

## Checagem

Veja [checagem.json](../modelos/checagem.json). `conferencias` é lista por ID
de afirmação, `resultado` e evidências com ficha/trecho/forca. `eventos` é
histórico completo das perguntas de contradição: ID, afirmação, palavras
originais, evidências mostradas, desfecho e motivo quando houver. Duplicação
de afirmação nos eventos é erro. Não crie um novo ID para insistir.

As entradas não recebem caminhos implícitos; os exemplos são dados fictícios,
nunca uma conferência científica real ou confirmação fornecida por usuário.
