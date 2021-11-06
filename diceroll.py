#Diceroll



import random
from collections import defaultdict

def main():
    dice = int(input("Enter the number of dice: "))
    sides = int(input("Enter the number of sides: "))
    rolls = int(input("Enter the number of rolls to simulate: "))
    result = roll(dice, sides, rolls)
    maxH = 0
    for i in range(dice, dice * sides + 1):
        if result[i] / rolls > maxH: maxH = result[i] / rolls
    for i in range(dice, dice * sides + 1):
        print('{:2d}{:10d}{:8.2%} {}'.format(i, result[i], result[i] / rolls, '#' * int(result[i] / rolls / maxH * 40)))


def roll(dice, sides, rolls):
    d = defaultdict(int)
    for i in range(rolls):
        d[sum(random.randint(1, sides) for i in range(dice))] += 1
    return d

main()
