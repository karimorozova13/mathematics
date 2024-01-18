import plotly.graph_objects as go 
import numpy as np

# matrix - rectangular table of numbers (прямокутна таблиця чисел )
# matrix - transformation of space (перетворення простору )

# coordinate line

num_points = 10
points_x= np.random.randint(-10,10,num_points)
points_y = np.zeros(num_points)

# create Figure() for graph
fig = go.Figure()

# horizontal X-axis
fig.add_trace(go.Scatter(x=[-10,10], y=[0,0], mode='lines', name='X-axis'))

# points to the coordinate line
fig.add_trace(go.Scatter(x=points_x, y=points_y, mode='markers', name='Points'))

# graph view
fig.update_layout(
    title='Coordinate line',
    xaxis=dict(title='X axis'),
    yaxis=dict(title='Y axis'),
    showlegend=True
)

fig.show()