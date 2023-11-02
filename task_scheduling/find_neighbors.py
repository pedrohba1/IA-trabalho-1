import itertools


from .system_types import SystemState, ProcessorState, Task
import networkx as nx


def find_neighbors(current_state: SystemState, G: nx.DiGraph) -> list[SystemState]:
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

    # identify completed tasks
    completed_tasks = {task.node_id for processor in current_state.processors for task in processor.tasks}

    # Identify scheduled tasks
    task_to_processor = {task.node_id: idx for idx, processor in enumerate(current_state.processors) for task in processor.tasks}
    
    # Identify tasks ready for execution (all predecessors are completed)
    ready_tasks = [node for node in G.nodes() if node not in completed_tasks and all(pred in completed_tasks for pred in G.predecessors(node))]


    # Assign ready tasks to processors
    for ready_task in ready_tasks:
        execution_time = G.nodes[ready_task]['execution_time']
        dependencies = list(G.predecessors(ready_task))

        # Add the task to an existing processor's task list
        for idx, processor in enumerate(current_state.processors):
            task_communication_time = 0
            # Initialize communication time to zero
            task_to_schedule = Task(
            node_id=ready_task, execution_time=execution_time,
            dependencies=dependencies
            )
            # Check each of the task's dependencies
            for pred in task_to_schedule.dependencies:
                # Check if the dependency was processed on a different processor
                if task_to_processor[pred] != idx:
                    # Add the communication time from the graph
                    task_communication_time += G[pred][ready_task]['weight']
            
            # Now we have the total communication time for the task to be scheduled
            task_to_schedule.communication_time = task_communication_time
            
            # Schedule the task on the current processor
            new_tasks = processor.tasks + [task_to_schedule]
            new_processor = ProcessorState(tasks=new_tasks)
            new_processors = current_state.processors[:idx] + [new_processor] + current_state.processors[idx+1:]
            next_states.append(SystemState(processors=new_processors))

    return next_states



