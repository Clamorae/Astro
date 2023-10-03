import matplotlib.figure
import matplotlib.backends
import numpy as np

x = np.linspace(0,10,1000)
y = (-7 * x) + 19

fig = matplotlib.figure.Figure()
ax = fig.add_subplot(111)
ax.plot(x,y,label = "f(x) = -7x + 19")
ax.legend()
ax.grid()


fig.savefig("1.png")