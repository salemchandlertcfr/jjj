# Adaptador Notion — plano de integração

Base: S11 §§9.1, 11, 12 e 17. Este arquivo especifica a integração desejada;
o pacote local não instala páginas, Files, Custom Agents, ferramentas de sessão,
credenciais ou auditoria do Notion. Não declare a integração pronta sem exercitá-la.

## Contrato de transporte

Entrada: rótulo do membro, modelo real autorizado, via, brief em texto e tempo
limite. Saída: texto do veredito, situação `ok`, `falhou`, `invalido` ou
`substituido`, modelo efetivo, tempo e custo observado ou desconhecido.
O conteúdo universal vem de [membro](membro.md), [crítico](critico.md) e
[relator](relator.md). Não introduza regra da plataforma no método universal.

## Pré-requisitos para chamar

Verifique nas ferramentas reais a criação de sessão filha com modelo escolhido
pelo usuário, modo incógnito e computador novo; passagem de texto sem link
de origem; mensagem posterior à mesma sessão; espera/tempo limite; e listagem
dos eventos para auditoria. O mapa aprovado no projeto referencia essa escolha
de modelo. Não presuma que opção citada na fonte ainda existe ou funciona.

No desenho de S11, o computador novo reduz acesso aos arquivos locais da sessão
de origem. Isso não remove permissões de busca no workspace. Briefs proíbem
consulta a páginas e sessões, mas a proibição textual não é isolamento técnico.
Sem capacidade de auditar ou restringir o acesso exigido, preserve o bloqueio.

## Execução e auditoria planejadas

Uma sessão por membro, no modelo de juiz; crítico, normalizador e relator em
sessões separadas que não produziram o artefato. Dispare juntos ou em lotes
sem compartilhar resultados da rodada 1. A única troca, quando permitida, vai
à mesma sessão do membro. Uma repetição de transporte é permitida por assento.

Audite eventos: toda busca/leitura no workspace invalida o veredito e vira
alerta à condutora. A fonte exige sempre nos testes e no conselho completo;
nos demais, por amostragem. Se não houver amostragem definida, não alegue que
a auditoria ocorreu. Em vazamento, refaça o afetado com restrições reforçadas
e audite todos. Testes com material reservado podem exigir ambiente distinto.

Conteúdo sigiloso autorizado vai somente às sessões permitidas, nunca a páginas
do Notion. Não publique dossiê ou chave. Só a condutora incorpora o pacote e
suas referências na persistência do projeto.

## Publicação e alternativas futuras

Plano de publicação: SKILL como página, referências como subpáginas, scripts
em Files e instruções dos papéis nas sessões filhas. Isso é mapeamento de
artefatos, não evidência de que páginas foram criadas.

Custom Agent e ponte para outras famílias são futuros e condicionados à
universalidade: instruções exportáveis, ganho demonstrado e autorização.
Não substitua sessão incógnita/computador novo por Custom Agent presumindo
equivalência. A integração deve registrar o que foi efetivamente verificado.
