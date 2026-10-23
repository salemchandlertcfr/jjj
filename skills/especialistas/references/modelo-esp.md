# Modelo de uma especialidade curada

S13 §§6.3, 8.3–8.4. Biblioteca é um Git separado; testes fechados ficam em
outro repositório, jamais clonado pela sessão escritora. Nenhuma especialidade
de produção acompanha este pacote.

```text
esp-area/
  SKILL.md
  ORIGEM.md
  references/       até 3 módulos .md
  scripts/          contas determinísticas, quando houver
```

`SKILL.md`: campos abertos name/description e opcionais permitidos; até 300
linhas. Corpo: escopo/limites, perguntas da área, decisão que manda no resto,
receitas, critérios, erros típicos, ordens de grandeza, escolas, fontes e
scripts. Saber de prática é opcional e marcado, com autoria da contribuição
humana, sem usar isso como credencial de um agente.

Cada afirmação tem fonte; cada ordem de grandeza, fonte e data. Até três
módulos, sem roteiro de entrevista ou persona. Bloco completo até 8.000
palavras. Curadoria revê esses limites por teste; não os trate como ótimo
científico. A auditoria estrutural não confere cada afirmação.

`ORIGEM.md`: escopo, versão/tag/hash, pontos de partida e partes aproveitadas,
fontes, conferência de todas as afirmações, refutação das 3–5 centrais,
revisão humana quando disponível, resultados por modelo, validade inicial de
12 meses, licenças/atribuições e errata. Veja o [esqueleto](../assets/modelos/esp-SKILL.md).

Não copie conteúdo sem licença compatível. S13 permite MIT, Apache 2.0 e
CC BY com atribuição; demais materiais são referências, não texto vendorizado.
A licença do projeto não está definida. As alegações científicas de S13
permanecem atribuídas ao plano; não foram auditadas por estes validadores.
