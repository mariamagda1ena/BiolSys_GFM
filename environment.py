# environment.py

import numpy as np
import random

class Environment:
    """
    Klasa środowiska przechowuje optymalny fenotyp alpha
    oraz reguły jego zmiany w czasie.
    """
    def __init__(self, alpha_init, c, delta):
        """
        :param alpha_init: początkowa lista wektorów alpha
        :param c: wektor kierunkowy zmiany
        :param delta: odchylenie std w losowej fluktuacji
        """
        self.alpha = alpha_init
        self.c = c
        self.delta = delta

    def expand(self,dim):
        """
        Powielamy jedno losowe siedlisko,
        metoda wykorzystywana sporadycznie
        """
        alpha, c = self.alpha, self.c

        alpha.append(alpha[random.randint(0,len(alpha)-1)])

        new_vector = np.random.uniform(-1, 1, dim)
        rescaled = new_vector*(np.linalg.norm(c[0])/np.linalg.norm(new_vector))
        c.append(rescaled)

        self.alpha, self.c = alpha, c

    def update(self):
        """
        Zmiana środowiska w każdym pokoleniu,
        dla każdego optimum losujemy osobną zmianę:
        alpha(t) = alpha(t-1) + N(c, delta^2 I)
        """

        # jak nie będzie siedlisk to tu wyskoczy index error
        n = len(self.alpha[0])
        alpha, c = self.alpha, self.c

        for i in range(len(alpha)):
            random_shift = np.random.normal(loc=c[i], scale=self.delta, size=n)
            alpha[i] = alpha[i] + random_shift

        self.alpha = alpha 

    def get_optimal_phenotype(self):
        return self.alpha
