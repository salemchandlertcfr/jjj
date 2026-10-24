# Avaliação do mapa

Estado: apoio local verificado e primeiro ensaio textual, em 23/10/2026.
Plano: [S15 §13](../../sources/originais/plano-cir-mapa.md).
Metodologia: [S01](../../sources/originais/skill-creator.md).

## Verificação determinística

Na raiz: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p test_cir_mapa.py -v`.
Os 21 testes exercitam cronologia em Git real, anterioridade/evidência alteradas,
limites de força causal, princípio/contraexemplo, cotas, datas, sonda filtrada,
exclusões do sorteio, pares inseparáveis, congelamento, vazamento, pacote,
inventário contra a interface real de especialistas e extração/CLIs fora do projeto.
Dados e identidades Git são sintéticos; não há pesquisa ou fonte real nesses testes.

Há 30 mutações estruturais inválidas e 15 variações válidas do mesmo modelo.
Isso não equivale aos 30 mapas semânticos variados de S15 nem mede a qualidade
causal dos mapas. Rival que é uma negação disfarçada, árvore incompleta mas
plausível e retrospectiva parafraseada continuam exigindo crítico e avaliação real.
O [corpus lexical](frases-plantadas.json), escrito junto ao verificador, reúne
40 frases contaminadas e 20 limpas PT/EN: todas tiveram a classificação esperada.
A triagem nunca bloqueia. Não se estima generalização a partir desse corpus.

Os cartões conferem IDs/títulos/doses de S08 e texto literal de S15. A concordância
com o índice real da condutora não foi testada: o arquivo está ausente. Três links
antigos da documentação e sete erros gerais de importação/setup continuam por
condutora e módulos do conselho ausentes. Nenhuma dessas falhas foi ocultada.

## Ensaio textual com e sem skill

Os [três prompts e critérios prévios](evals.json) rodaram uma vez por condição,
em duas sessões novas sem histórico do autor. Cada condição compartilhou uma
sessão entre seus três casos; isso limita independência entre casos. Uma terceira
sessão aplicou o grader oficial, sem escrever as respostas. Não houve cegamento
de condição, isolamento de filesystem ou execução Claude/Notion. Os agentes
foram instruídos a não consultar a outra condição; isso não prova uma sandbox.

| Caso | Com skill | Sem skill |
| --- | --- | --- |
| Causa sem mecanismo | 4/4 | 3/4 |
| Falsa impossibilidade | 4/4 | 0/4 |
| Reserva exposta | 3/4 | 3/4 |
| Total | 11/12 | 6/12 |

Os números medem adesão textual a uma rubrica composta, não superioridade geral,
recall, causalidade real ou eficácia do método. O caso 2 sem skill conserva cautela
factual: faltam requisitos específicos da rubrica, como lei/conta, destinos banco/
estacionamento e classe de referência. Seu 0/4 não significa quatro afirmações
falsas. Parte do ganho favorece os procedimentos descritos explicitamente na skill.
Os prompts também já revelam as tensões a tratar; não são sala limpa ou teste oculto.

No caso 3 com skill, faltou pedir explicitamente novos casos não expostos, e o
critério composto falhou. A resposta preserva a cronologia e não promete que
substituir casos depois da solução restaure reserva cega. Em avaliação futura,
separar cenários antes/depois do congelamento tornará essa expectativa mais clara.
A falha foi preservada; nenhuma resposta foi reescrita para melhorar a nota.

A condição com skill ocorreu enquanto formatos.md ainda era escrito; o executor
registrou essa ausência. Portanto o ensaio não avalia a interface CLI final.
Os testes determinísticos posteriores exercitam o pacote completo, separadamente.
execution.md é relato declarativo, sem transcrição instrumentada. Modelo exato,
tokens, tempo nativo e custo permanecem desconhecidos; nenhum valor foi estimado.

Examine as respostas e evidências no [viewer oficial estático](avaliacao.html),
no [benchmark](iteration-1/benchmark.json) e nos [hashes](iteration-1/artifacts.sha256).
Revisão humana pendente; não houve feedback humano fabricado.

## Reproduzir agregação e continuar a avaliação

Auxiliares oficiais externos de anthropics/skills, revisão fixa
`dbd4588f9e1033efb41dad4bef2f7947c8993d44`, com hashes conferidos:

```bash
python3 -B scripts/reproduzir_avaliacao_mapa.py --skill-creator /caminho/skills/skill-creator
python3 -B scripts/reproduzir_avaliacao_mapa.py --skill-creator /caminho/skills/skill-creator --check
```

O script usa agregador e viewer oficiais, sem HTML próprio. Valores zero exigidos
pelo agregador existem apenas numa cópia temporária e são removidos da saída;
não representam medição. Auxiliares upstream não foram incorporados ao projeto.
Os registros preservados permitem reproduzir agregação/viewer, não a resposta
estocástica de cada agente.

Os [20 pedidos de acionamento](acionamento.json) estão preparados e não executados.
Permanecem avaliações semânticas, comparação de desenhos às cegas, usuários
simulados como teste de comportamento (nunca dados do fenômeno), memória real,
plataformas, permissões e custo. Regra de correspondência/recall do Anexo A e
aceite humano dos temas 2/3 exigem o responsável e uma execução real. Esses
requisitos não impedem publicar o alpha local com seu escopo explícito.
