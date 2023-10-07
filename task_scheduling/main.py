import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_random_dag(num_nodes, num_edges, weight_range=(1, 10)):
    """
    Generates a random Directed Acyclic Graph (DAG) with given nodes and edges.
    
    Parameters:
    - num_nodes: Number of nodes
    - num_edges: Number of edges
    - weight_range: Tuple of (min_weight, max_weight)
    
    Returns:
    - G: A NetworkX DiGraph representing the DAG
    """
    
    G = nx.DiGraph()
    for i in range(num_nodes):
        G.add_node(i)

    while G.number_of_edges() < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        
        # Ensure the graph remains acyclic and there's no self-loop
        if u != v and nx.has_path(G, v, u) == False and not G.has_edge(u, v):
            weight = random.randint(*weight_range)
            G.add_edge(u, v, weight=weight)
    
    return G

def draw_graph(G):
    """
    Draws the graph with edge weights.
    """
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

if __name__ == '__main__':
    num_nodes = 10
    num_edges = 15
    G = generate_random_dag(num_nodes, num_edges)
    draw_graph(G)
