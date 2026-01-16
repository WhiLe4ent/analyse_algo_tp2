# coding=utf-8

import sys
from graph import *




if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage : python3 votreFonction.py <filename> [autres arguments?]")
        exit(1)
    filename = sys.argv[1]

    g = Graph.initGraph(filename)

        ## Appel à la fonction principale

