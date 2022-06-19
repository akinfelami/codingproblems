"""
Given an array of integers and a positive integer , determine the number of (i,j)
pairs where i<j and ar[i] + ar[j] is divisible by k.

"""


def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(n):
            if i < j and (ar[i]+ar[j]) % k == 0:
                count += 1
    return count
