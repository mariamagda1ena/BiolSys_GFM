# config.py

import numpy as np

# -------------------
# PARAMETRY POPULACJI
# -------------------
N = 200          # pojemność siedliska (maksymalna liczba osobników zasiedlających jedno siedlisko)
n = 2            # wymiar przestrzeni fenotypowej

# --------------------
# PARAMETRY MUTACJI
# --------------------
mu = 0.5         # prawdopodobieństwo mutacji dla osobnika
mu_c = 0.5       # prawdopodobieństwo mutacji konkretnej cechy, jeśli osobnik mutuje
xi = 0.3      # odchylenie standardowe w rozkładzie normalnym mutacji

# --------------------
# PARAMETRY SELEKCJI
# --------------------
sigma = 0.5    # parametr w funkcji fitness (kontroluje siłę selekcji)
threshold = 0.5  # przykładowy próg do selekcji progowej (do ewentualnego użycia)

# --------------------
# PARAMETRY ŚRODOWISKA
# --------------------

# Początkowe alpha(t)
alpha = np.array([0.0, 0.0])
# Wektor kierunkowej zmiany c początkowego siedliska
c = np.array([0.08, 0.08])

delta = 0.05  # odchylenie standardowe dla fluktuacji
max_generations = 100  # liczba pokoleń do zasymulowania
fitness_levels = [0.5,0.95] # threshholdy fitnessu do reprodukcji

max_num_optims = 1 # finalna liczba optimów fenotypowych

# ----------------------
# PARAMETRY REPRODUKCJI
# ----------------------
# W wersji bezpłciowej zakładamy klonowanie z uwzględnieniem mutacji.
# Jeśli chcemy modelować płciowo, trzeba dodać odpowiednie parametry.

children_proportion = [2,3] # max liczba dzieci dla każdego thresholdu

p = 1 # prawdopodobieństwo sukcesu reprodukcyjnego w pojedynczej próbie Bernoullego