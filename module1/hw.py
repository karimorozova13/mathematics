import numpy as np

a =np.array([[1,2,3,4,5]])
b= np.array([[1/2,1,2,3,4]])

# transpose 
transpose_b= np.transpose(b)
print( a+ transpose_b)
print(np.dot(a,transpose_b))
print(a / transpose_b)