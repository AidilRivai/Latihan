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