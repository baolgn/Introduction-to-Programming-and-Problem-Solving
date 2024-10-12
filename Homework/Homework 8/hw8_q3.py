"""
Author: Bao Nguyen
Assignment / Part: HW8 - Q3
Date Due: April 4, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def create_error_log(dna_sequence, indices_file):
    try:
        with open(indices_file, 'r') as file:
            with open("error_log.txt", "w") as error_file:
                line_number = 1
                for line in file:
                    line = line.replace('\n', '')
                    try:
                        index = int(line)
                        if index >= len(dna_sequence):
                            error_file.write(f"IndexError at LINE {line_number}: The value read, {index}, is larger "
                                             f"than the sequence length of {len(dna_sequence)}.\n")
                    except ValueError:
                        error_file.write(f"ValueError at LINE {line_number}: The value read, '{line}', cannot be "
                                         f"casted into an integer to be used as an index.\n")
                    line_number += 1
    except FileNotFoundError:
        with open("error_log.txt", "w") as error_file:
            error_file.write("FileNotFoundError: The file specified was not found or could not be opened.\n")


def main():
    create_error_log("ACTGC AXT", 'indices.txt')


main()
