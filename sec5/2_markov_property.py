"""
Markov Property

    Como podemos notar pelo nome, a propriedade de Markov é uma
    componente central da terioa do proccesso de decição de markov

    No conteto da RL, isso parece um pouco diferente da forma canonica
        (isermos ver essa forma)

Revisão do Processo de Markov
    Dado uma sequencia {x1, x2, x3, ..., xt}
    Nós podemos simplificar p{xt | xt-1, xt-2, ..., 2, 1}

    Temos:
        Markov de primeira ordem p{xt | xt-1}
        Markov de segunda ordem p{xt | xt-1, xt-2}

    Simples exemplo:
        Considere a sentença: "Seja um simples exemplo"

        Dado a sentença "Seja um simples", qual a próxima palavra? (+/-Fácil)

        Dado a última palavra "simples", predizer a próxima palavra?
            Não é fácil

        Dado a letra "um", qual a predição da próxima palavra?
            Isso é muito dificil!

    Assim vemos que a  estratégia de usar a suposição de markov é uma
    propriedade limitada? Não é necessáriamente.
    Podemos definir nosso problema de mode que seja limitado.


Processo de markov aplicado a RL
    {S(t), A(t)} produz 2 saídas -> {s(t+1), R(t+1)}

    Propriedade de Markov:
        p{st+1, Rt+1 | St, At}

    Notação por conveniência:
        p(s', r | s, a) = p{St+1 = s, Rt+1 = r| St = s, At = a}

    A conjunta sobre s' e r são condicionada em 2 outras variáveis
    Diferente da forma "usual" Markov: 1 RV condicionada em 1 outra RV

Outras distribuições condicionais
    Pode ser encontrado usando regras de probilidade
    regra da probabilidade total: (Procurar essa lei)
        p(s' | s, a) = SUM_r p(s', r | s, a)
        ou
        p(r | s, a) = SUM_s'p(s', r | s, a)


Exsite limitação da suposiçao e markov?
    Não necessáriamente.
    Recente aplicações:
        Deep Mind usou concatenação dos 4 mais recentes frames de um jogo
        para representar o estado quando estava jogando atari (2013)

        Estado pode ser representado para construir um tipo de dependência
        do passado para o presente

        Tipicamente pensar o estado correto agora = algums coisas nós
        medimos no mesmo instante (?)

        E também não precisamos dos dados brutos, podemos transformar e criar
        novas variáveis a partir de dados brutos)

        Qualquer input a partir dos sensores dos agentes podem ser usados
        para formar o estado atual.









"""




