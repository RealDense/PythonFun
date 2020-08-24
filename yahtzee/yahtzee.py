#!/bin/python

import random

games = 50000
rounds = 13
numOfDice = 5
results = {'yahtzee': [0, 0, 0], '4 of a Kind': 0,
           '3 of a Kind': 0, 'got in a game': 0, 'in one game': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}


def rollDice(numDice):
    rolls = []
    for roll in range(numDice):
        rolls.append(random.randint(1, 6))

    return rolls


for game in range(games):
    if game % 500 == 0:
        print(game)
    rolledYahtzee = False
    yThisGame = 0
    for i in range(rounds):
        numOfSame = 0
        most = 0
        # print("-------------")
        for j in range(3):
            countValues = [0, 0, 0, 0, 0, 0]
            countValues[most] = numOfSame
            rolls = rollDice(numOfDice - numOfSame)
            for k in range(6):
                countValues[k] += rolls.count(k+1)
            most = countValues.index(max(countValues))
            numOfSame = countValues[most]
            # print(rolls)
            # print(most+1)
            # print(countValues)
            if numOfSame == numOfDice:
                results['yahtzee'][j] += 1
                yThisGame += 1
                rolledYahtzee = True
                # print("yahtzee")
                break
            # print(set(rolls))
            # if len(set(rolls)) == 1:
            #     results['yahtzee'][j] += 1
        if numOfSame == 4:
            results['4 of a Kind'] += 1
        if numOfSame == 3:
            results['3 of a Kind'] += 1
    if rolledYahtzee:
        results['got in a game'] += 1
    if yThisGame > 0:
        results['in one game'][yThisGame - 1] += 1

print(results)

print("Probabilities for rolls")
print("-----------------------")
print("Yahtzee     -- %d", results['got in a game']/games * 100)
print("4 of a kind -- %d", results['4 of a Kind']/games * 100)
print("3 of a kind -- %d", results['3 of a Kind']/games * 100)
