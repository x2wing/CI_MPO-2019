import numpy as np
import pandas as pd


start = 2
stop = 6
step = 0.5
lenght = int((stop - start)/step)
c= 0.13
y = np.linspace(start, stop, lenght)
φ = np.vectorize(lambda y: y**c + np.e**c)
x = np.vectorize(lambda y: y**2-4*y*np.log(φ(y)))

table = pd.DataFrame({

    'параметр y': y,
    'аргумент φ': φ(y),
    'функция x': x(y),
        })



print(table)