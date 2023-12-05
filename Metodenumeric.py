import matplotlib.pyplot as plt
import numpy as np

#################################################### Bisection

def fungsi(x, n):
    return 500 - x**3 + n*x

def bisection(a, b, n, toleransi=0.01, max_iter=100):
    c = (a + b) / 2

    iterasi = 1
    while iterasi <= max_iter:
        error = abs((b - a) / c) if c != 0 else abs(b - a)

        if fungsi(c, n) == 0 or error < toleransi:
            break
        elif fungsi(a, n) * fungsi(c, n) < 0:
            b = c
        else:
            a = c

        c = (a + b) / 2
        iterasi += 1

    return c

# Nilai n dari nomor kelompok
n = 7

# Nilai awal tebakan a dan b
a = -10
b = 10

# Mendapatkan nilai x yang memenuhi fungsi f(x) = 0 menggunakan Metode Bisection
nilai_x = bisection(a, b, n)
print("Nilai x dengan Metode Bisection:", nilai_x)

#################################################### Newton Rhapson

def fungsi(x, n):
    return 500 - x**3 + n*x

def turunan_fungsi(x, n):
    return -3*x**2 + n

def newton_raphson(x, n, toleransi=0.01, max_iter=100):
    iterasi = 1
    while True:
        x_baru = x - (fungsi(x, n) / turunan_fungsi(x, n))
        error = abs((x_baru - x) / x_baru)
        x = x_baru
        if error < toleransi or iterasi >= max_iter:
            break
        iterasi += 1
    return x

# nomor kelompok
n = 7

# Nilai awal tebakan
tebakan_awal = 10

nilai_x_newton = newton_raphson(tebakan_awal, n)
print("Nilai x dengan Metode Newton-Raphson:", nilai_x_newton)

#################################################### Metode Secant

def fungsi(x, n):
    return 500 - x**3 + n*x

def secant(x0, x1, n, toleransi=0.01, max_iter=100):
    iterasi = 1
    while True:
        x_baru = x1 - (fungsi(x1, n) * (x1 - x0)) / (fungsi(x1, n) - fungsi(x0, n))
        error = abs((x_baru - x1) / x_baru)
        x0 = x1
        x1 = x_baru
        if error < toleransi or iterasi >= max_iter:
            break
        iterasi += 1
    return x_baru

# Nilai n dari nomor kelompok
n = 7

# Nilai awal tebakan
x0 = 0
x1 = 10

nilai_x_secant = secant(x0, x1, n)
print("Nilai x dengan Metode Secant:", nilai_x_secant)

#################################################### Regula Falsi

def fungsi(x, n):
    return 500 - x**3 + n*x

def regula_falsi(a, b, n, toleransi=0.01, max_iter=100):
    iterasi = 1
    while True:
        c = (a*fungsi(b, n) - b*fungsi(a, n)) / (fungsi(b, n) - fungsi(a, n))
        error = abs((c - b) / c)
        if fungsi(a, n) * fungsi(c, n) < 0:
            b = c
        else:
            a = c
        if error < toleransi or iterasi >= max_iter:
            break
        iterasi += 1
    return c

# Nilai n dari nomor kelompok
n = 7

# Nilai awal tebakan dari a dan b
a = -10
b = 10

nilai_x_regula_falsi = regula_falsi(a, b, n)
print("Nilai x dengan Metode Regula Falsi:", nilai_x_regula_falsi)


######################################################################## Menampilkan Plot

x_range = np.linspace(-10, 10, 1000)

# Menghitung relative error 
relative_error_bisection = [abs(bisection(a, b, n) - nilai_x) / nilai_x for a, b in zip(x_range, x_range[1:])]
relative_error_newton = [abs(newton_raphson(x0_newton, n) - nilai_x_newton) / nilai_x_newton for x0_newton in x_range]
relative_error_secant = [abs(secant(x0_secant, x1_secant, n) - nilai_x_secant) / nilai_x_secant for x0_secant, x1_secant in zip(x_range, x_range[1:])]
relative_error_regula_falsi = [abs(regula_falsi(a, b, n) - nilai_x_regula_falsi) / nilai_x_regula_falsi for a, b in zip(x_range, x_range[1:])]

# Plot hasil dari keempat metode
plt.figure(figsize=(10, 6))
plt.plot(x_range[1:], relative_error_bisection, label='Bisection')
plt.plot(x_range, relative_error_newton, label='Newton-Raphson')
plt.plot(x_range[1:], relative_error_secant, label='Secant')
plt.plot(x_range[1:], relative_error_regula_falsi, label='Regula Falsi')

plt.title('Grafik Relative Error Metode Numerik untuk f(x)')
plt.xlabel('Nilai x')
plt.ylabel('Relative Error')
plt.legend()

# Menampilkan plot
plt.grid()
plt.show()