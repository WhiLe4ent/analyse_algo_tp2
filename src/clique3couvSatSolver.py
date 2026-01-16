# coding=utf-8

import sys
import os
from pycosat import solve as solveSAT

sys.path.append(os.path.join(os.getcwd(), 'utils'))
from graph import Graph


def get_complement_graph(g):          # O(n^2)
    n = g.nb_vertices()
    g_bar = Graph(n)

    for i in range(n):
        for j in range(i + 1, n):
            if not g.is_edge(i, j):
                g_bar.add_edge(i, j)

    return g_bar


def solve3ColorSat(g, versatile=False):
    """
    Résout 3-COLORATION via une réduction SAT.
    """
    n = g.nb_vertices()
    cnf = []

    def var(v, c):
        return 3 * v + c + 1

    for v in range(n):
        cnf.append([var(v, 0), var(v, 1), var(v, 2)])

    for v in range(n):
        cnf.append([-var(v, 0), -var(v, 1)])
        cnf.append([-var(v, 0), -var(v, 2)])
        cnf.append([-var(v, 1), -var(v, 2)])

    for u in range(n):
        for v in range(u):
            if g.edges[u][v] == 1:
                for c in range(3):
                    cnf.append([-var(u, c), -var(v, c)])

    if versatile:
        print("Formule SAT (CNF) :")
        print(cnf)

    sol = solveSAT(cnf)

    if sol == "UNSAT":
        return None

    colors = [0] * n
    for v in range(n):
        for c in range(3):
            if var(v, c) in sol:
                colors[v] = c + 1

    return colors


def solve3CouvertureParCliques(g, versatile=False):
    """
    Résout la couverture par 3 cliques
    via réduction vers 3-COLORATION + SAT.
    """
    if versatile:
        print("Construction du graphe complémentaire")

    g_bar = get_complement_graph(g)

    if versatile:
        print("Résolution 3-COLORATION via SAT")

    colors = solve3ColorSat(g_bar, versatile)

    if colors is None:
        return None

    clique1 = [i for i, c in enumerate(colors) if c == 1]
    clique2 = [i for i, c in enumerate(colors) if c == 2]
    clique3 = [i for i, c in enumerate(colors) if c == 3]

    return [clique1, clique2, clique3]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage : python3 ens3.py <filename> [-v]")
        exit(1)

    filename = sys.argv[1]
    versatile = "-v" in sys.argv or "--versatile" in sys.argv

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
