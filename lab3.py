import numpy as np
import pandas as pd


p= np.sqrt(0.17)* np.log10(5)
x= -2.7
px = p*x
if px<=-2:
    y=np.log(np.abs(p)+np.abs(x))
elif -2<px<0:
    y=np.log(np.abs(p-x))
elif px>=0:
    y=np.exp(p+x**2)

print(y)
