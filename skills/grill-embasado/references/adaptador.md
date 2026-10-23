# Conversa, persistência e modelos

S12, §§9–12 e 17. Universal primeiro: protocolo em texto; adaptador só muda
conversa, registros e chamada do leitor. Claude primeiro é o desenho da v1:
modelo escolhido pelo usuário no projeto, sem nomes ou capacidades inventados.

| Hospedeiro | Perguntas | Registro | Leitor |
| --- | --- | --- | --- |
| Notion | Texto no chat da condutora | Condutora executa scripts, persiste e versiona | Sessão filha em computador separado, após verificação |
| Claude Code | Texto no terminal; múltipla escolha só para logística natural | Mesmos scripts | Subagente com contexto e permissões auditados |
| Chat sem computador | Mesmo protocolo | Blocos para salvar depois | Conversa nova com brief filtrado |

Essas são instruções de adaptação, não integrações implementadas. O pacote
não abre sessões, autentica provedores, pesquisa na web ou cria Custom Agents.
Sem leitor real, marque parada pendente; sem pesquisa, não conferida.

Só a condutora usa `--registrar` no dossiê; o script não autentica papéis nem
é barreira de permissões. Ela integra Markdown/JSON, registra última pergunta,
modo, fronteira, perguntas/turnos/minutos/modelo e faz Git com identidade real.
Não altere `estado.json` diretamente nem aprove passos por conta própria.

Auditoria usa transcrição normalizada com ID estável, `papel: usuario` e
`texto` intacto. Exportação nativa do hospedeiro precisa de adaptação testada;
nesta versão não há leitor automático de logs do Notion ou Claude Code.
