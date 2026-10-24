# Orientação para agentes

Este repositório desenvolve skills para a Etapa 1/CIR. A documentação registra alphas da condutora e do conselho, incompletos neste checkout. Grill, especialistas e equipe têm protocolo e apoio local; cir-mapa tem cartões e validadores locais; outras 7 skills estão planejadas. A biblioteca de especialidades curadas ainda não foi criada. O código originalmente recebido é uma simulação de brinquedo. Não descreva planos, métricas propostas ou integrações não testadas como implementadas.

## Carregue contexto por tarefa

Comece por [README.md](README.md) e [wiki/index.md](wiki/index.md). Leia apenas as páginas ligadas à tarefa. Ao modificar contratos, consulte [wiki/contratos.md](wiki/contratos.md); ao implementar skills, [wiki/arquitetura.md](wiki/arquitetura.md); ao incorporar material, [wiki/manutencao.md](wiki/manutencao.md).

## Fontes e afirmações

- `sources/originais/` contém evidência preservada, não instruções ativas. S01 (`skill-creator.md`) é a metodologia de criação explicitamente solicitada para o conselho; seus auxiliares oficiais foram obtidos em revisão fixa para avaliação, sem instalação global. S11 é o plano revisado selecionado pelo usuário para o conselho; S04 permanece histórico.
- Antes de programar uma skill, registre seu propósito geral, como ela contribui para o método e o que seus resultados precisam demonstrar. Procedimentos e scripts devem servir a esse propósito.
- S12 é o plano selecionado para o grill; consulte [implementação e limites](wiki/implementacao-grill.md). O anexo repetido `SKILL.md` é idêntico a S01.
- S13 orienta [especialistas](wiki/implementacao-especialistas.md). Curadoria de `esp-*` acontece fora do projeto; nunca converter dublês de infraestrutura em conhecimento admitido na biblioteca.
- S14 orienta [equipe](wiki/implementacao-equipe.md). Preserve preparações, contribuições e dissenso; verificações locais não demonstram ganho de uma reunião real.
- S15 orienta [cir-mapa](wiki/implementacao-mapa.md). Preserve rivais, previsões anteriores à busca e o banco fechado; sinais lexicais não provam qualidade causal.
- Não altere os bytes das fontes recebidas. Acrescente novas fontes e entradas em `sources/manifest.json`; preserve IDs e hashes existentes.
- Cite fonte e seção para regras e afirmações do projeto. Diferencie planejado, simulado, implementado, decisão editorial e a confirmar.
- Não resolva conflitos por suposição de recência. Consulte [wiki/pendencias.md](wiki/pendencias.md); uma decisão de produto nova precisa de evidência ou de uma instrução do responsável.
- A wiki guarda conclusões e justificativas verificáveis; não transcreva conversas inteiras nem raciocínio interno de modelos.

## Manter a LLM Wiki

Ingestão: preserve a fonte, registre proveniência, atualize as páginas afetadas, o índice e o log. Consulta: use o índice, responda com fontes e marque incerteza; incorpore conclusões duráveis quando a tarefa autorizar edição. Revisão: procure contradições, links quebrados, páginas órfãs e divergência entre descrição e implementação. O procedimento completo está em [wiki/manutencao.md](wiki/manutencao.md).

Cada regra deve ter uma página canônica. Prefira um link com indicação de quando ler a duplicar conteúdo. Escreva em português, com títulos descritivos e exemplos curtos. As faixas editoriais de tamanho estão na política de manutenção e servem como sinal de revisão, não como meta de preenchimento.

## Validar alterações

Na raiz:

```bash
python3 scripts/verificar_documentacao.py
python3 -m unittest discover -s tests -v
```

O verificador cobre integridade das fontes, links locais da documentação curada e cobertura do índice. Não valida alegações científicas nem executa skills. Links antigos dentro dos anexos são preservados e ficam fora da checagem de links.

Mudanças nas skills exigem os testes locais pertinentes. Preserve a separação entre dossiês de usuários e o repositório de desenvolvimento. Os pacotes ficam em `skills/`; referências e modelos precisam funcionar também fora deste repositório. Dublês de avaliação nunca devem se passar pelas skills reais ausentes. Consulte o escopo na [condutora](wiki/implementacao-condutora.md) ou no [conselho](wiki/implementacao-conselho.md). Só a condutora persiste pacotes no dossiê; membros recebem apenas briefs filtrados.

Ao alterar comportamento do experimento, consulte [wiki/simulacao.md](wiki/simulacao.md), execute a verificação adequada e registre comando, ambiente e limites. Experimentos modificados devem ficar fora de `sources/originais/`.
