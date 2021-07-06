
# ## Data Structures ==> Iterables Object
# - Data Iterables
# - Berisi lebih dari 1 Value
# - List, Tuple, Set, Dictionary
# - Bisa berisi Data primitif (string-integer-Float-boolean) atau Data Structures

# #### LIST
# menggunakan simbol ==> []

# list_A = [data1, data2, data2, data3, dst]

# #### Mengubah Tipe data Structure
# str(), int(), float() ===> Ubah tipe data primitif

# list(data) ===> Mengubah data menjadi tipe LIST 

# kalimat = "Nama saya adalah Adam White dan saya tinggal di jakarta"
# print(kalimat.split(" "))
# data = kalimat.split(" ")
# print(type(data))
# ### fungsi dari .split() akan menghasilkan LIST
# '''

hari=['senin', 'selasa', 'rabu','kamis','jumat','sabtu','minggu']
print(len(hari))
# data_list=["andi", "jakarta", True, 26, 1.75, ["sepeda","motor","Mobil", ["DA", "DS"]]]
# # print(data_list)

# # Aplikasi Transaksional (HAMPIR DIPAKAI DI SEMUA)
# # CRUD - Create - Read - Update - Delete

# ##### Cara Akses DAta / Elemen dalam list
# # - menggunakan Indexing
# # - Indexing ==> Urutan Elemen ==> dimulai dari NOL 
# # - Angka index berupa integer
# # - Index Positif Maksimal => Elemen -1

# # BasicSyntax:
# #     NamaLIST[Index]
'''
print(hari[1])
print(hari[0])
print(hari[-1])

###untuk mengetahui jumlah elemen dalam list
# basicsyntax:
    # len(namavar)
print(len(hari))

###Menampilkan seluruh data dalam list
print(hari)

####Menggunakan LOOPING UNUK AKSES LIST

for i in hari: ##(Mengakses seluruh elemen dalam LIST)
    print(i)
    if i == "rabu":
        print("Looping dihentikan oleh Break")
        break

'''

# #####Extend
# - data yang akan ditambahkan ke dalam list harus berupa data iterables(String atau data structures)
# - data yang ditambahakn, per elemen dari data iterables

nama=["aa", "bb", "cc"]
nilai=[10,20,30]
#contoh
print(nama)
nama.extend("dd")
###nama.extend(78) ### akan error klo bukan str karena tidak iterable
print(f"nama setelah di extend:{nama}")

# nama.extend(nilai)
# print(nama)
# akan menghasilkan
# ['aa', 'bb', 'cc', 1, 2, 3]

# #####Append
# -data yang ditambahkan bisa berupa data iterables(string & data structures) maupun data tunggal(integer, float, boolean)
# -data iterables akan ditambahkan sebagai data tunggal bukan setiap elemennya

# contoh 1
a = ["aa","bb","cc","dd"]
b = [10,20,30,40,50,60]

print(a)
a.append(74)
print(f"list setelah tambah data dengan append: {b}")

nama.append(nilai)
print(nama)
#akan menghasilkan
['aa', 'bb', 'cc', [1, 2, 3]]
