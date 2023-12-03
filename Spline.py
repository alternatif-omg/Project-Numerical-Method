import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Data yang ditambahkan secara langsung
data = """5
100.0 9.0
200.0 11.0
300.0 19.0
400.0 21.0
500.0 23.0"""

# Konversi data string ke list of tuples
data_lines = data.strip().split('\n')
n = int(data_lines[0])
data_values = [tuple(map(float, line.split())) for line in data_lines[1:]]

# Extract x_values dan y_values dari data
x_values, y_values = zip(*data_values)

# Tampilkan data yang diberikan
print("===== Metode Spline =====")
print("Data banyaknya produk terhadap banyaknya pekerja:")
for i in range(n):
    print(f"x {i + 1} = {x_values[i]}  y {i + 1} = {y_values[i]}")

# Konversi ke numpy array
x_values_np = np.array(x_values)
y_values_np = np.array(y_values)

# Interpolasi menggunakan Cubic Spline
spline = CubicSpline(x_values_np, y_values_np)

# Masukkan titik data untuk menghitung nilai
k = float(input("Masukkan data jumlah pekerja: "))

# Hitung interpolasi menggunakan spline
result = spline(k)

# Tampilkan nilai hasil interpolasi
print(f"Produk yang dihasilkan {k} pekerja adalah {result} ton")

# Visualisasi data dan hasil interpolasi
x_range = np.linspace(min(x_values_np), max(x_values_np), 100)
y_spline = spline(x_range)

plt.scatter(x_values_np, y_values_np, label='Data yang Diberikan')
plt.scatter(k, result, color='red', label=f'Interpolasi pada {k} pekerja: {result:.2f} ton')
plt.plot(x_range, y_spline, label='Cubic Spline', linestyle='--', color='green')
plt.legend()
plt.xlabel('Banyaknya Pekerja')
plt.ylabel('Banyaknya Produk')
plt.title('Interpolasi Cubic Spline')
plt.show()
