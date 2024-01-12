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

a= np.array([[1,2],[3,4]])

b=np.array([[5,6],[7,8]])
c1 = a.dot(b)
print(c1)

c= np.array([[4,6],
             [3,2]])
d= np.array([[8,2],
             [3,1]])
print(c.dot(d))

k = np.array([ [1, 2], 
              [3, 4], 
              [5,6]])
l = np.array([ [7, 8, 9], 
              [10, 11, 12] ])
total = k.dot(l)
print(total)