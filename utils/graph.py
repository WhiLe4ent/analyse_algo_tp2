# coding=utf-8

class Graph:

    def __init__(self, nb_vertices, edges=None):
        """
        Structure d'un noeud
        :param nodes: nom du noeud
        :param edges: liste des arêtes
        """
        self.size = nb_vertices
        if edges is None:
            edges = [[0 for x in range(nb_vertices)]
                     for y in range(nb_vertices)]
        self.edges = edges

    def copy(self):
        return Graph(self.size, self.edges)

    def nb_vertices(self):
        return self.size

    def listEdges(self):
        listEdges = []
        n = self.size
        for i in range(n):
            for j in range(i + 1, n):
                if self.edges[i][j] == 1:
                    listEdges.append((i, j))
        return listEdges

    def add_edge(self, i1, i2):
        self.edges[i1][i2] = 1
        self.edges[i2][i1] = 1

    def remove_edge(self, i1, i2):
        self.edges[i1][i2] = 0
        self.edges[i2][i1] = 0

    def is_edge(self, i1, i2):
        if self.edges[i1][i2] == 1:
            return True
        else:
            return False

    @staticmethod
    def initGraph(filename):
        """
        Initialise un graphe en fonction d'un fichier
        :param filename: nom du fichier
        :return: le graphe créé
        """
        with open(filename, "r") as file:  # Open the file in read mode
            line = file.readline().strip()
            while line[0] == 'c':
                line = file.readline().strip()

            firstLine = line.split(" ")
            if firstLine[0] != 'p' or firstLine[1] != 'edge':
                print("The first non-commentary line should be 'p edge N E' \
                       where N and E are the number of vertices and edges.")
                exit(1)
            nb_vertices = int(firstLine[2])

            g = Graph(nb_vertices)
            for line in file:
                line = line.strip()
                if line[0] == "c":
                    continue
                link = line.split(" ")
                Graph.add_edge(g, int(link[1]), int(link[2]))
        return g

    def __str__(self):
        return "Nodes : " + str(list(range(self.size))) + " Edges : " + str(self.edges)

    def __repr__(self):
        return self.name
