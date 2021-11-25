#!/usr/bin/env python3
"""
In a text file, there is a single character <H>.
Your text editor can execute only two operations in this file:
<Copy All> and <Paste>.
Given a number <n>, write a method that calculates the fewest number
of operations needed to result in exactly <n> <H> characters in the file.
"""


def find_largest_prime_factor(n):
    """
    Finds largest prime factor of <n>
    """
    # Initialize the largest prime factor to 1
    largest_prime_factor = 1

    # For each prime number in the range of 2 to <n>
    for prime_number in range(2, n + 1):
        # If the prime number is a factor of <n>
        if n % prime_number == 0:
            # Set the largest prime factor to the prime number
            largest_prime_factor = prime_number

    # Return the largest prime factor
    return largest_prime_factor


def minOperations(n):
    """
    Return the minimum number of operations needed to result in exactly
    n <H> characters in the file.

    Use Prime Factorization to find the number of operations needed.
    """
    # Initialize the number of operations to 0
    operations = 0

    # While the number of <H> characters is not equal to n
    while n != 0:
        # If the number of <H> characters is greater than n
        if n > 0:
            # Find the largest prime factor of n
            prime_factor = find_largest_prime_factor(n)

            # Increment the number of operations by the prime factor
            operations += prime_factor

            # Subtract the prime factor from n
            n -= prime_factor

        # If the number of <H> characters is less than n
        else:
            # Find the largest prime factor of n
            prime_factor = find_largest_prime_factor(n)

            # Decrement the number of operations by the prime factor
            operations -= prime_factor

            # Add the prime factor to n
            n += prime_factor

    # Return the number of operations
    return operations
