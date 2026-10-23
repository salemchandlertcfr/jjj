# Avaliação de especialistas

Estado: apoio local testado e primeiro ensaio textual, em 23/10/2026.
Plano: [S13 §14](../../sources/originais/plano-especialistas.md).
Método: [S01](../../sources/originais/skill-creator.md).

## Testes de infraestrutura

Na raiz: `python3 -B -m unittest discover -s tests -p test_especialistas.py -v`.
Os 33 testes cobrem cobertura, formação, biblioteca, transporte, fila e regra
de admissão. O teste parametrizado inclui as [30 violações plantadas](fichas-plantadas.json),
todas rejeitadas. Bibliotecas Git e o adaptador executor são dublês temporários,
sem especialidade científica real ou validação Claude. O adaptador testado
recebe enunciados e blocos, sem gabaritos, e devolve respostas controladas;
seu resultado positivo não admite uma esp de produção.

## Seis ensaios textuais

Os [três casos](evals.json) cobrem problema antes do catálogo, formação e
contexto, e curadoria com regressão/empate. Cada um rodou uma vez com a skill
e outra sem, em sessões sem histórico do autor. Um avaliador separado usou
o grader oficial. Os nomes exatos de modelo não foram disponibilizados;
não é teste Claude nem avaliação cega. Saídas são propostas, não execuções
de equipes ou pesquisa.

| Caso | Com skill | Sem skill |
| --- | --- | --- |
| Problema antes do catálogo | 4/4 | 4/4 |
| Dose, papel e distante | 4/4 | 4/4 |
| Curadoria e empate | 4/4 | 4/4 |

**Empate nesta rubrica**, sem evidência de ganho. Os prompts explicitam várias
regras, e o terceiro é ambíguo sobre duas versões: o baseline liga a revisão
de outra versão à regressão e presume que a anterior não estava admitida.
Passou na assertion de não substituir, com ressalva do avaliador. O segundo
caso não mede todos os acessos por papel. As assertions e esses limites
continuam disponíveis nos `grading.json`; não foram ajustados para favorecer
a skill após o resultado.

Veja o [viewer oficial estático](avaliacao.html), o [benchmark](iteration-1/benchmark.json)
e os [hashes dos artefatos](iteration-1/artifacts.sha256). Revisão humana
pendente; o viewer permite baixar feedback, que não foi fabricado.
`execution.md` contém relatos, sem transcrição instrumentada; claims de
processo não são comprovadas só pelo autorrelato.

## Métricas e reprodução

Os intervalos de parede preservados em `timing.json` usam janelas diferentes;
alguns excluem leitura inicial. Não há tempo médio/delta comparável no
benchmark. Valores brutos ficam como `observed_interval_seconds`; tempo
comparável, tokens, modelo exato e duração nativa ficam desconhecidos.
Não converter caracteres em tokens nem tratar 12 assertions como 12 runs.

Com auxiliares oficiais externos `skills/skill-creator` de `anthropics/skills`,
revisão `dbd4588f9e1033efb41dad4bef2f7947c8993d44`:

```bash
python3 -B scripts/reproduzir_avaliacao_especialistas.py --skill-creator /caminho/skills/skill-creator
python3 -B scripts/reproduzir_avaliacao_especialistas.py --skill-creator /caminho/skills/skill-creator --check
```

O script confere hashes oficiais e dos registros, valida as contagens,
agrega em cópia temporária compatível com o upstream e remove métricas
substitutas antes de salvar. Não chama modelos nem altera as saídas.

## O que não foi medido

Os [20 pedidos de acionamento](acionamento.json) estão preparados, não
executados. Nenhuma esp real foi curada: os testes de ganho em conhecimento,
erro plantado, identificabilidade, recrutada × fixa, uma × duas propostas,
distante, comparação de modelos e transporte em plataformas seguem pendentes.
Problemas fechados das futuras esp ficam fora do pacote/repositório de
desenvolvimento; o escritor nunca recebe o banco. A avaliação de recrutamento
fica fora do pacote distribuído para não carregar casos no contexto dos agentes.
