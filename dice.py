#!/bin/python

import random


def rollDice(sides, numOfDice, iterations):
    # sides = 6
    # numOfDice = 3
    # iterations = 1000

    results = [0 for x in range(numOfDice * sides + 1)]
    pay = 1
    score = 0
    paid = 0

    for i in range(iterations):
        roll = 0
        paid += pay
        for j in range(numOfDice):
            roll += random.randint(1, sides)
        results[roll] += 1
        if roll == 17 or roll == 39 or roll == 40:
            score += 5
        if roll == 16:
            score += 10
        if roll == 15 or roll == 41:
            score += 15
        if roll == 14 or roll == 42:
            score += 20
        if roll == 13 or roll == 43:
            score += 50
        if roll == 12 or roll == 44:
            score += 50
        if roll == 11 or roll == 45:
            score += 30
        if roll == 10 or roll == 46:
            score += 50
        if roll == 9 or roll == 47:
            score += 100
        if roll == 8 or roll == 48:
            score += 100
        if score >= 100:
            # print("Score", score)
            # print("Cost", pay)
            # print("Round", i+1)
            return [score, pay, i+1, paid]
        if roll == 29:
            pay = pay*2

    # for i in range(numOfDice, len(results)):
    #     print('{:>3}'.format(i), '{:>8}'.format(
    #         round(results[i]/iterations * 100, 6)))


# results = []
score = 0
cost = 0
attempts = 0
paid = 0

a = 100000

for i in range(a):
    result = rollDice(6, 8, 100000)
    score += result[0]
    cost += result[1]
    attempts += result[2]
    paid += result[3]

score = score/a
cost = cost/a
attempts = attempts/a
paid = paid/a

print("Score", score)
print("Cost", cost)
print("Round", attempts)
print("I PAID HOW MUCH", paid)
