import unittest
import tempfile
import shutil
import os
import networkx as nx


from task_scheduling import read_graph, initialize_system, find_neighbors, SystemState, Task, ProcessorState, goal_check


class test_scheduler(unittest.TestCase):
    def setUp(self):
        1

    def tearDown(self):
        1

    def test_find_neighbors(self):
        """
        tests for finding neighbors in the task scheduling problem

        It uses the graph in example.dot and the find_neighbors function
        must return 6 neighbors based on the initial state representation:
        1.  0 and 1 in P1;
        2. 0 in P1 and 1 in P2;
        And that logic repeats for tasks 3 and 7, arranging in total 6 states.

        """

        # Determine the absolute path of the script running this code
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the full path to the .dot file
        # Ensure 'filename' does not contain the '.dot' extension already
        dot_file_path = os.path.join(script_dir, f"example")
        G = read_graph(dot_file_path)

        initial_state = initialize_system(G, 2)
        self.assertEqual(initial_state.end_time, 9)
        self.assertEqual(
            initial_state.processors[0].tasks[0].execution_time, 9)
        next_states = find_neighbors(G, initial_state)
        for state in next_states:
            print(state)
        self.assertEqual(len(next_states), 6)

    def test_goal_check(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        dot_file_path = os.path.join(script_dir, f"example2")
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
    # def test_Astart(self):
    #     print("attempt to solve with Astar")


if __name__ == '__main__':
    unittest.main()
