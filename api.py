import graph as g
import forceDirectedEngine
import view
from PyQt5.QtWidgets import QApplication

app = QApplication([])
running = False

graph = None
engine = forceDirectedEngine.forceDirectedEngine()
window = view.applicationWindow(engine)
window.show()

def newGraph():
    global graph
    graph = g.graph()
    return graph

def addNode(n):
    global graph
    graph.addNode(n)

def addEdge(n, m):
    global graph
    graph.addUndirectedEdge(n,m)

def showGraph():
    global engine
    global graph
    global window
    engine.__init__(graph)
    window.plotGraph(window.forceDirectedEngine.nodeCoordinates, window.forceDirectedEngine.graph)
    window.resize(1000,1000)

def setNodeQueue(q):
    global window
    window.queue = q 

def run():
    global running
    if running == False:
        app.exec_()
    running = True

