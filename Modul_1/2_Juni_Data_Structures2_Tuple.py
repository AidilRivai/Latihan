# #Menambahkan Data di Index tertentu
# # -Secara Default ketika kita menambahkan data,
# # Data akan dimasukkan ke paling akhir(Index Terakhir)

# hari =['senin', 'selasa', 'rabu','kamis','jumat','sabtu','minggu']

# hari.append('sunday') ## secara default sunday akan ditambahkan di paling akhir (Index terakhir)
# print(hari)

# ## Insert
# # Basic Syntax:
# # NamaList.insert(index, Data)

# # contoh:
# hari.insert(1,"monday") ##Monday akan ditambahkan di index 1, data lain akan mundur indexingnya
# print(hari)

# #### Mengupdate Element Dalam List
# # Basic Syntaxnya:
# # Namalist[index] //---Index data yang akan diubah/diupdate---// = Data Baru

# # contoh:
# # kita akan mengubah rabu menjadi wednesday
# hari[3] = "wednesday"
# print(hari)

# ######Menghapus Element Dalam List

# #Menghapus berdasarkan data
# # -Remove
# # Basic Syntax:
# # Namalist.remove(Data)

# # contoh(Menghapus sunday dari data):
# hari.remove('sunday')
# print(hari)

# #Menghapus berdasarkan index
# # -pop
# # Basic Syntax:
# # Namalist.pop(index)
# # Jika nilai index tidak ditentukan, akan menggunakan index default
# # index defaultnya adalah index paling akhir

# hari.pop() ## akan menghapus data index terakhir(minggu)
# print(hari)

# #akan menghapus wednesday ==> index=3
# hari.pop(3)
# print(hari)

# ###### List Multi dimensi
# ### ada list di dalam list

## Cara akses Multi dimensi dapat digunakan juga untuk update maupun hapus data
'''
from typing import List, Tuple


data=["Rendi", ["Bandung", "Jakarta", "Bekasi"], 27000,
["motor", "sepeda", "mobil", [True, [96, 85, ["apel", "anggur"], 9.85,["Kopi",["Teh", "Susu"], "Jus"]]]]]

## akses 27000
print(data[2])

##akses bekasi
print(data[1][2])

##akses mobil
print(data[3][2])

##update mobil menjadi kereta
data[3][2] = 'kereta'
print(data[3][2])

### akses Teh
print(data[3]) ##Print datanya dulu biar lebih gampang
print(data[3][3][1][4][1][0])

# ###update Teh
# data[3][3][1][4][1][0]="Soda"
# print(data)

#### additional Function
Angka = [8,20,36,12,5,80,150,20,3,12]

#mendapatkan nilai terbesar dari list
print(max(Angka))

### Mendapatakan nilai terkecil dari list
print(min(Angka))

### Mendapatkan Jumlah Summary
print(sum(Angka))

#### Fungsi Count ===> fungsinya sama dengan count pada string
print(Angka.count(12))

### Mengurutkan angka-nilai dalam list
Angka.sort() ## mengurutkan dari nilai terkecil ke terbesar
print(Angka)

Angka.sort(reverse=True) ### Mengurutkan dari nilai terbesar ke terkecil
print(Angka)






#######################################################

#####Tuple
Mirip dengan List, tetapi datanya Immutable
Data Immutable ==> Data tidak bisa berubah

Tuple ==> Menggunakan Tanda Kurung ==> ()
Atau dengan Memisahkan data dengan Koma (,)

Inisiasi membuat Tuple atau list kosong
tuple_A = () ===> Inisiasi Tuple Kosong
List_A = [] ===> Inisiasi List
angka = 0
data = ""

############################
# Membuat Tuple
tuple_A = ()
tuple_B = tuple()
tuple_C = ("senin", "selasa", "rabu")
tuple_D = "jumat","sabtu", 85, True

print(type(tuple_D))


############# CRUD
hari = ('senin', 'selasa', 'rabu','kamis')

# Create - Menambah data ===> tidak dapat dilakukan
# hari.append("jumat") ===> tidak bisa, akan error termasuk extend
# print(hari)

# ### Update - Ubah data ===> tidak dapat dilakukan
# hari[1] = 'monday' ===> tidak bisa, akan error
# print(hari)

### Delete - Hapus data ===> tidak dapat dilakukan
# hari.pop() ===> tidak bisa, akan error termasuk remove
# print(hari)

### Hanya dapat melakukan akses/Read data - metodenya menggunakan indexing dan slicing yang teknisnya sama persis dengan LIST

print(hari[2])
print(hari[:3])
print(hari.index("senin"))
print(len(hari))

############ SET
- unordered list 
- unique
- Non-Indexing
- Sama seperti Himpunan di math 
- tidak bisa berisi data bertipe list 
- bisa berisi semua tipe data basic/primitif
- bisa berisi tuple

#### membuat data set
set_a = {data}
set_b = set() ##untuk inisiasi set kosong
set(data) ==> untuk mengubah data menjadi SET 
'''
# contohnya:

# buah_tuple=('anggur', 'apel', 'jeruk', 'pisang', 'nanas', 'semangka','anggur', 'apel', 'jeruk', 'pisang', 'nanas', 'semangka',
# 'anggur', 'apel', 'jeruk', 'pisang', 'nanas', 'semangka','anggur', 'apel', 'jeruk', 'pisang', 'nanas', 'semangka',
# 'anggur', 'apel', 'jeruk', 'pisang', 'nanas', 'semangka','anggur', 'apel', 'jeruk', 'pisang', 'nanas', 'semangka',
# 'anggur', 'apel', 'jeruk', 'pisang', 'nanas', 'semangka','anggur', 'apel', 'jeruk', 'pisang', 'nanas', 'semangka',
# 'anggur', 'apel', 'jeruk', 'pisang', 'nanas', 'semangka')

# print(buah_tuple)
# list=list(buah_tuple)

# set_buah=set(buah_tuple)
# print(set_buah)

Angka = {20,58,23,55,12,20,150,60,87,58,60}

#### Menambahkan data ke dalam SET
### Update
# Angka.update(500) ===> error
Angka.update('Geri')
print(Angka)

# fungsi Update pada SET memiliki karakter yang sama dengan EXTEND pada list
# - hanya menerima data iterables ===> string dan Data structures
# - tidak menerima data tunggal ===> boolean, integer, float
# - yg ditambahkan adalah setiap elemen dari data iterables tersebut

### Add
Angka.add("Geri")
print(Angka)

### Fungsi add pada set memiliki karakter yang sama dgn append pada list
# - data yang ditambahkan dianggap sebagai data tunggal
# - bisa menerima semua tipe data kecuali list

### Tidak bisa menggunakan Indexing

## Menghapus data (sama kyk list memakai remove)
Angka.remove('G')
print(Angka)
# Angka.remove('malam') ===> akan error karena tidak ada data

Angka.discard('malam') ##===> tidak akan keluar error meskipun datanya tidak ada
