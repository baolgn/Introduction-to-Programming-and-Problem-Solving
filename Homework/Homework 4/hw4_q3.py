"""
Author: Bao Nguyen
Assignment / Part: HW4 - Q3
Date Due: February 22, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
days = int(input("Enter the number of days (1 to 100): "))

while days < 1 or days > 100:
    days = int(input("Enter a valid number of days (1 to 100): "))

total_steps = 0
for i in range(1, days + 1):
    total_steps += i * 2 - 1

print("The baby will have taken a total of", total_steps, "steps after", days, "days.")
