# Decisões da documentação

Estado: decisões editoriais e contratos de implementação adotados nesta organização. Revisão: 2026-10-23.

Estas decisões organizam o conhecimento recebido. Não aprovam regras de produto ainda conflitantes nos planos.

## D01 — Uma wiki, com fontes preservadas

**Contexto:** nove anexos repetem conceitos, detalham versões diferentes e misturam intenção, exemplos e simulação.

**Decisão:** preservar todos em `sources/originais/`, registrar proveniência e SHA-256 no [manifesto](../sources/manifest.json) e sintetizar assuntos em `wiki/`. Adotar índice, log e um schema de manutenção, inspirados na [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

**Consequência:** a leitura cotidiana é curta e rastreável; a consulta profunda continua possível. A wiki exige atualização quando entram novas fontes. Não duplicar esse conteúdo em GitHub Wiki, `docs/` ou arquivos de instruções por ferramenta.

## D02 — Maturidade e conflitos explícitos

**Contexto:** o repositório de destino estava vazio; o material recebido não contém as skills específicas implementadas. S05 declara sua substituição, mas outros documentos têm divergências sem precedência explícita.

**Decisão:** usar S02 como mapa da arquitetura e S08 como detalhamento operacional; S06/S09 explicam o método; S07 explica aperfeiçoamentos; S04 detalha o conselho com ressalvas. Preservar S05 como histórico. Essa é uma organização de leitura, sem declarar resolvidos os conflitos.

**Consequência:** planos não viram funcionalidades por efeito da redação. [Pendências](pendencias.md) precisam ser encerradas por decisão explícita antes de prometer conformidade integral.

**Atualização:** S10 detalhou a condutora; a seleção posterior de S11 pelo usuário estabelece a revisão atual do conselho, conforme D05. S04 permanece histórico.

## D03 — Contexto carregado conforme a necessidade

**Contexto:** reunir todos os anexos em um prompt obrigaria pessoas e agentes a reler material extenso e contraditório.

**Decisão:** README orienta a entrada; AGENTS contém só regras transversais; páginas temáticas guardam detalhes, fontes e links. Usar um exemplo canônico e um verificador sem dependências. Manter decisões em uma página enquanto forem poucas.

**Consequência:** cada tarefa carrega menos contexto. As [faixas de tamanho](manutencao.md) são escolhas locais, não exigências de Karpathy. Dividir uma página somente quando houver uma necessidade de consulta independente.

## D04 — Primeiro alpha universal da condutora

**Contexto:** o usuário forneceu [S10](../sources/originais/plano-etapa-1-cir-condutora.md) e pediu o desenvolvimento da `etapa-1-cir`.

**Decisão:** implementar protocolo e mecanismos locais portáveis em Python/Git, sem copiar código de terceiros ou presumir integrações de plataforma. Seguir a única escritora definida por S10; identificar Claude-first como perfil limitado e bloquear dependências ausentes. Manter transporte de agentes, hooks e validação de plataformas como próximos incrementos.

**Consequência:** o pacote pode ser instalado e seus mecanismos exercitados localmente, mas isso não representa o fluxo completo validado. Envios de dossiês são explícitos; commits locais sobrevivem a falha de rede. Aprovação aponta para o commit apresentado, enquanto o commit do registro é localizado por ID para evitar autorreferência. A recuperação suspende o desfazimento quando identifica edições posteriores desconhecidas. Escopo e verificações em [implementação](implementacao-condutora.md) e [avaliação](avaliacao-condutora.md).

## D05 — Conselho conforme o plano revisado, com propósito antes do código

**Contexto:** o usuário pediu desenvolver o conselho seguindo o novo [S11](../sources/originais/plano-conselho-especialistas-revisado.md), usando o `skill-creator` fornecido e entendendo primeiro o propósito geral. S11 revisa S04 e alinha a v1 ao Claude-first.

**Decisão:** partir da contribuição pretendida — refutação independente com evidência e dissenso, sem escolher pelo usuário — e derivar protocolo, interfaces e avaliação. Implementar apoio local, com o mesmo juiz escolhido em sessões separadas, mantendo pesquisa, crítica, relatoria e isolamento como capacidades a verificar. Aplicar S01 com auxiliares oficiais fixados e licença conferida, sem incorporá-los ao pacote. Conselho retorna artefatos externos; só a condutora os persiste.

**Consequência:** o conflito antigo de famílias deixa de bloquear a v1 selecionada; a verificação operacional permanece necessária. JSONL por hipótese/critério e desfechos factuais explícitos concretizam o placar, sem confundir escolha de valor com fato. Avaliações locais sustentam afirmações limitadas ao que exercitaram. Veja [implementação](implementacao-conselho.md), [avaliação](avaliacao-conselho.md) e [pendências](pendencias.md).

## D06 — Grill com protocolo universal e verificadores locais

**Contexto:** o usuário selecionou S12 e S01 para começar a implementar o grill. Seu propósito foi registrado antes do código. O checkout está incompleto na condutora e no conselho; a pesquisa não está instalada.

**Decisão:** implementar protocolo, formatos e auxiliares autocontidos, mantendo classificação e julgamento semântico com o agente e a persistência com a condutora. Usar regex apenas como triagem explicável; suspeitas exigem revisão, não promessa de neutralidade. Receber conferência externa sem imitar pesquisa ausente. Manter o perfil Claude-first do plano e identificar os ensaios daqui como exploratórios, sem alegar validação naquela plataforma.

**Consequência:** mecanismos locais podem ser exercitados e empacotados já; o fluxo integrado permanece pendente. Dados de persona e avaliação ficam fora do pacote para não contaminar entrevistas. Escopo, comandos e limites em [implementação do grill](implementacao-grill.md).
