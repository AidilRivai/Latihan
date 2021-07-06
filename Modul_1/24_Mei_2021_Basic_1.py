## Phyton

# High End Programming Language
# Interpreter Lang. ==> program akan mengeksekusi setiap baris kode/perintah
# dari atas ke bawah
# Compiler ==> Java, C, C++, C#
# Case Sensitive ==> A dan a itu berbeda
# Nama - nama - NAMA - namA ==> 4 data yang berbeda
# - tidak membutuhkan semicolon(;)
# Tabulasi - Indentasi - Menjorok ke dalam : memiliki fungsi sebagai penanda suatu blok kode
# untuk menampilkan / mengeluarkan hasil code ke layar/screen
# gunakan perintah

# print("Hello World")
# print(5+3+10)
# print(1/2)


# # Comment
# - Comment: baris yang tidak akan dieksekusi oleh phyton, tambahkan tanda pagar di depan kalimat (#)

# untuk eksekusi code
# - button run code => tombol warna hijau pojok kanan atas
# via terminal => pastikan path terminal sudah tertuju/ sudah berada di directory file yang akan dirun
# jangan lupa di save

# tipe data di python
## tipe data primitif
# - tipe data dasar :

# - String: Alfanumerik termasuk karakter khusus (!@#$%^&"")
# - Integer: Bilangan Bulat
# - Float: Bilangan Desimal
# # - Complex Number: Jarang digunakan di data science - Bilangan Imajiner
# # - Boolean: True dan False 

# ### String
# # - Ditandai dengan tanda kutip ==> diapit oleh tanda kutip

# # print('halo')
# # print("selamat")
# # print('''malam''')

# # print('selamat malam, hari ini hari jum'at') ==> akan error
# # error karena ada penggunaan kutip di dalam kutip

# #alt 1
# print('selamat malam, hari ini hari jum"at')

# #alt 2
# print("selamat malam, hari ini hari jum'at")

# #alt 3
# print('selamat malam, hari ini hari jum\'at') ### gunakan backslash sebagai penanda escape character

# #alt 4
# print('''selamat malam, hari ini hari jum'at''')

# ##print multi line string
# # print("selamat malam, 
# # hari ini hari jum'at")

# ##untuk print multiline string gunakan 3 tanda kutip
# print("""selamat malam
# hari ini hari jumat""")

# #alt 2 pakai 3 kutip '''


# #tipe data numerik: integer - float
#beda string dan numerik
#numerik bisa menggunakan seluruh operasi matematis

### integer
# print(9)

# print ('9')

# print (5 + 5)

# print ('5' + '5')

# print(9/3)

# print ('A' + 'B')

# print('-8')
# print(type('-8'))

# print(-8)
# print(type(-8))
# #untuk mengetahui jenis dari tipedata
# # type(dataygdicek)

### Float
# #bilangan Desimal

# print(8.6)
# print(type(8.6))


###Boolean
# print(True)

# print(False)

# print(type(True))

### Variabel
# - suatu tempat untuk menyimpan data dan kita beri nama
# - Case Sensitive : variable kopi berbeda dengan variable KOPI 
# - tidak bisa diawali dengan number: 23nama => error
# - tidak bisa menggunakan karakter spesial (@!$%dll)
# - tidak bisa ada Spasi
# - tidak bisa menggunakan reserved words (kata kunci yang sudah digunakan oleh phyton, contohnya print, type)
# - tidak perlu mendefinisikan/mendeklarasikan tipe data untuk variabel
# - pemberian nama bebas, dan bisa menggunakan kombinasi huruf kapital (A-Z), huruf kecil (a-z), angka (0-9) dan underscore
# Nama_Siswa25
# - pemberian nama variable bebas, selama mengikuti aturan yang berlaku

# import keyword

# print(keyword.kwlist)

##Contoh penggunaan variabel
Nama = 'Joni'

print(Nama)
