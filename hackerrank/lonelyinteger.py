"""
Given an array of integers, where all elements but one occur twice, find the unique element.
"""


def lonelyinteger(a):
    for i in a:
        if a.count(i) == 1:
            return i
