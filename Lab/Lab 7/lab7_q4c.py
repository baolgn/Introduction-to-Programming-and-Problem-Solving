"""
Author: Bao Nguyen
Assignment / Part: Lab 7 - Q4c
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


def main():
    print("Welcome!")
    while True:
        password = prompt_user_for_pw()
        if is_strong_pw(password):
            print("Thank you! Your password is considered strong.")
            return
        else:
            print("Password too weak! Strong passwords must be greater than or equal to 8 characters in length, "
                  "contain at least 1 special character from the following: '!', '@', '#', '*', "
                  "contain at least 1 uppercase character, "
                  "contain at least 1 lowercase character, "
                  "and contain at least 1 number\n")


if __name__ == "__main__":
    main()
