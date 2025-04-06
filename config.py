# config.py

import numpy as np

# -------------------
# PARAMETRY POPULACJI
# -------------------
N = 50           # pojemność siedliska (maksymalna liczba osobników zasiedlających jedno siedlisko)
n = 2            # wymiar przestrzeni fenotypowej

# --------------------
# PARAMETRY MUTACJI
# --------------------
mu = 0.75        # prawdopodobieństwo mutacji dla osobnika
mu_c = 0.5       # prawdopodobieństwo mutacji konkretnej cechy, jeśli osobnik mutuje
xi = 0.1      # odchylenie standardowe w rozkładzie normalnym mutacji

# --------------------
# PARAMETRY SELEKCJI
# --------------------
sigma = 1     # parametr w funkcji fitness (kontroluje siłę selekcji)
threshold = 0.5  # przykładowy próg do selekcji progowej (do ewentualnego użycia)

# --------------------
# PARAMETRY ŚRODOWISKA
# --------------------

# Początkowe alpha(t)
alpha = np.array([-3.5, 3.5])
# Wektor kierunkowej zmiany c początkowego siedliska
c = np.array([0.07, -0.07])   

delta = 0.07   # odchylenie standardowe dla fluktuacji
max_generations = 121  # liczba pokoleń do zasymulowania
circle_radius = 0.5

max_num_optims = 5 # finalna liczba optimów fenotypowych

# ----------------------
# PARAMETRY REPRODUKCJI
# ----------------------
# W wersji bezpłciowej zakładamy klonowanie z uwzględnieniem mutacji.
# Jeśli chcemy modelować płciowo, trzeba dodać odpowiednie parametry.
# Zawsze maksymalna liczba dzieci będzie odwrotnie proporcjonalna do odległości od optimum
# Jeśli wpiszemy 1,3,5 to dla osobnika znajdującego się w odległości 1*circle_radius max liczbą dzieci będzie 5 itd.
children_proportion = [1,3,5]

p = 0.5 # prawdopodobieństwo sukcesu reprodukcyjnego w pojedynczej próbie Bernoullego