import numpy as np

A = np.array([[-1,1,2],
               [0,-1,-3],
               [4,-3,2]])
B = np.array([1,-4,7])


def solve_inv_matrix(a, b, verbose=False):
    inv_m = np.linalg.inv(a)
    t = b.T
    return inv_m.dot(t)
print(f"Вектор рішення: \r\n {solve_inv_matrix(A, B)}")


def solve_cramer(a, b,verbose=False):
    D = np.linalg.det(a)
    num_variables = a.shape[0]
    
    solutions = np.zeros(num_variables)

    for i in range(num_variables):
        temp_matrix = a.copy()
        temp_matrix[:, i] = b.flatten()

        determinant_temp = np.linalg.det(temp_matrix)

        solutions[i] = determinant_temp / D
    return solutions


print(f"Вектор рішення: \r\n {solve_cramer(A, B)}")

def gaussian_elimination(a, b):
    n = len(b)
    
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a [i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    
    return b


print(f"Вектор рішення: \r\n {gaussian_elimination(A, B)}")



