#import numpy as np

#GÖREV 1
# x=np.random.randint(0,100,1000)
# meanvalue=np.mean(x)
# stdvalue=np.std(x)
# print(x)
# print()
# print(meanvalue)
# print()
# print(stdvalue)
# print()
# print(x[x>50])
# print()
# y=x.reshape(10,100)
# print(y)
# print()
# print(np.sum(y,axis=1))
# print()
# print(np.mean(y,axis=1))

#GÖREV 2
# x=np.random.random(size=(10,10))
# print(x)
# print(np.linalg.inv(x))
# ozdegerler, ozvektorler =np.linalg.eig(x)
# print(ozdegerler)
# print(ozvektorler)
# ortalama=np.mean(x)
# y=x-ortalama
# print(y)

#GÖREV 3
# import matplotlib.pyplot as plt
#x=np.random.normal(50,10,1000),
# plt.hist(x, bins=30, edgecolor='red')
# plt.xlabel("Değerler")
# plt.ylabel("Değerler")
# plt.title("Histogram")
# plt.grid(True)
# plt.show()
# yirmibeslik=np.percentile(x,25)
# yetmisbeslik=np.percentile(x,75)
# print(yirmibeslik)
# print(yetmisbeslik)

# ortalama = np.mean(x)
# std = np.std(x)
# zscore = (x-ortalama) / std
# #print(zscore)
# yenihal=zscore.reshape(10,100)
# #print(yenihal)
# print(np.mean(yenihal,axis=0))

#GÖREV 4
# def f(A):
#     row, column = A.shape
#     sonuc = np.zeros_like(A, dtype=float)
#
#     for i in range(row):
#         for j in range(column):
#             komsu = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
#                      (i, j - 1), (i, j + 1),
#                      (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
#             toplam = 0
#             sayisi = 0
#             for ki, kj in komsu:
#                 if 0 <= ki < row and 0 <= kj < column:
#                     toplam += A[ki, kj]
#                     sayisi += 1
#             sonuc[i, j] = toplam / sayisi
#     return sonuc
# B=np.arange(0,25).reshape((5,5))
# yenimatrix=f(B)
# print(B)
# print(yenimatrix)



