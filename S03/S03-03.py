import numpy as np

rng = np.random.Generator(np.random.PCG64())

array = rng.normal(100,15,1000)

print(f"the array has a mean of {np.mean(array)} a std of {np.std(array)} for a total of {array.size} values")