class Node:
    
    def __init__(self, label):
        self.label = label
        
class Graph:
    
    nodes = {}      # used to find a node by its label
    matrix = []     # contains 2D array of edges
    edge_index = {} # used to check the index of an edge given its label
    visited = []
    related = []
    
    def add_node(self, node):
        #first check if it is a node and not in the node list
        #if not then you add it to the dictionary of nodes
        
        if node.label not in self.nodes:
            self.nodes[node.label] = node
            for row in self.matrix:
                row.append(0)
            self.matrix.append([0] * (len(self.matrix)+1))
            self.edge_index[node.label] = len(self.edge_index)
            return True
        else:
            return False
            
    def add_edge(self,u, v, weight):
        #check to see if nodes u and v are in the node dictionary
        if u in self.nodes and v in self.nodes:
            #self.matrix[self.edge_index[u]][self.edge_index[v]] = weight
            self.matrix[self.edge_index[v]][self.edge_index[u]] = weight
            self.visited.append((u,v))
            
        """ 
        To represent an edge between nodes:
        (u,v) changes to store a 1
        (v,u) changes to store a 1
        """
    def print_graph(self):
        print("  01234567")
        for v, i in sorted(self.edge_index.items()):
            print(str(v) + ' ', end='')
            for j in range(len(self.matrix)):
                print(self.matrix[i][j], end='')
            print(' ')
    
    def warnsfdorff(self,startX,startY,depth=0):
        
        if depth > 1:
            return
        
        check = dict()
        check[1]= upTwoRightOne(startX,startY)
        check[2]= upOneRightTwo(startX,startY)
        check[3]= downOneRightTwo(startX,startY)
        check[4]= downTwoRightOne(startX,startY)
        check[5]= downTwoLeftOne(startX,startY)
        check[6]= downOneLeftTwo(startX,startY)
        check[7]= upOneLeftTwo(startX,startY)
        check[8]= upTwoLeftOne(startX,startY)
        
        if depth == 0:
            self.add_edge(startX, startY, 1)
      
        loopCounter = 1
        degree = 0
        
        #list of next available moves in order of their degree
        
        while loopCounter <= len(check):
            if check[loopCounter] != None:
                degree += 1
                self.warnsfdorff(check[loopCounter]["startX"], check[loopCounter]["startY"], depth+1)
            loopCounter += 1
        
        
        print("STARTx: " + str(startX) + " STARTy: " + str(startY) + " ---- THIS IS THE DEGREE: " + str(degree))
        
        if (startX,startY) not in self.visited:
            self.related.append({"startX":startX, "startY":startY, "degree":degree}) #need moveType in here
        
        for i in check:
            if check[i] != None:
                for j in range(0, len(self.related)):
                    if check[i]["startX"] == self.related[j]["startX"] and check[i]["startY"] == self.related[j]["startY"]:
                        self.related[j]["moveType"]=check[i]["moveType"]
        
        print(self.related)
        #self.related.sort()
        #sorted(self.related, key=lambda d: d['degree'])
        #print(str(len(self.visited)))
        #now sort by degree and then pick the first one with the lowest degree and mark as visited
        #need a base case if length of visited != 63 and if visited startX and startY aren't in visited
        #actually dont need to return the moveType as the key of check is already the moveType
        

g = Graph()

for i in range(0,8):
    g.add_node(Node(i))

#KNIGHT DIRECTIONS

#moveType 1
def upTwoRightOne(u, v):
    # isVisited = (u, v)
    # if isVisited not in g.visited:
    if u < 7 and v > 1:
        if (u+1, v-2) not in g.visited:
        #g.add_edge(u+1, v-2, weight)
            return {"startX":u+1, "startY":v-2, "moveType":1}
    return None

#moveType 2
def upOneRightTwo(u, v):
    #isVisited = (u, v)
    #if isVisited not in g.visited:
    if u < 6 and v > 0:
        if (u+2, v-1) not in g.visited:
                #g.add_edge(u+2, v-1, weight)
            return {"startX":u+2, "startY":v-1, "moveType":2}
    return None
    

#moveType 3
def downOneRightTwo(u, v):
    # isVisited = (u, v)
    # if isVisited not in g.visited:
    if u < 6 and v < 7:
        if (u+2,v+1) not in g.visited:
        #g.add_edge(u+2, v+1, weight)
            return {"startX":u+2, "startY":v+1, "moveType":3}
    return None
    
#moveType 4
def downTwoRightOne(u, v):
    # isVisited = (u, v)
    # if isVisited not in g.visited:
    if u < 7 and v < 6:
        if (u+1, v+2) not in g.visited:
            return {"startX":u+1, "startY":v+2, "moveType":4}
    return None

#moveType 5
def downTwoLeftOne(u, v):
    # isVisited = (u, v)
    # #print("entered")
    # if isVisited not in g.visited:
        #print("entered next level")
    if u > 0 and v < 6:
        #print("entered NEXT NEXT LVL")
        if (u-1, v+2) not in g.visited:
        #g.add_edge(u-1, v+2, weight)
            #print("------------------------------------")
            return {"startX":u-1, "startY": v+2, "moveType":5}
    return None
        
#moveType 6
def downOneLeftTwo(u, v):
    # isVisited = (u, v)
    # if isVisited not in g.visited:
    if u > 1 and v < 7:
        if (u-2, v+1) not in g.visited:
        #g.add_edge(u-2, v+1, weight)
            return {"startX":u-2, "startY":v+1, "moveType":6}
    return None
        
#moveType 7
def upOneLeftTwo(u, v):
    # isVisited = (u, v)
    # if isVisited not in g.visited:
    if u > 1 and v > 0:
        if (u-2, v-1) not in g.visited:
        #g.add_edge(u-2, v-1, weight)
            return {"startX":u-2, "startY":v-1, "moveType":7}
    return None

#moveType 8
def upTwoLeftOne(u, v):
    # isVisited = (u, v)
    # if isVisited not in g.visited:
    if u > 0 and v > 1:
        if (u-1, v-2) not in g.visited:
        #g.add_edge(u-1, v-2, weight)
            return {"startX":u-1, "startY":v-2, "moveType":8}
    return None


g.warnsfdorff(1,0)
g.print_graph()
#need a way to count legal moves and know what your starting square is
#and check if visited
#assign numbers to the directions

