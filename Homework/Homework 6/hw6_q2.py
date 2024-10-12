"""
Author: Bao Nguyen
Assignment / Part: HW6 - Q2
Date Due: March 07, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
max_num = int(input("Enter a positive integer 'max_num': "))

pattern = 'A'
print("\nIteration 1:", pattern)

for i in range(2, max_num + 1):
    new_pattern = ""
    for char in pattern:
        if char == 'A':
            new_pattern += 'B'
        elif char == 'B':
            new_pattern += 'A'
    pattern += new_pattern
    print("Iteration " + str(i) + ": " + pattern)
