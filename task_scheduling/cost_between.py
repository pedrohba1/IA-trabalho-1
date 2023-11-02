import networkx as nx
from .system_types import SystemState


def cost_between(state1: SystemState, state2: SystemState, G: nx.DiGraph) -> float:
    """_summary_

    Args:
        G (nx.DiGraph): the task graph. Won't be used here, but is needed for compatibility with the other function
        state1 (SystemState): state to compare
        state2 (SystemState): state to compare

    Returns:
        float: the absolute value between the end time of both SystemState.
    """

    return abs(state1.end_time - state2.end_time)
