# Indução: padrões e revisão

S12, §§6.2 e 7. A tabela abaixo é lida por `perguntas.py`; regex opera sobre
texto sem acentos, em minúsculas. Erro impede envio. Suspeita exige reescrita
ou justificativa em `justificativas`, pela chave do padrão. Esta triagem não
detecta toda indução nem resolve semântica. Leia a mensagem inteira, inclusive
base e motivo: uma âncora fora da interrogação também direciona.

```json
[
  {"id":"concordancia","nivel":"erro","regex":"voce nao acha|nao seria melhor|concorda que|(?:certo|ne|faz sentido)\\s*\\?"},
  {"id":"recomendacao","nivel":"erro","regex":"recomendo|minha recomendacao|sugiro que|basta (?:dizer|responder) sim|aceita a recomendacao"},
  {"id":"elogio-concordancia","nivel":"erro","regex":"excelente ideia|otima ideia|voce (?:esta|tem) razao|concordo com voce|perfeito[!,.]"},
  {"id":"opcoes-reflexao","nivel":"erro","so_reflexao":true,"regex":"\\b(?:ou|prefere)\\b|(?:^|\\n)\\s*(?:[-*]|[a-c][).])\\s+"},
  {"id":"pressuposto","nivel":"suspeita","regex":"por que .* (?:falha|fracassa)|como .* (?:prova|provou|comprovou)|a fonte (?:prova|mostrou que)|obviamente|certamente"},
  {"id":"pergunta-dupla","nivel":"suspeita","regex":"\\be (?:qual|quem|quando|onde|como|quanto|por que)\\b"},
  {"id":"solucao-abertura","nivel":"suspeita","so_abertura":true,"regex":"\\b(?:dashboard|chatbot|blockchain|implementar|algoritmo|tela|botao|notificacao|aplicativo|recomendar)\\b"}
]
```

Exemplos:

| Indutora | Revisão neutra |
| --- | --- |
| Você não acha que o clique reforça o viés? | Que efeito você espera que priorizar pelo clique tenha sobre o que a pessoa vê? |
| Isso resolve, certo? | Que parte do problema isso resolve? |
| Por que a versão atual falha? | Como a versão atual se sai nesse caso? |
| Uns 30% fazem isso; e no seu caso? | No seu caso, em que parte das vezes acontece? |
| Prefere mostrar tudo ou só o relevante? | O que você quer que a pessoa veja primeiro? |
| A fonte prova; o que você muda? | Um estudo, força 4 e evidência indireta, relatou o efeito. O que isso muda na sua versão? |

“Ou não” e alternativas que a própria pessoa trouxe podem ser neutras, mas a
v1 sinaliza `ou` na reflexão de forma conservadora: prefira redação aberta.
Nomes de mecanismos na abertura são suspeitas, não proibições automáticas:
podem ser palavras da pessoa; cite a origem na justificativa.
