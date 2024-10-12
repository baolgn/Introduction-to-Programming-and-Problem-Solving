"""
Author: Bao Nguyen
Assignment / Part: HW8 - Q1
Date Due: April 4, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def find_longest_word_in_file(file_path):
    try:
        longest_word = ""
        current_word = ""
        with open(file_path, 'r') as file:
            char = file.read(1)
            while char:
                if char not in " \t\n\r\f\v" and char not in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
                    current_word += char
                else:
                    if current_word:
                        if len(current_word) > len(longest_word):
                            longest_word = current_word
                        current_word = ""
                char = file.read(1)
        if current_word:
            if len(current_word) > len(longest_word):
                longest_word = current_word
        return longest_word
    except FileNotFoundError:
        return None


def replace_substr_in_file(file_path, target_substr, replacement_word):
    with open(file_path, 'r+') as file:
        content = file.read()
        content = content.replace(target_substr, replacement_word)
        file.seek(0)
        file.write(content)
        file.truncate()


def count_word_occurrences_in_file(file_path, target_word):
    count = 0
    current_word = ""
    with open(file_path, 'r') as file:
        char = file.read(1)
        while char:
            if char not in " \t\n\r\f\v" and char not in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
                current_word += char
            else:
                if current_word:
                    if current_word == target_word:
                        count += 1
                    current_word = ""
            char = file.read(1)
    if current_word == target_word:
        count += 1
    return count


def main():
    input_file = "input.txt"

    found_longest_word = find_longest_word_in_file(input_file)
    if found_longest_word is not None:
        print(f"Longest word in the file: {find_longest_word_in_file(input_file)}")

        target_substr = "test"
        replacement_word = "exam"
        replace_substr_in_file(input_file, target_substr, replacement_word)
        print(f'Replaced "{target_substr}" with "{replacement_word}" in the file.')

        word_to_count = "exam"
        word_occurrences = count_word_occurrences_in_file(input_file, word_to_count)
        print(f'Occurrences of "{word_to_count}" in the file: {word_occurrences}')
    else:
        print(f"The file '{input_file}' does not exist.")


main()
