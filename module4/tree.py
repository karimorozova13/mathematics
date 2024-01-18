import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_nodes_from([1, 2, 3, 4, 5, 6, 7])

G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])

pos = {1: (0, 0), 2: (-1, -1), 3: (1, -1), 4: (-2, -2), 5: (0, -2), 6: (2, -2), 7: (1, -3)}


nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, edge_color='gray', arrows=True)
plt.show()