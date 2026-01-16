# coding=utf-8
from collections import deque


def est_biparti(graph):                             # -> O(n + n^2) = O(n^2)
    n = graph.nb_vertices()                             # O(1)
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
                if graph.edges[u][v] == 1:              # O(1)
                    if colors[v] == 0:              # O(1)
                        colors[v] = next_color      # O(1)
                        queue.append(v)             # O(1)
                    elif colors[v]==current_color:  # O(1)
                        return False                # O(1)

    return True                                     # O(1)
