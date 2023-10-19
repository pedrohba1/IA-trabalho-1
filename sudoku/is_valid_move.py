# Additional utility function you might need for `find_neighbors`:
def is_valid_move(grid, row, col, num):
    """
    Check if placing `num` in the specified row and column is a valid move.

    Arguments:
    grid -- A 2D list representing the Sudoku grid.
    row -- The row index where the number is to be placed.
    col -- The column index where the number is to be placed.
    num -- The number to be placed in the specified position.

    Returns:
    True if it is a valid move, False otherwise.
    """
    # Check if 'num' is not in the specified row and column.
    for i in range(len(grid)):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    return True
