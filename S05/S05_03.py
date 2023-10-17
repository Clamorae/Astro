import requests
import scipy as sp
import numpy as np
import matplotlib.backends.backend_agg as back
import matplotlib.figure as figure

response = requests.get("https://s3b.astro.ncu.edu.tw/ai_202309/data/sample_s05.data")

open("data", "wb").write(response.content)
data_x = np.array([])
data_y = np.array([])

with open ("data", 'r') as f :
    for line in f:
        (x_buf, y_buf) = line.split()
        np.append(data_x,float(x_buf))
        np.append(data_y,float(y_buf))

def residual(param, x, y):
    residue = param[0]*x + param[1]-y
    return residue

param0 = [1, 12]

least = sp.optimize.least_squares(residual, param0, args = (data_x, data_y))

fig = figure.Figure()
canvas = back.FigureCanvasAgg(fig)
ax = fig. add_subplot (111)

ax.set_xlabel('X [ arbitrary unit ]')
ax.set_ylabel('Y [ arbitrary unit ] ')
print(least)

ax.plot(data_x, data_y, linestyle = 'None', marker = 'o', markersize = 5.0, color = 'blue', zorder =0.2, label = 'synthetic data for least - squares method')
ax.legend()
fig.savefig("./Astro/S05/S05_03.png")