"""
Author: Bao Nguyen
Assignment / Part: HW1 - Q3
Date Due: February 01, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
print("Enter number of coins:")
quarters = int(input("Number of quarters: "))
dimes = int(input("Number of dimes: "))
nickels = int(input("Number of nickels: "))
pennies = int(input("Number of pennies: "))
DOLLARS = int((quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01) // 1)
CENTS = int((quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01) * 100 % 100)
print("The total is", DOLLARS, "dollar(s) and", CENTS, "cent(s)")
