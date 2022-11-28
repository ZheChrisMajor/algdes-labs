import igraph as ig
from igraph import Graph
import matplotlib.pyplot as plt

def getUndirectedWeight(vertices, edge):
    first_red = vertices[edge.source]['color'] == 'red'
    second_red = vertices[edge.target]['color'] == 'red'
    if first_red and second_red:
        return 2
    elif first_red or second_red:
        return 1
    else:
        return 0

def many(labels, colors, edges, weights, source, sink):
    j = Graph(n=len(labels), edges=edges, directed=True)
    j.vs['label'] = list(labels.keys())
    j.vs['color'] = colors
    if (j.is_dag()):
        # Negate all edgeweights, to run shortest path normally
        j.es['weight'] = list(map(lambda x: -x, weights))
        result = j.distances(labels[source], labels[sink], j.es['weight'])[0][0]
        if result != float("inf"):
            result = result*-1
            return int(result + 1 if colors[labels[source]] == 'red' else result)
        else: 
            return -1
    else:    
        for comp in j.decompose():
            if source in comp.vs['label'] and sink in comp.vs['label']:
                comp.to_undirected()
                if comp.is_tree():
                    comp.es['weight'] = list(map(lambda x: getUndirectedWeight(comp.vs, x), comp.es))
                    source_new_id = list(comp.vs['label']).index(source)
                    sink_new_id = list(comp.vs['label']).index(sink)
                    return int(comp.distances(source_new_id, sink_new_id, comp.es['weight'])[0][0] / 2)
            else:   
                return -1
    return "-"