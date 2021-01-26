# Cryptarithm-solver

Program ini adalah program untuk menyelesaikan suatu persoalan cryptarithm. Program ini menggunakan metode brute force dengan bahasa python 3. Program ini akan menampilkan semua solusi dari cryptarithm yang diberikan (jika ada), menuliskan berapa banyak tes beserta waktu yang dibutuhkan.

Program ini dapat langsung dijalankan. Terdapat dua opsi cara memasukkan input soal:
1. Memasukkan secara manual
Dalam memasukkan soal, perhatikan bahwa perlu ada minimal empat baris. Baris pertama sampai baris ketiga terakhir adalah semua kata yang ingin dimasukkan. Khusus untuk kata terakhir, akhiri dengan tanda '+'. Baris kedua terakhir menunjukkan tanda garis dan dibebaskan untuk memasukkan beberapa tanda '-'. Baris terakhir adalah hasil dari kata yang ingin dimasukkan.
Sebagai contoh, apabila ingin mencari solusi dari cryptarithm SEND + MORE = MONEY, format memasukkannya adalah 
```
SEND
MORE+
-----
MONEY
```
2. Memasukkan melalui file eksternal
Masukan juga bisa ditulis melalui file eksternal yang berformat .txt. dan hasilnya akan ditulis ke file eksternal yang juga berformat .txt. Format memasukkannya juga sama seperti memasukkan secara manual. Namun, perlu diperhatikan bahwa satu file hanya bisa memasukkan satu masukan saja dan file diakhiri dengan new line (\n).
```
SEND
MORE+
-----
MONEY

```

Program ini ditulis Akeyla Pradia Naufal dengan NIM 13519178 sebagai tugas kecil 1 dari mata kuliah IF2211 Strategi Algoritma tahun ajaran 2020/2021 semester genap.
