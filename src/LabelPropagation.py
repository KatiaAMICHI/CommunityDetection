import gc
import random

import networkx as nx
from tqdm import tqdm

from src.plot_read_data import graph_reader

# file = r"../res/com-youtube.ungraph.txt"
# file_test = r"../res/test0.txt"
# file_graph = r"../res/com-youtube.ungraph.txt"

gc.disable()


class LabelPropagation:
    """
        Label propagation class.
    """

    def __init__(self, graph):
        self.graph = graph
        self.nodes = list(graph.nodes())
        self.edges = list(nx.edges(self.graph))

        # Step 1: give a unique label to each node in the network
        self.labels = {node: node for node in self.nodes}

        self.nb_label = len(set(self.labels.values()))
        self.edges_common_count = self.common_count_generator()
        self.end_propagation = False

    def common_count(self, node_1, node_2):
        """
        methode qui renvoie le nombre de voisin en commun entre deux noeud
        :param graph:           NetworkX graph.
        :param node_1:      le preimier noeud de edge.
        :param node_2:      le second noeud de edge.
        """
        return int(len(set(nx.neighbors(self.graph, node_1)).intersection(set(nx.neighbors(self.graph, node_2)))))

    def common_count_generator(self):
        """

        :return: un dictionnaire pour chaque arete le nombre de voisin commun entre deux noeud
        """

        return {edge: self.common_count(edge[0], edge[1]) for edge in tqdm(self.edges)}

    def get_edges_common_count(self, neighbor, node_root):
        return self.edges_common_count[(neighbor, node_root)] \
            if (neighbor, node_root) in self.edges_common_count.keys() \
            else self.edges_common_count[(node_root, neighbor)]

    def set_labels(self, node_root, neighbors):
        scores = {}

        scores = {neighbor: (self.get_edges_common_count(neighbor, node_root) if not neighbor in scores.keys()
                             else (scores[neighbor] + self.get_edges_common_count(neighbor, node_root))) for neighbor in
                  tqdm(neighbors)}

        max_label = [k for k, v in scores.items() if v == max(scores.values())]

        if self.labels[node_root] not in max_label:
            self.labels[node_root] = random.sample(max_label, 1)[0]
        del scores, max_label

    def propagation(self):
        # Step 2: Arrange the nodes in the network in a random order
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
        del i

# graph = graph_reader(file_graph)
# label_propagation = LabelPropagation(graph)
# label_propagation.loop_propagation(10)
