import unittest
import tempfile
import shutil
import os
import networkx as nx

from graph_gen import generate_tree
from scheduler import greedy_scheduler


class test_scheduler(unittest.TestCase):
    def setUp(self):
        1

    def tearDown(self):
        1

    
    def test_greedy_search(self):
        # Generate a new tree
        tree = generate_tree(5)
        schedule, time = greedy_scheduler(tree, 2)
        print("\n schedule: " )
        print(schedule)
        print("\n time: ", time)
        


if __name__ == '__main__':
    unittest.main()


