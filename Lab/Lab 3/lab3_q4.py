"""
Author: Bao Nguyen
Assignment / Part: Lab 3 - Q4
Date: February 16
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
base = float(input("Please enter a positive integer to serve as the base: "))
highest_power = float(input("Please enter a positive integer to serve as the highest power: "))

if base <= 0 or highest_power <= 0 or highest_power % 1 != 0 or base % 1 != 0:
    print("ERROR: Both values must be POSITIVE INTEGERS.")
else:
    for power in range(0, highest_power + 1):
        print(base, "^", power, "=", base**power)
