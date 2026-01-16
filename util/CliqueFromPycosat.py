# coding=utf-8

import sys
from pycosat import solve as solveSAT
from pysat.card import *
from graph import *



def solveClique(g, sizeC, versatile):
    """
    Résout Clique
    """

    if versatile:
        print("Graphe d'entrée")
        print(g)

    n = g.nb_vertices()  # nombre de noeuds du graphe

    """
    Pour chaque sommet u, on crée une variable booléenne x_u
    qui sera vraie ssi la clique passe par u
    """

    """
    On veut que la clique soit de taille `size'.
    """
    cnf = CardEnc.equals(lits=[i for i in range(1, n + 1)], bound=sizeC, top_id=n, encoding=EncType.seqcounter)
    #cnf = counter([i for i in range(1, n + 1)], size, n + 1)

    """
    Pour chaque paire de sommets (u,v), si (u,v) n'est pas une arête,
    on rajoute la contrainte qu'une des extrémités ne doit pas appartenir
    à la clique.
    """
    for u in range(1, n + 1):
        for v in range(1, u):
            if g.edges[u - 1][v - 1] == 0:
                cnf.append([-u, -v])

    if versatile:
        print("Entrée pour le SAT solveur")
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
        print("usage : python3 CliqueFromPycosat.py <filename> <size_clique> [-v]")
        exit(1)
    filename = sys.argv[1]
    try:
        sizeC = int(sys.argv[2])
    except:
        print("Le deuxième argument <size_clique> doit être un entier.")
        exit(1)
    if len(sys.argv) > 3 and (sys.argv[3] == "-v"
                              or sys.argv[3] == "--versatile"):
        versatile = True
    else:
        versatile = False

    g = Graph.initGraph(filename)

    solution = solveClique(g, sizeC, versatile)

    print("Solution pour le problème Clique")
    if solution != []:
        print(solution)
    else:
        print("Pas de clique de taille " + str(sizeC) + ".")
