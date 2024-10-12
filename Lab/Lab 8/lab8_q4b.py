"""
Author: Bao Nguyen
Assignment / Part: Lab 8 - Q4a
Date: March 29
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def get_last_char(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in reversed(lines):
                for char in reversed(line):
                    if char.isalpha():
                        return char
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
        return None


def alphabet_soup(filename):
    last_char = get_last_char(filename)
    if last_char is None:
        last_char = 'a'
    else:
        last_char = chr(ord(last_char) + 1)

    with open(filename, 'a') as file:
        for char in range(ord(last_char), ord('z') + 1):
            file.write('\n' + chr(char))


def main():
    ALPHABET_FILE = "alphabet.txt"
    alphabet_soup(ALPHABET_FILE)
    last_char = get_last_char(ALPHABET_FILE)
    if last_char is not None:
        print(f"The last alphabetic character in '{ALPHABET_FILE}' is: {last_char}")
    else:
        print(f"No alphabetic character found in '{ALPHABET_FILE}'")


if __name__ == "__main__":
    main()
