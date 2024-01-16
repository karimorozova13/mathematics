import numpy as np 


def mixed_product(v1,v2,v3):
    res= np.dot(v1, np.cross(v2,v3))
    return res

a = np.array([2, -2, -3])
b = np.array([4, 0, 6])
c = np.array([-7, -7, 1])

omega = np.linalg.det(np.dstack([a,b,c])) # == mixed_product
print(omega)
print(mixed_product(a,b,c))
