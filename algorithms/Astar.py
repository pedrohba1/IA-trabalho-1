# Author: Pedro Bufulin


import networkx as nx
import heapq

from .reconstruct_path import reconstruct_path

from typing import Callable, List, Any, Tuple, Optional

GenericState = Any

GoalCheckFunc = Callable[[GenericState], bool]

FindNeighborsFunc = Callable[[nx.DiGraph, GenericState], List[GenericState]]

HeuristicFunc = Callable[[nx.DiGraph, GenericState], float]

CostFunc = Callable[[nx.DiGraph, GenericState], float]


def Astar(
    initial_state: GenericState,
        goal_check: GoalCheckFunc,
        find_neighbors: FindNeighborsFunc,
        heuristic: HeuristicFunc,
        cost_between: CostFunc,
        search_space: GenericState = None
) -> Tuple[Optional[List], nx.DiGraph]:
    """
    Implements the A* search algorithm for pathfinding in a graph. The function is a general-purpose pathfinding 
    algorithm designed to operate on any graph-like structure. This specific implementation requires the graph 
    to be represented in a way that's compatible with the provided helper functions.

    Args:
        initial_state (any): 
            The starting state of the search. This is typically a representation of a board, puzzle configuration, 
            or another state from which the search begins.

        goal_check (callable): 
            A function that takes a state and returns a boolean indicating if the goal has been reached. It is used 
            at each step of the algorithm to determine if the search is complete.

        find_neighbors (callable): 
            A function responsible for expanding (or "generating") the neighbors of the current state. It takes the 
            current state as an argument and returns a list of possible successor states. These successors are the 
            states reachable from the current state following the rules defined by the problem domain.

        heuristic (callable): 
            A function that estimates the cost (or distance) to reach the goal from the current state. This function 
            is heuristic in nature and does not need to be perfectly accurate. Instead, it guides the A* algorithm 
            in prioritizing states that seem more promising. It takes the current state as an argument and returns 
            an integer or float value representing the estimated cost.

        cost_between (callable): 
            A function that calculates the actual cost of transitioning from the current state to a neighbor state. 
            This is used by A* to track the actual cost of the path found so far. It takes two states as arguments 
            (the current state and one of its successors) and returns an integer or float representing the cost of 
            the transition.

    Returns:
        list: 
            It returns the list of the sequence of states chosen in order to find the solution. The state at the
            end of the list is the final solution. it returns None if it was unable to find a solution
    """
    G = nx.DiGraph()

    # adds the stat node
    start_node = 1
    G.add_node(start_node, state=initial_state, visited=False)
    node_counter = 1

    # Data setup
    open_set = []
    # We push the start node with a priority of 0
    heapq.heappush(open_set, (0, start_node))

    # Dictionary to keep track of actual costs from start node to current
    g_cost_map = {start_node: 0}
    # Estimated total cost from start to goal through the current node
    f_cost_map = {start_node: heuristic(initial_state, search_space)}

    # For path reconstruction: to keep track of the parent of each node.
    came_from = {}

    while open_set:
        # Pop the node with the lowest cost from the priority queue
        _, current_node = heapq.heappop(open_set)

        # Skip processing if we've already visited this node
        if G.nodes[current_node]['visited']:
            continue

        # Extract the actual state associated with the node
        current_state = G.nodes[current_node]['state']

        # Goal check
        if goal_check(current_state, search_space):
            return (reconstruct_path(came_from, current_node, G), G)

        # mark node as visited
        G.nodes[current_node]['visited'] = True

        neighbors = find_neighbors(current_state, search_space)
        for neighbor in neighbors:
            # add neighbors to the graph first
            node_counter += 1
            # New path is better, update the parent
            came_from[node_counter] = current_node
            G.add_node(node_counter, state=neighbor, visited=False)
            G.add_edge(current_node, node_counter, weight=cost_between(
                G.nodes[current_node]['state'],
                G.nodes[node_counter]['state'], G)
            )

            child_g_cost = g_cost_map[current_node] + \
                G[current_node][node_counter]['weight']

            if node_counter not in g_cost_map or child_g_cost < g_cost_map[node_counter]:
                # This path to neighbor is better than any previous one. Record it
                g_cost_map[node_counter] = child_g_cost
                f_cost_map[node_counter] = child_g_cost + \
                    heuristic(neighbor, search_space)

                # Add the neighbor to the open set if not already present
                heapq.heappush(
                    open_set, (f_cost_map[node_counter], node_counter))

    print("Failed to reach the goal.")
    # or an empty path, or whatever signals failure appropriately in your application.
    return (None, None)
