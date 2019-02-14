import graph
import vector
import forceDirectedEngine as fde
import sys
import pyqtgraph as pg
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget

class applicationWindow(pg.GraphicsWindow):
    def __init__(self, fde, parent=None):
        super(applicationWindow, self).__init__(parent)

        self.forceDirectedEngine = fde

        self.graph = self.addPlot()
        self.graph.resize(1000,800)
        self.graphPlot(self.forceDirectedEngine.nodeCoordinates, self.forceDirectedEngine.graph)
        self.graph.scene().sigMouseMoved.connect(self.showNode)

        self.label = pg.LabelItem(justify="right")
        self.label.setMinimumWidth(1000)
        self.addItem(self.label)


    def update(self):
        pass

    # takes in 
    # a dict containing node name as key and vector.vector as value
    # a graph.graph item and plots the points and edges
    def graphPlot(self, coordinates, graph):
        xVals = []
        yVals = []
        nodes = graph.getNodes()
        for n in nodes:
            v = coordinates[n]
            xVals.append(round(v.x, 3))
            yVals.append(round(v.y, 3))

        self.graph.plot(x=xVals, y=yVals, pen=None, symbol='o', symbolSize=10, symbolBrush=(100,100,100))

        for n in nodes:
            edges = graph.getEdges(n)
            v = coordinates[n]
            for e in edges:
                w = coordinates[e[0]]
                self.graph.plot(x=[v.x, w.x], y=[v.y, w.y], pen='b')

    def showNode(self, evt):
        mouseCoord = self.graph.vb.mapSceneToView(evt)
        pos = vector.vector(mouseCoord.x(), mouseCoord.y())
        coordinates = self.forceDirectedEngine.nodeCoordinates
        epsilon = 0.5

        for v in coordinates:
            if (pos - coordinates[v]).length() < epsilon:
                self.label.setText(v)
                return
        #self.label.setText("")

        
if __name__ =='__main__':
    app = QApplication(sys.argv)
    graph = graph.graph()
    graph.addNode("a")
    graph.addNode("b")
    graph.addNode("c")
    graph.addNode("d")
    graph.addNode("e")

    graph.addUndirectedEdge("a", "b")
    graph.addUndirectedEdge("a", "c")
    graph.addUndirectedEdge("b", "c")
    graph.addUndirectedEdge("a", "e")
    graph.addUndirectedEdge("b", "d", weight=100)

    engine = fde.forceDirectedEngine(graph)
    win = applicationWindow(engine)
    win.resize(1000,800)
    win.show()
    app.exec_()
