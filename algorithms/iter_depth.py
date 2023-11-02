# Author: Vitor Ramos

import networkx as nx

from typing import Callable, List, Any, Tuple

GenericState = Any
GoalCheckFunc = Callable[[GenericState, GenericState], bool]
FindNeighborsFunc = Callable[[GenericState, GenericState], List[GenericState]]


def iter_depth_search(
        initial_state: GenericState,
        goal_check: GoalCheckFunc,
        find_neighbors: FindNeighborsFunc,
        max_depth: int,
        search_space: GenericState = None,
) -> Tuple[list[GenericState], nx.DiGraph]:
    """
    Implements the iterative depth search first.
    Args:
        initial_state (GenericState):
            The starting state of the search.

        goal_check (GoalCheckFunc):
            A function that checks if the current state is the goal state.

        find_neighbors (FindNeighborsFunc):
            A function that generates the neighbors of a given state.

        max_depth (int):
            a value to limit the depth of the search.
              
        search_space (GenericState):
            The environment or space in which the search is taking place.
            Usually a graph.
    Returns:
        List[GenericState]: 
            A list representing the path from the initial state to the goal state,
            or an empty list if no path is found.
    """
    # initialize the solution graph
    G = nx.DiGraph()

    # Add the start node
    start_node = 1
    G.add_node(start_node, state=initial_state, visited=True)

    node_counter = 1
    def depth_limited_search(current_node: int, depth: int) -> list:
        nonlocal node_counter  
        nonlocal G
        # if it found a goal, return the recursion
        if depth == 0 and goal_check(G.nodes[current_node]["state"], search_space):
            return [G.nodes[current_node]["state"]]
        elif depth > 0:
            for neighbor in find_neighbors(G.nodes[current_node]["state"], search_space):
                node_counter +=1 
                G.add_node(node_counter, state=neighbor, visited=True)
                G.add_edge(current_node, node_counter, weight=0)
                path = depth_limited_search(node_counter, depth - 1)
                if path:
                    return [G.nodes[current_node]["state"]] + path
        return []

    for depth in range(max_depth):
        path = depth_limited_search(start_node, depth)
        if path:
            return (path,G)

    print("goal not found")
    return (path,G)
