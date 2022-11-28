import igraph as ig
import matplotlib.pyplot as plt
from igraph import Graph

# Filter function - no two connected nodes can have the same color
def alternateEdgeFilter(colors, edge):
    return colors[edge[0]] != colors[edge[1]]

def alternate(labels, colors, edges, weights, source, sink):
    filtered_edges = list(filter(lambda edge: alternateEdgeFilter(colors, edge), edges))
    j = Graph(n=len(labels), edges=filtered_edges, directed=True)
    j.vs['label'] = list(labels.keys())
    j.vs['color'] = colors
    test = j.distances(labels[source], labels[sink])
    result = test[0][0]
    if result == float("inf"):
        return "false"
    return "true"