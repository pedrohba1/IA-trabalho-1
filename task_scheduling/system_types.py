from typing import List
import plotly.figure_factory as ff


class Task:
    def __init__(self, node_id: int, execution_time: int, communication_time: int = 0, dependencies: List[int] = None):
        self.node_id = node_id
        self.execution_time = execution_time
        self.communication_time = communication_time
        if dependencies is None:
            self.dependencies = []
        else:
            self.dependencies = dependencies
    
    def __str__(self) -> str:
        state_str = "\n"
        state_str += f"   - node id: {self.node_id}\n"
        state_str += f"    - Execution time: {self.execution_time}\n"
        state_str += f"    - Communication time: {self.communication_time}\n"
        state_str += f"   - Dependencies: {self.dependencies}\n"
        return state_str

class ProcessorState:
    def __init__(self, tasks: List[Task] = None):
        if tasks is None:
            tasks = []
        self.tasks = tasks
        self.total_time = sum(task.execution_time + task.communication_time for task in tasks)

    @property
    def total_execution_time(self) -> int:
        """The total execution time required for all tasks in this ProcessorState."""
        return sum(task.execution_time for task in self.tasks)


    @property
    def total_communication_time(self) -> int:
        """The total communication time required for all tasks in this ProcessorState."""
        return sum(task.communication_time for task in self.tasks)


class SystemState:
    def __init__(self, processors: List[ProcessorState] = None):
        if processors is None:
            processors = []
        self.processors = processors

    def __str__(self) -> str:
        state_str = "\n"
        for i, processor in enumerate(self.processors):
            state_str += f"  Processor {i}, total time: {processor.total_time} (with communication time: {processor.total_communication_time}):\n"
            if not processor.tasks:
                state_str += f"    - Processor is free of tasks -\n"
                continue
            # Add the details of each task in the processor's task list
            for task in processor.tasks:
                state_str += f"    - Task ID: {task.node_id}, Execution Time: {task.execution_time}, Communication Time: {task.communication_time}\n"

        # Optional: You can still display the system end time
        state_str += f"System end time: {self.end_time}\n"
        return state_str

    @property
    def end_time(self) -> int:
        """The end time of the SystemState, which is the maximum end time of all the ProcessorStates."""
        return max(processor.total_time + processor.total_communication_time for processor in self.processors) if self.processors else 0

    def plot_gantt_chart(self):
        """Generate and display a Gantt chart for the current system state."""


        # creates a dict of all tasks, to make it easier to serach for dependencies
        tasks_dict = {}
        task_to_processor = {}
        for p_id, processor in enumerate(self.processors):
            for task in processor.tasks:
                task_to_processor[task.node_id] = p_id
                tasks_dict[task.node_id] = task

        

        df = []
        colors = {
            'Execution': 'rgb(0, 255, 100)',
            'Communication': 'rgb(220, 0, 0)'
        }

        task_finish_time = {}
        for _, processor in enumerate(self.processors):
            start_time = 0
            for task in processor.tasks:

                if task.dependencies:
                    for dep in task.dependencies:
                        # checks if dependencies are from the same processor
                        
                        # checks if dependencies are not from the same processor
                        if (task_to_processor[dep] != task_to_processor[task.node_id]):
                            # Create a Gantt chart entry for the task's communication time (if any)

                            # start time is incremented by  end of dependency time
                            start_time +=  task_finish_time[dep]
                            if task.communication_time:
                                df.append(dict(Task=f"task-{task.node_id}",
                                            Start=start_time,
                                            Finish=start_time + task.communication_time,
                                            Resource='Communication'))
                            start_time += task.communication_time

              

                # Create a Gantt chart entry for the task's execution time
                df.append(dict(Task=f"task-{task.node_id}",
                               Start=(start_time),
                               Finish=start_time + task.execution_time,
                               Resource='Execution'))
                task_finish_time[task.node_id] = start_time + task.execution_time 
                start_time += task.execution_time

            

        fig = ff.create_gantt(
            df, colors=colors, index_col='Resource', show_colorbar=True, group_tasks=True)
        fig.update_layout(xaxis_type='linear', autosize=False, width=800, height=400)
        fig.show()
