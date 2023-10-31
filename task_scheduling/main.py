from system_types import Task, ProcessorState, SystemState

task1 = Task(node_id=1, execution_time=2, communication_time=1)
task2 = Task(node_id=2, execution_time=4, communication_time=2)
processor1 = ProcessorState([task1, task2])

task3 = Task(node_id=3, execution_time=3)
processor2 = ProcessorState([task3])

system = SystemState([processor1, processor2])
system.plot_gantt_chart()