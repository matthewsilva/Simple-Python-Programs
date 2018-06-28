#!/usr/bin/env python3

# Matthew Silva CSC 110 - Homework 6.2 - Analysis of Algorithms

# Due October 23, 2017 11:55 pm

# Allows the user to specify a text file containing population data for
# US states and prints out the list of states and populations, now sorted
# by population

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

# Takes two lists and sorts the first, performing the same operations on
# the second list to maintain their correspondence 
def dualSort(list1, list2):
    for i in range(0, len(list1)):            
        min = i
        for j in range(i + 1, len(list1)):
            # comparison
            if list1[j] < list1[min]:
                min = j
        # swap
        list1[i], list1[min] = list1[min], list1[i]
        list2[i], list2[min] = list2[min], list2[i]
    return list1, list2

# Prompts the user to enter a filename for a text file containing state
# population data and then sorts the list using selection sort, printing
# the sorted list after completion
def main():
    stateList, popList = getStateData()
    popList, stateList = dualSort(popList, stateList)
    for i in range(len(popList)):
        print(stateList[i], popList[i])


if __name__ == "__main__":
    main()