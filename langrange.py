import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_values, y_values, k):
    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term = term * (k - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

# Provide the dataset
data = """5
100.0 9.0
200.0 11.0
300.0 19.0
400.0 21.0
500.0 23.0"""

# Convert the provided data string to a list of tuples
data_lines = data.strip().split('\n')
n = int(data_lines[0])
data_values = [tuple(map(float, line.split())) for line in data_lines[1:]]

# Extract x_values and y_values from the data
x_values, y_values = zip(*data_values)

# Tampilkan data yang diberikan
print("===== Metode Langrange =====")
print("Data banyaknya produk terhadap banyaknya pekerja:")
for i in range(n):
    print(f"x {i + 1} = {x_values[i]}  y {i + 1} = {y_values[i]}")

# Masukkan titik data untuk menghitung nilai
k = float(input("Masukkan data jumlah pekerja: "))

# Hitung interpolasi menggunakan polinomial orde 3
result = lagrange_interpolation(x_values[:4], y_values[:4], k)  # Menggunakan empat titik data terdekat

# Tampilkan nilai hasil interpolasi
print(f"Produk yang dihasilkan {k} pekerja adalah {result} ton")

# Visualisasi data dan hasil interpolasi
x_values_np = np.array(x_values)
y_values_np = np.array(y_values)

plt.scatter(x_values_np, y_values_np, label='Data yang Diberikan')
plt.scatter(k, result, color='red', label=f'Interpolasi pada {k} pekerja: {result} ton')
plt.legend()
plt.xlabel('Banyaknya Pekerja')
plt.ylabel('Banyaknya Produk')
plt.title('Interpolasi Lagrange')
plt.show()
