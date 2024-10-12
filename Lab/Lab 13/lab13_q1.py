"""
Author: Bao Nguyen
Assignment / Part: Lab 13 - Q1
Date: May 3
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    print(factorial(4))


main()
