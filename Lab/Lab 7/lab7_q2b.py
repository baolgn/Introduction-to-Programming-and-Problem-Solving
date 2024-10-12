"""
Author: Bao Nguyen
Assignment / Part: Lab 7 - Q2b
Date: March 15
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def numberify(word):
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
            numberified_word += char.upper()
    return numberified_word


def main():
    message = input("Please enter a message to numberify: ")
    words = message.split()
    numberified_message = ""
    for word in words:
        if len(word) > 3:
            numberified_message += numberify(word) + " "
        else:
            numberified_message += word.upper() + " "
    print("Your numberified string is:", numberified_message.strip())


if __name__ == "__main__":
    main()
