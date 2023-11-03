import unittest
import tempfile
import shutil
import os
import networkx as nx


from task_scheduling import read_graph, initialize_system, find_neighbors, SystemState, Task, ProcessorState, goal_check, cost_between, heuristic
from algorithms import least_cost_path, Astar, greedy_search, iter_depth


class test_scheduler(unittest.TestCase):
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

    def test_find_neighbors(self):
        """
        tests for finding neighbors in the task scheduling problem

        It uses the graph in example.dot and the find_neighbors function
        must return 6 neighbors based on the initial state representation:
        1.  0 and 1 in P1;
        2. 0 in P1 and 1 in P2;
        And that logic repeats for tasks 3 and 7, arranging in total 6 states.

        """

        self.assertEqual(self.initial_state.end_time, 1)
        next_states = find_neighbors(self.initial_state, self.G)
        self.assertEqual(len(next_states), 4)

    def test_cost_between(self):
        """
        Tests the cost between states. 
        the initial state is tested against the next states and the costs are calculated
        """
        next_states = find_neighbors(self.initial_state, self.G)
        print("\ninitial state: \n")
        for state in next_states:
            print("cost between: ", cost_between(
                self.initial_state, state, self.G))

    def test_goal_check(self):
        """
        Tests for checking if the current SystemState is the goal.
        Whewn all the tasks are scheduled, we have a goal state. 
        """
        tasks_p1 = [
            Task(node_id=0, execution_time=1, communication_time=0),
            Task(node_id=1, execution_time=2,
                 communication_time=0, dependencies=[0]),
            Task(node_id=2, execution_time=4,
                 communication_time=0, dependencies=[0]),
        ]
        tasks_p2 = [
            Task(node_id=3, execution_time=2,
                 communication_time=1, dependencies=[1]),
        ]

        processor1 = ProcessorState(tasks_p1)
        processor2 = ProcessorState(tasks_p2)

        system = SystemState([processor1, processor2])
        self.assertTrue(goal_check(system, self.G))

    def test_heuristic(self):
        """
        Tests the heuristic against the simpler scheduling graph
        """
        initial_state = initialize_system(self.G, 2)

        val = heuristic(initial_state, self.G)
        self.assertEqual(val, 4)

    def test_iter_depth(self):
        """
        tests the application of the least cost algorithm
        """
        solution, _ = iter_depth.iter_depth_search(
            search_space=self.G,
            initial_state=self.initial_state,
            goal_check=goal_check,
            max_depth=40,
            find_neighbors=find_neighbors)
        print("\n initial state: \n ")
        print(solution[0])

        print("\n final state \n")
        print(solution[-1])
        self.assertTrue(goal_check(solution[-1], self.G))

    def test_least_cost(self):
        """
        tests the application of the least cost algorithm
        """
        solution = least_cost_path(
            search_space=self.G,
            initial_state=self.initial_state,
            goal_check=goal_check,
            find_neighbors=find_neighbors,
            cost_between=cost_between)
        print("\n initial state: \n ")
        print(solution[0])

        print("\n final state \n")
        print(solution[-1])

    def test_Astar(self):
        """tests the application of the Astar algorithm"""
        initial_state = initialize_system(self.G, 2)

        solution = Astar(
            search_space=self.G,
            initial_state=initial_state,
            goal_check=goal_check,
            find_neighbors=find_neighbors,
            cost_between=cost_between,
            heuristic=heuristic)
        print("\n initial state: \n ")
        print(solution[0])

        print("\n final state \n")
        print(solution[-1])

    def test_greedy(self):
        """tests the application of the greedy search algorithm"""
        initial_state = initialize_system(self.G, 2)

        solution = greedy_search(
            searchSpace=self.G,
            initial_state=initial_state,
            goal_check=goal_check,
            find_neighbors=find_neighbors,
            heuristic=heuristic)
        print("\n initial state: \n ")
        print(solution[0])

        print("\n final state \n")
        print(solution[-1])


if __name__ == '__main__':
    unittest.main()
