"""
Para definir os estados do ambiente temos que observar uma maneira
de listar os estados com eficiencia.

Por exemplo, num jogo de xadres, podemos pensar em todos os estados com
todas as escohas:
    9! = 362880  >>>  3^9 = 19683

Se listarmos todos os tipos de possibilidades teremos varias situações
identicas. Isso certamente irá causar um ruído no nosso conjunto de
treinamento e também um aumento no consumo de memória.

A ordem de inicialização v(s) para os valores desejados, nós devemos
enumerar todos os estados.

A inicialização deverá ser diferente de X e O!


"""
