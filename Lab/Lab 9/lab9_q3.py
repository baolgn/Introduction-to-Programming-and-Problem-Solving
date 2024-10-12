"""
Author: Bao Nguyen
Assignment / Part: Lab 9 - Q3
Date: April 5
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

import random


def get_random_word(filepath):
    words = []
    with open(filepath, 'r') as file:
        for line in file:
            word = ''
            for char in line:
                if char != ' ' and char != '\n':
                    word += char
                elif word:
                    words.append(word)
                    word = ''
            if word:
                words.append(word)
    return random.choice(words)


def main():
    print(get_random_word("words.txt"))


main()
