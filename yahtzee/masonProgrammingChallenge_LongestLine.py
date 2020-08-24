#!/bin/python

import random
import sys

SIZE = 10
LIMIT = 3

VALUE = 0
VISITED = 1

if len(sys.argv) > 1:
    SIZE = int(sys.argv[1])


def printMap(numMap):
    for row in numMap:
        print(row)


def findPath(numMap, location, SIZE):
    paths = [0]
    # find path from each direction
    numMap[location[0]][location[1]][VISITED] = True
    for y in range(-1, 2):
        for x in range(-1, 2):
            if not (0 <= location[0] + x < SIZE):
                continue
            if not (0 <= location[1] + y < SIZE):
                continue
            if (numMap[location[0]+x][location[1]+y][VISITED]):
                # Been visisted
                continue
            if (abs(numMap[location[0]][location[1]][VALUE] - numMap[location[0] + x][location[1] + y][VALUE]) > LIMIT):
                paths.append(
                    findPath(numMap, [location[0] + x, location[1] + y], SIZE))

    return max(paths)+1


def longest(numMap, SIZE):
    #     path = [0]
    #     for y in range(SIZE):
    #         for x in range(SIZE):
    #             path.append(findPath(numMap, [x, y], SIZE))
    #     return max(path)
    return max(max([[findPath(numMap, [x, y], SIZE) for x in range(SIZE)] for y in range(SIZE)]))


map1 = [[1, 9, 5], [6, 4, 3], [2, 8, 7]]
map1 = [[0 if (x+y) % 2 == 0 else 9 for x in range(SIZE)]for y in range(SIZE)]
# printMap(map2)
# map1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# map1 = [[1, 9, 1], [9, 1, 9], [1, 9, 1]]
for row in range(len(map1)):
    for col in range(len(map1[row])):
        map1[row][col] = [map1[row][col], False]
        # print(col)
# print(map1[1][1])
print(longest(map1, len(map1)))
