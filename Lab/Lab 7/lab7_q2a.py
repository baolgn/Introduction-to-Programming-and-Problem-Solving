"""
Author: Bao Nguyen
Assignment / Part: Lab 7 - Q2a
Date: March 15
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def numberify(word):
    """
    Returns a numberified version of the passed-in string word.
    """
    numberified_word = ""
    for char in word:
        if char.upper() == 'A':
            numberified_word += '4'
        elif char.upper() == 'E':
            numberified_word += '3'
        elif char.upper() == 'I':
            numberified_word += '1'
        elif char.upper() == 'S':
            numberified_word += '5'
        elif char.upper() == 'T':
            numberified_word += '7'
        elif char.upper() == 'O':
            numberified_word += '0'
        else:
            numberified_word += char
    return numberified_word
