"""
Author: Bao Nguyen
Assignment / Part: HW2 - Q1
Date Due: February 08, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
guests = int(input("Enter the number of guests: "))
slices_per = int(input("Enter the number of pizza slices each guest will eat: "))
slices_total = int(guests*slices_per)

if slices_total % 8 == 0:
    large_pizzas = int(slices_total // 8)
    slices_remain = 0
else:
    large_pizzas = int(slices_total // 8 + 1)
    slices_remain = int(8 - slices_total % 8)

print("\nMinimum of whole large pizza required:", large_pizzas)
print("Total number of large pizza slices needed:", slices_total)
print("Number of large pizza slices left over:", slices_remain)