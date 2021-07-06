# 1.
# input
# Masukkan Jumlah Hari:
# Output (Nyatakan jumlah hari tsb dalam)
# ... Tahun ... Bulan ... minggu ... Hari 

# contoh
# Masukkan Jumlah Hari: 35
# Output
# 00 Tahun 01 Bulan 00 Minggu 05 Hari
# Ketentuan:
# - Format output dalam format 2 digit
# 1 tahun = 365 hari
# 1 bulan = 30 hari
# 1 minggu = 7 hari 
# jumlah hari maksimal 4000, jika diinput diatas 4000 keluar notif: Jumlah hari diatas batas maksimal
# - Jumlah hari tidak bisa menerima nilai dibawah NOL
# jika diinput dibawah 0/nilai negatif keluar notif : jumlah hari di bawah batas Minimum
# - Jumlah hari tidak bisa menerima String, atau angka Desimal ==> Keluar notif:
# Jumlah Hari yang anda masukkan salah
'''
hari=(input("Masukkan Hari: "))

if hari.isdigit():
    hari=int(hari)
    if hari<=4000 and hari>=0:
        tahun=round(hari/365)
        sisaharitahun=round(hari%365)
        bulan=round(sisaharitahun/30)
        sisaharibulan=round(sisaharitahun%30)
        minggu=round(sisaharibulan/7)
        hari=round(sisaharibulan%7)
        print(f"{tahun:02} Tahun {bulan:02} Bulan {minggu:02} Minggu {hari:02} Hari")
    elif hari>4000:
        print("Jumlah hari diatas batas maksimal")
    elif hari<0:
        print("Jumlah hari di bawah batas minimum")
else:
    print("Jumlah Hari yang anda masukkan salah")
'''
# 2.
# Hitung BMI (Body Mass Index)
# Rumus BMI: Massa(dalam Kg) / (tinggi (dalam Meter) pangkat 2)
# Input:
# Masukkan Tinggi Badan (dalam cm):
# Masukkan Berat badan (Dalam kg):
# Outputnya
# Tinggi badan anda ... (dalam meter) dan berat anda ... (kg), BMI anda ... (nilai BMI)... (dibulatkan 2 angka dibelakang koma)... 
# dan anda termasuk .... (sesuai kondisi)...

# Kondisi:
# BMI < 18.5 ==> Berat badan Kurang
# 18.5 - 24.9 ==> Berat badan ideal
# 25 - 29 ==> Berat badan Berlebih
# 30 - 39.9 ==> Berat badan sangat Berlebih
# BMI >= 40 ==> Obesitas
'''
tb=input("Masukkan Tinggi Badan(dalam cm): ")
bb=input("Masukkan Berat Badan(dalam kg): ")
meter=100

if tb.isdigit() and bb.isdigit():
    tb=(int(tb)/100)
    bb=int(bb)
    tb=round(tb,2)
    bb=round(bb,2)
    if tb <=(300/meter) and bb<=200:
        BMI=(bb/(pow(tb,2)))
        BMI=round(BMI,2)
        if BMI<18.5:
            print(f"Tinggi badan anda {tb} meter dan berat anda {bb} kg, BMI anda {BMI} dan anda termasuk Berat Badan Kurang")
        elif BMI>= 18.5 and BMI<25:
            print(f"Tinggi badan anda {tb} meter dan berat anda {bb} kg, BMI anda {BMI} dan anda termasuk Berat Badan Ideal")
        elif BMI>=25 and BMI<30:
            print(f"Tinggi badan anda {tb} meter dan berat anda {bb} kg, BMI anda {BMI} dan anda termasuk Berat Badan Berlebih")
        elif BMI>=30 and BMI<40:
            print(f"Tinggi badan anda {tb} meter dan berat anda {bb} kg, BMI anda {BMI} dan anda termasuk Berat Badan Sangat Berlebih")
        else:
            print(f"Tinggi badan anda {tb} meter dan berat anda {bb} kg, BMI anda {BMI} dan anda termasuk Obesitas")
    elif tb >(300/meter) or bb>200:
        print('Tinggi/Berat badan anda diatas batas')
    elif tb<=0 or bb<=0:
        print("Tidak menerima Nol atau angka negatif")

else:
    print("tidak menerima nilai desimal atau string")
'''
# Ketentuan
# -Nilai BMI pada Output dibulatkan 2 angka Desimal
# -Nilai TInggi dan BB tidak menerima nilai negatif atau dibawah NOL
# keluar notif: "Tidak menerima angka negatif"
# Inputan (Nilai tinggi badan dan berat badan) tidak menerima nilai desimal atau String
# kalau input string atau desimal : "angka yang anda masukkan salah"
# Batas maksimal tinggi badan : 300 cm
# Batas maksimal BB: 200 kg
# kalau diatas itu "Tinggi/berat badan anda diatas batas"
# - notifikasi keluar setelah user melakukan input tinggi dan berat badan 


# 3. 
# Input:
# Masukkan Nilai:

# Output:
# Nilai anda .... dan anda .... (Sesuai Kondisi)

# Kondisi:
# 90 Keatas : Grade A
# 85 Keatas : Grade A-
# 80 Keatas : Grade B 
# 75 Keatas : Grade B- 
# 70 Keatas : Grade C 
# 65 Keatas : Grade D 
# dibawah 65 dan diatas 40: Perlu Remedial
# dibawah 40 : Tidak Lulus
# Nilai Maksimum 100, Nilai minimum NOL
# Jika Nilai diatas 100 ==> nilai diluar jangkauan
# Jika nilai dibawah nol ==> tidak menerima angka negatif

nilai=int(input("Masukkan Nilai: "))
if nilai>0 and nilai<=100:
    if nilai>=90:
        grade="Grade A"
    elif nilai>=85 and nilai <90:
        grade="Grade A-"
    elif nilai>=80 and nilai <85:
        grade="Grade B"
    elif nilai>=75 and nilai <80:
        grade="Grade B-"
    elif nilai>=70 and nilai <75:
        grade="Grade C"
    elif nilai>=65 and nilai <70:
        grade="Grade D"
    elif nilai>=40 and nilai <65:
        grade="Perlu Remedial"
    else:
        grade="Tidak Lulus"
    print(F"Nilai anda {nilai} dan anda {grade}")
elif nilai>100:
    print("Nilai diluar Jangkauan")
else:
    print("Tidak menerima angka negatif")



# ### Additional Funct
# Print(abs(-5)) ====> ## Absolut ==> mengabaikan arah Vector ==> Mengambil Nilai Positifnya
# negatif .... 0 ..... positif
