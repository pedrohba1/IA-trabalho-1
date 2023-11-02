import networkx as nx
import os
from typing import Callable, List, Tuple, Optional

def generate_output(
        result: Tuple[Optional[List], nx.DiGraph], filename: str,
        calculate_solution_cost: Callable) -> None:
    path, graph = result

    if path is None:
        print("No solution was found.")
        return
    # Convert path to a string representation, assuming states are named appropriately.
    path_str  = ""
    for idx, state in enumerate(path):
        path_str += f"#{idx}\n"
        path_str += str(state)


    # Calculate solution cost, assuming it can be derived from the path/states.
    solution_cost = calculate_solution_cost(path)

    # Open the file in write mode
    with open(filename, 'w') as file:
        file.write(f"Solução: \n{path_str}\n")

        # Count visited nodes
        visited_nodes_count = sum(
            1 for node in graph.nodes if graph.nodes[node].get('visited', False))

        # Depth of the goal is the length of the path minus one
        goal_depth = len(path) - 1


    # Print out the information
    file_path = os.path.abspath(filename)
    print(f"Caminho da solução escrito  em: {file_path}")
    print(f"Número de nós visitados: {visited_nodes_count}")
    print(f"Total de nós: {len(graph.nodes())}")
    print(f"Profundidade da meta: {goal_depth}")
    print(f"Custo da solução: {solution_cost}")

