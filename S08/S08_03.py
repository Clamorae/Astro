import uncertainties
from uncertainties import unumpy as unp

a = uncertainties.ufloat(16.8,0.6)
b = uncertainties.ufloat(5.8,0.2)

G = uncertainties.ufloat(314.701,0.183)

temp = unp.exp((unp.log(G)-a)/b)

print(f"Effective Temperature: {temp:.2f} K")