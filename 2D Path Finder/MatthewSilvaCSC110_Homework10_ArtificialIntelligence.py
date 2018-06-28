#!/usr/bin/env python3

# Matthew Silva CSC 110 - Homework 10 - Artificial Intelligence

# Due November 27, 2017 11:55 pm

# This is the next_move function for the HackerRank AI Challenge, BotClean.
# next_move will print out the next move of the bot when provided with the
# row position of the bot, the column position of the bot, and the board.
# The goal of the bot is to clean the board of all dirt, represented as
# a 'd'.

# Takes the row position of the bot, the column position of the bot, and
# the board as a 2 dimensional array with 5 rows and 5 columns
# Prints the next move of the bot, which will either be a direction
# (RIGHT, LEFT, DOWN, UP), or a cleaning command (CLEAN).
# The bot will always move towards the closest dirt spot or clean a dirt
# spot that it is on top of.
def next_move(posr, posc, board):
    nextDirtR, nextDirtC = closestDirt(posr, posc, board)
    if (nextDirtR != -1 and nextDirtC != -1):   # If dirt is still left
        if (nextDirtC > posc):
            print("RIGHT")
        elif (nextDirtC < posc):
            print("LEFT")
        elif (nextDirtR > posr):
            print("DOWN")
        elif (nextDirtR < posr):
            print("UP")
        else:   # If the bot is on top of the dirt, clean it
            print("CLEAN")
    print("")

# Takes the row position of the bot, the column position of the bot, and
# the board as a 2 dimensional array with 5 rows and 5 columns.
# Find the closest dirt space to the bot in terms of the number of moves
# required to reach it and returns the row position and column position of
# that space of dirt
def closestDirt(posr, posc, board):
    dirtsR = []
    dirtsC = []
    distances = []
    for r in range(5):      # For 5 rows
        for c in range(5):  # For 5 columns
            if board[r][c] == "d":  # Record positions of dirt spaces
                dirtsR.append(r)
                dirtsC.append(c)
    if len(dirtsR) == 0:    # If no dirt spaces were found, return -1, -1
        return -1, -1
    for i in range(len(dirtsR)):    # Calculate distances from bot to dirts
        distances.append(abs(dirtsR[i] - posr) + abs(dirtsC[i] - posc))
    minDist = distances[0]  # Initialize minimums
    minDistIndex = 0
    for i in range(len(distances)): # Find the closest dirt's index
        if distances[i] < minDist:
            minDist = distances[i]
            minDistIndex = i                            # Return row and column
    return dirtsR[minDistIndex], dirtsC[minDistIndex]   # of closest dirt

# main function for testing
def main():
    grid = [['b','-','-','-','d'],
        ['-','d','-','-','d'],
        ['-','-','d','d','-'],
        ['-','-','d','-','-'],
        ['-','-','-','-','d']]

    next_move(0,0,grid)


if __name__ == "__main__":
    main()
