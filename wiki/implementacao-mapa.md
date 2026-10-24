# Implementação do mapa do fenômeno

Estado: `0.1.0-alpha.1`, protocolo e apoio local; revisão em 23/10/2026.
Plano selecionado: [S15](../sources/originais/plano-cir-mapa.md), preservado byte a byte do ZIP, com proveniência no manifesto. Metodologia: [S01, skill-creator](../sources/originais/skill-creator.md).

## Propósito e contribuição ao método

Entender o fenômeno e por que o job falha antes de conceber soluções. O mapa precisa preservar causas rivais, evidência e desconhecimento, distinguir limites de princípio de dificuldades atuais e reunir casos antes que uma solução influencie sua seleção. Alimenta idealidade, desafios, prova e seções 3, 5, 12 e 15 do CIR. Fontes: [S02 §7](../sources/originais/plano-geral-skills-cir.md), [S08 tema 2](../sources/originais/fluxograma-completo-ideal.md) e S15 §§1, 4–7.

O resultado deve mostrar o que foi observado, o que ainda é hipótese e que observação mudaria cada leitura; não justificar uma ideia inicial. Por isso, a pessoa formula sua versão antes dos exemplos, a pesquisa contra tem outro pesquisador, verificadores não produzem a versão e o conselho não decide. Apoio determinístico não prova esses comportamentos numa execução real.

## Pacote e capacidades locais

O [pacote universal](../skills/cir-mapa/SKILL.md) contém cartões literais de S15 para 2.1–2.7 e integração, referências por sub-etapa/papel, modelos fictícios e seis CLIs Python 3.10+ sem dependências externas.

| Auxiliar | O que verifica ou devolve |
| --- | --- |
| mapa.py | IDs, oito categorias, fontes/hipótese, rivais e exceções explícitas, árvores, tipos de evidência e requisitos mínimos da força, contradições e K; cronologia em snapshots Git; Mermaid de árvores/laços. |
| casos.py | Cotas, lados, datas, separação de antes/desfecho, pares e sonda declarada; projeção para sonda, sorteio estratificado em 3.6 e busca de vazamento literal. |
| pacote.py | Projeção anônima por campos e forma igual para contrastes: sete linhas, banco só por contagens e limite de 600 palavras, sem truncamento ou vencedor. |
| inventario.py | Itens para a cobertura real de especialistas, com centrais/princípio; lacunas K separadas porque o contrato atual não admite esse tipo. |
| cartoes.py | Sete IDs, campos, títulos e doses contra índice explícito. Teste confere também S08 e texto selecionado de S15. |
| sinais.py | Triagem contextual PT/EN por peça, léxico externo e exceções por linha. Nunca bloqueia, nem certifica limpeza. |

Os [formatos](../skills/cir-mapa/references/formatos.md) documentam todos os campos e limites. Markdown precisa de bloco canônico JSON para validação automática; a prosa fora dele depende de revisão. Sem `--git`, cronologia fica pendente. Com Git, o teste comprova anterioridade dos snapshots e imutabilidade das previsões/fichas referidas, não desconhecimento anterior do autor.

A condutora continua única leitora/escritora do dossiê; os scripts não alteram estado nem fazem commits. Trabalhadores recebem só briefs filtrados. A implementação não modificou condutora, conselho, fontes anteriores ou testes existentes. Pesquisa e integração de plataforma não foram simuladas como disponíveis.

## Usar e conferir

Copie a pasta inteira da skill para o hospedeiro e confirme pesquisa real, modelos por papel e isolamento antes de executar o método. Na raiz deste repositório:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p test_cir_mapa.py -v
python3 -B scripts/empacotar_skill.py --skill skills/cir-mapa --destino /tmp/cir-mapa.skill
python3 -B skills/cir-mapa/scripts/mapa.py skills/cir-mapa/assets/modelos/mapa.json
```

O último comando exercita apenas dados fictícios e deve reportar cronologia pendente. O modelo de casos é preenchível de um caso e falha nas cotas até receber um banco real completo; isso evita apresentá-lo como avaliação pronta. O pacote extraído fora do repositório foi exercitado nos testes com mapa, banco, sorteio, inventário, Mermaid e pacote reais de CLI.

## Diferenças e limites

S15 foi selecionado para este trabalho: detalha/ajusta S08/S02 em árvore com outras causas, rivais em linhas sem matriz, previsões prévias e busca contra, triagem mais verificação/conselho completo na 2.3, visão de fora, cotas/sonda e contrastes. As fontes anteriores permanecem intactas. O índice e brief.py reais não estão no checkout: não se afirma que a guarda foi integrada à condutora.

Os 21 testes locais passaram, incluindo 30 mutações estruturais rejeitadas, 15 variações estruturalmente válidas e corpus lexical 40/20 PT/EN. São dados sintéticos escritos junto ao validador, sem estimativa de generalização. Não cobrem automaticamente todas as falhas semânticas de S15 §13, como rival de fachada, uma árvore plausível mas incompleta ou retrospectiva parafraseada. Veja [avaliação](../evals/cir-mapa/README.md).

Permanecem o aceite humano, recall com regra de correspondência escolhida pelo responsável, comparações cegas do desenho, sonda com modelos efetivos, pesquisa, fontes científicas, fiscalização de permissões e Notion/Claude. Os sete erros gerais e três links antigos da condutora ausente permanecem separados das verificações novas. O projeto inteiro e o método não foram declarados prontos.
