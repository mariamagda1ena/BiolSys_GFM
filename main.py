# main.py

import numpy as np
import config
from environment import Environment
from population import Population
from mutation import mutate_population
from selection import proportional_selection, threshold_selection
from reproduction import asexual_reproduction, bernoulli_reproduction
from visualization import plot_population

# main.py

import os
import shutil
import time
import numpy as np
import config
from environment import Environment
from population import Population
from mutation import mutate_population
from selection import proportional_selection, threshold_selection
from reproduction import asexual_reproduction
from visualization import plot_population

def main():

    start_time = time.time()

    env = Environment(alpha_init=config.alpha0, c=config.c, delta=config.delta)
    pop = Population(size=config.N, n_dim=config.n)

    # Katalog, w którym zapisujemy obrazki (możesz nazwać np. "frames/")
    frames_dir = "frames"

    # Usuń katalog frames_dir, jeśli istnieje
    if os.path.exists(frames_dir):
        shutil.rmtree(frames_dir)

    os.makedirs(frames_dir, exist_ok=True)  # tworzy folder, jeśli nie istnieje

    survivors = pop.get_individuals()
    for generation in range(config.max_generations):
        # 1. Reprodukcja
        if len(survivors) > 0:
            new_population = bernoulli_reproduction(survivors, env.get_optimal_phenotype(), config.p,
                                                    config.circle_radius, config.children_proportion, config.N, config.sigma)
            pop.set_individuals(new_population)
        else:
            print(f"Wszyscy wymarli w pokoleniu {generation-1}. Kończę symulację.")
            break
            
        # 2. Mutacja
        mutate_population(pop, mu=config.mu, mu_c=config.mu_c, xi=config.xi)

        # 3. Zmiana środowiska
        env.update()
        # Rozszerzanie środowiska w równych odstępach pokoleń
        if generation > 0 and generation % (config.max_generations // config.max_num_optims) == 0:
            env.expand(config.n)

        # 4. Selekcja
        survivors = threshold_selection(pop, env.get_optimal_phenotype(), config.sigma, config.threshold)
        pop.set_individuals(survivors)

        # 5. Zapis aktualnego stanu populacji do pliku PNG
        frame_filename = os.path.join(frames_dir, f"frame_{generation:03d}.png")
        plot_population(pop, env.get_optimal_phenotype(), generation, config.circle_radius, config.children_proportion, save_path=frame_filename, show_plot=False)

    print("Symulacja zakończona. Tworzenie GIF-a...")

    # Tutaj wywołujemy funkcję, która połączy zapisane klatki w animację
    create_gif_from_frames(frames_dir, "simulation.gif")
    print("GIF zapisany jako simulation.gif")

    end_time = time.time()
    print(f"Czas wykonania: {end_time - start_time:.2f} sekundy")

def create_gif_from_frames(frames_dir, gif_filename, duration=0.2):
    """
    Łączy wszystkie obrazki z katalogu `frames_dir` w jeden plik GIF.
    Wymaga biblioteki imageio (pip install imageio).
    :param frames_dir: folder z plikami .png
    :param gif_filename: nazwa pliku wyjściowego GIF
    :param duration: czas wyświetlania jednej klatki w sekundach
    """
    import imageio
    import os

    # Sortujemy pliki po nazwach, żeby zachować kolejność generacji
    filenames = sorted([f for f in os.listdir(frames_dir) if f.endswith(".png")])
    
    with imageio.get_writer(gif_filename, mode='I', duration=duration) as writer:
        for file_name in filenames:
            path = os.path.join(frames_dir, file_name)
            image = imageio.v2.imread(path)
            writer.append_data(image)


if __name__ == "__main__":
    main()
