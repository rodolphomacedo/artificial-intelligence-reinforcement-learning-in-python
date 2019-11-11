"""
A primeira abordagem para o EED é chamada de Epsilon Greedy.

Como funciona?
    Escolhemos um valor de Epsilon pequeno, indicando a probabiliade de
    exploração, como exemplo 10%, 5%, etc.
"""


def epsilon_greedy(p):
    eps = 0.1

    if p < eps:
        return p.rand()
    else:
        return p.best()

"""
Ao longo do experimento podemos testar infinitos numeros de vezes,
mas haverá momentos que não será mais necessário explorar pois já
encontramos o ótimo.

Se o Eps continuar com 10%, siginifica que em 10% das nossas escolhas
podem estar abaixo do ótimo.

Podemos fazer um teste A/B para medir a siginificancia do resultado, e se
for estatisticamente signifiva, podemos mudar o valo de Eps para 0.
(Esse é a parte Greedy)
"""
