import plotly.graph_objects as go
import numpy as np

def dot_product(start_vec1, end_vec1, start_vec2, end_vec2):
    vector1 = np.array(end_vec1) - np.array(start_vec1)
    vector2 = np.array(end_vec2) - np.array(start_vec2)
    
    scalar_product = np.dot(vector1,vector2)
    return scalar_product

vector1_start = [1, 2]
vector1_end = [4, 6]


vector2_start = [3, 1]
vector2_end = [6, 3]


print(dot_product(vector1_start, vector1_end, vector2_start, vector2_end))
    