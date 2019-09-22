from pprint import pprint

import numpy as np
import pandas as pd

# [0.1, 0.5] шаг 0.1
start = 0.1
stop = 0.5
step = 0.1
# ограничитель числа итераций. число слогаемых для предотвращения зацикливания
n = 100
# точность разность между значением функции и суммы
EPS = 0.001
# количество аргументов x
lenght = int((stop - start) / step + 1)

# массив x
X = np.linspace(start, stop, lenght)
# массив значений y в точках x
Y = np.vectorize(lambda x: 1 / (1 - x))(X)


# функция вычисления y(x) через сумму кол-во слогаемых и ошибку
def get_S(X: np.ndarray, Y: np.ndarray, num: int):
    S = []
    N = []
    eps = []
    r = range(0, num, 1)
    Yc = list(Y)
    # перебираем все x
    for x in X:
        s = 0
        # из массива Y вытаскиваем по элементу за каждый проход
        # т.е. каждому x соответствуюет свой истинный y
        Yi = Yc.pop(0)
        # от 0 до ограничетеля n
        for n, i in enumerate(r, 1):
            # итерация вычисления суммы
            s += x ** i
            # точность
            epsi = np.abs(Yi - s)
            # если точность нормас переходим к следующему x
            if epsi < EPS:
                break
        # заполняем массивы
        S.append(s)
        N.append(n)
        eps.append(epsi)
    return S, N, eps


S, N, eps = get_S(X, Y, n)

table = pd.DataFrame({

    'аргумент': X,
    'точное значение': Y,
    'приближенное значение': S,
    'кол. слагаемых': N,
    'ошибка': eps,
})

pprint(table)
