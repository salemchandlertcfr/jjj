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
