import random

"""Module description
   * this script handles the computation of the Spanning Tree Algorithm
   * Detailed description to algorithm can be find at the bottom of the file

   author: 7056674
   date: 04.06.2022
   version: 0.0.1
   license: free
"""
''' ## Start Vertex Class ## '''
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

    """Description:
        * prints all information about object of this class in readable format
        * used during development, irrelevant for program
    Args:
        * self: reference to its own object
    Test: 
        * call function on existing object to see if printed data matches
    """
    def show_meta(self):
        print("Name:", self.name, "ID:", self.id)
        print("Root ID:", self.root.id, "Weight to Root:", self.weightToRoot)
        print("Next hop ID:", self.nextHop.id)
        print("Neighbors:", self.nghbrsPrint())
        print("Casts:", self.nmbrOfCasts)
        print(" - - - ")
    
    """Description: 
        * prints neighboring vertices of itself
        * used during development, irrelevant for program
    Args:
        * self: reference to its own object
    Return:
        * List of tuples of name of self and neighbor
    Test: 
        * call function on existing object to see if printed data matches
    """
    def nghbrsPrint(self):
        result = []
        for nghbr in self.nghbrs:
            tpl = (nghbr[0].name, nghbr[1])
            result.append(tpl)
        return result

    """Description: 
        * finds vertices that it is connected with
        * stores object of every neighbor in list self.neighbor 
        * neighbor is found if in edges there is a tuple containing selfs name
        * from this tuple extract other vertexs name
        * get corresponding object by looking for name in dictionary of all vertices
    Args:
        * self: reference to itself (like every other function inside this class, so this will not be mentioned on all the other functions)
        * edges: list of tuples of strings and edgge weight
        * _allVrtcs: dictionary with key being objects name, value is reference to every object
    Return:
        * none
        * indirectly return list as it writes results to nghbrs directly
    Test: 
        * self=Vertex("B", 1)
        * edges=[("A-B", 4), ("B-C", 3)]
        * _allVrtcs={"A": Vertex("A", 2), "B": Vertex("B", 1), "C": Vertex("C", 4)}
        --> nghbrs=[(Vertex("A", 2), 4), (Vertex("C", 4), 3)]
    """
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

    """Description: 
        * given other vertex, determines weight of edge beween self and other vertex
        * iterates over every neighbor in nghbrs list until given other neighbor is found
    Args:
        * nghbrVrtx: reference to object of other Vertex in Spanning Tree
    Return:
        * Integer: weight of edege
    Test: 
        * A vertex where there is an edge connecting it to self
        --> must return weight of said edge
    """
    def getEdgeWeight(self, nghbrVrtx):
        for nghbr in self.nghbrs:
            # find neighbor in nghbr array
            if nghbrVrtx.name == nghbr[0].name:
                # return value of corresponding weight of edge to nghbrVrtx
                weight = nghbr[1]
        return weight

    """Description: 
        * heart of the algorithm
        * simulates a device in a network broadcasting to receive information about root
        * sends 'broadcast' to every vertex object in nghbrs list
        * increments counter of broadcasts by 1
    Args:
        * self
    Return:
        * none
    Test: 
        * none
    """
    def broadcast(self):
        #broadcast must be sent to every neighbor
        for nghbr in self.nghbrs:
            vrtx = nghbr[0]
            # call function of receiving vertex to handle broadcast
            vrtx.receiveNewRoot(self)
        self.nmbrOfCasts += 1

    """Description: 
        * when being sent a broadcast, determines what information to update
        * Case 1: recieved a broadcast with a better root (lower rootID)
        * Case 2: recieved broadcast with same rootID as self but would improve path weight to root
    Args:
        * sender: reference to object that sent the broadcast in order to reference its known root and other information
    Return:
        * none
    Test: 
        * create Vertex objects and run the algorithm
    """
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


"""Description: 
    * creates Vertex objects for every tupel in vrtcsTplList
Args:
    * vrtcsTplList: list of tuples representing vertex with name and id
Return:
    * dictionary with object name as key and reference to object as value
Test: 
    * vrtcsTplList = [("A", 3), ("B", 77)]
    --> {"A": Vertex("A", 3), "B": Vertex("B", 77)}
"""
def createVertices(vrtcsTplList):
    vrtcs = {}
    for vrtx in vrtcsTplList:
        newVrtx = Vertex(vrtx[0], vrtx[1])
        vrtcs[newVrtx.name] = newVrtx
    return vrtcs

"""Description: 
    * 
Args:
    * input_edges: list of tuples representing vertex with name and id
    * vrtcsDict: dictionary with object name as key and reference to object as value
Return:
    * none
Test: 
    * needs objects of class Vertex, cannot be formulated generally
"""
def generateNghbrs(input_edges, vrtcsDict):
    for vrtx in vrtcsDict:
        vrtcsDict[vrtx].findNeighbors(input_edges, vrtcsDict)

"""Description: 
    * iterates over every vertex object and determines lowest number of braodcasts
Args:
    * vrtcsDict: dictionary with object name as key and reference to object as value
Return:
    * number of broadcasts of object with least broadcasts
Test: 
    * needs objects of class Vertex, cannot be formulated generally
"""
def leastBroadcasts(vrtcsDict):
    lowestNumCasts = vrtcsDict[list(vrtcsDict)[0]].nmbrOfCasts
    for vrtx in vrtcsDict:
        if vrtcsDict[vrtx].nmbrOfCasts < lowestNumCasts:
            lowestNumCasts = vrtcsDict[vrtx].nmbrOfCasts
    return lowestNumCasts

"""Description: 
    * from dict of all Vertex objects gets every objects name and name of nextHop
    * if name of next hop is own name it is root
    * store names or name and root as tuple
Args:
    * vrtcsDict: dictionary with object name as key and reference to object as value
Return:
    * list of tuples representing vertex and nextHop from this vertex
Test: 
    * needs objects of class Vertex, cannot be formulated generally
"""
def generateOutput(vrtcsDict):
    hopList = []
    for vrtx in vrtcsDict:
        if vrtcsDict[vrtx].name != vrtcsDict[vrtx].root.name:
            tpl = (vrtcsDict[vrtx].name, vrtcsDict[vrtx].nextHop.name)
        else:
            tpl = (vrtcsDict[vrtx].name, "Root")
        hopList.append(tpl)
    return hopList

"""Description: 
    * For a list of tuples containing vrtx name and name of next hop returns list of tuples stringified
Args:
    * List of Tuples - exapmle [("A", "B"), ("B", "C"), ("C", "Root"), ("D", "C")]
Return:
    * dict of strings for each vertex with key being index
    * each string contains vertx name and name of "next hop" vertex
    * if there is no next hop contains "Root"
Test: 
    * tplList = [("A", "B"), ("B", "C"), ("C", "Root"), ("D", "C")]
    --> {1: "A -> B", 2: "B -> C", 3: "C -> Root", 4: "D -> C"}
"""
def outputToDict(tplList):
    outputDict = {}
    for i in range(len(tplList)):
        lineStr = tplList[i][0] + " -> " + tplList[i][1]
        outputDict[i] = lineStr
    return outputDict

"""Description: 
    * Because input comes from JSON needs to be formatted to be processed further
Args:
    * vrtcs: list of dicts from JSON containing info about vrtcs created in frontend
Return:
    * list of tuples of string name of vertex and int id of vertex
Test: 
    * vrtcs = [{'vrtxName': "A", 'vrtxID': 3}, {'vrtxName': "B", 'vrtxID': 5}]
    --> [("A", 3), ("B", 5)]
"""
def formatVrtcs(vrtcs):
    formattedVrtcs = []
    for vrtx in vrtcs:
        tpl = (vrtx["vrtxName"], vrtx["vrtxID"])
        formattedVrtcs.append(tpl)
    return formattedVrtcs

"""see formatVrtcs
Args:
    * edges: list of dicts from JSON containing info about edges created in frontend
Test:
    * edges = [{'From': "A", 'To': "B", 'Weight': 3}, ...]
    --> [("A-B", 3, ...)]
"""
def formatEdges(edges):
    formattedEdges = []
    for edge in edges:
        edgeStr = edge["From"] + "-" + edge["To"]
        tpl = (edgeStr, edge["Weight"])
        formattedEdges.append(tpl)
    return formattedEdges

"""Description:
    * vertices and edges must confirm to certain rules
    * ensures that
        + lowest vertex ID only exists once, since this will be root and there can not be two roots
        + no edge is defined twice
Args:
    * vrtcs: list of tuples describing vertices
    * edges: list of tuples describing edges
Return:
    * boolean
Test: 
    * 1.
        + vrtcs: [("A", 2), ("B", 1), ("C", 5), ("D", 1)]
        + edges: [("A-B", 4), ("B-C", 4), ("C-A", 1), ("D-C", 3)]
        --> False
    * 2.
        + vrtcs: [("A", 2), ("B", 1), ("C", 5), ("D", 8)]
        + edges: [("A-B", 4), ("B-C", 4), ("C-A", 1), ("D-C", 3)]
        --> True
    * 3.
        + vrtcs: [("A", 2), ("B", 1), ("C", 5), ("D", (1))]
        + edges: [("A-B", 4), ("B-C", 4), ("C-B", 1), ("D-C", 3)]
        --> False
"""
def isValidInput(vrtcs, edges):
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
"""Description:
    * main function
    * is the one that needs to be imported anywhere to use algorithm
Args:
    * input_vertices: list sent from frontend JSON-like: [{'vrtxName': "A", 'vrtxID': 3}, {'vrtxName': "B", 'vrtxID': 5}]
    * input_edges: list sent from frontend JSON-like: [{'From': "A", 'To': "B", 'Weight': 3}, ...]
Return:
    * list of strings for each vertex
    * each string contains vertx name and name of "next hop" vertex
    * if there is no next hop contains "Root"
Test: 
    * 
"""
def evaluateSpanningTree(input_vertices: list, input_edges: list) -> list:
    input_vertices = formatVrtcs(input_vertices)
    input_edges = formatEdges(input_edges)

    allVrtcs = {}
    minimumCasts = len(input_vertices) * len(input_vertices)

    # print("vrtcs:", input_vertices)
    # print("edges:", input_edges)

    if isValidInput(vrtcs=input_vertices, edges=input_edges):
        allVrtcs = createVertices(input_vertices)
        generateNghbrs(input_edges, allVrtcs)

        # as long as any vertex has less broadcasts than specified in minimumCasts
        while leastBroadcasts(allVrtcs) < minimumCasts:
            # choose vertex to send broadcast at random
            rndmVrtx = random.choice(list(allVrtcs))
            # chosen vertex sends broadcast
            allVrtcs[rndmVrtx].broadcast()

    return outputToDict(generateOutput(allVrtcs))