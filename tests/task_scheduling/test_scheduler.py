import unittest
import tempfile
import shutil
import os
import networkx as nx


from task_scheduling import read_graph, initialize_system


class test_scheduler(unittest.TestCase):
    def setUp(self):
        1

    def tearDown(self):
        1

    
    def test_find_neighbors(self):
        """
        tests for finding neighbors in the task scheduling problem

        the state representation is given in the types
        """

        # Determine the absolute path of the script running this code
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the full path to the .dot file
        # Ensure 'filename' does not contain the '.dot' extension already        
        dot_file_path = os.path.join(script_dir, f"example")
        G = read_graph(dot_file_path)
        
       
        initial_state = initialize_system(G,2)
        self.assertEqual(initial_state.end_time, 9)
        self.assertEqual(initial_state.processors[0].tasks[0].execution_time, 9)
        print(initial_state)


        





    # def test_Astart(self):
    #     print("attempt to solve with Astar")
        


if __name__ == '__main__':
    unittest.main()


