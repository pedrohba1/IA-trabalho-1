def cost_between(state1, state2):
    """
    Calculate the cost of moving from state1 to state2. 

    Arguments:
    state1 -- The current state.
    state2 -- The neighbor state.

    Returns:
    The cost of the move. In Sudoku, this is typically constant, as each move involves placing a single number.
    """
    return 1  # Constant cost for each move in Sudoku