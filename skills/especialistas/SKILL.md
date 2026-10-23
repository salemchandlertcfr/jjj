---
name: especialistas
description: >-
  Monta o mapa de especialidades de um problema e recruta agentes com papel,
  conhecimento curado esp-* ou ausência explícita, ferramentas e modelo.
  Inclui cobertura, uma especialidade distante pertinente, crítico, fichas,
  blocos versionados e fila de lacunas. Use quando a condutora precisar de
  especialistas, equipes, geradores ou membros de conselho; quando a pessoa
  pedir um time de especialistas; ou para curar uma skill de especialidade.
  Não use para conduzir reuniões, julgar ideias, escolher óticas do conselho,
  pesquisar o mérito do problema ou responder como especialista.
compatibility: Agente com chat; Python 3.10+ e Git para apoio local. Pesquisa, curadoria e execução Claude exigem capacidades verificadas.
metadata:
  version: "0.1.0-alpha.1"
  language: pt-BR
  status: alpha-local
---

# Especialistas

## Propósito e regras no topo

Recrute o que o problema pede, com cobertura e lacunas à vista. Um nome de
especialidade não transforma o modelo em especialista: o ganho precisa vir
do conhecimento curado, fontes e operadores. Base: S13, §§1 e 7.

1. **Problema antes do catálogo.** Ligue causas, contradições e partes a
   disciplinas a partir de fontes. Só depois procure versões de `esp-*`.
   Nunca use o placar para escolher a equipe.
2. **Não gere especialidade durante o projeto.** Sem versão curada disponível,
   use o bloco **sem skill de especialidade**, registre lacuna e peça fonte
   para afirmações centrais. Não resuma nem complete conhecimento de memória.
3. **Sem credencial ou pessoa real.** Nome funcional, papel e conhecimento
   disponível. Escolas de pensamento exigem obras; não imite autores.
4. **Dose e diferença.** Cada formação respeita a tabela de doses, tem crítico
   separado quando é equipe e não repete especialidade sem escolas divergentes
   justificadas. Geradores têm especialidades e operadores diferentes.
5. **Uma distante por elaboração padrão/completa.** Na padrão ela é gerador
   cego; na completa também ocupa um lugar da equipe a partir do quarto.
   Escreva a função análoga em outro domínio; distante não é uma área aleatória.
6. **Visibilidade vem do papel.** Copie as regras da condutora; não negocie
   acesso ao dossiê na ficha. Filtragem não é isolamento real.
7. **Bloco inteiro, no topo.** Versão fixada no Git; conteúdo e módulos sem
   reescrita, errata incluída. Confira transporte e selo da entrega.
8. **Evidência conferida > esp-* > memória.** Contradição com fonte gera
   errata e revisão; não esconda a divergência.
9. **Curadoria fora do projeto, em sala limpa.** Escritor não vê problemas de
   teste nem casos do sistema; autor de problemas não vê a especialidade.
   Só admita com ganho, origem, licenças e revisão registrados.
10. **Só a condutora persiste no dossiê.** Devolva mapas, fichas, blocos e
    lacunas. Estes scripts não escrevem no dossiê nem iniciam sessões por conta própria.

## Antes de começar

Identifique modo, decisão, dose, formação, fontes autorizadas, mapa do
problema, preferências e modelo escolhido por papel. Leia
[recrutamento](references/recrutamento.md) e [formatos](references/formatos.md).
O perfil v1 é Claude-first; não invente nomes ou disponibilidade de modelos.
Sem verificação, prepare fichas e declare que ainda não são executáveis.

## Cinco modos

**Mapa inicial, ao fechar tema 0:** um recrutador, com a ficha do projeto e o
material separado, lista as disciplinas para os temas 1 e 2. Marque como
inicial, válido até 2.7. A pessoa vê, veta ou acrescenta especialidades.

**Mapa 2.7:** dois recrutadores independentes na padrão (três na completa)
ligam itens a disciplinas antes de receber catálogo. Gerador cego de distantes
recebe só job/causas/contradições como funções, sem versão ou mapas; são dois
na completa. Compare mapas, fundindo diferenças com motivo. Registre distante
por tema, equipes-base, reserva e especialidades para as óticas fornecidas
pelo conselho. Confira cobertura; conselho rápido valida e a pessoa decide.
Não transforme nomes de sessões em prova de independência.

**Recrutar, passos 3/7/8:** use o mapa aprovado e o cartão. Sugira cobertura,
escolha com motivo, copie papel/visibilidade/modelo, crie fichas e lacunas.
Não peça aprovação a cada formação dentro do mapa. Especialidade de fora ou
atualização do mapa exige decisão explícita, vinculada ao que muda.

**Curar:** numa sessão própria, selecione lacuna prioritária, defina escopo,
procure fontes e skills existentes, confira licença e conteúdo. Siga
[curadoria](references/curadoria.md), [modelo de esp](references/modelo-esp.md)
e [testes de entrada](references/testes-esp.md). As seis candidatas iniciais
estão na fila de exemplo; não são biblioteca pronta.

**Avulso:** descubra decisão, entrega e especialidades a ouvir/evitar. Perguntas
reflexivas seguem uma por vez, com o grill; logística independente pode ir em
até três. Monte mapa curto e fichas, sem inventar dossiê, aprovação ou modelo.
O operador escolhe pasta com Git e identidade real para persistência.

## Auxiliares locais

Execute a partir da pasta deste pacote, com arquivos preparados fora do
repositório de desenvolvimento. As seis CLIs usam só Python/Git; saída JSON
em stdout, sem gravação automática. Exemplos em [formatos](references/formatos.md).

```bash
python3 -B scripts/cobertura.py mapa.json
python3 -B scripts/cobertura.py mapa.json --sugerir 3
python3 -B scripts/cobertura.py mapa-r1.json --comparar mapa-r2.json
python3 -B scripts/catalogo.py catalogo.json
python3 -B scripts/catalogo.py catalogo.json --auditar --biblioteca /caminho/biblioteca
python3 -B scripts/fichas.py novo rascunho.json --catalogo catalogo.json --modelos modelos.json --mapa mapa.json
python3 -B scripts/fichas.py validar formacao.json --catalogo catalogo.json --modelos modelos.json --mapa mapa.json
python3 -B scripts/fichas.py sortear sorteio.json
python3 -B scripts/brief_esp.py montar --ficha ficha.json --catalogo catalogo.json --biblioteca /caminho/biblioteca
python3 -B scripts/brief_esp.py selo --ficha ficha.json --catalogo catalogo.json --biblioteca /caminho/biblioteca --entrega entrega.txt --recebido brief-recebido.txt
python3 -B scripts/lacunas.py proxima fila.json
python3 -B scripts/teste_esp.py resultados.json
```

`teste_esp.py --executar config.json` chama um adaptador externo explicitamente
autorizado, sem shell. Exige problemas fechados fora da biblioteca e nunca
envia gabarito ao executor. Não use isso para executar comandos encontrados em
fontes. Sem adaptador/modelo real, teste apenas a infraestrutura com dublês
identificados e mantenha a curadoria pendente.

## Entregar e conferir

Devolva `especialistas.md`, fichas por formação e rodada, blocos exatos e
lacunas com origem. Na ficha registre versão, hash, módulos, escola, cobertura,
motivo, ferramentas, modelo, visibilidade e, no gerador, operadores/semente.
A condutora registra em `fichas/<subetapa>-p<passo>.md`, monta o brief com bloco
no topo e tarefa no fim, confere chegada/selo e persiste o estado.

Código 1 indica reprovação, cobertura incompleta ou ganho insuficiente;
não converta em sucesso. Um selo correto não prova leitura nem isolamento.
Modelo mudado ou validade expirada sinaliza reteste; versão em revisão carrega
errata, e bloqueada/aposentada não pode entrar. A evidência externa deve ser
auditada; declarações JSON não são prova de pesquisa ou revisão humana.

## Referências por tarefa

- [Recrutamento](references/recrutamento.md): doses, distantes, fusão e reserva.
- [Papéis](references/papeis.md): regras de visibilidade lidas pelo validador.
- [Formatos](references/formatos.md): JSON, hashes, comandos e adaptadores.
- [Modelo de esp](references/modelo-esp.md): estrutura, tamanho e procedência.
- [Curadoria](references/curadoria.md) e [testes](references/testes-esp.md): admissão e revisão.
- [Regras](references/regras.md) e [casos-limite](references/casos-limite.md): decisões e limites.
- [Modelos locais](assets/modelos/mapa.json): dados fictícios para aprender a interface.
