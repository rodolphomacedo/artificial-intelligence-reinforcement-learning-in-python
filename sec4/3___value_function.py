"""
Função de Valor é atribuido ao Problema de atribuição de crédito

Dois modos de ver a função de valor:
    1. Tenho que realizar um certa tarefa, uma me dará uma baixa recompensa
    imediata e outra me dará uma recompesa maior mas num tempo posterior.
    Qual dessas acões devo tomar? (Ir para o bar ou estudar para prova)

    2. Quando tiver mais velho num bom emprego, quais foram as ações de
    maior valor que tomei que me levaram até aqui?

Função de Valores em diferentes áreas:
    Atribuição em propaganda e marketing
    Suponha que uma empresa fez 10 anuncios, e ocorreu uma venda que sabemos
    ter sido baseada nos anuncios.
    Agora temos que investir mais $100, qual investir:

    i.) O anúncio responsável pela venda foi o último? Então devemos alocar
    todo capital nesse anúncio pois ele foi o maior responsavél?

    ii.) Todos o anúncios de modo geral foram responsáveis para a venda, assim
    todos o anúncios receberam quantias iguais?

    iii.) Todos os anúncios foram responsáveis pela venda, porém com
    intensidade diferentes, assim todos receberão uma quantia de dinheiro,
    porém cada um receberá um valor distinto.


Recompensas Atrasadas
    Estamos olhando o problema por um outro ângulo.

    Atribuição de crédito: presente -> passado
    Recompensas atrasadas: presente -> futuro *

    Esse campo está relacionado com o campo de "planejamento", ou seja,
    a ideia de recompensas atrasasdas nos informa que a IA precisa ter
    uma capacidade de previsão  do futuro para tomar suas decisões.

Recompensas vs Valores
    As recompensas são imediatadas dados as ações em cada estado.
    O valor de um estado é uma medida das possíveis recompensas futuras.

    Muitas vezes no próximo estado não tem uma recompensa não há uma
    recompensa associada (imediatismo) mas a função de valor associada
    a esse estado, implica que é uma ação correta a ser tomada.

    * Assim a recompensa associada a esse estado não pode ser tida como
    um valor a ser seguida, por que ela sozinha não diz nada sobre
    o valor futuro.

Eficiência
   Um jogo-da-velha tem 3^(3*3) =  19683 possíbilidades
   Se o tabuleiro fosse  4x4 com ganhador com 3 peças alinhadas, teriamos:
       3^(4*4) = 3 Milhões de possibilidades

    A função de valor pode dizer o quão bom será no futuro dado
    o estado atual. E isso é extremamante útil.
    Essa função tem a capacidade de predizer o futuro dado o estado atual.

    E essa função ainda não poderá ser encontrada, não existe uma
    forma de encontra-lá efetivamente.

    Se tivessemos uma forma de obter essa função toda informação estaria
    disponível e não iriamos precisar de um modelo para estimar a os
    valores dessa função.

    Maldição da dimensionalidade (VER)

Função de Valor em RL
    Estimativa da função de valor é a tarefa central em RL. Os algoritmos
    evolucionários, tipo algoritmos genéticos, não tem esse tipo de
    função internamente. E é um tipo de algoritomos que não estamos
    interessados, no caso de estudos de RL.

Matematicamente
    V(s) = E[futuras recompensas | S(t) = s]

Encontrando V(s)
    Vamos introduzir algumas situações irrealistas para podermos resolver o
    problema. Mas nas situação posteriores não iremos precisar dessas
    suposições.

    Algoritmos iterativo:
        inicialize V(s)
        V(s) = 1 if s = estado de vitória
        V(s) = 0 if s = perda ou empate
        V(s) = 0.5 caso contrário

    Depois de incializado o v(s)
        v(s) <- v(s) + alpha(v'(s) - v(s))

    Obs: O 's' significa todos os possíveis estados que aquele estado pode
        assumir
    Obs2: O estado final nunca será aualizado pois não haverá um v(s')

Pseudocodigo:
    for t in range(max_iteractions):
        state_history = play_game
        for (s, s') in state_history from end to start:
            v(s) = v(s) + learning_rate *(v(s') - v(s))

Jogando o jogo
    Como jogar o jogo/gerar novos episodios?

    maxV = 0
    maxA = None
    for a, s' in possible_next_states:
        if v(s') > maxV:
            maxV = V(s')
            maxA = a
    perform action maxA


O problema
    O problema com a função de valor anterior é que ela não é precisa,
    pois se a funçaõ fosse precisa não iriamos precisar fazer
    todo trabalho que fizemos nos passos anteriores.

    Ações aleatorias nos permitem visitar e conhecer lugares que
    ainda não visitamos.
    Com isso nós podemos melhorar nossa estimativas para os estados.
    Mas para vencer nós precisamos tomar as melhores ações a fim de
    maximizar a recompensas.

    Esse é um problema que já conversamos anteriormente, EED!

    Nós iremos usar epsilon-greedy


Intiução
    A equação acima nos lembra da mesma equação do filtro passa baixa
    e da média da função de valor que construimos na secção 3.
    Essa também é a mesma função do gradiente descendente.

    * v(s) := é a função de valor no estado 's', ou seja, esse valor é
    a medida que indica o quão bom (ou mais valioso) está sendo
    as tomadas de decisão que estamos tomando.

    Por isso queremos que v(s') >= v(s) para todo 's'.

    Assim v(s') - v(s) >= 0

    Portanto, querermos que a função de valor no estado atual (s) seja tão
    próximo ao valor de v(s') quanto se possível.

    Usaremos alpha como sendo a taxa de aprendizagem, ou seja, um
    percentual sobre a diferença dos valores das funções de valores
    atual com o próximo. Assim atualizamos os valores da função de
    valor com esse novo número.

    Essa suposição implica que o v(s') é mais preciso que v(s)

    O que a algotimo faz é dentre todos os possíveis caminhos (como a árvore
    de decisão do inicio do curso - do xadres) traçar uma atribuição de valores
    a todos os estados que o agente está visitando.
    A cada época, o agente faz um percurso no espaço de soluções, e treina
    a função de valores.

    E, obviamente utilizamos o melhor v(s') para atualizar a função de valor,
    e todos os outros v(s') são não ótimos são descartados.

Resumo
    A ideia é que uma ação que ao agente toma agora não leva a uma recompensa
    maior, mas tende a maximizar o total das somadas recompesas no longo prazo.
    Assim, maximizar a função de valor v()!

    Nós estamos olhando o problema a partir de uma perspectiva computacional,
    no qual a árvore de possibilidades de todos os estados possíveis no
    jogo e suas transições irá crescer exponencialmente, ou seja, procurar
    um valor de um estado na força bruta não é viável.

    Nós,portanto usamos um algoritmo iterativo que essencialmente tráz o
    valor de um estado atual mais próximo possível do próximo estado,
    uma vez que existem múltiplos estados possíveis.

    Como o algoritmo é estocástico, e dado a construção do modelo, o agente
    tende a convergir para o valor esperado ao longo do tempo.

    Vamos ver variações dessa forma de calcular ao longo de todo o curso,
    com pequenas alterações, embora a função que estamos aprendendo nesta
    não seja como a versão formal que aprenderemos mais adiante e que
    será usada ao longo de todo curso.

    Tudo que foi visto nesse seção foi de modo informal, e foi apenas para
    se acostumar com o modo de pensar e resover um problema em RL.

"""



