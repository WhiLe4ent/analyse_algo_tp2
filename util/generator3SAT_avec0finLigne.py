# coding=utf-8

from random import random
from sys import argv


def generate3SAT(s, p, filename):

    listNeg = [-1,1]
    clauses = []
    for i in range(1,s+1):
        for j in range(i + 1, s+1):
            for k in range(j + 1, s+1):
                for sign_i in listNeg:
                    for sign_j in listNeg:
                        for sign_k in listNeg:
                            if random() < p:
                                clauses.append((sign_i * i, sign_j * j, sign_k * k))
    nb_clauses = len(clauses)

    with open(filename,'w') as file:
        file.write("c\n")
        file.write("c Random 3CNF with " + str(s) + " variables.\n")
        file.write("c Each clause appears with probability 7/8.\n")
        file.write("c\n")
        file.write("p cnf " + str(s) + " " + str(nb_clauses) + "\n")
        for e in clauses:
            file.write(str(e[0]) + " " + str(e[1]) + " " + str(e[2]) + " 0\n")



if __name__ == '__main__':
    if len(argv) <= 2:
        print("Usage: python generator3SAT.py <nb_variables> <output_file>")
        exit(1)

    try:
        size = int(argv[1])
    except TypeError:
        print("The first argument is the size of the graph and should be an integer.")
        exit(1)

    if size <= 1:
        print("The size of the graph should be larger than one.")
        exit(1)

    file_output = argv[2]

    generate3SAT(size, float(7/8), file_output)
