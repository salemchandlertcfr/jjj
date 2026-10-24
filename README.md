# Skills para a Etapa 1 — CIR

Projeto de uma família de skills para transformar uma ideia em um **Conceito Ideal de Referência (CIR)**: uma descrição funcional do que uma solução deve realizar, antes de escolher a implementação e o produto viável. O método IDEAL orienta a concepção; uma condutora, skills temáticas e especialistas estruturam o trabalho.

**Estado em 24/10/2026:** a documentação registra alphas da condutora [`etapa-1-cir`](skills/etapa-1-cir/SKILL.md) e do [`conselho-especialistas`](skills/conselho-especialistas/SKILL.md). Este checkout está incompleto nesses dois componentes. [`grill-embasado`](skills/grill-embasado/SKILL.md) tem protocolo e verificadores de entrevista; [`especialistas`](skills/especialistas/SKILL.md), recrutamento e infraestrutura de biblioteca; [`equipe-especialistas`](skills/equipe-especialistas/SKILL.md), reuniões e validação local de atas e saídas. [`cir-mapa`](skills/cir-mapa/SKILL.md) tem cartões e validadores locais para o tema 2. [`cir-sintese`](skills/cir-sintese/SKILL.md) tem montagem rastreável e auxiliares de passagem/pronto. As outras 6 skills seguem planejadas. O fluxo completo, as especialidades curadas e as integrações de plataforma precisam de avaliação. O desenvolvimento segue o `skill-creator` fornecido pelo usuário.

## Comece pelo que precisa fazer

| Necessidade | Leia |
| --- | --- |
| Instalar e experimentar a condutora alpha | [Implementação e uso](wiki/implementacao-condutora.md) |
| Instalar e usar o conselho alpha | [Implementação do conselho](wiki/implementacao-conselho.md) |
| Usar e desenvolver perguntas embasadas | [Implementação do grill](wiki/implementacao-grill.md) |
| Recrutar especialistas e preparar a biblioteca | [Implementação de especialistas](wiki/implementacao-especialistas.md) |
| Conduzir reuniões e preservar contribuições e dissenso | [Implementação da equipe](wiki/implementacao-equipe.md) |
| Desenvolver o mapa do fenômeno, causas e casos | [Implementação do mapa](wiki/implementacao-mapa.md) |
| Consolidar o CIR e conferir a passagem | [Implementação da síntese](wiki/implementacao-sintese.md) |
| Entender o método e suas fronteiras | [Método IDEAL](wiki/metodo-ideal.md) |
| Percorrer o processo do início à entrega | [Fluxo da Etapa 1](wiki/fluxo-etapa1.md) |
| Implementar ou revisar as skills | [Arquitetura](wiki/arquitetura.md) e [contratos](wiki/contratos.md) |
| Ver um exemplo curto | [Exemplo de aplicação](wiki/exemplo.md) |
| Saber o que falta decidir ou construir | [Pendências](wiki/pendencias.md) |
| Consultar qualquer assunto | [Índice da wiki](wiki/index.md) |

## O que há no repositório

- `wiki/`: síntese por assunto, com referências aos anexos e separação entre evidência, proposta e decisão editorial.
- `skills/`: pacotes universais, referências e scripts em Python sem dependências externas; consulte os limites de cada implementação.
- `sources/`: os dezesseis arquivos distintos recebidos, preservados byte a byte, e seu [inventário](sources/README.md).
- [AGENTS.md](AGENTS.md): instruções curtas para agentes que modificam o repositório.
- `scripts/verificar_documentacao.py`: verificação local de links, navegação e integridade das fontes.

A documentação segue uma adaptação da [LLM Wiki de Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): fontes preservadas, conhecimento sintetizado e regras de manutenção. A wiki é a documentação temática do projeto; não há uma segunda árvore `docs/` repetindo seu conteúdo. Veja a [política de manutenção e volume](wiki/manutencao.md).

## Verificar e experimentar

A partir da raiz, com Python 3.10 ou superior para conferir a documentação:

```bash
python3 scripts/verificar_documentacao.py
python3 -m unittest discover -s tests -v
```

Esses comandos usam apenas a biblioteca padrão; os testes da condutora também precisam de Git. Para executar a simulação exploratória, use Python 3.11 ou superior:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-experimentos.txt
.venv/bin/python sources/originais/simulacao_etapa1.py 100
```

O argumento reduz parte das rodadas; os experimentos extras mantêm contagens próprias. A simulação expressa premissas, sem validar empiricamente o método. Consulte [execução, métricas e limitações](wiki/simulacao.md) antes de interpretar os resultados.

## Contribuir

Leia [AGENTS.md](AGENTS.md) e altere a página canônica do assunto junto com a mudança correspondente. Preserve as fontes e registre contradições em [pendências](wiki/pendencias.md). As escolhas desta organização estão em [decisões](wiki/decisoes.md); novas fontes e revisões relevantes entram no [log](wiki/log.md).
