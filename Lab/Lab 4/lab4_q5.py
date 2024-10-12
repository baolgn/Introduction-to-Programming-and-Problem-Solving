"""
Author: Bao Nguyen
Assignment / Part: Lab 4 - Q5
Date: February 23
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
message_width = int(input("Python needs to tell you a secret. How many characters wide can its message be? "))

if message_width < 3 or message_width % 2 == 0:
    message_width = int(input("Please enter a width that is at least 3 characters wide and an odd number. "))

for row in range(message_width):
    ans = ""
    for column in range(message_width):
        if row == column:
            ans += "X"

        elif row + column == message_width - 1:
            ans += "X"

        else:
            ans += " "

    print(ans)

for row in range(message_width):
    current_row = ""
    for column in range(message_width):
        if row == 0 or row == message_width - 1:
            if column != 0 and column != message_width - 1:
                current_row += "0"

            else:
                current_row += " "

        elif column == 0 or column == message_width - 1:
            current_row += "0"

        else:
            current_row += " "

    print(current_row)

for row in range(message_width):
    ans = ""
    for column in range(message_width):
        if row == column:
            ans += "X"

        elif row + column == message_width - 1:
            ans += "X"

        else:
            ans += " "

    print(ans)

for row in range(message_width):
    current_row = ""
    for column in range(message_width):
        if row == 0 or row == message_width - 1:
            if column != 0 and column != message_width - 1:
                current_row += "0"

            else:
                current_row += " "

        elif column == 0 or column == message_width - 1:
            current_row += "0"

        else:
            current_row += " "

    print(current_row)

print("- From Python")
