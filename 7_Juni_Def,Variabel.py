### Variabel
'''
Global Variabel ==> Variabel yang di define di luar function
bisa digunakan disemua tempat

Local Variabel ==> variabel yang di define di dalam function
hanya bisa digunakan di function tersebut. (tempat dimana variabel tersebut di define)
'''
'''
a=20 ## Global Variabel

def totalbelanja(): ## Inisiasi Def Function
    a = 25 ## Local Variabel
    harga= 65000 ## Local Variabel
    total= harga*a ## Local Variabel
    print(f"Nilai A - Local Variabel dalam def function {a}")
    print(f"harga apel {a} Kilo adalah {total}")

totalbelanja() ## Memanggil - atau menggunakan def function
print(f"Nilai A - Global Variabel {a}")

def totalbelanja2():
    a=80
    harga= 100000
    total= harga*a
    print(f"harga apel {harga}")
    print(f"nilai a - local variabel dalam def function {a}")
    print(f"harga apel {a} kilo adalah {total}")

totalbelanja2()
print("="*50)
totalbelanja()
print("="*50)
print(f"nilai a global adalah {a}")
'''
### untuk menggunakan global variabel ke dalam function, 
# kita dapat memasukkan nilai global variabel tersebut ke dalam argumen/parameter dari function

### Argumen - Parameter

# -Argumen ==> Local Variabel, tetapi Value nya kita yang tentukan dari luar function / dari global variabel
# -Fungsi dari argumen ==> memasukkan value ke dalam local variabel
# -value kita tentukan/masukkan ketika memanggil function
# -pemberian nama argumen, sama dengan pemberian nama variabel
'''
### Single Argument
def belanjaan(berat): ## berat adalah arguman yang akan digunakan sebagai local variabel
    # value dari berat ditentukan berdasarkan inputan dari user
    # ketika memanggil function
    harga = 50000
    total = berat*harga
    print(f"Harga pisang {berat} adalah {total}")

# belanjaan(berat) ##Memanggil function sekaligus memasukkan value ke dalam argumen
belanjaan(5)

Belanja = int(input('anda mau beli berapa kilo: '))
belanjaan(Belanja)

'''
def Guru(nama,pelajaran):
    print(f"nama guru adalah {nama}")
    print(f"mengajar pelajaran {pelajaran}")
'''
# Guru("Roni", "Sejarah")
# Guru("Ekonomi","Susi") ## akan salah hasilnya, urutan memasukkan value harus sama dengan urutan argumen
# Guru("Mike") ## Akan Error, jumlah value harus sama dengan jumlah argumen
# argumen ada 2 => nama dan pelajaran, value hanya 1 ==> Mike
# Guru("Gio","Fisika","Kimia") 
# Argumen ada 2 => nama dan pelajaran, value ada 3 ==> gio, fisika, kimia

# Guru(5.7, 90) ## tidak akan error, karena value yang dimasukkan 2, meskipun integer dan float
# Guru(["adit","adi"],["kimia","fisika"])

##### Keywords
Guru(pelajaran="Ekonomi",nama="Susi")
# Ketika menggunakan keywords, meskipun posisi terbalik, hasil akan benar

#### Keywords ===> menggunakan nama argumen ketika input value
# Guru(nama="Andi", pelajaran="English") #pasti benar
Guru(nama="Harry") ## Akan Error, jumlah value harus sama dengan jumlah argumen
# argumen ada 2 => nama dan pelajaran, value hanya 1
'''
##### Default Value #####
def employee(nama, jabatan="staff", gaji=1000):
    print(f"Nama Pegawai {nama}")
    print(f"bekerja sebagai {jabatan}")
    print(f"memiliki gaji sebesar {gaji}")

# employee("Deni","Manajer",1500)
# employee(nama="rendi",gaji="4000") ## tidak akan error karena jabatan sudah ada nilai default
# employee(nama="ardi") ##tidak akan error karena jabatan dan gaji sudah ada nilai default
# employee("tedi") ## tidak akan error karena jabatan dan gaji sudah ada nilai default
# employee(jabatan="direktur", gaji=10000) ### error karena nama tidak ada nilai default

#### Return Function
# - Function dengan Return Value
# - Function hanya mengembalikan Value 
# - Value yang dikembalikan bebas, tergantung kebutuhan kita
# - ketika kita hanya ingin mendapatkan hasil dari fungsi/program di dalam function 
# - dengan menggunakan return function kita dapat memasukkan hasil dari fungsi ke dalam variabel
# - atau bisa langsung digunakan untuk fungsi atau kalkulasi lanjutan
# - penentuan value yang akan direturn sangat krusial
# - jumlah value yang akan direturn tidak dibatasi

# Basic Syntax:
# def namaFunction(Argumen):
#     program
#     return Value ## Value bebas, sesuai kebutuhan

angka = 80
##Fungsi konvensional
# if angka%2 == 0:
#     print("genap")
# else:
#     print("ganjil")

### Dengan def Function
def cekbil(x):
    if x%2==0:
        print("Genap")
    else:
        print("Ganjil")

# cekbil(angka)

### Dengan return value ==> Return Function
def gangen2(x):
    if x%2 == 0:
        return "GENAP"
    else:
        return "GANJIL"

#### Cara Memanggil - Menggunakan Function

### Def Function konvensional
# cekbil(angka)
# print("="*50)

### Return Function
# print(gangen2(angka))

### Ketika menggunakan return function, tidak ada perintah print() di dalam fungsinya.

############# Return Function

# def kuadrat(x):
#     hasil = x**2
#     return hasil

# print(kuadrat(5))

# def kuadrat(x):
#     hasil = x**2
#     return "Hello World"

# print(kuadrat(5))

# def kuadrat(x):
#     hasil=x**2
#     return x
# print(kuadrat(5))

# def kuadrat(x):
#     return x**2

# print(kuadrat(10))

# def kuadrat(x):
#     return x**2

# kalkulasi = kuadrat(7)*100
# print(kalkulasi)
# def kuadrat(x):
#     print(x**2)

# kalkulasi = kuadrat(8)*100 ### akan menghasilkan error, karena tidak bisa melakukan perkalian antara integer dan nonetype
# print(kalkulasi)

# hasil = 500 ### Global Variabel
# def kuadrat(x):
#     hasil = x**2 ### meskipun namanya sama, ini merupakan local variabel
#     return hasil ### Local Variabel, tidak mempengaruhi global variabel

# # print(kuadrat(10))

# # print(f"isi variabel hasil adalah {hasil}") ### yang digunakan tetap value dari global variabel

# def pangkat(x,y):
#     hasil = x**y
#     return hasil

# def perkalian(x,y):
#     hasil = x*y
#     return hasil

# kalkulasi = kuadrat(8) * 75
# # print(kalkulasi)

# A = kuadrat(10)
# B = pangkat(2,4)

# print(A)
# print(B)

# C = perkalian(A,B)

# print(C)

# totalkalkulasi= perkalian(kuadrat(10),pangkat(2,4))
# print(totalkalkulasi)

### menggunakan def function konvensional
def kuadrat1(x):
    hasil= x**2
    print(hasil)

def perkalian1(x,y):
    hasil = x*y
    print(hasil)

def pangkat1(x,y):
    hasil = x**y
    print(hasil)

A = kuadrat1(10)
B = pangkat1(2,4)

totalcalc= perkalian1(kuadrat1(10),pangkat1(2,4))

# print(totalcalc)

# print(print(36)*print(16))

