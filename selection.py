# selection.py

import numpy as np

def fitness_function(phenotype, habitat, sigma):
    """
    Funkcja fitness: phi_alpha(p) = exp( -||p - alpha||^2 / (2*sigma^2) )
    :param phenotype: fenotyp osobnika (np.array)
    :param sigma: odchylenie (float) kontrolujące siłę selekcji
    """
    #dist_matrix = np.array(phenotype) - np.array(alpha)
    #min_dist = min(np.linalg.norm(dist_matrix, axis=1))
    min_dist = np.linalg.norm(phenotype - habitat.get_optim())

    return np.exp(-min_dist / (2 * sigma**2))

def threshold_selection(population, habitats, sigma, threshold):
    """
    Model progowy:
      - Eliminujemy osobniki, których fitness < threshold.
      - Pozostałe przechodzą do kolejnej fazy (o ile nie przekroczymy N).
      - Jeśli liczba ocalałych > N, wtedy dodatkowa redukcja.
    """
    individuals = population.get_individuals()
    survivors = []
    for ind in individuals:
        closest_habitat_idx = ind.find_new_digs(habitats)[0] # threshold_selection włączamy po zmianie środowiska, więc osobnik musi sobie znaleźć nowe miejsce do życia
        # w tym miejscu można brać min_distance zamiast closest_idx i to dać do fitnessu
        # ale trzeba by zrobić jakić overloading funkcji fitness
        f = fitness_function(ind.get_phenotype(), habitats[closest_habitat_idx], sigma)
        if f >= threshold:
            survivors.append(ind)
    return survivors
