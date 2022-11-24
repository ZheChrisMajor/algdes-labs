
def parseInput():
    num_vertices, num_edges, num_reds = map(int, input().split())
    source, sink = input().split()
    #print(num_vertices,num_edges,num_reds)
    #print(source,sink)
    labels = {}
    colors = []
    for i in range(num_vertices):
        name = input().strip()
        red = ' *' in name
        name = name.split()[0] if red else name
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
