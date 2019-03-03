from src.plot_read_data import graph_reader
from src.LabelPropagation import LabelPropagation

file = r"../res/com-youtube.ungraph.txt"
file_test = r"../res/test0.txt"
file_graph = r"../res/com-youtube.ungraph.txt"
NB_LOOP = 2


def run():
    graph = graph_reader(file_test)
    label_propagation = LabelPropagation(graph)
    label_propagation.loop_propagation(NB_LOOP)


if __name__ == "__main__":
    run()
