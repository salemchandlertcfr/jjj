---
name: cir-sintese
description: >-
  Método do tema 6 da Etapa 1 do IDEAL, sub-etapas 6.1 a 6.6: monta o CIR
  com 17 seções a partir de registros, preserva cópias e dissenso, confere
  ligações por afirmação, gera pacote da Etapa 2 e estacionamento da Etapa 3,
  testa passagem com leitores novos, verifica pronto por evidência e prepara
  retrospectiva após aprovação. Use para fechar/remontar o CIR, rastrear uma
  frase, montar a passagem, auditar prontidão ou testar entendimento sem contexto.
  Não escolhe conceito, muda propósito/métrica/núcleo, define tecnologia ou preço.
compatibility: Python 3.10+, Git e dossiê autorizado para os auxiliares locais. Sessões Claude e pesquisa exigem hospedeiro verificado.
metadata:
  version: 0.1.0-alpha.1
  language: pt-BR
  status: alpha-local
---

# Síntese do CIR

## Propósito e fronteira

Consolide o que o dossiê demonstra, sem perder nem inventar. A escolha veio do
5.7; aqui se documenta, confere e entrega. A aprovação pertence à pessoa.
Base: S16 §§1/6/7; [origem e limites](references/origem.md).

O CIR é montado; redatores só escrevem ligações. Cada frase tem origem.
O que obriga ou promete vai por cópia, com hash, inclusive o dissenso inteiro.
Corrigir é mudar a origem, registrar pela skill dona e remontar. Nunca edite
`06-cir.md` para contornar a conferência. O pacote usa as mesmas fontes.

## Entrada e quem lê

A condutora lê esta skill e os [cartões](references/cartoes.md). Receba decisão
5.7, hashes dos temas, blocos e inventário dos registros, banco, fronteiras,
estacionamento, casos, saídas, fontes, Entendimento, placar e estado.
Carregue no 6.1 no lugar da cir-prova, respeitando três skills ativas.
Antes disso, a condutora usa só os formatos de [construção](references/construcao.md).

Confira modelo de trabalho e modelo de juiz escolhidos no 0.3. Redator,
decompositor e reconstrutor usam trabalho; verificador, leitores e juízes usam
juiz, em sessões novas. Esta skill prepara tarefas; não abre agentes.
Sem dependência real, marque pendente e prepare o artefato possível.

Agentes recebem só o brief, não a skill ou o dossiê. Veja
[visibilidade](references/agentes.md) e [formatos locais](references/formatos.md).
Isolamento e modelo efetivo exigem auditoria do hospedeiro; JSON não os garante.

## Percurso do tema

1. **6.1 — montar e conferir.** Confirme hashes antes de ler. Pergunte temor,
   essência e “o que não é” antes dos redatores e grave com hash.
   Monte as 17 seções das origens Git; seção vazia é pendência, não invenção.
   Famílias que perderam ficam na 6, fora das 7–10; superados vão à 17.
   [Montagem](references/montagem.md), [ligações](references/ligacoes.md).
2. Um redator por seção recebe só seus blocos/fontes e esp do tema. Escreve
   conclusão primeiro e ligações com IDs. Seções 1 e 14 vêm por último, vendo
   o CIR, sem as versões da pessoa. Mostre as duas lado a lado para escolha.
   A escolhida, venha de quem vier, também passa pela conferência.
3. Outro decompositor divide cada ligação em afirmações. Verificador vê só
   afirmação e fontes citadas, sem autoria: sustentada, não sustentada,
   exagerada ou contradiz, com trecho. Todas são conferidas, não amostra.
   Sorteie lotes de até 20, preferindo misturar seções. Crítico lê o conjunto
   depois, procurando contradição, conclusão sem apoio e distribuição torta.
   [Conferência](references/conferencia.md).
4. **6.2 — pacote.** Gere nove partes das mesmas fontes, na mesma versão.
   Capacidade aponta às métricas com base/limite. Princípio/restrição leva
   refuta_se e “em vez disso”, escrito e conferido separadamente. Parte vazia
   pede motivo registrado. Conselho rápido Passagem ensaia a primeira decisão,
   guardião confere propósito, pesquisa confere perguntas abertas.
   [Pacote](references/pacote.md).
5. **6.3 — estacionamento.** Consolide por tipo, preservando todas as origens
   e os motivos literais. Saídas ideais são régua do MVP. Guardião procura
   função do propósito estacionada; refutador confere motivo/proveniência.
   [Etapa 3](references/etapa3.md).
6. **6.4 — passagem.** Grave perguntas previstas antes, sem repassá-las.
   Três leitores novos recebem só CIR/pacote e hashes; reformulam propósito,
   núcleo/princípios, exclusões, primeira tarefa e bancada **antes** de perguntar.
   Registrem deduzi/chutei e frase de apoio. Dois juízes recebem reformulações
   anônimas e gabarito extraído dos documentos, sem perguntas/previstas.
   Divergência entre juízes ou leituras pede correção; leitor não preenche lacuna.
   [Passagem](references/passagem.md).
7. Condutora e crítico classificam cada pergunta, responsável e destino.
   Central muda primeira decisão, propósito ou núcleo. Responda pela origem;
   só a pessoa responde o que só ela sabe; ninguém sabe vai à seção 15, com
   responsável e prazo. Nova rodada com leitores novos até zero centrais e
   reformulações batendo. Até três rodadas; extra só com “sim” registrado.
   Vazamento invalida a rodada. Pular teste exige risco/ressalva I14 e aviso
   “aprovado sem teste de passagem”, nunca um passe fictício.
8. **6.5 — pronto.** Cada um dos 14 itens exige arquivo, seção, ID e hash.
   Não verificado conta como falha. Reexecute vigia nos três documentos,
   pendências e todas as fontes (C-6.5); não reutilize memória de checagem.
   Cada pendência volta ou tem ressalva da pessoa, motivo e objetivo.
   [Pronto](references/pronto.md).
9. **6.6 — trava, depois retrospectiva.** Mostre commit, itens, ressalvas,
   perguntas abertas e o que reverteria. Só “sim” explícito para esse commit
   aprova. Antes da retrospectiva, grave a avaliação da pessoa. Compare o
   previsto antes com o acontecido; reconstrução cega é marcada como tal.
   Qualidade da decisão é separada do desfecho. Melhoria tem dono, skill e
   seção; aplicar mudanças nas skills é outra decisão fora do projeto.
   [Retrospectiva](references/retrospectiva.md).

## Regras de parada e voltas

Número, qualificador, escopo e confiança são os da origem; confiança traz base
numérica. Sem sustentação volta ao redator; contradição sai e vai à pessoa.
Cobertura inclui todos os registros exigidos, temor e ao menos dez casos.
Lista lexical só aponta suspeitas: semântica e omissões sutis pedem verificador.

Mudou propósito, núcleo, princípio, restrição ou escolha? É volta à skill dona,
com prova do que a pede, nunca esclarecimento cosmético. `cir.py usos` ajuda
achar dependentes; não decide sozinho quais vereditos mudariam.
Mudou núcleo/pacote: repita passagem; só número sem efeito na decisão, histórico,
estacionamento ou ficha pode pedir apenas remontagem e conferência.
Veja [voltas e auditoria](references/voltas.md) e [regras](references/regras.md).

Abstenção documenta tentativas e refutações, sem conceito nas seções 7–10 nem
pacote da Etapa 2. Escolha de refutada mantém a refutação e o motivo literal.
Não transforme uma escolha humana em evidência de que a hipótese resistiu.

## Auxiliares locais

Leem entradas explícitas e retornam JSON em stdout. Só a condutora persiste
os mapas `arquivos`; nenhuma CLI escreve no dossiê, publica Notion ou chama Claude.
Leia o contrato local de projeção JSON em Markdown antes de converter registros.
Não afirmar integração com `registrar.py`, `brief.py` ou `vigia.py` ausentes.

```bash
python3 -B scripts/cir.py montar 06-blocos.md --git /pasta/dossie
python3 -B scripts/cir.py conferir 06-blocos.md --git /pasta/dossie --documento 06-cir.md --vereditos vereditos.json
python3 -B scripts/cir.py afirmacoes 06-blocos.md --git /pasta/dossie --semente 31
python3 -B scripts/cir.py usos 06-blocos.md --git /pasta/dossie --termo P1
python3 -B scripts/cir.py redator 06-blocos.md --git /pasta/dossie --secao 3
python3 -B scripts/pacote.py etapa2 06-blocos.md --git /pasta/dossie
python3 -B scripts/pacote.py etapa3 06-blocos.md --git /pasta/dossie
python3 -B scripts/leitor.py previstas previstas.json
python3 -B scripts/pronto.py evidencias.json --git /pasta/dossie
python3 -B scripts/pronto.py conceito.md --auditoria
python3 -B scripts/cir.py conferir conceito.md --sem-dossie
python3 -B scripts/retrospectiva.py retrospectiva.json --git /pasta/dossie
python3 -B scripts/retrospectiva.py projetos.json --mediana
python3 -B scripts/cartoes.py --indice indice-da-condutora.json
```

Projeto de teste não gera aprendizado nem espelho. Em real aprovado, aprendizado
transporta só números e códigos de método, nunca conteúdo; a condutora persiste.
Espelho é oferta depois do sim, só de leitura, ligado ao commit aprovado.

## Avaliar com honestidade

Testes locais verificam mecanismos. Não comprovam sessão Claude, isolamento,
verdade científica ou entendimento humano. O aceite do Motor e o gabarito são
da pessoa, escritos antes. Alvos S16 §13 dependem de ensaios reais; não declarar
18/20 infidelidades ou zero centrais sem executar e registrar os testes.
Exemplos de uso em [exemplos](references/exemplos.md); perguntas em [grill](references/grill.md).
