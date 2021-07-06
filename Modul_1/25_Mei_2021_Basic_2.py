# Nama = 'Aidil'
# print(Nama)

# Assignment Operator: =
# Kotak dan Data 

# Kotak = Data 
# # Kiri = Kanan ==> memasukkan data disebelah kanan ke dalam variabel sebelah Kiri


# ## Single Assignment

# Angka = 58
# nama = "Aidil"
# Kota = "Jakarta"

# Sisi = 25

# LuasPersegi = Sisi * Sisi

# print(Angka)
# print(Angka * 5)
# # print(nama)
# # print(LuasPersegi)

# a= 15
# b= 60
# c= 'Kota Jakarta'
# d= 6.05
# e= True

# # # a,b,c,d,e adalah variabel
# # # 15,60, "Kota Jakarta", 6.05, True ini adalah data/value yang kita masukkan ke variabel

# # print (a)
# # print (c)
# # print(type(e))


# ## Multiple assignment
# a, b, c= 50, 100, 200

# ## Pastikan jumlah variable sama dengan jumlah data/value pisahkan data atau variable menggunakan koma

# print(c)

# print(b)

# ## Kita dapat menggantikan data/value dari variabel, data yang akan digunakan adalah data yang paling baru/ paling bawah

# b ="bekasi"
# print(b)

# ##menukar nilai
# a=50
# b=999
# print (b)
# print(a)

# a, b = b, a

# print (a)

##Assign Multiple variable with single value

# a = b = c = d = e = 750

# print(e)

# print(c)

### untuk menerima inputan dari user

# Nama = input("masukkan nama:")
# Kota = input("masukkan kota:")

# print(Nama)
# print(Kota)

# #mengakses string menggunakan metode indexing
# Indexing = urutan
# Indexing pada python dimulai dari nol 

# A = urutan 0 ( urutan = index)
# d = urutan 1
# a = 2
# m = 3
# spasi = 4 
# W = 5
# h = 6
# i = 7
# t = 8
# # e = 9
# Nama = "Adam White"
# #akses indexing menggunakan kurung siku
# [ ]
# Basic Syntax:
# NamaVariabel[Index]

# ###akses indexing
# print(Nama[5]) #akses huruf W
# print(Nama[8]) #akses huruf t
# print(Nama[0]) #akses huruf a
# print(Nama[3])

# ##untuk mengetahui index(urutan) dari karakter tertentu
# syntax:
# namavariabel.index(karakter yang dicari)

# print(Nama.index("h"))
# print(Nama.index("i"))

# ###Mengakses beberapa karakter sekaligus ===> slicing/subsetting
# Basic Syntax:
# namavariable [ start : end : step ]
# start dan end adalah angka Index 
# start => awal akses indexing
# # end => akhir akses indexing tetapi exclude
# # step = langkah mengakses index dari start hingga end
# Nama="Adam White"
# # print(Nama[0:9:3])

# # # namavar[start:end]
# # # [inclusive:exclusive]

# # # -ketika step tidak ditentukan valuenya, step akan menggunakan nilai default = 1
# # # start berlaku inclusive
# # # end berlaku exclusive

# # print(Nama[0:7])

# ##gunakan fungsi len(data)
# # untuk mengetahui jumlah data/karakter, spasi akan dihitung sebagai karakter tersendiri
# ##untuk data primitif , Len hanya untuk data string

# print(len(Nama))

# ##fungsi unutuk mengubah tipe data
# int(data) ==> mengubah data menjadi integer
# str(data) ==> mengubah data menjadi String 
# float(data) ==> Mengubah data menjadi float 

# note: data harus sesuai format

# A ='9'
# print(type(A))

# A = int(A)
# print(type(A))

# B=600
# B=str(B)
# print(type(B))

# C=8.96
# C=float(C)
# print(type(C))


##string manipulation
Nama = "adam white"
NAMA = "DEAN WINCHESTER"
usia = 26
print(Nama)
# print(Nama.capitalize()) ##mengubah huruf pertama menjadi kapital
# print(Nama.title()) ##mengubah huruf pertama setiap suku kata menjadi kapital
# print(Nama.upper()) ##mengubah semua huruf jadi kapital
# print(NAMA.lower()) ##mengubah semua karakter menjadi huruf kecil
print(len(Nama))