"""
Componentes de um sistema Reinforcement Learning

Nptações engraçadas:
    S(t), A(t) -> R(t+1), S(t+1)
        (sars')

    s' = estado que iremos quando partimos do estado 's'
    r =  recomensa  que ganhamos  quando estamos estamos no estato 's'

Novos termos:
Epsiodio := Representa uma corrida no jogo.
    Cenários Epsódicos são que joga e termina, joga e termina,...
    Cenários Contínuos nunca terminam
    * Não iremos ver a parte de cenários contínuos


    Quando falamos em final do jogo, exsitem algumas situações que
        indicam que o final do jogo acontenceu.

Pendulu Inerted \ Cart-pole
    Esse problema foi bem estudado em controle e hoje podemos encontrar
    vários trabalhos em RL

    Umas das variáves de estado é o âgulo theta que é um espaço de estado
    continuo.
    Assim podemos ter variáveis de estado discretas, continuas e infinitas

Groundhog Day
    A ideia é a aprender vários epsódios repeditos como o filme Groundhog day,
    que acorda todos os dias no mesmo dia e tenta viver esse dia da melhor
    maneira possível.
    Mesmo que podemos perder várias vezes no primeiros espisódios,
    o agente irá apreder cada vez mais. Cada episódio é um novo começo.
"""
