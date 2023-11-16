import scipy.constants as cons
import numpy as np

lum = 1055
radius = 72

k = cons.physical_constants["Boltzmann constant"]

temp = ((lum * 3.828e26) / (4 * np.pi * k[0] * radius ** 2)** 0.25)

print(f"Effective Temperature: {temp:.2f} K")