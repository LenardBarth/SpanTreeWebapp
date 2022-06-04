import random
import re

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

def createVertices(vrtcsTplList):
    vrtcs = {}
    for vrtx in vrtcsTplList:
        newVrtx = Vertex(vrtx[0], vrtx[1])
        vrtcs[newVrtx.name] = newVrtx
    return vrtcs

def generateNghbrs(vrtcsDict):
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

def printOutputToFile(tplList):
    try:
        file = open("output.txt", "w")
        for tpl in tplList:
            str = tpl[0] + " -> " + tpl[1] + "\n"
            file.write(str)
        file.close()
        print("Successfully printed result to 'output.txt' in current directory")
    except:
        print("[!] - Error: Could not write result to file")

def handleInput(line):
    # Regular expression to check if line in input is definition of edge with pattern: ' <name1> - <name2> = <weight>' or ' <name1> - <name2> : <weight>'
    # (weight is number, number of spaces anywhere not specific)
    edgeRgx = re.compile(r"""\s*(?P<edgeVrtx1>[a-zA-Z][a-zA-Z0-9_]*)\s*-\s*(?P<edgeVrtx2>[a-zA-Z][a-zA-Z0-9_]*)\s*[:=]\s*(?P<edgeWeight>[0-9]+);*""")
    # Regular expression to check if line in input is definition of vertex with pattern: ' <name> = <ID>' or ' <name> : <ID>'
    # (ID is number, number of spaces anywhere not specific)
    vrtxRgx = re.compile(r"""\s*(?P<vrtxName>[a-zA-Z][a-zA-Z0-9_]*)\s*[:=]\s*(?P<vrtxID>[0-9]+);*""")
    # check same line for edge pattern
    edgeMatch = edgeRgx.search(line)
    # match is not None if there is a matching string
    if edgeMatch:
        # filter out edges connecting to self or ones that have weight of 0
        if (not (edgeMatch.group('edgeVrtx1') == edgeMatch.group('edgeVrtx2'))) and (not (int(edgeMatch.group('edgeWeight')) == 0)):
            # transform input to data for spanning tree
            tpl = (edgeMatch.group('edgeVrtx1')+"-"+edgeMatch.group('edgeVrtx2'), int(edgeMatch.group('edgeWeight')))
            # make sure a definition for this edge has not been appended yet
            if not any (tpl[0] == edge[0] for edge in input_edges):
                # make data available to be processed
                input_edges.append(tpl)
    # if line does not match vertex pattern 
    else:
        # check line for vertex pattern
        vrtxMatch = vrtxRgx.search(line)
        # match is not None if there is a matching string
        if vrtxMatch:
            tpl = (vrtxMatch.group('vrtxName'), int(vrtxMatch.group('vrtxID')))
            # make sure a definition for this vertex has not been appended yet
            if not any (tpl[0] == vrtx[0] for vrtx in input_vertices):
                input_vertices.append(tpl)

def initializeFromFile(path):
    try:
        inpF = open(path, "r")
        line = inpF.readline()
    except FileNotFoundError:
        print("[!] - Error: File not found")
        return False
    except:
        print("[!] - Error: Error while opening file")
        return False
        
    # read until definition of graph starts
    while not '{' in line:
        line = inpF.readline()

    # read definition of graph's vertices and edges
    parseLine = inpF.readline()
    # print(parseLine)
    while parseLine != '' and not '}' in parseLine:
        # check line if it matches the pattern of a comment: '  //...'
        # (arbitrary number of spaces before '//' and any or none character after)
        commentLinePattern = re.compile(r"\s*//.*")
        # handle line content only if it is not a comment
        if commentLinePattern.search(parseLine) == None:
            handleInput(parseLine)
        # read next line
        parseLine = inpF.readline()
    inpF.close()
    return True

def isValidInput(vrtcs, edges):
    if (vrtcs!={} and edges!={}):
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
    + the weight to root is less than the known weight
 * broadcasting will be terminated once every vertex has broadcasted at least as many times as specified in 'minimumCasts'
 * output will list every vertex with its next hop on its (cheapest) way to root
    + 'cheapest' only assuming the algorithm has run enough times to determine that
'''
input_vertices = []
input_edges = []
allVrtcs = {}
minimumCasts = 5

'''~~~  Specify FILE to read input from HERE  ~~~'''
# filepath = "test_input.txt"
filepath = "test_input.txt"


# ensures the algoritm is run at least once
if minimumCasts < 1:
    minimumCasts = 1

# print("vrtcs:", input_vertices)
# print("edges:", input_edges)

if initializeFromFile(filepath) and isValidInput(vrtcs=input_vertices, edges=input_edges):
    allVrtcs = createVertices(input_vertices)
    generateNghbrs(allVrtcs)

    # as long as any vertex has less broadcasts than specified in minimumCasts
    while leastBroadcasts(allVrtcs) < minimumCasts:
        # choose vertex to send broadcast at random
        rndmVrtx = random.choice(list(allVrtcs))
        # chosen vertex sends broadcast
        allVrtcs[rndmVrtx].broadcast()

    output = generateOutput(allVrtcs)
    printOutputToFile(output)


