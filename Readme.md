# AI Algorithms for Sudoku and Task Scheduling

This repository explores the application of various artificial intelligence algorithms to solve two distinct problems: Sudoku and task scheduling. Each problem is approached with multiple algorithms, each illustrating different strategies and heuristics.

## Introduction

### Sudoku Solver

Sudoku, a popular logic-based number-placement puzzle, requires a player to populate a 9x9 grid in a manner where each column, each row, and each of the nine 3x3 subgrids contain all digits from 1 to 9. Solving Sudoku puzzles can often be complex and requires logical deduction. In this project, we tackle this challenge using several AI algorithms:

- **A***: Searches the path with the lowest expected total cost.
- **Hill Climbing**: An optimization technique taking steps iteratively to find the peak solution based on the current neighboring states.
- **Iterative Depth Search**: Explores the deepest level of decision tree first, expanding breadth as needed.
- **Least Cost Search**: Explores paths with the lowest cost first.

### Task Scheduling

Task scheduling involves the allocation of tasks to resources over given time periods, often with various constraints and objectives. Efficient task scheduling is crucial in numerous fields to enhance productivity and resource management. We address this problem using the following AI strategies:

- **A***: An informed search strategy applying a heuristic to guide its path exploration.
- **Greedy Search**: A technique making the locally optimal choice, hoping to find the global optimum.
- **Local Search**: Operates using a single current state and moves to neighboring states judged by defined criteria.
- **Genetic Algorithm**: Mimics the process of natural selection to generate solutions to optimization and search problems.
- **Ant Colony Optimization**: A probabilistic technique useful in finding the optimal path, inspired by the behavior of ants searching for food.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (version 3.11 recommended)
- Dependencies: {List of dependencies or a reference to `requirements.txt`}

### Installation

1. Clone the repository to your local machine.
2. Install dependencies from `requirements.txt` with `pip install -r requirements.txt` 

### Testing

`sudoku` and `task_scheduling` folders have each a Makefile. Enter one of these folders
and check the Makefile for test script. Usually it's `make test`.
