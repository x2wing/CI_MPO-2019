import numpy as np


a = 1.45
γ = 0.2
x = np.log(a+1/a)
y= np.sin(x+a)*(1+(x+a)**2)/(γ*np.sin(a))

print(y)