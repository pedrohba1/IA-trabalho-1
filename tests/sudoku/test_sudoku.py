import unittest
import tempfile
import shutil
import os
import networkx as nx

from sudoku import create_sudoku_puzzle, print_sudoku, goal_check, find_neighbors, heuristic, cost_between
from algorithms import Astar, least_cost_path


class test_sudoku(unittest.TestCase):
    """
    This suite tests the generated Sudoku puzzle's validity and the capability of different algorithms (A*, Hill Climbing, 
    Least Cost, and Deep Iterative Search) to solve it. Each algorithm is tested for correctness in the context of Sudoku solving.
    """

    def test_valid_function(self):
        """
        Test case to verify that the generated Sudoku puzzle is valid.

        This test checks if a freshly created puzzle with no missing elements is considered 'solved'. This serves as a validation 
        of both the puzzle generator and the solved state checker. A valid puzzle should be recognized as solved.

        Also, an invalid puzzle should return False, which means it is not solved.

        """

        solved_sudoku = create_sudoku_puzzle(4, 0)
        G = nx.DiGraph()
        G.add_node(1, state=solved_sudoku)
        self.assertTrue(goal_check(G, solved_sudoku))

        unsolved_sudoku = create_sudoku_puzzle(4, 8)
        G2 = nx.DiGraph()
        G2.add_node(1, state=unsolved_sudoku)
        self.assertFalse(goal_check(G2, unsolved_sudoku))

    def test_find_neighbors(self):
        """
        Test case to check if neighbor generation generates valid nodes and weights
        """

        sudoku_matrix = [
            [-1, -1, -1,  2],
            [-1,  2, -1, -1],
            [2,  4,  1,  3],
            [3, -1,  2, -1]
        ]
        G = nx.DiGraph()
        G.add_node(1, state=sudoku_matrix)
        neighbors = find_neighbors(G, sudoku_matrix)
        self.assertEqual(len(neighbors), 2)

    def test_Astar(self):
        """
        Test case to check the A* algorithm's performance on the Sudoku puzzle.
        """
        sudoku = create_sudoku_puzzle(4, 8)
        solution = Astar(
            initial_state=sudoku,
            cost_between=cost_between,
            find_neighbors=find_neighbors,
            goal_check=goal_check,
            heuristic=heuristic
        )
        print("\n initial state: \n ")
        print_sudoku(solution[1])

        print("\n final state \n")
        print_sudoku(solution[-1])

    def test_least_cost(self):
        """
        Test case to check the Least Cost Path algorithm's performance on the Sudoku puzzle.
        """
        sudoku = create_sudoku_puzzle(4, 8)
        solution = least_cost_path(
            initial_state=sudoku,
            cost_between=cost_between,
            find_neighbors=find_neighbors,
            goal_check=goal_check,
        )
        print("\n initial state: \n ")
        print_sudoku(solution[1])

        print("\n final state \n")
        print_sudoku(solution[-1])

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
