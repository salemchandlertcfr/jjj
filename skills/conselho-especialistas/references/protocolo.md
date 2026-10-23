# Protocolo de julgamento

Base: S11 §§4–9 e 12–13. Leia [propósito](proposito.md) antes de confundir o
roteiro com o objetivo: o exame melhora a decisão por refutação, não por consenso.

## Entrada e capacidades

Receba da condutora brief filtrado, critérios prévios, hipóteses em cartões,
fichas relevantes e parecer quando exigido. O mapa e a chave ficam fora das
sessões cegas. Confirme a composição, doses e ferramentas efetivas. Sem critério
ou `refuta_se`, devolva o que falta; sem hipótese alternativa, registre o limite
de comparação. Não crie critérios depois para ajustar às hipóteses.

A condutora executa anonimização, guarda a chave e confere fidelidade. Remova
marcas como “minha versão” e “a da IA” somente se não mudar o sentido; caso
contrário, devolva. Cartão longo demais volta à origem; não o resuma inventando
uma versão avaliada. A condutora aprova o tamanho máximo e a estrutura fixa.

Declare como a pesquisa será feita: `pesquisa-cientifica` real se instalada e
verificada, ou busca/leitura web do hospedeiro com procedimento manual equivalente
documentado. Refutar exige contraevidência e leitura das fontes; conferir exige
verificar que o trecho sustenta a afirmação. Registre consultas, fontes e lacunas.
Fixtures e dublês são instrumentos de avaliação; não satisfazem pesquisa real.

## Preparação privada

Monte painel com o mesmo modelo real de juiz em todos os papéis, escolhido pelo
usuário e acessível pela via verificada. Sessões são distintas e não produziram
o artefato. IDs no JSON são designações; audite o isolamento real do ambiente.

Sorteie por membro ordem e, acima de seis hipóteses, subconjuntos com cobertura
e sobreposição. Registre a semente e a distribuição no painel privado. Cada
brief mostra apenas a ótica, o rótulo e os cartões atribuídos. Não revela mapa,
semente, chave, origem, preferência nem identidades dos demais modelos.

Na dose completa, normalizador separado e sem autoria uniformiza a redação,
sem modificar premissas, conteúdo ou incerteza. A condutora confere a fidelidade
e preserva as versões. Não use o texto normalizado sem essa conferência.
Normalizar nos demais casos com versões humanas e de IA é proposta a avaliar,
não uma integração automaticamente disponível (S11 §17).

## Rodada 1 e crítica

Dispare membros independentes em paralelo ou em lotes quando o ambiente limitar
concorrência. Não envie resultados antecipados a quem ainda está julgando.
Cada membro tenta refutar contra cada critério, registra lastro e o que mudaria
o sinal. Verifique cobertura exata: hipóteses atribuídas × critérios, sem duplicatas.

`+` significa que a hipótese resiste ao critério; `-`, que é refutada nesse
critério; `0`, resultado neutro ou sem efeito conforme a definição prévia do
critério; `?`, insuficiência de informação. Não use `0` para esconder desconhecido.
A definição dos sinais é convenção operacional do contrato desta versão; não
se transforma em escala numérica.

O crítico, em sessão própria, confere método, lógica, lastro e vazamento. Recebe
vereditos pelos rótulos, briefs atribuídos e fontes autorizadas; não conhece
autoria, mapa ou preferências. Marca cada achado com célula, motivo e evidência.
Ele não atribui sinais às hipóteses nem produz um voto adicional.

Vazamento de workspace/dossiê invalida o veredito afetado e exige auditoria e
alerta. Não o mantenha na matriz como se apenas tivesse menor confiança. Um
validador pode sinalizar suspeitas lexicais; a auditoria real decide o ocorrido.

## Divergência e uma troca

Há divergência relevante quando um critério decisivo recebe `+` e `-`, quando
existe falha fatal, quando a maioria dos membros observadores responde `?`, ou
quando o crítico derruba o lastro de veredito decisivo. Cobertura ausente deve
ser mostrada; não é resposta negativa, desconhecida ou convergente.

Se a dose permitir, envie aos mesmos membros da rodada 1 apenas argumentos
anônimos dos pontos divergentes, em ordem sorteada, e as notas do crítico. Não
revele quem escreveu nem modelo ou origem. Cada mudança de sinal referencia
evidência nova e seu vínculo ao critério; pressão de maioria não é evidência.
Sem elemento novo, mantenha a posição. Guarde anterior e revisão; uma troca só.

Persistindo o impasse, devolva a divergência e a lacuna de pesquisa ou casos à
condutora. Ela dimensiona nova avaliação; não provoque debate livre nem gere
mais versões para apagar o resultado inconclusivo.

## Triagem e confirmação de falha fatal

Triagem comum tem uma rodada e só procura falha fatal. Registre classificação,
motivo e lastro sem descartar a hipótese: sem falha fatal, impossível em princípio,
difícil hoje ou fere um valor. Uma objeção isolada passa pelo crítico e, na dose
padrão/completa, por segundo refutador independente de outra ótica. Sem essa
conferência, a alegação permanece pendente e não é entregue como falha confirmada.

Triagem reforçada recebe parecer de verificação e dois refutadores; uma troca
é permitida somente com divergência. Ausência do parecer exigido é bloqueio,
não autorização para simular uma equipe que o produziu.

## Matriz, síntese e entrega

Mantenha cada sinal ligado ao membro, critério, hipótese, justificativa e fonte.
Sem soma, média, ranking, vencedor ou recomendação. No rápido, a síntese copia
literalmente os argumentos e aponta divergências. No completo, relator real,
separado e sem ferramentas escreve convergências, melhores argumentos de cada
lado, falhas apontadas, condições de mudança e lacunas.

Confira toda posição minoritária e também os argumentos que a sustentam.
Checagem por IDs não prova que a paráfrase é fiel ou que não recomenda; faça
leitura independente. Relator não resolve impasse por adjetivos como “mais
promissor”, “preferível” ou “melhor opção”.

Devolva à condutora pacote externo, resumo de cerca de 300 palavras e caminhos.
Ela incorpora no dossiê pelo seu registro, com decisão, vigia e commit. O conselho
não escreve diretamente nele. No avulso, grave em pasta nova própria com Git.
Inclua fichas novas sem duplicar, placar, custos observados, ausências, invalidações
e limites de isolamento. Chave e modelo continuam privados até a decisão.

## Falhas e situações especiais

| Situação | Encaminhamento |
| --- | --- |
| Transporte falha ou expira | Uma nova tentativa; depois alternativa autorizada de mesmo nível ou espera |
| Juiz indisponível ou créditos esgotados | Preserve resultados; peça escolha entre esperar e troca explícita. Nunca rebaixe silenciosamente |
| Veredito fora do formato | Um pedido de correção; persistindo, invalide e exclua da matriz |
| Todos concordam sem lastro | Crítico registra alerta; devolva necessidade de pesquisa |
| Ideia incidental de membro | Retorne à condutora para banco com origem `conselho`; não é avaliação de si própria |
| Usuário quer ser membro | Sua posição entra como versão/decisão, fora dos membros julgadores |
| Usuário quer saber modelos/autoria | Após sua decisão, sob pedido; antes, preserve cegamento e explique a finalidade |
| Material sigiloso | Só sessões autorizadas; não publicar em páginas do Notion; família e via obedecem à autorização |
| Falta obrigatória | Preserve o ponto e devolva bloqueio com próximo passo, sem fabricar aprovação |

O pacote está pronto quando entregas previstas chegaram ou faltas estão explícitas,
crítica real foi feita, matriz e síntese estão disponíveis, placar foi atualizado
e chave permaneceu separada. Pronto do pacote não significa aprovação humana,
certeza científica ou conclusão do CIR.
