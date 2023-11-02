from typing import Any


def heuristic(state: list[list[int]], searchSpace: Any = None) -> float:
    """
    Heuristic function that estimates the cost to reach the goal from the current state.

    Arguments:
    state -- A 2D list representing the Sudoku grid.

    Returns:
    An integer estimate of the cost to reach a solved state from the current state.
    """
    # For Sudoku, a simple heuristic might be the number of empty cells (-1s) in the state.
    return sum(row.count(-1) for row in state)
