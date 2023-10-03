import numpy as np
import matplotlib.pyplot as plt

rng = np.random.Generator(np.random.PCG64())

array = rng.normal(1000,1000,10**6)
plt.hist(array)
plt.savefig("2.png")