import time
import string


class Node:

    def __init__(self, n):

        self.name = n
        self.related = []
        self.colour = "white"

    def add_relation(self, n):
        if n not in self.related:
            # appends the node to the related list and sorts it
            self.related.append(n)
            self.related.sort()


class Graph:

    nodes = {}
    # so we can find any node by its name

    # def add_node(self, node):
    def add_node(self, node):
        # combine letters and numbers to make nodes
        # check it doesnt already exist in the dictionary

        if node.name not in self.nodes:
            self.nodes[node.name] = node
            # self.nodes[node.colour] = "white"

    def get_nodes(self):
        return sorted(list(self.nodes.keys()))

    def add_edge(self, u, v):
        # needs the list of letters and numbers
        # check if the node is in nodes,
        # then calculate all the edges via the rules e.g. down1 left2, up2 right 1
        if u in self.nodes and v in self.nodes:
            # adds v to u's list of edges and vice versa
            self.nodes[u].add_relation(v)
            self.nodes[v].add_relation(u)

    def print_graph(self):
        print("this is the graph")
        for key in sorted(list(self.nodes.keys())):
            print(key + str(self.nodes[key].related))

    def dfs(self, n, route, u, limit):
        u.colour = "gray"
        route.append(u)
        if n < limit:
            connected = []
            for i in u.related:
                connected.append(g.nodes[i])

            i = 0
            done = False

            while i < len(connected) and not done:
                if connected[i].colour == "white":
                    done = self.dfs(n+1, route, connected[i], limit)

                i += 1

            if not done:
                u = route.pop()
                u.colour = "white"
        else:
            done = True

            x = 0
            while x < len(route):
                print(route[x].name)
                x += 1

        return done

g = Graph()

# gets a list of the alphabet characters in uppercase
sample_size = list(string.ascii_uppercase)


# create graph nodes
def createGraph(boardWidth):

    letters = []
    numbers = []

    for x in range(0, boardWidth):
        letters.append(sample_size[x])
        numbers.append(x+1)

    counter = 0

    # add nodes
    while counter < boardWidth:  # letter (adjust to board size)
        for y in range(0, boardWidth):
            g.add_node(Node(letters[counter]+str(numbers[y])))
        counter += 1
    return letters


def downTwoLeftOne(lettersList, currentLetter, number):
    # border cases
    if currentLetter == "A":
        return False
    if number <= 2:
        return False
    letterPosition = lettersList.index(currentLetter)
    newLetter = lettersList[letterPosition-1]
    number -= 2
    return newLetter+str(number)


def downTwoRightOne(lettersList, currentLetter, number):
    if number <= 2:
        return False
    letterPosition = lettersList.index(currentLetter)
    if letterPosition == len(lettersList)-1:
        return False
    newLetter = lettersList[letterPosition+1]
    number -= 2
    return newLetter+str(number)


def downOneLeftTwo(lettersList, currentLetter, number):
    letterPosition = lettersList.index(currentLetter)
    if letterPosition <= 1:
        return False
    if number < 2:
        return False
    newLetter = lettersList[letterPosition-2]
    number -= 1
    return newLetter+str(number)


def downOneRightTwo(lettersList, currentLetter, number):
    if number < 2:
        return False
    letterPosition = lettersList.index(currentLetter)
    if letterPosition >= len(lettersList)-2:
        return False
    newLetter = lettersList[letterPosition+2]
    number -= 1
    return newLetter+str(number)


def upTwoLeftOne(lettersList, currentLetter, number):
    if number >= len(lettersList)-2:
        return False
    if currentLetter == "A":
        return False
    letterPosition = lettersList.index(currentLetter)
    newLetter = lettersList[letterPosition-1]
    number += 2
    return newLetter+str(number)


def upTwoRightOne(lettersList, currentLetter, number):
    if number >= len(lettersList)-1:
        return False
    letterPosition = lettersList.index(currentLetter)
    if letterPosition >= len(lettersList)-1:
        return False
    newLetter = lettersList[letterPosition+1]
    number += 2
    return newLetter+str(number)


def upOneLeftTwo(lettersList, currentLetter, number):
    if number >= len(lettersList):
        return False
    letterPosition = lettersList.index(currentLetter)
    if letterPosition <= 1:  # if we get an "A" or a "B"
        return False
    newLetter = lettersList[letterPosition-2]
    number += 1
    return newLetter+str(number)


def upOneRightTwo(lettersList, currentLetter, number):
    if number >= len(lettersList):
        return False
    letterPosition = lettersList.index(currentLetter)
    if letterPosition >= len(lettersList)-2:
        return False
    newLetter = lettersList[letterPosition+2]
    number += 1
    return newLetter+str(number)


def make_edges(nodeList, letters):

    for n in range(0, len(nodeList)-1):
        if downTwoLeftOne(letters, nodeList[n][:1], int(nodeList[n][1:])) != False:
            g.add_edge(nodeList[n], downTwoLeftOne(letters, nodeList[n][:1], int(nodeList[n][1:])))
        if downTwoRightOne(letters, nodeList[n][:1], int(nodeList[n][1:])) != False:
            g.add_edge(nodeList[n], downTwoRightOne(letters, nodeList[n][:1], int(nodeList[n][1:])))
        if downOneLeftTwo(letters, nodeList[n][:1], int(nodeList[n][1:])) != False:
            g.add_edge(nodeList[n], downOneLeftTwo(letters, nodeList[n][:1], int(nodeList[n][1:])))
        if downOneRightTwo(letters, nodeList[n][:1], int(nodeList[n][1:])) != False:
            g.add_edge(nodeList[n], downOneRightTwo(letters, nodeList[n][:1], int(nodeList[n][1:])))

        if upTwoLeftOne(letters, nodeList[n][:1], int(nodeList[n][1:])) != False:
            g.add_edge(nodeList[n], upTwoLeftOne(letters, nodeList[n][:1], int(nodeList[n][1:])))
        if upTwoRightOne(letters, nodeList[n][:1], int(nodeList[n][1:])) != False:
            g.add_edge(nodeList[n], upTwoRightOne(letters, nodeList[n][:1], int(nodeList[n][1:])))
        if upOneLeftTwo(letters, nodeList[n][:1], int(nodeList[n][1:])) != False:
            g.add_edge(nodeList[n], upOneLeftTwo(letters, nodeList[n][:1], int(nodeList[n][1:])))
        if upOneRightTwo(letters, nodeList[n][:1], int(nodeList[n][1:])) != False:
            g.add_edge(nodeList[n], upOneRightTwo(letters, nodeList[n][:1], int(nodeList[n][1:])))

g.print_graph()
route = []
board = 7
lettersList = createGraph(board)
nodeList = g.get_nodes()
make_edges(nodeList, lettersList)
g.print_graph()
start = time.time()
nodes = g.dfs(1, route, g.nodes["A1"], board*board)
end = time.time()
print(">this is the time taken: " + str(end - start))
nodeList = []
print(nodes)
