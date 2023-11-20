import scipy.constants as cons
import numpy as np

lum = 72
radius = 1055

k = cons.physical_constants["Boltzmann constant"]

temp = ((lum) / (4 * np.pi * k[0] * radius ** 2))** 0.25

print(f"Effective Temperature: {temp:.2f} K")