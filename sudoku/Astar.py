# Author: Pedro Bufulin


import heapq
from collections import namedtuple

# Define a structure for our nodes/states.
Node = namedtuple('Node', ['cost', 'heuristic_cost',
                  'total_cost', 'state', 'parent'])

# The actual implementations of `goal_check`, `find_neighbors`, `heuristic`, and `cost_between`
#  will depend on the problem you're solving (e.g., Sudoku, task scheduling, pathfinding).


def a_star_algorithm(initial_state, goal_check, find_neighbors, heuristic, cost_between):
    """
    Apply the A* algorithm.

    Arguments:
    initial_state -- The starting state of the problem.
    goal_check -- Function to check if the goal has been reached.
    find_neighbors -- Function to find neighboring states.
    heuristic -- Function to determine the heuristic cost from a state to the goal.
    cost_between -- Function to compute the cost between two states.

    Returns:
    A tuple (path, cost) where path is a list of states from start to goal, and cost is the total cost of the path.
    If no path is found, returns (None, float('inf')).
    """

    # Create the priority queue as a heap structure.
    open_set = []

    # Create a dictionary to hold the cost values to reach each node (g-cost).
    g_cost = {initial_state: 0}

    # Create the start node. Cost from start to start is 0.
    start_node = Node(cost=0, heuristic_cost=heuristic(
        initial_state), total_cost=heuristic(initial_state), state=initial_state, parent=None)

    # Push the start node onto the priority queue.
    heapq.heappush(open_set, start_node)

    # While there are still nodes to explore:
    while open_set:
        # Pop the node with the lowest total_cost off the priority queue.
        current_node = heapq.heappop(open_set)

        # If it's the goal, reconstruct the path and return it.
        if goal_check(current_node.state):
            return reconstruct_path(current_node), current_node.cost

        # For each neighbor of the current node's state:
        for neighbor_state in find_neighbors(current_node.state):
            # Calculate the cost to get to this neighbor.
            tentative_g_cost = current_node.cost + \
                cost_between(current_node.state, neighbor_state)

            # If we have not encountered the state yet, or we found a cheaper path to it:
            if neighbor_state not in g_cost or tentative_g_cost < g_cost[neighbor_state]:
                # Update the cost to get to the neighbor.
                g_cost[neighbor_state] = tentative_g_cost

                # Create a new node for the neighbor.
                neighbor_node = Node(
                    cost=tentative_g_cost,
                    heuristic_cost=heuristic(neighbor_state),
                    total_cost=tentative_g_cost + heuristic(neighbor_state),
                    state=neighbor_state,
                    parent=current_node
                )

                # Add the neighbor to the priority queue to explore later.
                heapq.heappush(open_set, neighbor_node)

    # If we've checked all nodes and not found the goal, return None.
    return None, float('inf')


def reconstruct_path(node):
    """
    Reconstruct the path from the start state to the given node.

    Arguments:
    node -- The ending node.

    Returns:
    A list of states representing the path from the start to the end.
    """
    path = []
    while node.parent is not None:
        path.append(node.state)
        node = node.parent
    path.append(node.state)  # The initial state.
    return path[::-1]  # Reversed path from start to goal.
