"""
Author: Bao Nguyen
Assignment / Part: Lab 3 - Q5
Date: February 16
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
num_values = int(input("Please enter how many positive values you want to consider: "))
largest_value = 0

for i in range(1, num_values + 1):
    value = float(input())
    if i == 0 or value > largest_value:
        largest_value = value

print("The largest of these values is", largest_value)
