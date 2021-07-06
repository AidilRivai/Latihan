'''
# 1. 
# Adam memelihara Ayam dan Kambing, Jumlah Ayam dan Kambing Adam ada 13 Ekor
# Jumlah kaki ayam dan kambing ada 32
# berapa jumlah masing-masing ayam dan kambing adam?
# notes: jangan gunakan angka langsung, tetapi gunakan variabel
# contoh
# Jumlah_Hewan = 13
# Jumlah_Kaki = 32

jumlah_hewan = 13
jumlah_kaki = 32
kaki_ayam = 2
kaki_kambing = 4
kambing = int((jumlah_kaki-(jumlah_hewan*kaki_ayam))/(kaki_kambing-kaki_ayam))
ayam = int(jumlah_hewan-kambing) 
print(f"1. Adam memiliki ayam {ayam} Ekor dan Kambing {kambing} Ekor")

# 2. 
# Sembilan belas tahun yang lalu,
# umur anak setengah tahun lebih muda dari seperempat umur ibunya
# umur anak sekarang sembilan belas tahun lebih tua dari sepertujuh umur ibunya
# berapa umur ibu ketika melahirkan anaknya
# output:
# Umur ibu ketika melahirkan anaknya adalah .... tahun

tahunlalu=19
lebihmuda=1/2
rasio1=4
rasio2=7
ibu=round(((lebihmuda)+(tahunlalu/rasio1))/((rasio2/(rasio1*rasio2))-(rasio1/(rasio1*rasio2))))
anak=round(19+(ibu/rasio2))
print(f"2. Usia ibu saat melahirkan anaknya adalah {ibu-anak} tahun")

# 3. 
# Jumlah umur usia budi dan ayahnya sekarang adalah 50 tahun
# empat tahun lalu, usia ayah budi enam kali usia budi.
# berapa usia ayah budi dan usia budi saat ini

jumlahusia=50
tahunlalu=4
rasioayah=6
rasiobudi=1
umurbudi=round(((jumlahusia-tahunlalu+(rasioayah*tahunlalu)))/(rasioayah+rasiobudi))
umurayah=round(jumlahusia-umurbudi)
print(f"3. Usia ayah saat ini {umurayah} tahun dan usia budi saat ini {umurbudi} tahun")


# 4.
# input :
# masukkan kalimat : ..... 
# masukkan karakter (huruf atau angka): .... 


print("4. Jawaban")
kalimat = input("Masukkan kalimat: ")
karakter = input("Masukkan karakter(huruf atau angka): ")
print("jumlah karakter", karakter,"di dalam kalimat", kalimat,"adalah",(kalimat.lower()).count(karakter.lower()))

# 5.
# Input:
# Masukkan kalimat:
# masukkan huruf vokal:

print('5. Jawaban')
kalimat= input("Masukkan kalimat: ")
vokal= input("Masukkan Huruf Vokal: ")
kalimat1= kalimat.replace("a",vokal.lower())
kalimat1= kalimat1.replace("i",vokal.lower())
kalimat1= kalimat1.replace("u",vokal.lower())
kalimat1= kalimat1.replace("e",vokal.lower())
kalimat1= kalimat1.replace("o",vokal.lower())
kalimat1= kalimat1.replace("A",vokal.upper())
kalimat1= kalimat1.replace("I",vokal.upper())
kalimat1= kalimat1.replace("U",vokal.upper())
kalimat1= kalimat1.replace("E",vokal.upper())
kalimat1= kalimat1.replace("O",vokal.upper())
print(kalimat1)
'''
# 6.
# Jarak Mobil A dan B adalah 120 KM
# A berjalan 60km/jam dari timur 
# B berjalan 40km/jam dari barat
# A dan B start pukul 9
# Jam berapa A dan B bertemu/bertabrakan

Pukul= 9
Mobil_A = 60
Mobil_B = 40
Jarak = 120
Jam_untuk_bertemu = (Jarak/(Mobil_A+Mobil_B))
Jam = round(Jam_untuk_bertemu)
Menit = round(Jam_untuk_bertemu-Jam,1)
Menit60= round(Menit*60)

print("6. mereka akan bertemu pada jam", (Pukul+Jam), "lewat", (Menit60), 'menit' )