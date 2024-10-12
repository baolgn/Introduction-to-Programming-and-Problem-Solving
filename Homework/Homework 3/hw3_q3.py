"""
Author: Bao Nguyen
Assignment / Part: HW3 - Q3
Date Due: February 15, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
current_xp = float(input("Enter this user's current XP: "))

if current_xp > 60:
    level = "ERROR"
elif current_xp >= 40:
    level = 5
elif current_xp >= 30:
    level = 4
elif current_xp >= 25:
    level = 3
elif current_xp >= 15:
    level = 2
else:
    level = 1

if level == "ERROR":
    print("ERROR: Please enter a valid XP value.")
else:
    print("Level", level, end=" ")
    print("Player (XP: ", current_xp, ")", sep="")
