## Operator Gabungan - Numerik
#- Variabel yang akan digunakan, harus sudah didefinisikan terlebih dahulu/ sudah memiliki value sebelumnya
'''
angka = 10
# #angka = angka + 15
# #print(angka)

# angka += 15 ## bentuk sederhana/bentuk lain dari angka = angka + 15(plus bisa diganti * - / // %)
# print(angka)

# print(pow(2,3)) ##built in python
# print(2**3) ##2 pangkat 3

### Operator Perbandingan - Comparison
# Hasil dari operator perbandingan ==> Boolean ==> True atau False
# Output ==> Boolean ==> True or False

# a == b ## a sama nilainya dengan b
# a != b ## a tidak sama nilainya dengan b

a=5
b=5
# c=5

# print (a==b==c) ## hasilnya akan True jika nilainya Sama
# print (a!=b!=c) ## hasilnya akan True jika hasilnya tidak sama

# a=5
# b=5.0
# print(a==b) ## akan menghasilkan TRUE meskipun float dan integer

# a=5
# b= '5'
# print(a==b)## akan menghasilkan False karena string dan integer

# a= 5.0
# b= '5'
# print(a==b) ## akan menghasilkan false karena string dan float
# ## == akan menghasilkan true jika keduanya numerik dan nilainya sama, jika numerik dan string, meskipun nilainya "sama" akan bernilai false

# a='andi'
# b='dnoi'
# print (a==b)

## operator "==" dan "!=" bisa digunakan untuk tipe data string, tidak terbatas di numerik

#### operator dibawah ini, mengharuskan tipe data yang digunakan adalah numerik

a>b 
a<b
a<=b
a>=b
'''
'''
# a=5
# b='5'

# print(a != b)
# print(a == b)

## print(a > b) ## error karena tidak sama

# a=5
# b=10

# print(a>=b)

# ## Operator Logika ==> menghasilkan True atau False
# AND 
# OR 
# NOT ==> Menghasilkan nilai kebalikannya True ==> False, False ==> True ===> Umumnya Jarang digunakan
# a AND b ===> akan menghasilkan TRUE jika KEDUANYA TRUE, jika kondisi A dan kondisi B menghasilkan TRUE  
# a OR b ===> akan menghasilkan FALSE jika KEDUANYA FALSE, jika kondisi A dan kondisi B menghasilkan FALSE

a = 5
b = 10
c = 15
d = 20

# print(a or b) ##tidak seperti ini
print((a<b)and(d>c))
print((a<b)and(d>c)and(c<d)) ## bisa lebih dari 2 kondisi, akan true karena semua yang kondisi yang diuji menghasilkan TRUE
print(True and True)

print(b<a)
print(d<c)
print((b<a)or(d<c))
## menghasilkan FALSE karena 2 kondisi yang diuji menghasilkan FALSE

print(not(b<a))

## AND dan OR dapat digunakan bersamaan sesuai kebutuhan
# ((a>b)or(a<c)) and (b>d) ##Contohnya

### Operator Membership ==> menghasilkan TRUE atau False
## IN dan NOT IN
# Digunakan hanya untuk STRING dan Data Collection

kalimat = 'Nama Saya Jeki dan saya tinggal di Jakarta'

## IN akan menghasilkan TRUE jika karakter ada di dalam STRING
print('Saya' in kalimat)
print('Andre' in kalimat)
print('z' in kalimat)
#print(5 in kalimat) ## Harus STRING tidak boleh integer
print('5' in kalimat)
print('i' in kalimat)

## NOT IN akan menghasilkan TRUE jika karakter TIDAK ADA di dalam STRING
print('w' not in kalimat)
print('a' not in kalimat)
'''
# usia = int(input("Masukkan usia: "))
# print(f"usia anda 10 tahun lagi adalah: {usia +10}") ##pake alternatif 4 yang ada di 27 Mei matematis

'''
##Error Handling Expression
basic syntax:
try:
    program .... ==> Program yang akan diuji ketika ada Errornya
except:
    Notifikasi atau program yang dijalankan ketika ada error
'''

# try:
#     usia = int(input("Masukkan usia: "))
#     nama = input("Masukkan nama: ")
#     usia = int(usia)
#     print(f"Nama anda {nama} usia anda 10 tahun lagi adalah: {usia +10}")
# except:
#     print("angka yang anda masukkan salah")

### Conditional Statement
## IF statement (WAJIB DIPAHAMI)
'''
Pengecekan Kondisi
Kondisi yang dicek adalah Apakah kondisi bernilai TRUE atau FALSE 

BASIC SYNTAX:
## jika ada 1 kondisi yang akan diuji/dicek
if ...kondisi...: ## Kondisi HARUS BERNILAI TRUE agar program dijalankan
    program ## jika ada 1 ketentuan


angka=int(input("Masukkan angka: "))
if angka > 20:
    print("angka yang anda masukkan diatas 20")

## Jika ada 2 ketentuan
if ...kondisi...:
    program1 - Ketentuan 1 #program 1 akan dijalankan KETIKA Kondisi BERNILAI TRUE
else:
    program2 - Ketentuan 2 #program 2 akan dijalankan KETIKA KOndisi BERNILAI FALSE
'''
# angka = int(input("Masukkan angka: "))
# if angka % 2 == 0:
#     print("Angka Genap")
# else:
#     print("Angka Ganjil")

# Jika hanya ada 2 ketentuan gunanak if .... else .... 

# Jika ada Ketentuan Lebih dari 2, Kondisi lebih dari 1

# basic Syntax:
# if ...kondisi 1...:
#     program 1 - ketentuan 1 ==> program akan dijalankan jika kondisi 1 bernilai TRUE 
# elif ...kondisi 2...:
#     program 2 - ketentuan 2 ==> program akan dijalankan jika kondisi 2 bernilai TRUE 
# elif ...kondisi3...:
#     program 3 - ketentuan 3 ==> program akan dijalankan jika kondisi 3 bernilai TRUE 
# dst....
# else:
#     program XX - ketentuan XX ==> program akan dijalankan JIKA SEMUA KONDISI BERNILAI FALSE 
'''
angka = int(input("Masukkan Angka:"))
if angka == 20:
    print("angka yang anda masukkan 20")
elif angka>20:
    print('angka yang anda masukkan lebih dari 20')
else:
    print("angka yang anda masukkan kurang dari 20")
'''

## Jika ada 2 kondisi sekaligus yang akan diuji
## Bisa menggunakan Operator And atau OR
## Atau menggunakan NESTED IF

## NESTED IF == IF di dalam IF

# Contoh
# JIKA nilai diatas atau sama dengan 85 dan perempuan, Mahasiswi Teladan
# Jika nilai diatas atau sama dengan 85 dan laki-laki, Mahasiswa Teladan
# Jika nilai dibawah 85 dan perempuan, Mahasiswi Telatan
# Jika nilai dibawah 85 dan laki-laki, Mahasiswa Telatan

nilai=int(input("Nilai : "))
gender=input("Gender M/F: ")
'''
if nilai >= 85:
    if gender == "M":
        print("Mahasiswa Teladan")
    else:
        print("Mahasiswi Teladan")
else:
    if gender == "M":
        print("Mahasiswa Telatan")
    else:
        print("Mahasiswi Telatan")
'''
## ALT 2
if nilai >= 85 and gender == "M":
    print('Mahasiswa Teladan')
elif nilai >=85 and gender == "F":
    print("Mahasiswi Teladan")
elif nilai <85 and gender == "M":
    print("Mahasiswa Telatan")
else:
    print("Mahasiswi Telatan")

TUGAS PERSONAL
1.
input:
