import networkx  as nx 
import matplotlib.pyplot as plt

# empty graph
G= nx.Graph()

# add Vertexes
G.add_nodes_from([1,2,3,4,5])

# add adges (ребер)
G.add_edges_from([(1,2), (1,3), (2,4), (2,5)])

# graph visualisation
pos =nx.spring_layout(G) #position of top
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700,node_color='teal', font_size=10, edge_color='green')

plt.show()