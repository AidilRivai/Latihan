### Personal Assignment
'''
Deadline nya 22 Juni 2021

1. Morse Konverter
Auto Decoder - Encoder Morse 

Buat 1 Dictionary untuk Inisiasi.

Input : 
Masukkan Kata : .... 

Output :
- Jika yg dimasukkan adalah Kata-kata 
Kata yg anda masukkan adalah ... kata-kalimat ... Jika diubah menjadi Kode morse menjadi ..... -Kode morse- 

- Jika yg dimasukkan adalah kode morse 
Kode morse yg anda masukkan adalah ..... jika diubah menjadi kata/kalimat menjadi ... 

Ketentuan :
- Hanya menerima alfabet, angka dan spasi (Untuk kalimat)
- Untuk pemisah kode morse Bebas 
- Jangan Lupa untuk Error Handling
- Kalimat/kata tidak bisa dicampur dg Kode morse 

Contoh :
Masukkan Kata : 
Hello 

Output :
....| . |.-.. |.-.. |---

Kata yang anda masukkan adalah (Hello) Jika diubah menjadi Morse Menjadi ....| . |.-.. |.-.. |---


Masukkan Kata :
....| . |.-.. |.-.. |---

Output :
Kode morse yg anda masukkan adalah ....| . |.-.. |.-.. |--- jika diubah menjadi kata/kalimat menjadi Hello 

2. Kalkulator 
Gunakan Return Function 

Input :
Masukkan Angka 1:
Masukkan Angka 2:
Masukkan Operator : .... Operator hanya terbatas pada (+ - * /)

Output :
Hasil dari Angka1 operator Angka 2 adalah ... 

Contoh :
Masukkan Angka 1 : 15
Masukkan Angka 2 : 2
Masukkan Operator : *

Hasil dari 15 * 2 = 30

Ketentuan :
- Error Handling 

3. Caesar Cipher
Input Kata : .... (Hanya menerima Kata - Alfabet)
Masukkan Angka : .... (Menerima Integer dari minus hingga positif tidak dibatasi)

Output :
Hasil Caesar Cipher 

Contoh :
Masukkan Kata : Joni 
Masukkan Angka : 2

Hasil Caesar Cipher : lqpk

Kata : Joni 
Angka : -2

Hasil Caesar Cipher :
imlg

4. Hitung Hari 
Input : 
Masukkan nama Hari :
Masukkan Angka : 

Output :
Angka Hari dari hari -nama hari- adalah .... 

Contoh :
Masukkan Nama hari : Sabtu 
Masukkan Angka : -3

-3 Hari dari hari sabtu adalah Rabu 

Masukkan Nama hari : Minggu 
Masukkan Angka : 4

4 Hari dari hari minggu adalah Kamis 

Ketentuan :
- Error handling 
- Angka hanya Integer dan tidak terbatas Positif maupun negatif 

5. Konversi Angka Romawi  ==> Deadline Minggu 27 Juni 2021

Gunakan Function Def/lambda dan dictionary 

Maksimal : 4000
Minimal : 0

Lvl 1 :
input :
Silakan masukkan Angka :

Output :
Angka Romawi dari ..angka.. adalah ...Angka romawi...


Lvl 2 : -Optional-
Silakan masukkan Romawi : 

Output :
Angka Arab dari ..angka romawi.. adalah ...angka arab... 
'''

# kata=input("Masukkan Kata/Kode Morse: ")
# kata2=kata.upper()
# spec="""!"#$%&'()*+,/:;<=>?[\]^_`{|}~"""
# MORSE_DICT= { 'A':'.-', 'B':'-...',
#             'C':'-.-.', 'D':'-..', 'E':'.',
#             'F':'..-.', 'G':'--.', 'H':'....',
#             'I':'..', 'J':'.---', 'K':'-.-',
#             'L':'.-..', 'M':'--', 'N':'-.',
#             'O':'---', 'P':'.--.', 'Q':'--.-',
#             'R':'.-.', 'S':'...', 'T':'-',
#             'U':'..-', 'V':'...-', 'W':'.--',
#             'X':'-..-', 'Y':'-.--', 'Z':'--..',
#             '1':'.----', '2':'..---', '3':'...--',
#             '4':'....-', '5':'.....', '6':'-....',
#             '7':'--...', '8':'---..', '9':'----.',
#             '0':'-----'}

# def morse(kalimat):
#     terjemah=''
#     cekkalimat = True    
#     for alfabet in kalimat:
#         if alfabet in spec:
#             cekkalimat = False
#             terjemah += 'Hanya menerima alfabet/angka/-/.'
#             break            
#     for alfabet in kalimat:
#         if alfabet != ' ' and cekkalimat==True:
#             terjemah += MORSE_DICT[alfabet] + '|'
#         else:
#             terjemah += ' '
#     return terjemah
    
# ###print(kata2)
# print(morse(kata2))

##################################### 2.

# operator = "+-*/"
# Angka1 = (input("masukkan angka pertama: "))
# Angka2 = (input("masukkan angka kedua: "))
# operator2= input("masukkan operator: ")

# def jumlah(x,y):
#     return x+y
# def kurang(x,y):
#     return x-y
# def kali(x,y):
#     return x*y
# def bagi(x,y):
#     return x/y
# def cekfloat(x):
#     try:
#         float(x)
#         return True
#     except ValueError:
#         return False
# if cekfloat(Angka1)==True and cekfloat(Angka2)==True:    
#     angka1=float(Angka1)
#     angka2=float(Angka2)
#     if operator2 in operator:
#         if operator2 == "+":
#             print(angka1, operator2, angka2, '=', jumlah(angka1,angka2))
#         elif operator2 == "-":
#             print(angka1, operator2, angka2, '=', kurang(angka1,angka2))
#         elif operator2 == "*":
#             print(angka1,operator2,angka2,'=',kali(angka1,angka2))
#         else:
#             print(angka1,operator2,angka2,'=',bagi(angka1/angka2))
#     else:
#         print("operator matematika yang anda masukkan salah")
# else:
#     print('angka yang anda masukkan salah')

############################### 4.

dict_day={'senin':0, 'selasa':1, 'rabu':2,
     'kamis':3, 'jumat':4, 'sabtu':5, 'minggu':6}
def cekhari(x):
    list_hari = list(dict_day.keys())
    if x in list_hari:
        return True
    else:
        return False
def cekangka(y):
    try:
        int(y)
        return True
    except ValueError:
        return False

def hari(day, num):
    list_day = list(dict_day.keys())
    if cekhari(day) == True and cekangka(num) == True:
        num1=int(num)
        modulus = num1%len(list_day)
        num_sum = list_day.index(day) + modulus
        if num_sum > len(list_day):
            return list_day[num_sum - len(list_day)]
        else:
            return list_day[list_day.index(day) + modulus]
    else:
        return 'hari yang anda masukkan salah'

inputhari=input('Masukkan hari: ')
inputhari2=inputhari.lower()
inputangka=input('masukkan angka: ')

print(hari(inputhari2, inputangka))

############################### 5.
# angka=input('Masukkan Angka: ')
# Roman={1:'I', 4:"IV", 5:"V", 9:"IX",
#     10:'X', 40:'XL', 50:"X", 90:"XC",
#     100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
# def cekangka(x):
#     try:
#         int(x)
#         return True
#     except ValueError:
#         return False

# def Romawi(a):
#     if cekangka(angka) == True:
#         a=int(angka)
#         angka2 = list(Roman.keys())
#         symbol = list(Roman.values())
#         i = 12
#         hasil = (f'angka romawi dari {angka} adalah ')
#         if a>=0 and a<=4000:
#             while a:
#                 bagi = a // angka2[i]
#                 a %= angka2[i]
#                 while bagi:
#                     hasil += symbol[i]
#                     bagi -= 1
#                 i -= 1
#         else:
#             hasil = "angka yang anda masukkan terlalu besar/kecil"
#     else:
#         hasil = "angka yang anda masukkan salah"
#     return hasil
# # print("angka romawi dari", angka, "adalah", end=' ', (Romawi(angka)))
# print(Romawi(angka))
