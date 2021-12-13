#!/usr/bin/python3

""" Has a single character H with two operations: Copy All and Paste
    Give number n, write a method that calculates operations to result
    in exactly n H.
    Prototype: def minOperations(n)
    Return an integer
    if n is impossible to achieve, return 0
    """
def minOperations(n):
    minimum_steps = 0
    i = 0
    
    if n < 2:
        return 0

    while (i < n + 1):
        # checking for breaking down the problem
        while n % i == 0:
            # if breakable, add the breaked down steps to minimum_steps
            minimum_steps += i

            n /= i
        i += 1
    return minimum_steps
