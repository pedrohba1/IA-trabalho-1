import unittest
import tempfile
import shutil
import os
import networkx as nx

from sudoku import create_sudoku_puzzle, print_sudoku, goal_check, find_neighbors, heuristic, cost_between
from algorithms import Astar

class test_sudoku(unittest.TestCase):
    """
    This suite tests the generated Sudoku puzzle's validity and the capability of different algorithms (A*, Hill Climbing, 
    and Deep Iterative Search) to solve it. Each algorithm is tested for correctness in the context of Sudoku solving.
    """

    def test_valid_function(self):
        """
        Test case to verify that the generated Sudoku puzzle is valid.

        This test checks if a freshly created puzzle with no missing elements is considered 'solved'. This serves as a validation 
        of both the puzzle generator and the solved state checker. A valid puzzle should be recognized as solved.

        Also, an invalid puzzle should return False, which means it is not solved.
        
        """
        self.assertTrue(goal_check(create_sudoku_puzzle(4, 0)))
        self.assertFalse(goal_check(create_sudoku_puzzle(4, 2)))

    # def test_Astar(self):
        # """
        # Test case to check the A* algorithm's performance on the Sudoku puzzle.

        # The test involves solving the puzzle using the A* algorithm and verifying that the solution is correct.
        # """
        # sudoku = create_sudoku_puzzle(4, 8)
        # solution = Astar(
            # sudoku,
            # goal_check=goal_check, 
            # find_neighbors=find_neighbors, 
            # heuristic=heuristic,
            # cost_between=cost_between
        # )  # This is a hypothetical function call; replace with your actual A* function
        # self.assertTrue(goal_check(
            # solution), "A* algorithm should successfully solve the Sudoku puzzle.")

    # def test_hill_climbing(self):
    #     """
    #     Test case to evaluate the Hill Climbing algorithm on the Sudoku puzzle.

    #     The puzzle is solved using Hill Climbing, and the solution's correctness is verified.
    #     """
    #     solution = hill_climbing(self.sudoku)  # Replace with your actual Hill Climbing function
    #     self.assertTrue(goal_check(solution), "Hill Climbing algorithm should successfully solve the Sudoku puzzle.")

    # def test_deep_iterative_search(self):
    #     """
    #     Test case to assess the Deep Iterative Search algorithm's effectiveness.

    #     This method involves applying Deep Iterative Search to the puzzle and verifying the solution's accuracy.
    #     """
    #     solution = deep_iterative_search(self.sudoku)  # Replace with your actual Deep Iterative Search function
    #     self.assertTrue(goal_check(solution), "Deep Iterative Search should successfully solve the Sudoku puzzle.")


if __name__ == '__main__':
    unittest.main()
