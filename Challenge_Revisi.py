import math
# word = input('masukkan kalimat: ')
# def is_triangular(n):
#     if n==0 or n==1:
#         return True
    
#     triangular_sum = 0

#     for i in range(n):
#         triangular_sum += i

#         if triangular_sum == n:
#             return True

#         if i == n:
#             return False

# def bla(c):
#     word1= c.replace(' ','')
#     line = 0
#     start = 0
#     end = 0
#     triangular= int((math.sqrt((2*(len(word1)))+(1/4))-(1/2)))
#     done = False
#     if is_triangular(len(word1)):
#         while not done:
#             start = end
#             end = start + line + 1
#             if end>len(word1):
#                 break
#             print(word1[start:end])
#             line += 1
#     else:
#         print('salah')

# bla(word)

# line = 0
# start = 0
# end = 0
# triangular= int((math.sqrt((2*(len(word1)))+(1/4))-(1/2)))
# bener = False
# if is_triangular(len(word1)):
#     while not bener:    
#         start = end
#         end = start+triangular-line
#         if (end-start)<1:
#             break
#         print(word1[start:end])
#         line += 1
# else:
#     print('salah')



def hitung_luas_segitiga(alas, tinggi):
  luas = (alas * tinggi) / 2
  return luas
    
var1 = hitung_luas_segitiga(5, 7)
var1
