#!/usr/bin/python3.6
# coding: utf-8

import gc
import networkx as nx
from src.Community import Community

file = r"../res/com-youtube.ungraph.txt"
file_test = r"/home/katy/PycharmProjects/CommunityDetection/res/test0.txt"
file_graph = r"/home/katy/PycharmProjects/CommunityDetection/res/com-youtube.ungraph.txt"
NB_LOOP = 2

gc.disable()


class Louvain(Community):
    def __init__(self, graph):
        Community.__init__(self, graph)

    def louvin_algorithm(self):
        # 3 Iterate from step 2 until the partition does not evolve
        while not self.end_propagation:
            # 2 For all u ∈ V:
            for node in self.nodes:
                # Remove node u from its community
                # Insert node u in a neighboring community that maximizes Q
                neighbors = nx.neighbors(self.graph, node)
                self.set_labels(node, neighbors)

            current_label_count = len(set(self.labels.values()))

            if self.nb_label == current_label_count:
                self.end_propagation = True
            else:
                self.nb_label = current_label_count
            del current_label_count

    # 4 Transform the communities into (hyper-)nodes and go back
    # to step 1 with the new graph
