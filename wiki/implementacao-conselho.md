# Implementação do conselho

Estado: `0.1.0-alpha.1`, implementação local. Revisão: 2026-10-23. Requisito atual: [S11 — plano revisado](../sources/originais/plano-conselho-especialistas-revisado.md).

## Propósito e alcance

O pacote [`skills/conselho-especialistas/`](../skills/conselho-especialistas/SKILL.md) ajuda a melhorar decisões tentando refutar hipóteses por critérios prévios. Entrega razões, incerteza e dissenso ao usuário, sem recomendar nem escolher. A separação de julgadores, crítico e relator serve a esse propósito; uma matriz preenchida sozinha não comprova qualidade ou independência. O protocolo conceitual está em [conselho de especialistas](conselho-especialistas.md).

| Apoio local entregue | Limite da verificação |
| --- | --- |
| Validação de brief, anonimização e chave separada | Não prova anterioridade dos critérios nem ausência de toda marca semântica de autoria. |
| Painel, ordens e subconjuntos por membro | Não abre sessões nem garante isolamento de memória, arquivos ou ferramentas. |
| Vereditos, crítica, divergência, matriz e síntese | Confere estrutura; pesquisa, crítica real e fidelidade da síntese precisam de exame próprio. |
| Placar JSONL e custos | Brier exige desfechos factuais observados; medidas desconhecidas permanecem ausentes. |
| Transporte CLI configurável e pacote de retorno | CLI cobre a rodada 1; somente a condutora grava o dossiê. |

Os scripts usam Python 3.10+ e biblioteca padrão. O fluxo real precisa de pesquisa verificável, sessões independentes e modelo autorizado. A skill de pesquisa continua planejada; busca e leitura do hospedeiro podem atender mediante capacidade verificada e procedimento documentado. Fichas fixas e sessões simuladas são dublês de avaliação. Notion, hooks e instalação automática de serviços não foram validados.

## Instalar e preparar

Copie a pasta completa da skill para a área de skills do agente escolhido e confira suas capacidades. Para gerar o ZIP `.skill`, na raiz deste repositório:

```bash
python3 scripts/empacotar_skill.py --skill skills/conselho-especialistas --destino ../conselho-especialistas.skill
```

No agente, peça “use conselho-especialistas para tentar refutar estas hipóteses pelos critérios já fixados”. Se faltarem critérios ou prova de execução necessária, ele deve explicitar a falta antes do julgamento. Leia os [formatos](../skills/conselho-especialistas/references/formatos.md) e use os [modelos preenchíveis](../skills/conselho-especialistas/assets/modelos/brief.json); campos pendentes não constituem entrada pronta.

Os comandos abaixo usam arquivos preparados pelo operador, fora do dossiê. Consulte `--help` antes de executar:

```bash
python3 skills/conselho-especialistas/scripts/conselho.py preparar --entrada pedido.json --mapa juiz.json --produtores produtores.json
```

`produtores.json` é obrigatório: lista as sessões que produziram o material; use `[]` explicitamente para material externo. O mapa de juiz declara família `anthropic`, modelo real escolhido, nível `juiz`, via e `autorizado: true`; disponibilidade e autorização precisam ser verificadas. Não copie modelos ou preços históricos. A dose completa também requer normalização externa atestada; os parâmetros opcionais constam da ajuda.

O JSON retornado contém briefs individuais **e dados privados** de painel e autoria. Distribua somente cada brief ao membro correspondente. Não envie o resultado inteiro aos julgadores. Sessões declaradas não demonstram isolamento técnico.

## Executar e consolidar

O transporte local começa em simulação de despacho, sem chamadas:

```bash
python3 skills/conselho-especialistas/scripts/paralelo_cli.py --briefs membros.json --config transporte.json
```

Chamadas reais exigem `--executar`, autorização na configuração, modelo esperado e capacidades declaradas. O comando configurado usa argumentos explícitos sem shell, diretórios temporários e uma tentativa de reparo por membro. Diretório temporário **não restringe permissões do processo**; o hospedeiro deve controlar acesso, autenticação, modelo efetivo e auditoria. A segunda rodada necessita de transporte que retome as mesmas sessões, além da crítica, divergência e autorização exigidas.

Após execução e crítica reais:

```bash
python3 skills/conselho-especialistas/scripts/conselho.py consolidar --preparo preparo.json --vereditos vereditos.json --critica critica.json
```

O conselho completo requer também `--sintese sintese.json`, produzida por relator separado. Consulte as opções de custos, rodada anterior e troca na ajuda. Examine completude, alertas, faltas e limites; consolidação estrutural não equivale a validação científica.

## Receber na condutora

`consolidar` devolve `arquivos`, sem gravar o dossiê. Inclui o placar efetivo em `conselho/<id>/placar.jsonl`. A condutora monta um checkpoint com `tipo: "checkpoint"`, `escolha` factual e esse mapa de arquivos; guarda a entrada fora do dossiê e registra:

```bash
python3 skills/etapa-1-cir/scripts/registrar.py registrar ../cir-meu-projeto --session sessao-1 --entrada ../recebimento-conselho.json
```

Esse recebimento preserva a entrega e suas limitações; não aprova hipóteses nem avança uma trava. A condutora apresenta evidência e dissenso, coleta a decisão humana e aplica o contrato do passo atual. Veja [implementação da condutora](implementacao-condutora.md).

O desenvolvimento aplicou o `skill-creator` fornecido como S01, com origem e auxiliares oficiais fixados; eles não foram incorporados ao pacote. Casos, resultados e limites da avaliação estão em [avaliação do conselho](avaliacao-conselho.md). Eficácia do método e integrações reais permanecem em [pendências](pendencias.md).
