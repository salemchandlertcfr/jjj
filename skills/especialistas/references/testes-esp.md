# Avaliação e regra de entrada

S13 §14. Não confundir testar a infraestrutura com validar uma especialidade.
Executores recebem enunciado e, na condição com, o bloco; nunca gabarito,
fonte do gabarito ou a outra resposta. Autor dos problemas não vê a esp;
escritor não vê testes. Pares com/sem são lançados juntos.

Para cada modelo de papel, três execuções por condição e problema. Entram
5–10 problemas internos e 1–2 externos; metade dos internos são variantes
novas. Todos têm gabarito verificável ou rubrica com dois avaliadores cegos.
Na criação as condições são com/sem; na revisão, nova/anterior.

Admitir exige ganho médio de pelo menos 10 pontos percentuais e nenhum
problema pior em duas das três comparações pareadas. Empate não entra.
O modelo menor também é testado nas duas condições para comparação, mas
não é automaticamente modelo de produção nem precisa satisfazer a porta
dos papéis aos quais não foi designado. Declare qualquer escolha nova no 0.3.

`teste_esp.py` valida a matriz completa, sem preencher faltas com zero.
Falha/timeout permanece teste incompleto. Gabaritos numéricos e igualdade
têm avaliação determinística; rubrica é julgada externamente e importada.
O modo `--executar` é opt-in, comando por argumentos, sem shell, quatro
processos simultâneos, timeout de até 60 s por execução. Adaptador precisa
verificar o modelo real e devolver JSON; sua declaração não é prova independente.

Métricas ainda dependentes de ensaio real: identificabilidade, recrutada ×
fixa, uma × duas propostas com fusão, distante, focada × exaustiva, persona,
modelo menor e formas de transporte. Não inferir custo/tokens de caracteres.
Uma esp só é publicada depois de origem, licenças, fontes e revisões, além
do resultado numérico; `admitir: true` não grava ou publica nada.
