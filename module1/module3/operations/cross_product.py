import numpy as np 

# Векторний добуток (Cross Product)

def normal_vector(vector1,vector2):
    # Обчислення векторного добутку (cross product)
    n = np.cross(vector1,vector2)
    return n


vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])


normal = normal_vector(vector1, vector2)
print("Vector normal to the plane:", normal)