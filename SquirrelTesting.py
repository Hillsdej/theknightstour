class Node:
    
    def __init__(self, label):
        self.label = label
        
class Graph:
    
    nodes = {}      # used to find a node by its label
    matrix = []     # contains 2D array of edges
    edge_index = {} # used to knightMovesDict the index of an edge given its label
    visited = []
    related = []
    
    def add_node(self, node):
        #first knightMovesDict if it is a node and not in the node list
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
        #knightMovesDict to see if nodes u and v are in the node dictionary
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
    
    def countAvailableMoves(self, array):
        counter = 0
        print("entering counter")
        print(len(array))
        i = 1
        
        print("this is the visited list >>>>>> " + str(self.visited))
        
        while i <= len(array):
            if array[i] != None:
              if (array[i]["startX"], array[i]["startY"]) not in self.visited:
                 counter += 1
                 i += 1
            else:
                 i += 1
            
        
        # for i in range(1, len(array)):
        #     print(str(i))
        #     if array[i] != None:
        #         if (array[i]["startX"], array[i]["startY"]) not in self.visited:
        #             counter += 1
        
        print("this is the array:" + str(array))
        print("this is the counter: " + str(counter))
        return counter
    
    def warnsfdorff(self,startX,startY,depth=0, moveType = None):
        print("----------------------------------------------------------------")
        print("THIS IS STARTx >>> " + str(startX))
        print("")
        print("THIS IS STARTy >>> " + str(startY))
        print("")
        print("THIS IS THE DEPTH: " + str(depth))
        print("")
        
        if depth == 0:
            self.add_edge(startX,startY,1)
        
        if len(self.visited)>=4:
            return self.visited
            
        knightMovesDict = dict()
        knightMovesDict[1]= upTwoRightOne(startX,startY)
        knightMovesDict[2]= upOneRightTwo(startX,startY)
        knightMovesDict[3]= downOneRightTwo(startX,startY)
        knightMovesDict[4]= downTwoRightOne(startX,startY)
        knightMovesDict[5]= downTwoLeftOne(startX,startY)
        knightMovesDict[6]= downOneLeftTwo(startX,startY)
        knightMovesDict[7]= upOneLeftTwo(startX,startY)
        knightMovesDict[8]= upTwoLeftOne(startX,startY)
        
        print("KMD: " + str(knightMovesDict))
        print("")
        
        # if depth == 0 and (startX, startY) not in self.related:
        #     self.add_edge(startX, startY, 1)
      
        kmdCounter = 1
        
        print("THIS IS THE KMD COUNTER: " + str(kmdCounter))
        
        while kmdCounter < len(knightMovesDict):
            #x=2 y=1
            if knightMovesDict[kmdCounter] != None:
                adjacentNodeX = knightMovesDict[kmdCounter]["startX"]
                adjacentNodeY = knightMovesDict[kmdCounter]["startY"]
                
                print(" ")
                print("THIS IS THE NEXT X: " + (str(adjacentNodeX)))
                print("THIS IS THE NEXT Y: " + (str(adjacentNodeY)))
                print(" ")
                
                if depth == 1:
                    print("ENTERING IF")
                    print("")
                     
                    numberAvailableMoves = self.countAvailableMoves(knightMovesDict) #2,1
                    print("THIS IS THE NUMBER OF AVAILABLE MOVES (IN IF): " + str(numberAvailableMoves))
                    print("")
                    
                    self.related.append({"startX":startX, "startY":startY, "degree":numberAvailableMoves, "moveType":moveType})#move type might be different
                    print("This is the numberAvailableMoves: " + str(numberAvailableMoves))
                    print("")
                    print("THIS IS THE RELATED LIST: " + str(self.related))
                    print(str(len(self.related)))
                    return
                    
                else:
                    print("")
                    print("ENTERING ELSE")
                    print("THIS IS STARTx <<< " + str(startX))
                    print("THIS IS STARTy <<< " + str(startY))
                    print(str(self.related))
                    
                    print("")
                    self.warnsfdorff(adjacentNodeX, adjacentNodeY, depth+1, moveType = knightMovesDict[kmdCounter]["moveType"]) #goes back here
                    print("")
                    kmdCounter += 1
                
            else:
                kmdCounter += 1
        
        #basically I need a base case to check 
        #if the length of the self.related list is
        #big enough or if its finished looping recursively
        #then after ive stopped the recursive bit
        #I then need to call this
        print("This is the sorted list")
        print(bubbleSort(self.related))
        print("")
        
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

def bubbleSort(array):
    
    if len(array)<=1:
        return array
    
    notSorted = True
    
    while notSorted == True:
        
        notSorted = False
        
        for i in range(0,len(array)-1):
            
            if array[i]["degree"] > array[i+1]["degree"]:
                array[i], array[i+1] =  array[i+1], array[i]
                notSorted = True
    
    return array  
            
#g.add_edge(2,1,1)
g.print_graph()
g.warnsfdorff(2,1)
g.print_graph()
#print(bubbleSort(g.related))
#need a way to count legal moves and know what your starting square is
#and knightMovesDict if visited
#assign numbers to the directions

