#!/usr/bin/python3
"""
Project 0x1C - Prime game

Maria and Ben are playing a game.
Given a set of consecutive integers starting from 1 up to and including n,
they take turns choosing a prime number from the set and removing that number
and its multiples from the set.
The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.
"""


def isWinner(x, nums):
    """
        Returns the winner of the game.

        Args:
            x: number of rounds
            nums: list of consecutive integers (n)
            (n and x will not be larger than 10000)

        Returns:
            Name of player that won most rounds.
            If winner is not determined, returns None.
    """
    if x < 1 or x > 10000:
        return None
    if len(nums) < 1 or len(nums) > 10000:
        return None
    if len(nums) < x:
        return None
    for i in range(x):
        if len(nums) == 1:
            return "Ben"
        try:
            nums.remove(nums[0])
        except ValueError:
            return "Maria"
        for j in range(2, nums[0]):
            try:
                nums.remove(j)
            except ValueError:
                continue
        try:
            nums.remove(nums[0])
        except ValueError:
            return "Maria"
    return "Maria"
