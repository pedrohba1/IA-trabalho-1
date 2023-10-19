import random
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout


def save_graph(G, filename):
    """
    Save the graph in GEXF format to the specified file.
    """
    nx.drawing.nx_agraph.write_dot(G, filename + ".dot")


def read_graph(filename: str):
    """
    Read the graph in DOT format from the specified file.
    """
    G = nx.drawing.nx_agraph.read_dot(filename + ".dot")

    # Convert attribute values from strings
    for n, data in G.nodes(data=True):
        if 'execution_time' in data:
            data['execution_time'] = int(data['execution_time'])

    for u, v, data in G.edges(data=True):
        if 'weight' in data:
            data['weight'] = int(data['weight'])

    return G


def generate_tree(num_nodes: int):
    """
    Generate a tree with a specified number of nodes.
    """
    G = nx.DiGraph()
    for i in range(num_nodes):
        # Adding execution time to nodes
        G.add_node(i, execution_time=random.randint(1, 10))

    for i in range(1, num_nodes):
        # Random selection from existing nodes to ensure acyclic graph
        parent = random.choice(list(G.nodes)[:i])
        # Adding an edge and assigning a random weight to it (transmission time)
        G.add_edge(parent, i, weight=random.randint(1, 10))

    return G


def draw(G):
    """
    Draw the tree with edge weights and node execution times.
    """
    pos = graphviz_layout(
        G, prog='dot')  # 'dot' from graphviz creates a hierarchical layout

    # Extracting the transmission time
    edge_labels = nx.get_edge_attributes(G, 'weight')
    node_labels = {i: f"{i}\n({data['execution_time']})" for i, data in G.nodes(
        data=True)}  # Creating labels with execution time

    # Draw nodes, edges, labels, and edge labels
    nx.draw(G, pos, labels=node_labels, with_labels=True, node_size=2000,
            node_color='skyblue', font_size=10, font_weight='bold', arrowsize=20)
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=edge_labels, font_color='red')

    plt.title("Task Tree")
    plt.show()


if __name__ == "__main__":
    num_nodes = 10  # Specify the number of nodes in the tree
    tree = generate_tree(num_nodes)
    save_graph(tree, "test")
    draw(tree)
