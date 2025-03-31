import matplotlib.pyplot as plt
import numpy as np


def plot_population(population, alpha, generation, circle_radius, save_path=None, show_plot=False):
    """
    Rysuje populację w 2D wraz z optymalnym fenotypem alpha oraz okręgami wokół optimum.
    Można zarówno wyświetlać (show_plot=True), jak i zapisywać obraz (save_path != None).
    circle_radius - skaluje promień okręgów.
    """
    population_xs = [ind.get_phenotype()[0] for ind in population.get_individuals()]
    population_ys = [ind.get_phenotype()[1] for ind in population.get_individuals()]

    optima_xs = [optim[0] for optim in alpha]
    optima_ys = [optim[1] for optim in alpha]

    plt.figure(figsize=(16, 8))

    # Rysowanie okręgów wokół optimum
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
                circle = plt.Circle(optim, r * circle_radius, color=c, fill=True, zorder=1, label=l)
            
            plt.gca().add_patch(circle)
            skip_label+=1

    plt.scatter(population_xs, population_ys, label="Osobnik", alpha=0.7)
    plt.scatter(optima_xs, optima_ys, color='black', label="Optimum", marker='X')

    # Informacje o danym pokoleniu
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