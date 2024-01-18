import numpy as np 
import matplotlib.pyplot as plt 

# IN PLANE

# AB = (x,y) - coordinates
#  | AB | = square of x*x + y+y = Modulus

# модуля вектора, magnitude of vector
def compute_vector_magnitude(vector):
    return np.sqrt(np.sum(vector ** 2))

vector_a = np.array([2,3])

magnitude_a = compute_vector_magnitude(vector_a)
print(magnitude_a)
print(vector_a)

plt.figure(figsize=(6,6))
plt.quiver(0,0, vector_a[0], vector_a[1], angles='xy', scale_units='xy', scale= 1, color='b', label= 'Vector A')

plt.text(vector_a[0] / 2, vector_a[1] / 2, f'Modulus: {magnitude_a:.2f}', color='r')

plt.xlim([0, 5])
plt.ylim([0, 5])
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('magnitude of vector on a plane')
plt.xlabel('Axis X')
plt.ylabel('Axis Y')
plt.legend()
plt.show()
