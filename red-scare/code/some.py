import many from many

def some(labels, colors, edges, weights, source, sink):
    return "true" if many(labels, colors, edges, weights, source, sink) > 0 else "false"

