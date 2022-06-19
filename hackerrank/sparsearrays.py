"""
There is a collection of input strings and a collection of query strings. 
For each query string, determine how many times it occurs in the list of input strings. 
Return an array of the results.
"""


def matchingStrings(strings, queries):
    result = []
    for i in queries:
        count = 0
        for j in strings:
            if i == j:
                count += 1
        result.append(count)
    return result
