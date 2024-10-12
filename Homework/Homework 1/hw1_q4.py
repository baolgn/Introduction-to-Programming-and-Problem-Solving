"""
Author: Bao Nguyen
Assignment / Part: HW1 - Q4
Date Due: February 01, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
dollars = int(input("Enter amount of dollars: "))
cents = int(input("Enter amount of cents: "))
total_cents = float(dollars*100+cents)
quarters = int(total_cents // 25)
dimes = int((total_cents % 25) // 10)
nickels = int(((total_cents % 25) % 10) // 5)
pennies = int((((total_cents % 25) % 10) % 5))
print(dollars, "dollars and", cents, "cents are:")
print(quarters, "quarters,", dimes, "dimes,", nickels, "nickels, and", pennies, "pennies")
