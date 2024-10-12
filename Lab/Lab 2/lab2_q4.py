"""
Author: Bao Nguyen
Assignment / Part: Lab 2 - Q4
Date: February 09
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

highest = float(input("Enter your highest exam grade: "))
second_highest = float(input("Enter your second highest exam grade: "))
third_highest = float(input("Enter your third highest exam grade: "))
average_hw = float(input("Enter your average homework grade: "))
average_lab = float(input("Enter your average lab grade: "))

weighted_highest = highest * 0.25
weighted_second_highest = second_highest * 0.20
weighted_third_highest = third_highest * 0.15
weight_average_hw = average_hw * 0.2
weight_average_lab = average_lab * 0.2

total_weighted = (weighted_highest + weighted_second_highest + weighted_third_highest + weight_average_hw
                  + weight_average_lab)

if total_weighted > 92:
    grade = "A"
elif total_weighted >= 90:
    grade = "A-"
elif total_weighted >= 87:
    grade = "B+"
elif total_weighted >= 83:
    grade = "B"
elif total_weighted >= 80:
    grade = "B-"
elif total_weighted >= 77:
    grade = "C+"
elif total_weighted >= 73:
    grade = "C"
elif total_weighted >= 70:
    grade = "C-"
elif total_weighted >= 67:
    grade = "D+"
elif total_weighted >= 60:
    grade = "D-"
else:
    grade = "F"

print("Your final grade is", grade)
