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
    # Find prime factors of n
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    if n > 2:
        prime_factors.append(n)
    # Count number of operations
    operations = 0
    for i in range(len(prime_factors)):
        operations += prime_factors[i] - 1
    return operations
