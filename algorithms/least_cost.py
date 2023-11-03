# Pedro Bufulin


import networkx as nx
import heapq

from .reconstruct_path import reconstruct_path
from typing import Callable, List, Any, Tuple


GenericState = Any

GoalCheckFunc = Callable[[GenericState], bool]

FindNeighborsFunc = Callable[[nx.DiGraph, GenericState], List[GenericState]]

HeuristicFunc = Callable[[nx.DiGraph, GenericState], float]

CostFunc = Callable[[nx.DiGraph, GenericState], float]


def least_cost_path(
        initial_state: GenericState,
        goal_check: GoalCheckFunc,
        find_neighbors: FindNeighborsFunc,
        cost_between: CostFunc,
        search_space: GenericState = None
) -> Tuple[list[GenericState], nx.DiGraph]:
    """
    Implements the least-cost pathfinding algorithm (Dijkstra's algorithm) for graphs. The function is designed for general-purpose 
    pathfinding and operates on any graph-like structure, provided the graph is represented compatibly with the provided helper functions.

    Args:
        search_space (GenericState):
            A space to get information about the search from. Sometimes might not be necessary, in the case
            of the sudoku problem. 

        initial_state (GenericState): 
            The starting state of the search. This is typically a representation of a board, puzzle configuration, 
            or another state from which the search begins.

        goal_check (GoalCheckFunc): 
            A function that takes a state and returns a boolean indicating if the goal has been reached. It is used 
            at each step of the algorithm to determine if the search is complete.

        find_neighbors (callable): 
            A function responsible for expanding (or "generating") the neighbors of the current state. It takes the 
            current state as an argument and returns a list of possible successor states. These successors are the 
            states reachable from the current state following the rules defined by the problem domain.

        cost_between (callable): 
            A function that calculates the actual cost of transitioning from the current state to a neighbor state. 
            This is used by the algorithm to track the actual cost of the path found so far. It takes two states as 
            arguments (the current state and one of its successors) and returns an integer or float representing the 
            cost of the transition.

    Returns:
        list: 
            It returns the list of the sequence of states that the algorithm has chosen in the path to the solution. 
            The state at the end of the list is the final solution. It returns None if it was unable to find a solution.
    """
    G = nx.DiGraph()

    # Add the start node
    start_node = 1
    G.add_node(start_node, state=initial_state)
    node_counter = 1

    # Data setup
    open_set = []
    # We push the start node with a priority of
    heapq.heappush(open_set, (0, start_node))

    # it's just the actual costs, no heuristic.
    g_cost_map = {start_node: 0}

    visited_nodes = set()
    came_from = {}  # For path reconstruction

    while open_set:
        # pop the smallest element from the priority queue
        # heappop returns a tuple, containing the cost and the node.
        # We are not interested int he cost in this case, so we assign _ to it
        _, current_node = heapq.heappop(open_set)

        if current_node in visited_nodes:
            continue

        G.nodes[current_node]['visited'] = True
        current_state = G.nodes[current_node]['state']

        if goal_check(current_state, search_space):
            return (reconstruct_path(came_from, current_node, G), G)

        visited_nodes.add(current_node)

        neighbors = find_neighbors(current_state, search_space)
        for neighbor in neighbors:
            node_counter += 1
            came_from[node_counter] = current_node
            G.add_node(node_counter, state=neighbor)
            G.add_edge(current_node, node_counter, weight=cost_between(
                G.nodes[current_node]['state'],
                G.nodes[node_counter]['state'],
                G))

            g_cost = g_cost_map[current_node] + \
                G[current_node][node_counter]['weight']

            if node_counter not in g_cost_map or g_cost < g_cost_map[node_counter]:
                g_cost_map[node_counter] = g_cost
                # Here, we push only the known cost.
                heapq.heappush(open_set, (g_cost, node_counter))

    # If there is no solution, return None or appropriate failure indication.
    return (reconstruct_path(came_from, current_node, G), G)
