# coding=utf-8

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
import networkx as nx
sys.path.append(os.path.join(os.getcwd(), 'utils'))

from graph import Graph


def show_graph(g, title="Graphe"):
    """
    Affiche un graphe avec matplotlib et networkx.
    """
    G = nx.Graph()

    n = g.nb_vertices()
    G.add_nodes_from(range(n))

    for u in range(n):
        for v in range(u + 1, n):
            if g.is_edge(u, v):
                G.add_edge(u, v)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            node_size=500, font_size=12, font_weight='bold')
    plt.title(title)
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: python showGraph.py <graph_file>")
        exit(1)

    filename = sys.argv[1]
    g = Graph.initGraph(filename)
    show_graph(g, title=filename)
 