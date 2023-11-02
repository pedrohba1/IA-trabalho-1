
from .is_valid_move import is_valid_move
from typing import Any
import networkx as nx
from .sudoku_types import Sudoku



def find_neighbors(state: Sudoku, G: Any = None) -> list[Sudoku] :
    """
    Generate all valid successor states from the current state.
'   The successors are simply the valid values for the first position of 
    empty cell it finds.
    Args:
        G (nx.DiGraph): the Sudoku directed graph. In this scenario it is not
        necessary to use it to generate the next states, but as for pattern for other
        types of problems, it is inserted here.
        state (list[list[int]]): A Sudoku, representing the state from which to generate
        neighbors

    Returns:
        _type_:
    """
    N = len(state)  # Assuming a square grid
    successors = []

    # Find the first empty cell
    for i in range(N):
        for j in range(N):
            if state[i][j] == -1:  # Assuming -1 represents an empty cell
                # Try filling the cell with a valid number
                for num in range(1, N + 1):
                    if is_valid_move(state, i, j, num):  # Assuming you have a function to check validity
                        new_state = [row[:] for row in state]  # Make a deep copy
                        new_state[i][j] = num
                        successors.append(new_state)
                return successors  # Return after the first empty cell is processed

    return successors  # In case there are no empty cells
