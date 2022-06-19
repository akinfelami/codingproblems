"""
Given five positive integers, find the minimum and maximum values that can be calculated by 
summing exactly four of the five integers. Then print the respective minimum and maximum 
values as a single line of two space-separated long integers.
"""


def miniMaxSum(arr):
    min = arr[0]
    max = arr[0]
    sum = 0
    for i in arr:
        sum += i
        if i > max:
            max = i
        elif i < min:
            min = i

    print(str(sum - max) + " " + str(sum - min))
