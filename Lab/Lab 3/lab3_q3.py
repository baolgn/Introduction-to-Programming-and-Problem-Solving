"""
Author: Bao Nguyen
Assignment / Part: Lab 3 - Q3
Date: February 16
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
user_input = input("Enter a string to be printed (in the format [text]-[text]):\n")

print("Printing:")
line = ""

for dash in user_input:
    if dash == "-":
        print(line)
        line = ""
    else:
        line += dash

print(line)