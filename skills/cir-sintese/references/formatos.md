# Contratos locais v1

S16 §§4/8/10. Interface explícita do alpha, sem presumir parser ou envelope da
condutora ausente. Python 3.10+, Git. JSON tem schema_version 1; Markdown
aceita exatamente uma projeção cercada por ` ```json cir-sintese-v1 ` (sem
espaços externos). A projeção é canônica para montar; prosa fora dela não é
validada como registro. O CIR gerado é comparado **inteiro** na conferência.
Não adicionar texto livre para contornar a projeção: primeiro registrar na origem.

## Origens e blocos

Registro de origem: `{schema_version:1,itens:[...]}`. Cada item tem id, tipo,
tema inteiro 0–6, subetapa, registro, texto literal e dados (objeto). Os tipos
aceitos estão em sintese_core.py: propósito, métrica, caso, dissenso etc.
Textos e dados são lidos do objeto Git; não se duplicam no manifesto.
O formato local exige registrar a projeção dos itens no arquivo de origem;
não inventa como extrair semanticamente um Markdown antigo.

Manifesto do 06-blocos.md: schema_version, commit_base completo, hashes_estado
(mapa caminho→SHA256 completo), escolha referencia|refutada|abstencao,
avisos_metodo, inventario, blocos, ligacoes e em_vez_disso. Todos os arquivos
de origem precisam constar nos hashes do estado e no commit base. Working tree
e objeto devem bater. Caminhos relativos regulares, sem links simbólicos ou `..`.

Inventario é a lista independente extraída dos registros, antes da montagem.
A CLI a compara aos itens completos de todos os arquivos de hashes_estado;
nessa interface, esses arquivos precisam conter a projeção de registros com itens.
Excluir o mesmo item de blocos e inventario também é bloqueado.
Cada entrada tem id e origem `{arquivo,commit,sha256,item}`. Blocos usam esse
mesmo formato, mais secao 1–17 e superado_por opcional. ID e item têm de coincidir;
fontes são ancestrais do commit base. Uma origem alterada exige registro/refresh
pela condutora, sem atualizar hashes em silêncio. Para histórico, preserve as
versões como itens distintos no registro atual; o antigo aponta ao sucessor.
Isso é mais restrito que aceitar qualquer trecho de um arquivo antigo.

Não confundir hash de arquivo, de bloco/manifesto e de afirmação. Git fornecido
e hashes não autenticam papéis ou quem conhecia o desfecho. A CLI não grava
06-blocos.md, estado.json, decisões ou o histórico; devolve mapas para a condutora.

## Ligações e tarefas

suas_versoes: essencia, o_que_nao_e, temor, sequencia inteira e hash, criado por
`cir.py suas-versoes`. Sequência tem de anteceder ligações; é registro declarativo,
sem prova de anterioridade externa. O temor também deve ser item do inventário.

Ligação: id `lig-*`, secao, texto, origens (IDs de blocos), sessao_redator,
sessao_decompositor distinta, sequencia, conclusao booleano e afirmacoes.
Afirmação: id, texto, inicio/fim (spans no texto original) e origens, subconjunto
das origens da ligação. Spans não se sobrepõem e cobrem todos os caracteres não
brancos: nenhuma frase fica fora. Atomicidade e exaustividade semântica dependem
do decompositor/critico reais. Uma conclusão por seção, antes das cópias.

`cir.py afirmacoes` retorna lotes sorteados ≤20, com id, afirmacao, hash e fontes
(texto/dados), sem identidade do redator. Mistura é aleatória; não promete
estratificação em cada lote. `redator --secao N` envia só blocos da seção;
1/14 também recebem CIR montado. Projeções não revogam acesso ao workspace:
a condutora precisa revisar identidade no conteúdo e configurar permissões.

Vereditos: `{schema_version:1,vereditos:[{id,hash,sessao,veredito,trecho}]}`.
Hash vem da tarefa (texto e fontes). Sessão diferente de redator/decompositor;
veredito sustentada|nao_sustentada|exagerada|contradiz; trecho presente na fonte.
Sem veredito é pendente; veredito antigo não vale após a correção. A declaração
não comprova modelo escolhido, independência ou suporte semântico.

Conferir também emite suspeitas numéricas/lexicais. Não apaga um sinal porque
um juiz disse sustentada: crítico deve resolver a suspeita. Qualificadores,
causas inventadas e probabilidade expressa por palavras podem escapar à triagem.
`usos` segue IDs/depende_de e busca literal, sem determinar mudanças de veredito.

## Pacote e estacionamento

Texto/dados vêm das origens ativas, no mesmo commit_base/hash_blocos do CIR.
Dados por tipo usados na Etapa 2:

- killer/pergunta/fronteira: acoes (texto das 3–5 ações iniciais já registradas);
  killer também teste_mais_barato.
- capacidade: metricas (IDs); metrica: linha_base, fonte, limite, todos explícitos.
- caso: saida `{arquivo,commit,sha256}`, verificada em objeto Git regular.
- fronteira: texto em forma de pergunta e respeita.
- pergunta: data_busca ISO e quem_responde.
- principio/restricao: refuta_se e onde_mora. em_vez_disso no manifesto cobre
  cada ID com texto, sessao_redator e verificacao `{hash,sessao,veredito,trecho}`.
  Hash = digest de `{texto,origem:<item inteiro>}`; veredito sustentada, sessão
  distinta, trecho presente no item de origem. Exige verificação semântica real.
- alternativa_viva: prova. refutada/descartada: refutou e desafio.
- qualquer registro pode justificar parte vazia com dados.ausencia_partes
  (números 1–9); o motivo será o texto literal desse registro.

Estacionamento: dados.tipo apelo|necessidade_vizinha|mercado|falha_mercado e motivo
literal. Junta duplicatas de texto/tipo, conservando todos os IDs/motivos.
Equivalência semântica e função perdida no propósito pedem guardião.

## Passagem

leitor.py previstas recebe schema_version/previstas [{id,texto}] e sela estado.
abrir recebe estado e --evento com cir e pacote (textos), gabarito (cinco trechos
literais), modelo_juiz, leitores e juizes. Leitor/juiz: id, sessao, modelo;
leitor também especialidade sistemas|dominio|generalista. Três leitores e dois
juízes, cinco sessões novas e nunca reutilizadas no histórico. Modelo é um
identificador escolhido, não prova de disponibilidade ou chamada Claude.

Fases: reformulacoes (três) → perguntas (três) → julgamentos (dois) → classificacao
(condutora). registrar recebe tipo, ator e conteudo. Cinco campos de reformulação:
proposito, nucleo_principios, o_que_nao_e, primeira_tarefa, bancada. Pergunta: id,
texto, modo deduzi|chutei|pergunta, apoio literal quando inferiu/chutou e
muda_primeira_decisao booleano. Juiz recebe rótulos R1–R3, por campo veredito
bate|diverge|incompleta e trecho do gabarito. Não recebe perguntas ou previstas.

Classificação por ID: classe central|secundaria, quem dossie|usuario|ninguem_sabe,
destino; se muda campo protegido, registro_volta é obrigatório. prevista opcional
aponta ao ID anterior. Evento também leva comparacao_leituras {conferida:true,
divergencias:[]}; a comparação semântica entre leitores é externa e explícita.
Nada fecha com central, campo divergente/incompleto ou ambiguidade declarada.
Quarta e seguintes: autorizacao com resposta sim, registro e rodada exata.
Invalidar conserva rodada contaminada; ela não conta como passagem concluída.

## Pronto, aprovação e retrospectiva

assets/pronto.yaml é JSON válido (subconjunto YAML) com os 14 itens/requisitos.
Entrada do pronto tem escolha referencia|refutada|abstencao, artefatos caminho→hash
(CIR, estacionamento e, salvo abstenção, pacote Markdown e JSON), itens com id I1–I14, evidencia_id
e evidencia {arquivo,commit,sha256,secao}. Arquivo da evidência é projeção v1 com
evidencias [{id,item,secao,trecho,responsavel,hash_artefatos,resultado,verificacoes,
quantidade?}]. Hash_artefatos = digest do mapa artefatos. Evidência de outra seção,
critério ou versão falha. Requisitos são declarações estruturadas; o crítico
confere se provam de fato o item. Quantidades mínimas: I4/I10 três, I11 dez.

conferencia_fontes: hash_artefatos, executada, todas_citadas, pendentes; esse
relato externo não é pesquisa executada pela CLI. Pendencias: lista de destino
volta|ressalva, registro, motivo, objetivo. Triagem lexical roda nos artefatos
inteiros, inclusive aspas; pode sinalizar proibições legítimas. Vigia/pendencias
reais da condutora continuam pendentes.

pronto.py RELATORIO --git RAIZ --aprovar CONSENTIMENTO valida o relatório selado,
resposta literal sim, commit com arquivos/hash atuais, registro/data ISO e
ressalvas (id,registro,motivo,objetivo). Não é autenticação do consentimento.
Só a condutora coleta o sim, grava a trava e apresenta a versão aprovada. Pular
I14 exige aviso no CIR/pacote pela apresentação da condutora, com o registro.
Os auxiliares geram versões NÃO APROVADAS e não publicam espelho Notion.

Retrospectiva recebe aprovacao selada, sua_avaliacao selada (funcionou,
nao_funcionou), comparacoes, melhorias, tangentes, projeto_real. Comparação tem
id, expectativa {tipo registrada, texto, origem Git} e commit_desfecho posterior,
ou tipo reconstrucao, texto, cega_declarada:true, sessao; tem ainda
qualidade_decisao boa|ruim|indeterminada, base_na_epoca e desfecho. É declaração
separada; o script não deduz a qualidade do resultado. Melhoria: id, dono, skill,
secao, acao específica, origem. Tangentes: classificadas e com_funcao.

Brier usa previsoes_conselho/usuario [{probabilidade,desfecho bool,
referencia_desfecho}]; faltante fica fora, sem inventar observação factual.
Em real, hash_projeto opaco, data e metodo só com fracao_tangentes_4_4,
taxa_4_10, doses, passagem e voltas. Subcampos são fechados e valores numéricos;
notas_metodo só códigos da lista do script, sem prosa de domínio. Em teste não
retorna linha de aprendizado. --mediana recebe projetos, mostra valores com
n<3, mediana com n≥3; não altera fração/dose automaticamente. Nenhuma CLI persiste.
