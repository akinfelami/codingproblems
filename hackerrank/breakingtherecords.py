"""
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points and least points in a game.
 Points scored in the first game establish her record for the season, and she begins counting from there.
"""


def breakingRecords(scores):
    min = scores[0]
    max = scores[0]
    mincount = 0
    maxcount = 0
    for i in scores:
        if i < min:
            min = i
            mincount += 1
        elif i > max:
            max = i
            maxcount += 1

    return [maxcount, mincount]
