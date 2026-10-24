---
name: cir-mapa
description: >-
  Método do tema 2 (Mapa) da Etapa 1 do IDEAL: job map, falhas e causas
  rivais com evidência, contradições, projeção de referência, espaço K,
  banco de casos e especialidades. Use quando a condutora abrir o tema 2
  ou 2.1 a 2.7, ou para mapear um job, investigar causas de uma falha de
  um fenômeno ou classificar trade-offs fora da Etapa 1. Não use para
  pesquisa de mercado, preço, concorrência, validação comercial,
  depurar um incidente técnico, revisão de literatura avulsa ou gerar soluções.
compatibility: Agente com chat; Python 3.10+ e Git para auxiliares. Pesquisa e sessões independentes exigem capacidades verificadas no hospedeiro.
metadata:
  version: "0.1.0-alpha.1"
  language: pt-BR
  status: alpha-local
---

# Entender o fenômeno antes de conceber a solução

Entenda onde e por que o job falha, diferencie conhecimento e incerteza,
reúna casos antes da solução e identifique quem precisa pensar o problema.
O mapa alimenta métricas e RFI no tema 3, desafios no tema 4, prova no tema 5
e as seções 3, 5, 12 e 15 do CIR. Não é catálogo de problemas para justificar
uma ideia pronta. Base metodológica: S02 §7, S08 tema 2, S09 passo 2 e S15.

## Responsabilidades e limites reais

No fluxo, a condutora conversa com a pessoa e é a única a ler/gravar o dossiê.
Esta skill entrega cartões e método; não abre agentes, não escolhe causas pelo
usuário, não inventa fontes, não aprova o tema e não altera estado.json.
Os scripts recebem arquivos selecionados explicitamente e retornam stdout.
O hospedeiro deve impor permissões: filtrar um brief não revoga acesso a arquivos.

O perfil de execução do plano é Claude-first: modelo por papel escolhido em 0.3,
sessões independentes e não produtoras para verificação/conselho. Sonda usa o
modelo dos geradores do tema 4. Não substitua execução ausente por falas simuladas.
Este pacote é universal; não inclui Claude, pesquisa, condutora ou as genéricas.
Antes de uma execução real, confirme capacidades, modelo, autorização e isolamento.
Dependência ausente devolve trabalho parcial e bloqueio preciso, sem parecer falso.

## Antes de começar

Leia os [cartões](references/cartoes.md) e a referência da sub-etapa. Receba
propósito congelado, job e variações, partes/valores, material do tema 0 e mapa
inicial de especialidades, por brief filtrado. Não procure o dossiê por conta própria.
A declaração de propósito aprovada é pré-requisito do tema 2, sem presumir aprovação.

Na abertura, a condutora pergunta o que a pessoa sabe do fenômeno, onde o job
falha, em que fontes confia e quais casos viveu. Preço, mercado, disposição a
pagar e concorrência ficam na Etapa 3. Produto existente só entra como modo atual
de executar uma etapa, com fonte e falha. Leia [fenômeno](references/fenomeno.md).

A versão da pessoa vem primeiro em cada peça. Não mostre exemplos ou a lista
pronta antes dela; categorias entram depois, como teste de completude. Marque
origem “sua”, “IA” ou “sua depois de ver a IA”, na memória privada da condutora.
Solução incidental vai ao banco, tecnologia às fronteiras e negócio ao estacionamento.

## Conduzir o tema

Releia o cartão antes de cada passo. Preserve o ciclo: grill; versão da pessoa;
triagem conforme cartão; pesquisa; perguntas embasadas; conferência; elaboração
e alternativas cegas; verificação e conselho; escolha humana; registro com
opções, evidência, dissenso, confiança e condição de reversão. Não confunda
conformidade de estrutura com decisão humana ou conhecimento demonstrado.

| Peça | Referência e exigência central |
| --- | --- |
| 2.1 Job map · padrão | [Job map](references/job-map.md): oito categorias; verbo/objeto sem meio; modo de hoje com fonte ou hipótese; passagens, variações, gambiarras e decomposição cega. Categoria inaplicável exige motivo. |
| 2.2 Falhas e causas · completa | [Causas](references/causas.md): árvores com “outras causas” em cada nó; rivais de origens diferentes; previsões antes da busca; pesquisadores a favor/contra separados; verificação e conselho completo Evidência. |
| 2.3 Contradições · completa | [Contradições](references/contradicoes.md): par de parâmetros e ligação física; triagem de princípio, prova/contraexemplo separados, parecer e conselho completo com refutador de limites teóricos. |
| 2.4 Projeção · padrão | [Projeção](references/projecao.md): versão da pessoa; visão de fora sem ver ideia/projeção; taxas-base com fonte; ajustes justificados; dois horizontes e faixas por parte. |
| 2.5 Espaço K · completa | [Espaço K](references/espaco-k.md): sabido com trecho, incerto com teste/custo, impossível de saber com motivo; analogia por função e distância. Sem geradores. |
| 2.6 Casos · completa | [Casos](references/casos.md): 15–30 candidatos, cotas e ambos os lados; antes separado do desfecho; sonda; guarda e sorteio somente em 3.6. |
| 2.7 Especialidades · padrão | Use especialistas: dois recrutadores, fusão e distante; inventário desta skill alimenta cobertura. Não gere esp-* de memória. |

A integração em equipe acontece depois da 2.6 e antes da 2.7. No fechamento,
conselho completo Evidência examina pacote e 1–2 diagnósticos de contraste cegos,
sem vencedor. Diferenças voltam como perguntas. Veja [integração](references/integracao.md).
O tema não tem trava formal, mas a pessoa decide e a condutora registra o fechamento.
“Causa desconhecida”, com observação que a resolveria, é resposta legítima.

## Invariantes que protegem o diagnóstico

- Correlação isolada é hipótese. Força pede mecanismo e dependência, com fontes.
  Evidências ficam em linhas, tipadas; não some contagens ou pesos para confirmar.
- “Erro humano” não encerra cadeia. Cinco porquês só dentro de um ramo; registre
  lacunas, laços e outras causas. Rivais precisam ser mecanismos distintos, não negações.
- Toda falha central pede duas causas de origens diferentes. Se as rivais foram
  buscadas e nenhuma se sustenta, registre exceção, dissenso e o que resolveria;
  não fabrique uma rival para preencher o campo.
- “De princípio” exige lei/teorema, premissas e conta. Vale enquanto as premissas
  valerem; folga até o limite pode ser quebrável. “Ninguém conseguiu” é limite atual.
- Não resolva contradições aqui. O contraexemplo fica na ficha; o desafio do 4.2
  recebe apenas o par e as premissas móveis, sem a solução que geraria fixação.
- O banco fechado não entra no mapa: só contagens por tipo. Caso usado como
  evidência ganha marca “visto”. Expostos, conhecidos do modelo, pós-solução ou
  sem sonda concluída não vão para os reservados.
- O sorteio mantém pares juntos e é registrado uma vez no 3.6. Não sorteie de novo
  ao adicionar casos; depois do congelamento, marque os novos “depois da solução”.
- Dados de usuários precisam ser reais. Opinião de um agente em persona não vira
  dado. Sem entrevistas, use pesquisa e [roteiro de observação](references/dados-de-usuarios.md).

## Quem recebe o quê

A condutora monta cada brief, sem distribuir a skill inteira a trabalhadores.
Leia [geradores](references/geradores.md) antes de montar tarefas; sorteie operadores
sem repetição e registre semente na memória privada. Cada gerador entrega várias
opções, inclusive improváveis, probabilidade declarada e o que não sabe.

| Papel | Contexto permitido |
| --- | --- |
| Decomposição | Job e variações; sem mapa, versão da pessoa ou fichas. |
| Rivais | Job, mapa sem fontes, falha e operador; sem árvores/causas já propostas. |
| Contradições | Job, mapa, falhas/causas e valores; sem listas rivais/autoria. |
| Visão de fora | Fenômeno, job, partes; sem ideia, projeção ou restante do mapa. |
| Sonda | Só o antes e corte de cada caso; nunca desfecho nem banco completo. |
| Contraste | Fenômeno, job e partes; nada do tema 2. Mesmo formato/limite do pacote. |
| Verificação | Afirmações técnicas sem autoria; nunca julga nem escolhe causas. |
| Conselho | Critérios prévios, hipóteses anônimas, parecer, fichas autorizadas; sem autoria. |

Candidatos só podem entrar em briefs de coleta/validação 2.6 e sorteio 3.6.
Mesmo nesses passos, a sonda recebe somente a projeção antes/desfecho filtrada.
Marcador fora de casos/ exige suspensão e auditoria pela condutora; não copie o
conteúdo vazado no alerta. Teste ferramentas/permissões, não apenas o texto do brief.

## Apoio local e interfaces

Leia [formatos](references/formatos.md) antes de preencher os modelos. Os auxiliares
validam JSON v1 ou um bloco canônico dentro do Markdown; prosa livre não recebe
selo automático de validação. Campos editoriais e conteúdo científico precisam
ser revisados pelo crítico. Use `--help` no caminho efetivo da instalação.

```bash
python3 -B <skill>/scripts/mapa.py 02-mapa.md --git <checkout-do-dossie>
python3 -B <skill>/scripts/mapa.py 02-mapa.md --mermaid
python3 -B <skill>/scripts/sinais.py texto.md --peca causa
python3 -B <skill>/scripts/casos.py validar candidatos.md
python3 -B <skill>/scripts/casos.py sonda candidatos.md
python3 -B <skill>/scripts/casos.py sortear candidatos.md --etapa 3.6 --semente 42
python3 -B <skill>/scripts/casos.py validar candidatos.md --vazamento <raiz-dos-briefs-e-saidas>
python3 -B <skill>/scripts/pacote.py montar 02-mapa.md
python3 -B <skill>/scripts/pacote.py conferir contraste.json
python3 -B <skill>/scripts/inventario.py 02-mapa.md
python3 -B <skill>/scripts/cartoes.py --indice <subetapas.json-da-condutora>
```

`sinais.py` apenas alerta, nunca bloqueia. Validação estrutural inválida retorna
código 1; sem `--git`, a cronologia aparece pendente. O histórico prova ordem de
snapshots, não que o autor ainda desconhecia o resultado. Não declare verificação
integral enquanto ela estiver pendente. Não há integração automática com brief.py
ou vigia: isso exige a condutora completa e testes no hospedeiro.

`inventario.py` mantém lacunas K separadas porque o contrato atual de cobertura
aceita apenas causa/contradição/parte/job. Ligá-las aos itens exige revisão; não
as descarte nem as declare cobertas por um tipo inventado.

## Modo avulso e encerramento

Fora da Etapa 1, use apenas 2.1–2.3 em dose leve/padrão: grill curto, versão da
pessoa, mapa/causas/rivais, contradições e sinais. Conselho somente a pedido.
Use pasta própria `mapas/<data>-<assunto>/` com Git; não crie CIR nem banco de casos.
No fluxo, retorne arquivos e pendências à condutora. Mapa, banco e autoria têm
visibilidades diferentes; não entregue um pacote único a todos os papéis.

Mudança de job, parte ou propósito volta à pessoa para decidir reabertura do tema 1.
Revisões de causas/contradições propagam conforme [integração](references/integracao.md).
Não reabra, congele ou avance o método automaticamente.

Consulte [regras](references/regras.md), [perguntas de grill](references/grill.md),
[exemplos](references/exemplos.md), [modelos editoriais](assets/modelos/documentos.md)
e [origem e limites](references/origem.md) conforme a tarefa. Exemplos da skill são
fictícios e separados dos casos de avaliação; não são pesquisa já realizada.
