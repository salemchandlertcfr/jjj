# Implementação da condutora

Estado: `0.1.0-alpha.1`, primeira implementação local. Revisão: 2026-10-23. Requisito principal: [S10 — plano da condutora](../sources/originais/plano-etapa-1-cir-condutora.md).

## O que esta versão entrega

O pacote [`skills/etapa-1-cir/`](../skills/etapa-1-cir/SKILL.md) reúne instruções em português, referências carregadas por tarefa, modelos de dossiê e scripts em Python 3.10+ com biblioteca padrão e Git. Ele coordena e registra; não produz pesquisa, ideias ou pareceres por conta própria.

| Parte | Comportamento implementado |
| --- | --- |
| Dossiê | Inicialização em pasta dedicada, modelos pendentes, Git e índices curtos para agentes. Sem sobrescrever uma pasta ocupada. |
| Estado e retomada | Schema, resumo, histórico do ciclo, escrita atômica, revisão concorrente e trava por sessão. |
| Ordem e aprovação | Registro sequencial dos passos; versão antes da geração; validação antes da decisão; aprovação vinculada à pergunta e ao commit apresentado. |
| Briefs | Seleção explícita por papel, conteúdo aprovado e barreiras para campos reservados. Filtro não equivale a sandbox. |
| Registro | Registro e arquivos declarados num commit; recuperação após interrupção; falha de commit preserva o estado anterior. |
| Vigia e pronto | Sinais contextuais para revisão; conferência de integridade e evidências declaradas para os 14 critérios. Não julgam mérito científico. |

O catálogo das 51 sub-etapas vem de S08; só o tema 0 tem cartões operacionais incluídos. Os demais aguardam as skills temáticas. Fornecer um cartão aprovado permite montar um brief; não instala a skill executora. Dublês são exclusivamente de avaliação e precisam ser identificados como tal.

## Instalar e iniciar

Copie a pasta inteira `skills/etapa-1-cir/` para a área de skills do agente escolhido. O conteúdo não depende dos anexos desta wiki. A instalação e as capacidades do hospedeiro precisam ser verificadas; neste alpha não há instalação automática no Notion nem plugin de hooks.

Para gerar um pacote ZIP `.skill`, na raiz deste repositório:

```bash
python3 scripts/empacotar_skill.py --destino ../etapa-1-cir.skill
```

Para experimentar os scripts a partir da raiz do repositório, use uma pasta nova fora de qualquer outro repositório Git:

```bash
python3 skills/etapa-1-cir/scripts/dossie_init.py ../cir-meu-projeto --projeto meu-projeto --session sessao-1
python3 skills/etapa-1-cir/scripts/estado.py resumo ../cir-meu-projeto
python3 skills/etapa-1-cir/scripts/estado.py dose ../cir-meu-projeto --session sessao-1 --planejada padrao --usada padrao --motivo "Dose inicial da ficha; ajustar conforme incerteza e decisões do usuário."
python3 skills/etapa-1-cir/scripts/pendencias.py ../cir-meu-projeto
```

O último comando deve apontar pendências: o esqueleto inicial não está pronto. Configure sua identidade Git antes da inicialização. Se ela faltar, os arquivos ficam preservados e o comando explica como configurar a identidade local e executar `dossie_init.py PASTA --finalizar`. Nenhuma identidade ou aprovação é inventada.

No agente, peça “use a skill etapa-1-cir para começar este projeto” e informe o caminho do dossiê. A condutora deve ler o resumo, conferir o Git e conduzir o tema 0. Dependência ausente é um bloqueio explícito, sem parecer simulado.

## Registrar e retomar

Consulte `--help` dos scripts para as operações de estado, dose, propósito e aprovação. `estado.py configurar` recebe JSON descritivo com mapa de modelos e restrições, sem alterar progresso ou instalar serviços. `estado.py rodada` registra novas famílias e mudança no CIR para sinalizar a regra de parada. Os detalhes de entrada ficam em [formatos do pacote](../skills/etapa-1-cir/references/formatos.md).

Um checkpoint mínimo é um JSON com `tipo: "checkpoint"`, `escolha` descrevendo o que foi registrado e, opcionalmente, `arquivos` mapeando caminhos relativos permitidos para textos. Guarde o JSON de entrada fora do dossiê ou declare sua persistência; um arquivo não rastreado inesperado impede commit. Execute:

```bash
python3 skills/etapa-1-cir/scripts/registrar.py registrar ../cir-meu-projeto --session sessao-1 --entrada ../checkpoint.json
```

Decisões no passo 10 exigem dose planejada/usada com motivo, contexto, opções, escolha, motivo e objetivo do usuário, evidências, dissenso, confiança e condição de reversão. O registro guarda o commit-base; o commit que efetivamente contém a decisão é retornado e localizável pelo ID no histórico. Isso evita a referência impossível a um commit contendo seu próprio hash.

Após interrupção de registro, execute `registrar.py recuperar PASTA --session ID`. A recuperação distingue commit já realizado de gravação ainda não commitada. Se um arquivo mudou fora da transação, ela preserva as edições e suspende o desfazimento automático para revisão. Um commit local pode existir mesmo se o envio falhar: não crie outra decisão para tentar enviar o mesmo conteúdo.

## Limites e próxima integração

O remoto é opcional e não é configurado a partir do repositório de desenvolvimento. A configuração inicial não acessa rede nem comprova privacidade. Envio exige `--push --confirmar-remoto-privado`, autenticação externa e autorização para os dados. Uma falha deixa o commit local e um aviso de envio pendente. Não há sincronização automática ou armazenamento de credenciais.

O [conselho alpha](implementacao-conselho.md) está disponível como pacote separado; instalá-lo exige verificar suas capacidades. S11 revisa S04 e adota Claude primeiro, com o mesmo modelo de juiz em sessões independentes e óticas distintas. As outras 11 skills, hooks, auditoria de permissões e provas reais no Notion/Claude Code continuam pendentes. A próxima integração deve conservar os contratos, verificar o transporte real e executar o aceite humano dos temas 0 e 1 antes de chamar o fluxo completo de pronto.

Verificação local e seus limites estão registrados em [avaliação da condutora](avaliacao-condutora.md). Decisões e lacunas do sistema continuam em [pendências](pendencias.md).
