---
name: conselho-especialistas
description: >-
  Julga hipóteses, decisões e documentos às cegas, por critérios prévios e
  pesquisa de refutação, com membros independentes, crítico separado e
  dissenso preservado. Use quando a condutora pedir triagem, validação ou
  validação integrada, ou quando o usuário pedir conselho para avaliar,
  testar ou tentar derrubar uma ideia. Não use para gerar ideias, elaborar
  uma versão, resumir opiniões, fazer brainstorm ou decidir pelo usuário.
compatibility: Agente com sessões independentes e pesquisa verificável; Python 3.10+ e Git para apoio local. Adaptadores de plataforma exigem integração verificada.
metadata:
  version: "0.1.0-alpha.1"
  language: pt-BR
  status: alpha-local
---

# Conselho de especialistas

## Propósito e regras no topo

Melhore ideias e decisões tentando refutar hipóteses com independência e
evidência. Mostre onde resistem, onde falham e por que há dissenso; o usuário
decide. O valor está no exame, não no preenchimento dos artefatos. Leia
[propósito](references/proposito.md) ao começar ou rever o desenho.

1. **Não decida nem recomende.** Sem votos, soma, média, ranking ou vencedor.
   Preserve o melhor argumento de cada posição, inclusive a minoritária.
2. **Critérios antes.** Exija critérios com `refuta_se`, fixados antes de os
   membros receberem as hipóteses. Não invente critérios para salvar um brief.
   Hash e declaração de data não provam sozinhos a cronologia.
3. **Rodada 1 independente.** Cada membro recebe só seu brief e fontes
   autorizadas, em ordem sorteada, sem autoria, preferência, identidades dos
   modelos, outros vereditos ou acesso ao dossiê. Sessão nova não prova isolamento.
4. **Quem produziu não julga.** Exclua sessões produtoras; crítico e relator
   ficam fora dos membros julgadores. Audite ferramentas e acesso efetivo.
5. **Concordância não verifica.** `+` e `-` exigem fonte que sustente a afirmação
   ou raciocínio verificável; `?` é legítimo. Não fabrique pesquisas ou pareceres.
6. **Uma troca, só com motivo.** Divergência relevante e dose permissiva são
   pré-requisitos; mudar sinal exige evidência nova identificada.
7. **Claude primeiro.** Use o modelo de juiz escolhido pelo usuário e verificado
   no ambiente, igual em todos os membros e papéis de julgamento. Nenhum modelo
   mais leve substitui um juiz por conveniência. Veja [modelos](references/modelos.md).
8. **Só a condutora persiste no dossiê.** Prepare e devolva um pacote externo;
   autoria, mapa de modelos e semente ficam privados. Não abra o dossiê para membros.
9. **Declare limites reais.** Scripts verificam estrutura, não verdade científica,
   isolamento nem neutralidade semântica. Dependência ausente é lacuna ou bloqueio.

## Antes de executar

Identifique pergunta, tipo de conselho, template, dose, critérios prévios,
hipóteses anônimas, fichas conferidas, parecer quando exigido e restrições.
Receba da condutora apenas o necessário; não procure contexto no dossiê.

Leia [formatos](references/formatos.md), [conselhos](references/conselhos.md)
e somente o [template aplicável](#mapa-das-referências). Verifique modelo real,
via de transporte, sessões independentes, pesquisa e auditoria antes de chamar.
As outras onze skills da família não estão incluídas neste pacote.

`pesquisa-cientifica` é uma dependência planejada. Uma execução real pode usar
busca e leitura web do hospedeiro, com capacidade explicitamente verificada e
procedimento manual documentado de refutar/conferir. Sem pesquisa necessária,
preserve o passo e devolva o bloqueio. Fichas fixas e sessões simuladas são
dublês exclusivos de avaliação; nunca constituem conselho real validado.

Pedido avulso: fixe com o usuário pergunta e critérios antes da avaliação;
se faltar critério, peça-o sem sugerir um critério sob medida para as opções.
Use pasta própria nova com Git, `conselhos/<data>-<assunto>/`. Não crie um CIR
nem assuma a escrita do dossiê da condutora. Preserve a limitação de cronologia
se as opções já tiverem sido expostas. Não declare retroativamente cegamento.

## Roteiro

Siga o [protocolo](references/protocolo.md); os scripts são apoio determinístico.
Consulte a interface real antes do uso, por exemplo:

```bash
python3 <raiz-da-skill>/scripts/valida_brief.py --help
python3 <raiz-da-skill>/scripts/painel.py --help
python3 <raiz-da-skill>/scripts/paralelo_cli.py --help
```

Substitua `<raiz-da-skill>` pelo caminho instalado. Não adivinhe flags.

1. **Conferir entrada.** `valida_brief.py` confere estrutura e marcas de autoria.
   Devolva faltas à condutora. Ela guarda a chave produzida por `anonimiza.py`.
2. **Preparar painel.** `painel.py` usa template, dose, restrições e mapa privado;
   `sorteio.py` e `briefs_membros.py` distribuem ordens e subconjuntos. Para mais
   de seis hipóteses, exija cobertura e sobreposição visíveis. Registre ausências.
3. **Normalizar na dose completa.** Sessão separada, sem autoria, uniformiza
   a forma. A condutora confere fidelidade antes do envio; não altere conteúdo.
4. **Rodada 1.** Dispare membros independentes em paralelo ou lotes auditáveis.
   Cada um refuta e entrega o [veredito](references/membro.md). Repetição de
   transporte: no máximo uma; troca de modelo só pela política autorizada.
5. **Conferir e criticar.** `valida_veredito.py` confere o formato; peça uma
   correção, depois invalide. O [crítico](references/critico.md) confere lastro,
   método e vazamento em sessão própria. Sem crítica real, não declare validação.
6. **Detectar divergência.** `divergencia.py` registra `+` versus `-` decisivos,
   falha fatal, maioria `?` ou lastro decisivo derrubado. Não observado não é acordo.
7. **Trocar se permitido.** Envie argumentos anônimos e crítica aos mesmos
   membros, uma única vez. Exija evidência nova para toda mudança de sinal.
8. **Consolidar.** `matriz.py` preserva sinais e argumentos. No rápido, copie
   literalmente os argumentos; no completo, um [relator](references/relator.md)
   real e separado redige síntese neutra. `sintese_check.py` confere referências
   ao dissenso; a leitura independente verifica fidelidade e ausência de recomendação.
9. **Devolver.** Atualize [placar](references/placar.md) e custos no pacote externo.
   Entregue à condutora matriz, síntese, crítica, vereditos, fichas novas, faltas,
   limites de capacidade e caminhos, com resumo de cerca de 300 palavras.

Em triagem, procure só falha fatal: não descarte hipóteses. Uma falha fatal
isolada passa pelo crítico e, nas doses padrão/completa, por segundo refutador
independente de outra ótica antes de chegar ao usuário.

## Encerrar ou devolver bloqueado

Confira entregas previstas ou faltas explícitas, crítica real, matriz e síntese,
chave fora dos briefs e placar atualizado. Diferencie pacote estruturalmente
válido, exame parcial e conselho concluído. Guarde trabalho válido quando houver
falha; devolva o próximo passo concreto. Não avance aprovação da Etapa 1.

Se persistir divergência, mostre o que falta pesquisar ou testar. Não force
consenso nem gere alternativas para resolver o impasse. Ideia incidental de
membro retorna ao banco pela condutora, com origem `conselho`, sem virar avaliação.

## Mapa das referências

| Necessidade | Leia |
| --- | --- |
| Entender o porquê antes do processo | [Propósito](references/proposito.md) |
| Executar rodadas, tratar falhas e entregar | [Protocolo](references/protocolo.md) |
| Compor por tipo e dose | [Conselhos](references/conselhos.md) |
| Aplicar método de cada ótica | [Óticas](references/oticas.md) |
| Instruir sessões cegas | [Membro](references/membro.md), [crítico](references/critico.md), [relator](references/relator.md) |
| Rever invariantes e racionalizações | [Regras](references/regras.md) |
| Trocar artefatos e consultar modelos preenchíveis | [Formatos](references/formatos.md) |
| Registrar previsão e desfecho | [Placar](references/placar.md) |
| Escolher e verificar mapa real | [Modelos](references/modelos.md) |
| Integrar plataforma, sem presumir instalação | [Notion](references/adaptador-notion.md), [Claude Code/CLI](references/adaptador-claude-code.md) |
| Conferir base, atribuição e limites | [Origem](references/origem.md) |

Templates: [Propósito](references/templates/proposito.md),
[Evidência](references/templates/evidencia.md),
[Idealidade](references/templates/idealidade.md),
[Diversidade](references/templates/diversidade.md),
[Elementos](references/templates/elementos.md),
[Arquitetura](references/templates/arquitetura.md),
[Prova](references/templates/prova.md),
[Passagem](references/templates/passagem.md),
[Sob demanda](references/templates/sob-demanda.md).
