"""
You are given a two-digit integer n. Return the sum of its digits.

"""


def solution(n):
    sum = 0
    for digit in str(n):
        sum = sum + int(digit)

    return sum
