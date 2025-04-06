# reproduction.py

import copy
import numpy as np
import config
from mutation import mutate_individual
from selection import fitness_function

def bernoulli_reproduction(survivors, habitats, p, circle_radius, children_proportion, N, sigma):
    """
    Generuje nową populację na podstawie odległości osobników od najbliższego optimum oraz
    prawdopodobieństwa reprodukcji w oparciu o rozkład Bernoullego.
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
        """
        Gdy mamy wiele optimów, takie liczenie odległości jest kompletnie bez sensu

        # distance = np.linalg.norm(np.array(parent.get_phenotype()) - np.array(alpha))

        W naszym przypadku, alpha jest macierzą! Róznica (phenotype - alpha) daje macierz wektorów fenotypu od poszczególnych optimów
        
        DLA n OPTIMÓW:

        - np.linalg.norm() spłaszcza macierz w wektor długości 2n i liczy normę L2 z tego długiego wektora.
        - Wynikiem tej funkcji jest jedna liczba, równa n^2*RMS odległości od poszczególnych optimów (n^2 razy średnia kwadratowa)
        - Gdy optima się oddalają, średnia kwadratowa jest bardzo szybko dominowana przez duże odgległości, dlatego osobniki nagle przestają się rozmnażać
        """
        distance  = parent.find_new_digs(habitats)[1] # konieczne tylko w pierwszej generacji, w kolejnych stanowi zabezpieczenie

        for threshold, max_children in rules:
            if distance <= threshold * circle_radius:
                chance = max_children
                children = np.random.binomial(chance, p)
                for _ in range(children):
                    new_individual = copy.deepcopy(parent)
                    new_individual.set_parent_habitat_idx(parent.get_current_habitat_idx())
                    # trzymamy indeksy zamiast obiektów Habitat, żeby ułatwić sobie analizę
                    mutate_individual(new_individual,mu=config.mu, mu_c=config.mu_c, xi=config.xi)
                    current_habitat_idx = new_individual.find_new_digs(habitats)[0]
                    habitats[current_habitat_idx].add_residents(new_individual)
                    # new_population.append(new_individual)


    # main.py wtedy przechowuje gdzieś listę obiektów klasy Habitat i konstruuje populację
    # a jaki jest wtedy output tej metody??
    for habitat in habitats:
        residents = habitat.get_residents()
        if len(residents) > N:
            fitnesses = [(ind, fitness_function(ind.get_phenotype(), habitat, sigma)) for ind in residents]
            fitnesses.sort(key=lambda x: x[1], reverse=True)
            new_population.extend([ind for ind, _ in fitnesses[:N]])
        else:
            new_population.extend(residents)

    
    # ona jest appendowana też wcześniej
    return new_population


