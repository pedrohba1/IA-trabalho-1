import itertools


from .system_types import SystemState, ProcessorState, Task
import networkx as nx


def find_neighbors(G: nx.DiGraph, current_state: SystemState) -> list[SystemState]:
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
    task_to_processor = {}
    for idx, processor in enumerate(current_state.processors):
        for task in processor.tasks:
            task_to_processor[task.node_id] = idx
            completed_tasks.add(task.node_id)

    # Identify tasks ready for execution (all predecessors are completed)
    ready_tasks = []
    for node in G.nodes():
        if node not in completed_tasks:
            predecessors = list(G.predecessors(node))
            if all(pred in completed_tasks for pred in predecessors):
                ready_tasks.append(node)

    # Assign ready tasks to processors
    for ready_task in ready_tasks:
        execution_time = G.nodes[ready_task]['execution_time']
        task_to_schedule = Task(
            node_id=ready_task, execution_time=execution_time)

        # Add the task to an existing processor's task list
        for idx, processor in enumerate(current_state.processors):
            task_to_schedule.communication_time = 0
            # before adding a task to a processor, we need to check
            # if the task_to_schedule has any dependencies that ran 
            # on different processors.
            # If so, increment the communication_time for each
            # dependency in the graph
            
            
            new_tasks = processor.tasks + [task_to_schedule]
            new_processor = ProcessorState(
                tasks=new_tasks)
            new_processors = current_state.processors[:idx] + [
                new_processor] + current_state.processors[idx+1:]
            next_states.append(SystemState(processors=new_processors))

    return next_states



