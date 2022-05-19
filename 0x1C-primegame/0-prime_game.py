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
    count_m = 0
    count_b = 0
    for i in range(x):
        nums = [i for i in nums if i % 2 != 0]
        nums = [i for i in nums if i % 3 != 0]
        nums = [i for i in nums if i % 5 != 0]
        nums = [i for i in nums if i % 7 != 0]
        if len(nums) == 0:
            return None
        if nums[0] % 2 == 0:
            count_m += 1
        else:
            count_b += 1
    if count_m > count_b:
        return "Maria"
    elif count_b > count_m:
        return "Ben"
    else:
        return None
