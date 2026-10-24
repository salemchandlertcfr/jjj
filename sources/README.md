# Fontes e proveniência

Catorze arquivos distintos fornecidos pelo usuário, recebidos em **22 e 23/10/2026**. Essas datas não estabelecem quando foram escritos. Os nomes foram simplificados para caminhos estáveis; os bytes foram preservados. O [manifesto](manifest.json) registra ID, nome recebido, caminho, tamanho e SHA-256. O anexo repetido `SKILL.md` é igual a S01 byte a byte; não recebeu outro ID. S14 veio em ZIP: o Markdown foi preservado sem alteração; nome/hash do contêiner e caminho interno também estão no manifesto.

| ID | Arquivo preservado | Uso na síntese e estado |
| --- | --- | --- |
| S01 | [skill-creator](originais/skill-creator.md) | Metodologia de criação e avaliação solicitada para o conselho. Confirmada como cópia exata da revisão oficial identificada abaixo; não é implementação das skills CIR. |
| S02 | [Plano geral das skills — CIR](originais/plano-geral-skills-cir.md) | Mapa da arquitetura de 13 skills, execução, persistência e roadmap. Planejamento. |
| S03 | [simulacao_etapa1.py](originais/simulacao_etapa1.py) | Único código do projeto recebido; experimento de brinquedo com NumPy, executado tecnicamente. |
| S04 | [Plano detalhado — conselho-especialistas](originais/plano-conselho-especialistas.md) | Versão histórica do conselho, preservada. Para a implementação atual, o usuário forneceu a revisão S11. |
| S05 | [Plano da skill — método IDEAL](originais/plano-skill-etapa1-ideal.md) | Histórico: a abertura declara a proposta de skill única substituída pelo plano geral CIR e fluxo completo. |
| S06 | [Método IDEAL — passo a passo](originais/metodo-ideal-passo-a-passo.md) | Resumo do método em cinco fases e nove passos. |
| S07 | [Fluxograma aperfeiçoado — CIR](originais/fluxograma-aperfeicoado-cir.md) | Razões e introdução do ciclo por tema, doses e formações. |
| S08 | [Fluxograma completo — IDEAL em ciclo](originais/fluxograma-completo-ideal.md) | Detalhamento operacional em 51 sub-etapas; amplia S07 com casos reservados e teste de passagem. |
| S09 | [Concepção Ideal da Solução — IDEAL v2](originais/concepcao-ideal-solucao.md) | Definição, fundamentos, CIR, pronto, hipóteses e limites. Identifica-se como versão para revisão. |
| S10 | [Plano detalhado — etapa-1-cir, condutora](originais/plano-etapa-1-cir-condutora.md) | Requisitos da primeira implementação: protocolo, dossiê, estados, briefs, registros, retomada e testes. Anexado após a documentação inicial. |
| S11 | [Plano revisado — conselho-especialistas](originais/plano-conselho-especialistas-revisado.md) | Base ativa da implementação do conselho, explicitamente selecionada no pedido. Adota Claude primeiro, com sessões e óticas independentes, e resolve a divergência de famílias de S04. |
| S12 | [Plano detalhado — grill-embasado](originais/plano-grill-embasado.md) | Selecionado pelo usuário para implementar perguntas embasadas, registro fiel, Entendimento e checagem. Integrações e metas conversacionais precisam de avaliação. |
| S13 | [Plano detalhado — especialistas](originais/plano-especialistas.md) | Selecionado para recrutamento, biblioteca, fichas e curadoria com teste de ganho. A primeira leva de `esp-*` é candidata, não conhecimento já admitido. |
| S14 | [Plano detalhado — equipe-especialistas](originais/plano-equipe-especialistas.md) | Selecionado para reuniões com preparação individual, crítico, síntese rastreável e dissenso; ganho de equipe e transporte real continuam a avaliar. |

## Como interpretar as fontes

S02 e S08 orientam a síntese da arquitetura e do fluxo; S06/S09 explicam o método; S10 especifica a condutora. Para o conselho, S11 é a revisão fornecida e selecionada pelo usuário para desenvolvimento; S04 fica como histórico. S12/S13/S14 foram selecionados para grill, especialistas e equipe. S05 tem substituição explícita. Não há precedência universal entre os demais documentos: detalhamento ou posição na lista de anexos não resolvem conflitos. As [decisões](../wiki/decisoes.md) e [pendências](../wiki/pendencias.md) registram esse tratamento. Escopos: [condutora](../wiki/implementacao-condutora.md), [conselho](../wiki/implementacao-conselho.md), [grill](../wiki/implementacao-grill.md), [especialistas](../wiki/implementacao-especialistas.md) e [equipe](../wiki/implementacao-equipe.md).

Links dos originais para páginas de Notion, outros planos ou estudos foram mantidos. O conteúdo de destinos não anexados não foi presumido como parte da análise. Alegações científicas e números citados nos planos não foram todos auditados externamente; a wiki evita promovê-los a resultados demonstrados deste projeto.

Os textos em `originais/` são material de referência. Sua preservação não ativa instruções nem instala recursos. S01 foi invocado para o desenvolvimento e orienta também o trabalho sequencial do grill, especialistas e equipe, com S12–S14 selecionados pelo usuário. Seus bytes foram comparados com o [skill-creator oficial da Anthropic](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator), revisão `dbd4588f9e1033efb41dad4bef2f7947c8993d44`, sob Apache 2.0. Auxiliares oficiais foram usados externamente para avaliações, sem vendorização. Essa atribuição não define a licença do projeto inteiro.

## Referências externas usadas na organização

Consultadas em 22/10/2026, sem copiar seus textos integrais:

- [Andrej Karpathy — LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): camadas de fontes/síntese/schema, índice, log e manutenção.
- [Agent Skills — Best practices](https://agentskills.io/skill-creation/best-practices): conteúdo específico, detalhe moderado e referências carregadas conforme a necessidade.
- [Diátaxis](https://diataxis.fr/): necessidades de aprendizado, tarefa, referência e explicação.

A aplicação concreta desses princípios está em [manutenção](../wiki/manutencao.md). Para acrescentar fontes, siga seu procedimento de ingestão e execute o [verificador](../scripts/verificar_documentacao.py).
