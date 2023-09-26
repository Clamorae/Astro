import uncertainties

Astar = uncertainties.ufloat(17.54,0.02)
Bstar = uncertainties.ufloat(18.93,0.03)

diff = abs(Astar - Bstar)

print(f" the magnitude difference between {Astar} and {Bstar} is {diff}")