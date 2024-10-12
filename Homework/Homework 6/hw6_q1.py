"""
Author: Bao Nguyen
Assignment / Part: HW6 - Q1
Date Due: March 07, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
suspect_initials = input("Enter the initials of the suspects: ")
candy_wrappers = input("Enter the candy wrappers: ")
print("")

suspect_found = False

for initial in suspect_initials:
    if initial in candy_wrappers:
        print(initial, "is a candy thief suspect")
        suspect_found = True

if not suspect_found:
    print("No candy thief found")
