#!/usr/bin/env python3

# Matthew Silva CSC 110 - Homework 7.2 - Cryptography

# Due October 30, 2017 11:55 pm

# Allows the user to call caesarPlus, which uses a modified Caesar
# cipher to encrypt the given plaintext using a given shift

# Takes a string of plaintext and an integer shift as inputs
# and returns the encrypted ciphertext after applying a modified
# Caesar cipher encryption algorithm
# The algorithm is modified by shifting the plaintext characters by the given
# shift plus their position within the string.
def caesarPlus(plaintext,shift):  
	alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]  
	# initialize ciphertext as blank string
	ciphertext = ""
	# loop through the length of the plaintext
	for i in range(len(plaintext)):				        
		# get the ith letter from the plaintext
		letter = plaintext[i]					
		# find the number position of the ith letter
		num_in_alphabet = alphabet.index(letter)		
		# find the number position of the cipher by adding the shift	
		cipher_num = (num_in_alphabet + shift + i) % len(alphabet)	
		# find the cipher letter for the cipher number you computed
		# Note that the cipher is shift is modified by the current
		# index of the plaintext 
		cipher_letter = alphabet[cipher_num]			
		# add the cipher letter to the ciphertext
		ciphertext = ciphertext + cipher_letter			
		# return the computed ciphertext
	return ciphertext	
