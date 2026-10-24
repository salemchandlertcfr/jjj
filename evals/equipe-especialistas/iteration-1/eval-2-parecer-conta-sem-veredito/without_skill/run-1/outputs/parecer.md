# Parecer de verificação técnica

**A1 — Não sustentada.** Observar zero erros em 50 ensaios não prova que a taxa de erro seja exatamente zero. Uma amostra finita sem erros é compatível com taxas positivas: sob o modelo de A2, a probabilidade desse resultado é `(1 - p)**50`.

**A2 — Correta, condicionada ao modelo.** Para 50 ensaios Bernoulli independentes, com a mesma probabilidade de erro `p`, o limite superior unilateral exato de confiança de 95% resolve `(1 - p)**50 = 0.05`, resultando em `p = 1 - 0.05**(1/50)`.

## Cálculo executado em Python

```python
n = 50
alpha = 0.05
limite_superior = 1 - alpha ** (1 / n)
print(limite_superior)
print(100 * limite_superior)
```

Resultado calculado: **0.058155079116972**, equivalente a **5.815507911697%**, aproximadamente **5,82%**.

## Limites e decisão

O resultado pressupõe ensaios Bernoulli independentes, probabilidade de erro constante e registro correto dos resultados. A independência e as demais condições não foram verificadas nos dados; nenhum conjunto de dados foi fornecido. O nível de confiança descreve a cobertura do procedimento em repetições sob esse modelo, não uma probabilidade de 95% atribuída ao parâmetro após esta observação. O limite não demonstra ausência de erros nem garante desempenho em outras condições.

**Decisão sobre a hipótese inteira: não emitida.** A hipótese completa, seus critérios de aceitação e a adequação dos dados ao modelo não foram especificados. As conclusões sobre A1 e A2 não bastam para aprová-la ou reprová-la. Cabe ao solicitante decidir após explicitar a hipótese, a tolerância ao erro e as evidências necessárias.

Não foram realizadas pesquisa externa, reunião, revisão crítica ou verificação da independência dos dados. Este parecer usa apenas as afirmações fornecidas e o cálculo Python registrado acima.
