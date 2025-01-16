import networkx as nx

def degree_preserving_random_graph(G, swap_attempts=10):

    G_random = G.copy()
    nx.double_edge_swap(G_random, nswap=swap_attempts * len(G.edges()), max_tries=swap_attempts * len(G.edges()) * 10)
    return G_random

def save_randomized_network(G_random, output_file):

    nx.write_edgelist(G_random, output_file, data=False)
    print(f"Randomized network saved to: {output_file}")

def generate_and_save_random_graph(input_file, output_file, swap_attempts=10):


    G = nx.read_edgelist(input_file, nodetype=int)
    G_random = degree_preserving_random_graph(G, swap_attempts)
    save_randomized_network(G_random, output_file)


input_file = "../ca-netscience.txt"
output_file = "../randomized_network_ca-netscience.txt"

generate_and_save_random_graph(input_file, output_file)
