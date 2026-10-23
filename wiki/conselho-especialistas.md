# Conselho de especialistas

Estado: protocolo com implementação local `0.1.0-alpha.1`; execução e isolamento de plataforma exigem verificação. Revisão: 2026-10-23. Referência atual: [S11 — plano revisado](../sources/originais/plano-conselho-especialistas-revisado.md).

O conselho melhora ideias e decisões tentando refutar hipóteses contra critérios definidos previamente. Mostra onde resistem, onde falham e o que permanece incerto. Preserva evidência e dissenso, inclusive o argumento minoritário. Não produz a versão principal, não recomenda uma opção e não decide pelo usuário. Esse propósito orienta o protocolo; preencher artefatos não demonstra que houve um exame independente.

## Entrada e entrega

O brief reúne pergunta, hipóteses sem autoria, critérios com `refuta_se`, critérios decisivos, tipo de conselho, template, dose, fontes conferidas, parecer técnico quando necessário e restrições de compartilhamento. A preparação valida o contrato, separa a chave de autoria e monta briefs individuais. Critérios precisam ter sido fixados antes da exposição das hipóteses aos julgadores; hash e declaração registram essa alegação, mas não provam a cronologia.

Um brief incompleto volta à origem com a lacuna identificada. No modo avulso, primeiro se fixam pergunta e critérios; se as opções já foram expostas, a limitação é registrada. Não se inventa um critério para favorecer uma opção conhecida. Consulte os [formatos executáveis](../skills/conselho-especialistas/references/formatos.md).

A entrega reúne vereditos, crítica, matriz, síntese, divergências, faltas, placar e custos conhecidos. O script devolve um mapa `arquivos`, com caminhos sob `conselho/<id>/`, para **somente a condutora** registrar no dossiê. O conselho trabalha fora dele. A chave de autoria e o mapa privado ficam fora dos briefs e da apresentação antes da decisão. Instalação, comandos e integração estão em [implementação do conselho](implementacao-conselho.md).

## Processo de julgamento

1. **Preparar:** conferir entrada, anonimizar, sortear ordens por membro e registrar a composição privada. Na dose completa, executar normalização em sessão separada e conferir fidelidade antes do envio.
2. **Julgar independentemente:** cada membro recebe só seu brief, busca evidência para refutar e não vê os outros vereditos, autoria ou preferência do usuário.
3. **Criticar:** um crítico separado examina método, lógica, lastro e possível contaminação; ele não vota.
4. **Detectar divergência:** sinais opostos em critério decisivo, falha fatal, maioria `?` ou perda do lastro de um veredito decisivo podem justificar aprofundamento.
5. **Trocar quando permitido:** no máximo uma troca, com motivo e dose compatível, retomando os mesmos membros. Mudança de sinal exige evidência nova identificada.
6. **Consolidar:** preservar sinais e argumentos, sem soma, média, ranking, vencedor ou recomendação. No rápido, a síntese copia argumentos dos vereditos; no completo, um relator separado organiza os achados.

Cada célula da matriz conserva `+`, `0`, `-` ou `?` por membro, com sustentação e condição de revisão. Concordância não comprova uma afirmação. Falta de observação não vira acordo. Para mais de seis hipóteses, o preparo distribui subconjuntos com cobertura e sobreposição; as ausências continuam visíveis. A triagem procura falha fatal sem descartar automaticamente hipóteses; um apontamento isolado passa por revisão, conforme a dose. Fontes: [S11, §§6–9](../sources/originais/plano-conselho-especialistas-revisado.md) e [protocolo do pacote](../skills/conselho-especialistas/references/protocolo.md).

## Modelos, registro e limites

O usuário selecionou S11, que revisa [S04](../sources/originais/plano-conselho-especialistas.md): a v1 é **Claude-first**, com o mesmo modelo de juiz escolhido e verificado para todos os papéis de julgamento. A independência vem de sessões não produtoras e óticas distintas; isso exige auditoria real de contexto, memória, arquivos e ferramentas. Várias famílias ficam para uma fase posterior. Nomes e preços nas fontes não são catálogo atual. Veja [modelos](../skills/conselho-especialistas/references/modelos.md).

O placar local é JSONL, por hipótese e critério; probabilidade é opcional. Brier só usa previsões probabilísticas com desfecho factual explicitamente observado e referenciado. Uma decisão de valor do usuário é registrada à parte e não vira desfecho factual. Não há ajuste automático de templates. Revelar autoria ou modelos exige a decisão prévia e a permissão prevista no protocolo.

Scripts conferem estrutura e invariantes locais. Pesquisa real, crítica, relatoria, neutralidade da normalização e isolamento continuam exigindo execução e exame. Notion ainda não tem integração validada; o transporte CLI local cobre a primeira rodada. A segunda precisa de um hospedeiro que preserve as sessões. Veja [avaliação](avaliacao-conselho.md) e [pendências](pendencias.md).
