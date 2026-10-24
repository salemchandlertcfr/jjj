# Registro de execução — caso 3

Condição: without_skill, run-1.

Baseline textual produzido com o assistente Codex disponível, usando conhecimento geral e o prompt do caso. O arquivo evals.json foi acessado apenas para extrair id e prompt. Não foram consultados expectations, skills, AGENTS, wiki, fontes do projeto, testes nem saídas da condição com skill. Não houve pesquisa externa nem uso de modelos externos.

A execução ocorreu sem isolamento de filesystem: o processo compartilha o workspace com as demais condições. A separação foi procedimental, sem leitura dos respectivos artefatos.

Sem integração real: não foram executadas as etapas dos projetos descritos nos prompts, nem acessados aplicativos, serviços ou ferramentas de domínio. Foram apenas redigidas respostas e gravados os artefatos locais desta condição.

As métricas nativas de tokens e duração não estavam disponíveis. Os campos correspondentes em timing.json permanecem null. Não foi realizada avaliação ou julgamento da própria resposta, nem git commit/push.
