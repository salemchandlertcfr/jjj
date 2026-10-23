# Adaptador Claude Code e transporte CLI

Base: S11 §§9.2, 11, 12 e 17. A definição de subagentes no plugin Claude Code
é plano de integração. Este pacote não instala plugin, CLIs, login, provedor,
acesso web ou isolamento. O transporte local configurável é apoio opcional.

## Sessões cegas planejadas

Um subagente por membro, no modelo de juiz escolhido, com busca/leitura web e
Python quando a ótica exigir. Ele não deve herdar `CLAUDE.md`, dossiê, arquivos
do projeto, conversa de origem ou ferramentas de leitura do workspace. Verifique
na versão real do hospedeiro quais opções permitem isso e audite a execução.
Diretório temporário e sessão com outro nome não demonstram isolamento.

Crítico usa sessão separada com fontes autorizadas; relator e normalizador
não têm ferramentas. Juiz de diversidade e leitor da Etapa 2 recebem apenas o
material atribuído e não usam busca para completar contexto. Rodada 2, quando
autorizada, retorna à mesma sessão do membro e preserva o histórico da rodada 1.

## Transporte local opcional

Consulte primeiro:

```bash
python3 <raiz-da-skill>/scripts/paralelo_cli.py --help
```

A interface local recebe briefs e configuração explícita de comandos. Preparar
uma configuração não autoriza dispará-la nem verifica seu modelo. A execução
real exige opção explícita e capacidade registrada; modo de teste identifica
dublês de avaliação. Nunca use uma saída de teste para declarar conselho real.
Use somente os campos, flags e placeholders confirmados pelo `--help`/código
instalado, sem construir comandos de shell com conteúdo não confiável.

Tempo limite, concorrência e uma nova tentativa por assento são mecanismos de
transporte; preserve a situação final e o modelo efetivo. Não trate repetição
de transporte como segunda rodada deliberativa. Substituição exige alternativa
de mesmo nível autorizada no mapa. Sem capacidade real, devolva espera/bloqueio.

O script local não torna subprocessos incapazes de ler outros caminhos, usar
rede ou herdar permissões. Antes de chamar um membro real, comprove que sua
via restringe o acesso necessário, que o contexto não herda o dossiê e que há
auditoria apropriada. Rodar um comando isolado em diretório temporário não
substitui essa comprovação. Custos não informados ficam desconhecidos.

## Pesquisa e persistência

Web real do hospedeiro pode sustentar pesquisa manual de refutar/conferir com
consulta, fonte, trecho, afirmação e conferência registrados. Não anuncie
`pesquisa-cientifica` instalada por usar esse procedimento. Sem web ou fonte
necessária, registre a lacuna. Fichas fixas são somente dublês de avaliação.

O conselho escreve apenas em seu workspace/pacote externo ou pasta avulsa nova;
somente a condutora persiste no dossiê. Não repasse seu caminho aos subagentes.
Outras famílias e pontes de API permanecem experimento futuro autorizado,
condicionado a ganho demonstrado; este alpha usa Claude primeiro.
