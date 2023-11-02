import networkx as nx
from .system_types import SystemState


def goal_check(system_state: SystemState, G: nx.DiGraph) -> bool:
    """
    Checks if all tasks are scheduled across the processors.

    Args:
        system_state (SystemState): The current state of the system.
        G (nx.DiGraph): A directed graph that contains all tasks, their execution times
        and communication times (weights)

    Returns:
        bool: True if all tasks are scheduled, false otherwise.
    """

    # Aggregate all scheduled tasks across all processors
    scheduled_tasks = set()
    for processor in system_state.processors:
        for task in processor.tasks:
            scheduled_tasks.add(int(task.node_id))

    # Compare against all tasks in the graph
    all_tasks = set([int(i) for i in G.nodes()])

    if scheduled_tasks == all_tasks:
        return True
    return False
