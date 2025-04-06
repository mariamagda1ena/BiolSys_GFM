import matplotlib.pyplot as plt
import numpy as np
from imageio.v2 import sizes

from selection import *


def plot_population(population, habitats, generation, fitness_levels, children_proportion, sigma, save_path=None, show_plot=False):
    """
    Rysuje populację w 2D wraz z optymalnym fenotypem alpha oraz okręgami wokół optimum.
    Można zarówno wyświetlać (show_plot=True), jak i zapisywać obraz (save_path != None).
    circle_radius - skaluje promień okręgów.
    children_proportion - pokazuje proporcję między szansami na potomków a ograniczeniem obszaru dla posiadania ich
    """
    alpha = [habitat.get_optim() for habitat in habitats]
    population_xs = [ind.get_phenotype()[0] for ind in population.get_individuals()]
    population_ys = [ind.get_phenotype()[1] for ind in population.get_individuals()]
    population_phenotypes = np.array([ind.get_phenotype() for ind in population.get_individuals()])
    optima_xs = [optim[0] for optim in alpha]
    optima_ys = [optim[1] for optim in alpha]


    plt.figure(figsize=(16, 16))
    labels = sorted(children_proportion)

    # Rysowanie okręgów wokół optimum
    sorted_proportion = sorted(children_proportion)
    # Lista [(odległość, max liczba dzieci)]
    #rules = [(threshold, max_children) for threshold, max_children in zip(reversed(sorted_proportion), sorted_proportion)]
    colors = ["#c7e3c7", "#8ac58a", "#44a244"]
    sorted_levels = sorted(zip(fitness_levels, children_proportion), key=lambda x: x[0], reverse=False)
    legend_labels = set()
    for (threshold, max_children), c, l in zip(sorted_levels, colors, labels):
        radius = np.sqrt(-2 * sigma ** 2 * np.log(threshold))  # Poziomice fitness
        for optim in alpha:
            label = f"{l} szans na potomka"
            if label not in legend_labels:
                legend_labels.add(label)
            else:
                label = None
            circle = plt.Circle(optim, radius, color=c, fill=True, label=label, zorder=1)
            plt.gca().add_patch(circle)

    # Ustalanie koloru każdego osobnika na podstawie najbliższego optimum
    color_map = plt.cm.get_cmap('tab10')
    forbidden = [2]  # pomijamy zielony
    valid_indices = [i for i in range(10) if i not in forbidden]
    optimum_colors = [color_map(valid_indices[i % len(valid_indices)]) for i in range(len(alpha))]
    individual_colors = []
    closest_optimum = []  #Lista do śledzenia, które optimum jest najbliżej każdego osobnika
    for ind_point in population_phenotypes:
        distances = np.linalg.norm(alpha - ind_point, axis=1)  # Obliczenie odległości do każdego optimum

        closest_optimum_idx = np.argmin(distances) # Indeks najbliższego optimum
        closest_optimum.append(closest_optimum_idx)
        individual_colors.append(optimum_colors[closest_optimum_idx])  # Kolor osobnika = kolor najbliższego optimum

    optimum_counts = [0] * len(alpha)
    for idx in closest_optimum:
        optimum_counts[idx] += 1

    plt.scatter(population_xs, population_ys, color=individual_colors, label="Osobnik", alpha=0.7)

    plt.scatter(optima_xs, optima_ys, color=optimum_colors, edgecolors='black', marker='X', s=150)


    for i in range(len(alpha)):
        label_optimum = f"Optimum {i + 1} ({optimum_counts[i]} osobników)"
        plt.scatter([], [], color=optimum_colors[i], label=label_optimum, edgecolors='black', marker='X',s=200)

    plt.title(f"Pokolenie: {generation}")


    plt.text(0, 5.5, f"Liczba osobników: {len(population.get_individuals())}",
             fontsize=12, ha='center', color='black', zorder=6)
    
    plt.text(0, 5.0, f"Liczba optimów fenotypowych: {len(alpha)}",  # Przesunięcie w dół
             fontsize=12, ha='center', color='black', zorder=6)
    
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.legend(loc='upper right',fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()

    if save_path is not None:
        plt.savefig(save_path)  # Zapis do pliku
    if show_plot:
        plt.show()
    else:
        plt.close()