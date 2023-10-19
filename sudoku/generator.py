import random

# Assuming the 'is_valid_move' function checks whether it's valid to place a number in a certain position.
from .is_valid_move import is_valid_move


def create_sudoku_puzzle(N: int, K: int) -> list[list[int]]:
    """
    Generates a sudoku puzzle.

    Arguments:
    N -- Size of the sudoku grid (N x N).
    K -- Number of cells to leave empty in the generated puzzle.

    Returns:
    A grid of integers of NxN, with K elements missing. The missing values are marked by -1.
    """

    def generate_sudoku_solution(grid):
        """
        A recursive function that tries to fill the grid with numbers to form a valid solution.
        """
        for row in range(N):
            for col in range(N):
                if grid[row][col] == -1:
                    nums = list(range(1, N + 1))
                    # Randomize the numbers before placing them
                    random.shuffle(nums)
                    for num in nums:
                        if is_valid_move(grid, row, col, num):
                            grid[row][col] = num
                            # Recursively continue to fill up the grid
                            if generate_sudoku_solution(grid):
                                return True
                            # Backtrack if no number leads to a solution
                            grid[row][col] = -1
                    return False  # Return False if no numbers can be placed in this cell
        return True  # A solution is found if we've filled up the grid successfully

    # Create an empty Sudoku grid with -1 indicating blank spaces.
    grid = [[-1 for _ in range(N)] for _ in range(N)]

    # Generate a complete Sudoku solution randomly.
    if not generate_sudoku_solution(grid):
        # In case the solution isn't found
        raise ValueError("Solution couldn't be generated. Please try again.")

    # Randomly remove K numbers to create the puzzle, ensuring we don't remove more numbers than there are cells.
    K = min(K, N*N)  # Ensure we don't try to remove more cells than exist
    cells = [(i, j) for i in range(N) for j in range(N)]
    random.shuffle(cells)  # Randomize the cells we'll be emptying
    for i in range(K):
        row, col = cells[i]
        grid[row][col] = -1  # Remove the number by setting the cell to -1

    return grid  # Return the generated puzzle


def print_sudoku(grid: list[list[int]]):
    """
    Prints the sudoku grid in a readable format, replacing -1 with '_'.

    Arguments:
    grid -- a 2D list of integers representing the Sudoku puzzle.
    """
    for row in grid:
        # Replace -1 with underscores for visibility
        formatted_row = ['_' if x == -1 else str(x) for x in row]
        print(' '.join(formatted_row))  # Print the formatted row
