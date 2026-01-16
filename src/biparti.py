# coding=utf-8
from collections import deque


def est_biparti(graph):
    """
    Teste si un graphe est biparti (2-coloriable) via BFS.
    Complexite totale: O(V^2) car matrice d'adjacence
    """
    n = graph.nb_vertices()  # O(1)
    if n == 0:  # O(1)
        return True  # O(1)

    couleurs = [-1] * n  # O(V)

    for start in range(n):  # O(V) iterations
        if couleurs[start] != -1:  # O(1)
            continue  # O(1)

        file = deque([start])  # O(1)
        couleurs[start] = 0  # O(1)

        while file:  # O(V) iterations au total
            u = file.popleft()  # O(1)
            for v in range(n):  # O(V)
                if not graph.is_edge(u, v):  # O(1)
                    continue  # O(1)
                if couleurs[v] == -1:  # O(1)
                    couleurs[v] = 1 - couleurs[u]  # O(1)
                    file.append(v)  # O(1)
                elif couleurs[v] == couleurs[u]:  # O(1)
                    return False  # O(1)

    return True  # O(1)
