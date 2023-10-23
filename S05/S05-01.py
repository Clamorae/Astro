import scipy as sp
import numpy as np
import matplotlib as mplt
import matplotlib.figure as figure
import matplotlib.backends.backend_agg as back

def dydx(t, y):
    dy = -3 * y
    return dy

x = np.linspace(0,10,100)
y_0 = 1

solution = sp.integrate.solve_ivp(dydx,[0.0, 50.0],[y_0],method = 'RK45', dense_output = True , t_eval = x ,rtol =10** -6 , atol =10** -9)

print(solution)

x = solution.t 
y = solution.y[0]

fig = figure.Figure()
canvas = back.FigureCanvasAgg(fig)
ax = fig.add_subplot (111)

ax.set_title(r'$dy/dx=-3y$')
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')

ax.plot(x,y, linestyle = '--', linewidth = 3.0, color = 'blue', zorder = 0.2, label = 'numerical solution')
ax.legend()

fig.savefig("S05_01.png")
