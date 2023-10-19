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

def find_neighbors(G: nx.DiGraph , current_state: SystemState, current_time: int):
    """ Generate all valid neighbors for the current state

    Args:
        G (nx.DiGraph): A directed graph that contains all nodes with their
        execution times and weighted edges where the weights represent the communication time
        between processes
        current_state (SystemState): The current state

    Returns:
        List[SystemState]: a list of valid SystemState's generated from current_state
    """
    next_states = []


    # Step 2: For each processor, try scheduling each schedulable task.
    for i, proc in enumerate(current_state):
        for task in schedulable_tasks:
            new_state = current_state.copy()
            task_list, proc_time = proc

            # Calculate new time, including transmission time if the task has dependencies.
            # This example doesn't calculate actual transmission time.
            new_time = proc_time + task[1]  # Simplified: not including transmission time

            # Schedule the task.
            new_task_list = task_list + [task]
            new_state[i] = (new_task_list, new_time)

            next_states.append(new_state)

    # Step 3: Consider starting new tasks on other processors.
    # ... (similar to step 2, but you would add new task lists rather than appending to existing ones)

    return next_states