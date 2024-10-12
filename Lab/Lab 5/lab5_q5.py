"""
Author: Bao Nguyen
Assignment / Part: Lab 5 - Q5
Date: March 1
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
phrase = input("Enter a phrase: ")
modified_phrase = ""
start = 0
end = 0

for i in range(len(phrase)):
    char = phrase[i]
    if char == " " or i == len(phrase) - 1:
        word = phrase[start:end + 1] if i == len(phrase) - 1 else phrase[start:end]

        if not word.isdigit():
            modified_phrase += word
        else:
            modified_phrase += "X" * len(word)

        if i != len(phrase) - 1:
            modified_phrase += " "

        start = i + 1
        end = i
    else:
        end = i + 1

print(modified_phrase)
