A = [25,20,5,15,75]
B = [30,5,80,62,85]
C = [5,10,60,15,30]

triplet = lambda x,y,z: x*y*z 
hasil = list(map(triplet, A, B,C)) ## Lambda Function dengan Variabel
print(hasil)

hasil = list(map(lambda x,y,z: x*y*z,A,B,C)) ### Langsung menggunakan lambda Function di Map
print(hasil)

Hasil = list(map(lambda x,y: x*y, A,B))
print(Hasil)

########### Notes:
# - Pada penggunaan map - seringnya, format function berupa lambda function secara langsung
# - tujuannya agar lebih mudah mengetahui jumlah argumen yang harus digunakan
# - karena jumlah argumen/data iterables pada map function harus sama dengan jumlah argumen pada function (lambda/def)

# ###### Filter Function
# Basic Syntax:
# filter(function, argumen)

# - function yang digunakan berupa comparison function ==> yang menghasilkan True atau False
# - untuk melakukan pengecekan kondisi 
# - function ==> comparison function
# - argumen - data iterables
# - function hanya bisa 1
# - data iterables/argumen ==> hanya bisa 1
# - akan mengeluarkan yang hasilnya True
# - menghasilkan object sehingga perlu dikonversi

# A= [2,15,25,20,18,75,40,41,35,80,120,170,190]

# hasil= list(filter(lambda x: x%2 == 0, A))
# hasil2= list(filter(lambda x: x>100, A))

# print(hasil)
# print(hasil2)

# ### Reduce
from functools import reduce
# C=[1,2,3,4,5]


# Basic Syntax:
# reduce(function, argumen)
# - Argumen => Data iterables
# - Menghasilkan 1 Value 

# hasil3 = reduce(lambda a,b: a+b, C)
# print(hasil3)

1+2
(1+2)+3
(1+2+3)+4
(1+2+3+4)+5 ###===> hasil ini yang akan dikeluarkan oleh fungsi reduce

# Latihan
# - Gunakan Lambda, Map, Filter atau reduce 
# - TIdak menggunakan DEF Function atau fungsi konvensional lain
# - Dibuat dalam 1 baris code

# Berapa total bilangan genap yang telah dipangkatkan 3 antara 1-200 (1 dan 200 included)

# number = list(range(1,201))
# # pangkat=
# print(number)

# hasil=reduce(lambda a,b: a+b,(list(map(lambda x:x**3,(list(filter(lambda x: x%2 ==0, number)))))))
# print(hasil)