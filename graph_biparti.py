import sys

from matplotlib import colors
import os
sys.path.append(os.path.join(os.getcwd(), 'utils'))
from graph import Graph
from collections import deque

def isGraphBiparti(g):                              # -> O(n + n^2) = O(n^2)
    n = g.nb_vertices()                             # O(1)
    colors = [0] * n                                # O(n)

    for start_node in range(n):                     # O(n)
        if colors[start_node] != 0:                 # O(1) bfs une seule fois / node
            continue

        queue = deque([start_node])                 # O(1)
        colors[start_node] = 1                      # O(1)

        while queue:                                # O(n)
            u = queue.popleft()                     # O(1)
            current_color = colors[u]               # O(1)
            next_color = -current_color             # O(1)

            for v in range(n):                      # O(n)
                if g.edges[u][v] == 1:              # O(1)
                    if colors[v] == 0:              # O(1)
                        colors[v] = next_color      # O(1)
                        queue.append(v)             # O(1)
                    elif colors[v]==current_color:  # O(1)
                        return False                # O(1)

    return True                                     # O(1)

# Le temps de calcul correspond bien à la complexité O(n^2) attendue.
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python checkBipartite.py <filename>")
        exit(1)
        
    filename = sys.argv[1]

    try:
        g = Graph.initGraph(filename)
        is_bipartite = isGraphBiparti(g)
        
        if is_bipartite:
            print(f"The graph in {filename} IS bipartite.")
        else:
            print(f"The graph in {filename} is NOT bipartite.")
            
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")