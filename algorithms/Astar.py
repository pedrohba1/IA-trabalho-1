# Author: Pedro Bufulin


import heapq
from collections import namedtuple

# Define a structure for our nodes/states.
Node = namedtuple('Node', ['cost', 'heuristic_cost', 'total_cost',
                  'state', 'parent', 'state_id'])  # Added state_id

# The actual implementations of `goal_check`, `find_neighbors`, `heuristic`, and `cost_between`
#  will depend on the problem you're solving (e.g., Sudoku, task scheduling, pathfinding).


def Astar(initial_state, goal_check, find_neighbors, heuristic, cost_between):
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

   # This dictionary will map each unique ID to a unique state.
    id_to_state = {1: initial_state}  # The initial state gets ID 1
    next_id = 2  # The next available unique ID

    # Create the priority queue as a heap structure.
    open_set = []

    # Create a dictionary to hold the cost values to reach each node (g-cost), but indexed by state ID now.
    g_cost = {1: 0}  # The initial state (ID 1) has a g-cost of 0.

    # Create the start node with an initial ID.
    start_node = Node(cost=0, heuristic_cost=heuristic(initial_state), total_cost=heuristic(initial_state),
                      state=initial_state, parent=None, state_id=1)  # Added state_id

    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if goal_check(current_node.state):
            # Adjusted function call
            return reconstruct_path(current_node, id_to_state), current_node.cost

        for neighbor_state in find_neighbors(current_node.state):
            tentative_g_cost = current_node.cost + \
                cost_between(current_node.state, neighbor_state)

            neighbor_state_id = None  # We will determine this ID soon.

            # Check if this state is new. If it is, assign a new ID.
            # Look through the dictionary values.
            if neighbor_state not in id_to_state.values():
                neighbor_state_id = next_id
                # Store the new state with its ID
                id_to_state[next_id] = neighbor_state
                next_id += 1
            else:
                # If it's an already encountered state, fetch the corresponding ID.
                for state_id, state in id_to_state.items():
                    if state == neighbor_state:
                        neighbor_state_id = state_id
                        break

            if neighbor_state_id not in g_cost or tentative_g_cost < g_cost[neighbor_state_id]:
                g_cost[neighbor_state_id] = tentative_g_cost

                neighbor_node = Node(
                    cost=tentative_g_cost,
                    heuristic_cost=heuristic(neighbor_state),
                    total_cost=tentative_g_cost + heuristic(neighbor_state),
                    state=neighbor_state,
                    parent=current_node,
                    state_id=neighbor_state_id  # Added state_id
                )

                heapq.heappush(open_set, neighbor_node)

    # If we've checked all nodes and not found the goal, return None.
    return None, float('inf')


def reconstruct_path(node, id_to_state):
    """
    Reconstruct the path from the start state to the given node.

    Arguments:
    node -- The ending node.

    Returns:
    A list of states representing the path from the start to the end.
    """
    path = []
    while node.parent is not None:
        path.append(id_to_state[node.state_id])  # Use the ID to fetch the actual state
        node = node.parent
    path.append(id_to_state[node.state_id])  # For the initial state
    return path[::-1]  # Reversed path from start to goal.
