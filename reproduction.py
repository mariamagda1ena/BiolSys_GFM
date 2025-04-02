# reproduction.py

import copy
import numpy as np
#from numpy.distutils.command.config import config
import config
from mutation import mutate_individual
from selection import fitness_function


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

def bernoulli_reproduction(survivors, alpha, p, circle_radius, children_proportion, N, sigma):
    """
    Generuje nową populację na podstawie odległości od alpha oraz
    prawdopodobieństwa reprodukcji w oparciu o rozkład Bernoulliego.
    """
    new_population = []
    # Zabezpieczenie: jeśli ktoś w configu nie poda listy rosnącej
    sorted_proportion = sorted(children_proportion)
    # Lista [(odległość, max liczba dzieci)]
    rules = [(threshold, max_children) for threshold, max_children in zip(sorted_proportion, reversed(sorted_proportion))]

    if len(survivors) == 0:
        # Zabezpieczenie: jeśli wszyscy wymarli, inicjujemy od nowa (albo zatrzymujemy symulację).
        return []

    for parent in survivors:
        distance = np.linalg.norm(np.array(parent.get_phenotype()) - np.array(alpha))
        for threshold, max_children in rules:
            if distance <= threshold * circle_radius:
                chance = max_children
                children = np.random.binomial(chance, p)
                for _ in range(children):
                    new_individual = copy.deepcopy(parent)
                    mutate_individual(new_individual,mu=config.mu, mu_c=config.mu_c, xi=config.xi)
                    new_population.append(new_individual)
    # Przeżywają najlepiej dostosowane osobniki
    if len(new_population) > N:
        fitnesses = [(ind, fitness_function(ind.get_phenotype(), alpha, sigma)) for ind in new_population]
        fitnesses.sort(key=lambda x: x[1], reverse=True)
        return [ind for ind, _ in fitnesses[:N]]
    else:
        return new_population


