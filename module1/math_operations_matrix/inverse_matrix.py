import numpy as np

# E = single matrix (одинична)
# [[1,0,0],
#  [0,1,0],
#  [0,0,1]]


# non-degenerate matrix  |A| != 0
# degenerate matrix  |A| == 0

# inverse matrix if matrix is non-degenerate

# attached matrix.

A = np.array([[1, 0, 3],
              [-1,-1,2],
              [4,  7,2]])
det = round(np.linalg.det(A))
print(det) #-25 !=0
a11 = 1 * round(np.linalg.det(np.array([[-1,2],[7,2]])))
a12 = -1 * round(np.linalg.det(np.array([[-1,2],[4,2]])))
a13 = 1 * round(np.linalg.det(np.array([[-1,-1],[4,7]])))
a21 = -1 * round(np.linalg.det(np.array([[0,3],[7,2]])))
a22 = 1 * round(np.linalg.det(np.array([[1,3],[4,2]])))
a23 = -1 * round(np.linalg.det(np.array([[1,0],[4,7]])))
a31 = 1 * round(np.linalg.det(np.array([[0,3],[-1,2]])))
a32 = -1 * round(np.linalg.det(np.array([[1,3],[-1,2]])))
a33 = 1 * round(np.linalg.det(np.array([[1,0],[-1,-1]])))


print(a11) #-16
print(a12) #10
print(a13) #-3
print(a21) #21
print(a22) #-10
print(a23) #-7
print(a31) #3
print(a32) #-5
print(a33) #-1
attached_m = np.array(([[-16,10,-3],
                        [21,-10,-7],
                        [3,-5,-1]]))
# inverse_m = -1/25 * attached_m
# inverse_m = np.array([[16/25, -21/25, -3/25],
#                     [-2/5,   2/5,    1/5],
#                     [3/25,   7,25,   1/25]
#                     ])

inverse_matrix = np.linalg.inv(A)
print(inverse_matrix)
print(A.dot(inverse_matrix))