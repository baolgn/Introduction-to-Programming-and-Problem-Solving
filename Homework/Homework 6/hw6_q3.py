"""
Author: Bao Nguyen
Assignment / Part: HW6 - Q3
Date Due: March 07, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
string = input("Enter a string of lowercase letters: ")
print("")
decreasing_stop = False

for i in range(1, len(string)):
    if string[i] >= string[i - 1] and not decreasing_stop:
        decreasing_stop = i

if not decreasing_stop:
    print(string, "is decreasing.")
else:
    print(string, "is not decreasing.")
    print("It stopped being lexicographically decreasing at location", decreasing_stop)
