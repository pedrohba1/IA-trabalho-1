import networkx as nx
from .sudoku_types import Sudoku


def cost_between(state1: Sudoku, state2: Sudoku, G: nx.DiGraph = None) -> int:
    """
    Calculate the cost of moving from one state to another based on the difference in
    the number of -1 entries in the Sudoku grid.

    Args:
        G (nx.DiGraph): A Digraph representing the search space. It is not used in this 
        specific scenario of the sudoku but the param is necessary for compatibility.
        state1 (Sudoku): A sudoku representation with a grid as a 2D list or array.
        state2 (Sudoku): Another sudoku representation with a grid as a 2D list or array.

    Returns:
        int: The absolute difference in the count of -1's in each Sudoku state.
    """
    def count_neg_ones(grid):
        return sum(row.count(-1) for row in grid)

    count1 = count_neg_ones(state1)
    count2 = count_neg_ones(state2)

    return abs(count1 - count2)
