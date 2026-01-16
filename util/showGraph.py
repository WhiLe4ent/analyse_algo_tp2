import networkx as nx
import matplotlib.pyplot as plt

def read_dimacs_graph(path):
    G = nx.Graph()

    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("c"):
                continue

            parts = line.split()

            if parts[0] == "p":
                # p edge nb_vertices nb_edges
                n = int(parts[2])
                G.add_nodes_from(range(n))

            elif parts[0] == "e":
                _, u, v = parts
                G.add_edge(int(u), int(v))

    return G


# -------- UTILISATION --------
G = read_dimacs_graph("graph.dimacs")

plt.figure(figsize=(4, 4))
pos = nx.spring_layout(G, seed=42)  # layout automatique (pas Graphviz)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=800,
    node_color="lightblue",
    edge_color="gray",
    font_size=12
)

plt.savefig("graph.png", dpi=200)
plt.show()
