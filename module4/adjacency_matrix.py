import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def build_and_visualize_graph(adjacency_matrix):

    graph = nx.Graph()
    num_nodes = adjacency_matrix.shape[0]

    graph.add_nodes_from(range(num_nodes))

    # Додавання ребер та їх ваг
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if adjacency_matrix[i, j] != 0:
                graph.add_edge(i, j, weight=adjacency_matrix[i, j])


    pos = nx.spring_layout(graph)

    nx.draw(graph, pos, with_labels=True, font_size=10, node_size=700, font_color='black', edge_color='gray')


    # Додавання ваг ребер
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_color='red')


    plt.title("Graph from Adjacency Matrix")
    plt.show()


example_adjacency_matrix = np.array([
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
])


build_and_visualize_graph(example_adjacency_matrix)