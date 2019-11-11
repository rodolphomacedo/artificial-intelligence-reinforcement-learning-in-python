"""
Nessa parte iremos ver uma outra maneira de resolver o EED.
Supondo que saibamos que o verdade valor da nossa estimativa
seja muito menor do que 10. Colocamos um teto para a estimativa!

"""
import numpy as np
import matplotlib.pyplot as plt
import ipdb

class Bandit:
    def __init__(self, m, upper_limit):
        self.m = m
        self.mean = upper_limit
        self.N = 1

    def pull(self):
        return np.random.randn() + self.m

    def update(self, x):
        self.N += 1
        self.mean = (1 - 1.0/self.N)*self.mean + 1.0/self.N*x


def run_experiment(m1, m2, m3, eps, N, upper_limit):
    # ipdb.set_trace(context=5)
    bandits = [Bandit(m1, upper_limit), Bandit(m2, upper_limit),
               Bandit(m3, upper_limit)]
    data = np.empty(N)

    for i in range(N):
        j = np.argmax([b.mean for b in bandits])
        x = bandits[j].pull()
        bandits[j].update(x)
        data[i] = x

    cumulative_average = np.cumsum(data) / (np.arange(N) + 1)
    print(bandits)

    # Ploting restults
    plt.plot(cumulative_average)
    plt.plot(np.ones(N)*m1)
    plt.plot(np.ones(N)*m2)
    plt.plot(np.ones(N)*m3)
    plt.xscale('log')
    plt.show()

    for b in bandits:
        print(b.mean)

    return cumulative_average


if __name__ == '__main__':
    c1 = run_experiment(1.0, 2.0, 3.0, 0.1, 100000, 10)
    c2 = run_experiment(1.0, 2.0, 3.0, 0.05, 100000, 10)
    c3 = run_experiment(1.0, 2.0, 3.0, 0.01, 100000, 10)

    plt.plot(c1, label='eps = 0.1')
    plt.plot(c2, label='eps = 0.05')
    plt.plot(c3, label='eps = 0.01')
    plt.legend()
    plt.xscale('log')
    plt.show()

    plt.plot(c1, label='eps = 0.1')
    plt.plot(c2, label='eps = 0.05')
    plt.plot(c3, label='eps = 0.01')
    plt.legend()
    plt.show()
