# Implementação do grill embasado

Estado: `0.1.0-alpha.1`, protocolo e apoio local. Requisito: [S12, plano do grill](../sources/originais/plano-grill-embasado.md), selecionado pelo usuário; metodologia: [S01, skill-creator](../sources/originais/skill-creator.md), cujo anexo repetido tem o mesmo SHA-256.

## Propósito e evidência necessária

Revelar o que a pessoa sabe, quer e decidiria, com perguntas embasadas que não sugerem respostas; preservar suas palavras e encaminhar afirmações sobre o mundo para conferência externa. No método, abre a sub-etapa, desafia depois da pesquisa e organiza a checagem, sem elaborar soluções nem julgar. Fontes: S12, §§1, 4–6.

Os resultados precisam demonstrar base rastreável, escolha pela decisão que a resposta muda, ausência de indução, fidelidade textual, separação de valores e fatos e parada com lacunas explícitas. Validações estruturais não comprovam neutralidade semântica, revelação ou mérito científico.

## Fronteiras desta implementação

O [pacote universal](../skills/grill-embasado/SKILL.md) é autocontido, com Python 3.10+ e biblioteca padrão; o registro com trava usa Unix. Só a condutora persiste no dossiê; os auxiliares recebem arquivos explicitamente selecionados e devolvem registros e texto. Classificação de afirmações e avaliação do valor são trabalho do agente, com validação pelos scripts; não são simuladas por um classificador de palavras.

Neste checkout, a pasta da condutora e vários módulos do conselho não constam de `main`. Pesquisa científica também não está instalada. A integração real fica pendente, sem substituir essas skills por dublês ou corrigir suas implementações neste trabalho.

## O que funciona localmente

| Auxiliar | Verificação e comportamento |
| --- | --- |
| `perguntas.py` | Base obrigatória, consistência com índice de fichas, força/apoio visíveis, mapa sem ciclos, fronteira e maior valor; uma reflexão ou até três logísticas independentes. Gera a mensagem e sinaliza padrões lexicais. |
| `respostas.py` | Append com trava e repetição idempotente, texto original, afirmações/ideias como trechos literais, histórico de correções; busca, exportação só de fatos vigentes e auditoria por ID de mensagem. |
| `entendimento.py` | Origem por resposta vigente ou trecho autorizado, marca de leitura para paráfrase, Markdown com hash, brief filtrado, parada com confirmação/leitor atuais e registro de contradição sem insistência. |

São mecanismos locais, não classificação semântica, pesquisa científica ou execução de modelos. Os comandos não descobrem o dossiê nem alteram `estado.json`. A condutora integra modo, fronteira, custos e resultados. O script de registro escreve somente no JSONL explicitamente indicado; não autentica o papel de quem o chama.

## Usar e verificar

Copie a pasta inteira `skills/grill-embasado/` para a área de skills do hospedeiro. Antes de uso real, confira sessão/modelo Claude escolhido, pesquisa e permissões. O pacote não instala essas capacidades. Exemplo de chamada: “Use grill-embasado, abertura, dose padrão, com o cartão da 1.3”. Sem cartão, a skill começa pela decisão em jogo; sem pesquisa, mantém não conferida.

Na raiz do repositório:

```bash
python3 -B skills/grill-embasado/scripts/perguntas.py skills/grill-embasado/modelos/pergunta.json
python3 -B -m unittest discover -s tests -p test_grill.py -v
python3 -B scripts/empacotar_skill.py --skill skills/grill-embasado --destino ../artifacts/grill-embasado.skill
```

O [contrato JSON](../skills/grill-embasado/references/formatos.md) e os [modelos](../skills/grill-embasado/modelos/pergunta.json) descrevem o fluxo completo. Arquivos de trabalho e dossiês ficam fora do repositório de desenvolvimento; não use as respostas fictícias dos modelos como dados reais.

## Evidência e limitações

Em Python 3.12.14, **42 testes locais passaram**, exercitando as regras e um fluxo CLI após empacotamento/extração fora do repositório. A [avaliação](../evals/grill-embasado/README.md) preserva três casos, com/sem skill, avaliados por outra sessão: 12/12 assertions com skill e 9/12 sem. São assistentes disponíveis aqui, não Claude em produção. Não houve entrevista completa, persona oculta executada ou revisão humana; métricas de revelação, deriva e acionamento continuam sem medir.

A triagem lexical sinalizou 18/20 indutoras e 0/20 neutras num corpus escrito junto ao validador. Não detectou pressupostos em “Qual benefício você terá ao adotar isso?” e “Por que você desperdiça tempo com o processo atual?”. Isso não é uma estimativa de generalização. A correção de falso alerta em conjunções do cartão foi validada nos testes; o texto da skill permaneceu o mesmo durante os seis ensaios.

A suíte geral e o verificador da documentação continuam com as falhas anteriores: sete erros de carregamento/setup em módulos ausentes e três links para a condutora ausente. A nova skill não resolve nem oculta essas falhas. As doze fontes mantêm integridade conferível pelo manifesto.

Pendentes: validação em Claude/Notion, leitor e pesquisa reais, auditoria de isolamento e transcrição nativa, atualização automática de bases invalidadas e integração transacional com a condutora. “Chega” interrompe sem simular fechamento pronto. Próximas avaliações estão especificadas no [procedimento de avaliação](../evals/grill-embasado/README.md).
