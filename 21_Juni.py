nilai = {
    "Andi":85,
    "Beni":96,
    "Dodi":75,
    "Riko":80,
    "Andre":90,
    "Login": {"Userid" : "Admin", "Password":"Rahasia", "Cars":["Jazz","Yaris"]}
}

print(nilai["Login"])
nilai["Login"]["Cars"].insert(1,"Xpander")
print(nilai["Login"])