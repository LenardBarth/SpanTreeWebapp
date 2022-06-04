import random

'''
    ## Vertex Class ##
    Represents Node in Spanning Tree
'''
class Vertex:
    name = "none"       # string filled from input
    id = 0              # int filled from input
    root = None         # contains Vertex object that represents this vertexes known root
    weightToRoot = -1   # sum of all edge weights on way to root
    nextHop = None      # contains Vertex object that represents next vertex on way to root
    nghbrs = []         # array of tuples of Vertex object and weight of edge to this vertex
    nmbrOfCasts = 0     # int number of times broadcast function was called

    def __init__(self, _name, _id):
        self.name = _name
        self.id = _id
        self.root = self
        self.weightToRoot = 0
        self.nextHop = self
        self.nghbrs = []
        self.nmbrOfCasts = 0

    def show_meta(self):
        print("Name:", self.name, "ID:", self.id)
        print("Root ID:", self.root.id, "Weight to Root:", self.weightToRoot)
        print("Next hop ID:", self.nextHop.id)
        print("Neighbors:", self.nghbrsPrint())
        print("Casts:", self.nmbrOfCasts)
        print(" - - - ")
        pass
    
    def nghbrsPrint(self):
        result = []
        for nghbr in self.nghbrs:
            tpl = (nghbr[0].name, nghbr[1])
            result.append(tpl)
        return result

    def findNeighbors(self, edges, _allVrtcs):
        for edge in edges:
            # if own name is FIRST name of edge and has not been appended yet
            # -> append tuple of SECOND name and path weight
            if (self.name == edge[0].split("-")[0]) and not any(_allVrtcs[edge[0].split("-")[1]].name in tpl[0].name for tpl in self.nghbrs):
                self.nghbrs.append((_allVrtcs[edge[0].split("-")[1]], edge[1]))
            # if own name is SECOND letter in name of edge and has not been appended yet
            # -> append tuple of FIRST letter and path weight
            elif (self.name == edge[0].split("-")[1]) and not any(_allVrtcs[edge[0].split("-")[0]].name == tpl[0].name for tpl in self.nghbrs):
                self.nghbrs.append((_allVrtcs[edge[0].split("-")[0]], edge[1]))
        pass

    def getEdgeWeight(self, nghbrVrtx):
        for nghbr in self.nghbrs:
            # find neighbor in nghbr array
            if nghbrVrtx.name == nghbr[0].name:
                # return value of corresponding weight of edge to nghbrVrtx
                weight = nghbr[1]
        return weight

    def broadcast(self):
        #broadcast must be sent to every neighbor
        for nghbr in self.nghbrs:
            vrtx = nghbr[0]
            # call function of receiving vertex to handle broadcast
            vrtx.receiveNewRoot(self)
        self.nmbrOfCasts += 1

    def receiveNewRoot(self, sender):
        # store weight of edge connecting broadcasting vertex and self(receiving vertex)
        weightBetween = self.getEdgeWeight(sender)
        # if broadcasted root id is less than known root id -> accept new root and update weight
        if sender.root.id < self.root.id:
            self.root = sender.root
            self.nextHop = sender
            self.weightToRoot = sender.weightToRoot + weightBetween
        # if incoming root id is already known root of self but new weight to root can be less -> keep root but update weight
        elif sender.root.id == self.root.id and sender.weightToRoot + weightBetween < self.weightToRoot:
            self.nextHop = sender
            self.weightToRoot = sender.weightToRoot + weightBetween
''' ## End of Vertex Class ## '''


def createVertices(vrtcsTplList):
    vrtcs = {}
    for vrtx in vrtcsTplList:
        newVrtx = Vertex(vrtx[0], vrtx[1])
        vrtcs[newVrtx.name] = newVrtx
    return vrtcs

def generateNghbrs(input_edges, vrtcsDict):
    for vrtx in vrtcsDict:
        vrtcsDict[vrtx].findNeighbors(input_edges, vrtcsDict)

def leastBroadcasts(vrtcsDict):
    lowestNumCasts = vrtcsDict[list(vrtcsDict)[0]].nmbrOfCasts
    for vrtx in vrtcsDict:
        if vrtcsDict[vrtx].nmbrOfCasts < lowestNumCasts:
            lowestNumCasts = vrtcsDict[vrtx].nmbrOfCasts
    return lowestNumCasts

def generateOutput(vrtcsDict):
    hopList = []
    for vrtx in vrtcsDict:
        if vrtcsDict[vrtx].name != vrtcsDict[vrtx].root.name:
            tpl = (vrtcsDict[vrtx].name, vrtcsDict[vrtx].nextHop.name)
        else:
            tpl = (vrtcsDict[vrtx].name, "Root")
        hopList.append(tpl)
    return hopList

def outputToString(tplList):
    outputString = ""
    for tpl in tplList:
        outputString = outputString + tpl[0] + " -> " + tpl[1] + "\n"
    return outputString

def formatVrtcs(vrtcs):
    formattedVrtcs = []
    for vrtx in vrtcs:
        tpl = (vrtx["vrtxName"], vrtx["vrtxID"])
        formattedVrtcs.append(tpl)
    return formattedVrtcs

def formatEdges(edges):
    formattedEdges = []
    for edge in edges:
        edgeStr = edge["From"] + "-" + edge["To"]
        tpl = (edgeStr, edge["Weight"])
        formattedEdges.append(tpl)
    return formattedEdges

def isValidInput(vrtcs, edges):
    # example valid vrtcs: {"A": 2, "B": 18, "C", 1}
    # example valid edges: {"A-B": 2, "B-C": 3, "C-A", 2}
    if (vrtcs!=[] and edges!=[]):
        # start value is infinty - will be used to compare against
        minVrtxID = float('inf')
        for vrtx in vrtcs:
            # make sure lowest ID exists only once
            if vrtx[1] < minVrtxID:
                minVrtxID = vrtx[1]
            elif vrtx[1] == minVrtxID:
                print("[!] - Error: Root ID exists twice")
                return False
        # 
        for edge in edges:
            for otherEdge in edges:
                # check if edge was defined twice in inverse direction (A-B and B-A)
                if edge[0] == otherEdge[0][::-1]:
                    print("[!] - Error: Edge", edge, "was defined twice with", otherEdge)
                    return False
        return True
    else:
        return False

'''
SPANNING TREE ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~

 * all vertices created from the 'input_vertices' list start out as their own root with pathweight 0
 * neighbors to any given vertex are determined using the 'input_edges' list and stored with the according weight
 * a random vertex broadcasts its known root vertex and the pathweight to this root to its neighbors
 * a vertex receiving a broadcast will update its root and pathweight if
    + the incoming root ID is less than the ID of the known root
    + the weight to a root it already knows is less than the known weight
 * broadcasting will be terminated once every vertex has broadcasted at least as many times as specified in 'minimumCasts'
 * output will list every vertex with its next hop on its (cheapest) way to root
'''
def evaluateSpanningTree(input_vertices: list, input_edges: list) -> str:
    input_vertices = formatVrtcs(input_vertices)
    input_edges = formatEdges(input_edges)

    allVrtcs = {}
    minimumCasts = len(input_vertices) * len(input_vertices)

    print("vrtcs:", input_vertices)
    print("edges:", input_edges)

    if isValidInput(vrtcs=input_vertices, edges=input_edges):
        allVrtcs = createVertices(input_vertices)
        generateNghbrs(input_edges, allVrtcs)

        # as long as any vertex has less broadcasts than specified in minimumCasts
        while leastBroadcasts(allVrtcs) < minimumCasts:
            # choose vertex to send broadcast at random
            rndmVrtx = random.choice(list(allVrtcs))
            # chosen vertex sends broadcast
            allVrtcs[rndmVrtx].broadcast()

    return outputToString(generateOutput(allVrtcs))