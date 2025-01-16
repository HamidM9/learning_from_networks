import networkx as nx
import numpy as np
import random

def approximate_apl(G, num_samples):

    nodes = list(G.nodes())
    sampled_pairs = random.sample([(random.choice(nodes), random.choice(nodes)) for _ in range(num_samples)], num_samples)

    path_lengths = []
    for u, v in sampled_pairs:
        try:
            path_lengths.append(nx.shortest_path_length(G, source=u, target=v))
        except nx.NetworkXNoPath:
            continue

    return np.mean(path_lengths) if path_lengths else None


G = nx.read_edgelist("../ca-MathSciNet.txt", nodetype=int)


apl_approx = approximate_apl(G, num_samples=50000)

print("Approximated Average Shortest Path Length:", apl_approx)
