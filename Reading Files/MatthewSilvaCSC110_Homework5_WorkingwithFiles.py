#!/usr/bin/env python3

# Matthew Silva CSC 110 - Homework 5 - Working with Files

# Due October 9, 2017 11:55 pm

# Allows the user to specify a text file containing olympics information
# and search that text file for the location of the summer Olympics in
# a given year

# Prompts the user for the path to a text file containing summer olympics
# data (year and location separated by comma, one pair per line) and
# returns a list of the file's years and a list of the file's locations
def getData():
    validFile = False   # Ensures the user's filename could be opened
    while validFile == False:
        fileName = input ("Please enter the name of the data file: ")
        try:
            file = open(fileName, "r")
            validFile = True
        except IOError:
            print("Invalid file name try again ...")
    years = []
    locations = []
    line = file.readline()
    while (line != ""): # Keep parsing lines until an empty line
        year, loc = line.split("\t")
        year.strip()
        year = int(year)
        loc.strip()
        years.append(year)
        locations.append(loc)
        line = file.readline()
    return years, locations

# Takes a year and two corresponding lists of years and locations.
# Returns an empty string if the year was not found in the list of years
# Returns the corresponding location of the given year if it was found.
def findLocation(givenYear, years, locations):
    i = 0
    while ( i < len(years)):
        if givenYear == years[i]:   # If the year was found, return the
            return locations[i]     # location at the same index
        i += 1
    return ""
    

# Main function
def main():
    years, locations = getData()
    validYear = False           # Ensures the user's year input is valid (integer)
    while validYear == False:
        try:
            givenYear = int(input("Enter the year you are interested in: "))
            validYear = True
        except ValueError:
            print("Invalid year - must be an integer")
    locOfYear = findLocation(givenYear, years, locations)
    if locOfYear == "": # If findLocations returned an empty string, nothing was found
        print("No Olympics were held that year")
    else:
        print("In {} the Olympics were held in {}".format(givenYear, locOfYear))
    
    
if __name__ == "__main__":
    main()
