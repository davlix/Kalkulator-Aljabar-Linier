import numpy as np

def solve_linear_equation():
    print("Masukkan koefisien matriks A (baris x kolom):")
    a = np.array([input().split() for _ in range(n)], dtype=float)
    print("Masukkan matriks B:")
    b = np.array(input().split(), dtype=float)
    x = np.linalg.solve(a, b)
    print("Hasilnya adalah:")
    print(x)

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

def find_eigenvalues():
    print("Masukkan matriks:")
    a = np.array([input().split() for _ in range(n)], dtype=float)
    eigvals = np.linalg.eigvals(a)
    print("Nilai eigen dari A adalah:")
    print(eigvals)

print("=== Kalkulator Aljabar Linier ===")
n = int(input("Masukkan jumlah baris/kolom: "))

while True:
    print("\nPilih operasi:")
    print("1. Mencari solusi persamaan linier")
    print("2. Mencari matriks inverse")
    print("3. Mencari determinan matriks")
    print("4. Mencari nilai eigen matriks")
    print("5. Keluar")
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
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
