"""
Some phone usage rate may be described as follows:

first minute of a call costs min1 cents,
each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
each minute after 10th costs min11 cents.
You have s cents on your account before the call. What is the duration of the longest call 
(in minutes rounded down to the nearest integer) you can have?

"""


def solution(min1, min2_10, min11, s):
    x = s - min1  # how much is left after
    if x < 0:
        return 0
    if x == 0:
        return 1
    if x > 0:
        y = min2_10 * 9
        z = x - y
        if z < 0:
            return 1 + x//min2_10
        if z == 0:
            return 10
        if z > 0:
            a = z//min11
            return 10 + a
