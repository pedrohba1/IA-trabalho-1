from typing import Any
import networkx as nx

def goal_check(sudoku: list[list[int]], G: Any = None) -> bool:
    """
    Checks if a given Sudoku grid is solved. (if the sudoku in question does not have subgrids)

    Args:
        grid (list[list[int]]): A 2D list of integers representing the Sudoku puzzle

    Returns:
        bool: True if the puzzle is solved, false otherwise
    """


    N = len(sudoku)

    # Function to check if a segment (row or column) is valid
    def is_segment_valid(segment):
        # Filter out the unsolved cells, if any
        filtered_segment = [num for num in segment if num != -1]

        # Instead of using set for uniqueness, we'll use a dictionary to count occurrences.
        number_counts = {}
        for number in filtered_segment:
            if number in number_counts:
                # If the number is already in the dictionary, the segment is not valid
                return False
            # If it's the first occurrence, set its count to 1
            number_counts[number] = 1

        # Check if the segment has the correct length
        return len(filtered_segment) == N

    # Check each row
    for row in sudoku:
        if not is_segment_valid(row):
            return False

    # Check each column
    for col in range(N):
        column = [sudoku[row][col] for row in range(N)]
        if not is_segment_valid(column):
            return False

    return True
