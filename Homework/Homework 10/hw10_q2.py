"""
Author: Bao Nguyen
Assignment / Part: HW10 - Q2
Date Due: April 18, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def group_anagrams(file_path):
    try:
        with open(file_path, 'r') as file:
            words = list(set(line.strip() for line in file))

        anagram_groups = {}

        for word in words:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            else:
                anagram_groups[sorted_word] = [word]

        anagrams = list(anagram_groups.values())

        return anagrams

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None

    except Exception as e:
        print(f"An error occurred while processing the file '{file_path}': {e}")
        return None


def main():
    input_file = "sample_file.txt"
    anagrams = group_anagrams(input_file)
    if anagrams is not None:
        print(anagrams)
    else:
        print("Anagram grouping failed.")


main()
