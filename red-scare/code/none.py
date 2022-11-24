import igraph as ig
import matplotlib.pyplot as plt
from igraph import Graph

def noneEdgeFilter(labels, colors, source, sink, edge):
    blue_one = colors[edge[0]] == 'blue'
    blue_two = colors[edge[1]] == 'blue'
    not_source_or_sink_blue = ((blue_one and edge[0] not in list([labels[source], labels[sink]])) or 
        (blue_two and edge[1] not in list([labels[source], labels[sink]])))
    has_source = labels[source] in edge
    has_sink = labels[sink] in edge
    
    #Filter to and from blue vertices unless source or sink.
    return (
        (blue_one and blue_two) or
        (not_source_or_sink_blue and (has_source or has_sink)) or
        (has_source and has_sink)
    )

def none(labels, colors, edges, weights, source, sink):
    # Only use edges from and to black nodes or source/sink
    filtered_edges = list(filter(lambda edge: noneEdgeFilter(labels, colors, source, sink, edge), edges))
    j = Graph(n=len(labels), edges=filtered_edges, directed=True)
    j.vs['label'] = list(labels.keys())
    j.vs['color'] = colors
    result = j.distances(labels[source], labels[sink])[0][0]
    if result == float("inf"):
        return -1
    return result