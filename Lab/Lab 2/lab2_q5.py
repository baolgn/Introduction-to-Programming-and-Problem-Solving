"""
Author: Bao Nguyen
Assignment / Part: Lab 2 - Q5
Date: February 09
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

first_number = float(input("Enter your first number: "))
operation = input("Enter the operation (+, -, *, /): ")
second_number = float(input("Enter your second number: "))

if operation == "+":
    answer = first_number + second_number
if operation == "-":
    answer = first_number - second_number
if operation == "*":
    answer = first_number * second_number
if operation == "/":
    if second_number != 0:
        answer = first_number / second_number

if operation == "/":
    if second_number != 0:
        print(first_number, operation, second_number, "=", answer)
    else:
        print(first_number, operation, second_number, "is an invalid operation.")
else:
    print(first_number, operation, second_number, "=", answer)
