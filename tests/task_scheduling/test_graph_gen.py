import unittest
import tempfile
import shutil
import os
import networkx as nx

from task_scheduling import generate_tree, save_graph, read_graph

class test_graph_gen(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_generate_tree(self):
        num_nodes = 5
        tree = generate_tree(num_nodes)
        self.assertEqual(len(tree.nodes), num_nodes)

    def test_save_and_read_graph(self):
        # Generate a new tree
        tree = generate_tree(5)

        # Save it to a file
        filepath = os.path.join(self.test_dir, 'test_graph')  # temp file path
        save_graph(tree,filepath)

        # Now, try to read it back
        same_tree = read_graph(filepath)

        # Assert the loaded graph has the same structure as the original one
        self.assertTrue(nx.is_isomorphic(tree, same_tree, node_match=lambda x, y: x == y))

    # ... any other tests ...

if __name__ == '__main__':
    unittest.main()


