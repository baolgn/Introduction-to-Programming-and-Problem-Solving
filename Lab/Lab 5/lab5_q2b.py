"""
Author: Bao Nguyen
Assignment / Part: Lab 5 - Q2B
Date: March 1
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
user_input = input("Enter your phrase: ")
reversed_input = ""

for i in range(len(user_input) - 1, -1, -1):
    reversed_input += user_input[i]

print(reversed_input)
