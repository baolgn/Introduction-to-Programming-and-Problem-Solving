"""
Author: Bao Nguyen
Assignment / Part: Lab 3 - Q2
Date: February 16
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
print("This is a four operation calculator.")
check_input = input("Hit enter to continue or Q to quit calculator: ")

while check_input != "Q":

    if check_input == "":
        first_number = float(input("Enter your first number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        second_number = float(input("Enter your second number: "))

        if operation == "+":
            answer = first_number + second_number
            print(first_number, operation, second_number, "=", answer)
        if operation == "-":
            answer = first_number - second_number
            print(first_number, operation, second_number, "=", answer)
        if operation == "*":
            answer = first_number * second_number
            print(first_number, operation, second_number, "=", answer)
        if operation == "/":
            if second_number != 0:
                answer = first_number / second_number
                print(first_number, operation, second_number, "=", answer)
            else:
                print(first_number, operation, second_number, "is an invalid operation.")

    check_input = input("Hit enter to continue or Q to quit calculator: ")
