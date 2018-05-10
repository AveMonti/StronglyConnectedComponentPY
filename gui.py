from graph import Graph

#Drow
import matplotlib.pyplot as plt
import networkx as nx
from PyQt4 import QtGui
#Import
import ast
import sys

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.button = QtGui.QPushButton('Display value', self)
        self.button.clicked.connect(self.handleButton)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)

        self.textbox = QtGui.QLineEdit(self)
        self.textbox.insert("[(1, 0),(0, 2),(2, 1),(0, 3),(3, 4)]")
        layout.addWidget(self.textbox)
        #self.textbox.move(20, 20)
        #self.textbox.resize(280,40)
        self.label = QtGui.QLabel()
        self.label.setText("Hello")
        layout.addWidget(self.label)

    def handleButton(self):
        graphValue = str(self.textbox.text())
        myGraph = ast.literal_eval(graphValue)
        g = Graph(len(myGraph))
        for x in myGraph:
            g.addEdge(int(x[0]), int(x[1]))
        self.label.setText(str(g.printSCCs()))

        #drow
        G = nx.DiGraph()
        G.add_edges_from(myGraph)
        val_map = {'A': 1.0,
                   'D': 0.5714285714285714,
                   'H': 0.0}

        values = [val_map.get(node, 0.25) for node in G.nodes()]
        red_edges = [('A', 'C'), ('E', 'C')]
        edge_colours = ['black' if not edge in red_edges else 'red'
                        for edge in G.edges()]
        black_edges = [edge for edge in G.edges() if edge not in red_edges]

        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),node_color = values, node_size = 500)
        nx.draw_networkx_labels(G, pos)
        # nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
        nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
        plt.show()



if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
