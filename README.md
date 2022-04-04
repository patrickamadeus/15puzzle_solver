# 15puzzle_solver :jigsaw:

## Table of Contents
- [15puzzle_solver](#15puzzle_solver)
  - [Table of Contents](#table-of-contents)
  - [Algoritma Greedy](#algoritma-greedy)
  - [Requirement and Installation](#requirement-and-installation)
  - [Running Program](#running-program)
  - [Author](#author)

## Algoritma Branch & Bound
Algoritma Branch and Bound merupakan jenis algoritma yang digunakan untuk mencari solusi optimal untuk persoalan berbasis kombinatorial, diskrit, dan lainnya dengan memanfaatkan optimisasi secara matematis. Persoalan N-Puzzle (dalam implementasi Tugas Kecil kali ini 15-Puzzle) merupakan salah satu persoalan yang dapat diselesaikan dengan algoritma ini

## Requirement and Installation
Untuk dapat menjalankan permainan ini, maka pastikan perangkat sudah dilengkapi oleh aplikasi berikut :
1. [Python 3](https://www.python.org/downloads/)
2. Library PyGame (via pip / installer lain)


## Running Program
Program dapat dijalankan dengan cara :
1. Buat testcase **15 Puzzle** yang hendak dicari solusinya (pastikan format benar)
2. Masukkan file berekstensi `.txt` pada folder `/test`. Format file text adalah sebagai berikut:

    ```
    5 1 2 4
    9 6 3 8
    0 10 7 11
    13 14 15 12
    ```
    Setiap angkanya dibatasi oleh whitespace, dengan angka `0` menandakan block yang kosong. File test tidak diakhiri newline / terminator apapun.
3. Masuk ke folder `/src` dan jalankan `main.py`
4. Masukkan nama file yang telah dibuat berikut dengan ekstensi `.txt`. Sebagai contoh : 
    ```shell
    $ python main.py
    ...
    Enter your filename (with extension): tcY1.txt
    ...
    ```
5. Apabila puzzle solvable, lanjut ke tahap 6. Sebaliknya akan dikeluarkan luaran `NOT SOLVABLE`, seperti berikut:
    ```shell
    $ python main.py
    ...
    Enter your filename (with extension): tcX1.txt

    ...

    THIS PROBLEM IS NOT SOLVABLE
    ```
6. Pilih `(y/n)` untuk visualisasi
7. Visualisasi akan ditampilkan via window GUI (y) atau luaran terminal (n), beserta dengan informasi keberjalanan algoritma pada terminal. 
    - Contoh keluaran dengan pilihan `(n)` di terminal adalah sebagai berikut :
        ```shell
        $ python main.py
        ...

        Enter your filename (with extension): tcY1.txt

        ...

        The Problem is solvable!
        Please wait...

        Do you want to launch graphical visualization? (y/n) n

        Total Node(s) Needed to Solve : 52
        ALGORITHM RUNTIME: 0.00500 s
        ---------------------
        | 05 | 01 | 02 | 04 |
        -----+----+----+-----
        | 09 | 06 | 03 | 08 |
        -----+----+----+-----
        |    | 10 | 07 | 11 |
        -----+----+----+-----
        | 13 | 14 | 15 | 12 |
        -----+----+----+-----
        STEP 1: MOVE DOWN
        ---------------------
        | 05 | 01 | 02 | 04 |
        -----+----+----+-----
        |    | 06 | 03 | 08 |
        -----+----+----+-----
        | 09 | 10 | 07 | 11 |
        -----+----+----+-----
        | 13 | 14 | 15 | 12 |
        -----+----+----+-----


        ... (STEP LAINNYA)


        ---------------------
        | 01 | 02 | 03 | 04 |
        -----+----+----+-----
        | 05 | 06 | 07 | 08 |
        -----+----+----+-----
        | 09 | 10 | 11 |    |
        -----+----+----+-----
        | 13 | 14 | 15 | 12 |
        -----+----+----+-----
        STEP 8: MOVE UP
        ---------------------
        | 01 | 02 | 03 | 04 |
        -----+----+----+-----
        | 05 | 06 | 07 | 08 |
        -----+----+----+-----
        | 09 | 10 | 11 | 12 |
        -----+----+----+-----
        | 13 | 14 | 15 |    |
        -----+----+----+-----
        PROBLEM SOLVED!!
        ```
        **NB : Mekanisme `MOVE` program ini memiliki persepektif pada pergerakan ubin, bukan pergerakan slot kosong, sebagai contoh `MOVE UP` berarti ubin N bergerak ke atas mengisi slot kosong**

    - Contoh keluaran dengan pilihan `(y)` dapat dilihat pada laporan di folder `/docs`

## Author
Patrick Amadeus Irawan (13520109)
