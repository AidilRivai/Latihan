### Additional Funck
'''
print(abs(-5)) ## absolut ==> Mengabaikan arah Vector == Mengambil Nilai Positifnya
# negatif .... 0 ... Positif

nama='andre'
usia=25
alfabet = A - Z, a-z
numerik = 0-9
print(nama.isalnum()) ##melakukan pengencekan string, seluruh elemennya adalah alfabet dan numerik
#Tanpa karakter lain termasuk spasi
print(nama.isalpha()) ## melakukan pengencekan string, apakah seluruh string merupakan alfabet
print(nama.isdigit()) ## melakukan pengecekan string, apakah seluruh string merupakan alfabet
print(nama.isupper()) ## apakah string merupakan upper case
print(nama.islower()) ## apakah string merupakan lower case

## Hasil dari Fungsi namaVar.isxxx adalah Boolean (TRUE ATAU FALSE)
'''

angka= 'AB'
# print(angka.isalpha())
# print(angka.isalnum())
print(angka.isdigit())
'''
#### Looping

- Mengeksekusi suatu program yang sama, berulang kali

Jenis Looping:
-While Loop ==> secara natural ==> Infinite Loop
-For Loop ==> Secara natural ==> Finite Loop 

- Looping memiliki karakter yang mirip dengan IF statement 
- Looping Membutuhkan Conditional Statement Untuk diuji (Boolean - True atau False)
- program akan dijalankan jika conditional statement BERNILAI TRUE 
- Perbedaan signifikan antara IF dan LOOPING, IF hanya menjalankan program satu kali
- Sedangkan Loop menjalankan Program beberapa kali
- sama seperti IF, looping juga bisa dilakukan secara hirarki-bertingkat - Nested LOOP 
- IF ==> mengeksekusi program satu kali jika kondisi TRUE 
- Looping mengeksekusi Program beberapa kali selama kondisi bernilai TRUE
- Looping akan berhenti mengeksekusi program, ketika kondisi bernilai FALSE 
'''
#### While Loop
'''
Basic Syntax:
while ....kondisi....: ==> Conditional Statement (Pengujian True atau False)
    Program ==> akan dieksekusi selama kondisi bernilai true 


angka = 1 ### Inisiasi kondisi yang akan dilakukan pengujian (Define Variabel)
#### Pengujian dibutuhkan untuk memulai proses Looping

while angka < 10: ###pengecekan kondisi variabel
    print(f"Angka anda: {angka}") ## program yang akan dieksekusi selama kondisi bernilai TRUE
    angka += 1 ## dibutuhkan untuk membuat kondisi False
    ## Dibutuhkan Untuk Menghentikan Proses Looping/Iterasi
print(f"Angka anda {angka} program di luar looping")

#### Proses pengulangan pada looping lebih dikenal sebagai iterasi

### Proses Looping
# Iterasi Awal - Inisiasi pertama
# Iterasi 1 : Angka = 1
# Dilakukan Pengecekan Kondisi ===> angka<10
# 1<10 ===> True 

# Karena bernilai TRUE maka program dibawah while akan dieksekusi
# print(f"angka anda : {angka}")
# saat ini angka = 1

# angka anda = 1
# masuk ke program angka += 1 ==> Proses Increment Manual ==> Penambahan 1

# angka = angka +1 
# angka = 2
# Iterasi Pertama Selesai


angka = 689 ## variabel inisiasi untuk pengecekan kondisi looping
tebak = 8 ## Variabel inisiasi untuk pengecekan kondisi looping

#isi variabel antara angka dan tebak bebas, selama berbeda
while angka != tebak: ### Pengecekan kondisi, jika true program dibawah while (1 blok dgn while akan dieksekusi)
    tebak = int(input("Masukkan angka tebakan anda: "))
    if tebak == angka:
        print('Tebakan anda Benar!!')
    elif tebak > angka:
        print("angka dibawah tebakan anda")
    else:
        print("angka diatas tebakan anda")


password = "jack125"
Login = "a" ##isi bebas asalkan berbeda dengan password

coba = 1
batas_coba = 5

## coba dan batas_coba merupakan BATAS PERCOBAAN, User Input Password

while password != Login and coba <= batas_coba:
    if coba <= batas_coba:
        Login = input("Masukkan Password Anda: ")
        if Login != password and coba <= batas_coba:
            coba +=1
            print("password yang anda masukkan salah, silahkan coba lagi")
            print(f"percobaan ke - {coba}")
        elif Login != password and coba == batas_coba:
            coba +=1
            print("Password anda salah, kesempatan habis, silahkan coba 30 menit")
        else:
            print("Password anda benar anda berhasil login")


### While Loop
from _typeshed import OpenTextModeUpdating
from typing import DefaultDict


- Secara Natural ===> Infinite Loop 
- Inisiasi awal, perlu mendefine variabel
- menggunakan comparison operator/operator perbandingan (==, !=, <, >, dst) maupun logical operator (And, or, not)
- variable yang di define, digunakan di prosess comparison
- proses decrement/increment dilakukan manual
- decrement/increment dibutuhkan untuk menghentikan looping


### FOR LOOP

Secara natural ==> Finite Loop 
Inisiasi awal, Tidak perlu mendefine variable
hanyan menggunakan operator membership (IN)
Proses decrement/increment dilakukan secara otomatis 
sehingga proses menghentikan looping berjalan secara otomatis 

basic syntax: 
for ..... variabel .... in .....iterable object....:
    Program

variabel yanf digunakan bebas, tapi umumnya, hanya menggunakan 1 karakter
i,j,k,l,m,n, dst

contoh:
for karakter in kalimat:
    print(karakter)

for i in kalimat:
    print(i)

iterable object ==> object/data yang memiliki value lebih dari satu ==> string & data structure
non iterable object ==> integer, float, boolean
for loop (Proses looping) akan dijalankan selama kondisi bernilai TRUE ==> looping akan dijalankan hingga seluruh data iterables diakses

### range()
range()
- tipe data range ==? range mirip dengan akses indexing, tetapi berisi angka numerik
- angka berupa integer
- membuat deret angka
- angka yang digunakan hanya terbatas pada integer

range(start, end, step)

###range 1 angka
range(10) ==> ketika angka di dalam range hanya 1
angka tsb berarti nilai dari END

jika start dan step tidak ditentukan nilainya, maka akan menggunakan nilai Default
nilai default dari start ==> 0
nilai default dari step ==> 1 ==> secara default terjadi penambahan 1, increment otomatis

### range 2 angka
range (1,10) ==> ketika angka di dalam range ada 2 angka,
angka tersebut berarti nilai dari start dan end 
berarti nilai step menggunakan nilai default ==>

start dan end mengikuti aturan yang sama dg proses slicing/indexing 
start ==> inclusive
end ===> exclusive ==> akses/pembuatan deret angka akan berhenti di end - 1 (jika step increment 1) atau end+1 (jika step decrement -1)

###contoh

range(1,21,1) ==> akses Start = 1, END = 21-1 (akses berhenti di nilai 20), karena increment otomatis (Step=1)
range(20,1,-1) ==> akses start =20, end = 1+1 (akses berhenti di nilai 2), karena decrement otomatis (Step=-1)
'''

#contoh lagi:
# for i in range(10):
#     print(i)

# for i in range(1,21):
#     print(i)

kalimat = "makanan"

for i in kalimat:
    print(i.upper())


