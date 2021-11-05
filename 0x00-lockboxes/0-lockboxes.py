#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    - boxes is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
      - There can be keys that do not have boxes
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be opened, else return False
    """
    # Create a list of keys with default box being 0
    keys = [0]
    # Iterate through lists in boxes and put keys in keys list
    for i, box in enumerate(boxes):
        if i in keys:
            # Appending all keys inside of boxes that can be opened
            [keys.append(key) for key in box if key not in keys]
        # Condition met when current box cannot be opened with current keys   
        else:
            # Perform same loop on remaining boxes
            for j in range(i, len(boxes)):
                if j in keys:
                    # Same sort of appending as before
                    [keys.append(key) for key in boxes[j] if key not in keys]
            # Attempt to open box that met above else condition
            if i in keys:
                # Same appendage
                [keys.append(key) for key in box if key not in keys]
            else:
                # GG
                return False
    return True
