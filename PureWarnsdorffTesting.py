import time


class Node:

    def __init__(self, label):
        self.label = label


class Graph:

    nodes = {}       # used to find a node by its label
    matrix = []      # contains 2D array of edges
    edge_index = {}  # the index of an edge given its label
    visited = []  # stores all the squares that have been visited
    related = []  # stores the squares that are adjacent to the current square
    pathNum = 1
    rowLength = 8
    columnLength = 8

    def add_node(self, node):
        # if it is a node and not in the node list
        if node.label not in self.nodes:
            self.nodes[node.label] = node
            for row in self.matrix:
                row.append(0)
            self.matrix.append([0] * (len(self.matrix)+1))
            self.edge_index[node.label] = len(self.edge_index)
            return True
        else:
            return False

    def add_edge(self, u, v, weight):
        # knightMovesDict to see if nodes u and v are in the node dictionary
        if u in self.nodes and v in self.nodes:
            self.matrix[self.edge_index[v]][self.edge_index[u]] = weight
            self.visited.append((u, v))

        """
        To represent an edge between nodes:
        (u,v) changes to store a 1
        (v,u) changes to store a 1
        """

    def print_graph(self):
        print("<<<<<<<<<< Knight Tour WARNSDORFF >>>>>>>>>>>")
        print("")
        singleNums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for v, i in sorted(self.edge_index.items()):
            print(str(v) + ' ', end='')
            for j in range(len(self.matrix)):
                if self.matrix[i][j] in singleNums:
                    print(self.matrix[i][j], end='  |')
                else:
                    print(self.matrix[i][j], end=' |')
            print(' ')

    def countAvailableMoves(self, array):
        counter = 0
        i = 1

        while i <= len(array):
            if array[i] != None:
                if (array[i]["startX"], array[i]["startY"]) not in self.visited:
                    counter += 1
                    i += 1
            else:
                i += 1

        return counter

    def warnsdorff(self, startX, startY, depth=0, moveType=None):

        if depth == 0:
            self.add_edge(startX, startY, self.pathNum)

        if len(self.visited) <= (self.rowLength*self.columnLength):
            # Look in all directions for knight moves

            knightMovesDict = dict()
            knightMovesDict[1] = upTwoRightOne(startX, startY)
            knightMovesDict[2] = upOneRightTwo(startX, startY)
            knightMovesDict[3] = downOneRightTwo(startX, startY)
            knightMovesDict[4] = downTwoRightOne(startX, startY)
            knightMovesDict[5] = downTwoLeftOne(startX, startY)
            knightMovesDict[6] = downOneLeftTwo(startX, startY)
            knightMovesDict[7] = upOneLeftTwo(startX, startY)
            knightMovesDict[8] = upTwoLeftOne(startX, startY)

            kmdCounter = 1

            while kmdCounter <= len(knightMovesDict):

                if knightMovesDict[kmdCounter] != None:
                    # legal move found
                    adjacentNodeX = knightMovesDict[kmdCounter]["startX"]
                    adjacentNodeY = knightMovesDict[kmdCounter]["startY"]

                    if depth == 1:
                        # count the number of available moves
                        # the adjacent unvisited square has
                        numberAvailableMoves = self.countAvailableMoves(knightMovesDict)

                        self.related.append({"startX": startX, "startY": startY, "degree": numberAvailableMoves, "moveType": moveType})

                        return

                    else:
                        # look at the adjacent unvisited square
                        self.warnsdorff(adjacentNodeX, adjacentNodeY, depth+1, moveType=knightMovesDict[kmdCounter]["moveType"])
                        kmdCounter += 1

                else:
                    kmdCounter += 1

            sortedRelated = bubbleSort(self.related)
            relatedCounter = 0

            while relatedCounter < len(sortedRelated):
                nextX = sortedRelated[relatedCounter]["startX"]
                nextY = sortedRelated[relatedCounter]["startY"]
                if (nextX, nextY) not in self.visited:
                    self.related = []
                    self.pathNum += 1
                    self.warnsdorff(nextX, nextY)
                else:
                    relatedCounter += 1
        return self.visited

g = Graph()


# KNIGHT DIRECTIONS

# moveType 1
def upTwoRightOne(u, v):
    if u < g.rowLength-1 and v > 1:
        if (u+1, v-2) not in g.visited:
            return {"startX": u+1, "startY": v-2, "moveType": 1}
    return None


# moveType 2
def upOneRightTwo(u, v):
    if u < g.rowLength-2 and v > 0:
        if (u+2, v-1) not in g.visited:
            return {"startX": u+2, "startY": v-1, "moveType": 2}
    return None


# moveType 3
def downOneRightTwo(u, v):
    if u < g.rowLength-2 and v < g.columnLength-1:
        if (u+2, v+1) not in g.visited:
            return {"startX": u+2, "startY": v+1, "moveType": 3}
    return None


# moveType 4
def downTwoRightOne(u, v):
    if u < g.rowLength-1 and v < g.columnLength-2:
        if (u+1, v+2) not in g.visited:
            return {"startX": u+1, "startY": v+2, "moveType": 4}
    return None


# moveType 5
def downTwoLeftOne(u, v):
    if u > 0 and v < g.columnLength-2:
        if (u-1, v+2) not in g.visited:
            return {"startX": u-1, "startY": v+2, "moveType": 5}
    return None


# moveType 6
def downOneLeftTwo(u, v):
    if u > 1 and v < g.columnLength-1:
        if (u-2, v+1) not in g.visited:
            return {"startX": u-2, "startY": v+1, "moveType": 6}
    return None


# moveType 7
def upOneLeftTwo(u, v):
    if u > 1 and v > 0:
        if (u-2, v-1) not in g.visited:
            return {"startX": u-2, "startY": v-1, "moveType": 7}
    return None


# moveType 8
def upTwoLeftOne(u, v):
    if u > 0 and v > 1:
        if (u-1, v-2) not in g.visited:
            return {"startX": u-1, "startY": v-2, "moveType": 8}
    return None


def bubbleSort(array):

    if len(array) <= 1:
        return array

    notSorted = True

    while notSorted == True:

        notSorted = False

        for i in range(0, len(array)-1):

            if array[i]["degree"] > array[i+1]["degree"]:
                array[i], array[i+1] = array[i+1], array[i]
                notSorted = True

    return array


for i in range(0, g.rowLength):
    g.add_node(Node(i))

start = time.time()
g.warnsdorff(0, 0)
end = time.time()
print(">this is the time taken: " + str(end - start))
g.print_graph()
print(str(g.visited))
