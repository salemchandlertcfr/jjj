# Simulação exploratória

Estado: código recebido e executado; experimento de brinquedo, sem validação empírica do método. Revisão: 2026-10-22.

## O que o modelo representa

[S03](../sources/originais/simulacao_etapa1.py) compara oito variantes da concepção ideal. Sorteia ideias para o núcleo, a cadeia até o resultado e tangentes, além de dano, ruído de avaliação, surpresa e custos artificiais. A formulação principal é `Q = núcleo ** (1-w) * cadeia ** w`; há uma alternativa aditiva. O valor líquido é `net = A*Q - T`.

| Variante | Escolha representada |
| --- | --- |
| V1 | Foco no núcleo; cadeia tratada depois. |
| V2 | Núcleo e cadeia, sem tangentes. |
| V3 | Divergência máxima e CIR amplo. |
| V4 | Divergência ampla, CIR estreito e abstração de tangentes. |
| V5 | CIR amplo elaborado antes da convergência. |
| V4+A | Avaliação extra. |
| V4+R | Mais ideias. |
| IDEAL | Esboço integrado curto, triagem e avaliação forte. |

`Q` expressa qualidade artificial; `T1` e `T`, custos convencionados da Etapa 1 e totais; `comps`, quantidade de componentes; `surp`, surpresas reconhecidas; `dano`, presença de dano. `rep` é uma contagem proxy cuja regra varia por variante. A coluna `melhor%` escolhe vencedores **somente entre V1–V5**. O `nan` dessa coluna para as outras variantes significa ausência do campo, sem indicar falha numérica da execução.

## Executar

Na raiz, com Python **3.11 ou superior** para a dependência fixada:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-experimentos.txt
.venv/bin/python -B sources/originais/simulacao_etapa1.py 100
```

Sem argumento, o programa usa 6.000 rodadas na série principal. Os experimentos extras C–F têm contagens fixas: executam 160.000 avaliações de variante independentemente do argumento. Reduzir para 100 não torna o conjunto inteiro uma amostra de 100. `-B` evita criar bytecode junto às fontes.

## Verificação realizada

Em 22/10/2026, com **Python 3.12.14 e NumPy 2.3.5**, a CLI com `100` terminou com código 0, 104 linhas de saída e stderr vazio, em aproximadamente 23 segundos neste ambiente.

Uma checagem adicional exercitou 640 configurações de `rodada`: seeds 0–63, cinco conjuntos de premissas e formas multiplicativa/aditiva. Verificou repetição determinística no mesmo ambiente, oito variantes, valores finitos, `Q` em [0,1], tempos positivos, coerência de `net` e ausência de dano quando sua probabilidade é zero. Isso verifica propriedades técnicas, não a superioridade de uma variante em projetos reais.

## Limites e cuidados de interpretação

- Custos em dias, distribuições, ganhos de avaliação e peso `A` foram assumidos. Resultados e rankings dependem dessas escolhas; não são estimativas de prazo ou eficácia real. [S09, §10](../sources/originais/concepcao-ideal-solucao.md) também explicita essa limitação.
- Amostras vazias não são tratadas: `resumo([])` produz NaN e avisos. `n=1` gera séries vazias por `NR//2=0`; filtros e subfaixas também podem ficar vazios. Esse NaN tem causa diferente do campo ausente em `melhor%`.
- A CLI não valida adequadamente o domínio das entradas. Parâmetros fora das faixas previstas não estão cobertos pela verificação.
- Determinismo foi confirmado na versão testada. As variantes consomem um gerador em sequência e só compartilham parte das amostras; a comparação não é perfeitamente pareada. Não se garante igualdade entre versões de NumPy.
- `v5leve`, nos experimentos extras, altera uma constante global temporariamente. O fluxo sequencial funcionou; isso não estabelece segurança para chamadas concorrentes.

O código original permanece intacto. Novos experimentos ou correções devem ter arquivo próprio e registrar premissas, ambiente e relação com S03. O [método](metodo-ideal.md) e suas [pendências](pendencias.md) exigem avaliação além deste modelo.
