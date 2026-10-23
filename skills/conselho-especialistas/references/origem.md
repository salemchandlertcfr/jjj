# Origem, atribuição e limites

## Base desta implementação

S11, `plano-conselho-especialistas-revisado.md`, fornecido pelo responsável,
orienta propósito (§1), composição/óticas/templates (§5), protocolo (§6), regras
(§7), formatos (§8), adaptadores (§9), mapa Claude-first (§10), estrutura de
arquivos (§11), papéis (§12), casos-limite (§13) e avaliações (§14). SHA-256 da
fonte preservada: `33268e2a5443223742c67b62943f963c47217efc1ec696f930d7c0bf6baf7286`.

O responsável determinou S11 como revisão ativa; ela substitui o antigo desenho
de S04 no conflito Claude-first/múltiplas famílias. Os nomes e preços de modelos
na fonte são históricos, não catálogo atual. A implementação pede escolha real
do usuário e conferência no ambiente; não afirma disponibilidade futura.

S01, `skill-creator.md`, é a referência genérica fornecida, não skill instalada
com seus auxiliares. Foram aproveitados entendimento do propósito antes do
processo, draft curto, carregamento progressivo e avaliação comparada com/sem
skill, apresentada para revisão humana ainda pendente. SHA-256:
`dcd4803e61e913e6fc27294184cd3a71f09f5e924ff20c8a9a20173e7b3c2bcf`.
S01 foi confirmado byte a byte no repositório oficial
[`anthropics/skills`, revisão dbd4588](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator),
sob Apache-2.0. Auxiliares oficiais de avaliação e viewer foram usados fora
do pacote, com hashes fixados. Otimização de acionamento não foi executada;
citar a referência não instala ferramentas.

O contrato local JSON v1 concretiza formatos da fonte. São decisões operacionais:
hash de critérios com declaração auditável, mapas/chaves privados, matriz com
não observados, crítica estruturada, uma linha de previsão por célula e
probabilidade opcional. O contrato não alega prova automática de cronologia,
isolamento, verdade, qualidade científica ou ausência de recomendação.

## Ideias de projetos externos

| Referência | Ideia aproveitada | Situação de código/licença |
| --- | --- | --- |
| [llm-council](https://github.com/karpathy/llm-council), Andrej Karpathy | Opiniões independentes, revisão anônima e compilação | Segundo S11, sem licença; somente inspiração conceitual, sem copiar código |
| [claude-council](https://github.com/hex/claude-council), hex | Transporte paralelo, repetição por assento e papéis | S11 informa MIT. Implementação local escrita para este contrato; não alegar código externo copiado sem verificação de bytes/licença |
| Fluxograma IDEAL e plano da condutora, fornecidos pelo responsável | Ciclo, critérios, decisão humana e persistência exclusiva da condutora | Fontes do projeto; não constituem autorização para redistribuir anexos de terceiros |

Não foi atribuída ao pacote uma licença de terceiros por analogia. Se incorporar
código externo depois, confira a licença real, preserve avisos e registre quais
trechos foram usados. Este arquivo atribui ideias, sem afirmar auditoria dos
repositórios ou atividade atual dos mantenedores.

## Evidência e capacidade

As referências científicas citadas em S11 motivam o desenho; este pacote não
repete seus resultados como validação empírica própria. Alvos de acerto, lastro,
estabilidade e custo em S11 §14 são metas de avaliação, não resultados obtidos.

Onze skills restantes da família não estão incluídas: `grill-embasado`,
`pesquisa-cientifica`, `especialistas`, `equipe-especialistas`, `cir-proposito`,
`cir-mapa`, `cir-idealidade`, `cir-divergencia`, `cir-arquitetura`, `cir-prova`
e `cir-sintese`. A condutora é pacote separado. Este conselho não cria resultados
dessas dependências por simulação. Web real verificada pode apoiar procedimento
manual; fichas fixas/dublês são instrumentos explícitos de avaliação.

Notion e Claude Code têm planos de integração exportáveis. Um transporte CLI
configurável não prova integração, acesso a um modelo nem isolamento. Relatórios
de avaliação devem distinguir checagens determinísticas, execuções com dublês,
avaliações reais de julgamento e integrações de plataforma exercitadas.
