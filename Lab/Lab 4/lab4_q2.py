"""
Author: Bao Nguyen
Assignment / Part: Lab 4 - Q2
Date: February 23
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
check_input = input("Press ENTER to continue or Q to quit calculator: ")

while check_input != "Q":
    if check_input == "":
        first_factor = int(input("Please input your first factor: "))
        second_factor = int(input("Please input your first factor: "))

        if first_factor > 0 and second_factor > 0:
            product = 0
            for i in range(second_factor):
                product += first_factor
            print("Your product is:", product)

        else:
            print("ERROR: Positive integers must be entered.")

    check_input = input("Hit enter to continue or Q to quit calculator: ")
