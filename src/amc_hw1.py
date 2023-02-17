import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

import is_g_k_colorable


def create_custom_graph():
    g = nx.Graph()
    g.add_nodes_from([i for i in range(1, 15)])
    edges = [
        (1, 2), (1, 3), (1, 4), (1, 7),
        (2, 3), (2, 4), (2, 8),
        (3, 4), (3, 6),
        (4, 5),
        (5, 6), (5, 7), (5, 13),
        (6, 7), (6, 12),
        (7, 14),
        (8, 9), (8, 10), (8, 11),
        (9, 10), (9, 11), (9, 14),
        (10, 11), (10, 12),
        (11, 13),
        (12, 13), (12, 14),
        (13, 14)
    ]
    g.add_edges_from(edges)
    nx.draw_spring(g, with_labels=True)
    plt.show()
    return g


if __name__ == "__main__":
    g = create_custom_graph()
    print(g.degree)
    print(nx.normalized_laplacian_spectrum(g))
    gc = is_g_k_colorable.GraphColoring(g.number_of_nodes())
    gc.graph = nx.adjacency_matrix(g).toarray().tolist()
    print(gc.graph_coloring(m=3))
