import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'utils'))
from graph import Graph

def is_valid_3coloring(g, color):    # Complexité Totale : O(n^2)
    n = g.nb_vertices()         
    
    for u in range(n):               # O(n)
        if color[u] not in {1,2,3}:
            return False        

        for v in range(n):           # O(n)
            if g.edges[u][v] == 1:
                if color[u] == color[v]:
                    return False

    return True


def is_consistent(g, colors, i):     # Complexité Totale : O(n)
    n = g.nb_vertices()         
    for j in range(n):               # O(n)
        if g.edges[i][j] == 1 and colors[i] == colors[j]:
            return False        
    return True


def backtrack_3col(g, colors, i):           # Complexité Totale : O(n * 3^n)
    n = g.nb_vertices()

    if i == n:
        return True

    for c in [1, 2, 3]:                     # O(3)
        colors[i] = c

        if is_consistent(g, colors, i):     # O(n)
            if backtrack_3col(g, colors, i + 1): # T(n-1)
                return True

        colors[i] = 0      

    return False           


def get_complement_graph(g): # O(n^2)
    """
    Construit le graphe complémentaire G_barre.
    """
    n = g.nb_vertices()        
    g_bar = Graph(n)                # O(n^2)
    
    for i in range(n):              # O(n)
        for j in range(i + 1, n):   # O(n/2) 
            if not g.is_edge(i, j):
                g_bar.add_edge(i, j)
            
    return g_bar   


def solve3CouvertureParCliques(g, versatile=False): # Complexité Totale : O(n * 3^n)
    """
    Résout le problème en réduisant vers 3-Coloration.
    """
    if versatile:
        print("...")

    g_bar = get_complement_graph(g) # O(n^2)
    
    n = g.nb_vertices()
    colors = [0] * n                # O(n)
    
    if versatile:
        print("...")

    if backtrack_3col(g_bar, colors, 0): # O(n * 3^n)
        clique1 = [i for i, c in enumerate(colors) if c == 1] # O(n)
        clique2 = [i for i, c in enumerate(colors) if c == 2] # O(n)
        clique3 = [i for i, c in enumerate(colors) if c == 3] # O(n)
        
        return [clique1, clique2, clique3] 
    else:
        return None

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage : python3 ens3.py <filename> [-v]")
        exit(1)
        
    filename = sys.argv[1]
    versatile = "-v" in sys.argv

    try:
        g = Graph.initGraph(filename)
        
        cliques = solve3CouvertureParCliques(g, versatile)

        if cliques:
            print("Le graphe PEUT être couvert par 3 cliques.")
            print(f"Clique 1 : {cliques[0]}")
            print(f"Clique 2 : {cliques[1]}")
            print(f"Clique 3 : {cliques[2]}")
        else:
            print("Le graphe NE PEUT PAS être couvert par 3 cliques.")
            
    except FileNotFoundError:
        print(f"Erreur : Le fichier {filename} est introuvable.")
    except Exception as e:
        print(f"Erreur : {e}")