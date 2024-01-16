import numpy as np

def calculate_cosine_angle(vector1, vector2):
    # magnitude_vector1 = np.linalg.norm(vector1)
    mod1 = np.sqrt(np.sum(np.array(vector1) ** 2))
    mod2 = np.sqrt(np.sum(np.array(vector2) ** 2))
    
    cos_f = np.dot(vector1, vector2) / (mod1*mod2)
    return cos_f
    
vector1 = (3, 4)
vector2 = (1, 2)
angle_degrees = np.degrees(np.arccos(calculate_cosine_angle(vector1,vector2)))
print(calculate_cosine_angle(vector1,vector2))
print(angle_degrees)
