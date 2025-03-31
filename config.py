# config.py

import numpy as np

# -------------------
# PARAMETRY POPULACJI
# -------------------
N = 150           # liczba osobników w populacji
n = 2            # wymiar przestrzeni fenotypowej

# --------------------
# PARAMETRY MUTACJI
# --------------------
mu = 0.5         # prawdopodobieństwo mutacji dla osobnika
mu_c = 0.5       # prawdopodobieństwo mutacji konkretnej cechy, jeśli osobnik mutuje
xi = 0.5         # odchylenie standardowe w rozkładzie normalnym mutacji

# --------------------
# PARAMETRY SELEKCJI
# --------------------
sigma = 1      # parametr w funkcji fitness (kontroluje siłę selekcji)
threshold = 0.1  # przykładowy próg do selekcji progowej (do ewentualnego użycia)

# --------------------
# PARAMETRY ŚRODOWISKA
# --------------------
# Początkowe alpha(t)
alpha0 = [np.array([0.0, 0.0])]
# Wektor kierunkowej zmiany c
c = np.array([0.01, 0.01])     
delta = 0.1    # odchylenie standardowe dla fluktuacji
max_generations = 300  # liczba pokoleń do zasymulowania
circle_radius = 0.5
p = 0.5
max_num_optims = 6 # finalna liczba optimów fenotypowych

# ----------------------
# PARAMETRY REPRODUKCJI
# ----------------------
# W wersji bezpłciowej zakładamy klonowanie z uwzględnieniem mutacji.
# Jeśli chcemy modelować płciowo, trzeba dodać odpowiednie parametry.
# Zawsze maksymalna liczba dzieci będzie odwrotnie proporcjonalna do odległości od optimum
# Jeśli wpiszemy 1,3,5 to dla osobnika znajdującego się w odległości 1*circle_radius max liczbą dzieci będzie 5 itd.
children_proportion = [1,3,5]
