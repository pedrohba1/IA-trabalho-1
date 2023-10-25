
from .system_types import SystemState
import networkx as nx


def heuristic(searchSpace: nx.DiGraph, state: SystemState) -> float:
    """
    Calculates the heuristic value for a given SystemState based on the critical path approach.

    In the critical path approach, we attempt to estimate the time cost of executing all tasks
    in a single processor.

    Args:
        searchSpace (nx.DiGraph): A directed graph that contains all tasks with their execution times
                                  and weighted edges representing communication time between tasks.
        state (SystemState): The current state of the system.

    Returns:
        float: The heuristic value representing the estimated cost to reach the goal from the current state.
    """
    
    # Get all unscheduled tasks
    scheduled_tasks = set()
    for processor in state.processors:
        for task in processor.tasks:
            scheduled_tasks.add(task.node_id)
    
    unscheduled_tasks = set(searchSpace.nodes()) - scheduled_tasks
    
    # If all tasks are scheduled, the heuristic value is 0
    if not unscheduled_tasks:
        return 0.0
    
    # Create a subgraph containing only the unscheduled tasks
    subgraph = searchSpace.subgraph(unscheduled_tasks).copy()

    # Calculate the longest path in the subgraph, accounting for execution time and communication time
    critical_path = 0.0
    for path in nx.all_simple_paths(subgraph, source=min(unscheduled_tasks), target=max(unscheduled_tasks)):
        time_cost = sum([subgraph.nodes[node]['execution_time'] for node in path])
        
        # Add communication time between dependent tasks
        for i in range(len(path) - 1):
            time_cost += subgraph[path[i]][path[i+1]].get('weight', 0)
        
        critical_path = max(critical_path, time_cost)

    return critical_path