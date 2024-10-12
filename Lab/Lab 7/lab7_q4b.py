"""
Author: Bao Nguyen
Assignment / Part: Lab 7 - Q4b
Date: March 15
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def prompt_user_for_pw():
    password = input("Please enter your password: ")
    return password


def is_strong_pw(pw):
    if len(pw) < 8:
        return False

    special_characters = '!@#*'
    has_special_char = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in pw:
        if char in special_characters:
            has_special_char = True
        elif char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    return has_special_char and has_uppercase and has_lowercase and has_digit
