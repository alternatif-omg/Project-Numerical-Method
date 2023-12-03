import numpy as np
import matplotlib.pyplot as plt

def lu_decomposition(matrix):
    n = len(matrix)
    lower = np.zeros((n, n))
    upper = np.zeros((n, n))

    for i in range(n):
        # Upper triangular matrix
        for k in range(i, n):
            sum_ = 0
            for j in range(i):
                sum_ += lower[i][j] * upper[j][k]
            upper[i][k] = matrix[i][k] - sum_

        # Lower triangular matrix
        for k in range(i, n):
            if i == k:
                lower[i][i] = 1  # Diagonal elements are 1
            else:
                sum_ = 0
                for j in range(i):
                    sum_ += lower[k][j] * upper[j][i]
                lower[k][i] = (matrix[k][i] - sum_) / upper[i][i]

    return lower, upper

def forward_substitution(lower, b):
    n = len(b)
    y = np.zeros(n)

    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= lower[i][j] * y[j]

    return y

def backward_substitution(upper, y):
    n = len(y)
    x = np.zeros(n)

    for i in reversed(range(n)):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= upper[i][j] * x[j]
        x[i] /= upper[i][i]

    return x

def lu_decomposition_visualization(matrix):
    n = len(matrix)
    lower = np.zeros((n, n))
    upper = np.zeros((n, n))
    steps = []

    for i in range(n):
        step = {}
        step['iteration'] = i + 1

        # Upper triangular matrix
        for k in range(i, n):
            sum_ = 0
            for j in range(i):
                sum_ += lower[i][j] * upper[j][k]
            upper[i][k] = matrix[i][k] - sum_

        step['upper'] = np.copy(upper)

        # Lower triangular matrix
        for k in range(i, n):
            if i == k:
                lower[i][i] = 1  # Diagonal elements are 1
            else:
                sum_ = 0
                for j in range(i):
                    sum_ += lower[k][j] * upper[j][i]
                lower[k][i] = (matrix[k][i] - sum_) / upper[i][i]

        step['lower'] = np.copy(lower)

        steps.append(step)

    return steps

def solve_lu_decomposition(matrix, b):
    lower, upper = lu_decomposition(matrix)
    y = forward_substitution(lower, b)
    x = backward_substitution(upper, y)
    return x

def plot_lu_decomposition_steps(steps):
    fig, axes = plt.subplots(len(steps), 3, figsize=(15, 5 * len(steps)))

    for i, step in enumerate(steps):
        axes[i, 0].imshow(step['upper'], cmap='Blues', interpolation='none')
        axes[i, 0].set_title(f'Upper {step["iteration"]}')

        axes[i, 1].imshow(step['lower'], cmap='Reds', interpolation='none')
        axes[i, 1].set_title(f'Lower {step["iteration"]}')

        combined_matrix = np.dot(step['lower'], step['upper'])
        axes[i, 2].imshow(combined_matrix, cmap='Greens', interpolation='none')
        axes[i, 2].set_title('Lower * Upper')

    plt.tight_layout()
    plt.show()

# Mengonversi persamaan menjadi bentuk matriks
coefficients = np.array([[8, 1, 1], [1, 8, 1], [1, 1, 8]], dtype=float)
constants = np.array([10, 10, 10], dtype=float)
augmented_matrix = np.column_stack((coefficients, constants))

# Visualisasi dekomposisi LU
steps = lu_decomposition_visualization(augmented_matrix)
plot_lu_decomposition_steps(steps)

# Menyelesaikan SPL dengan metode Dekomposisi LU
solution = solve_lu_decomposition(coefficients, constants)
print("\nMetode dekomposisi LU")
print("\nSolusi SPL:")
for i, value in enumerate(solution):
    print(f"x{i + 1} = {value}")
