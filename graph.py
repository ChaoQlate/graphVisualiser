class graph(object):
    def __init__(self, defaultWeight=1):
        self.adjacencyList = dict()
        self.defaultWeight = defaultWeight
    
    def addNode(self, n):
        if not self.validNode(n):
            self.adjacencyList[n] = []
    
    def addDirectedEdge(self, n, m, weight=None):
        if n == m:
            return
        weight = self.defaultWeight if weight == None or weight <= 0 else weight
        if self.validNode(n):
            self.addNode(n)
        if self.validNode(m):
            self.addNode(m)
        connections = self.adjacencyList[n]
        for i in range(len(connections)):
            if m == connections[i][0]:
                connections[i] = (m, weight)
                return
        connections.append((m, weight))

    def addUndirectedEdge(self, n, m, weight=None):
        self.addDirectedEdge(n, m, weight)
        self.addDirectedEdge(m, n, weight)
    
    def validNode(self, n):
        if n in self.adjacencyList:
            return True
        return False

    def getNodes(self):
        return list(self.adjacencyList.keys())

    def getEdges(self, n):
        return self.adjacencyList[n]

    def show(self):
        for key in self.adjacencyList:
            print(key, ": ", end="")
            for v in self.adjacencyList[key]:
                print(v, "-> ", end="")
            print()