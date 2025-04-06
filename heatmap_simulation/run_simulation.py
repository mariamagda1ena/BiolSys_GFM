# run_simulation.py
import numpy as np
import matplotlib.pyplot as plt
from main import main
from multiprocessing import Pool
import config

def simulate_for_params(mu_sigma):
    mu, sigma = mu_sigma
    avg_std, avg = main(mu, sigma)  # Uruchomienie symulacji dla konkretnego mu i sigma
    return (mu, sigma, avg_std, avg)

def run_simulation():
    # Parametry mu i sigma
    mu_values = np.linspace(0.2, 0.7, 5)  # Przykładowe wartości dla mutacji
    sigma_values = np.linspace(0.5, 1, 5)  # Przykładowe wartości dla selekcji

    # Macierz na wyniki
    std_matrix = np.zeros((len(sigma_values), len(mu_values)))
    avg_matrix = np.zeros((len(sigma_values), len(mu_values)))
    # Uruchamiamy symulację wielokrotnie

    # for i, sigma in enumerate(sigma_values):
    #     for j, mu in enumerate(mu_values):
    #         print(i)
    #         print(j)
    #         avg_std = main(mu, sigma)  # Uruchomienie symulacji dla konkretnego mu i sigma
    #         std_matrix[i, j] += avg_std


    # Tworzymy pool procesów
    with Pool() as pool:
        # Parametry do przetworzenia
        params = [(mu, sigma) for mu in mu_values for sigma in sigma_values]

        # Uruchamiamy równolegle obliczenia
        results = pool.map(simulate_for_params, params)

        # Zbieramy wyniki
        for mu, sigma, avg_std, avg in results:
            i = np.where(sigma_values == sigma)[0][0]  # Indeks dla sigma
            j = np.where(mu_values == mu)[0][0]  # Indeks dla mu
            print(i)
            print(j)
            std_matrix[i, j] += avg_std
            avg_matrix[i, j] += avg


    # Rysowanie heatmapy
    plt.figure(figsize=(10, 6))
    plt.title(f'Średnie odchylenie standardowe dostosowania dla różnych wartości mutation_rate i sigma dla p={config.p}')
    im = plt.imshow(std_matrix, cmap='plasma', origin='lower',
                    extent=[mu_values[0], mu_values[-1], sigma_values[0], sigma_values[-1]], aspect='auto')

    plt.colorbar(im, label='Średnie odchylenie std fitnessu')
    plt.xlabel('Mutation rate (mu)')
    plt.ylabel('Selection strength (sigma)')
    plt.tight_layout()
    plt.show()
    plt.figure(figsize=(10, 6))

    plt.title(f'Średnie dostosowania dla różnych wartości mutation_rate i sigma dla p={config.p}')
    im = plt.imshow(avg_matrix, cmap='plasma', origin='lower',
                    extent=[mu_values[0], mu_values[-1], sigma_values[0], sigma_values[-1]], aspect='auto')

    plt.colorbar(im, label='Średnie fitnessu')
    plt.xlabel('Mutation rate (mu)')
    plt.ylabel('Selection strength (sigma)')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_simulation()

