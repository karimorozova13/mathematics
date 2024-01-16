import matplotlib.pyplot as plt
import numpy as np

# cos(x) = v[0] / |v|
# cos(y) = v[1] / |v|
# cos(z) = v[2] / |v|

def magnitude(vector):
    return np.sqrt(np.sum(vector**2))

def compute_direction_cosines(vector):
    cos_alfa = vector[0] / magnitude(vector)
    cos_beta = vector[1] / magnitude(vector)
    cos_gamma = vector[2] / magnitude(vector)
    return cos_alfa, cos_beta, cos_gamma
    

vector = np.array([2,3,4])
cos_alpha, cos_beta, cos_gamma = compute_direction_cosines(vector)
print(vector)
print(magnitude(vector))
print(cos_alpha)
print(cos_beta)
print(cos_gamma)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], color='b', label='Vector A')

ax.text(vector[0] / 2, vector[1] / 2, vector[2] / 2, f'α={cos_alpha:.2f}\nβ={cos_beta:.2f}\nγ={cos_gamma:.2f}', color='r')

ax.set_xlim([0, 5])
ax.set_ylim([0, 5])
ax.set_zlim([0, 5])
ax.set_xlabel('Axis X')
ax.set_ylabel('Axis Y')
ax.set_zlabel('Axis Z')
ax.set_title('Directional cosines of a vector on a plane')


plt.legend()
plt.show()

