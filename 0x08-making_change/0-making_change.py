#!/usr/bin/python3
"""
Deterrmine fewest coin to meet the value total
"""


def makeChange(coins, total):
    """
    Given a file of coins
    Fewest no. of coins to get to total
    """
    if total < 1:
        return 0
    make_change = 0
    coins.sort(reverse=True)
    for i in coins:
        temp = int(total / i)
        total -= (temp * i)
        make_change += temp
        if total == 0:
            return make_change
    if total != 0:
        return -1
