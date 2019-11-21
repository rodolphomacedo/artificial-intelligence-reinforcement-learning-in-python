"""
Markov Decision Process (MDPs)

Basicamente estamos analisando os processos de decisão de markov (MDP)

Qualquer tarefa de RL com o conjunto de estados, ações e recompensas
que segue a propriedade de markov, é um MDP

MDP é definida com as coleções de:
    Conjunto de estados
    Conjunto de ações
    Conjuntos de recompensas
    Estado de transições probabilidade, probabilidades de recomepensas
    (definido como conjunto anterior)
    Fator de desconto (Iremos ver mais para frente no curso)

    Geralmente escrito como uma tupla de 5 posições

Política
    Uma ou mais peças para completar o quebra cabeça
    Geralmente a política é rotulada de PI
    Tecnicamente PI não é parte de um MDP, mas é parte da solução,
        juntamente com a função de valor

    A politica não pode ser definida por uma equação matemática,
    é mais como um algoritmo.

    A única excessão é quando voce definie a poílitica ótima,
    que pode ser definida matemáticamente em termos de uma função de valor.

    Falaremos para sobre políticas ótimas em aulas posteriores, mas por
    enquanto podemos entender o PI como uma notação curta para navegar
    pelo ambiente.


Diagrame de estados
    Podemos imaginar também que podemos desenhar diagramsa d transição de
    estados para MDPs, assim como fazermos para modelos markov e
    modelos de markov ocultos.
    Podemos desenhar os gráficos, apensar de não ser muito comum.

Probabilidade de transição
        p(s' | s, a)

    A transição de estados pode ser estocastico, ou seja, não se
    limitando a ser deterministico.
    Lembre-se que a percepção do ambiente é em relação ao agente e não
    ao próprio ambiente em si.

Ações
    Tipicamente nós pensamos que sejam ações como um joystick de inputs
    (up, down, left, right, jump)
    Ou nos movimentos de Blackjack
    Ações pode ser muito amplas, por exemplo, distribuição de fundos do governo


Agente vs Ambiente
    Algumas vezes podemos ter uma confusão sobre oque é um ambiente e um
    um agente.

"""
