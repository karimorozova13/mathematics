import numpy as np

# for determinant == 0 is enough if its rows/columns were linear dependent
matrix_example = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

rank = np.linalg.matrix_rank(matrix_example)
print(rank)