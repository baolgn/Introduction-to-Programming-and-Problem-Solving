"""
Author: Bao Nguyen
Assignment / Part: Lab 4 - Q3
Date: February 23
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
print("Welcome to the Factorial Factory!")

num_factorials = 0
while num_factorials <= 0:
    num_factorials = int(input("Please enter the amount of factorials that you would like to calculate: "))
    if num_factorials <= 0:
        print("ERROR: Please enter a positive amount of factorials to calculate")

for i in range(num_factorials):
    factorial_input = -1
    while factorial_input < 0:
        factorial_input = int(input("Please enter a positive integer: "))
        if factorial_input < 0:
            print("Please enter a positive integer.")

    factorial_result = 1
    for j in range(1, factorial_input + 1):
        factorial_result *= j

    print(factorial_input, "!", sep="", end=" ")
    print("is equal to", factorial_result)

print("Have a nice day! Thanks for visiting the Factorial Factory")
