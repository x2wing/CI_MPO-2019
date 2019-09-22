import numpy as np
import pandas as pd


start = 0.1
stop = 0.5
step = 0.1
# число слогаемых для предотвращения зацикливания
n = 10
EPS = 0.01
lenght = int((stop - start)/step+1)


X = np.linspace(start, stop, lenght)
Y = np.vectorize(lambda x: 1/(1-x))(X)
# S = np.vectorize(lambda y: y**2-4*y*np.log(φ(y)))
def get_S(X, Y, num):
	y = N = eps = []
	r = range(0,num,1)
	Yc = list(Y)
	for x in X:
		s = 0
		Yi = Yc.pop(0)
		print(f'Yi={Yi}')
		for n, i in enumerate(r):
			s+=x**i
			epsi = np.abs(Yi-s)
			if epsi < EPS:
				break
		y.append(s)
		eps.append(epsi)
		N.append(n)
	return y, N, eps



S, N, eps = get_S(X, Y, n)
print(S, N, eps)
table = pd.DataFrame({

    'аргумент': X,
    'точное значение': Y,
    'приближенное значение': S,
    'количество слагаемых': N,
    'ошибка': eps,
        })



print(table)