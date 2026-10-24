# Parecer de verificação técnica

**A1 não sustenta a conclusão de taxa exatamente zero. A2 sustenta a fórmula, condicionalmente ao modelo binomial descrito abaixo.** Este parecer trata das duas afirmações; não aprova nem reprova a hipótese inteira. Essa decisão permanece com a pessoa solicitante ou com o conselho competente, com critérios e evidências próprios.

## A1 — “Observar zero erros em 50 ensaios prova que a taxa de erro é zero”

- **Conclusão:** não sustenta.
- **Justificativa:** a frequência observada é zero, mas uma amostra finita sem erros também pode ocorrer quando a taxa populacional é positiva. Sob ensaios independentes com taxa comum de 1%, a probabilidade de nenhum erro em 50 ensaios é `0.99**50 = 0.6050060671375364`, aproximadamente 60,50%. Esse contraexemplo basta para invalidar a alegação de prova; não estima a taxa real destes dados.
- **Lastro:** identidade matemática `P(X=0)=(1-p)**50` sob o modelo binomial e conta C3, executada em Python e reproduzida pelo auxiliar da skill. Sem fonte externa.
- **Incerteza:** a taxa real e o processo de coleta não foram fornecidos. Mesmo sob o modelo, o resultado observado não distingue taxa exatamente zero de todas as taxas positivas.
- **Especialidade pertinente:** inferência estatística; nenhum bloco `esp-*` foi fornecido e nenhuma autoridade de especialista é atribuída.
- **Mudaria se:** a afirmação fosse reformulada para “a frequência de erros observada foi zero”. Provar taxa populacional exatamente zero exigiria fundamento adicional que não decorre dessa observação finita.
- **Destino:** rejeitada a inferência de prova; preservada a informação de zero erros observados em 50 ensaios.

## A2 — “Sob ensaios Bernoulli independentes, o limite superior unilateral de 95% com zero erros em 50 é 1 - 0.05**(1/50)”

- **Conclusão:** sustenta, condicionalmente a ensaios Bernoulli independentes com a mesma taxa de erro `p`, fixa durante os 50 ensaios, e ao limite exato binomial unilateral de 95%.
- **Justificativa:** nesse modelo, `P_p(X=0)=(1-p)**50`. O limite superior `u` satisfaz `(1-u)**50 = 0.05`, portanto `u = 1 - 0.05**(1/50)`.
- **Lastro:** derivação acima e contas C1, C2 e C4 executadas e reproduzidas em Python. Resultado: `u = 0.058155079116972264`, ou `5.815507911697226%`, aproximadamente **5,82%**.
- **Incerteza e limites:** independência, taxa comum, registro correto dos erros e plano de amostragem não foram verificados nos dados. Dependência, heterogeneidade das taxas ou seleção dos ensaios podem alterar a aplicação do limite. Ensaios independentes com taxas diferentes não formam, por essa condição isolada, o modelo binomial usado aqui. A conta certa não valida esses pressupostos.
- **Especialidade pertinente:** inferência estatística; sem bloco `esp-*` ou autoridade externa conferida.
- **Mudaria se:** o modelo ou o procedimento pretendido fosse diferente, ou os dados contradissessem seus pressupostos; seria necessário recalcular ou considerar a aplicação indeterminada.
- **Destino:** incorporada como conclusão matemática condicional; aplicação aos dados reais permanece indeterminada.

O nível de 95% descreve a cobertura do procedimento em repetições sob o modelo. Não significa que há 95% de probabilidade de o parâmetro fixo estar neste intervalo, nem que a hipótese inteira foi aprovada.

## Registro do cálculo realmente executado

Arquivo [conta.py](conta.py), executado com Python 3.12.14:

```python
import json
from math import exp, isclose, log

n = 50
alpha = 0.05
limite_direto = 1 - alpha ** (1 / n)
limite_refeito = 1 - exp(log(alpha) / n)
prob_zero_no_limite = (1 - limite_direto) ** n
prob_zero_com_taxa_1_porcento = (1 - 0.01) ** n

assert isclose(limite_direto, limite_refeito, rel_tol=1e-12, abs_tol=1e-15)
assert isclose(prob_zero_no_limite, alpha, rel_tol=1e-12, abs_tol=1e-15)

print(json.dumps({
    "n": n,
    "alpha": alpha,
    "limite_direto": limite_direto,
    "limite_refeito": limite_refeito,
    "limite_percentual": 100 * limite_direto,
    "prob_zero_no_limite": prob_zero_no_limite,
    "prob_zero_com_taxa_1_porcento": prob_zero_com_taxa_1_porcento,
}, ensure_ascii=False, indent=2))
```

Saída preservada em [conta_resultado.json](conta_resultado.json):

```json
{
  "n": 50,
  "alpha": 0.05,
  "limite_direto": 0.058155079116972264,
  "limite_refeito": 0.058155079116972264,
  "limite_percentual": 5.815507911697226,
  "prob_zero_no_limite": 0.05000000000000002,
  "prob_zero_com_taxa_1_porcento": 0.6050060671375364
}
```

A conta foi refeita pela expressão equivalente com `exp` e `log` e conferida por substituição na probabilidade de zero erros. Também foi executado `ata.py contas` sobre [contas.json](contas.json): C1 a C4 retornaram `confere: true`, conforme [contas_conferencia.json](contas_conferencia.json). Isso constitui reprodução aritmética automática, sem revisão crítica independente.

## Escopo da entrega

Não houve reunião, pesquisa externa, consulta a especialistas ou revisão crítica. Não foram fornecidas posições individuais ou dissenso; não se atribui consenso. A única execução técnica foi a dos cálculos locais registrados. A decisão sobre a hipótese inteira não é extraída dessas duas conclusões.
