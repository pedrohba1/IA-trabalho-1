
from .system_types import SystemState
import networkx as nx


def heuristic(state: SystemState, searchSpace: nx.DiGraph) -> float:
    """
    Calculates the heuristic value for a given SystemState based on the most resources required.

    This approach estimates the time cost by considering the execution time for the
    most resource-intensive remaining unscheduled tasks. This heuristic is admissible because
    it does not overestimate the cost, since it assumes perfect parallelization, which is 
    never worse than the actual scheduling outcome

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

    # Calculate the maximum execution time among the unscheduled tasks
    most_resources_required = sum([searchSpace.nodes[task]['execution_time']
                                  for task in unscheduled_tasks]) / len(state.processors)

    return most_resources_required
