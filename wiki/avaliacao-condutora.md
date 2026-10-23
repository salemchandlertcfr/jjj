# Avaliação da condutora

Estado: verificação local da primeira implementação; avaliação em plataformas e aceite humano pendentes. Revisão: 2026-10-23.

## Reproduzir

Na raiz, com Python 3.10+ e Git disponíveis:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/verificar_documentacao.py
python3 scripts/gerar_subetapas.py --check
python3 scripts/empacotar_skill.py --destino ../etapa-1-cir.skill
```

Os testes usam dossiês e identidades fictícias isoladas. Não acessam contas de modelos nem enviam dados para o GitHub. Conferem estado, bloqueios e persistência reais; não avaliam a qualidade das ideias que as futuras skills vão gerar.

Resultado local em 23/10/2026: **66 testes aprovados**, em aproximadamente 35,5 segundos, com Python 3.12.14 e Git 2.52.0. O pacote de 46 arquivos também foi extraído fora do repositório e passou por inicialização, resumo de cinco linhas, dose, checkpoint com commit, vigia, detecção de pendências e liberação da trava. O catálogo de 51 sub-etapas passou na conferência de geração. Testes específicos de configuração estão em [test_configuracao.py](../tests/test_configuracao.py).

## Cobertura e interpretação

A suíte de [testes locais](../tests/test_etapa_1_cir.py) exercita inicialização, estado inválido, revisões concorrentes, duas sessões, ordem do ciclo, aprovações explícitas, propósito congelado, filtragem de briefs, placeholders, registros e falhas de Git. Inclui entradas de caminho indevido, symlinks e alterações alheias ao registro.

Esse escopo demonstra mecanismos determinísticos no ambiente testado. Não estabelece taxas de acionamento, ausência de viés, aderência conversacional em sessões longas, isolamento real de ferramentas ou portabilidade de plataformas. Sinais heurísticos da vigia precisam de revisão; presença e hash de evidências não provam seu mérito.

Uma exploração conversacional usou duas sessões novas: uma leu a skill e outra respondeu sem ela, com os mesmos dois cenários fictícios. Com a skill, a resposta preservou a trava diante de um “ok” sobre pausa e encaminhou arquitetura/preço às etapas correspondentes. A resposta sem skill avançou no primeiro cenário e propôs tecnologia/preços no segundo. Foi uma execução por condição, sem serviços reais; ilustra os casos e não demonstra superioridade estatística ou cumprimento das metas.

Os alvos de [S10, §13](../sources/originais/plano-etapa-1-cir-condutora.md) permanecem **metas de avaliação**, sem alegação de terem sido alcançados por estes testes locais. Em especial, seguem pendentes comparações A/B/C com três execuções por condição, quatro perfis de usuário, retomada em dez pontos, compactação, custo por dose, vinte casos-limite, vinte consultas de acionamento, auditoria de acesso aos reservados e aceite humano dos temas 0 e 1.

Use a [implementação da condutora](implementacao-condutora.md) para instalar o alpha e consultar os limites de integração.
