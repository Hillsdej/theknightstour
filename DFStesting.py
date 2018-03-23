# import time
# start = time.time()

# def boardBuilder(width, height):
#     board = []
#     square = []
#     for i in range(0,width):
#         square.append(i)
#     for j in range(0, height):
#         board.append(square)
#     return board

# print(boardBuilder(8, 8))

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

    def add_node(self, node):
        
        #check it doesnt already exist in the dictionary
        if node.name not in self.nodes:
            self.nodes[node.name] = node
            self.nodes[node.colour] = node

    

    def add_edge(self,u,v):
        if u in self.nodes and v in self.nodes:
            #adds v to u's list of edges and vice versa
            self.nodes[u].add_relation(v)
            self.nodes[v].add_relation(u)


    def print_graph(self):
        print("this is the graph")
        for key in sorted(list(self.nodes.keys())):
            print(key + str(self.nodes[key].related))

    def dfs(self, n, route, u, limit):
        print("----------------------------------------------------------------------------------------")
        print("this is n: " + str(n))
        print("this is u: " + str(u.name))
        u.colour = "gray"
        route.append(u)
        j = 0
        while j < len(route):
            print(route[j].name)
            j += 1

        #print("this is the length of the path: " + str(len(route)))
        if n < limit:
            connected = []
            print("this is u when after n < limit: " + u.name)
            for i in u.related:
                print("this is the name when it enters the for: " + u.name)
                #print(g.nodes[i].name)
                print(g.nodes[i].name)
                connected.append(g.nodes[i])
                
            i = 0
            #print("this is done before assignment: " + str(done))
            done = False
         #   print("this is done after assignment: " + str(done))

            while i < len(connected) and not done:
                print("this is the name in the while loop " + u.name)
                print(connected[i].name + " " + connected[i].colour)
          #      print("entered for sure")
                if connected[i].colour == "white":
                    print("entered if with " + u.name + " as u" )
                    print("this is the connected node: " + connected[i].name + " " + connected[i].colour)
                    done = self.dfs(n+1, route, connected[i], limit)
                
                i += 1
           #     print("this is i: " + str(i))

                        

                #print(done)
            if not done:
                #   print("entering?")
                # for k in route:
                #     route[i].colour = "white"
                u = route.pop()
                print("this is the route after its been popped: " + str(len(route)))
                print("this is where it restarts " + str(u.name))
                u.colour = "white"
                #self.dfs(0, route, u, limit)
        else:
            done = True


        print("------------------------>>>>>>>>this is the status of done: " + str(done))
        x = 0 
        while x < len(route):
            print(route[x].name)
            x += 1
      
        return done
        #return len(route)
    
g = Graph()

## examples of adding singular nodes
## a = Node('A')
## g.add_node(a)
## g.add_node(Node('B'))

import string
sample_size = list(string.ascii_uppercase) #gets a list of the alphabet characters in uppercase

for i in range(0,12):
    g.add_node(Node(sample_size[i]))

edges = ['AG','AF','AI','BC','BH','BJ','CI','CK','DJ','DL','EG','EK','FH','FL','GL','JK']
#edges = ['AB', 'AD', 'BC', 'BD', 'DE', 'EF', 'FC']

for edge in edges:
    g.add_edge(edge[:1], edge[1:])

route = [] 
nodes = g.dfs(1,route,g.nodes["A"],12)
print(nodes)
# with open("dfs_output.txt", "w") as f:
# for i in nodes:
#     print(i.name)
#     #print("\n")
# g.print_graph()



            
        
