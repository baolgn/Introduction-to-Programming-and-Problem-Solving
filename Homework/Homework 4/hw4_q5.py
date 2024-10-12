"""
Author: Bao Nguyen
Assignment / Part: HW4 - Q5
Date Due: February 22, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
sandcastle_layers = int(input("Please enter a positive integer: "))

for line in range(sandcastle_layers, 0, -1):
    print(" " * (sandcastle_layers - line), end="")
    for asterisk in range(2 * line - 1):
        print("*", end="")
    print()

for line in range(1, sandcastle_layers):
    print(" " * (sandcastle_layers - line - 1), end="")
    for asterisk in range(2 * line + 1):
        print("*", end="")
    print()
