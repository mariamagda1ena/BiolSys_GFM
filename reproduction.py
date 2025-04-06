# reproduction.py

import copy
import numpy as np
import config
from mutation import mutate_individual
from selection import fitness_function

def bernoulli_reproduction(survivors, habitats, p, fitness_levels, children_proportion, N, sigma):
    """
    Generuje nową populację na podstawie odległości osobników od najbliższego optimum oraz
    prawdopodobieństwa reprodukcji w oparciu o rozkład Bernoullego.
    """
    new_population = []
    if len(survivors) == 0:
        # Zabezpieczenie: jeśli wszyscy wymarli, inicjujemy od nowa (albo zatrzymujemy symulację).
        return []

    sorted_levels = sorted(zip(fitness_levels, children_proportion), key=lambda x: x[0], reverse=True)
    # print(sorted_levels)

    for parent in survivors:
        fitness = fitness_function(parent.get_phenotype(), habitats[parent.get_current_habitat_idx()], sigma)

        for threshold, max_children in sorted_levels:
            if fitness  >= threshold :
                chance = max_children
                children = np.random.binomial(chance, p)
                for _ in range(children):
                    new_individual = copy.deepcopy(parent)
                    mutate_individual(new_individual,mu=config.mu, mu_c=config.mu_c, xi=config.xi)
                    current_habitat_idx = new_individual.find_new_digs(habitats)[0]
                    habitats[current_habitat_idx].add_residents(new_individual)


    for habitat in habitats:
        residents = habitat.get_residents()
        if len(residents) > N:
            fitnesses = [(ind, fitness_function(ind.get_phenotype(), habitat, sigma)) for ind in residents]
            fitnesses.sort(key=lambda x: x[1], reverse=True)
            new_population.extend([ind for ind, _ in fitnesses[:N]])
        else:
            new_population.extend(residents)
            
    return new_population


