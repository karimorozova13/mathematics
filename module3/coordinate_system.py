import plotly.graph_objects as go 
import numpy as np 

fig = go.Figure()

fig.add_trace(go.Scatter(x=[0,0],y=[-10,10], mode='lines', name='Y axis'))

fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(size=8, color='red'), name='Start'))

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')

points_x = np.random.randint(-8,8,5)
points_y = np.random.randint(-8,8,5)

fig.add_trace(go.Scatter(x=points_x,y=points_y,mode='markers', marker=dict(size=10, color='blue'), name='Point'))

fig.update_layout(
    title='Coordinate system on a plane with points',
    xaxis=dict(title='X axis'),
    yaxis=dict(title='Y axis'),
    showlegend= True
)

fig.show()