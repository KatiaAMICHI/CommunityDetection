#!/usr/bin/python3.6
# coding: utf-8

import gc
import random
import time

import networkx as nx
from tqdm import tqdm

from src.Community import Community

file = r"../res/com-youtube.ungraph.txt"
file_test = r"/home/katy/PycharmProjects/CommunityDetection/res/test0.txt"
file_graph = r"/home/katy/PycharmProjects/CommunityDetection/res/com-youtube.ungraph.txt"
NB_LOOP = 2

gc.disable()


class LabelPropagation(Community):
    """
        Label propagation class.
    """

    def __init__(self, graph):
        Community.__init__(self, graph)

    def propagation(self):
        # Step 2: Arrange the nodes in the network in a random order
        global neighbors
        random.shuffle(self.nodes)

        # Step 3: for each node in the network (in this random order)
        # set its label to a label occurring with the highest frequency
        # among its neighbours
        for node in tqdm(self.nodes):
            # charger tous les voisin de noeud courant
            neighbors = nx.neighbors(self.graph, node)
            # changer le label par le voison avec le plus grand score
            self.set_labels(node, neighbors)

        current_label_count = len(set(self.labels.values()))

        if self.nb_label == current_label_count:
            self.end_propagation = True
        else:
            self.nb_label = current_label_count
        del current_label_count

        if neighbors:
            del neighbors

    def loop_propagation(self, nb_loop):
        i = 0
        print("\n%d communauté au début avant propagation. \n" % (self.nb_label))

        while i < nb_loop and not self.end_propagation:
            self.propagation()
            print("\nPropagation num : %d, avec %d nombre de communauté.\n" % (nb_loop, self.nb_label))
            i += 1
        print(" edges_common_count : ", self.labels)

        del i

    def get_labels(self):
        return self.labels

    def __str__(self):
        return "[{}:{}]: {}".format(len(set(self.labels.values())), self.nb_label,
                                    self.end_propagation)




