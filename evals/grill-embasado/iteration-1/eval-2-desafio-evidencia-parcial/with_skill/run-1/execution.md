# Execução observada — caso 2 com skill

- Li somente o caso de ID 2 em `evals/grill-embasado/evals.json`, por seleção em Python, preservando seu prompt.
- Li `AGENTS.md`, `README.md` e `wiki/index.md`; consultei `skills/grill-embasado/SKILL.md`, o modelo de pergunta, o validador e as referências de origem, modos, contradição, formatos, qualidade, tipos e indução.
- Li também a skill de onboarding disponibilizada pelo ambiente; não executei configuração de ambiente, instalação ou acesso à rede.
- Preparei em `/tmp/grill-eval-2-with-skill-run-1/` uma entrada de desafio, dose completa, com uma pergunta de contraexemplo e um índice que reproduz exclusivamente os dados autorizados de F-052.
- Executei, a partir de `skills/grill-embasado/`, `python3 -B scripts/perguntas.py /tmp/grill-eval-2-with-skill-run-1/pergunta.json --indice /tmp/grill-eval-2-with-skill-run-1/indice.json`.
- O comando terminou com código 0 e retornou `aprovada: true`, sem erros, suspeitas ou pendências. A triagem do script é estrutural e lexical.
- Revisei a mensagem quanto à única pergunta, reprodução dos trechos, indicação da força e das limitações e ausência de conclusão atribuída à pessoa.
- Salvei em `outputs/mensagem.md` somente a mensagem renderizada pela função do validador, sem acrescentar texto.

## Limitações

Não fiz perguntas reais à pessoa nem pesquisa externa. A ficha foi tratada como entrada autorizada do caso, sem nova conferência de sua fonte. A saída é somente a próxima mensagem: não houve resposta da pessoa, registro de reação, leitura independente ou fechamento do grill. A avaliação não demonstra efeito da entrevista nem verdade universal da afirmação ou do resultado. Não alterei código ou arquivos fora dos artefatos solicitados e das entradas temporárias em `/tmp`.

O tempo registrado em `timing.json` usa duas leituras do relógio UTC do ambiente; tokens, duração em milissegundos e modelo ficam nulos, conforme solicitado.
