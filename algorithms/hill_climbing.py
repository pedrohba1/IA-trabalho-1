# Author: Gustavo Melo  

import random

def is_valid_move(grid, row, col, num):
    # Verifica se é um movimento válido na grade Sudoku
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    # Verifica a sub-grade 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def evaluate_solution(grid):
    # Avalia a qualidade da solução atual contando os números corretamente posicionados
    correct_count = 0
    for row in range(9):
        for col in range(9):
            if is_valid_move(grid, row, col, grid[row][col]):
                correct_count += 1
    return correct_count

def hill_climbing_sudoku(grid):
    max_iterations = 1000
    best_solution = [row[:] for row in grid]  # Cria uma cópia profunda da solução inicial
    best_score = evaluate_solution(grid)

    for _ in range(max_iterations):
        # Faz um movimento aleatório na solução atual
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)

        if is_valid_move(grid, row, col, num):
            grid[row][col] = num

            # Avalia a nova solução
            new_score = evaluate_solution(grid)

            # Verifica se a nova solução é melhor que a anterior
            if new_score > best_score:
                best_solution = [row[:] for row in grid]
                best_score = new_score

    return best_solution

# Função para imprimir o Sudoku
def print_sudoku(grid):
    for row in grid:
        print(" ".join(map(str, row)))

# Cria um Sudoku puzzle (substitua esta parte com sua própria função create_sudoku_puzzle)
N = 9
sudoku_puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Sudoku usando subida de encosta
solved_sudoku = hill_climbing_sudoku(sudoku_puzzle)

# Imprime a solução
print_sudoku(solved_sudoku)
