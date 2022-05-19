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
    
    def isPrime(num):
        """
            Returns True if num is a prime number.

            Args:
                num: integer to check

            Returns:
                True if num is a prime number, False otherwise
        """
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def removeMultiples(num, nums):
        """
            Removes all multiples of num from nums.

            Args:
                num: integer to remove multiples of
                nums: list of consecutive integers

            Returns:
                list of consecutive integers without num and its multiples
        """
        while num in nums:
            nums.remove(num)
        for i in range(num + num, len(nums), num):
            nums.remove(i)
        return nums

    def getWinner(nums):
        """
            Returns the winner of the game.

            Args:
                nums: list of consecutive integers

            Returns:
                Name of player that won most rounds.
                If winner is not determined, returns None.
        """
        if len(nums) == 0:
            return "Maria"
        for num in nums:
            if isPrime(num):
                nums = removeMultiples(num, nums)
                return getWinner(nums)
        return "Ben"

    winners = {"Maria": 0, "Ben": 0}
    for i in range(x):
        nums = list(range(1, len(nums) + 1))
        winner = getWinner(nums)
        winners[winner] += 1
    if winners["Maria"] > winners["Ben"]:
        return "Maria"
    elif winners["Maria"] < winners["Ben"]:
        return "Ben"
    else:
        return None
