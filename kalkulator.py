import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def solve_linear_equation():
    print("Masukkan koefisien matriks A (baris x kolom):")
    a = np.array([input().split() for _ in range(n)], dtype=float)
    print("Masukkan matriks B:")
    b = np.array(input().split(), dtype=float)
    x = np.linalg.solve(a, b)
    print("Hasilnya adalah:")
    print(x)

    if n == 2:
        plt.figure()
        for i in range(n):
            plt.plot([0, a[i][0]], [0, a[i][1]], label=f"Persamaan {i + 1}")
        plt.scatter(x[0], x[1], color='red', label="Solusi")
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid()
        plt.title("Visualisasi Persamaan Linier")
        plt.legend()
        plt.show()

def find_inverse():
    print("Masukkan matriks:")
    a = np.array([input().split() for _ in range(n)], dtype=float)
    a_inv = np.linalg.inv(a)
    print("Matriks inverse dari A adalah:")
    print(a_inv)

def find_determinant():
    print("Masukkan matriks:")
    a = np.array([input().split() for _ in range(n)], dtype=float)
    det = np.linalg.det(a)
    print("Determinan dari A adalah:")
    print(det)

    if n == 2:
        plt.figure()
        plt.quiver([0, 0], [0, 0], [a[0][0], a[1][0]], [a[0][1], a[1][1]], angles='xy', scale_units='xy', scale=1, color=['r', 'b'])
        plt.title("Visualisasi Determinan (Area Paralelogram)")
        plt.grid()
        plt.show()

def find_eigenvalues():
    print("Masukkan matriks:")
    a = np.array([input().split() for _ in range(n)], dtype=float)
    eigvals, eigvecs = np.linalg.eig(a)
    print("Nilai eigen dari A adalah:")
    print(eigvals)
    print("Vektor eigen dari A adalah:")
    print(eigvecs)

    if n == 2:
        origin = [0, 0]
        plt.figure()
        plt.quiver(*origin, eigvecs[:, 0], eigvecs[:, 1], color=['r', 'b'], scale=5)
        plt.title("Visualisasi Eigenvektor")
        plt.grid()
        plt.show()

def solve_nonlinear_equation():
    print("Masukkan persamaan non-linier (misalnya, x**2 - 4):")
    equation = sp.sympify(input())
    x = sp.symbols('x')
    solutions = sp.solveset(equation, x, domain=sp.S.Reals)
    print("Solusi dari persamaan adalah:")
    print(solutions)

    func = sp.lambdify(x, equation, 'numpy')
    x_vals = np.linspace(-10, 10, 500)
    y_vals = func(x_vals)
    plt.figure()
    plt.plot(x_vals, y_vals, label=str(equation))
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.scatter([float(sol) for sol in solutions], [0] * len(solutions), color='red', label="Solusi")
    plt.title("Grafik Persamaan Non-Linier")
    plt.grid()
    plt.legend()
    plt.show()

def matrix_properties():
    print("Masukkan matriks:")
    a = np.array([input().split() for _ in range(n)], dtype=float)
    trace = np.trace(a)
    rank = np.linalg.matrix_rank(a)
    norm = np.linalg.norm(a)
    print(f"Trace: {trace}")
    print(f"Rank: {rank}")
    print(f"Norm: {norm}")

    plt.figure()
    plt.imshow(a, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.title("Visualisasi Heatmap Matriks")
    plt.show()

print("=== Kalkulator Aljabar Linier dengan Visualisasi ===")
n = int(input("Masukkan jumlah baris/kolom: "))

while True:
    print("\nPilih operasi:")
    print("1. Mencari solusi persamaan linier")
    print("2. Mencari matriks inverse")
    print("3. Mencari determinan matriks")
    print("4. Mencari nilai eigen matriks")
    print("5. Menyelesaikan persamaan non-linier")
    print("6. Menampilkan properti matriks (trace, rank, norm)")
    print("7. Keluar")
    choice = int(input("Masukkan pilihan: "))

    if choice == 1:
        solve_linear_equation()
    elif choice == 2:
        find_inverse()
    elif choice == 3:
        find_determinant()
    elif choice == 4:
        find_eigenvalues()
    elif choice == 5:
        solve_nonlinear_equation()
    elif choice == 6:
        matrix_properties()
    elif choice == 7:
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
