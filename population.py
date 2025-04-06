# population.py

import numpy as np
from individual import Individual

class Population:
    """
    Klasa przechowuje listę osobników (Individual)
    oraz pomaga w obsłudze różnych operacji na populacji.
    """
    def __init__(self, alpha_init, size, n_dim):
        """
        Inicjalizuje populację losowymi fenotypami w n-wymiarach.
        :param alpha: fenotyp początkowy, wokół którego inizjalizujemy populację
        :param size: liczba osobników (N)
        :param n_dim: wymiar fenotypu (n)
        """
        self.individuals = []
        for _ in range(size):
            # przykładowo inicjalizujemy fenotypy w okolicach [0, 0, ..., 0]
            phenotype = np.random.normal(loc=alpha_init, scale=1.0, size=n_dim)
            self.individuals.append(Individual(phenotype))

    def get_individuals(self):
        return self.individuals

    def set_individuals(self, new_individuals):
        self.individuals = new_individuals
