from many import many as many

def some(labels, colors, edges, weights, source, sink):  
    res= many(labels, colors, edges, weights, source, sink)
    if res == "-":
        return res
    else: 
        return "true" if res > 0 else "false"
        
