# Implementação do recrutamento de especialistas

Estado: `0.1.0-alpha.1`, protocolo e infraestrutura local. Plano selecionado: [S13](../sources/originais/plano-especialistas.md); metodologia de criação: [S01](../sources/originais/skill-creator.md).

## Propósito antes do código

Ter em cada sub-etapa as especialidades que o problema exige, com papel, conhecimento curado e equipamento explícitos. A contribuição ao método é cobertura verificável de causas, contradições e partes, com uma analogia distante pertinente e lacunas visíveis. Não basta renomear o mesmo modelo ou preencher fichas com credenciais inventadas. Fonte: S13, §§1 e 7.

Os resultados devem demonstrar recrutamento independente da disponibilidade do catálogo, formação coerente com dose e papel, fidelidade dos blocos de conhecimento, registro de ausência de especialidade e admissão na biblioteca só com ganho e proveniência. Os scripts validam contratos; não comprovam independência real, verdade científica ou qualidade conceitual.

## Escopo desta entrega

O [pacote universal](../skills/especialistas/SKILL.md) contém protocolo e apoio local para mapa, recrutamento, biblioteca, lacunas e avaliação. Conhecimento de novas `esp-*` não foi gerado durante o projeto: a primeira leva de S13 §6.5 está como fila de curadoria, sem especialidades de produção inventadas. Pesquisa, revisão humana, executores Claude e testes fechados continuam necessários para admiti-las. Os testes de infraestrutura usam bibliotecas temporárias fictícias, identificadas como dublês.

Só a condutora persiste no dossiê. Não alterar as implementações incompletas de condutora/conselho ou alegar integração real. Os auxiliares recebem entradas explícitas e devolvem saídas para revisão e persistência pelo responsável.

## Capacidades implementadas

| Auxiliar | Comportamento local |
| --- | --- |
| `cobertura.py` | Liga itens a especialidades, reporta descobertos centrais, sugere por cobertura ponderada sem placar/catálogo e compara propostas. Verifica equipes-base, distante e composição declarada do 2.7. |
| `fichas.py` | Copia visibilidade/modelo do papel; valida composição, dose, distância, duplicatas/escolas, ausência de skill e sessões não produtoras. Sorteia operadores diferentes com semente. |
| `catalogo.py` | Projeção sem placar para recrutamento; auditoria de tag/commit/hash e limites; marcadores externos sem revelá-los; validade/modelo novo sinalizam reteste. |
| `brief_esp.py` | Texto inteiro do Git, módulos selecionados e errata, ou bloco sem skill. Hashes de biblioteca/conteúdo/transporte; conferência de primeira linha e bloco no topo da mensagem recebida. |
| `lacunas.py` | Agrega pedidos sem inflar prioridade, sugere próxima e registra situação/motivo, devolvendo atualização sem gravar. |
| `teste_esp.py` | Matriz completa com três execuções por condição/modelo/problema; ganho ≥10 pontos, sem piora em 2/3. Execução externa opt-in sem shell e sem enviar gabarito ao adaptador. |

Formação válida ainda não é executável sem modelo verificado e decisão do mapa. Fora do mapa exige decisão explícita. Na completa, uma distante a partir do quarto lugar implica equipe de pelo menos quatro especialistas; o crítico fica fora dessa contagem, inclusive na leve, pela regra geral de S13 §7. Geradores são um grupo isolado, sem outro crítico duplicado. Essa interpretação operacional está no [recrutamento](../skills/especialistas/references/recrutamento.md).

O mapa JSON é a projeção de cobertura; `especialistas.md` conserva preferências, conselhos, fusão e decisões. Os scripts não geram pesquisa, reuniões, análises da especialidade ou aprovações. Os [formatos](../skills/especialistas/references/formatos.md) e [schemas](../skills/especialistas/assets/schemas/ficha.schema.json) documentam as interfaces; as verificações semânticas/entre arquivos dependem de código e revisão, não só de JSON Schema.

## Usar e verificar

Copie a pasta `skills/especialistas/` inteira para o hospedeiro. Python 3.10+ e Git bastam para o apoio local. O pacote não instala modelos nem cria a biblioteca de produção. Os modelos de exemplo deixam Claude não configurado; não os confunda com disponibilidade real.

Na raiz:

```bash
python3 -B skills/especialistas/scripts/cobertura.py skills/especialistas/assets/modelos/mapa.json --sugerir 3
python3 -B -m unittest discover -s tests -p test_especialistas.py -v
python3 -B scripts/empacotar_skill.py --skill skills/especialistas --destino ../artifacts/especialistas.skill
```

O fluxo após extração foi exercitado fora do repositório: mapa, criação de ficha e bloco sem skill. No uso real, mapas/fichas vão ao dossiê só pela condutora. Biblioteca e banco fechado de testes são separados; não publicar a biblioteca nem copiar casos do sistema para uma esp.

## Evidência e pendências

**33 testes locais passaram** em Python 3.12.14. Incluem 30 fichas plantadas, preservação de objetos Git apesar de alterações no diretório de trabalho, rejeição de tag movida/hash errado, errata, selo/transporte, sorteio, sessões, prioridade e admissão/rejeição. Um adaptador dublê executou a matriz de 72 chamadas com/sem sem receber gabaritos; isso testa a infraestrutura, não ganho de conhecimento real.

O [ensaio textual](../evals/especialistas/README.md) rodou três casos com e sem skill em sessões separadas, avaliadas por outra sessão: **12/12 nas duas condições**. A rubrica é guiada e pouco discriminativa; não demonstra ganho. Os intervalos de tempo não começam no mesmo ponto e não foram comparados por médias/deltas. Modelo exato, tokens e duração nativa são desconhecidos. Revisão humana permanece pendente no viewer.

Restam curadoria das seis `esp-*`, fontes e licenças, revisão de conteúdo, sala limpa real, modelos Claude e testes fechados. Identificabilidade, ganho das especialidades, recrutada × fixa, distante, acionamento e Notion/Claude Code ainda não foram validados. Regex não detecta todo nome próprio; hash/selo não prova leitura nem isolamento. O catálogo só verifica presença de ORIGEM e consistência de arquivos, não a veracidade de suas alegações.

Os sete erros anteriores da suíte geral e os três links da condutora ausente continuam explícitos. A nova skill não os corrige ou oculta; S01–S12 permanecem preservadas.
