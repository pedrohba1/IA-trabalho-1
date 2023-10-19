import itertools


from .system_types import SystemState, ProcessorState, Task
import networkx as nx


def get_task_info(G, node):
    return (node, G.nodes[node]['execution_time'])

def is_task_complete(task, current_time):
    return current_time >= task[1]


def can_schedule(task, completed_tasks):
    # Here, you'd check if all of the task's dependencies are in completed_tasks.
    # This example doesn't use actual task dependencies.
    return True  # Simplified assumption

def find_neighbors(G: nx.DiGraph , current_state: SystemState):
    """ Generate all valid neighbors for the current state

    Args:
        G (nx.DiGraph): A directed graph that contains all nodes with their
        execution times and weighted edges where the weights represent the communication time
        between processes
        current_state (SystemState): The current state

    Returns:
        List[SystemState]: a list of valid SystemState's generated from current_state
    """
    next_states: list(SystemState) = []

    # Step 1: Identify scheduled tasks
    completed_tasks = set()
    for processor in current_state.processors:
        for task in processor.tasks:
            completed_tasks.add(task.node_id)



    return next_states