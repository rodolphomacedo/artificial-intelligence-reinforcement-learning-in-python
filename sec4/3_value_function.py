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





"""
