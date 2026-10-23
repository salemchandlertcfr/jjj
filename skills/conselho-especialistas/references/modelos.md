# Mapa de modelos reais

Base: S11 §§9, 10, 13 e 17. S11 é a revisão ativa desta implementação e adota
Claude primeiro; S04 é histórico. Não imponha múltiplas famílias para satisfazer
uma regra histórica substituída, nem diga que a integração existe porque há plano.

Na versão inicial, membros, crítico, relator e normalizador usam o mesmo modelo
de juiz Claude escolhido pelo usuário. O mapa é privado e separado dos briefs.
Não fixe nomes comerciais, versões futuras, preços ou qualidade a partir das
tabelas históricas da fonte. Verifique de novo por projeto e quando houver troca.

Antes de executar, registre:

1. A escolha real do usuário e as famílias autorizadas.
2. Identificador exato do modelo e nível de juiz, disponibilidade e data da conferência.
3. Via concreta de transporte, autenticação fornecida pelo ambiente sem copiar segredos,
   ferramentas disponíveis, isolamento e possibilidade de auditar eventos.
4. Sessões produtoras que precisam ser excluídas e restrições de sigilo.
5. Alternativa de mesmo nível previamente autorizada ou decisão de esperar.

O contrato JSON mínimo do juiz é
`{familia:"anthropic", modelo:<identificador real>, nivel:"juiz", via:<transporte>, autorizado:true}`.
Consulte [formatos](formatos.md) e o modelo preenchível; campos adicionais de
capacidade e autorização precisam de referência verificável, não de texto gerado.

Confirme que o modelo pedido foi usado de fato. Grave o efetivo no painel
privado e no registro de transporte, sem expô-lo aos membros ou à apresentação
prévia à decisão. A identidade pode ser revelada depois da decisão, se o usuário
pedir; não há publicação automática da chave.

Falha de transporte permite uma nova tentativa por assento. Depois, use somente
alternativa autorizada do mesmo nível ou preserve o trabalho e pergunte se o
usuário prefere esperar ou trocar. Não rebaixe um juiz, nem troque silenciosamente
o mapa. Se a plataforma só oferecer outro modelo, declare indisponibilidade.

Outras famílias pertencem à fase futura de comparação cega: primeiro demonstrar
ganho no papel e qualidade equivalente no banco de calibração. Na suspeita de
autopreferência, o crítico é o primeiro papel a testar outra família. Este alpha
não anuncia essa política futura como capacidade multi-provedor implementada.

Registre custos observados, unidade, moeda quando aplicável, modelo efetivo,
tempo, falhas e origem da medição. Use `null`/desconhecido para custo indisponível;
zero só quando verificado. Refaça a linha de base ao mudar o mapa. Não estime
preços atuais copiando números da fonte.
