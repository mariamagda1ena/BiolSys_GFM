# environment.py

import numpy as np
import random
from individual import Individual # type: ignore

class Environment:
    """
    Klasa środowiska przechowuje optymalny fenotyp alpha
    oraz reguły jego zmiany w czasie.
    """
    def __init__(self, alpha_init, c, delta):
        """
        :param alpha_init: początkowa wektor alpha
        :param c: wektor kierunkowy zmiany
        :param delta: odchylenie std w losowej fluktuacji
        """
        self.habitats = [Habitat(alpha_init, c)]
        self.delta = delta

    def expand(self, dim):
        """
        Powielamy jedno losowe optimum, ale nadajemy mu inny wektor kierunkowy
        """
        habitats = self.habitats
        origin = random.choice(habitats)

        # ten dodatkowy shift jest bardzo potrzebny, bez niego wychodzą dziwne bugi (⊙ _ ⊙ )
        new_optim = origin.get_optim() + np.random.normal(loc=0, scale=self.delta, size=2)

        new_vector = np.random.uniform(-1, 1, dim)
        # przeskalowujemy tak, żeby wszystkie siedliska poruszały się tak samo szybko
        new_vector = new_vector*(np.linalg.norm(origin.get_vector())/np.linalg.norm(new_vector))

        new_habitat = Habitat(new_optim, new_vector)
        
        self.habitats.append(new_habitat)

    def update(self):
        """
        Zmiana środowiska w każdym pokoleniu,
        dla każdego optimum losujemy osobną zmianę:
        habitat(t) = habitat(t-1) + N(c, delta^2 I)
        """
        for habitat in self.habitats:
            habitat.shift(self.delta)


    def get_optimal_phenotypes(self):
        # czy to w ogóle jest potrzebne?
        return [habitat.get_optim() for habitat in self.habitats]

    def get_habitats(self):
        return self.habitats
    
class Habitat:
    def __init__(self, optim, vector):
        self.optim = optim
        self.vector = vector
        self.residents = [] # koniecznie lista obiektów klasy Individual

    def shift(self, delta):
        random_shift = np.random.normal(loc=self.vector, scale=delta, size=len(self.optim))
        self.optim += random_shift
        #print(self.optim)

    def add_residents(self, individual):
        
        assert isinstance(individual, Individual), "individual must be an instance of the Individual class"
        self.residents.append(individual)

    def get_optim(self):
        return self.optim
    
    def get_vector(self):
        return self.vector
    
    def get_residents(self):
        return self.residents