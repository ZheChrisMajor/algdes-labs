# python main.py < ../data/G-ex.txt
#requires mat.plotlib and 
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
# print(few(labels, colors, edges, weights, source, sink))
print(many(labels, colors, edges, weights, source, sink))
