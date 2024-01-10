import numpy as np

"""
    m -row
    n - column
"""

# square matrix row len == column len

# diagonals

def print_diagonals(matrix):
    rows, cols = len(matrix), len(matrix[0])
    
    if rows != cols:
        print('It is not a square matrix')
        
    main_diag= [matrix[i][i] for i in range(rows)]
    anti_diag = [matrix[i][cols - 1 -i] for i in range(rows)]
    
    print(main_diag)
    print(anti_diag)
m = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print_diagonals(m)

# identity matrix
m1 = np.identity(4)
m2 = np.eye(4)

print(m1)
print(m2)

# Upper triangular matrix
m4 = np.array([[1, 2, 3],[0, 5, 6],[0, 0, 9]])

# Lower triangular matrix
m4 = np.array([[0, 0, 3],[7, 5, 0],[8, 6, 0]])

# Transposed matrix At - make columns as rows

a = np.array([[1,5,3],[5,1,2]])
b= np.array([[1,2], [3,4]])
c= np.array([[1,2,2,2], [3,4,4,4]])
d= np.array([np.ones(4), np.ones(4), np.ones(4), np.ones(4)])
print(d)
