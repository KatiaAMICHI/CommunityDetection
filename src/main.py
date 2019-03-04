#!/usr/bin/python3.6
# coding: utf-8

from src.plot_read_data import graph_reader, plot_graph
from src.LabelPropagation import LabelPropagation
import time

file = r"../res/com-youtube.ungraph.txt"
file_test = r"../res/test0.txt"
file_graph = r"../res/com-youtube.ungraph.txt"
NB_LOOP = 100000000000000000


def run():
    graph = graph_reader(file_test)
    print("list(graph.nodes()) : ", list(graph.nodes()))
    label_propagation = LabelPropagation(graph)

    start_time = time.time()
    label_propagation.loop_propagation(NB_LOOP)
    print("PY Temps d execution : %s secondes ---" % (time.time() - start_time))
    labels = label_propagation.get_labels()
    plot_graph(graph, labels=labels)


if __name__ == "__main__":
    run()
