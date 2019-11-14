"""
Representações de estados

Como representar os estados no jogo tic-tac-toe.
A representação deveria ser em um vetor (array do tipo numpy)
cuja a busca deveria ser O(1), busca a partir do index de um
dicionário que é imutável.

Assim poderiamos utilizar essa estrutura para representar a estrutura
de 3x3 dos jogos.

Como o jogo tem 3^(3x3) = 19683 posições, podemos fazer um vetor
com 19683 posições, que nesse caso não é muito grande e podemos representar
na memória.

Lembrando que todas as posições incluem posições impossíveis com todas as
entradas iguais a X. Isso não influencia o algoritmos a ser melhor ou pior.



"""
