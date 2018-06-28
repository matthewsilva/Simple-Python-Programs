#!/usr/bin/env python3

# Matthew Silva CSC 110 - Homework 6.2 - Analysis of Algorithms

# Due October 23, 2017 11:55 pm

# Allows the user to specify a text file containing population data for
# US states. Prompts the user to enter the abbreviation for a state and
# prints the population for the state, as well as the number of comparisons
# required to find the population using a binary or linear search algorithm

# Prompts the user to enter the name of a file, and returns the opened file
# Will prompt the user for input again if the file name was invalid
def getFile():
    validFile = False
    while validFile == False:   # Keeps prompting for filename until valid file is opened
        fileName = input ("Please enter the name of the data file: ")
        try:
            file = open(fileName, "r")
            validFile = True
        except IOError:
            print("Invalid file name try again ...")
    return file

# Gets state population data from the user-specified text file and returns
# the list of states and the list of their corresponding populations
def getStateData():
    inFile = getFile()
    stateList = []
    popList = []
    line = inFile.readline()
    line = line.strip()
    while line != '':   # Keeps reading lines until empty line
        state, population = line.split(",")
        state = state.strip()
        stateList.append(state)
        population = population.strip()
        population = int(population)
        popList.append(population)
        line = inFile.readline()
        line.strip()
    return stateList, popList

# Takes a list of states, a list of their populations, and a state abbreviation
# and uses a linear search algorithm to find and return the population of the
# state with the given abbreviation. Returns -1 if the state wasn't found
# Also separately returns the number of comparisons made to find the state
def getPopLinear(stateList, popList, state):
    counter = 0
    found = False
    population = -1
    i = 0
    while i < len(stateList) and found == False:    # Stops if the end was reached
        counter += 1                                # or if the state was found
        if stateList[i] == state:   # State was found
            population = popList[i]
            found = True
        i += 1
    return population, counter

# Takes a list of states sorted alphabetically, a list of their populations,
# and a state abbreviation and uses a binary search algorithm to find and
# return the population of the state with the given abbreviation. Returns
# -1 if the state wasn't found
# Also separately returns the number of comparisons made to find the state
def getPopBinary(stateList, popList, state):
    counter = 0
    found = False
    population = -1
    first = 0
    last = len(stateList) -1
    while first <= last and found == False: # Stops if the spot where the state should
        counter += 1                        # have been was passed or the state was found
        middle = (last+first)//2
        if stateList[middle] == state:  # State was found in the middle
            population = popList[middle]
            found = True
        elif stateList[middle] > state: # If the state comes earlier, reset last to middle-1
            last = middle - 1
        else:                           # If the state comes later, first to middle+1
            first = middle + 1
    return population, counter

# Prompts the user for the filepath of a text file containing state population data,
# sorted alphabetically by the state's abbreviation. Prompts the user for a state's
# abbreviation and finds that state's population using both a linear and binary
# search. Prints the population and the number of comparisons required for each
# search algorithm.
def main():
    stateList, popList = getStateData()
    state = input("Enter state abbreviation: ")
    linearPop, linearComps = getPopLinear(stateList, popList, state)
    binaryPop, binaryComps = getPopBinary(stateList, popList, state)
    if linearPop == -1: # If the state wasn't found, print error instead of found info
        print("Invalid state abbreviation")
    else:
        print("Binary Search: comps = {}".format(binaryComps))
        print("Linear Search: comps = {}".format(linearComps))
        print("The population of {} is {}".format(state,linearPop))
        print("The population of {} is {}".format(state,binaryPop))


if __name__ == "__main__":
    main()
