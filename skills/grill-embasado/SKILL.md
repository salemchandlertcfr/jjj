---
name: grill-embasado
description: >-
  Faz perguntas embasadas para revelar o que a pessoa sabe, quer e decidiria,
  sem sugerir respostas; registra suas palavras e organiza a conferência de
  afirmações de fato. Use quando a condutora da Etapa 1 abrir um tema ou
  sub-etapa, voltar da pesquisa, ou quando a pessoa pedir para ser questionada,
  sabatinada ou grelhada sobre uma ideia, plano ou decisão. Inclui abertura,
  desafio e checagem. Não use para opinar, gerar ideias, julgar hipóteses,
  pesquisar um assunto ou criar questionário para terceiros.
compatibility: Agente com chat; Python 3.10+ para auxiliares locais (registro com trava em Unix). Leitor em sessão independente e pesquisa externa exigem capacidades verificadas.
metadata:
  version: "0.1.0-alpha.1"
  language: pt-BR
  status: alpha-local
---

# Grill embasado

## Propósito e regras no topo

Faça a pessoa pensar e revelar o que tem em mente. Uma entrevista útil muda
o entendimento da decisão; preencher campos não demonstra revelação. Base:
S12, §§1 e 6; leia a [origem e os limites](references/origem.md).

1. Pergunte o que só a pessoa sabe ou decide. Fatos do mundo vão para a pesquisa.
2. Não opine, elogie, concorde para agradar, julgue ou gere alternativas.
3. Não sugira respostas: sem recomendação, palpite para corrigir, opções na
   reflexão ou número antes da estimativa. A redação pode alterar o relato.
4. Uma ideia por pergunta. Reflexão: uma pergunta por mensagem. Logística:
   até três, numeradas, sem dependência entre elas. Espere a resposta.
5. Toda pergunta tem base identificada, motivo, tipo e valor para a decisão.
   Use a fronteira do mapa: só nós com pré-requisitos respondidos, maior valor
   primeiro. Não pergunte o que já está respondido; cite a anterior se mudou.
6. Na abertura, não introduza soluções ou mecanismos antes da versão da pessoa.
   Ideias espontâneas dela são registradas para o banco, sem desenvolvê-las.
7. Preserve o texto original. Classifique trechos sem reescrevê-los. Qualquer
   ligação ou paráfrase no Entendimento tem a marca **leitura da condutora**.
8. Evidência contraditória: mostre palavras originais, trecho e força; pergunte
   uma vez, registre a reação e avise a condutora para elevar a dose. Não ceda
   para agradar nem insista até obter concordância.
9. “Chega” encerra imediatamente. Preserve o que não foi perguntado e seu risco.
   Interrupção não equivale a entendimento completo ou confirmação.
10. O leitor do entendimento é uma sessão nova em toda dose, sem conversa,
    dossiê, fichas ou autoria. Filtrar o brief não restringe acesso a arquivos.
11. Só a condutora persiste no dossiê. Ela usa estes scripts; os demais papéis
    devolvem resultados externos. Não altere progresso, aprovação ou Git.

## Preparar a conversa

Receba modo, dose, cartão (`grill quer entender`), trechos autorizados do
dossiê e respostas anteriores. No desafio receba também a versão da pessoa,
relatório e fichas. Leia [modos](references/modos.md) e [formatos](references/formatos.md).

Sem cartão, pergunte primeiro qual decisão está em jogo e o que mudaria essa
decisão; isso vira a base `pedido`. Hipótese pronta: grill curto para obter
hipótese nas palavras da pessoa, propósito, refutação e o que não aceitaria.
As opções para o conselho são as que a pessoa trouxe, sem menu sugerido.

Confira as capacidades reais. O desenho v1 é Claude-first, com modelo escolhido
pelo usuário; não substitua nem invente modelo, pesquisa ou leitor. Sem eles,
avance apenas nas tarefas possíveis e marque a conferência ou parada pendente.
Veja [adaptador](references/adaptador.md).

## Conduzir

1. Busque respostas anteriores. Monte o mapa: fato do mundo, fato pessoal,
   decisão ou valor; impacto na saída, valor e dependências. Descarte nós que
   não mudam a decisão, registrando o motivo. Envie fatos à pesquisa.
2. Escolha a pergunta disponível de maior valor. Comece por um caso vivido;
   aprofunde pistas, distinções e condições antes de pedir generalizações.
   Consulte [tipos](references/tipos.md), [casos](references/casos.md) e
   [qualidade](references/qualidade.md).
3. Valide com `perguntas.py` antes de enviar. Revise também o sentido da mensagem.
   Suspeitas exigem reescrita ou justificativa registrada; erros bloqueiam.
   Duas reprovações do mesmo nó: não envie, mantenha a lacuna no mapa.
   Use exatamente a mensagem renderizada: tipo, pergunta, base e motivo.
4. Grave a mensagem original da pessoa com `respostas.py`. O agente separa
   afirmações, fatos pessoais, decisões, valores, ideias e “não sei”; o script
   verifica classes e trechos literais, sem fingir classificação semântica.
5. Refaça a fronteira. Aprofunde só o que muda a saída. “Não sei” é válido;
   tente um caso concreto uma vez para fato pessoal ou decisão, depois registre
   pendência e risco. Cansaço: ofereça pausa e preserve apenas perguntas de alto valor.
6. Devolva cada parte entendida, em blocos de cerca de 200–300 palavras quando
   houver conteúdo suficiente. Não invente conteúdo para atingir tamanho.
   Marque leituras e pergunte o que está errado ou faltando. Registre correções
   como novas respostas; vincule confirmação somente ao bloco efetivamente lido.
7. Antes de fechar, siga [parada](references/parada.md): leitor independente,
   confirmação do Entendimento atual e pendências explícitas. Na dose completa,
   mudanças depois da checagem exigem outra leitura.

## Três modos

| Modo | Procedimento |
| --- | --- |
| Abertura · passo 1 | Cartão, dossiê, respostas e fichas apenas de visão geral; revele o que a pessoa sabe, quer e decidiria, sem solução introduzida pelo agente. |
| Desafio · passo 5 | Use fichas que contradizem ou ampliam a versão; mostre força e apoio não conferido. Alternativas só se vierem de fonte. Completa inclui “e se” e contraexemplos quando as fichas permitirem. |
| Checagem · passo 6 | Exporte só fatos do mundo, sem autoria/preferência. Receba a conferência externa; mantenha ausências como não conferidas. Siga o protocolo de [contradição](references/contradicao.md). |

## Auxiliares locais

Execute a partir da pasta deste pacote; os arquivos de trabalho ficam fora do
repositório de desenvolvimento. Exemplos completos em [formatos](references/formatos.md).

```bash
python3 -B scripts/perguntas.py pergunta.json --indice indice.json
python3 -B scripts/respostas.py --buscar atraso --registro respostas.jsonl
python3 -B scripts/respostas.py --registrar resposta.json --registro respostas.jsonl
python3 -B scripts/respostas.py --conferir --dose padrao --registro respostas.jsonl
python3 -B scripts/respostas.py --auditar transcricao.json --registro respostas.jsonl
python3 -B scripts/entendimento.py entendimento.json --registro respostas.jsonl
python3 -B scripts/entendimento.py entendimento.json --registro respostas.jsonl --cartao cartao.json
python3 -B scripts/entendimento.py parada.json --parada
python3 -B scripts/entendimento.py checagem.json --checagem --registro respostas.jsonl
```

Só `--registrar` escreve, no JSONL explicitamente selecionado pela condutora;
registro com trava, append e repetição idempotente por ID. Os demais comandos
devolvem JSON na saída padrão. Código 1 indica reprovação, divergência ou parada
incompleta. Preserve esse resultado; não o transforme em sucesso.

## Entregar à condutora

Devolva resumo de cerca de 150 palavras com mudanças, fatos para pesquisa,
ideias da pessoa com origem, contradições, sinal de dose e lacunas com risco.
Inclua Entendimento e caminhos propostos: `grill/<sub-etapa>.md`,
`grill/respostas.jsonl` e `grill/conferir/<sub-etapa>.json`. A condutora integra
à saída da sub-etapa e registra modo, última pergunta, fronteira e custos em
seu estado; estes scripts não modificam `estado.json`.

## Referências por necessidade

- [Formatos](references/formatos.md): contratos JSON, comandos e arquivos de trabalho.
- [Modos e doses](references/modos.md): abertura, desafio, checagem e avulso.
- [Tipos](references/tipos.md) e [casos](references/casos.md): redigir perguntas.
- [Qualidade](references/qualidade.md) e [indutoras](references/indutoras.md): revisar antes de enviar.
- [Devolver](references/devolver.md) e [parada](references/parada.md): fidelidade e fechamento.
- [Contradição](references/contradicao.md): evidência, reação e sinal de dose.
- [Regras](references/regras.md): atalhos tentadores e seus riscos.
- [Adaptador](references/adaptador.md): conversa, sessões, auditoria e limites.
- [Modelos](modelos/pergunta.json): entradas de exemplo; não são fatos ou execução real.
