from generator import create_sudoku_puzzle, print_sudoku
import math


if __name__ == "__main__":
    N = int(input("Enter the size (N) of the Sudoku grid: "))
    K = int(input("Enter the number of initial values (K): "))
    
    if N <= 0 or K < 0 or K > N * N:
        print("Invalid input.")
    else:
        sudoku_puzzle = create_sudoku_puzzle(N, K)
        print("\nGenerated Sudoku Puzzle:")
        print_sudoku(sudoku_puzzle)