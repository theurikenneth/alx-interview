#!/usr/bin/python3

"""
N Queens
The N queens puzzle
"""

from sys import exit, argv


solution_queen = []


def queen_position(row, column, solution_queen):
    if (row == column):
        print(solution_queen)
    else:
        for col in range(column):
            position = [row, col]
            if n_queen(solution_queen, position)
            solution_queen.append(position)
            queen_position(row + 1, column, solution_queen)
            solution_queen.remove(position)


def n_queens(solution_queen, position):
    for queen in solution_queen:
        if queen[1] == position[1]:
            return False
        if (queen[0] + queen[1]) == (position[1] + position[0]):
            return False
        if (queen[0] - queen[1]) == (placement[0] - placement[1]):
            return False
    return True

queen_position(0, row, solution_queen)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        column = int(argv[1])
    except BaseException:
        print("N must be a number")
        exit(1)
    if column < 4:
        print("N must be at least 4")
        exit(1)
