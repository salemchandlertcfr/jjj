# Mesa, tarefas e estado

S14 §§6/9/13. A condutora é a mesa na v1. Os scripts preparam mensagens e
validam eventos; não abrem sessões nem conferem permissões de provedor.

O estado tem revisão e hash para detectar edições acidentais; não é assinatura
ou autenticação. Somente `iniciar`, `registrar`, `timeout` e `reparar` produzem
novo estado, em stdout. A persistência atômica/concorrrente fica com a condutora.
Não sobrescreva a entrada com redirecionamento de shell.

Preparações e posições têm tarefas paralelas e não recebem umas às outras.
Falas são sequenciais; crítico por último e fechamento do líder. Checagem é
tarefa da mesa entre rodadas e antes da resposta individual. A abertura e
as posições não podem ser puladas. Uma revisão da saída e uma resposta do líder.

`retomar` envia, na fala, só eventos desde a última fala do membro. Na primeira,
recebe preparações inteiras e abertura. `sem_estado` envia ata completa,
referência do papel e bloco do próprio membro. Nenhum recebe modelo dos outros,
ficha completa, chave de fusão, marcadores ou quarentena. A transcrição real
ainda precisa ser comparada à mensagem preparada.

Timeout: `mesa.py timeout estado.json --ator M1`, uma repetição; na segunda,
preparação faltante é registrada e fala pode virar sem fala. Menos de dois
especialistas preparados não abre reunião; no individual é necessário um.
Líder/crítico/posição indisponíveis suspendem para a condutora, sem fingir conclusão.

Vazamento: o evento não entra na ata pública; vai à quarentena privada. Use
`reparar --ator M1 --sessao nova --nota auditoria`. Substitua a sessão indicada;
se ocorreu na rodada, a rodada aceita anterior é preservada na quarentena e
repetida. Sessão nova e nota não provam que o ambiente deixou de vazar.
