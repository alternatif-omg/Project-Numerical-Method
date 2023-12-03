import numpy as np
import matplotlib.pyplot as plt

def gauss_seidel(coefficients, constants, tolerance=0.01, max_iterations=100):
    n = len(constants)
    x = np.zeros(n)  # Inisialisasi solusi awal
    errors = []  # Menyimpan error relatif pada setiap iterasi

    for iteration in range(max_iterations):
        x_old = np.copy(x)

        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += coefficients[i, j] * x[j]
            x[i] = (constants[i] - sigma) / coefficients[i, i]

        # Menghitung error relatif
        relative_error = np.max(np.abs((x - x_old) / x))
        errors.append(relative_error)

        print(f"Iterasi {iteration + 1}: {x}, Error Relatif: {relative_error}")

        # Mengecek toleransi
        if relative_error < tolerance:
            print(f"\nKonvergen setelah {iteration + 1} iterasi.")
            plot_errors(errors)
            return x

    print("\nMetode Gauss-Seidel tidak konvergen dalam jumlah maksimal iterasi.")
    plot_errors(errors)
    return None

def plot_errors(errors):
    plt.plot(range(1, len(errors) + 1), errors, marker='o')
    plt.title('Konvergensi Metode Gauss-Seidel')
    plt.xlabel('Iterasi')
    plt.ylabel('Error Relatif')
    plt.grid(True)
    plt.show()

# Mengonversi persamaan menjadi bentuk matriks
coefficients = np.array([[8, 1, 1], [1, 8, 1], [1, 1, 8]], dtype=float)
constants = np.array([10, 10, 10], dtype=float)

# Menyelesaikan SPL dengan metode Gauss-Seidel
result = gauss_seidel(coefficients, constants, tolerance=0.01, max_iterations=100)

if result is not None:
    print("metode gausseidel")
    print("\nSolusi SPL:")
    for i, value in enumerate(result):
        print(f"x{i + 1} = {value}")
