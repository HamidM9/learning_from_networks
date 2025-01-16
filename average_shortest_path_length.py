import networkx as nx
import numpy as np


G = nx.read_edgelist("../randomized_network_ca-netscience.txt", nodetype=int)


if nx.is_connected(G):
    apl = nx.average_shortest_path_length(G)
else:

    components = list(nx.connected_components(G))
    weighted_apl = np.mean([
        nx.average_shortest_path_length(G.subgraph(comp)) * (len(comp) / len(G.nodes()))
        for comp in components if len(comp) > 1
    ])
    apl = weighted_apl

print("Weighted Average Shortest Path Length:", apl)
