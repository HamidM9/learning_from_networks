import networkx as nx


def degree_preserving_random_graph(G, swap_attempts=10):

    G_random = G.copy()

    total_swaps = swap_attempts * len(G.edges())
    max_tries = min(total_swaps * 2, 100000)

    try:
        success = nx.directed_edge_swap(G_random, nswap=total_swaps, max_tries=max_tries)
        if not success:
            print(
                f"Warning: Could only perform {success} swaps out of {total_swaps}. The randomization may be partial.")
    except nx.NetworkXAlgorithmError as e:
        print(f"Edge swapping failed: {e}")
        print("Returning partially randomized graph.")

    return G_random


def save_randomized_network(G_random, output_file):

    nx.write_edgelist(G_random, output_file, data=False)
    print(f"Randomized directed network saved to: {output_file}")


def generate_and_save_random_graph(input_file, output_file, swap_attempts=10):

    G = nx.read_edgelist(input_file, nodetype=int, create_using=nx.DiGraph())
    G_random = degree_preserving_random_graph(G, swap_attempts)
    save_randomized_network(G_random, output_file)



input_file = "../ca-CSphd.txt"
output_file = "../randomized_network_ca-CSphd.txt"

generate_and_save_random_graph(input_file, output_file)
