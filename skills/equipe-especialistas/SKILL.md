---
name: equipe-especialistas
description: >-
  Conduz reuniões de especialistas com preparação individual, informação
  compartilhada por inteiro, falas em ordem, crítico separado e síntese que
  preserva contribuições e dissenso. Modos: elaboração, verificação técnica,
  integração, individual, fusão de paralelas e avulso. Use quando a condutora
  pedir reunião nos passos 7/8 ou fechamento do tema, ou quando a pessoa
  quiser que especialistas discutam e elaborem juntos. Não use para votar,
  julgar hipóteses, recrutar, gerar alternativas cegas ou responder sozinho.
compatibility: Agente com sessões retomáveis ou recriadas com a ata; Python 3.10+ para apoio local. Claude, pesquisa e isolamento exigem adaptadores verificados.
metadata:
  version: "0.1.0-alpha.1"
  language: pt-BR
  status: alpha-local
---

# Equipe de especialistas

## Propósito e regras no topo

Junte especialidades numa versão melhor sem fazer média ou perder informação
única. Uma reunião que termina em acordo não prova ganho. Base: S14 §§1/7;
limites e atribuições em [origem](references/origem.md).

1. Cada especialista prepara sozinho, por escrito. Antes da primeira fala,
   todos recebem as preparações **inteiras**, sem resumo da mesa.
2. Dê código a cada contribuição. Nada desaparece: entrou, mudou, rejeitada
   com motivo ou em aberto. Preserve o melhor argumento de cada dissenso.
3. O líder abre com mapa, sem preferência: convergências, divergências,
   informação única, perguntas dirigidas e o que ninguém cobriu.
4. Rodada 1: um ou dois fatos novos e motivo contra a proposta à frente.
   Depois, só novidade ou “passo”. Motivo antes da posição; honestidade
   mesmo contra todos, sem pedido de coesão ou oposição de fachada.
5. Autoridade na área só com `esp-*` ou fonte conferida. Para contrariá-la,
   traga fonte, conta ou contraexemplo; a evidência vence especialidade e memória.
6. O crítico fala por último e diz o que conferiu. “Nada a apontar” vale;
   não precisa inventar objeção. Mudança de posição cita a fala e o motivo.
7. O líder fecha cada rodada sem conteúdo novo. Depois, posições finais
   individuais, sem ver as outras. A síntese pode contrariar a maioria com lastro.
8. Contas em Python e refeitas; fonte nova fica a conferir. Material que
   não confere não sustenta decisão. A conta certa não valida o modelo científico.
9. Sem rodada extra. Impasse vira opções/dissenso e o que decidiria entre elas.
   Parada antecipada a partir da segunda, todos passando, crítico sem ponto aberto.
10. A equipe não julga hipóteses nem decide pela pessoa. Verificação entrega
    conclusões técnicas; integração relata conflitos. Conselho julga depois.
11. Sem autoria, identidade de modelo, dossiê ou casos reservados nos membros.
    Use nomes funcionais e blocos de especialidade recebidos do recrutamento.
12. A mesa transporta sem editar falas. Vazamento suspende; preserve registro
    privado, substitua sessão e repita rodada. Só a condutora persiste no dossiê.

## Quem lê o quê

- Mesa: este arquivo, [mesa](references/mesa.md), [modos](references/modos.md)
  e a referência de [Notion](references/ambiente-notion.md) ou
  [Claude Code](references/ambiente-claude-code.md).
- Líder: [lider](references/lider.md) e o modelo da saída, enviados no brief.
- Especialista: seu bloco inteiro, [especialista](references/especialista.md),
  material autorizado e tarefa. Não abrir workspace para carregar a skill.
- Crítico: [critico](references/critico.md), pauta, preparações, ata e checagens.

## Preparar

Receba pauta, pergunta, decisão técnica, formato da `cir-*`, validação posterior,
refuta_se, restrições, versão base sem autoria, dose e limite de rodadas.
Recrutamento e blocos vêm de `especialistas`; não os crie durante a reunião.
Leia [formatos](references/formatos.md) e [protocolo](references/protocolo.md).

Confirme modelo Claude escolhido para equipes, sessões isoladas e pesquisa.
Líder não fica abaixo dos especialistas, crítico usa o modelo do líder.
Não invente disponibilidade ou execução. Sem essas capacidades, prepare
artefatos e marque dependências; `executavel: false` não é reunião realizada.

## Modos

| Modo | Organização | Entrega |
| --- | --- | --- |
| Elaboração | Padrão: líder, três especialistas, crítico, duas rodadas. Completa: até três rodadas; distante a partir do quarto membro; centrais pedem duas/três paralelas e fusão. | Síntese como hipótese sem autoria para o passo 8. |
| Verificação | Completa, dois/três especialistas em sessões não produtoras, líder/crítico, uma/duas rodadas. | Parecer por afirmação: sustenta, não sustenta ou indeterminado; nunca veredito. |
| Integração | Equipe-base e saídas aprovadas; uma rodada, segunda só com conflito bloqueante. | Conflitos, combinações e dependências; gravidade, evidência e o que resolveria, sem decidir. |
| Individual | Um especialista e crítico; até duas revisões/respostas. | Entrega revista, sem simular uma discussão coletiva. |
| Fusão | Líder novo, sínteses A/B/C sorteadas sem atas/identidades, crítico. | Partes com origem; fora com motivo; opções ou contraprova para conflitos. |
| Avulso | Mesma elaboração padrão, fora do dossiê. | Ata e síntese na pasta escolhida pelo operador. |

Leve: um especialista prepara variações sozinho, **sem reunião**. Não iniciar
mesa de elaboração leve. O modo individual com crítico serve outra tarefa focada.

## Conduzir com a mesa

1. Valide pauta; confira fichas/blocos e inicialize formação, siglas e ordem
   sorteada por rodada com semente. As sessões/modelos ficam no estado privado.
2. Dispare as tarefas de preparação em paralelo. Confira selo/códigos e preserve
   textos literais. Timeout: uma repetição; só abra com ao menos dois especialistas
   e crítico disponível. Formação insuficiente volta à condutora.
3. Líder faz o mapa. Entregue preparações inteiras e abertura aos membros.
4. Passe a palavra na ordem sorteada, um por vez; depois crítico, líder e
   checagens. Registre sem editar. Não avance fora de fase ou sobre revisão obsoleta.
5. Após as rodadas, recolha posições finais em paralelo, sem revelar as outras.
6. Valide saída e lastro. Crítico revisa uma vez a versão atual; líder responde
   a cada ponto, aceitando ou mantendo com motivo. Não invente aprovação humana.
7. Devolva pacote externo para `equipe/<reuniao>/`, custos e placar, mais resumo
   de cerca de 300 palavras. A condutora grava; perguntas à pessoa ficam na saída.

## Auxiliares locais

Os comandos usam JSON explícito e devolvem JSON em stdout, sem gravação no dossiê.
Não redirecione estado para o mesmo arquivo de entrada. Escreva outro arquivo
e deixe a condutora integrar atomicamente. Código 1 indica reprovação/erro.

```bash
python3 -B scripts/pauta.py montar pauta.json
python3 -B scripts/mesa.py iniciar inicio.json
python3 -B scripts/mesa.py tarefas estado.json --transporte retomar
python3 -B scripts/mesa.py registrar estado.json --evento evento.json --revisao 0
python3 -B scripts/ata.py contas contas.json
python3 -B scripts/ata.py fontes fontes-novas.json
python3 -B scripts/sintese.py saida.json --estado estado.json
python3 -B scripts/parecer.py parecer.json --estado estado.json
python3 -B scripts/fusao.py preparar paralelas.json
python3 -B scripts/fusao.py validar fusao.json --brief brief-publico.json
python3 -B scripts/custos.py estado.json
python3 -B scripts/mesa.py entregar estado.json
```

Sem pesquisa instalada, `ata.py fontes` devolve não conferida. Adaptador externo
autorizado chama os verificadores reais; não imite pesquisa com dublê. Contas
aceitam só Python matemático restrito, descrito em formatos, sem código arbitrário.

## Limites de evidência

Estrutura, hash e selo não comprovam que a informação foi lida, que a fonte
sustenta a afirmação, que a analogia serve ou que houve isolamento. Revise
semântica, transporte e eventos reais. Compare equipe ao melhor isolado e a
isolados com síntese, às cegas: onde não ganhar, use o mais simples. Não
trate os alvos numéricos do plano como resultados desta implementação.
