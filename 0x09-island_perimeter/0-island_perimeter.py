#!/usr/bin/python3
"""
Island perimeter
"""


def island_perimeter(grid):
    """
    create a function that returns the perimeter
    of the island described in grid
    """
    land_perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[a][a])):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    land_perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    land_perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    land_perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    land_perimeter += 1
    return (land_perimeter)
