"""
Author: Bao Nguyen
Assignment / Part: HW3 - Q2
Date Due: February 15, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
day = input("Enter the day the call started at: ")
time = int(input("Enter the time the call started at (hhmm): "))
duration = int(input("Enter the duration of the call (in minutes): "))

if time < 0 or time > 2359:
    print("\nERROR: Please enter a valid time in military time (hhmm).")
else:
    if day == "Fri" or day == "Sat" or day == "Sun":
        total_cost = 0.10 * duration
        print("\nThis call will cost $", round(total_cost, 2), sep="")
    elif day == "Mon" or day == "Tue" or day == "Wed" or day == "Thr":
        if 530 <= time <= 2100:
            total_cost = 0.55 * duration
            print("\nThis call will cost $", round(total_cost, 2), sep="")
        else:
            total_cost = 0.35 * duration
            print("\nThis call will cost $", round(total_cost, 2), sep="")
    else:
        print("\nERROR: Please enter a valid day of the week (Mon, Tue, Wed, Thr, Fri, Sat, Sun).")
