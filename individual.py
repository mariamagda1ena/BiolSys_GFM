# individual.py

import numpy as np

class Individual:
    """
    Klasa opisująca pojedynczego osobnika.
    Przechowuje wektor fenotypu w n-wymiarowej przestrzeni.
    """
    def __init__(self, phenotype):
        self.phenotype = phenotype
        self.parent_habitat_idx = 0
        self.current_habitat_idx = 0

    def find_new_digs(self, habitats):
        """
        Osobnik sam sobie wylicza wszystkie odległości i wybiera gdzie zamieszkać
        habitats: lista obiektów klasy Habitat, nie indeksów
        """
        distances = [np.linalg.norm(self.phenotype - habitat.get_optim()) for habitat in habitats]
        closest_habitat_idx = np.argmin(distances)
        min_distance = distances[closest_habitat_idx]

        self.set_current_habitat_idx(closest_habitat_idx)  
        return closest_habitat_idx, min_distance

    def get_phenotype(self):
        return self.phenotype
    
    def set_phenotype(self, new_phenotype):
        self.phenotype = new_phenotype


    def get_parent_habitat_idx(self):
        return self.parent_habitat_idx

    def set_parent_habitat_idx(self, idx):
        self.parent_habitat_idx = idx

    def get_current_habitat_idx(self):
        return self.current_habitat_idx

    def set_current_habitat_idx(self, idx):
        self.current_habitat_idx = idx