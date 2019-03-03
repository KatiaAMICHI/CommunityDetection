import pandas as pd
import networkx as nx


def graph_reader(input_path):
    """
    methode pour lire un fichier de "input_path" et renvoie un graph
    :param input_path:          fichier à lire.
    :return graph:              Networkx graph, graphe a renvoyer.
    """
    edges = pd.read_csv(input_path, header=4, sep='\t')
    graph = nx.from_edgelist(edges.values.tolist())
    return graph
