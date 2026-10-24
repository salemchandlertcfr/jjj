# Avaliação da equipe

Estado: protocolo local testado e primeiro ensaio textual, em 23/10/2026.
Plano: [S14 §14](../../sources/originais/plano-equipe-especialistas.md).
Método: [S01](../../sources/originais/skill-creator.md).

## Testes de protocolo

Na raiz: `python3 -B -m unittest discover -s tests -p test_equipe.py -v`.
Os 40 testes cobrem pauta, ordem/fases, preparação e posição privadas,
compartilhamento integral, crítico, contribuições, dissenso, evidência,
verificação, integração, individual, fusão, contas, custos e vazamento/reparo.
A reunião CLI inteira passa depois de extrair o pacote fora do repositório.
Eventos e fontes são fictícios e identificados; nenhum teste comprova
execução Claude, qualidade de uma especialidade ou ganho de equipe real.

## Seis ensaios textuais

Cada um dos [três casos](evals.json) rodou uma vez com a skill e outra sem,
em sessões sem histórico do autor. Outro avaliador usou o grader oficial e
conferiu evidências nas saídas. O nome exato do modelo não foi disponibilizado;
não é teste Claude nem comparação cega. Pedidos solicitam artefatos textuais,
sem simular preparações/reuniões realizadas ou revisões inexistentes.

| Caso | Com skill | Sem skill |
| --- | --- | --- |
| Informação única e dissenso | 4/4 | 4/4 |
| Parecer com conta, sem veredito | 4/4 | 4/4 |
| Fusão sem média | 4/4 | 4/4 |

**Empate nesta rubrica, sem demonstração de ganho.** Todos os critérios
passam nas duas condições; os prompts já explicitam várias regras.
O caso 1 fornece as preparações e posições, portanto não mede recuperação
de informação distribuída. O caso 2 tem conta correta reproduzível, mas
código/resultado e relato não comprovam historicamente a execução pelo agente;
independência e taxa comum seguem condicionais. O caso 3 pede fusão de duas
sínteses dadas, sem medir reuniões paralelas ou eficácia de um crítico.
Críticas da rubrica permanecem nos `grading.json`, sem ajuste posterior
para favorecer a skill.

Veja o [viewer oficial estático](avaliacao.html), o [benchmark](iteration-1/benchmark.json)
e os [hashes dos artefatos](iteration-1/artifacts.sha256). Revisão humana
pendente; nenhum feedback foi fabricado. `execution.md` é relato declarativo,
sem transcrição instrumentada. As métricas de tokens, tempo, chamadas,
erros, duração nativa e modelo exato ficam desconhecidas.

## Reprodução e próximos ensaios

Com os auxiliares oficiais externos `skills/skill-creator` de `anthropics/skills`,
revisão `dbd4588f9e1033efb41dad4bef2f7947c8993d44`:

```bash
python3 -B scripts/reproduzir_avaliacao_equipe.py --skill-creator /caminho/skills/skill-creator
python3 -B scripts/reproduzir_avaliacao_equipe.py --skill-creator /caminho/skills/skill-creator --check
```

O script confere hashes oficiais e dos registros, valida as contagens e
agrega em cópia temporária. O auxiliar upstream exige números: zeros de
compatibilidade existem só nessa cópia e são removidos antes de salvar.
Não são tempo medido ou custo estimado. O viewer é o oficial, sem HTML próprio.

Os [20 pedidos de acionamento](acionamento.json) estão preparados, não executados.
Faltam comparação com melhor isolado e isolados com síntese, recuperação de
informação única, mudança de posição sem pressão social, analogias distantes,
reuniões paralelas, revisão crítica real, modelos, plataformas e custo.
Teste de protocolo e adesão textual não substituem os alvos científicos do plano.
