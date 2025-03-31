# reproduction.py

import copy

import numpy as np
#from numpy.distutils.command.config import config
import config
from mutation import mutate_individual


def asexual_reproduction(survivors, N):
    """
    Wersja bezpłciowa (klonowanie):
    - Zakładamy, że potomków będzie tyle, aby utrzymać rozmiar populacji = N.
    - W najprostszej wersji: jeżeli mamy M ocalałych, 
      a M < N, to klonujemy ich losowo aż do uzyskania N osobników.
    """
    new_population = []
    if len(survivors) == 0:
        # Zabezpieczenie: jeśli wszyscy wymarli, inicjujemy od nowa (albo zatrzymujemy symulację).
        return []

    while len(new_population) < N:
        parent = copy.deepcopy(survivors[0])  # np. zawsze klonuj pierwszego (do testów)
        # W praktyce można klonować losowo: 
        # parent = copy.deepcopy(np.random.choice(survivors))
        new_population.append(parent)

    return new_population[:N]  # przycinamy, gdyby było za dużo

def bernoulli_reproduction(survivors, alpha, p, circle_radius, N):
    new_population = []
    if len(survivors) == 0:
        # Zabezpieczenie: jeśli wszyscy wymarli, inicjujemy od nowa (albo zatrzymujemy symulację).
        return []
    for parent in survivors:
        distance = np.linalg.norm(np.array(parent.get_phenotype()) - np.array(alpha))

        if distance <= 1 * circle_radius:
            max_children = 5
        elif distance <= 3 * circle_radius:
            max_children = 3
        elif distance <= 5 * circle_radius:
            max_children = 1
        else:
            max_children = 0

        children = np.random.binomial(max_children, p)

        for _ in range(children):
            new_individual = copy.deepcopy(parent)
            mutate_individual(new_individual,mu=config.mu, mu_c=config.mu_c, xi=config.xi)
            new_population.append(new_individual)

    return new_population[:N]

