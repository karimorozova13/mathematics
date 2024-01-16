import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

v1 = np.array([1, 0, 0]) #x
v2 = np.array([0, 1, 0]) #y
v3 = np.array([0, 0, 1]) #z

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', label='Vector 1')
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='g', label='Vector 2')
ax.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='b', label='Vector 3')

ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])
ax.set_xlabel('Axis X')
ax.set_ylabel('Axis Y')
ax.set_zlabel('Axis Z')
ax.set_title('orthonormal basis in 3D')
ax.legend()

plt.show()

# Cartesian coordinate system.
# {i, j , k}

# i * j = j * k = k * i = 0  scalar products == 0
# | i | = | j | = | k | = 1  length == 1