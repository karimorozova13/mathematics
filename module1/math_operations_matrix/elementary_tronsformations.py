import numpy as np

# types of elementary transformations:

# 1. (A−1)-1 = A
matrix = np.array([[1, 2, 1],
                   [3, -5, 3],
                   [2, 7, -1]])
inv_m = np.linalg.inv(matrix)
inv_inv_m = np.linalg.inv(inv_m)

# print(matrix)
# print(inv_m)
# print(inv_inv_m)

matrix_t = matrix.T


# 2. (At)-1 = (A-1)t
inv_t_m = np.linalg.inv(matrix_t)
t_inv_m =inv_m.T
# print(matrix_t)
# print(inv_t_m)
# print(t_inv_m)

# 3. (AB)-1 = B-1 * A-1
matrix_a = np.array([[1, 2, 1],
                   [3, -5, 3],
                   [2, 7, -1]])


matrix_b = np.array([[4, 3, 7],
                   [3, -2, 3],
                   [2, 3, -1]])
inv_a =np.linalg.inv(matrix_a)
inv_b =np.linalg.inv(matrix_b)

print(inv_b.dot(inv_a))

dot_m = matrix_a.dot(matrix_b)
inv_dot = np.linalg.inv(dot_m)
print(inv_dot)

# 4. det(A-1) = (detA)-1
inv_m1 = np.linalg.inv(matrix)
det_inv =np.linalg.det(inv_m1)
print(det_inv)

det_1 = round(np.linalg.det(matrix))
# (detA)-1
c= 1/det_1
print(c)





