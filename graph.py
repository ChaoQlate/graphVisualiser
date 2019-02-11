class graph(object):
    def __init__(self, defaultWeight=1):
        self.adjacencyList = dict()
        self.defaultWeight = defaultWeight
    
    def addNode(self, n):
        if not self.validNode(n):
            self.adjacencyList[n] = []
    
    def addDirectedEdge(self, n, m, weight=None):
        weight = self.defaultWeight if weight == None else weight
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

if __name__ == "__main__":
    g = graph()
    
    g.addNode(1)
    g.addNode(2)
    g.addNode(3)
    g.addNode(4)
    g.addNode(5)
    g.addNode(6)

    g.addDirectedEdge(1,2,101)
    g.addUndirectedEdge(3,4, 102)
    g.addUndirectedEdge(1,2, 103)
    g.addDirectedEdge(1,3,104)
    g.addDirectedEdge(1,4,105)
    g.addDirectedEdge(1,5,106)
    g.addDirectedEdge(1,6,107)

    g.show()


    