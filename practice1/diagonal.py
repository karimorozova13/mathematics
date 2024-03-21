import numpy as np

def print_diagonal(matrix):
    rows, cols = len(matrix), len(matrix[0])
    
    if rows != cols:
        print('We can not show')
        
    main_diagonal = [matrix[i][i] for i in range(rows)]
    print("main_diagonal: %s" %(main_diagonal))
    reverse_diagonal = [matrix[i][cols - 1 - i] for i in range(rows)]
    print("reverse_diagonal: %s" %(reverse_diagonal))
    
    
M  = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print_diagonal(M)

matrix1 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
identity_matrix = np.eye(4)
print("m1: %s" %(identity_matrix))
print(matrix1)