"""
Author: Bao Nguyen
Assignment / Part: HW3 - Q4
Date Due: February 15, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
import math

a = float(input("Please enter value of a: "))
b = float(input("Please enter value of b: "))
c = float(input("Please enter value of c: "))


if a == 0:
    if b == 0 and c == 0:
        print("\nThis equation has infinite solutions.")
    else:
        print("\nThis equation has no solutions.")
else:
    if b**2 - 4 * a * c > 0:
        solution_1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        solution_2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        print("\nThis equation has 2 solutions: x =", round(solution_1, 4), "and x =", round(solution_2, 4))
    if b**2 - 4 * a * c < 0:
        print("\nThis equation has no real solutions.")
    if b ** 2 - 4 * a * c == 0:
        solution = -b/(2 * a)
        print("\nThis equation has 1 solutions: x =", solution)
