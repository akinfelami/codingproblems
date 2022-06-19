
import sys

"""
Camel Case is a naming style common in many programming languages.
In Java, method and variable names typically start with a lowercase letter,
with all subsequent words starting with a capital letter(example:
                                                            * startThread).
Names of classes follow the same pattern, except that they start with a
capital letter(example: BlueCar).
Your task is to write a program that creates or splits Camel Case variable,
method, and class names.
"""


def solution(STDIN):
    inputData = [input().rstrip() for line in sys.stdin.readlines()]

    for STDIN in inputData:

        # Split operation
        if STDIN[0] == 'S':
            # Method
            # if STDIN[2] == 'M':
            pos = 4
            result = ''
            for i in STDIN[4:]:
                if i.isupper():
                    if STDIN[pos-1] == ';':
                        result = result + i.lower()
                        pos += 1
                    else:
                        result = result + ' ' + i.lower()
                        pos += 1
                else:
                    if i == "(" or i == ")":
                        pos += 1
                    else:
                        result = result + i
                        # Have to increase position anyway
                        pos += 1
            print(result, file=sys.stdout)
        elif STDIN[0] == 'C':
            # Method
            if STDIN[2] == 'M':
                pos = 4
                result = ''
                for i in STDIN[4:]:
                    if i == ' ':
                        pos += 1
                    else:
                        if STDIN[pos-1] == ' ':
                            result = result + i.upper()
                            pos += 1
                        else:
                            result = result + i
                            pos += 1
                print(result + '()')
            elif STDIN[2] == 'V' or STDIN[2] == 'C':
                pos = 4
                result = ''
                for i in STDIN[4:]:
                    if i == ' ':
                        pos += 1
                    else:
                        if STDIN[pos-1] == ' ':
                            result = result + i.upper()
                            pos += 1
                        else:
                            result = result + i
                            pos += 1
                print(result)
