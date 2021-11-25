#!/usr/bin/python3
"""
In a text file, there is a single character <H>.
Your text editor can execute only two operations in this file:
<Copy All> and <Paste>.
Given a number <n>, write a method that calculates the fewest number
of operations needed to result in exactly <n> <H> characters in the file.

Use Prime Factorization to find the number of operations.
"""


def minOperations(n):
    """
    Finds min amount of operations using Prime Factorization
    """
    op_count = 0  # Initialize operation count
    factor = 2  # start at 2 because 1 is not prime

    while n > 1:  # while n is not 1
        if n % factor == 0:  # if n is divisible by factor
            n = n // factor  # divide n by factor
            op_count += factor  # add factor to op_count
        else:  # if n is not divisible by factor
            factor += 1  # increment factor
    return op_count  # return op_count
