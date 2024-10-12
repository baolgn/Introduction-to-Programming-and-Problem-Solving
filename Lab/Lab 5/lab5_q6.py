"""
Author: Bao Nguyen
Assignment / Part: Lab 5 - Q6
Date: March 1
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
message = input("Please enter your message: ")
secret_message = ""
include_word = True
start = 0

for i in range(len(message)):
    char = message[i]
    if char == " " or i == len(message) - 1:
        word = message[start:i + 1] if i == len(message) - 1 else message[start:i]

        if word[0].isupper():
            for char in word[1:]:
                if char.isupper():
                    include_word = False

            if include_word:
                secret_message += word[0]

        include_word = True
        start = i + 1

print("Your secret message is:", secret_message)
