import numpy as np

# 3* A 
A =np.array([[2,1,-1], [0,1,-4]])
print(A*5)

B =np.array([[7,1,-1], [2,3,-4]])
print(B*2)

C =np.array([[1,5,-1], [7,1,-1], [5,3,1]])
print(C*5)

# matrix * matrix
"""
a= [[a11,a12],[a21,a22]]

b=[[b11,b12],[b21,b22]]

mul = [[a11*b11 + a12 * b21, a11*b12 + a12*b22 ], [a21*b11 + a22 * b21, a21 *b12 + a22 * b22]]
    
"""