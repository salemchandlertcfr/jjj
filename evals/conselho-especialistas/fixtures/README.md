# Banco controlado do conselho

Os três casos são sintéticos e suas fontes são dublês identificados. URLs `example.org/fixtures/` servem como identificadores do banco; não alegam artigos ou estudos reais. O campo `verificada: true` indica apenas que a ficha fixa foi conferida contra a premissa declarada do cenário.

- `01-certeza-total.json`: limite de princípio por entradas indistinguíveis; não escolher um vencedor geral.
- `02-dissenso-fonte-desconhecida.json`: preservar desacordo e incerteza; recusar ficha inexistente como lastro.
- `03-troca-sem-evidencia.json`: recusar mudança de posição motivada só pela opinião alheia e limitar a uma troca.

Cada arquivo separa o pedido do conselho, o mapa fictício do juiz e as expectativas da avaliação. As expectativas e os marcadores de autoria não devem ser enviados aos membros. O mapa não representa disponibilidade de um modelo externo.

Para obter as fichas fixas:

```bash
python3 evals/conselho-especialistas/fixtures/pesquisa_stub.py --cenario certeza-total --modo refutar
```

O helper não faz busca e não substitui a futura `pesquisa-cientifica` em uso real. Ele permite avaliar o julgamento sem confundir falha de busca com falha de raciocínio.
