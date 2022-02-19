#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    A function that determines the winner
    Consecutive integers from 1 up to n
    """
    if not nums or x < 1:
        return None
    n = max(nums)
    player_round = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not player_round[i]:
            continue
        for j in range(i * i, n + 1, i):
            player_round[j] = False
    player_round[0] = player_round[1] = False
    a = 0
    for i in range(len(player_round)):
        if player_round[i]:
            a += 1
        player_round[i] = a
    player_1 = 0
    for n in nums:
        player_1 += player_round[n] % 2 == 1
    if player_1 * 2 == len(nums):
        return None
    if player_1 * 2 > len(nums):
        return "Maria"
    return "Ben"
