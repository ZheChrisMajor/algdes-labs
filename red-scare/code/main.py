# python code/main.py < ../data/<file>.txt
# requires mat.plotlib and igraph
import igraph as ig
import matplotlib.pyplot as plt
from igraph import Graph
from few import few
from alternate import alternate
from none import none
from many import many
from some import some
from parse import parseInput
import sys

sys.stdout = open("./code/result.txt", "a")


""" iGraph config """
ig.config['plotting.backend'] = 'matplotlib'

"""Run"""
labels, colors, edges, weights, source, sink = parseInput()

result_none = none(labels, colors, edges, weights, source, sink)
result_alternate = alternate(labels, colors, edges, weights, source, sink)
result_few = few(labels, colors, edges, weights, source, sink)
result_many = many(labels, colors, edges, weights, source, sink)
result_some = some(labels, colors, edges, weights, source, sink)
print(sys.argv[1], len(labels),result_alternate, result_few, result_many, result_none, result_some, sep="\t")
