import igraph as ig
import matplotlib.pyplot as plt
from igraph import Graph

def alternateEdgeFilter(colors, edge):
    return colors[edge[0]] != colors[edge[1]]

def alternate(labels, colors, edges, weights, source, sink):
    filtered_edges = list(filter(lambda edge: alternateEdgeFilter(colors, edge), edges))
    j = Graph(n=len(labels), edges=filtered_edges, directed=True)
    j.vs['label'] = list(labels.keys())
    j.vs['color'] = colors
    ig.plot(j)
    plt.show()
    test = j.distances(labels[source], labels[sink])
    result = test[0][0]
    if result == float("inf"):
        return "false"
    return "true"