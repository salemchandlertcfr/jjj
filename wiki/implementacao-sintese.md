# Implementação da síntese do CIR

Estado: `0.1.0-alpha.1`, protocolo e apoio local testado. Plano selecionado: [S16](../sources/originais/plano-cir-sintese.md), preservado a partir do ZIP; metodologia [S01](../sources/originais/skill-creator.md).

## Propósito registrado antes do código

Consolidar o dossiê no CIR sem perder nem inventar: origem em cada frase, cópia literal do que obriga ou promete, dissenso preservado, passagem testada por leitores novos e prontidão por evidência. A skill documenta a escolha; não escolhe nem altera o conceito. Fontes: S16 §§1, 4 e 6.

O apoio local deve demonstrar integridade das origens Git, cobertura independente do que foi montado, remontagem estável, projeções restritas para agentes e vínculo de verificações à versão atual. Aprovação humana e persistência continuam com a condutora. Pesquisa, leitores Claude, modelo de juiz, isolamento e julgamento semântico não serão substituídos por declarações de execução.

## O que foi implementado

O [pacote universal](../skills/cir-sintese/SKILL.md) contém cartões literais do tema 6 e das seis sub-etapas, referências por tarefa, formatos, briefs, modelos e seis CLIs Python/Git. Não tem dependências Python externas. Base: S16 §§4–12.

| Auxiliar | Comportamento local |
| --- | --- |
| `cir.py` | Monta 17 seções de objetos Git, copia texto/dados, ordena superados e famílias; sela versões anteriores, prepara redator/verificador, confere montagem, ligações, números e cobertura, lista usos. |
| `pacote.py` | Gera nove partes das mesmas fontes e consolida estacionamento, preservando origens e motivos. Abstenção não gera pacote da Etapa 2. |
| `leitor.py` | Estado de previstas, três leitores, reformulações antes das perguntas, dois juízes anônimos, classificação e parada/rodada extra. |
| `pronto.py` | Critério único em pronto.yaml; evidência por item/arquivo/seção/hash/versão, auditoria e registro externo de consentimento ao commit. |
| `retrospectiva.py` | Anterioridade Git ou reconstrução marcada, decisão separada de desfecho, Brier factual, surpresa, melhorias e projeção de aprendizado sem conteúdo. |
| `cartoes.py` | Confere seis cartões contra índice explicitamente fornecido; não instala o índice ausente da condutora. |

A interface usa projeções JSON em Markdown nos registros e em `06-blocos.md`. Os [formatos](../skills/cir-sintese/references/formatos.md) explicam campos, hashes e diferenças. O inventário é comparado aos registros completos de origem: omitir o mesmo item de blocos e inventário não evita o bloqueio. A origem deve bater com o estado, working tree e commit base; correção exige registro e remontagem. As cópias vêm do objeto Git, não de texto repetido pelo redator.

Cada ligação tem afirmações com spans que cobrem todo o texto, referências e sessões distintas. Tarefas de verificador omitem autoria; cada veredito aponta ao hash do texto/fontes atuais. Isso não demonstra atomicidade ou sustentação semântica. O CIR inteiro pode ser comparado à remontagem para detectar edição manual. Documentos gerados continuam NÃO APROVADOS até a condutora coletar/persistir o sim à versão e ressalvas.

## Usar e verificar

Instale a pasta `skills/cir-sintese` no hospedeiro e leia `SKILL.md`. Modelos de entrada são parciais, sem projeto/modelo de produção. Na raiz:

```bash
python3 -B -m unittest discover -s tests -p test_cir_sintese.py -v
python3 -B scripts/empacotar_skill.py --skill skills/cir-sintese --destino /tmp/cir-sintese.skill
python3 -B skills/cir-sintese/scripts/cir.py --help
```

Os [comandos da skill](../skills/cir-sintese/SKILL.md) são relativos à pasta instalada; `--git` aponta ao dossiê autorizado. Nenhum comando grava no dossiê: a condutora persiste os mapas externos `arquivos` e demais relatórios em sua transação.

Os **38 testes** usam dossiês temporários fictícios. Validam bloqueios, cópia e remontagem, omissões, verificação obsoleta, pacotes, passagem, quatro evidências de pronto plantadas, aprovação e retrospectiva. O pacote extraído roda montagem/conferência/passagem de arquivos à Etapa 2/3 pela CLI. A [avaliação textual](../evals/cir-sintese/README.md) marcou 12/12 com skill e 6/12 sem, uma execução por caso/condição; resultado limitado à rubrica, revisão humana pendente. Benchmark/viewer oficiais são reproduzíveis.

## Limites de entrega

O contrato local é explícito e mais restrito que aceitar prosa livre dos temas. A condutora precisa adaptar `registrar.py`, `dossie_init.py`, `brief.py`, o índice e sua persistência; esses componentes estão ausentes ou incompletos aqui. Não foram executados pesquisa, vigia/pendencias reais, modelo Claude, bibliotecas curadas, isolamento ou espelho Notion. A CLI de pronto lê evidências declaradas e faz triagem própria; não afirma ter executado serviços externos.

Hashes, sessões e registros JSON não autenticam aprovação ou provam anterioridade cognitiva. Semântica da evidência, novidade da reconstrução, equivalência de reformulações, qualificadores omitidos e contradições exigem agentes/critico reais. Suspeitas lexicais podem incluir proibições legítimas. A condutora deve marcar na apresentação “aprovado sem teste de passagem” se a pessoa pular I14; os auxiliares não carimbam documentos como finais nem publicam páginas.

S16 §13 pede testes repetidos, cegos, 40 ligações, lacunas plantadas e aceite do Motor com gabarito prévio da pessoa: continuam pendentes. Os números de alvo do plano não são métricas já obtidas. A suíte geral permanece limitada pelas ausências de condutora/conselho e três links antigos; veja [pendências](pendencias.md).
