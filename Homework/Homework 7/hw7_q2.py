"""
Author: Bao Nguyen
Assignment / Part: HW7 - Q2
Date Due: March 14, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def create_word_pyramid(char, levels):
    word_pyramid = ""
    for i in range(1, levels + 1):
        word_pyramid += char * i + "\n"
        char = chr(ord(char) + 1)
    return word_pyramid.rstrip()


def add_pyramid_level(pyramid):
    updated_count = pyramid.count('\n')
    final_char = pyramid[-1]
    next_char = chr(ord(final_char) + 1)
    new_level = next_char * (updated_count + 2)
    return pyramid + "\n" + new_level


def count_pyramid_levels(pyramid):
    updated_count = 0
    for char in pyramid:
        if char == '\n':
            updated_count += 1
    return updated_count + 1


def main():
    char = 'B'
    levels = 5

    word_pyramid = create_word_pyramid(char, levels)
    print("Word Pyramid:")
    print(word_pyramid)

    updated_pyramid = add_pyramid_level(word_pyramid)
    print("\nUpdated Word Pyramid:")
    print(updated_pyramid)
    print("\nNumber of Levels in Pyramid:", count_pyramid_levels(updated_pyramid))


main()
