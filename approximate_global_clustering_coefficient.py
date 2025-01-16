import networkx as nx
import random
import numpy as np

def approximate_global_clustering(G, num_samples):

    nodes = list(G.nodes())
    sampled_nodes = random.sample(nodes, min(num_samples, len(nodes)))

    clustering_values = [nx.clustering(G, node) for node in sampled_nodes]
    return np.mean(clustering_values) if clustering_values else 0

G = nx.read_edgelist("../ca-MathSciNet.txt", nodetype=int)

approx_clustering = approximate_global_clustering(G, num_samples=50000)
print("Approximated Global Clustering Coefficient:", approx_clustering)
