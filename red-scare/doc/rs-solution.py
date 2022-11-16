# python rs-solution.py < ../data/G-ex.txt
#requires mat.plotlib and 
import igraph as ig
import matplotlib.pyplot as plt
from igraph import Graph




""" iGraph config """
ig.config['plotting.backend'] = 'matplotlib'
# j = Graph(n=num_vertices, edges=edges)
# j.vs['label'] = list(labels.keys())
# j.vs['color'] = colors
# j.es['weight'] = weights
    


def parseInput():
    num_vertices, num_edges, num_reds = map(int, input().split())
    source, sink = input().split()
    print(num_vertices,num_edges,num_reds)
    print(source,sink)
    labels = {}
    colors = []
    for i in range(num_vertices):
        name = input().strip()
        red = ' *' in name      
        name = name[:-2] if red else name
        labels[name] = i
        colors.append( 'red' if red else 'blue' )

    edges = []
    weights = []
    for i in range(num_edges):
        edge = input().strip().split()
        v_from, v_to = labels[edge[0]], labels[edge[2]]
        if edge[1] == '--': # If false then '->' which is directed
            # Add aux edge also
            edges.append([v_to, v_from])
            weights.append(1 if colors[v_from] == 'red' else 0)
        edges.append([v_from, v_to])
        weights.append(1 if colors[v_to] == 'red' else 0)
    return labels, colors, edges, weights, source, sink
    
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
    ig.plot(j)
    plt.show()
    test = j.distances(labels[source], labels[sink])
    result = test[0][0]
    if result == float("inf"):
        return -1
    return result

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

def few(labels, colors, edges, weights, source, sink):   
    j = Graph(n=len(labels), edges=edges, directed=True)
    j.vs['label'] = list(labels.keys())
    j.vs['color'] = colors
    ig.plot(j)
    plt.show()
    result = j.distances(labels[source],labels[sink],weights)[0][0]
    if result == float("inf"):
        return -1
    return result 

"""Run"""
labels, colors, edges, weights, source, sink = parseInput()
# print(none(labels, colors, edges, weights, source, sink))
# print(alternate(labels, colors, edges, weights, source, sink))
print(few(labels, colors, edges, weights, source, sink))

# ax = ig.plot(j)
# plt.show()
