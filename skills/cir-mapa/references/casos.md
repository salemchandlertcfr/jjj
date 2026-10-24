# 6.7 Banco de casos (2.6)

Os casos são situações reais passadas, com desfecho conhecido, juntadas antes de existir qualquer solução, para que a prova do tema 5 não possa ser escolhida a dedo. Escolher casos pelo resultado distorce a conclusão ([Geddes](https://doi.org/10.1093/pan/2.1.131)); fixar as escolhas antes de ver os dados é a lógica do pré-registro ([Nosek et al.](https://doi.org/10.1073/pnas.1708274114)).

| Tipo | O que é | Cota mínima |
| --- | --- | --- |
| Comum | Uma situação típica do job | O resto, até fechar de 15 a 30 |
| Falha | O job falhou, com o desfecho registrado | 3 |
| Sucesso | O job deu certo em condições difíceis | 3 |
| Simetria | Dois casos com os mesmos dados e os lados trocados, em que o desfecho certo deveria trocar junto ou ficar igual, como nos testes de invariância e de direção da CheckList ([Ribeiro et al.](https://doi.org/10.18653/v1/2020.acl-main.442)) | 2 pares; um pode ser espelho construído a partir de um caso real, marcado "construído" |
| Evidência contrária | A evidência mais importante ia contra a leitura óbvia | 2 |
| Nada relevante | O certo era dizer que não havia o que fazer ou o que achar; sistemas treinados só com perguntas que têm resposta dão palpites onde não há ([Rajpurkar, Jia e Liang](https://doi.org/10.18653/v1/p18-2124)) | 2 |
| Seus | Os que você trouxe | Todos, com a origem "sua" |
1. **Antes de qualquer solução:** o banco fecha no tema 2. Caso que aparecer depois do tema 3 entra marcado "depois da solução" e nunca vai para os reservados.
2. **O antes separado do desfecho:** cada caso tem o que se sabia até a data de corte, escrito sem o desfecho, e o desfecho, à parte. Quem conhece o desfecho acha que ele era mais previsível do que era ([Fischhoff](https://doi.org/10.1037/0096-1523.1.3.288)); a pesquisa respeita a data de corte.
3. **Os dois lados:** desfechos bons e ruins. Banco só de falhas, ou só de sucessos, é o "refuta se".
4. **Por que é difícil:** cada caso diz por que seria difícil para qualquer solução, e não para uma em particular.
5. **Três pesquisadores independentes,** cada um com uma cota diferente: falhas; sucessos e "nada relevante"; simetria e evidência contrária. Nenhum vê o banco dos outros.
6. **Sonda de memória:** no mesmo modelo dos geradores do tema 4, a sonda recebe só o começo de cada caso, sem o desfecho, e tenta completá-lo. Se acerta detalhes que não estavam no começo, o caso fica marcado "conhecido do modelo". Modelos já viram muitos testes no treino ([Sainz et al.](https://doi.org/10.18653/v1/2023.findings-emnlp.722)), e o vazamento entre o que ajusta e o que testa infla resultados ([Kapoor e Narayanan](https://doi.org/10.1016/j.patter.2023.100804)).
7. **Guarda:** o `casos/candidatos.md` fica fechado. Cada caso tem um marcador único (⟦…⟧), procurado pela vigia em todos os briefs e saídas; o `brief.py` bloqueia o arquivo fora do 2.6 e do 3.6. No `02-mapa.md`, só a contagem por tipo.
8. **Sorteio no 3.6:** estratificado por tipo, com a semente registrada, pelo `casos.py sortear`. Os casos "vistos", "conhecidos do modelo" ou "depois da solução" só podem ir para os de trabalho; se faltar caso para os reservados de um tipo, a condutora pede mais, ou um espelho construído.


Base: S15 §6.7. Referência de método; fontes científicas citadas pelo plano não foram reconferidas nesta implementação.
