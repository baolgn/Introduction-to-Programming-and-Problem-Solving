"""
Author: Bao Nguyen
Assignment / Part: Lab 1 - Q5
Date: February 02
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
integer = int(input("Enter an integer less than 100: "))
L = int(integer//50)
X = int((integer % 50)//10)
V = int(((integer % 50) % 10) // 5)
I = int(((integer % 50) % 10) % 5)
if integer < 100:
    print("L"*L, "X"*X, "V"*V, "I"*I, sep="")
else:
    print("Integer is larger than 100!")