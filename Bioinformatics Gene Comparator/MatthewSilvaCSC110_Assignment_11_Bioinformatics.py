#!/usr/bin/env python3

# Matthew Silva CSC 110 - Homework 11 - Bioinformatics

# Due December 4, 2017 11:55 pm

# Program to find all possible alignments of a pair of strings when adding
# gaps to the shorter string. Prints the optimal alignments and the work
# required to generate and score those alignments.

# Given:    Two strings of nucleotides
# Find:     The optimal alignments when adding gaps to the shorter string 

# Global variables to track work for adding gaps and comparisons of string
# characters
gap_work = 0
compare_work = 0

# Function to create a list of all ways one gap can be inserted into
# a string.  The input is a string, the output is a list of strings
# with a gap inserted into all positions of the input string

def insertOneGap(strng):
    global gap_work
    alignments = []
    for i in range(len(strng)):
        newStrng = strng[0:i] + '-' + strng[i:len(strng)]
        alignments = alignments + [newStrng]
        gap_work += 1
    alignments = alignments + [strng + '-']
    return alignments
            
# Function to take a set union of a pair of lists
# This is used to eliminate any duplicates in the list when they are combined
def Union(list1, list2):
    for a in list2:
        if a not in list1:
            list1 = list1 + [a]
    return list1


# Function to create all possible alignments of a string with a certain number
# of gaps inserted
def insertAllGaps(strng, gaps):
    # List of alignments starts with the initial string
    alignments = [strng]

    # Loop to insert one gap at a time
    for i in range(gaps):

        # Initialize list of new alignments with i gaps in the string
        newAlignments = []

        # For every string in the list of alignments
        for st in alignments:
            # Insert one gap in each alignment in the list
            al = insertOneGap(st)

            # Add the new alignment to the list of new alignments being created
            newAlignments = Union(newAlignments,al)

        # The alignments list now becomes the new alignments list to now
        # add another gap to each of the alignments in the new list
        alignments = newAlignments
    return alignments


# Function to print the optimal alignments and the work peformed to create
# and score these alignments

def printResults(st, alignments, scores):
    print("There are ", len(alignments), " alignments")
    print("The following alignments are optimal")
    for i in range(len(scores)):
        print(st)
        print(alignments[i])
        print("Score = " + str(scores[i]))
        print(" ")
    print("Amount of work done (gaps): " + str(gap_work))
    print("Amount of work done (comparisons): " + str(compare_work))

# Takes the string and the array of alignments
# Returns an array of scores based on the similarity between
# the string and the alignment
def computeScores(string, alignments):
    global compare_work # Call global variable into function
    scores = []
    for alignment in alignments:    # For each alignment...
        score = 0
        for i in range(len(string)):    # For each character in the string...
            if alignment[i] == '-': # If there's a gap, decrease the score
                score -= 1
            if alignment[i] == string[i]:   # If there's a match, increase the score
                score += 1
            compare_work += 1 
        scores.append(score)    # Add each new computed score to a list
    return scores

# Takes an array of scores and an array of alignments
# Returns an array of the highest scores and their corresponding alignments
def optimalScores(scores, alignments):
    optScores = []  # Initializes the new lists of optimal scores and alignments
    optAligns = []
    maxVal = scores[0]
    for i in range(len(scores)):    # Find the maximum score
        if scores[i] > maxVal:
            maxVal = scores[i]
    for i in range(len(scores)):
        if scores[i] == maxVal: # If a score is the maximum...
            optScores.append(scores[i]) # Add the score to an array...
            optAligns.append(alignments[i]) # And add the alignment to an array
    return optScores, optAligns
                
# Main function
def main():
    # Get the two strings to align
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")

    # Compute alignments adding gaps to the shorter string
    if len(str1) > len(str2):
        longStr = str1
        shortStr = str2
    else:
        longStr = str2
        shortStr = str1

    alignments = insertAllGaps(shortStr,len(longStr)-len(shortStr))
    scores = computeScores(longStr, alignments) # Score the alignments
    scores, alignments = optimalScores(scores, alignments)  # Find only the best alignments
    printResults(longStr,alignments, scores)    # Print the optimal alignments & scores

    # These have to be initialized back to 0 after main is called
    # because otherwise successive calls of main() will compute a running
    # total of the work completed instead of the individual task's work
    global gap_work
    gap_work = 0
    global compare_work
    compare_work = 0


if __name__ == "__main__":
    main()