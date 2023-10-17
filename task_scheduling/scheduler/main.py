from queue import PriorityQueue

import networkx as nx

def greedy_scheduler(graph: nx.DiGraph, num_processors: int):

    # Data structures to keep track of scheduling
    task_queue = PriorityQueue()
    processor_time = [0] * num_processors
    schedule = {i: [] for i in range(num_processors)}

    # Add tasks to the priority queue
    for node in graph.nodes():
        execution_time = graph.nodes[node]['execution_time']
        task_queue.put((execution_time, node))

    # While there are tasks to schedule
    while not task_queue.empty():
        # Get the task with the highest priority (shortest execution time here)
        execution_time, task = task_queue.get()
        
        # Find the processor that will be available next (greedy choice)
        next_processor_available = processor_time.index(min(processor_time))

        # Schedule the task for that processor
        schedule[next_processor_available].append(task)
        processor_time[next_processor_available] += execution_time

    return schedule, processor_time


if __name__ == "__main__":
    print("main run")