import networkx as nx
from .system_types import SystemState

def goal_check(G: nx.DiGraph, system_state: SystemState) -> bool:
    """
    Checks if all tasks are scheduled across the processors.

    Args:
        system_state (SystemState): The current state of the system.
        G (nx.DiGraph): A directed graph that contains all tasks.

    Returns:
        bool: True if all tasks are scheduled, false otherwise.
    """

    # Aggregate all scheduled tasks across all processors
    scheduled_tasks = set()
    for processor in system_state.processors:
        for task in processor.tasks:
            scheduled_tasks.add(task.node_id)

    # Compare against all tasks in the graph
    all_tasks = set([int(i) for i in G.nodes()])

    print(all_tasks)
    print(scheduled_tasks)

    return scheduled_tasks == all_tasks
