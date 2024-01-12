import numpy as np

# Decomposing the determinant by row or column

a = np.array([[4,-5,7],
              [1,-4,9],
              [-4,0,5]])

# m = 4*det([[-4,9],[0,5]]) - (-5)* det([[1,9],[-4,5]]) + 7* det([[1,-4],[-4,0]])
a1= np.array([[-4,9],[0,5]])
a2= np.array([[1,9],[-4,5]])
a3= np.array([[1,-4],[-4,0]])
print(round(np.linalg.det(a)))
print(round(np.linalg.det(a1)))
print(round(np.linalg.det(a2)))
print(round(np.linalg.det(a3)))
