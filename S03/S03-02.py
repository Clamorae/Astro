import numpy as np

matrix = np.matrix([[6,7],[5,6]])
matrix = np.matrix.astype(matrix,float)

inverse = np.linalg.inv(matrix)

print(f"the inverse of \n{matrix} \nis \n{inverse}")