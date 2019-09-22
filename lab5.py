import numpy as np

print('задание 1')
np.set_printoptions(precision=3)
n = 6
a = n
b = n

M = np.zeros((a, b))
f1 = lambda i, j: (i + 2) * i / j
for i in range(a):
    for j in range(b):
        M[i][j] = f1(i + 1, j + 1)
print(f'матрица {M}')
print('задание 2')

xi = np.ptp(M, axis=1,  )
print(f'вектор: {xi}')
print('задание 3')
# это магия
xi[::-1].sort()
print(f'по убыванию: {xi}')
print('задание 4')
P=1
for i in range(a):
    for j in range(b):
        # print(M[i,j])
        P *= M[i,j] + n
print(f'произвдение = {P}')