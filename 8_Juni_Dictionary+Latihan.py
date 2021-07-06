# nilai = {
#     "Andi":85,
#     "Beni":96,
#     "Dodi":75,
#     "Riko":80,
#     "Andre":90,
#     78:["Rio","Rendi"]
# }

# print(nilai["Andi"])
# print(nilai["Andre"])

# # #### perbedaan akses list dan dictionary
# # pada LIST kita akses data/elemen menggunakan indexing ===> urutan berupa numerik integer
# # pada dict kita akses data/elemen/items menggunakan key ===> umumnya berupa string atau integer
# # ketika akses dictionary menggunakan interger, ini bukan index tetapi key (jika ada keywords menggunakan integer)

# print(nilai[78])

# ###untuk melihat seluruh keys pada dict
# print(nilai.keys()) ### menampilkan seluruh keys pada dict, berupa object dict_keys

# print(list(nilai.keys())) ### menampilkan seluruh keys, kemudian mengubahnya menjadi list

# ########### Packing - Unpacking
# # - Sebenarnya serupa/mengadopsi konsep multiple assignment

# ### Packing
# # - Proses memasukkan beberapa data ke dalam SATU variabel

# user = "Rosi", 25, "Bandung"
# user1 = ("Roni",24,"JAkarta")

# print(type(user))

# #### Unpacking
# # - Proses men-assign beberapa data tadi (Packing) ke dalam beberapa variabel Baru

# # nama, usia, kota = user
# # print(nama)
# # # Jumlah Variabel baru harus sama dengan jumplah elemen dalam tuple/list
# # print(len(user)) ###untuk mengetahui jumlah elemen dalam tuple/list

# # ### Multiple Assignment
# # nama, usia, kota = "Rosi", 25, "Bandung" ### Jumlah Variabel harus sama dengan jumlah values

# # nama, _, Kota = user1 ##Gunakan underscore untuk mengabaikan Values tertentu

# # def genap(x):
# #     if x%2 == 0:
# #         return "Genap", x**2, "Selamat Siang"
# #     else:
# #         return "Ganjil", x**3, "Selamat Malam"

# # hasil = genap(25)
# # print(hasil)
# # gangen, kuadrat, greet = genap(22)
# # print(gangen)
# # print(kuadrat)
# # print(greet)

# ### Menampilkan Items dari Dict
# print(nilai.items())

# for i, j in nilai.items():
#     print(i) ### Merupakan Keys
#     print(j) ### Merupakan Values
#     # print("Ganti Iterasi")
#     print((j,i)) ### Mengubah items menjadi tuple, dan dibalik antara keys dan values
#     print([j,i])

# ### Mengubah nilai Andre menjadi 100
# print(f"Nilai Andre sebelumnya {nilai['Andre']}")
# nilai["Andre"] = 100
# print(nilai["Andre"])

### Latihan
# Buat Automatic Translator Hari
# Silahkan Buat 1 Dictionary untuk inisiasi
'''
Hari = {
    "senin":"monday",
    "selasa":"tuesday",
    "rabu":"wednesday",
    "kamis":"thursday",
    "jumat":"friday",
    "sabtu":"saturday",
    "minggu":"sunday"
}

hari1=input("Masukkan Nama Hari: ")
hari2=(hari1.lower())
# def translate(x):
#     if hari2 in Hari.keys():
#         return Hari.values()
#     elif hari2 in Hari.values():
#         return Hari.keys()
#     elif hari2 != Hari.values() or hari2 != Hari.keys():
#         return "Hari tidak ada"
#     else:
#         return "tidak menerima integer/float"

def translate(x):
    if hari2.isalpha():
        if hari2 in Hari.keys() or hari2 in Hari.values():
            for y, z in Hari.items():
                if y == hari2:
                    return(f'hari yang anda pilih adalah {hari1} dalam bahasa ingris adalah {z}')
                elif z == hari2:
                    return(f'the day you choose is {hari1} in indonesian is {y}')
        else:
            return "Hari tidak ditemukan"
    else:
        return "tidak menerima integer"

print(translate(hari2))
'''
#### Dictionary Multi Layer
member = {
    "name":"Jack",
    "email": "Jack@beast.com",
    "username":"Jack_666",
    "Pass":"Jack123",
    "age":23,
    "is_married":False,
    "height": 1.75,
    "Weight": 65.75,
    "job":"Data Analyst",
    "cars": ["Jazz","Xpander","Innova"],
    "address":{
        "street":"East Blue",
        "no":50,
        "city":["East Jakarta", "West Jakarta", "South Jakarta"],
        "zipcode": 56823,
        "geo": {
            "lat": 90.23,
            "lng": [20,57,[35,80], 76.50]
        }
    }
}

## Akses name
print(member['name'])

## Akses age
print(member['age'])

## Akses Xpander
print(member['cars']) ##akses cars

print(member['cars'][1])

## Akses East blue
# print(member['address']) ### Akses Dict Address

print(member['address']['street']) ## Akses Key - Street di dalam dict address

print(member['address']['no'])

print(member['address']['city'][1]) ## Akses West Jakarta

print(member['address']['geo']['lng'][2][0]) ### akses 35