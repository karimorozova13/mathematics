import matplotlib.pyplot as plt
import numpy as np 

# Directed line segment ->Спрямований відрізок -> →AB -> vector →a

points_x = np.array([1,0])
points_y = np.array([0,1])

plt.figure(figsize=(6,6))
plt.quiver(0,0, points_x[0], points_x[1], angles='xy', scale_units='xy', scale=1, color='r', label='X axis')
plt.quiver(0,0, points_y[0], points_y[1], angles='xy', scale_units='xy', scale=1, color='b', label='Y axis')

# Designation of the origin of coordinates
plt.scatter(0,0, color='b', marker='o')

# Adding signatures
plt.text(points_x[0], points_x[1], ' X', fontsize=12, color='r', va='bottom', ha='left')
plt.text(points_y[0], points_y[1], ' Y', fontsize=12, color='b', va='bottom', ha='left')

# Setting the graph view
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('coordinate system with unit vectors')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.show()
