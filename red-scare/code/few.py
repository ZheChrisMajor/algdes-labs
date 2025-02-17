import igraph as ig
import matplotlib.pyplot as plt
from igraph import Graph

def few(labels, colors, edges, weights, source, sink):   
    j = Graph(n=len(labels), edges=edges, directed=True)
    j.vs['label'] = list(labels.keys())
    j.vs['color'] = colors
    result = j.distances(labels[source],labels[sink],weights)[0][0]
    if result == float("inf"):
        return -1
    return int(result + 1 if colors[labels[source]] == 'red' else result)