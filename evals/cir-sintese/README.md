# Avaliação de cir-sintese

Estado: alpha local, 24/10/2026. Plano [S16 §13](../../sources/originais/plano-cir-sintese.md);
metodologia [S01](../../sources/originais/skill-creator.md).

## Testes locais

Na raiz: `python3 -B -m unittest discover -s tests -p test_cir_sintese.py -v`.
São 38 testes, com dossiês Git fictícios, sem pesquisa ou modelos reais.
Cobrem hashes e origens, leitura regular sem symlink/traversal, cobertura
contra registros completos, seis omissões, cópias, histórico, abstenção,
projeções, decomposição integral, veredito atual, sinais lexicais/números,
pacotes das mesmas fontes, deduplicação com motivos, passagem em fases,
modelos/sessões declarados, três rodadas, quatro itens de pronto plantados,
aprovação por commit, retrospectiva e privacidade do aprendizado.
Cinco correções registradas preservam as outras cópias; editar o CIR gerado
é detectado. O pacote extraído percorre montagem, conferência e Etapas 2/3
pela CLI fora do repositório.

As quatro evidências plantadas são três ausentes e uma de outro item. Um JSON
rotulado I1 com texto irrelevante ainda pede crítico: correspondência de campos
não prova relevância semântica. Os juízes de passagem nos testes são dublês
de protocolo, não leitores que acharam lacunas reais.

## Seis propostas textuais

Os [três casos](evals.json) rodaram uma vez por condição, com e sem skill, em
sessões sem o histórico do autor. Outro avaliador leu as saídas pelo grader
oficial. Os nomes exatos de modelo não foram disponibilizados; não é ensaio
Claude nem comparação cega.

| Caso | Com skill | Sem skill |
| --- | --- | --- |
| Fidelidade à origem | 4/4 | 2/4 |
| Passagem com lacuna central | 4/4 | 2/4 |
| Retrospectiva e privacidade | 4/4 | 2/4 |

A diferença nesta rubrica foi preservar literalmente o dissenso/remontar,
explicitar retorno da mudança de núcleo/reconferência e excluir testes do
aprendizado/reconstruir às cegas. O baseline também rejeitou garantias,
fechamento por “entendi” e viés de resultado; não se descreve sua saída como
falha geral. Os critérios são compostos: paráfrase fiel não conta como cópia
literal, e autorização genérica não comprova consentimento registrado.
O critério da melhoria usa “ou”: a rejeição da frase genérica passou mesmo
sem todos os campos de dono/skill/seção. Essas ressalvas e ambiguidades
permanecem nos grading.json, sem ajuste para favorecer a skill.

São **propostas textuais**, sem CIR real, agentes Claude, pesquisa C-6.5 ou
leitores independentes realizados. Uma execução por caso não mede variância,
causalidade, fidelidade semântica completa ou ganho no aceite do Motor.
`execution.md` é relato declarativo, sem transcrição instrumentada. Tokens,
tempo, chamadas, erros e duração nativa ficam desconhecidos, sem estimativa.
Revisão humana pendente; nenhum feedback foi fabricado.

Veja o [viewer oficial estático](avaliacao.html), os [dados](iteration-1/benchmark.json)
e os [39 artefatos com hashes](iteration-1/artifacts.sha256).

## Reprodução e pendências

Auxiliares externos do skill-creator Anthropic, revisão
`dbd4588f9e1033efb41dad4bef2f7947c8993d44`, sob Apache-2.0; não vendorizados.
O viewer HTML é gerado pelo auxiliar oficial.

```bash
python3 -B scripts/reproduzir_avaliacao_sintese.py --skill-creator /caminho/skills/skill-creator
python3 -B scripts/reproduzir_avaliacao_sintese.py --skill-creator /caminho/skills/skill-creator --check
```

O script confere hashes, assertions e contagens, usa agregador oficial em
cópia temporária compatível e remove zeros substitutos de métricas antes
de salvar. Não chama modelos nem muda saídas; reproduz benchmark/viewer.

Os [20 pedidos de acionamento](acionamento.json) estão preparados, não executados.
Restam os ensaios de 40 ligações com infidelidades sutis, lacunas reais/controle
limpo, vigia e fontes reais plantadas, comparações A/B/C repetidas e cegas,
plataformas e aceite do Motor com gabarito prévio da pessoa. As metas de S16
não foram convertidas em resultados desta avaliação local.
