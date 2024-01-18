import plotly.graph_objects as go 
import numpy as np

fig = go.Figure()

num_points = 10
points_x=np.random.rand(num_points) * 10
points_y=np.random.rand(num_points) * 10
points_z=np.random.rand(num_points) * 10

fig.add_trace(go.Scatter3d(x=points_x, y= points_y, z= points_z, mode='markers', marker=dict(size=5, color='red', opacity=0.8), name='Random points'))

fig.update_layout(
    title='3D plane with points',
    scene=dict(
        xaxis=dict(title='X axis'),
        yaxis=dict(title='Y axis'),
        zaxis=dict(title='Z axis')
        ),
    showlegend=True
)

fig.show()
