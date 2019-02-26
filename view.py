from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget
from PyQt5 import QtCore
import pyqtgraph as pg
import forceDirectedEngine as fde
import vector
import time
import queue

'''
custom class derived from the pyqt5 package, used as a window for the gui
contains a forceDirectedEngine for calculations on the coordinates
'''
class applicationWindow(QWidget, QtCore.QObject):
    def __init__(self, fde, parent=None):
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        super(applicationWindow, self).__init__(parent)

        self.forceDirectedEngine = fde

        self.axisItemB = pg.AxisItem("bottom", showValues=False, maxTickLength=0, pen='w')
        self.axisItemL = pg.AxisItem("left", showValues=False, maxTickLength=0, pen='w')
        self.graph = pg.PlotWidget(axisItems={"bottom" : self.axisItemB, "left" : self.axisItemL}, title="")
        self.graph.resize(1000,1000)

        self.plotGraph(self.forceDirectedEngine.nodeCoordinates, self.forceDirectedEngine.graph)
        self.graph.scene().sigMouseMoved.connect(self.showNearestNode)

        self.queue = None

        button = QPushButton("Next")
        button.clicked.connect(self.showNextNode)
        layout = QGridLayout()
        layout.addWidget(button, 0, 0)
        layout.addWidget(self.graph, 1, 0)

        self.setLayout(layout)

    def showNextNode(self):
        if self.queue.empty():
            return
        self.showNode(self.queue.get())

    # takes in 
    # a dict containing node name as key and vector.vector as value
    # a graph.graph item and plots the points and edges
    def plotGraph(self, coordinates, graph):
        xVals = []
        yVals = []
        nodes = graph.getNodes()

        for n in nodes:
            edges = graph.getEdges(n)
            v = coordinates[n]
            for e in edges:
                w = coordinates[e[0]]
                self.graph.plot(x=[v.x, w.x], y=[v.y, w.y], pen=(0,0,0))

        for n in nodes:
            v = coordinates[n]
            xVals.append(round(v.x, 3))
            yVals.append(round(v.y, 3))
            
        self.graph.plot(x=xVals, y=yVals, pen=None, symbol='o', symbolSize=15, symbolBrush=(255,0,0))

    def showNearestNode(self, evt):
        mouseCoord = self.graph.getPlotItem().vb.mapSceneToView(evt)
        pos = vector.vector(mouseCoord.x(), mouseCoord.y())
        coordinates = self.forceDirectedEngine.nodeCoordinates
        min_ = 1000000
        node = None
        for v in coordinates:
            if (pos - coordinates[v]).length() < min_:
                node = v
                min_ = (pos - coordinates[v]).length()
        self.showNode(node)

    def showNode(self, node):
        self.titleNode(node)
        self.highlightNode(node)

    #changes the title of the graph to display a node id
    def titleNode(self, node):
        self.graph.setLabels(title=(node if type(node) == str else ""))


    # highlights a specific node
    def highlightNode(self, node):
        if node not in self.forceDirectedEngine.nodeCoordinates.keys():
            return
        coord = self.forceDirectedEngine.nodeCoordinates[node]
        try:
            self.graph.removeItem(self.oldHighlight)
        except AttributeError:
            pass
        self.oldHighlight = self.graph.plot(x=[coord.x], y=[coord.y], pen=None, symbol='o', symbolSize=20, symbolBrush=(0,255,0))