# coding=utf-8

import sys
from pycosat import solve as solveSAT
from pysat.card import *
from graph import *


def solveEnsInd(g, sizeI, versatile):
    """
    Resout EnsInd (Ensemble Independant) via SAT-solver.
    Tres similaire a Clique, mais on interdit les aretes au lieu de les exiger.
    """

    if versatile:
        print("Graphe d'entree")
        print(g)

    n = g.nb_vertices()  # nombre de noeuds du graphe

    """
    Pour chaque sommet u, on cree une variable booleenne x_u
    qui sera vraie ssi l'ensemble independant contient u
    """

    """
    On veut que l'ensemble independant soit de taille `sizeI'.
    """
    cnf = CardEnc.equals(lits=[i for i in range(1, n + 1)], bound=sizeI, top_id=n, encoding=EncType.seqcounter)

    """
    Pour chaque paire de sommets (u,v), si (u,v) EST une arete,
    on rajoute la contrainte qu'au plus une des extremites peut appartenir
    a l'ensemble independant.
    (Difference avec Clique: on interdit les aretes au lieu des non-aretes)
    """
    for u in range(1, n + 1):
        for v in range(1, u):
            if g.edges[u - 1][v - 1] == 1:  # S'il y a une arete
                cnf.append([-u, -v])

    if versatile:
        print("Entree pour le SAT solveur")
        print(cnf)

    solutionSAT = solveSAT(cnf)
    if versatile:
        print("Solution pour SAT")
        print(solutionSAT)

    if solutionSAT != "UNSAT":
        solution = [i-1 for i in solutionSAT[:n] if i > 0]
    else:
        solution = []
    return solution


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage : python3 EnsIndFromPycosat.py <filename> <size_ensind> [-v]")
        exit(1)
    filename = sys.argv[1]
    try:
        sizeI = int(sys.argv[2])
    except:
        print("Le deuxieme argument <size_ensind> doit etre un entier.")
        exit(1)
    if len(sys.argv) > 3 and (sys.argv[3] == "-v"
                              or sys.argv[3] == "--versatile"):
        versatile = True
    else:
        versatile = False

    g = Graph.initGraph(filename)

    solution = solveEnsInd(g, sizeI, versatile)

    print("Solution pour le probleme Ensemble Independant")
    if solution != []:
        print(solution)
    else:
        print("Pas d'ensemble independant de taille " + str(sizeI) + ".")
