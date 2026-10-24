## 9. Exemplos limpos e contaminados

Os exemplos que a skill mostra aos agentes, no `exemplos.md`, nos briefs do crítico e no `grill.md`. A você, nenhum aparece antes da sua versão (regra 12). Todos vêm de casos de fora dos testes: o transporte escolar na zona rural, o estoque de um pequeno restaurante e um sistema distribuído.

| Peça | Contaminado | Sinal | Limpo |
| --- | --- | --- | --- |
| Etapa do job | "Conferir a lista no app" | Meio e produto | "Confirmar que todas as crianças embarcaram" |
| Etapa do job | "Fazer o pedido no sistema do fornecedor" | Meio e produto | "Repor o que vai faltar antes que falte" |
| Falha | "Falta um aplicativo que avise o atraso" | Falta de solução no lugar da falha | "A escola só sabe do atraso quando ele acontece" (2.1-6) |
| Falha | "O restaurante não usa um sistema de estoque" | Falta de solução | "O ingrediente acaba no meio do pico de sexta-feira, 3 vezes por mês" |
| Causa | "Os motoristas são irresponsáveis" | "Erro humano" fecha a cadeia; sem mecanismo | "O contrato paga por quilômetro, e rota longa rende mais" (2.2-3), com o que se deveria observar |
| Causa | "Nas semanas de mais falta de ingrediente, as vendas foram maiores; logo, o volume causa a falta" | Só correlação, sem mecanismo | "O pedido sai na segunda, pela média do mês, e o pico de sexta não entra na conta" (mecanismo, com ficha); "quando o pedido passou para quinta, a falta caiu" (dependência, com ficha) |
| Rival | "A rival é: não é a rota" | O oposto, e não uma alternativa | Outra cadeia: "o contrato não cobra pontualidade" |
| Contradição | "Consistência × disponibilidade: a equipe nunca conseguiu as duas; é de princípio" | "Ninguém conseguiu" como prova | De princípio só com o teorema: numa rede assíncrona em que mensagens se perdem, nenhum sistema garante ao mesmo tempo consistência atômica e resposta a toda requisição ([Gilbert e Lynch](https://doi.org/10.1145/564585.564601)). Com as premissas escritas, sem partição de rede o conflito pode ser quebrável |
| Contradição | "Chegar a tempo × sair mais tarde de casa: é física, não tem jeito" | "De princípio" sem premissas nem conta; a lei vale só no limite | O 2.3-1: t ≥ d / v máx., com as premissas, a conta e a folga entre o limite e o hoje marcada como quebrável (seção 8.4) |
| Contradição | "Estoque × desperdício: o jeito é pedir na quinta" | Solução no mapa | O par de parâmetros, com a forma física; a ideia vai para o banco |
| Projeção | "O mercado de transporte escolar vai crescer 8% ao ano" | Mercado; número sem faixa | A visão de fora, pela classe de referência, com as taxas-base e as faixas (seção 8.5) |
| Projeção | "Em 5 anos, veículos autônomos resolvem isso" | Tecnologia e adoção | O que acontece se nada mudar; tecnologia de uso geral só como tendência com fonte |
| Espaço K | "Ninguém sabe se chegar atrasado atrapalha o aprendizado" | Incerto sem o que o resolveria | O 2.5-2, com o estudo que resolveria e quanto custaria |
| Espaço K | "É impossível manter a estrada transitável na chuva" | Limite de hoje como impossibilidade | Limite de hoje, com a data (2.3-4), nas fronteiras |
| Analogia | "Dá para fazer como a coleta de leite e criar pontos de encontro" | Analogia como solução | O 2.5-4, com a função e o que corresponde ao quê; a ideia vai para o banco |
| Caso | "O município que resolveu tudo com rastreio por GPS" | Escolhido pelo resultado; solução no caso | Um caso com o antes, o desfecho e o porquê de ser difícil para qualquer solução (seção 8.7) |
| Caso | "Em 2021, a rota 5 atrasou porque o motorista dormiu, e ninguém percebeu a tempo" | O desfecho misturado ao antes | O que se sabia até a data de corte, sem o desfecho; o desfecho à parte |
- **O `sinais.py` pega o que tem marca no texto:** preço, mercado, concorrente, disposição a pagar; produto e tecnologia fora do "como é feita hoje"; "de princípio" sem premissas e "impossível" sem teorema; causa sem ficha; "erro humano" no fim de uma cadeia; palavras de correlação ("associado a", "quanto mais… mais") num cartão sem mecanismo; "dá para" e "basta" no mapa. Rival que é só o oposto, árvore sem ramo e caso escolhido a dedo quase nunca têm marca; quem os pega são o crítico, a verificação e o conselho.

Base: S15. Operadores não são executores; só a condutora despacha agentes.
