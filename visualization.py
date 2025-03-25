import matplotlib.pyplot as plt
import numpy as np


def plot_population(population, alpha, generation, circle_radius, save_path=None, show_plot=False):
    """
    Rysuje populację w 2D wraz z optymalnym fenotypem alpha oraz okręgami wokół optimum.
    Można zarówno wyświetlać (show_plot=True), jak i zapisywać obraz (save_path != None).
    circle_radius - skaluje promień okręgów.
    """
    x = [ind.get_phenotype()[0] for ind in population.get_individuals()]
    y = [ind.get_phenotype()[1] for ind in population.get_individuals()]
    plt.figure(figsize=(6, 6))

    # Rysowanie okręgów wokół optimum
    distances = [5, 3, 1]
    labels = ['5 szans na potomka', '3 szanse na potomka', '1 szansa na potomka'][::-1]
    gradient = [0.22, 0.3, 0.5]

    for r, g, l in zip(distances, gradient, labels):
        circle = plt.Circle(alpha, r * circle_radius, color='green', alpha=g, fill=True, zorder=1, label=l)
        plt.gca().add_patch(circle)

    plt.scatter(x, y, label="Osobnik", alpha=0.7)
    plt.scatter([alpha[0]], [alpha[1]], color='black', label="Optimum", marker='X')


    plt.title(f"Pokolenie: {generation}")
    # plt.text(0,5.5, f"Liczba osobników: {len(population.get_individuals())}",
    #          fontsize=10, ha='center', color='black', zorder=6)
    plt.xlim(alpha[0] - 6, alpha[0] + 6)
    plt.ylim(alpha[1] - 6, alpha[1] + 6)
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()

    if save_path is not None:
        plt.savefig(save_path)  # Zapis do pliku
    if show_plot:
        plt.show()
    else:
        plt.close()