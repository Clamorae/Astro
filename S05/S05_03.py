import requests
import scipy as sp
import numpy as np

response = requests.get("https://s3b.astro.ncu.edu.tw/ai_202309/data/sample_s05.data")

open("data", "wb").write(response.content)
data_x = np.array([])
data_y = np.array([])

with open ("data", 'r') as f :
    for line in f:
        (x_buf, y_buf) = line.split()
        np.append(data_x,float(x_buf))
        np.append(data_y,float(y_buf))

print(data_x)
print(data_y)

def residual(param, x, y):
    residue = param[0]*x + param[1]-y
    return residue

param0 = [1, 12]

least = sp.optimize.least_squares(residual, param0, args = (data_x, data_y))
print(least)