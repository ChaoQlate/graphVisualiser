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

        self.axisItemB = pg.AxisItem("bottom", showValues=False, maxTickLength=0)
        #self.axisItemT = pg.AxisItem("top", showValues=False, maxTickLength=0)
        self.axisItemL = pg.AxisItem("left", showValues=False, maxTickLength=0)
        #self.axisItemR = pg.AxisItem("right", showValues=False, maxTickLength=0)

        #self.graph = self.addPlot(axisItems={"bottom" : self.axisItemB, "top" : self.axisItemT, "left" : self.axisItemL, "right" : self.axisItemR})
        self.graph = self.addPlot(axisItems={"bottom" : self.axisItemB, "left" : self.axisItemL})

        self.graph.resize(1000,800)
        self.graphPlot(self.forceDirectedEngine.nodeCoordinates, self.forceDirectedEngine.graph)
        self.graph.scene().sigMouseMoved.connect(self.showNode)

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

        self.graph.plot(x=xVals, y=yVals, pen=None, symbol='o', symbolSize=10, symbolBrush=(255,0,0))

        for n in nodes:
            edges = graph.getEdges(n)
            v = coordinates[n]
            for e in edges:
                w = coordinates[e[0]]
                self.graph.plot(x=[v.x, w.x], y=[v.y, w.y], pen=(0,0,0))

    def showNode(self, evt):
        mouseCoord = self.graph.vb.mapSceneToView(evt)
        pos = vector.vector(mouseCoord.x(), mouseCoord.y())
        coordinates = self.forceDirectedEngine.nodeCoordinates
        min_ = 1000000
        node = 0
        for v in coordinates:
            if (pos - coordinates[v]).length() < min_:
                node = v
                min_ = (pos - coordinates[v]).length()
        self.graph.setLabels(title=node)

        
if __name__ =='__main__':
    app = QApplication(sys.argv)
    graph = graph.graph()

    graph.addNode("Pazzi")
    graph.addNode("Salviati")
    graph.addNode("Acciaiuolli")
    graph.addNode("Medici")
    graph.addNode("Barbadori")
    graph.addNode("Casteliani")
    graph.addNode("Strozzi")
    graph.addNode("Peruzzi")
    graph.addNode("Bischeri")
    graph.addNode("Ridolfi")
    graph.addNode("Tornabiouni")
    graph.addNode("Guadagini")
    graph.addNode("Albizzi")
    graph.addNode("Ginori")
    graph.addNode("Lamberteschi")


    graph.addUndirectedEdge("Pazzi", "Salviati")
    graph.addUndirectedEdge("Salviati", "Medici")
    graph.addUndirectedEdge("Acciaiuolli", "Medici")
    graph.addUndirectedEdge("Medici", "Barbadori")
    graph.addUndirectedEdge("Barbadori", "Casteliani")
    graph.addUndirectedEdge("Casteliani", "Strozzi")
    graph.addUndirectedEdge("Casteliani", "Peruzzi")
    graph.addUndirectedEdge("Peruzzi", "Bischeri")
    graph.addUndirectedEdge("Peruzzi", "Strozzi")
    graph.addUndirectedEdge("Strozzi", "Bischeri")
    graph.addUndirectedEdge("Strozzi", "Ridolfi")
    graph.addUndirectedEdge("Ridolfi", "Medici")
    graph.addUndirectedEdge("Tornabiouni", "Medici")
    graph.addUndirectedEdge("Tornabiouni", "Ridolfi")
    graph.addUndirectedEdge("Medici", "Albizzi")
    graph.addUndirectedEdge("Albizzi", "Ginori")
    graph.addUndirectedEdge("Albizzi", "Guadagini")
    graph.addUndirectedEdge("Guadagini", "Lamberteschi")
    graph.addUndirectedEdge("Guadagini", "Tornabiouni")
    graph.addUndirectedEdge("Guadagini", "Bischeri")

    '''
    graph.addNode("a")
    graph.addNode("b")
    graph.addNode("c")
    graph.addNode("d")
    graph.addNode("e")

    graph.addUndirectedEdge("a", "b")
    graph.addUndirectedEdge("a", "c")
    graph.addUndirectedEdge("b", "c")
    graph.addUndirectedEdge("a", "e")
    graph.addUndirectedEdge("b", "d", weight=10)
    '''

    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')

    engine = fde.forceDirectedEngine(graph)
    win = applicationWindow(engine)
    win.resize(1000,800)
    win.show()
    app.exec_()


#base the epsilon values from the zoom ??