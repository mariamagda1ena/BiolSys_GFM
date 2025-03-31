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
mu = 1         # prawdopodobieństwo mutacji dla osobnika
mu_c = 1       # prawdopodobieństwo mutacji konkretnej cechy, jeśli osobnik mutuje
xi = 0.2       # odchylenie standardowe w rozkładzie normalnym mutacji

# --------------------
# PARAMETRY SELEKCJI
# --------------------
sigma = 1.5      # parametr w funkcji fitness (kontroluje siłę selekcji)
threshold = 0.1  # przykładowy próg do selekcji progowej (do ewentualnego użycia)

# --------------------
# PARAMETRY ŚRODOWISKA
# --------------------

# Początkowe alpha(t)
alpha0 = [np.array([0.0, 0.0])]
# Wektor kierunkowej zmiany c początkowego siedliska
c = [np.array([0.03, 0.015]) ]    

delta = 0.06    # odchylenie standardowe dla fluktuacji
max_generations = 300  # liczba pokoleń do zasymulowania
circle_radius = 0.9
max_num_optims = 7 # finalna liczba optimów fenotypowych

# ----------------------
# PARAMETRY REPRODUKCJI
# ----------------------
#prawdopodobieństwo sukcesu w pojedynczej próbie Bernoullego
p = 0.75