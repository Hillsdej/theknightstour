# import time
# start = time.time()
# end = time.time()
# print(end - start)

class Node:

    def __init__(self, n):

        self.name = n
        self.related = []
        self.colour = "white"

    def add_relation(self, n):
        if n not in self.related:
            #appends the node to the related list and sorts it
            self.related.append(n)
            self.related.sort()


class Graph:

    nodes = {}
    #so we can find any node by its name

    # def add_node(self, node):
    def add_node(self, node):
        #combine letters and numbers to make nodes
        #check it doesnt already exist in the dictionary
        #for letter in letters add new node + number
        if node.name not in self.nodes:
            self.nodes[node.name] = node
            self.nodes[node.colour] = node

    def add_edge(self,u,v):
        #needs the list of letters and numbers
        #check if the node is in nodes, then calculate all the edges via the rules e.g. down1 left2, up2 right 1  
        if u in self.nodes and v in self.nodes:
            #adds v to u's list of edges and vice versa
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

## examples of adding singular nodes
## a = Node('A')
## g.add_node(a)
## g.add_node(Node('B'))
## g.add_node(Node('A1'))

import string
sample_size = list(string.ascii_uppercase) #gets a list of the alphabet characters in uppercase
letters = []
numbers = []
for x in range(0,4):
    letters.append(sample_size[x])
    numbers.append(x+1)

counter = 0

while counter < 4: #letter
    for y in range(0,4):
        g.add_node(Node(letters[counter]+str(numbers[y])))
    counter += 1
 
#edges = ['AG','AF','AI','BC','BH','BJ','CI','CK','DJ','DL','EG','EK','FH','FL','GL','JK']
    
# for edge in edges:
#     print(edge[:1], edge[1:])
    # g.add_edge(edge[:1], edge[1:])

g.add_edge("B4","D3")
g.add_edge("D3","B4")
# route = [] 
# nodes = g.dfs(1,route,g.nodes["A"],12)
# print(nodes)
g.print_graph()


