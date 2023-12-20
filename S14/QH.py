import matplotlib.pyplot as plt
import numpy as np
import math

def func(x):
    a = 3
    k = 2
    sigma = math.pi
    c = 1
    return(a*math.sin(k*x - sigma)+c)

x_value = np.linspace(-2*math.pi,2*math.pi,300)
y_value = []
for value in x_value:
    y_value.append(func(value))

plt.plot(x_value,y_value)
plt.show()