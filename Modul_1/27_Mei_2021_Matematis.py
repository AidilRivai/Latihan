# ### input() ===> menerima inputan dari user
# Nama = input('Masukkan Nama :')
# # Usia = input('Masukkan Usia :')
# print(Nama)
# print(type(Nama))
# # print(Usia)
# # print(type(Usia))

# ### semua inputan dari user python/program akan membaca sebagai tipe data STRING

# # ### opsi mengubah tipe data usia menjadi integer
# # # cara pertama
# # Usia = int(input("Masukkan Usia :"))
# # print(Usia)
# # print(type(Usia))

# ## cara kedua
# Usia = input("Masukkan Usia : ")
# Usia = int(Usia)
# print(Usia)
# print(type(Usia))

# ### Memasukkan isi dari variabel ke dalam suatu sentences/kalimat/statement
# Contoh Expected Output
# "Nama Saya adalah Thomas Andre dan berusia 25 Tahun"
# Thomas andre dan 25 didapat dari variabel

Nama = "Thomas Andre"
Usia = 25

############ Alternatif 1

# print("Nama saya adalah", Nama)
# print("Nama saya adalah", Nama, "dan berusia", Usia, "Tahun")

#############Alt 2 (Ketika akan menggunakan tanda +, semua variable harus bertipe data STRING)
# print("Nama saya adalah " + Nama)
# print("Nama saya adalah " + Nama + " dan berusia " + str(Usia) + " Tahun")

# # print(Nama + Nama) ##Concat ==> Menggabungkan beberapa STRING
# # print(Nama*5) ## Akan menampilkan STRING(Nama), sebanyak Value Integer(5)
# # print(nama/2) ##error
# # print(nama-2) ##error
# # print(Nama + 5) ##error
# # print(Nama * Nama) ##error
# # print(Nama * 2.5) ##error

# # Kita dapat menggunakan operator matematik pada String, tapi terbatas
# # tanda + hanya dapat digunakan untuk data STRING dan STRING
# # tanda * hanya dapat digunakan untuk data String dan Integer

################ Alternatif 3
# print("Nama saya adalah {} dan berusia {} Tahun".format(Nama, Usia))

# print("Nama saya adalah {} dan berusia {} Tahun".format(Usia, Nama))

# print("Nama saya adalah {1} dan berusia {0} Tahun".format(Usia, Nama))

######## Alternatif 4

# print(f"Nama saya adalah {Nama} dan berusia {Usia} Tahun")

##################### Operator matematis untuk data numerik (float dan integer)
# print(5+4)
# print(8*8)
# print(2**3) ##pangkat => 2 pangkat 3
# print(10-0.25)
'''
print(10/2)
print(10/3)
print(10//2)
print(21/7) #semua hasil pembagian menggunakan /, hasilnya akan menjadi float
print(15//2) ##semua hasil pembagian menggunakan //, hasilnya akan menjadi integer (mengabaikan nilai desimal, nilai belakang koma akan dihilangkan)

print("="*50)
##Modulus (sisa dari pembagian) ex: 10 dibagi 7 sisa 3
print(10%2)
print(10%3)
print(10%7)

print("="*50)
#### Fungsi Pembulatan
#Basic syntax:
#round(angka, jumlah desimal)
'''
# # print(round(3.347235434523563, 2)) ##dibulatkan 2 angka dibelakang koma
# # print(round(6.8495723421425, 3)) ##dibulatkan 3 angka dibelakang koma

# # print(round(7.849348594)) ##jika jumlah angka desimal tidak ditentukan, maka angka desimal NOL(tidak ada angka desimal)/menjadi angka bulat

# # print(round(2.5)) #angka didepan koma genap, angka akan dibulatkan kebawah
# # print(round(3.5)) #angka didepan koma ganjil, angka akan dibulatkan keatas

# ###### Jika pembulatan hingga ke angka (bilangan bulat)
# #####kalau angka dibelakang koma adalah 5(harus 5 saja tidak boleh ada angka lain dibelakangnya)
# # dan pembulatan menjadi angka bulat, kalau genap pembulatan kebawah, kalau ganjil pembulatan keatas

# # Library -- Package -- Module 
# # - Suatu program yang sudah dibut oleh anggota komunitas/user, baik individu maupun grup, yg bisa digunakan oleh user lain
# # - Ada beberapa package yang sudah terinstall dalam python secara default (Built in Package)
# # - untuk beberapa library/package yang belum ada, ketika ingin menggunakannya, kita harus melakukan instalasi terlebih dahulu

# # Cara menggunakan Library - package

# # Alt 1
# import math
# # math adalah salah satu library-package yang sudah terinstall secara default
# # built in package
# print(math.pi) ## ini nilai dari pi, 22/7
# print(math.pow(2, 3)) ## menampilkan pangkat, 2 pangkat 3
# print(math.floor(2.87)) ## melakukan pembulatan ke bawah, BERAPAPUN nilai desimalnya
# print(math.ceil(5.01)) ## Pembulatan ke atas, berapapun nilai desimalnya
# print(math.sqrt(64)) ## akar kuadrat

# ####cara melihat fungsi2nya
# ###print(math.)

# # pi, pow, flow, floor, ceil, sqrt adalah fungsi yang terdapat di package math 
# # cara menggunakan fungsi dari package 
# # namaPackage.namafungsi() 
# ### menggunakan kurung jika ada parameter

# ################ alt 2 (sering dipakai)
# import math as m ## menggunakan nama alias untuk package
# import math as m
# print(m.pi)
# print(m.pow(5, 3))
# print(m.floor(7.9))
# print(m.ceil(8.001))
# print(m.sqrt(25))

####################alt 3 (Sering dipakai)
# # kita akan langsung import fungsi dari package yang akan digunakan
# from math import pi, pow, floor, ceil, sqrt

# print(pi)
# print(pow(4, 7))
# print(floor(8.98))
# print(ceil(4.12))
# print(sqrt(16))

kalimat = "Nama saya adalah Adam White dan saya tinggal di Jakarta"
print(kalimat)
print(kalimat.replace("Adam", "Mike")) ##mengganti suatu karakter STRING dengan STRING baru
print(kalimat.split("dan")) 
print(kalimat.split(" ")) #kalimat akan dipisahkan berdasarkan karakter yang ada dalam parameter ()
# .split(parameter)
print(kalimat.split(" ",1))
print(kalimat.split(" ",2))
print(kalimat.count("A"))
print(kalimat.count("a"))