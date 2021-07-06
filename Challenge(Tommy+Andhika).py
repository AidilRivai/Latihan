npwp = str(input("Masukkan NPWP : "))
#no npwp 20 karakter
cek1 = npwp[0:2]
cek2 = npwp[3:6]
cek3 = npwp[7:10]
cek4 = npwp[11]
cek5 = npwp[13:16]
cek6 = npwp[17:20]
abjad = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def ceknpwp (i,j):
    for i in npwp :
        for j in abjad:
            if i == j:
                return "Kode seri NPWP tidak valid !"
                break
    if npwp[0] != "0" or npwp[1] == "0" or len(npwp) > 20 or len(npwp) < 20:
        return "Kode seri NPWP tidak valid !"
    elif npwp[2].isdigit() or npwp[6].isdigit() or npwp[10].isdigit() or npwp[12].isdigit() or npwp[16].isdigit():
        return "Kode seri NPWP tidak valid !"
    else:
        return "Kode seri NPWP valid !"

cek = ceknpwp(len(npwp),len(abjad))
print(cek)

if cek == "Kode seri NPWP valid !":
    x = int(npwp[1])
    if x >=1 and x <=3:
        y = "Wajib Pajak Badan"
    elif x >3 and x <=6:
        y = "Wajib Pajak Pengusaha"
    elif x == 5:
        y = "Wajib Pajak Karyawan"
    else :
        y = "Wajib Pajak Orang Pribadi"

    print("Identitas Wajib Pajak :", cek1, y)
    print("Nomor Registrasi :",cek2,".",cek3)
    print("Alat Pengaman :",cek4)
    print("Kode KPP :", cek5)
    print("Status Wajib Pajak :",cek6)
else:
    print("")

