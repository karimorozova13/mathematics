import networkx  as nx 
import matplotlib.pyplot as plt

def visualize_graph(graph, title):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_size=10, node_size=700, node_color='skyblue', font_color='black', edge_color='gray')
    plt.title(title)
    plt.show()
    
graph= nx.complete_graph(5)
visualize_graph(graph, 'Complete graph')
