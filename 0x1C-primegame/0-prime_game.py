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
    if x == 0:
        return None

    if x == 1:
        if nums[0] == 1:
            return "Maria"
        else:
            return "Ben"

    # Initialize the winner
    winner = "Maria"

    # Check if the winner is Ben
    for i in range(len(nums)):
        if nums[i] == 1:
            winner = "Ben"
            break

    # If winner is not determined, continue checking
    if winner == "Maria":
        for i in range(len(nums)):
            # Check if the winner is Maria
            if nums[i] == 1:
                winner = "Maria"
                break

            # Check if the winner is Ben
            for j in range(len(nums)):
                if nums[j] == 1:
                    winner = "Ben"
                    break

    return winner