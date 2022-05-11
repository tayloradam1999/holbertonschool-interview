#!/usr/bin/python3
"""
island_perimeter(grid): returns perimeter of the island in grid
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island explained in grid

    Args:
      grid (list of ints): grid of 0s and 1s
        - 0: water
        - 1: land
        - Each cell is square, with a side length of 1
        - Cells are connected horizontally/vertically (not diagonally)
        - Grid is rectangular, with its width and height not exceeding 100
        - The Grid is completely surrounded by water (0s)

    Returns:
      int: perimeter of the island

    Keep in mind:
      - There is only one island (or none)
      - The island will not have 'lakes' (water inside
      that isn't connected to the water around it)
    """
    perimeter = 0
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        # if we find a land cell, add 4 to the perimeter
        if grid[i][j] == 1:
          perimeter += 4
          # then, check if the cell is connected to the north, east, south, west
          # if it is, subtract 2 from the perimeter
          if i > 0 and grid[i - 1][j] == 1:
            perimeter -= 2
          if j > 0 and grid[i][j - 1] == 1:
            perimeter -= 2
    return perimeter