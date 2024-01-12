import numpy as np

a = np.array([[2,3],
              [4,5]])

# determinant = 2*5 - 3*4
determinant = round(np.linalg.det(a))
print(determinant)

b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

# determinant1 =1*5*9 + 2*6*7 + 3*4*8 - 3*5*7 - 2*4*9 - 1*6*8
determinant1 = round(np.linalg.det(b))
print(determinant1)

A = np.array(
    [[4, -5, 7],
     [1, -4, 9],
     [-4, 0, 5],
     ]
    )
print(round(np.linalg.det(A)))

# 1. determinant doesn't change with transponse
transpose_a = np.transpose(A)
print(round(np.linalg.det(transpose_a)))

# 2 if one row is zeros, determinants equal 0
zero_m= np.array(
    [[2, 7, 1, 2],
     [6, 1, 3, -1],
     [0, 0, 0, 0],
     [2, 9, 5, -1],
     ]
    )
zero_det = round(np.linalg.det(zero_m))
print(zero_det)

# 3. if change rows betwenn each other, determinant will change the sign +/-
c = np.array( [[1, 0, -1],
              [11, 4, 7],
              [-6, 0, 0],
            ])
d = np.array([[11, 4, 7],
              [1, 0, -1],
              [-6, 0, 0],
            ])
print(round(np.linalg.det(c)))
print(round(np.linalg.det(d)))

# 4 if gas two same rows, determinants equal 0
same_r = np.array(
    [[2, 7, 1, 2],
     [6, 1, 3, -1],
     [2, 7, 1, 2],
     [2, 9, 5, -1],
     ]
    )
print(round(np.linalg.det(same_r)))

# 5 if you mul row by num, determinant mul by this num
mul1 = np.array(
    [[2, 4, -12],
     [10, 3, 0],
     [1, -1, 1],
     ]
    )
b1 = np.array(
    [[1, 2, -6],
     [10, 3, 0],
     [1, -1, 1],
     ]
    )
print(round(np.linalg.det(mul1)))
print(round(np.linalg.det(b1)))

# 6 if some row is sum of el of other matrix in same row, determinat will be sum of determinant of that  matrix d(a)= d(b) + d(c)
A1 = np.array(
    [[6, 4, 12],
     [10, 3, 0],
     [1, -1, 1],
     ]
    )
#  a a a      b+c b+c b+c
# [6,4,12] = [2+4,3+1,9+3]
B1 = np.array(
    [[2, 3, 9],
     [10, 3, 0],
     [1, -1, 1],
     ]
    )
C1 = np.array(
    [[4, 1, 3],
     [10, 3, 0],
     [1, -1, 1],
     ]
    )
print(round(np.linalg.det(A1)))
print(round(np.linalg.det(B1)))
print(round(np.linalg.det(C1)))

# 7. if some row is Linear combination of others, determinants = 0
lin = np.array(
    [[2, 7, -1],
     [0, 1, 3],
     [2, 9, 5], #this row is sum of 1st row and second mul 2(*2) r = (2+7+(-1)) + ((0+1+3)*2) = 16
     ]
    )
print(round(np.linalg.det(lin)))

# 8. if to one row add ele from other row and mul by any num, determinant will not change
A2 = np.array(
    [[3, 8, 0],
     [1, 1, 1],
     [2, 9, 5],
     ]
    )
# first row = a1 - a2
B2 = np.array(
    [[2, 7, -1],
     [1, 1, 1],
     [2, 9, 5],
     ]
    )
print(round(np.linalg.det(A2)))
print(round(np.linalg.det(B2)))








