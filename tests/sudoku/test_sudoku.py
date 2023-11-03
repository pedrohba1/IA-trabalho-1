import unittest
import tempfile
import shutil
import os
import networkx as nx

from sudoku import create_sudoku_puzzle, print_sudoku, goal_check, find_neighbors, heuristic, cost_between, calculate_solution_cost
from algorithms import Astar, least_cost_path, iter_depth_search, hill_climbing, output_gen


class test_sudoku(unittest.TestCase):
    """
    This suite tests the generated Sudoku puzzle's validity and the capability of different algorithms (A*, Hill Climbing, 
    Least Cost, and Deep Iterative Search) to solve it. Each algorithm is tested for correctness in the context of Sudoku solving.
    """

    def setUp(self):
         self.sudoku_matrix = [
            [-1, -1, -1,  2],
            [-1,  2, -1, -1],
            [2,  4,  1,  3],
            [3, -1,  2, -1]
        ]

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
        self.assertTrue(goal_check(solved_sudoku))

        unsolved_sudoku = self.sudoku_matrix
        G2 = nx.DiGraph()
        G2.add_node(1, state=unsolved_sudoku)
        self.assertFalse(goal_check(unsolved_sudoku))

    def test_find_neighbors(self):
        """
        Test case to check if neighbor generation generates valid nodes and weights
        """
        G = nx.DiGraph()
        G.add_node(1, state=self.sudoku_matrix)
        neighbors = find_neighbors(self.sudoku_matrix)
        self.assertEqual(len(neighbors), 2)

    def test_Astar(self):
        """
        Test case to check the A* algorithm's performance on the Sudoku puzzle.
        """
        sudoku = create_sudoku_puzzle(4, 8)
        solution_path, _ = Astar(
            initial_state=sudoku,
            cost_between=cost_between,
            find_neighbors=find_neighbors,
            goal_check=goal_check,
            heuristic=heuristic
        )
        print("\n initial state: \n ")
        print_sudoku(solution_path[0])

        print("\n final state \n")
        print_sudoku(solution_path[-1])

    def test_least_cost(self):
        """
        Test case to check the Least Cost Path algorithm's performance on the Sudoku puzzle.
        """
        sudoku = create_sudoku_puzzle(4, 8)
        solution,_ = least_cost_path(
            search_space=nx.DiGraph(),
            initial_state=sudoku,
            cost_between=cost_between,
            find_neighbors=find_neighbors,
            goal_check=goal_check,
        )
        print("\n initial state: \n ")
        print_sudoku(solution[0])

        print("\n final state \n")
        print_sudoku(solution[-1])

    def test_hill_climbing(self):
        """
        Test case to evaluate the Hill Climbing algorithm on the Sudoku puzzle.

        The puzzle is solved using Hill Climbing, and the solution's correctness is verified.
        """
        solution_path, _ = hill_climbing(searchSpace=nx.DiGraph(), 
                                 initial_state=self.sudoku_matrix, 
                                 goal_check=goal_check, 
                                 find_neighbors=find_neighbors, 
                                 heuristic=heuristic)
        print("hill climbing solutions: \n")
        for sol in solution_path:
            print_sudoku(sol)

        self.assertTrue(goal_check(solution_path[-1]))

    def test_deep_iterative_search(self):
     """
      Tests the Deep iterative search algorithm 
     """
     sudoku = self.sudoku_matrix
     solution, sG = iter_depth_search(
            initial_state=sudoku,
            goal_check=goal_check,
            find_neighbors=find_neighbors,
            max_depth=20
        )
     print("\n initial state: \n ")
     print_sudoku(solution[0])
     for i in solution:
         print('\n')
         print_sudoku(i)
         print('\n')
     print("\n final state \n")
     print_sudoku(solution[-1])
     output_gen.generate_output((solution,sG),filename="test_output_sudoku" ,calculate_solution_cost=calculate_solution_cost)
     self.assertTrue(goal_check(solution[-1]))


if __name__ == '__main__':
    unittest.main()
