# coding=utf-8

import sys
import time
from graph import Graph
from src.biparti import est_biparti
from src.coloration import verifier_3coloration, resoudre_3col_backtracking
from src.couverture_cliques import resoudre_3couverture_cliques


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage : python3 main.py <function> <filename> [options]")
        print("  functions: biparti, verifier, 3col, 3couv")
        print("  options: -time (affiche le temps de calcul)")
        exit(1)

    function = sys.argv[1]
    filename = sys.argv[2]
    show_time = "-time" in sys.argv

    g = Graph.initGraph(filename)

    start_time = time.time()

    match function:
        case "biparti":
            if est_biparti(g):
                print("Le graphe EST biparti (2-coloriable)")
            else:
                print("Le graphe N'EST PAS biparti")

        case "verifier":
            if len(sys.argv) < 4:
                print("usage: python3 main.py verifier <filename> <coloration>")
                print("  coloration format: 0,1,2,0,1,...")
                exit(1)
            couleurs = list(map(int, sys.argv[3].split(',')))
            coloration = {i: c for i, c in enumerate(couleurs)}
            if verifier_3coloration(g, coloration):
                print("Coloration VALIDE")
            else:
                print("Coloration INVALIDE")

        case "3col":
            solution = resoudre_3col_backtracking(g)
            if solution:
                print("Le graphe EST 3-coloriable")
                print(f"Coloration: {solution}")
            else:
                print("Le graphe N'EST PAS 3-coloriable")

        case "3couv":
            cliques = resoudre_3couverture_cliques(g)
            if cliques:
                print("Le graphe PEUT etre couvert par 3 cliques")
                for i, clique in enumerate(cliques):
                    print(f"  Clique {i+1}: {clique}")
            else:
                print("Le graphe NE PEUT PAS etre couvert par 3 cliques")

        case _:
            print("Fonction non reconnue")
            print("  functions disponibles: biparti, verifier, 3col, 3couv")

    if show_time:
        elapsed = time.time() - start_time
        print(f"Temps de calcul: {elapsed:.6f} secondes")
