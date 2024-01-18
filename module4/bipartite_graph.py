import networkx  as nx 
import matplotlib.pyplot as plt

# Дводольний граф (Bipartite Graph)
graph = nx.complete_bipartite_graph(2,3)
group_nodes1 = {0,1}
group_nodes2 = {3,2,4}

pos = nx.spring_layout(graph)
node_colors = [0 if node in group_nodes1 else 1 for node in graph.nodes()]

nx.draw(graph,pos,with_labels=True, font_size=10, node_size=700, node_color=node_colors, cmap=plt.cm.Paired)

plt.title("Bipartite Graph with Node Colors")
plt.show()
