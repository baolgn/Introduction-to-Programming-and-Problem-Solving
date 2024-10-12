"""
Author: Bao Nguyen
Assignment / Part: Lab 5 - Q3
Date: March 1
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
user_message = input("Please enter your message: ")
consonant_amount = 0
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

for char in user_message:
    if char in consonants:
        consonant_amount += 1

print("Total number of consonants:", consonant_amount)
