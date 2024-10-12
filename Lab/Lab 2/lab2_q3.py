"""
Author: Bao Nguyen
Assignment / Part: Lab 2 - Q3
Date: February 09
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
import random

pseudo_slope = random.randint(-5, 5)
pseudo_intercept = random.randint(0, 10)

print("Welcome to Drawing Parallels! Test whether your line is parallel to the line f(x) = ", pseudo_slope, "x + ",
      pseudo_intercept, sep="")
input_slope = int(input("Enter a slope: "))
input_intercept = int(input("Enter a y-intercept: "))
lines_parallel = "PARALLEL" if pseudo_slope == input_slope else "NOT PARALLEL"

if lines_parallel == "PARALLEL" and pseudo_intercept == input_intercept:
      print("Your line f(x) = ", input_slope, "x + ", input_intercept, " is identical to the line f(x) = ",
            pseudo_slope, "x + ", pseudo_intercept, sep="")
else:
      print("Your line f(x) = ", input_slope, "x + ", input_intercept, " is ", lines_parallel, " to the line f(x) = ",
            pseudo_slope, "x + ", pseudo_intercept, sep="")
