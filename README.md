# Kalkulator Aljabar Linier dengan Visualisasi

Program ini adalah kalkulator aljabar linier interaktif berbasis Python yang mendukung berbagai operasi aljabar linier serta menyertakan visualisasi grafik untuk membantu memahami hasil perhitungan.

## Fitur

1. **Mencari solusi persamaan linier**
   - Menyelesaikan sistem persamaan linier menggunakan matriks koefisien dan matriks hasil.
   - Menampilkan solusi dalam grafik 2D jika sistem berukuran 2x2.

2. **Mencari matriks inverse**
   - Menghitung inversi matriks persegi.

3. **Mencari determinan matriks**
   - Menghitung determinan matriks persegi.
   - Menampilkan grafik area paralelogram untuk matriks 2x2.

4. **Mencari nilai eigen dan vektor eigen**
   - Menghitung nilai eigen dan vektor eigen dari matriks persegi.
   - Menampilkan grafik eigenvektor untuk matriks 2x2.

5. **Menyelesaikan persamaan non-linier**
   - Menyelesaikan persamaan non-linier simbolik.
   - Menampilkan grafik fungsi dan solusinya.

6. **Menampilkan properti matriks**
   - Menghitung trace, rank, dan norm matriks.
   - Menampilkan heatmap matriks.

## Prasyarat

Sebelum menjalankan program, pastikan Anda memiliki:
- Python 3.7 atau versi lebih baru.
- Paket berikut:
  - `numpy`
  - `sympy`
  - `matplotlib`

Anda dapat menginstal paket yang diperlukan dengan perintah berikut:
```bash
pip install numpy sympy matplotlib
```

## Cara Menjalankan

1. Simpan kode Python di file, misalnya `linear_algebra_calculator.py`.
2. Jalankan program menggunakan Python:
   ```bash
   python linear_algebra_calculator.py
   ```
3. Masukkan ukuran matriks (baris/kolom) dan pilih operasi yang diinginkan.
4. Ikuti petunjuk untuk memasukkan matriks atau persamaan.

## Tampilan Antarmuka

Setelah menjalankan program, Anda akan melihat menu utama dengan opsi berikut:

```
=== Kalkulator Aljabar Linier dengan Visualisasi ===

Pilih operasi:
1. Mencari solusi persamaan linier
2. Mencari matriks inverse
3. Mencari determinan matriks
4. Mencari nilai eigen matriks
5. Menyelesaikan persamaan non-linier
6. Menampilkan properti matriks (trace, rank, norm)
7. Keluar
```

Pilih nomor operasi yang diinginkan dan ikuti langkah-langkah selanjutnya.

## Contoh Penggunaan

### 1. Mencari Solusi Persamaan Linier

Jika Anda memasukkan matriks berikut:
- Matriks A (koefisien):
  ```
  2 1
  1 3
  ```
- Matriks B (hasil):
  ```
  8 18
  ```

Hasilnya akan ditampilkan sebagai:
```
Hasilnya adalah:
[2. 6.]
```
Dan grafik solusi:
![Grafik Solusi](#)

### 2. Mencari Determinan Matriks

Untuk matriks 2x2 berikut:
- Matriks:
  ```
  3 4
  2 5
  ```

Hasil determinan:
```
Determinan dari A adalah:
7.0
```
Dan visualisasi area paralelogram:
![Visualisasi Determinan](#)
