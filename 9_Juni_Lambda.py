# #### Lambda
# # - Lambda dapat digunakan dengan cara meng-assign fungsinya ke dalam variabel
# # - menggunakannya di dalam def function atau function lain

# # ### Basic Syntax:
# # lambda argumen : expression

# # -jumlah argumen tidak dipatasi
# # - expression => program/fungsi hanya dapat memiliki 1 fungsi saja

# ### contoh def function

# def kuadrat(x):
#     return x**2
# def kali(x,y):
#     return x*y

# ### lambda function
# lambda x: x**2 ### 1 argumen => x, fungsi/program.expression ==> x**2

# lambda kilo: kilo * 60000 ### 1 argumen ==> kilo

# lambda x, y: x*y

# lambda kilo, harga, diskon: (kilo*harga)-diskon

# ###Format Def Function

# def penjumlahan(x,y):
#     hasil = x+y
#     return hasil

# def kali(x,y):
#     hasil= x*y
#     return hasil

# def kuadrat(x):
#     hasil = x**2
#     return hasil

# def triple(x,y,z):
#     hasil = x*y*z
#     return hasil

# print(penjumlahan(15,25))
# print(kuadrat(10))
# print(kali(7,15))
# print(triple(5,7,10))

# Lambda Function - version
# menggunakan lambda dengan meng-assign ke variabel
'''
jumlah = lambda x,y: x+y

print(jumlah(15,25))

power = lambda angka: angka**2
print(power(2))

# Menggunakan lambda dengan def function 

def myfunc(x):
    return lambda y: y**x 

#myFunc(5) # 5 adalah argumen dari myfunc ==> x = 5

pangkat5=myfunc(5)
# pangkat5 ==> lambda y: y**5

print(pangkat5(7))
pangkat5(7) ##==> 7 merupakan nilai dari y
# pangkat5(7) ==> lambda y: y**5 ==> lambda 7: 7**5
pangkat7=myfunc(7) ## parameter x=7
pangkat7(9) ### y=9, ==> lambda y: y ** 7 ==> 9**7

# cek nilai ganjil genap

## fungsi konvensional
angka = 80

if angka%2 == 0:
    print('angka genap')
else:
    print('angka ganjil')

### DEF Function
#DEF Function Konvensiona
def gage(x):
    if x%2 == 0:
        print("Angka Genap")
    else:
        print("Angka Ganjil")
gage(85)

def gager(x):
    if x%2 == 0:
        return "Angka genap"
    else:
        return "Angka ganjil"

print(gager(91))
print('='*50)

### Lambda Function
cekgg = lambda x: True if x%2==0 else False
print(cekgg(25))
print(cekgg(64))

cekgangen = lambda x: 'ANGKA GENAP' if x%2 == 0 else "ANGKA GANJIL"

print(cekgangen(250))
print(cekgangen(261))
'''
####################################################
# Pangkat3= lambda x: x**3
# A=[5,8,15,10]

# hasil=[]
# for x in A:
#     hasil.append(Pangkat3(x))

# print(hasil)

########################### Map Function
# - Function yang memiliki karakter serupa dengan Lambda function
# - tapi digunakan untuk data iterables - data structures

A=[5,8,15,10]

def kuadrat1(x):
    return x ** 2

kuadrat2 = lambda a: a**2
#print(kuadrat1(A)) #akan error
#print(kuadrat2(A)) #akan error

##### Map Function:
# Basic Syntax:

# map(Function, Argumen)

# Function:
# - Bisa menggunakan lambda atau def function
# - Fungsi yang akan digunakan untuk Argumen/parameter

# argumen:
# - berbentuk data iterables 
# - jumlah argumen, harus sama dengan jumlah argumen yang digunakan pada function
# - sama seperti lambda, function/expression hanya SATU
# - hasil dari operasi map, berupa object-map, sehingga perlu di konversi agar dapat dibaca

hasil1 = list(map(kuadrat2, A)) ### Map function menggunakan lambda
print(hasil1)

hasil2 = list(map(kuadrat1, A)) ### Map function menggunakan DEF

### Hasil map berupa object-map, sehingga perlu di konversi
print(hasil2)

### Kuadrat1 dan kuadrat2 merupakan function yang digunakan di dalam map
### A adalah argumen ===> data iterables

### map dengan argumen 2 atau lebih

def perkalian(a,b):
    return a*b
kali = lambda x,y:x*y

B = [25, 15, 60, 12, 75]
C = [10, 25, 70]
D = [20,60,15,10,8]

print(perkalian(10,15))

hasil3 = list(map(perkalian, B, C))
print(hasil3)

# - perkalian => adalah function yang digunakan dalam map
# - B&C adalah argumen yang digunakan dalam Map, ada 2 argumen yang digunakan
# - karena ada 2 parameter yang digunakan di dalam function perkalian 
# - dua-duanya harus tipe data iterables
# - Jika jumlah elemen dari kedua data iterables/argumen berbeda, hasil akan mengikuti jumlah elemen terkecil

result = list(map(kuadrat2, B[1:3]))
print(result)