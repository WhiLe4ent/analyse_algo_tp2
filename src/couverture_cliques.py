# coding=utf-8

from graph import Graph
from src.coloration import backtrack_3col


def graphe_complementaire(g):
    """
    Construit le graphe complementaire de g.
    G' a une arete (u,v) ssi G n'a pas d'arete (u,v).
    Complexite: O(V^2)
    """
    n = g.nb_vertices()
    g_comp = Graph(n)

    for u in range(n):
        for v in range(u + 1, n):
            if not g.is_edge(u, v):
                g_comp.add_edge(u, v)

    return g_comp


def resoudre_3couverture_cliques(g):
    """
    Resout 3CouvertureParCliques via reduction a 3Col.

    Observation: si G est 3-colorie, les sommets de meme couleur forment
    un ensemble independant dans G, donc une clique dans G' (complementaire).

    Donc: 3CouvertureParCliques(G) <=> 3Col(G')

    Retourne les 3 cliques si possible, None sinon.
    Complexite: O(3^V) (backtracking sur le complementaire)
    """
    # Construire le graphe complementaire
    g_comp = graphe_complementaire(g)
    n = g_comp.nb_vertices()

    # Resoudre 3Col sur le complementaire
    colors = [0] * n
    if not backtrack_3col(g_comp, colors, 0):
        return None

    # Extraire les 3 cliques (sommets de meme couleur)
    cliques = [[], [], []]
    for sommet in range(n):
        cliques[colors[sommet] - 1].append(sommet)

    return cliques
