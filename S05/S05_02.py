import scipy as sp
import matplotlib as plt

def curve(x):
    y = -x**(1/x)
    return y

min = sp.optimize.minimize_scalar(curve, method = 'brent')

print(f"the minimum of the function is {min.fun} at x = {min.x}")