import unittest
import tempfile
import shutil
import os
import networkx as nx


from task_scheduling import read_graph, initialize_system, find_neighbors, SystemState, Task, ProcessorState, goal_check, cost_between, heuristic
from algorithms import least_cost_path, Astar


class test_gantt(unittest.TestCase):
    """
    We made some Gantt chart generation, and the intention of this 
    test is to check if it generates them correctly. 
    """
    def setUp(self):
        # Determine the absolute path of the script running this code
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the full path to the .dot file
        # Ensure 'filename' does not contain the '.dot' extension already
        dot_file_path = os.path.join(script_dir, f"simple_example")
        self.G = read_graph(dot_file_path)
        self.initial_state = initialize_system(self.G, 2)

    def tearDown(self):
        1


    def test_gantt(self):
        """
        Tests for checking if the current SystemState is the goal.
        Whewn all the tasks are scheduled, we have a goal state. 
        """
        script_dir = os.path.dirname(os.path.abspath(__file__))
        dot_file_path = os.path.join(script_dir, f"simple_example")
        G = read_graph(dot_file_path)

        # Defining the tasks
        task_0 = Task(node_id=0, execution_time=1)
        task_1 = Task(node_id=1, execution_time=2)
        task_2 = Task(node_id=2, execution_time=4)
        task_3 = Task(node_id=3, execution_time=2)

        # Assigning tasks to processors
        processor_A = ProcessorState(tasks=[task_0, task_1], total_time=1 + 2)
        processor_B = ProcessorState(tasks=[task_2, task_3], total_time=4 + 2)

        # Creating the SystemState
        solution_state = SystemState(processors=[processor_A, processor_B])
        self.assertTrue(goal_check(G, solution_state))
    


if __name__ == '__main__':
    unittest.main()
