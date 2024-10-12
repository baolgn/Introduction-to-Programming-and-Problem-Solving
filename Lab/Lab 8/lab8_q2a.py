"""
Author: Bao Nguyen
Assignment / Part: Lab 8 - Q2a
Date: March 29
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def decreasing_numbers(filename, n):
    try:
        with open(filename, 'w') as file:
            for i in range(n, 0, -1):
                file.write(str(i) + '\n')
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")


def main():
    decreasing_numbers("numbers.txt", 5)


if __name__ == "__main__":
    main()
