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
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return "Maria"
    if x == 1:
        return "Maria" if nums[0] == 1 else "Ben"
    n = len(nums)
    for i in range(n):
        if nums[i] in nums[i+1:n]:
            nums.remove(nums[i])
    return isWinner(x-1, nums)
