# coding=utf-8


def verifier_3coloration(graph, coloration):
    """
    Verifie si une coloration est une 3-coloration valide.
    Complexite totale: O(V + E)
    """
    n = graph.nb_vertices()  # O(1)

    for sommet in range(n):  # O(V) iterations
        if sommet not in coloration:  # O(1)
            return False  # O(1)
        if coloration[sommet] not in {0, 1, 2}:  # O(1)
            return False  # O(1)

    for u in range(n):  # O(V) iterations
        for v in range(n):  # O(V) iterations
            if graph.is_edge(u, v):  # O(1)
                if coloration[u] == coloration[v]:  # O(1)
                    return False  # O(1)

    return True  # O(1)


def resoudre_3col_backtracking(graph):
    """
    Resout 3-Col via backtracking.
    Complexite totale: O(3^V) dans le pire cas
    """
    n = graph.nb_vertices()  # O(1)
    coloration = {}  # O(1)

    def est_coherent(sommet, couleur):  # O(V) par appel
        for voisin in range(n):  # O(V) iterations
            if graph.is_edge(sommet, voisin):  # O(1)
                if voisin in coloration and coloration[voisin] == couleur:  # O(1)
                    return False  # O(1)
        return True  # O(1)

    def backtrack(sommet):  # Appele jusqu'a 3^V fois
        if sommet == n:  # O(1)
            return True  # O(1)

        for couleur in range(3):  # 3 iterations
            if est_coherent(sommet, couleur):  # O(V)
                coloration[sommet] = couleur  # O(1)
                if backtrack(sommet + 1):  # Recursion
                    return True  # O(1)
                del coloration[sommet]  # O(1)

        return False  # O(1)

    if backtrack(0):  # O(3^V) dans le pire cas
        return coloration  # O(1)
    return None  # O(1)
