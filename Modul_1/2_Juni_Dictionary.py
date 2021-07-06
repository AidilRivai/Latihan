'''
### Dictionary
- Asosiasi - Mapping - Kamus

Kata: Definisi
Keywords : Definition
Key : Value

#### General Char
- yang memisahkan antara Key dan Value adalah Titik dua (:)
- Key + Value ===> Item 
- yang memisahkan antar item adalah tanda koma (,)
- Key umumnya berbentuk String atau integer atau keduanya
- Value bisa berupa tipe data apapun

# Contoh
Dict_A = {}
Dict_B = dict(data)

dict_C = {
    key: value,
    key1: value1,
    key2: value2,
    dst
}
'''
# Contoh penggunaan
nilai = {
    "Andi":85,
    "Beni":96,
    "Dodi":75,
    "Riko":80,
    "Andre":90
}

###CRUD
### Read Data - Akses Data
'''
Basic Syntax:
NamaDictionary[Keyword]
'''

print(nilai['Andre'])
print(nilai['Andi'])

print(nilai.keys()) # Memunculkan isi seluruh keys dari dictionary
print(nilai.values()) # Memunculkan isi seluruh Value dari dictionary
print(nilai.items()) # Memunculkan items (Pasangan antara keys:values)

### Create Data - Menambahkan Data Baru
# Basic Syntax:
# Namadict[Keywords] = Values 

nilai['Jeki'] = 87
print(nilai)

##### Update Data - Sama seperti Create Data, hanya saja, keywords yang digunakan adalah keywords lama

nilai['Jeki']=100
print(nilai)

#### Hapus data - Delete
# basic syntax:
# namaDict.pop(Keys)
nilai.pop('Jeki')
print(nilai)


################### DEF Function
# General Characteristic
# - Memberikan nama untuk suatu Fungsi
# - Agar fungsi dapat digunakan berkali-kali tanpa perlu copas atau coding ulang
# - memiliki konsep yang sama dengan variabel,
# Bedanya variabel menyimpan data, kalau Def function menyimpan fungsi
# - Digunakan untuk fungsi yang sifatnya generik - umum
# - generik/umum ==> fungsi akan dipakai berkali-kali


# Basic Function:
# def NamaFunction(Argumen):
#     Program

# - NamaFunction => Nama Fucntion mengikuti aturan penamaan Variabel
# - Argumen => parameter, dan bersifat optional ==> bisa kosong
# - argumen juga bisa berisi ==> jumlah argumen tidak dibatasi
# - jumlah argumen bisa disesuaikan dengan kebutuhan

angka = 95
## Fungsi konvensional
if angka%2 == 0:
    print("genap")
else:
    print("ganjil")

#### Def Function - Konvensional
def cekbilangan(angka):
    if angka%2 == 0:
        print("genap")
    else:
        print("ganjil")

cekbilangan(959)


# ###### Return Function
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
#     return Value

#### Def Function dengan return Value ===> Return Function
def cekgenap(angka):
    if angka%2 == 0:
        return "Genap"
    else:
        return "Ganjil"

##############################
## Def Konvensional
cekbilangan(275)

## Return Function
print(cekgenap(263))

hasil = cekgenap(288)
print(hasil)

### Def Function Konvensiona ==> Pangkat
def Pangkat(x,y):
    hasil= x**y
    print(hasil)

#### Return Function ===> Pangkat
def pangkat2(x,y):
    hasil=x**y
    return hasil

# Hasil = Pangkat(4,4)
# print(Hasil * 7) #### tidak bisa untuk def function konvensional

hasil = pangkat2(5,6)
print(hasil*7)