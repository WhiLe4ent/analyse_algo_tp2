# coding=utf-8

import sys
from graph import Graph
from src.biparti import est_biparti
from src.coloration import verifier_3coloration, resoudre_3col_backtracking


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage : python3 main.py <function> <filename> [coloration]")
        print("  functions: biparti, verifier, 3col")
        exit(1)

    function = sys.argv[1]
    filename = sys.argv[2]

    g = Graph.initGraph(filename)

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

        case _:
            print("Fonction non reconnue")
            print("  functions disponibles: biparti, verifier, 3col")
