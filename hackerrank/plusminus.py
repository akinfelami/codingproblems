"""
Given an array of integers, calculate the ratios of its elements that are positive, 
negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. 
The test cases are scaled to six decimal places, 
though answers with absolute error of up to  are acceptable. 
"""


def plusMinus(arr):
    x = len(arr)-1

    sumn = 0
    sump = 0
    sumz = 0
    for i in arr:
        if i < 0:
            sumn = sumn + 1
        elif i > 0:
            sump = sump + 1
        else:
            sumz = sumz + 1
    print(str(sump/n))
    print(str(sumn/n))
    print(str(sumz/n))
