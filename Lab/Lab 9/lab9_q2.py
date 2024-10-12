"""
Author: Bao Nguyen
Assignment / Part: Lab 9 - Q2
Date: April 5
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

import super_secret_module
import random


def is_impostor(information, corrupter_function):
    corrupter_copy = corrupter_function(information)
    information.append("hi")
    if information == corrupter_copy:
        return True
    else:
        return False


def main():
    original_list = [1, 2, 3]

    print(is_impostor(original_list, super_secret_module.corrupter))


main()
