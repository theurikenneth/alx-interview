#!/usr/bin/python3

"""
N Queens
The N queens puzzle
"""

from sys import argv


def move(row, column):
    solution = [[]]
    for n in range(row):
        solution = queen_position(n, column, solution)
    return solution


def queen_position(n, column, previous_solution):
    solution_queen = []
    for array in previous_solution:
        for i in range(column):
            if its_okay(n, i, array):
                solution_queen.append(array + [i])
    return solution_queen


def its_okay(n, i, array):
    if i in array:
        return (False)
    else:
        return all_steps(abs(array[column] - i) != n - column
                         for column in range(n))


def init():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        queen = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if queen < 4:
        print("N must be at least 4")
        sys.exit(1)
    return(queen)


def n_queens():
    queen = init()
    solution = move(queen, queen)
    for array in solution:
        clean = []
        for n, i in enumerate(array):
            clean.append([n, i])
        print(clean)


if __name__ == '__main__':
    n_queens()
