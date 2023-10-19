import networkx as nx
from .sudoku_types import Sudoku


def cost_between(G: nx.DiGraph, state1: Sudoku, state2: Sudoku) -> float:
    """
    Calculate the cost of moving from one state to another. 

    In this case, since we only change one number between states, the cost can be 1.
    This can be explored further to find a better cost function.

    Args:
        G (nx.DiGraph): A Digraph representing the search space. It is not used in this 
        specific scenario of the sudoku but the param is necessary for compatibility
        state1 (Sudoku): A sudoku representation
        state2 (Sudoku): Another sudoku representation

    Returns:
        float: cost value
    """

    return 1  # Constant cost for each move in Sudoku
