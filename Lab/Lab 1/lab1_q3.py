"""
Author: Bao Nguyen
Assignment / Part: Lab 1 - Q3
Date: February 02
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
import math

scoops = int(input("Enter the number of ice cream scoops you want: "))
radius = float(input("Enter the radius of ice cream cone: "))
height = float(input("Enter the height of ice cream cone: "))
scoops_volume = float(scoops * 4/3 * math.pi * radius**3)
cone_volume = float(math.pi * radius**2 * height/3)
print("Your", scoops, "scoop ice cream cone has a total volume of", scoops_volume + cone_volume)
