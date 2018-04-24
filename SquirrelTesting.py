class Node:
    
    def __init__(self, label):
        self.label = label
        
class Graph:
    
    nodes = {}      # used to find a node by its label
    matrix = []     # contains 2D array of edges
    edge_index = {} # used to knightMovesDict the index of an edge given its label
    visited = []
    related = []
    pathNum = 1
    switchX = None
    switchY = None 
    
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
            self.matrix[self.edge_index[v]][self.edge_index[u]] = weight
            self.visited.append((u,v))
            
        """ 
        To represent an edge between nodes:
        (u,v) changes to store a 1
        (v,u) changes to store a 1
        """
    
    def print_graph(self):
        #print("  01234567")
        print("<<<<<<<<<< Knight Tour SQUIRREL >>>>>>>>>>>")
        print("")
        singleNums = [0,1,2,3,4,5,6,7,8,9]
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
        # print("entering counter")
        # print(len(array))
        i = 1
        
        #print("this is the visited list >>>>>> " + str(self.visited))
        
        while i <= len(array):
            if array[i] != None:
              if (array[i]["startX"], array[i]["startY"]) not in self.visited:
                 counter += 1
                 i += 1
            else:
                 i += 1
      
        #print("this is the array:" + str(array))
        #print("this is the counter: " + str(counter))
        return counter
    
    
    def checkForRepeats(self, array):
        #print(array)
        if len(array) != 0:
            repeated = 1
            firstNodesDegree = array[0]["degree"]
            for i in range(1, len(array)):
                if array[i]["degree"] == firstNodesDegree:
                    repeated += 1
                    #print(repeated)
    
        if repeated > 1:
            return array[0:repeated]
        else:
            return False
    
    def tieBreakRule(self, tieList):
        
        if self.switchX == 7 and self.switchY == 6:
            rule = [8,7,6,4,2,1,3,5] #2
        elif self.switchX == 2 and self.switchY == 2:
            rule = [5,1,8,6,7,3,4,2] #3
        elif self.switchX == 0 and self.switchY == 1:
            rule = [5,1,3,4,2,6,7,8] #4
        elif self.switchX == 7 and self.switchY == 5:
            rule = [2,1,4,3,5,6,7,8] #5 
        else:
            rule = [3,4,2,6,1,5,7,8] #1 original
        
        tiebreakCounter = 0
        ruleCounter = 0
        bestMoveTypeIndexInRule = 8
        while tiebreakCounter < len(tieList):
 
            #print(str(example[tiebreakCounter]["moveType"]))
            ruleCounter = 0
            
            while ruleCounter < len(rule):
                #print("this is the rule: " + str(rule[ruleCounter]))
                if tieList[tiebreakCounter]["moveType"] == rule[ruleCounter]:
                    #print("this is where they are the same: " + str(ruleCounter))
                    if ruleCounter < bestMoveTypeIndexInRule:
                        bestMoveTypeIndexInRule = ruleCounter
                        bestMove = tieList[tiebreakCounter]
                ruleCounter += 1
                
            tiebreakCounter += 1
        
        return bestMove
    
    def warnsfdorff(self,startX,startY,depth=0, moveType = None):
        
        print(str(startX) + " " + str(startY)) 
        if depth == 0 and (startX,startY) not in self.visited:
            #print(self.pathNum)
            self.add_edge(startX,startY,self.pathNum) #adds 6,0
        
        # if self.pathNum == 63:
        #     return self.visited
        if len(self.visited)<=64: #hardcoded for 8by8 board
            #return self.visited
            
            knightMovesDict = dict()
            knightMovesDict[1]= upTwoRightOne(startX,startY)
            knightMovesDict[2]= upOneRightTwo(startX,startY)
            knightMovesDict[3]= downOneRightTwo(startX,startY)
            knightMovesDict[4]= downTwoRightOne(startX,startY)
            knightMovesDict[5]= downTwoLeftOne(startX,startY)
            knightMovesDict[6]= downOneLeftTwo(startX,startY)
            knightMovesDict[7]= upOneLeftTwo(startX,startY)
            knightMovesDict[8]= upTwoLeftOne(startX,startY)
            
            print(knightMovesDict)
            print("this is depth: " + str(depth))
            # print("KMD: " + str(knightMovesDict))
            # print("")
            
            # if depth == 0 and (startX, startY) not in self.related:
            #     self.add_edge(startX, startY, 1)
          
            kmdCounter = 1
            
            # print("THIS IS THE KMD COUNTER: " + str(kmdCounter))
            
            while kmdCounter <= len(knightMovesDict):
                #print("entering")
                #x=2 y=1
                if knightMovesDict[kmdCounter] != None:
                    adjacentNodeX = knightMovesDict[kmdCounter]["startX"]
                    adjacentNodeY = knightMovesDict[kmdCounter]["startY"]
                    
                    # print(" ")
                    # print("THIS IS THE NEXT X: " + (str(adjacentNodeX)))
                    # print("THIS IS THE NEXT Y: " + (str(adjacentNodeY)))
                    # print(" ")
                    #DEPTH = 1
                    #LIST OF NOTHINGGGGGGG
                    if depth == 1:
                        # print("ENTERING IF")
                        # print("")
                         
                        numberAvailableMoves = self.countAvailableMoves(knightMovesDict) #2,1
                        #print(numberAvailableMoves)
                        # print("THIS IS THE NUMBER OF AVAILABLE MOVES (IN IF): " + str(numberAvailableMoves))
                        # print("")
                        
                        self.related.append({"startX":startX, "startY":startY, "degree":numberAvailableMoves, "moveType":moveType})#move type might be different
                        # print("This is the numberAvailableMoves: " + str(numberAvailableMoves))
                        # print("")
                        # print("THIS IS THE RELATED LIST: " + str(self.related))
                        # print(str(len(self.related)))
                        #NEED SOMETHING IN HERE
                        return
                        
                    else:
                        # print("")
                        # print("ENTERING ELSE")
                        # print("THIS IS STARTx <<< " + str(startX))
                        # print("THIS IS STARTy <<< " + str(startY))
                        # print(str(self.related)) #nothing
                        
                        # print("")
                        self.warnsfdorff(adjacentNodeX, adjacentNodeY, depth+1, moveType = knightMovesDict[kmdCounter]["moveType"]) #goes back here
                        #print("")
                        kmdCounter += 1
                    
                else:
                    kmdCounter += 1
                    
            
            #THIS IS NEEEEEEEEEEEEEEEEEEEEEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWwwwwwwwww
            if len(self.related) == 0 and (startX,startY) not in self.visited:
                self.add_edge(startX,startY,self.pathNum+1)
                return
            
            sortedRelated = bubbleSort(self.related)
            
            #print("this is the sorted: " + str(sortedRelated))
            #self.print_graph()
            relatedCounter = 0
            #repeated = 0
            while relatedCounter < len(sortedRelated):
                #Squirrels should go here
                #nextX = sortedRelated[relatedCounter]["startX"]
                #nextY = sortedRelated[relatedCounter]["startY"]
                # 
                #if len(sortedRelated) > 0:
    
                if startX == 7 and startY == 6:
                    self.switchX = startX
                    self.switchY = startY
                    #print(str(self.pathNum))
                if startX == 2 and startY == 2:
                    self.switchX = startX
                    self.switchY = startY
                    #print(str(self.pathNum))
                if startX == 0 and startY == 1:
                    self.switchX = startX
                    self.switchY = startY
                    #print(str(self.pathNum))
                if startX == 7 and startY == 5:
                    self.switchX = startX
                    self.switchY = startY
                    #print(str(self.pathNum))
                    
                    
                tieList = self.checkForRepeats(sortedRelated) #can return a repeated or non repeated list
                #print(str(tieList))
                if tieList == False:
                    nextX = sortedRelated[relatedCounter]["startX"]
                    nextY = sortedRelated[relatedCounter]["startY"]
                else:
                    bestMove = self.tieBreakRule(tieList)
                    nextX = bestMove["startX"]
                    nextY = bestMove["startY"]
                                        
                #print("<<<<<<<<<<<<< this is the tieList >>>>>>>>>>>>>>>>>>>" + str(tieList))
                
                #print(str(nextX) + " " + str(nextY))
            
                    
                """loop through the sorted related and check the first element's 
                   degree and see if there are more elements with the same degree.
                   if there are call the tie break rule and pass in the current(x,y)
                   and the SHORTENED sorted related. In the tie break rule check if the
                   current (x,y) is one that was stated. make a list of the containing
                   the first tiebreak rule e.g.[3,4,5,6,7,8,1,2]. Then loop through
                   the SHORTENED sortedRelated list and get the movetype of the first
                   element and check where that is in the tieBreakRule. Then move to
                   the next one. return the x and y of whichever one comes first in
                   the tiebreak rule.
                """
                print(self.visited)
                
                if (nextX,nextY) not in self.visited:
                    self.related = []
                    sortedRelated = []
                    self.pathNum += 1
                    self.warnsfdorff(nextX, nextY) #6,0 
                else:
                    relatedCounter += 1
        return self.visited

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
    
g.print_graph()

g.warnsfdorff(0,0)
#print("")
g.print_graph()

print(str(len(g.visited)))
print(g.visited)
#print(g.pathNum)
