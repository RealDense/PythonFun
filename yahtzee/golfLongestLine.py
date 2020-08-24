#!/bin/python

import random
import sys

SIZE = 10
LIMIT = 3

VALUE = 0
VISITED = 1


def findPath(numMap, location, SIZE):
    numMap[location[0]][location[1]][VISITED] = True
    paths = []
    # find path from each direction
    for y in [-1, 0, 1]:
        for x in range(-1, 2):
            if (0 <= location[0] + x < SIZE) and (0 <= location[1] + y < SIZE) and not (numMap[location[0]+x][location[1]+y][VISITED]) and (abs(numMap[location[0]][location[1]][VALUE] - numMap[location[0] + x][location[1] + y][VALUE]) > LIMIT):
                paths.append(
                    findPath(numMap, [location[0] + x, location[1] + y], SIZE))
    return max(paths, default=0)+1
    # return max(max(
    #     [
    #         [

    #             (findPath(numMap, [location[0] + x, location[1] + y], SIZE), 1)
    #             for x in [-1, 0, 1]
    #             if ((0 <= location[0] + x < SIZE) and (0 <= location[1] + y < SIZE) and not (numMap[location[0]+x][location[1]+y][VISITED])) and (abs(numMap[location[0]][location[1]][VALUE] - numMap[location[0] + x][location[1] + y][VALUE]) > LIMIT)
    #         ]
    #         for y in [-1, 0, 1]]
    # ))+1


map1 = [[1, 9, 5], [6, 4, 3], [2, 8, 7]]
map1 = [[0 if (x+y) % 2 == 0 else 9 for x in range(SIZE)]for y in range(SIZE)]
# map1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# map1 = [[1, 9, 1], [9, 1, 9], [1, 9, 1]]
map1 = [[[map1[row][col], False]
         for col in range(SIZE)] for row in range(SIZE)]
print(max(max([[findPath(map1, [x, y], SIZE)
                for x in range(SIZE)] for y in range(SIZE)])))


SIZE = 10


def findPath(numMap, location):
    numMap[location[0]][location[1]]['visited'] = True
    return max(max(max([[findPath(numMap, [location[0] + x, location[1] + y])for x in [-1, 0, 1]if not(not (0 <= location[0] + x < SIZE) or not (0 <= location[1] + y < SIZE) or (numMap[location[0]+x][location[1]+y]['visited'])) and (abs(numMap[location[0]][location[1]]['value'] - numMap[location[0] + x][location[1] + y]['value']) > 3)]for y in [-1, 0, 1]]), [0]))+1


print(max(max([[findPath([[{'value': 0 if (col+row) % 2 == 0 else 9, 'visited': False}
                           for col in range(SIZE)] for row in range(SIZE)], [x, y])
                for x in range(SIZE)] for y in range(SIZE)])))
