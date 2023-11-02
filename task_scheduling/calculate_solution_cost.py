from typing import List
from .system_types import SystemState

def calculate_solution_cost(path: List[SystemState]):
    """returns the end time of the system, which is the final cost of the solution"""
    return path[-1].end_time
    
