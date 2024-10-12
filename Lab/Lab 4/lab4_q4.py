"""
Author: Bao Nguyen
Assignment / Part: Lab 4 - Q4
Date: February 23
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
for column in range(1, 6):
    for row in range(1, 11):
        print(row ** column, sep="\t", end="\t")
    print()
