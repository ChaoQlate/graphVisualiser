import math
import copy
import vector

class forceDirectedEngine():
    def __init__(self, graph):
        self.graph = graph
        self.nodeCoordinates = dict()
        
        ## nodes are first spaced evenly in a circle with a distance 1 between nodes
        ## in the case of one node, the node is centred
        nodes = self.graph.getNodes()
        numNodes = len(nodes)
        angleInteval = 2 * math.pi / numNodes if numNodes != 0 else 1
        radius = numNodes * 1 / (2 * math.pi) if numNodes != 1 else 0
        for i in range(numNodes):
            self.nodeCoordinates[nodes[i]] = \
                vector.vector(radius * math.cos(i * angleInteval), radius * math.sin(i * angleInteval))

        for _ in range(70):
            self.simulate()

    def simulate(self):
        nodes = self.graph.getNodes()
        toDo = [x[:] for x in [[True] * len(nodes)] * len(nodes)]
        newNodeCoordinates = copy.deepcopy(self.nodeCoordinates)


        # loop through nodes
            # push/pull the other nodes not yet done in the todo array
            # for every push pull update the nxn todo array

        for i in range(len(nodes)):
            edges = self.graph.getEdges(nodes[i])
            for e in edges:
                if toDo[i][nodes.index(e[0])] == False:
                    continue
                v = self.nodeCoordinates[e[0]] - self.nodeCoordinates[nodes[i]]
                d = v.length()
                f = self.attraction(d, e[1] * 0.001) - self.repulsion(d)
                v = v.unitVector() * (f / v.length())

                newNodeCoordinates[nodes[i]] += v
                newNodeCoordinates[e[0]] += v * -1

                toDo[i][nodes.index(e[0])] = False
            for j in range(len(nodes)):
                if toDo[i][j] == True and i != j:
                    v = self.nodeCoordinates[nodes[j]] - self.nodeCoordinates[nodes[i]]
                    d = v.length()
                    f = - self.repulsion(d)
                    v = v.unitVector() * (f / v.length())

                    newNodeCoordinates[nodes[i]] += v
                    newNodeCoordinates[nodes[j]] += v * -1

                toDo[i][j] = False
        self.nodeCoordinates = newNodeCoordinates

    ## attraction based on hookes law
    @staticmethod
    def attraction(distance, resting, dampening=1):
        return (distance - resting) * dampening

    ## replusion based on coulombs law
    @staticmethod
    def repulsion(distance, dampening=30):
        return dampening / distance if distance != 0 else 100