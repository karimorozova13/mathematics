import numpy as np 
from numpy import linalg as LA 

# +, -

a = np.array([1,3])
b = np.array([2,0])

print(a + b)
print(a - b)

# angle between vectors

cos_angle = np.dot(a,b) / LA.norm(a) / LA.norm(b)
angle_radians = np.arccos(cos_angle)
print(cos_angle)
print(angle_radians)

# modulus, distance

modulus = LA.norm(a - b, ord=1)
print(modulus)