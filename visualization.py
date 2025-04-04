import matplotlib.pyplot as plt
import numpy as np


def plot_population(population, alpha, generation, circle_radius, children_proportion, save_path=None, show_plot=False):
    """
    Rysuje populację w 2D wraz z optymalnym fenotypem alpha oraz okręgami wokół optimum.
    Można zarówno wyświetlać (show_plot=True), jak i zapisywać obraz (save_path != None).
    circle_radius - skaluje promień okręgów.
    children_proportion - pokazuje proporcję między szzansami na potomków a ograniczeniem obszaru dla posiadania ich
    """
    population_xs = [ind.get_phenotype()[0] for ind in population.get_individuals()]
    population_ys = [ind.get_phenotype()[1] for ind in population.get_individuals()]
    population_phenotypes = np.array([ind.get_phenotype() for ind in population.get_individuals()])
    optima_xs = [optim[0] for optim in alpha]
    optima_ys = [optim[1] for optim in alpha]

    plt.figure(figsize=(16, 8))

    # Rysowanie okręgów wokół optimum
    sorted_proportion = sorted(children_proportion)
    # Lista [(odległość, max liczba dzieci)]
    rules = [(threshold, max_children) for threshold, max_children in zip(reversed(sorted_proportion), sorted_proportion)]

    legend_labels = set()
    colors = ["#c7e3c7", "#8ac58a", "#44a244"]
    for (threshold, max_children), c in zip(rules,colors):
        for optim in alpha:
            label = f"{max_children} szans na potomka"
            if label not in legend_labels:
                legend_labels.add(label)
            else:
                label = None
            circle = plt.Circle(optim, threshold * circle_radius, color=c , fill=True, label=label, zorder=1)
            plt.gca().add_patch(circle)
    """
    distances = [5, 3, 1]
    labels = ['1 szansa na potomka', '3 szanse na potomka', '5 szans na potomka']
    #gradient = [0.22, 0.3, 0.5]
    colors = ["#c7e3c7", "#8ac58a", "#44a244"]
    
    for r, c, l in zip(distances, colors, labels):

        skip_label = 0
        for optim in alpha:

            if skip_label:
                circle = plt.Circle(optim, r * circle_radius, color=c, fill=True, zorder=1)
            else:
                circle = plt.Circle(optim, r * circle_radius, color=c, fill=True, zorder=1, label=l)"
    
            skip_label+=1
    """
    # Ustalanie koloru każdego osobnika na podstawie najbliższego optimum
    optimum_colors= plt.cm.tab10(np.linspace(0, 1, len(alpha)))
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
    plt.scatter(optima_xs, optima_ys, color=optimum_colors, edgecolors='black', marker='X')

    for i in range(len(alpha)):
        label_optimum = f"Optimum {i + 1} ({optimum_counts[i]} osobników)"
        plt.scatter([], [], color=optimum_colors[i], label=label_optimum, edgecolors='black', marker='X')

    plt.title(f"Pokolenie: {generation}")


    plt.text(0, 5.5, f"Liczba osobników: {len(population.get_individuals())}",
             fontsize=10, ha='center', color='black', zorder=6)
    
    plt.text(0, 5.0, f"Liczba optimów fenotypowych: {len(alpha)}",  # Przesunięcie w dół
             fontsize=10, ha='center', color='black', zorder=6)
    
    plt.xlim(-16, 16)
    plt.ylim(-8, 8)
    plt.legend(loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()

    if save_path is not None:
        plt.savefig(save_path)  # Zapis do pliku
    if show_plot:
        plt.show()
    else:
        plt.close()