import numpy as np
import matplotlib.pyplot as plt

def gaussian_jordan_elimination(matrix):
    n = len(matrix)

    for i in range(n):
        # Pivoting
        pivot = matrix[i][i]
        if pivot == 0:
            raise ValueError("Matrix is singular. Cannot proceed with Gaussian-Jordan elimination.")

        # Scaling the pivot row
        matrix[i] = matrix[i] / pivot

        # Elimination
        for j in range(n):
            if j != i:
                ratio = matrix[j][i]
                matrix[j] -= ratio * matrix[i]

    return matrix

def plot_spl_solution(solution):
    # Plot titik solusi
    plt.scatter(range(1, len(solution) + 1), solution[:, 0], color='r', marker='o', label='Solusi SPL')

    # Persamaan SPL
    x_spl = np.linspace(0, len(solution) + 1, 100)
    y_spl1 = (10 - 8 * x_spl) / 1
    y_spl2 = (10 - x_spl) / 8
    y_spl3 = (10 - x_spl) / 8

    # Plot garis SPL
    plt.plot(x_spl, y_spl1, label='8x1 + x2 + x3 = 10', color='b')
    plt.plot(x_spl, y_spl2, label='x1 + 8x2 + x3 = 10', color='g')
    plt.plot(x_spl, y_spl3, label='x1 + x2 + 8x3 = 10', color='y')

    plt.xlabel('Index')
    plt.ylabel('Solution Values')
    plt.title('Visualisasi Solusi SPL dan Persamaan SPL')
    plt.legend()
    plt.grid(True)
    plt.show()

# Masukkan koefisien SPL dan hasilnya ke dalam matriks augmented
augmented_matrix = np.array([
    [8, 1, 1, 10],
    [1, 8, 1, 10],
    [1, 1, 8, 10]
], dtype=float)

# Selesaikan SPL menggunakan metode Gaussian-Jordan
solution_matrix = gaussian_jordan_elimination(augmented_matrix)

# Hasilnyaa
solution = solution_matrix[:, -1].reshape((-1, 1))  # Extract the last column and reshape to a column vector
print("Metode Gaussian Jordan")
print("Solusi SPL:")
print(solution)

# Visualisasikan solusi SPL
plot_spl_solution(solution)
