from .system_types import SystemState, ProcessorState, Task, List
import networkx as nx

def initialize_system(G: nx.digraph, processors_amount:int) -> SystemState:
    """_summary_

    Args:
        G (nx.digraph): A digraph where the nodes represent the tasks and the weights represent 
        the communication time between the tasks.

        processors_amount (int): the amount of processors. (it will usually be 2)

    Returns:
        SystemState: a representation of the state of task scheduling
    """
    root = [node for node, degree in G.in_degree() if degree == 0]
   # Validate the graph: It should have exactly one root.
    if not root:
        raise ValueError("The graph must have a root node (a node with no incoming edges).")

    if len(root) > 1:
        raise ValueError("The graph must have exactly one root node. Multiple root nodes found.")

    root_node = root[0]
    # Extract execution time from the graph's node attribute
    execution_time = G.nodes[root_node]['execution_time']

    # Prepare the initial state of the system
    system_state = SystemState()  # Creates a SystemState instance with an empty list of processors

    # Initialize ProcessorStates and add them to the system state
    for _ in range(processors_amount):
        # Creates ProcessorState instances with empty task lists and adds them
        processor_state = ProcessorState()
        system_state.processors.append(processor_state)

    # Assign the first task (from the root node) to the first processor
    root_task = Task(node_id=root_node, execution_time=execution_time)
    system_state.processors[0].tasks.append(root_task)
    system_state.processors[0].total_time += execution_time  # Update the total execution time

    return system_state
