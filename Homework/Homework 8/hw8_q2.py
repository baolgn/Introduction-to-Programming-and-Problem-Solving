"""
Author: Bao Nguyen
Assignment / Part: HW8 - Q2
Date Due: April 4, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def get_word_count(file_path):
    try:
        with open(file_path, 'r') as file:
            word_count = 0
            in_word = False
            end_of_file_reached = False
            while not end_of_file_reached:
                char = file.read(1)
                if not char:
                    end_of_file_reached = True
                else:
                    if char.isalnum():
                        if not in_word:
                            word_count += 1
                            in_word = True
                    else:
                        in_word = False
        return word_count
    except FileNotFoundError:
        return None


def main():
    file_path = "voltaire.txt"
    # assumes txt file is in same directory

    count = get_word_count(file_path)
    if count is not None:
        print(f"This file has {count} word(s).")
    else:
        print(f"The file '{file_path}' does not exist.")


main()
