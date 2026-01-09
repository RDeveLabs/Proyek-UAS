# Proyek UAS

## Identitas Mahasiswa
Nama : Raihan Arrasyid Monadika  
NIM : 312510206  
Kelas : TI.25.A.2

Repositori ini berisi implementasi proyek UAS berbasis Python dengan konsep modular dan OOP (Object Oriented Programming).  
Proyek dikembangkan untuk memenuhi tugas akhir mata kuliah, dengan fokus pada pembuatan aplikasi kalkulator sederhana yang memiliki pemisahan logika, data, dan tampilan.

## Struktur Proyek
- **Kalkulator.py** → Script utama untuk menjalankan aplikasi.
- **data.py** → Modul untuk pengelolaan data dan variabel.
- **proses.py** → Modul berisi logika perhitungan dan proses utama.
- **view.py** → Modul tampilan/output ke pengguna.
- **.gitignore** → File konfigurasi untuk mengecualikan file tertentu dari Git.

## Demo & Dokumentasi
Proses pembuatan dan demo aplikasi dapat dilihat di YouTube: https://youtu.be/5WhOzG6dpog

## Bahasa Pemrograman
Python 100%

## Flowchart

## Struktur dan peran tiap file
1. Kalkulator.py  
  Peran: Script utama yang mengeksekusi aplikasi. Fungsinya:
    - Menginisialisasi data awal (misalnya angka pertama/kedua, operator).
    - Memanggil fungsi dari proses.py untuk melakukan perhitungan.
    - Menggunakan view.py untuk menampilkan hasil atau pesan ke pengguna.

    Alur umum:  
    - Ambil input (CLI atau fungsi).
    - Validasi input (angka valid, operator valid).
    - Panggil fungsi proses (tambah, kurang, kali, bagi).
    - Tampilkan hasil lewat modul view.

2. data.py  
  Peran: Menyediakan struktur data dan utilitas validasi agar logika tetap bersih.  
  Fungsi: validasi (cek angka, cek operator).

3. proses.py  
  Peran: Inti kalkulasi—fungsi yang menerima input terstruktur dan mengembalikan hasil.
  Fungsi:
    - bagi(a, b).
    - Penanganan error (misalnya pembagian dengan nol).
  
4. view.py  
  Peran: Memisahkan presentasi dari logika. Menangani:
    - Format output (misalnya “Hasil: 2 + 3 = 5”).
    - Pesan error yang ramah pengguna (misalnya “Operator tidak dikenali”).
    - Bisa juga menangani input jika ingin CLI interaktif (prompt, menu).
