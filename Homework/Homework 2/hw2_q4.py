"""
Author: Bao Nguyen
Assignment / Part: HW2 - Q4
Date Due: February 08, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
Ting_days = int(input("Enter the number of days Ting has worked: "))
Ting_hours = int(input("Enter the number of hours Ting has worked: "))
Ting_minutes = int(input("Enter the number of minutes Ting has worked: "))
Justin_days = int(input("Enter the number of days Justin has worked: "))
Justin_hours = int(input("Enter the number of hours Justin has worked: "))
Justin_minutes = int(input("Enter the number of minutes Justin has worked: "))

print("\nThe total time both CAs worked together is:", Ting_days + Justin_days, "days,", Ting_hours + Justin_hours,
      "hours and", Ting_minutes + Justin_minutes, "minutes")
