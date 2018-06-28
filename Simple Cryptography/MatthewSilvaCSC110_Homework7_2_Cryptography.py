#!/usr/bin/env python3

# Matthew Silva CSC 110 - Homework 7.2 - Cryptography

# Due October 30, 2017 11:55 pm

# Allows the user to call poly2, which uses a modified polyalphabetic
# cipher to encrypt the given plaintext using a given codeword/secret

# Takes a string of plaintext and a string codeword/keyword phrase as inputs
# and returns the encrypted ciphertext after applying a modified
# polyalphabetic cipher encryption algorithm
# The algorithm is modified by appending the alphabet to the end of the
# codeword/keyword such that it is not repeated
def poly2(plaintext,codeword):
        alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        while len(codeword) < len(plaintext):   # While the codeword's shorter than plaintext,
            for i in range(len(alphabet)):      # append the alphabet to the end of it
                codeword = codeword + alphabet[i]
        ciphertext = ""
        for i in range(len(plaintext)): # Encrypt the plaintext to ciphertext
                letter = plaintext[i]
                num_in_alphabet = alphabet.index(letter)

                # Find the position in the codeword with the letter to shift
                shiftIndex = i % len(codeword)
                
                # Find the letter in the codeword to shift
                shiftLetter = codeword[shiftIndex]
                
                # Find the number associated with the letter to be used as the shift
                shift = alphabet.index(shiftLetter)
                
                cipher_num = (num_in_alphabet + shift) % len(alphabet)
                cipher_letter = alphabet[cipher_num]
                ciphertext = ciphertext + cipher_letter
        return ciphertext

