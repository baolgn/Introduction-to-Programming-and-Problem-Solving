"""
Author: Bao Nguyen
Assignment / Part: Lab 8 - Q2b
Date: March 29
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def squared_numbers(filename, outFile):
    try:
        with open(filename, 'r') as file:
            with open(outFile, 'w') as out_file:
                for line in file:
                    number = int(line.strip())
                    squared = number ** 2
                    out_file.write(str(squared) + '\n')
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")


def main():
    squared_numbers("numbers.txt", "squaredNumbers.txt")


if __name__ == "__main__":
    main()
