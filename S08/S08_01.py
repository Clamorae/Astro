import numpy as np
import scipy.constants as cons

c = cons.physical_constants["speed of light in vacuum"]
h = cons.physical_constants["Planck constant"]
k = cons.physical_constants["Boltzmann constant"]


temp = 30.0

wavelength_min = -8.0
wavelength_max = -3.0
wavelength = np.logspace (wavelength_min , wavelength_max , num=5001)
blackbody = 2.0 * h[0] * c[0]**2 / wavelength**5 / (np.exp (h[0] * c[0] / (wavelength * k[0] * temp) ) - 1.0 )

print(f"The peak frequencey is {max(blackbody)}")