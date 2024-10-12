"""
Author: Bao Nguyen
Assignment / Part: Lab 1 - Q2
Date: February 02
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
scones = int(input("Enter the number of scones you want to make: "))
butter = float((scones * 75/10)/75 * 1/3)
flour = float((scones * 350/10)/150)
milk = float((scones * 150/10)/100 * 1/2)
print("To make", scones, "scones, use", butter, "cups butter", flour, "cups flour", "and", milk, "cups milk")
