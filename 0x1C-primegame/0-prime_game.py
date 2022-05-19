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
    # Initialize variables
    maria = 0
    ben = 0
    # Loop through rounds
    for i in range(x):
        # Remove multiples of each number
        for j in nums:
            nums = list(filter(lambda a: a % j != 0, nums))
        # If Ben can't make a move, he loses
        if nums == []:
            return "Ben"
        # If Maria can't make a move, she loses
        if nums[0] == 1:
            return "Maria"
        # Remove first number
        nums = nums[1:]
    # If no one can make a move, return None
    return None
