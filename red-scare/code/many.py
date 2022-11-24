import igraph as ig
from igraph import Graph
import matplotlib.pyplot as plt

def many(labels, colors, edges, weights, source, sink):
    j = Graph(n=len(labels), edges=edges, directed=True)
    j.vs['label'] = list(labels.keys())
    j.vs['color'] = colors
    ig.plot(j)
    plt.show()
    # if (j.isDag()):
    #     # Do something
    # elif (j.isForest()):
    #     # Do something
    # else:
        # You done fucked up
        


