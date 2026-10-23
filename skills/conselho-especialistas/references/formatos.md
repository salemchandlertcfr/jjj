# Contratos e artefatos

Base: S11 §§4, 8 e 11. Os formatos JSON v1 abaixo são a concretização local
do protocolo. Consulte o `--help` de cada script para as flags efetivas; os
schemas em `assets/schemas/` e as validações de execução definem a estrutura
aceita. Esta referência não promete validação científica pelo formato.

## Separação pública e privada

| Artefato | Visibilidade e responsabilidade |
| --- | --- |
| Brief de avaliação e cartões | Filtrados e anônimos; fonte e sentido conferidos pela condutora |
| Chave de autoria e IDs originais | Privados, com a condutora; nunca no brief |
| Mapa e painel com modelo, sessões e semente | Privados; os membros recebem somente seu rótulo e ótica |
| Brief por membro | Só escopo atribuído, critérios, fontes e instruções |
| Vereditos, crítica, matriz, síntese | Anônimos; sem modelos ou origem antes da decisão |
| Placar completo e custos por modelo | Privados antes da decisão; apresentação filtrada |

O conselho opera numa pasta de trabalho externa. A entrega destinada ao
dossiê é `conselho/<id>/`, incorporada somente pela condutora via seu registro;
as fichas novas seguem em `vereditos.json` e a condutora as incorpora em
`fontes/`, sem duplicar fichas. O placar local fica em `conselho/<id>/placar.jsonl`.
A chave permanece fora dos briefs e do pacote público. Em modo avulso,
use `conselhos/<data>-<assunto>/` próprio com Git.

## Brief público v1

Campos: `schema_version:1`, `id`, `conselho`, `template`, `dose`, `pergunta`,
`criterios`, `criterios_fixados`, `hipoteses`, `fontes`, `parecer`, `restricoes`.

- Critério: `{id, descricao, refuta_se, decisivo:<boolean>}`.
- Fixação: `{sha256, em, antes_das_hipoteses:true, referencia}`. O hash vincula
  os critérios à referência de fixação; a declaração não prova cronologia.
- Hipótese pública: `{id, texto}`; autoria e ID original só na chave.
- Fonte: `{id, url, trecho, afirmacao, verificada:<boolean>}`. Uma fonte marcada
  verificada continua sujeita à conferência do crítico.
- Parecer: somente material de verificação relevante, com fontes, conclusão e
  incerteza, sem autoria. Quando obrigatório e ausente, devolva o bloqueio.
- Restrições: sigilo, ferramentas, acesso, via e escopo efetivamente autorizados,
  filtrados para não expor preferência nem identidade dos modelos.

Use o [modelo de brief](../assets/modelos/brief.json) como preenchível; campos
pendentes e hashes nulos não constituem uma entrada válida pronta para executar.
Identificadores aceitam letras, dígitos, `_`, `-` e ponto; booleanos não são inteiros.

## Painel privado e brief de membro

Mapa mínimo: `{familia:"anthropic", modelo:<escolha real>, nivel:"juiz",
via:<transporte>, autorizado:true}`. Modelo, autorização e disponibilidade
precisam ser verificados; um JSON preenchido não faz a chamada funcionar.

Painel: `{schema_version, id, conselho, template, dose, modelo_de_juiz,
so_claude:true, semente, membros, critico, relator, normalizador}`.
Cada membro contém `{rotulo, otica, modelo, sessao, hipoteses}`; os papéis fora
do painel têm sessões próprias. IDs de sessão não provam isolamento técnico.

Brief de membro expõe somente `{schema_version, conselho_id, membro, otica,
rodada:1, pergunta, criterios, criterios_sha256, hipoteses, fontes, parecer,
restricoes, instrucoes, entregar}`. A ordem e o subconjunto são atribuídos pelo
sorteio privado. Não inclua semente, modelos, mapa, chave, origem ou preferência.

## Veredito v1

Campos: `{schema_version:1, conselho_id, membro, rodada:1|2,
criterios_sha256, avaliacoes, falhas_fatais, fontes_novas}`.

Cada avaliação tem `{hipotese, criterio, sinal, justificativa, fontes,
raciocinio, mudaria, prob_resistir, evidencias_novas}`. `sinal` é `+`, `0`, `-`
ou `?`; `fontes` contém IDs; `prob_resistir` é `null` ou número de 0 a 1.
`+`/`-` exige fonte e/ou raciocínio explícito verificável. Todos os pares
hipóteses atribuídas × critérios devem estar presentes uma vez só.

Falha fatal: `{hipotese, criterio, motivo, fontes:[IDs]}`. Fontes novas precisam
das mesmas informações verificáveis das fichas, além da distinção entre hipótese
e fato. Rodada 2 exige `anterior`, divergência autorizada e evidência nova para
cada mudança. Uma troca só. Veja [modelo de veredito](../assets/modelos/veredito.json).

## Crítica estruturada

`{schema_version:1, conselho_id, aprovada:true, revisor, achados, referencia}`.
Cada achado contém `{membro, hipotese, criterio, tipo, justificativa, evidencias}`;
tipos: `lastro_insuficiente`, `possivel_vazamento`, `metodo`, `logica`.
`aprovada` é atestação de crítica real, não aprovação de uma hipótese. Use
[modelo de crítica](../assets/modelos/critica.json) sem transformar lacunas em atestação.
Confirmação de falha fatal exige `{hipotese, criterio, sessao, otica, referencia}`
em `confirmacoes_falha_fatal`; sessão e ótica precisam ser independentes.
O pacote público omite essas sessões. Vereditos invalidados por vazamento
permanecem na auditoria privada da condutora, fora de `vereditos.json`;
a matriz explicita sua ausência. Revise textos livres para evitar citações do
próprio conteúdo vazado. A validação de URLs é sintática, sem consulta DNS ou
prova de que uma página está pública.

## Matriz e síntese

Matriz: `{schema_version, conselho_id, criterios, hipoteses, celulas,
falhas_fatais, divergencias, alertas}`. Cada célula tem `{hipotese, criterio,
sinais, nao_observados}`. Cada sinal preserva `{membro, sinal, justificativa,
fontes, raciocinio, mudaria}`. Não introduza total, nota única, ranking ou vencedor.

No rápido, copie literalmente os argumentos. No completo, o relator entrega
síntese estruturada com referências de toda posição/argumento minoritário.
O envelope exige `{schema_version, conselho_id, tipo, pontos, falhas_fatais}`;
no completo, `relator` designado também é obrigatório. Cada ponto contém
`{hipotese, criterio, argumentos}` e cada argumento preserva literalmente
`{membro, sinal, justificativa, fontes, raciocinio, mudaria}`. Comentários
editoriais podem vir em `comentario`, separados do registro literal.
Campos opcionais `divergencias`, `lacunas` e `nao_observados` dos pontos
precisam reproduzir a matriz; `limites` é texto simples. Campos desconhecidos
são recusados. O [modelo editorial](../assets/modelos/sintese.md)
organiza a leitura sem substituir o JSON exigido pelo checker.

`conselho.py troca` entrega argumentos dos pontos divergentes sorteados por
membro e `fontes_da_troca` com as fichas citadas que não estavam no brief inicial.
Se utilizadas, fichas ausentes do próprio histórico precisam acompanhar o novo
veredito em `fontes_novas`. Reutilizar uma ficha já conhecida não autoriza mudar
sinal. IDs de fichas conflitantes bloqueiam a troca.

## Ferramentas e responsabilidade

| Script | Apoio determinístico; o que continua exigindo exame |
| --- | --- |
| `valida_brief.py` | Estrutura, critérios e alertas de autoria; não prova anterioridade real |
| `anonimiza.py` | Rótulos e chave; condutora confere sentido e marcas restantes |
| `sorteio.py` | Ordem/semente; não prova ausência de viés sem avaliação |
| `painel.py` | Composição/nível/sessões declaradas; não abre nem isola agentes |
| `briefs_membros.py` | Projeção filtrada; permissões reais exigem auditoria |
| `valida_veredito.py` | Cobertura/sinais/fontes e alertas; não comprova mérito científico |
| `divergencia.py` | Regras de divergência; não resolve o impasse |
| `matriz.py` | Preserva sinais/argumentos; não escolhe |
| `sintese_check.py` | Cobertura de referências e alertas; não prova fidelidade semântica |
| `placar.py` | Registro e Brier com desfecho explícito; decisão de valor não vira fato |
| `custos.py` | Medições fornecidas; não inventa preço |
| `paralelo_cli.py` | Transporte local configurável, tempo limite e repetição; não demonstra isolamento |

Consulte a ajuda real antes de invocar cada script. Falta de uma interface ou
capacidade exigida bloqueia a operação correspondente; não substitua por
personagens simulados nem declare o pacote integralmente validado.
