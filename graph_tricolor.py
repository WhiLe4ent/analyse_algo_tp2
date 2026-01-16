import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'utils'))
from graph import Graph

def is_valid_3coloring(g, color):    # O(n^2) -> polynomiale
    n = g.nb_vertices()              # O(1)

    for u in range(n):               # O(n)
        if color[u] not in {1,2,3}:  # O(1)
            return False

        for v in range(n):           # O(n)
            if g.edges[u][v] == 1:   # O(1)
                if color[u] == color[v]:
                    return False

    return True

def backtrack_3col(g, colors, i):           # O(3^n * n) -> exponential
    n = g.nb_vertices()                     # O(1)

    if i == n:                              # O(1)
        return True                         # O(1)

    for c in [1, 2, 3]:                     # O(3)
        colors[i] = c                       # O(1)

        if is_consistent(g, colors, i):     # O(n)
            if backtrack_3col(g, colors, i + 1):
                return True

        colors[i] = 0                       # O(1)

    return False


def is_consistent(g, colors, i):
    for j in range(g.nb_vertices()):  # O(n)
        if g.edges[i][j] == 1 and colors[i] == colors[j]:
            return False
    return True





# Quand même mieux d'avoir une liste
def build_adjacency_and_order(g):
    n = g.nb_vertices()
    adj = [[] for _ in range(n)]
    degrees = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            if g.edges[i][j] == 1:
                adj[i].append(j)
                adj[j].append(i)
                degrees[i] += 1
                degrees[j] += 1
    
    nodes_order = sorted(range(n), key=lambda x: degrees[x], reverse=True)
    
    return adj, nodes_order

def is_consistent_optimized(u, c, colors, adj):
    for v in adj[u]:
        if colors[v] == c:
            return False
    return True

def backtrack_3col_opti(idx, colors, adj, nodes_order):
    if idx == len(nodes_order):
        return True

    u = nodes_order[idx]

    for c in [1, 2, 3]:
        if is_consistent_optimized(u, c, colors, adj):
            colors[u] = c
            
            if backtrack_3col_opti(idx + 1, colors, adj, nodes_order):
                return True
            
            colors[u] = 0

    return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python 3coloration.py <filename>")
        exit(1)

    filename = sys.argv[1]

    try:
        g = Graph.initGraph(filename)
        n = g.nb_vertices()
        colors = [0] * n

        adj, nodes_order = build_adjacency_and_order(g)

        first_node = nodes_order[0]
        colors[first_node] = 1
        
        if backtrack_3col_opti(1, colors, adj, nodes_order):
            print("Le graphe EST 3-coloriable.")
            print("Coloration trouvée :", colors)
        else:
            print("Le graphe N'est PAS 3-coloriable.")

    except FileNotFoundError:
        print(f"Erreur : fichier {filename} introuvable.")
    except Exception as e:
        print(f"Erreur : {e}")