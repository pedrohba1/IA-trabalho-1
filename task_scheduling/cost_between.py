import networkx as nx
from .system_types import SystemState


def cost_between(G: nx.DiGraph, state1: SystemState, state2: SystemState) -> float:
    """_summary_

    Args:
        G (nx.DiGraph): _description_
        state1 (SystemState): _description_
        state2 (SystemState): _description_

    Returns:
        float: _description_
    """

    return abs(state1.end_time - state2.end_time)
