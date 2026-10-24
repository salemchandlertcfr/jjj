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
