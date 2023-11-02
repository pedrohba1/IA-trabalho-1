# Author: Pedro Bufulin

import networkx as nx
import heapq

from .reconstruct_path import reconstruct_path

from typing import Callable, List, Any

GenericState = Any
GoalCheckFunc = Callable[[GenericState], bool]
FindNeighborsFunc = Callable[[nx.DiGraph, GenericState], List[GenericState]]
HeuristicFunc = Callable[[nx.DiGraph, GenericState], float]


def greedy_search(
        searchSpace: GenericState,
        initial_state: GenericState,
        goal_check: GoalCheckFunc,
        find_neighbors: FindNeighborsFunc,
        heuristic: HeuristicFunc) -> list:
    """
    Implements the Greedy Best-First Search algorithm for pathfinding in a graph. This function is a general-purpose 
    pathfinding algorithm designed to operate on any graph-like structure. This specific implementation requires the 
    graph to be represented in a way that's compatible with the provided helper functions.

    The function arguments remain the same as the A* implementation except for the cost function, 
    which is not used in greedy best-first search.

    Returns:
        list: 
            It returns the list of the sequence of states chosen in order to find the solution. The state at the
            end of the list is the final solution. it returns None if it was unable to find a solution.
    """
    G = nx.DiGraph()

    # Adds the start node
    start_node = 1
    G.add_node(start_node, state=initial_state)
    node_counter = 1

    # Data setup
    open_set = []
    # We push the start node with a priority from the heuristic function
    heapq.heappush(open_set, (heuristic(
        searchSpace, initial_state), start_node))

    visited_nodes = set()  # Set to keep track of visited nodes
    came_from = {}  # For path reconstruction

    while open_set:
        # Pop the node with the lowest heuristic cost from the priority queue
        _, current_node = heapq.heappop(open_set)

        # Skip processing if we've already visited this node
        if current_node in visited_nodes:
            continue

        # Extract the actual state associated with the node
        current_state = G.nodes[current_node]['state']

        # Goal check
        if goal_check(searchSpace, current_state):
            return reconstruct_path(came_from, current_node, G)

        visited_nodes.add(current_node)  # Mark the node as visited

        neighbors = find_neighbors(searchSpace, current_state)
        for neighbor in neighbors:
            # Add neighbors to the graph first
            node_counter += 1
            came_from[node_counter] = current_node
            G.add_node(node_counter, state=neighbor)

            # No need to calculate g_cost since it's not used in greedy search

            # Check if neighbor is already visited or in open set
            if node_counter not in visited_nodes:
                # Use heuristic alone for priority
                h_cost = heuristic(searchSpace, neighbor)

                # Add the neighbor to the open set if not already present
                heapq.heappush(open_set, (h_cost, node_counter))

    print("Failed to reach the goal.")
    return None