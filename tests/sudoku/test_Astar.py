import unittest
import tempfile
import shutil
import os
import networkx as nx

from sudoku.generator import create_sudoku_puzzle, print_sudoku
from algorithms import Astar

class test_Astar(unittest.TestCase):
    sudoku = [[]]

    def setUp(self):
        self.sudoku = create_sudoku_puzzle(4,8)        



    def test_Astar(self):
        print_sudoku(self.sudoku)
        print("attempt to solve with Astar")
        


if __name__ == '__main__':
    unittest.main()


