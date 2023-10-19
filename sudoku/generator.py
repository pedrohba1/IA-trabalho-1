import random


def create_sudoku_puzzle(N: int, K: int):
    """
    Generates a sudoku puzzle

    Arguments:
    N -- Size of the sudoku grid
    K -- Amount of missing numbers
    Returns:
    A grid of integers of NxN, with K elements missing. The Mising values are marked by "_" character
    """

    def is_valid_move(grid, row, col, num):
        # Check row and column
        for i in range(N):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        return True

    def generate_sudoku_solution(grid):
        for row in range(N):
            for col in range(N):
                if grid[row][col] == -1:
                    nums = list(range(1, N + 1))
                    random.shuffle(nums)
                    for num in nums:
                        if is_valid_move(grid, row, col, num):
                            grid[row][col] = num
                            if generate_sudoku_solution(grid):
                                return True
                            grid[row][col] = -1
                    return False
        return True

    # Create an empty Sudoku grid with -1 indicating blank spaces
    grid = [[-1 for _ in range(N)] for _ in range(N)]

    # Generate a complete Sudoku solution
    generate_sudoku_solution(grid)

    # Randomly remove K numbers to create the puzzle
    cells = [(i, j) for i in range(N) for j in range(N)]
    random.shuffle(cells)
    for i in range(K):
        row, col = cells[i]
        grid[row][col] = '_'

    return grid


def print_sudoku(grid):
    for row in grid:
        print(" ".join(map(lambda x: str(x) if x != -1 else ' ', row)))


def print_sudoku(grid: list[list[int]]):
    for row in grid:
        print(" ".join(map(str, row)))
