import networkx as nx

def reconstruct_path(came_from: dict, current_node: int, graph: nx.digraph) -> list:
    """
    Reconstructs the path from the start node to the current node (usually the goal).
    """
    total_path = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        # Inserts at the beginning of the list
        total_path.insert(0, current_node)
    # Returns the list of states, not node IDs.
    return [graph.nodes[node]['state'] for node in total_path]
