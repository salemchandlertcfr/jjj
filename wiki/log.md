# Log da wiki

Registro cronológico de ingestões e revisões relevantes. Acrescentar novas entradas ao final; preservar o histórico e usar retificação quando necessário.

## 2026-10-22 — Ingestão inicial e síntese

- Incorporados os nove anexos S01–S09; nomes simplificados, bytes preservados e hashes registrados no [manifesto](../sources/manifest.json).
- Criadas páginas de método, fluxo, arquitetura, contratos e conselho; identificados o plano histórico substituído e conflitos que permanecem em [pendências](pendencias.md).
- Adotadas as [decisões editoriais](decisoes.md), a manutenção da LLM Wiki e um exemplo didático. Pesquisa externa limitada às referências registradas no [inventário](../sources/README.md).
- Confirmado que o destino estava vazio e que as skills específicas não constavam dos anexos. S01 é `skill-creator`, com recursos auxiliares ausentes.
- Executada S03 com 100 rodadas principais e verificação numérica adicional; condições e limites em [simulação](simulacao.md). Não houve avaliação empírica do método.
- Realizada revisão cruzada da síntese contra as fontes; o verificador cobre links locais, navegação e integridade, sem substituir essa revisão semântica.

## 2026-10-23 — Primeira implementação da condutora

- Recebido o plano detalhado da `etapa-1-cir` como S10, preservado e incorporado ao inventário.
- Criado o pacote universal alpha com protocolo, referências, catálogo de sub-etapas, modelos e scripts locais. Escopo entregue em [implementação](implementacao-condutora.md).
- Acrescentados testes de persistência e bloqueios, com [cobertura e limites](avaliacao-condutora.md). Integrações de plataforma, demais skills e aceite humano continuam pendentes.
- Suíte final: 66 testes aprovados. Pacote extraído fora do repositório funcionou nos comandos locais; catálogo de 51 sub-etapas conferido. A revisão corrigiu recuperação após edição manual, validade de aprovação, dose obrigatória no fechamento e reconhecimento de registros reais.

## 2026-10-23 — Conselho conforme o plano revisado

- Recebido e preservado S11, plano revisado do conselho selecionado pelo usuário; S04 permanece histórico. Atualizadas as decisões de v1 Claude-first, mesma escolha de juiz e única escritora do dossiê.
- Registrado o propósito antes da implementação: tentar refutar hipóteses com evidência e independência, preservando dissenso e decisão humana. Criado o [conselho alpha](implementacao-conselho.md), com scripts locais, referências e pacote de retorno à condutora.
- Confirmada a origem oficial de S01 e utilizados auxiliares fixados do `skill-creator` no workspace, sem vendorização. Avaliação comparativa limitada e testes locais documentados na [avaliação do conselho](avaliacao-conselho.md).
- Wiki, inventário e fronteiras da condutora atualizados. Restam 11 skills planejadas; pesquisa, isolamento e integrações reais continuam sujeitos às [pendências](pendencias.md).
- Verificação final: 143 testes aprovados (77 conselho, 66 existentes); documentação e integridade das 11 fontes conferidas. Os dois pacotes portáveis foram gerados; preparação do conselho executada após extração fora do repositório. Benchmark e viewer reproduzidos byte a byte. A revisão corrigiu URLs privadas iniciais, conteúdo invalidado republicado, fidelidade dos argumentos e distribuição das fichas na troca. Revisão humana dos seis ensaios permanece pendente.

## 2026-10-23 — Primeiro alpha local do grill

- Preservado S12 e registrado propósito antes da implementação. O anexo `SKILL.md` repetido é idêntico a S01; não foi duplicado no inventário.
- Criados protocolo universal, referências por tarefa, modelos JSON e três CLIs com primitivas compartilhadas para perguntas, respostas e Entendimento. Classificação semântica e persistência continuam com a condutora; pesquisa/leitor não foram simulados como integrações reais.
- Acrescentados testes locais com extração do pacote e fluxo CLI; executados seis ensaios com/sem skill e avaliação separada. Resultados, rubrica, hashes e limites em [avaliação](../evals/grill-embasado/README.md). Revisão humana pendente.
- Retificação do estado observado neste checkout: os comandos gerais não reproduzem os 143 passes históricos; faltam a pasta da condutora e módulos do conselho. O verificador acusa três links antigos, e a suíte geral tem sete erros anteriores. Essas falhas não foram corrigidas ou ocultadas pelo desenvolvimento do grill.

## 2026-10-23 — Recrutamento e infraestrutura da biblioteca

- Preservado S13 e registrado propósito antes do código. Criados pacote universal `especialistas`, seis CLIs, regras de papéis, schemas e modelos. Não foram geradas `esp-*` de produção.
- Executados 33 testes locais, com 30 fichas plantadas e bibliotecas/executor dublês temporários. Fluxo CLI passou após extração fora do repositório. Evidência e limites em [implementação](implementacao-especialistas.md).
- Rodados seis ensaios textuais, com/sem skill, avaliados por outra sessão: 12/12 nas duas condições, sem demonstração de ganho. Janelas de tempo não comparáveis foram preservadas sem média/delta; revisão humana pendente. Veja [avaliação](../evals/especialistas/README.md).
- Mantidos os bloqueios de condutora/conselho ausentes; curadoria, pesquisa, isolamento, modelos e validação de plataformas continuam pendentes.

## 2026-10-23 — Reuniões da equipe com rastreabilidade

- Preservado S14 a partir do ZIP, com bytes/hash do Markdown e proveniência do contêiner no manifesto. Registrado propósito antes do código: combinar especialidades sem perder informação única, fazer média arbitrária ou apagar dissenso.
- Criados pacote universal `equipe-especialistas`, sete CLIs, referências por papel/ambiente, schemas e modelos fictícios. Mesa ordena eventos e projeta tarefas; só a condutora persiste. Não foram abertas sessões Claude ou simulada pesquisa instalada.
- Executados 40 testes locais, incluindo reunião inteira pela CLI após extração fora do repositório. A revisão bloqueou campos privados em partes/dissenso da fusão, redefinição de contribuições fora da preparação e fala posterior sem novidade declarada. Estado não aceita métricas inválidas.
- Seis ensaios textuais com/sem skill, revisados separadamente: 12/12 assertions nas duas condições, sem demonstração de ganho de equipe. Preservados 44 artefatos com hashes; benchmark e viewer oficiais reproduzidos byte a byte. Tokens/tempo/modelo indisponíveis ficam nulos, sem estimativa. Revisão humana pendente; método em [avaliação](../evals/equipe-especialistas/README.md).
- A suíte geral também exercitou os 75 testes existentes de grill/especialistas sem regressões. Permanecem sete erros anteriores de imports/setup na condutora/conselho ausentes e três links antigos da condutora no verificador. As 14 fontes mantêm hashes íntegros. Pesquisa, isolamento, transporte Claude/Notion e comparações reais previstas no plano permanecem em [pendências](pendencias.md).

## 2026-10-23 — Primeiro alpha local do mapa do fenômeno

- Recebido e preservado S15 a partir de cir-mapa.zip, com hash do Markdown/contêiner e caminho interno no manifesto. O resumo do pedido foi conferido contra o checkout; suas afirmações antigas de maturidade não foram promovidas a fatos.
- Registrado propósito antes do código: diagnóstico rastreável do fenômeno, com rivais e desconhecimento, sem mercado ou solução. Criados cartões 2.1–2.7/integração, referências, modelos fictícios e seis CLIs locais. Alterações de S15 sobre S08/S02 e limites do contrato de cobertura K ficaram explícitos.
- Passaram 21 testes locais, incluindo 30 mutações estruturais, 15 variações válidas, corpus lexical 40/20 PT/EN, histórico Git e pacote extraído fora do projeto. Os 115 testes existentes dos componentes presentes também passaram; a suíte geral relata 139 itens, com os mesmos sete erros antigos (incluindo três falhas de carregamento). O verificador mantém os três links antigos da condutora ausente.
- Seis ensaios textuais avaliados por outra sessão: 11/12 assertions com skill e 6/12 sem. Rubrica composta e guiada, sem prova de ganho geral; falha com skill preservada. O ensaio antecedeu a conclusão de formatos.md e não valida a interface final. Tokens/tempo/modelo exato desconhecidos, revisão humana pendente. Veja [avaliação](../evals/cir-mapa/README.md).
- Agregação/viewer oficiais gerados com auxiliares externos fixados e hashes; fontes S01–S14 preservadas. Pesquisa, guarda integrada à condutora, isolamento real, sonda Claude, recall e aceite humano continuam pendentes; escopo em [implementação](implementacao-mapa.md).
