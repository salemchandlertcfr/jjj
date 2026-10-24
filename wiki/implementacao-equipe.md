# Implementação das reuniões de equipe

Estado: `0.1.0-alpha.1`, protocolo universal e apoio local testado. Plano selecionado: [S14](../sources/originais/plano-equipe-especialistas.md), recebido em ZIP e preservado sem alteração dos bytes do Markdown. O manifesto registra também o contêiner e seu hash. Metodologia: [S01, skill-creator](../sources/originais/skill-creator.md).

## Propósito antes do código

Combinar especialidades numa versão melhor do que cada uma produziria sozinha, sem média arbitrária nem perda do que só um sabe. No método, a equipe elabora, verifica tecnicamente e integra; o conselho julga e a pessoa decide. Fontes: S14 §§1, 4 e 7.

Os resultados precisam demonstrar que cada contribuição chegou à mesa e teve destino, que a mudança de posição tem motivo, que o dissenso continua visível e que números/fontes usados em decisões têm checagem. O protocolo deve restringir ordem, rodadas e acesso sem alegar que simples declarações provam isolamento ou mérito científico.

## O que está implementado

O [pacote universal](../skills/equipe-especialistas/SKILL.md) contém referências por papel/ambiente, modelos JSON, schemas documentais e sete CLIs Python sem dependências externas. Os [formatos](../skills/equipe-especialistas/references/formatos.md) são a referência dos campos e limites. Base: S14 §§4–12.

| Auxiliar | Responsabilidade local |
| --- | --- |
| `pauta.py` | Pergunta, decisão técnica, entrega, refutação, doses e rodadas; triagem lexical de autoria/preferência. |
| `mesa.py` | Estado, tarefas filtradas, ordem sorteada por semente, registro, timeout, suspensão/reparo e entrega externa. |
| `ata.py` | Preparações, abertura, posições, fontes, reprodução de contas e placar. |
| `sintese.py` | Destino de cada contribuição, divergências, dissenso, números e conteúdo acrescentado pelo líder. |
| `parecer.py` | Verificação por afirmação e relatório de integração sem veredito/decisão. |
| `fusao.py` | Sínteses A/B/C sem atas/identidade, líder novo, origem, exclusões, conflitos e crítica. |
| `custos.py` | Métricas fornecidas; ausência permanece desconhecida, com subtotal conhecido separado. |

Preparações ficam privadas até terminarem; chegam inteiras antes da primeira fala. A mesa exige fases e ator esperado, crítico após especialistas e fechamento antes das checagens. Posições finais não veem as outras. Síntese passa por uma revisão da versão atual e resposta a cada ponto. Mudança final sem motivo fica marcada, sem inventar convencimento.

Elaboração padrão tem três especialistas e duas rodadas. Completa admite até três, distante a partir do quarto especialista e plano de duas/três paralelas para saída central. Verificação exige sessões não produtoras; integração recebe saídas aprovadas. Individual tem especialista/crítico até duas revisões; avulso usa o protocolo padrão. Leve é preparação solo, sem mesa. A fusão é preparada/validada separadamente, sem abrir as reuniões paralelas automaticamente.

As CLIs recebem JSON e devolvem JSON; nenhuma grava no dossiê ou chama Claude. Só a condutora persiste o mapa `arquivos`, com ata literal, preparações, posições, saída, checagens, custos e placar. Estado com modelos, sessões e quarentena é privado. Resumo de cerca de 300 palavras é tarefa do agente, não texto inventado pelo script. Fontes: S14 §§6.7 e 8.13.

## Usar e verificar

Copie a pasta `skills/equipe-especialistas` como skill do hospedeiro. Leia `SKILL.md`; o exemplo é fictício, com modelo não configurado e `executavel: false`. Na raiz do repositório:

```bash
python3 -B skills/equipe-especialistas/scripts/pauta.py validar skills/equipe-especialistas/assets/modelos/pauta.json
python3 -B skills/equipe-especialistas/scripts/mesa.py iniciar skills/equipe-especialistas/assets/modelos/inicio.json
python3 -B skills/equipe-especialistas/scripts/ata.py contas skills/equipe-especialistas/assets/modelos/contas.json
python3 -B -m unittest discover -s tests -p test_equipe.py -v
python3 -B scripts/empacotar_skill.py --skill skills/equipe-especialistas --destino /tmp/equipe-especialistas.skill
```

Os **40 testes** cobrem bloqueios de protocolo, contribuição perdida, dissenso, fonte não conferida, número sem lastro, crítica e resposta, vazamento/reparo, modelos/sessões declarados, custos e fusão. Reuniões fictícias percorrem elaboração, verificação, integração e individual; a CLI reproduz uma reunião inteira após extração do pacote fora do repositório. Isso demonstra mecânica local, sem alegar agentes reais.

Os [seis ensaios textuais](../evals/equipe-especialistas/README.md) tiveram 12/12 assertions em cada condição, com/sem skill. Empate sem evidência de ganho; revisão humana pendente. O benchmark e o viewer oficial são reproduzíveis, com métricas indisponíveis nulas.

## Limites e próximas verificações

Contas são interpretadas por AST matemática restrita em outro Python (`-I -S`), com limites de tamanho, operações e tempo. Não há `exec`/`eval` de código recebido. Aritmética reproduzida não valida o modelo científico. Pesquisa ausente devolve fonte não conferida; adaptador autorizado precisa chamar os verificadores reais da pesquisa, cuja interface ainda será conferida.

Hashes, selos e JSON não autenticam papéis, provam leitura ou garantem suporte semântico. Regex pode deixar passar autoria, recomendações ou números por extenso; revisão do agente e do hospedeiro continua necessária. Sessões Claude, Notion, ferramentas, permissões, modelos efetivos, custo e retomada não foram validados em produção. A biblioteca curada ainda não existe.

S14 §14 pede comparações contra melhor isolado e isolados com síntese, informação distribuída, pressão social, regressão e revisão cega. Esses ensaios reais continuam pendentes; não converter alvos do plano em resultados. A suíte geral ainda encontra os sete erros anteriores de condutora/conselho ausentes e o verificador, três links antigos da condutora. Ver [pendências](pendencias.md).
