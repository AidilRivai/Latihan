# numpy => numerical phyton
# digunakan untuk erhitungan saintifik basic

# ==> bertipe data array
# -vector
# -matric
# - N-dimension Array 

# [1, 5, 6, 8, 20] ==> vector

# [[2,8,7],[80,63,20]] ==> Matrix

# [7] ==> Scalar

import numpy as np
from numpy.random.mtrand import randint
# ### Membuat Array
# a = [5,6,7,8,9,10] ##==> List basic

# # ### membuat array dary list basic
# n = np.array(a)

# # print(a)
# # print(n)
# # print(type(a))
# # print(type(n))

# ### operasi math basic
# # c = a + 5 ###akan error karena list tidak bisa ditambahkan dengan int
# # c = a +[5] ### akan menambahkan elemen 5 kedalam list

# # print(c)

# # d = n + 5
# # print(d)



# e = a*3 ## List
# f = n*3 ## Numpy Array
# # h = a ** 2 ## akan error
# g = n ** 2

# print(e)
# print(f)
# print(g)

# #Elementwise ==> operational math akan dieksekusi/dikalkulasi ke setiap elemen dalam array

# range(10) ##range built in python
# np.arange(10) ##arange() ==> fungsi range dari numpy

# # for i in range(1,10,2):
# #     print(i)

# # for j in np.arange(1.5,10.5,0.5):
# #     print(j)

# for i in np.arange(7.5):
#     print(i)

# ###membuat array dengan linear Space
# c= np.linspace(0,100,5)
# print(c)

# d= np.linspace(10.7,200,6)
# print(d)

# e= np.linspace(20,200.8,7)
# print(e)

### numpy.linspace(start,end,jumlahtitik)
## start-end tidak menganut inclusive - exclusive
## start-end keduanya bersifat inclusive
## start ==> bisa integer maupun float
## end ==> bisa integer maupun float
## jumlahtitik ==> harus integer

# ### membuat array dengan logaritmik scpace
# d= np.logspace(3,0,4)
# print(d)
# ## np.logspace(start,end,jumlah)
# ## start end bersifat inclusive
# ## start - end menunjukan nilai pangkat dari 10
# ## Jumlah harus integer
# e=np.logspace(-3,0,4)
# print(e)

# ### Membuat array dengan angka random
# a = np.random.rand(10)
# print(a)
# ## setiap di run, akan menghasilkan angka yang berbeda
# ## .rand(jumlah) ==> Jumlah angka yang ingin dibuat
# ## membuat angka random yang range nya antara 0-1

# b= np.random.randn(15)
# print(b)

# ## membuat angka random yang terdistribusi normal - membentuk bell shape

# # range angka antara -3 s/d 3
# # tetapi kebanyakan di -1 0 1

# ## membuat array dengan random nilai integer
# c = np.random.randint(100)
# print(c)

# # .randint(nilaipalingrendah, nilai tertinggi,jumlah)
# ## jika hanya 1 angka berarti itu adalah nilai batas atas (high)
# ## jika ada 2 angka berati itu adalah batas bawah (low) dan batas atas (high)


# d= np.random.randint(50,60)
# print(d)
# e= np.random.randint(50,100,15)
# print(e)

# def perkalian (baris, kolom):
#     return baris*kolom

# f = np.fromfunction(perkalian, (3,4), dtype=int)
# print(f)
# # np.fromfunction(function, (ukuran/bentuk), tipe data)
# #ukuran/bentuk ==> (baris, kolom)

# def jumlah (baris, kolom):
#     return baris+kolom
# g= np.fromfunction(jumlah, (4,3), dtype=int)
# print(g)

### Array multi dimensi - matrix

a= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

mat= np.array(a)
print(mat)

b = [5,8,11.5,9,25]
vect = np.array(b)
print(vect)

print(type(mat))
print(mat.ndim) ##untuk melihat dimensi array => 2 dimensi

print(vect.ndim) ## 1 dimensi
print(mat.size) ## untuk melihat ukuran/jumlah data dari array => 9
print(vect.size) # 5
print(mat.dtype)
print(vect.dtype)

matf = mat.astype("float64")
print(matf)
print(matf.dtype)
vectI=vect.astype("int32")
print(vectI)
print(vectI.dtype)

### Membuat matrix - array yang semua elemennya NOL
z1 = np.zeros(5) #Vector NOL yang jumlah elemennya 5
z2 = np.zeros((4,3)) # Membuat matrix nol (baris, kolom)
print(z1)
print(z2)

### membuat matrix - array yang semua elemennya 1
y1 = np.ones(7)
y2 = np.ones((3,3))
print(y1)
print(y2)

### Matrix identitas
m = np.eye(5)
n = np.identity(6)
print(m)
print(n)