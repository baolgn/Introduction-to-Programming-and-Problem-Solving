"""
Author: Bao Nguyen
Assignment / Part: Lab 13 - Q2
Date: May 3
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)


countdown(24)
