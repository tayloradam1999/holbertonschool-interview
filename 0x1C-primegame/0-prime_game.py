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
    if x <= 0:
        raise ValueError("x must be greater than 0")
    if nums is None or len(nums) == 0:
        raise ValueError("nums must not be empty")

    # Set the first player to be the first player to move
    player = 1

    # Loop through each round
    for i in range(x):
        # If the player can make a move, remove the number and its multiples
        if player in nums:
            nums.remove(player)
            for j in range(player + player, len(nums) + 1, player):
                if j in nums:
                    nums.remove(j)

        # Switch the player
        player = 1 if player == 2 else 2

    # Return the winner
    if player == 1:
        return "Maria"
    elif player == 2:
        return "Ben"
    else:
        return None
