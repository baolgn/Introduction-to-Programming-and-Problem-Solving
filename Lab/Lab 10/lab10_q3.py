"""
Author: Bao Nguyen
Assignment / Part: Lab 10 - Q3
Date: April 12
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def count_vowels(filename):
    vowels = "AEIOUaeiou"
    vowel_counts = {}

    with open(filename, "r") as file:
        text = file.read()

    for char in text:
        if char in vowels:
            char = char.upper()
            if char in vowel_counts:
                vowel_counts[char] += 1
            else:
                vowel_counts[char] = 1

    return vowel_counts


def main():
    filename = "sample_text.txt"
    vowels_output = count_vowels(filename)
    print(vowels_output)


main()
