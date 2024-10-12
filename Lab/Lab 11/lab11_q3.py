"""
Author: Bao Nguyen
Assignment / Part: Lab 11 - Q3
Date: April 19
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def count_vowels(filename):
    vowels = "AEIOU"
    vowel_counts = {vowel: 0 for vowel in vowels}

    with open(filename, "r") as file:
        text = file.read().upper()

    for vowel in vowels:
        vowel_counts[vowel] = text.count(vowel)

    return vowel_counts


def main():
    filename = "sample_text.txt"
    vowels_output = count_vowels(filename)
    print(vowels_output)


main()
