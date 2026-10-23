# Visibilidade dos papéis

Projeção local de S02 §9, S10 §§6.4/11 e S13 §§4/12. O código copia esta tabela,
não deixa o recrutador editar acessos. Casos reservados continuam protegidos
até a prova autorizada; este pacote não os abre nem gerencia permissões.
Adaptação futura precisa conferir o contrato real da condutora, ausente neste checkout.

```json
{
  "especialista": {"ve":["pauta","versao_sem_autoria","fontes","ata"],"nao_ve":["autoria","modelos_outros","casos_reservados"]},
  "verificador": {"ve":["hipoteses_sem_autoria","criterios","refuta_se","fontes"],"nao_ve":["autoria","preferencia_usuario","casos_reservados"]},
  "gerador": {"ve":["desafio","restricoes","operadores","fontes"],"nao_ve":["versao_usuario","banco_ideias","outros_geradores","casos_reservados"]},
  "critico": {"ve":["material_formacao"],"nao_ve":["autoria","casos_reservados"]},
  "conselheiro": {"ve":["hipoteses_sem_autoria","criterios","parecer","fontes"],"nao_ve":["autoria","preferencia_usuario","outros_membros_rodada1","casos_reservados"]}
}
```

Os códigos são descritores de material, não caminhos de arquivos. A condutora
resolve os trechos autorizados e o hospedeiro limita o acesso real. Identidade
de sessão e `modelo.verificado` são evidências declaradas, não autenticação.
