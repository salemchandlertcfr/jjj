# 6.3 Falhas e causas (2.2)

1. **O que é falha:** uma etapa ou passagem do job em que o resultado sai pior que o pretendido, para uma parte, com a frequência e a gravidade: "a criança chega depois do início da aula". "Falta de solução" não é falha: "não existe um aplicativo que…" vai para o banco.
2. **Falhas centrais:** as que mais pesam pelo propósito e pelas partes centrais, pelos sinais de intensidade da [`synthesize-research`](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management/skills/synthesize-research) (frequência, gravidade e emoção). A equipe sugere, e você escolhe; as outras ficam listadas, com o motivo de não serem centrais.
3. **Árvore com ramos:** cada falha central ganha uma árvore de causas, com ramos e um ramo "outras causas", que diz quanto acha que pesa. Árvores com ramos retirados pareceram completas a quem as leu ([Fischhoff, Slovic e Lichtenstein](https://doi.org/10.1037/0096-1523.4.2.330)); o ramo "outras causas" e a decomposição cega são a defesa. Ramo dividido em muitas partes parece pesar mais ([Tversky e Koehler](https://doi.org/10.1037/0033-295X.101.4.547)); a equipe confere se a árvore não dividiu demais o ramo favorito.
4. **Cinco porquês só dentro de um ramo,** para descer até onde dá para agir, com cada passo marcado como causa única ou ramo, como pede a `think-five-whys` da [thinking-framework-skills](https://github.com/product-on-purpose/thinking-framework-skills). Sozinhos, eles levam a uma cadeia única e dependem de quem pergunta ([Card](https://doi.org/10.1136/bmjqs-2016-005849)).
5. **Onde parar:** quando a próxima causa já não muda o que uma solução teria de fazer, quando sai do alcance do propósito, ou quando nenhuma evidência separa os próximos passos, e aí vira pergunta. As análises de causa raiz costumam parar cedo, numa causa só e em correções fracas ([Peerally et al.](https://doi.org/10.1136/bmjqs-2016-005511)).
6. **"Erro humano" não fecha cadeia:** pergunta-se o que tornou o erro provável: carga, desenho, informação, incentivo ou treino.
7. **Laços:** quando a falha alimenta a própria causa ("o ônibus atrasa, as famílias desistem, a rota perde crianças, a rota é cortada, o ônibus atrasa mais"), o laço fica desenhado, com o sentido de cada elo.
8. **Causas rivais:** toda falha central tem pelo menos duas causas, de origens diferentes: a sua, a da equipe e a dos geradores cegos. A rival é uma alternativa qualquer, e não só o oposto ([Hirt e Markman](https://doi.org/10.1037/0022-3514.69.6.1069)).
9. **Cadeia de mecanismo e o que se deveria observar, escritos antes:** cada causa é uma cadeia, "A leva a B, que leva à falha", com cada elo. Antes da busca, o cartão diz o que se deveria observar se a causa for verdadeira e se for falsa, como no process tracing da [thinking-framework-skills](https://github.com/product-on-purpose/thinking-framework-skills) ([Collier](https://doi.org/10.1017/S1049096511001429)).
10. **Busca a favor e busca contra, separadas,** em pesquisadores diferentes, com as perguntas contra escritas no cartão: "onde a falha acontece sem esta causa?" e "onde a causa está presente e a falha não?" ([Hart et al.](https://doi.org/10.1037/a0015701); [Sharma, Liao e Xiao](https://arxiv.org/abs/2402.05880)).

**Evidência tipada:** cada evidência entra com o tipo de teste:

| Teste | Se passar | Se falhar |
| --- | --- | --- |
| Palha ao vento | Aumenta um pouco a confiança | Diminui um pouco |
| Aro | A causa continua viva, sem ser confirmada | A causa cai |
| Arma fumegante | A causa fica confirmada | A causa não cai |
| Duplamente decisivo | Confirma esta causa e derruba as rivais | A causa cai |
| Não diagnóstica | Combina com todas as rivais: fica registrada e não pesa | — |

**Força da evidência,** que exige dependência e mecanismo, como nas ciências da saúde ([Russo e Williamson](https://doi.org/10.1080/02698590701498084)); os modelos confundem correlação com causa ([Jin et al.](https://arxiv.org/abs/2306.05836)), e o crítico e a verificação conferem:

| Força | Quando |
| --- | --- |
| Forte | A dependência foi medida (a falha muda quando a causa muda, por experimento, experimento natural ou comparação com controle), o mecanismo tem fonte, a causa passou num teste de aro ou de arma fumegante, e a busca contra não achou a falha, igual, sem ela |
| Média | Dependência e mecanismo têm fonte, mas a dependência vem de comparação sem controle ou de um contexto parecido, e não do mesmo |
| Fraca | Mecanismo com fonte e dependência só por relatos ou casos |
| Hipótese | Sem fonte, ou só correlação, sem mecanismo |

**Depois da busca:**

1. **Linhas, e não matriz:** cada causa é uma linha, com as suas evidências e os tipos ao lado. Nada de contar inconsistências nem de somar pesos: a matriz de hipóteses concorrentes não melhorou os julgamentos e deu peso a evidências pseudodiagnósticas ([Karvetski e Mandel](https://doi.org/10.1017/s1930297500008159); [Dhami, Belton e Mandel](https://doi.org/10.1002/acp.3550)), enquanto as hipóteses em linhas reduziram o viés de confirmação ([Dhami et al.](https://doi.org/10.1186/s41235-024-00560-y)).
2. **A observação que falta:** cada cartão diz qual seria a observação mais decisiva que ainda não se tem. Se for barata, vira pesquisa agora; se não, pergunta em aberto (CIR, seção 15).
3. **Verificação:** depois da elaboração, a equipe de verificação, com especialistas que não elaboraram as árvores e sem saber a autoria, recebe as afirmações técnicas dos cartões (a dependência, o mecanismo e o tipo de cada teste) e entrega o parecer P-2.2-1, afirmação por afirmação: sustenta, não sustenta ou incerto, com as contas e as fontes. O parecer não julga as causas; isso é do conselho.
4. **Conselho:** completo Evidência, às cegas, sobre os cartões de causa, com o parecer. Até 12 cartões por conselho, a começar pelas falhas centrais; com mais, outro conselho, e o que sobrar desce para rápido, com registro.
5. **Decisão:** por falha central, você decide que causas ficam como principais, que rivais ficam vivas (marcadas "rival viva", para os temas seguintes) e o que vira pergunta. "Causa desconhecida", com a observação que a resolveria, é uma resposta válida.


Base: S15 §6.3. Referência de método; fontes científicas citadas pelo plano não foram reconferidas nesta implementação.
