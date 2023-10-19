from typing import List, NamedTuple

from typing import List

class Task:
    def __init__(self, node_id: int, execution_time: int):
        self.node_id = node_id
        self.execution_time = execution_time

class ProcessorState:
    def __init__(self, tasks: List[Task] = None, total_time: int = 0):
        if tasks is None:
            tasks = []
        self.tasks = tasks
        self.total_time = total_time

class SystemState:
    def __init__(self, processors: List[ProcessorState] = None):
        if processors is None:
            processors = []
        self.processors = processors

    def __str__(self) -> str:
        state_str = "\n"
        for i, processor in enumerate(self.processors):
            state_str += f"  Processor {i}, total time: {processor.total_time}:\n"
            if not processor.tasks:
                continue
            # Add the details of each task in the processor's task list
            for task in processor.tasks:
                state_str += f"    - Task ID: {task.node_id}, Execution Time: {task.execution_time}\n"

        
        # Optional: You can still display the system end time
        state_str += f"System end time: {self.end_time}\n"
        return state_str

    @property
    def end_time(self) -> int:
        """The end time of the SystemState, which is the maximum end time of all the ProcessorStates."""
        return max(processor.total_time for processor in self.processors) if self.processors else 0
