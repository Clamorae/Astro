import scipy as sp

#TODO Print the curve

def curve(x):
    y = -x**(1/x)
    return y

min = sp.optimize.minimize_scalar(curve, method = 'brent')

print(min)