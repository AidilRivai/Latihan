# # Tugas Personal 3:
# # Deadline kamis tgl 3 Juni 2021
# # Submit via email 

# # 1.
# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4
# # 5 5 5 5 5

# print("1.")
# for a in range(1,6): #1,2,3,4,5
#     for b in range(1, a+1): ### untuk b di range a+1 start 1
#         print((a), end=" ")
#     print()
# print("="*50)

# # 2.
# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4
# # 1 2 3 4 5

print("2.")
for c in range(1,6):
    for d in range(1, c+1):
        print(d, end=" ")
    print()

# print("="*50)

# # 3.
# # 5
# # 5 4
# # 5 4 3
# # 5 4 3 2
# # 5 4 3 2 1
# print("3.")
# for e in range(4,-1,-1):
#     for f in range(5, e,-1):
#         print(f,end=" ")
#     print()

# print("="*50)

# # 4.
# # 1 1 1 1 1
# # 2 2 2 2
# # 3 3 3
# # 4 4
# # 5

# print("4.")
# for g in range(1,6):
#     for h in range(g,6):
#         print(g,end=" ")
#     print()

# print("="*50)

# # 5.
# # 1 2 3 4 5
# # 1 2 3 4
# # 1 2 3
# # 1 2
# # 1
# print("5.")
# for i in range(6,1,-1):
#     for j in range(1,i):
#         print(j,end=" ")
#     print()
# print("="*50)

# # 6.
# # 5 4 3 2 1
# # 5 4 3 2
# # 5 4 3
# # 5 4
# # 5
# print("6.")
# for k in range(1,6):
#     for l in range(5, k-1,-1):
#         print(l, end=" ")
#     print()
# print("="*50)

# # 7.
# #         *
# #       * * *
# #     * * * * *
# #   * * * * * * *
# #   * * * * * * *
# #     * * * * *
# #       * * *
# #         *

# print("7.") ###Mas Kal klo misalnya baca ini, untuk no 7 ini copas google, dan udah nyari yang ada penjelasannya gak nemu 
# ### adanya cuma commandnya doang, gak enak soalnya klo nyontek tapi gak ngerti juga,
# ### klo bisa minggu minta tolong dibahas mas
# ### Makasih

# kalimat=input("Masukkan Kalimat: ")
# kalimat1=(kalimat.replace(" ",""))
# baris=len(kalimat1)
# pisah=list(kalimat1)
# # if (baris // 2) == 0:
# for m in range(0, baris+1):
#         # for n in range(1, baris-m+1):
#             # print(" ", end="")
#     for n in range(1,2+m):
#         print("*", end="")
#     print()
# for m in range(baris,-1,-1):
#         # for n in range(1,baris-m+1):
#             # print(" ", end="")
#     for n in range(1,2+m):
#         print("*", end="")
#     print()

# print(kalimat1)