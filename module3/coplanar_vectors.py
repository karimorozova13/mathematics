import plotly.graph_objects as go
import numpy as np

# a plane to which they are parallel, or they lie on the same plane.
vector_a = np.array([2, 3, 1])
vector_b = np.array([1, 4, 2])

# normal to the plane formed by the vectors
normal_vector = np.cross(vector_a, vector_b)

# arr of points on plane

point_in_plane = np.array([0,0,0])
points_on_plane = np.column_stack((vector_a,vector_b,normal_vector)) + point_in_plane

fig = go.Figure()

fig.add_trace(go.Scatter3d(x=[0, vector_a[0]], y= [0, vector_a[1]], z = [0, vector_a[2]], mode='lines+markers', marker=dict(size=5), line=dict(color='red'), name='Vector A'))
fig.add_trace(go.Scatter3d(x=[0, vector_b[0]], y= [0, vector_b[1]], z = [0, vector_b[2]], mode='lines+markers', marker=dict(size=5), line=dict(color='blue'), name='Vector B'))
fig.add_trace(go.Scatter3d(x=[0, normal_vector[0]], y= [0, normal_vector[1]], z = [0, normal_vector[2]], mode='lines+markers', marker=dict(size=5), line=dict(color='green'), name='Normal'))

# Adding a plane to a graph
xx, yy = np.meshgrid(np.linspace(-2, 4, 5), np.linspace(-2, 4, 5))
zz = (-normal_vector[0] * xx - normal_vector[1] * yy - point_in_plane[2]) / normal_vector[2]
fig.add_trace(go.Surface(x=xx, y=yy, z=zz, opacity=0.3, colorscale='gray', name='Plane'))


fig.update_layout(scene=dict(aspectmode='data'))
fig.update_layout(scene=dict(xaxis_title='Axis X', yaxis_title='Axis Y', zaxis_title='Axis Z'))
fig.update_layout(title='Coplanar vectors lying in the plane and the normal to the plane')

fig.show()

