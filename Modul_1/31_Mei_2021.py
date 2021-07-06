'''

kalimat = "makanan"
for i in kalimat:
    #print(i.upper())
    print(i.lower())


kalimat = input("Masukkan kalimat: ")
ch = input("Masukkan Vokal:")
for karakter in kalimat:
    if karakter in 'aiueo':
        kalimat = kalimat.replace(karakter,ch.lower())
    elif karakter in 'AIUEO':
        kalimat = kalimat.replace(karakter. ch.upper())
'''

### Syntax Tambahan untuk Looping

### BREAK
# - untuk menghentikan proses looping secara paksa
# - secara normal/natural ==> looping akan berhenti, ketika kondisi false 
# - Break biasanya dipasangkan dengan IF statement
'''
angka =1 
while angka < 10:
    print(f"Angka anda: {angka}")
    if angka == 7:
        break ### semua program/perintah dibawah break(yang termasuk dalam looping) tidak akan dieksekusi
    ##looping dihentikan secara paksa dan langsung mengeksekusi program/perintah diluar looping
    print("Program di luar Looping")
    angka+=1
print ("===========Program diluar LOOPING============")

print("="*50)

angka =1 
while angka < 10:
    if angka == 7:
        break ### semua program/perintah dibawah break(yang termasuk dalam looping) tidak akan dieksekusi
    ##looping dihentikan secara paksa dan langsung mengeksekusi program/perintah diluar looping
    print(f"Angka anda: {angka}")
    print("Program di luar Looping")
    angka+=1
print ("===========Program diluar LOOPING============")
#### beda posisi pengaruh ke hasilnya!!!
'''
'''
for i in range(10):
    print(i)
    if i == 5:
        break
print("Program diluar Looping")


## Continue
- Menghentikan sementara Proses Looping / Menghentikan proses Iterasi
- Iterasi ==> part of Looping
- Langsung masuk ke iterasi berikutnya
- Continue sama seperti Break, akan dipasangkan dengan IF statement
- akan me-skip/melewatkan semua program dibawah continue kemudian melanjutkan iterasi berikutnya
'''
'''
for i in range(1,10):
    print(i)
    if i == 5:
        print("looping dihentikan oleh break")
        break
print("========== program diluar looping ============")
# '''
# for i in range(1,10):
    
#     if i == 5:
#         print("looping dihentikan oleh continue")
#         continue ## iterasi dihentikan, perintah di bawah continue(masih dalam blok looping tidak akan dieksekusi
#         ## langsung ke iterasi berikutnya i=6
#     print(i)
#     print(f"perintah bagian iterasi ke - {i}")
# print("========== program diluar looping ============")

##### Break dan Continue
# Break
# - proses keseluruhan looping dihentikan secara paksa
# - semua perintah di bawah break (masih dalam blok looping) tidak akan dieksekusi
# - langsung pindah ke program di luar looping

# CONTINUE 
# - Tahapan-Iterasi dari looping yang dihentikan
# - semua perintah dibawah sontinue (masih dalam blok looping) tidak akan dieksekusi
# - langsung pindah ke ITERASI BERIKUTNYA 
'''
################### ELSE
- Berbeda tujuan dan fungsi dengan ELSE pada IF statement
- Perintah dibawah ELSE akan Dieksekusi KETIKA LOOPING BERHENTI SECARA NATURAL
- ELSE biasanya dipasangkan dengan BREAK 
'''

# contoh penggunaan ELSE pada Looping
angka = 15
for i in range(25):
    print(i)
    if i == angka:
        print("Data Ditemukan")
        break ## akan menghentikan looping secara paksa
    # dan mengeksekusi perintah di luar looping
else:
    print("Data tidak ditemukan")
    print("Perintah masih di dalam LOOPING")
