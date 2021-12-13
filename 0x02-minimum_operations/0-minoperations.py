#!/usr/bin/python3

""" Has a single character H with two operations: Copy All and Paste
    Give number n, write a method that calculates operations to result
    in exactly n H.
    Prototype: def minOperations(n)
    Return an integer
    if n is impossible to achieve, return 0
    """


def minOperations(n):
    minimum_steps = []
    index = 1

    if n < 2:
        return 0

    while n != 1:
        index += 1
        if n % index == 0:
            while n % index == 0:
                n /= index
                factor_list.appned(index)
    return sum(minimum_steps)
