# python code/main.py < ../data/<file>.txt
# requires mat.plotlib and igraph
import igraph as ig
import matplotlib.pyplot as plt
from igraph import Graph
from few import few
from alternate import alternate
from none import none
from many import many
from parser import parseInput


""" iGraph config """
ig.config['plotting.backend'] = 'matplotlib'

"""Run"""
labels, colors, edges, weights, source, sink = parseInput()
# print(none(labels, colors, edges, weights, source, sink))
# print(alternate(labels, colors, edges, weights, source, sink))
print("few: ",few(labels, colors, edges, weights, source, sink))
print("many: ",many(labels, colors, edges, weights, source, sink))
