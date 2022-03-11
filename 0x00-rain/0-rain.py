#!/usr/bin/python3
"""
Given a list of non-negative integers representing the heights
of walls with unit width 1, as if viewing the cross-section of a relief map,
calculate how many square units of water will be retained after it rains.
"""


def rain(walls):
    """
    Returns sum of rainwater collected

    Assume that the ends of the list (before index 0 and after index walls[-1])
    are not walls, meaning they will not retain water.

    Args:
            walls: list of non-negative integers representing the heights of walls
                    with unit width 1, as if viewing the cross-section of a relief map

    Returns:
            sum of rainwater collected
            0 if list is empty
    """

    if not walls:
        return 0
    # Init variables
    # Max will find highest value in list with given index
    # Min will do the same, but for lowest value
    water = 0
    for i, j in enumerate(walls):
        # find tallest wall to the left
        max_left = max(walls[:i + 1])
        # find tallest wall to the right
        max_right = max(walls[i:])
        # find which is lower between the two
        min_wall = min(max_left, max_right)
        # calculate water retained
        water += min_wall - j
    return water
