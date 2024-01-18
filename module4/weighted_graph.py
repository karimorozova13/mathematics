import networkx  as nx 
import matplotlib.pyplot as plt

graph = nx.Graph()
graph.add_weighted_edges_from([(1, 2, 3), (2, 3, 2), (3, 4, 1), (4, 5, 4)])

pos = nx.spring_layout(graph)


# Витягнення ваг кожного ребра
edge_labels = {(u, v): d["weight"] for u, v, d in graph.edges(data=True)}


nx.draw(graph, pos, with_labels=True, font_size=10, node_size=700, node_color='skyblue', font_color='black', edge_color='gray')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='red', font_size=8)


plt.title("Weighted Graph")
plt.show()