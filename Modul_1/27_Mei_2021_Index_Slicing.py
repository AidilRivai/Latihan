Nama="Adam White"

# print(Nama[6])

# - Indexing dihiting dari kiri (Depan), index dimulai dari NOL 
# - Indexing dihitung dari kanan (belakang), index dimulai dari -1
# A -10 === 0
# d -9 === 1
# a -8 === 2
# m -7 === 3
# spasi -6 === 4
# W -5 === 5
# h -4 === 6
# i -3 === 7
# t -2 === 8
# e -1 === 9

print(Nama[-7])
print(Nama[3])
# print(Nama[-15]) = Error

print(Nama[0:10]) #mengakses index paling awal hingga paling akhir
print(Nama[:5]) #jika angka kosong berarti akan diakses dari paling ujung === sama artinya dengan Nama[0:5]
print(Nama[5:]) #sama artinya dengan 5:10
print(Nama[:]) #sama artinya dengan [0:10]

#Reverse Char
print(Nama[::-1])

#Menghitung jumlah karakter
# Str.count("")
print(Nama.count("a"))
