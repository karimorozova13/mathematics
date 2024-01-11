import numpy as np
from math import cos,sin, radians
#  (affine transformations)

# move triangle to the keft or right , no zoom, no rotate M1 + M2
# parallel

# Зсув
# horisontal [[1,k],[0,1]] * matrix
# vertical [[1,0], [k,1]] * matrix
# k = тангенс кута tan(32)


# scaling
triangle = np.array([[1.5,2],
                     [4,1],
                     [3.5,5]])
k =0.5 
# or 
m =np.array([[0.5,0], [0,0.5]])
print(triangle*k)
print(triangle.dot(m))

# mirror image by x
# matrix * m=[[1,0],[0,-1]]

# mirror image by y
# matrix * m=[[-1,0],[0,1]]

# mirror image by start of coordinates(0,0)
# matrix * m=[[-1,0],[0,-1]] 

# Rotation
# Θ -позитивний кут повороту — проти годинникової стрілки
# m = [[cosΘ, -sinΘ],[sinΘ, cosΘ]]

triangle1 = np.array([[1.5,4,3.5],[2,1,5]])
rotation= np.array([[cos(radians(180)), -sin(radians(180))],[sin(radians(180)), cos(radians(180))]])

print(rotation.dot(triangle1))
