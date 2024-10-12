"""
Author: Bao Nguyen
Assignment / Part: HW2 - Q3
Date Due: February 08, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
import math
import random

random_integer = random.randint(1, 20)
sqrt = math.sqrt(random_integer)
area = ((sqrt**2)*math.pi)

print("Random integer(1-20):", random_integer)
print("Square root of 20 is:", round(sqrt, 2))
print("\nArea of a circle with radius", round(sqrt, 2), "is:", round(area, 2))
