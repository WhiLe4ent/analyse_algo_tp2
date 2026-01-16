# coding=utf-8

import sys
import os
from pycosat import solve as solveSAT
from pysat.card import *

sys.path.append(os.path.join(os.getcwd(), 'utils'))
from graph import Graph

def solveIndepSet(g, sizeI, versatile):
    """
    Résout le problème Ensemble Indépendant (Independent Set)
    """

    if versatile:
        print("Graphe d'entrée")
        print(g)

    n = g.nb_vertices()

    """
    Pour chaque sommet u, on crée une variable booléenne x_u (indices 1 à n)
    qui sera vraie ssi le sommet u fait partie de l'ensemble indépendant.
    """

    # On veut exactement 'sizeI' sommets sélectionnés
    # CardEnc génère des clauses pour dire "Somme(x_i) = sizeI"
    cnf = CardEnc.equals(lits=[i for i in range(1, n + 1)], bound=sizeI, top_id=n, encoding=EncType.seqcounter)

    """
    Pour chaque paire de sommets (u,v), si (u,v) EST une arête,
    alors u et v ne peuvent pas être pris en même temps.
    Clause : (NON u OU NON v)  =>  [-u, -v]
    """
    for u in range(1, n + 1):
        for v in range(1, u):
            if g.edges[u - 1][v - 1] == 1:
                cnf.append([-u, -v])

    if versatile:
        print("Entrée pour le SAT solveur")
        print(cnf)

    solutionSAT = solveSAT(cnf)
    
    if versatile:
        print("Solution brute SAT")
        print(solutionSAT)

    if solutionSAT != "UNSAT":
        solution = [i-1 for i in solutionSAT[:n] if i > 0]
    else:
        solution = []
    return solution   


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage : python3 EnsInd.py <filename> <size_indep_set> [-v]")
        exit(1)
        
    filename = sys.argv[1]
    
    try:
        sizeI = int(sys.argv[2])
    except:
        print("Le deuxième argument <size_indep_set> doit être un entier.")
        exit(1)
        
    versatile = False
    if len(sys.argv) > 3 and (sys.argv[3] == "-v" or sys.argv[3] == "--versatile"):
        versatile = True

    try:
        g = Graph.initGraph(filename)
        
        solution = solveIndepSet(g, sizeI, versatile)

        print("Solution pour le problème Ensemble Indépendant")
        if solution != []:
            print(f"Trouvé (taille {sizeI}) : {solution}")
        else:
            print(f"Pas d'ensemble indépendant de taille {sizeI}.")
            
    except FileNotFoundError:
        print(f"Erreur : Le fichier {filename} est introuvable.")
    except Exception as e:
        print(f"Erreur : {e}")