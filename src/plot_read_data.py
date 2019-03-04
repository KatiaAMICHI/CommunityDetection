#!/usr/bin/python3.6
# coding: utf-8

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


def graph_reader(input_path):
    """
    methode pour lire un fichier de "input_path" et renvoie un graph
    :param input_path:          fichier à lire.
    :return graph:              Networkx graph, graphe a renvoyer.
    """

    edges = pd.read_csv(input_path, header=4, sep='\t')
    graph = nx.from_edgelist(edges.values.tolist())
    return graph


def plot_graph(graph, labels=None):
    dict_community = {}

    for k, v in labels.items():
        dict_community[v] = [k] if v not in dict_community.keys() \
            else dict_community[v] + [k]

    pos = nx.spring_layout(graph)  # positions for all nodes

    color = ['green', 'blue', 'red', 'yellow', 'orange', 'magenta',
             'cyan', 'white', 'black']

    i = 0
    for k, v in dict_community.items():
        if i > len(color):
            i -= 1
        nx.draw_networkx_nodes(graph,
                               pos,
                               nodelist=v,
                               node_color=color[i],
                               node_size=500,
                               alpha=0.8)
        i += 1
    nx.draw_networkx_edges(graph, pos, width=1.0, alpha=0.5)
    dict_labels = {}

    dict_labels = {node: node for node, label in labels.items()}

    nx.draw_networkx_labels(graph, pos, dict_labels, font_size=16)

    plt.axis('off')
    # plt.savefig("labels_and_colors.png")  # save as png
    # nx.draw(graph)
    plt.show()
