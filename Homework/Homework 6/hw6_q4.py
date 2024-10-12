"""
Author: Bao Nguyen
Assignment / Part: HW6 - Q4
Date Due: March 07, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
encoded_string = input("Enter an encoded string: ")
key = int(input("Enter a key: "))

decoded_message = ""

for i in range(len(encoded_string) - 1, -1, -(key + 1)):
    if not encoded_string[i].isdigit():
        decoded_message += encoded_string[i]

print("Your message is:", decoded_message)
