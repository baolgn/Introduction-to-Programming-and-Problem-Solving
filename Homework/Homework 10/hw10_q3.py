"""
Author: Bao Nguyen
Assignment / Part: HW10 - Q3
Date Due: April 18, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def word_frequency_counter(file_path):
    try:
        word_stats = {}

        with open(file_path, 'r') as file:
            lines = file.readlines()

            for line_number, line in enumerate(lines):
                words = line.strip().split()

                for position, word in enumerate(words):
                    if word in word_stats:
                        word_stats[word][0] += 1
                        word_stats[word][1].append(position)
                        word_stats[word][2].append(line_number)
                    else:
                        word_stats[word] = [1, [position], [line_number]]

        return word_stats

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred while processing the file '{file_path}': {e}")
        return None


def main():
    input_file = "sample_file.txt"
    word_stats = word_frequency_counter(input_file)
    if word_stats is not None:
        print("{")
        for word, (frequency, positions, lines) in word_stats.items():
            print(f"'{word}': ({frequency}, {positions}),")
        print("}")
    else:
        print("Word frequency counting failed.")


main()
