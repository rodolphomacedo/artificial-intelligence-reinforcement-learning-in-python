"""
Esse método de exploration-explotation também baseado no tet A/B
Intuitivamente, nós conhecemos a amostra a partir de 10 amostras, e esse
conhecimento é menos preciso do que a média de 1000 amostras.

Limite de Chernoff_hoeffding:
P{|X_ - mu| >= eps} <= 2exp(-2eps²N)

X_{UBC-j} = \Xbar_j + \sqrt{2 \frac{lnN}{N_j}}

N = Número de vezes que foi jogado
Nj = Número de vezes que jogamos com o bandido j

Esse modelo é parecido com o epsilon-greedy, mas não seremos ganânciosos
com relação a média, mas sim com ao limite de confiança da média amostral.

Mas por que isso funciona?
    Por que a nossa banda é construída baseada no N e Nj.
    Se Nj for grande comparado ao log(N), o  número é pequeno. Assim,
        a banda será pequena.
    Se Nj for pequeno, inidicando que visitamos muito pouco esse estado,
    então a banda será grande.
"""
