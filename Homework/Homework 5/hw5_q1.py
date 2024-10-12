"""
Author: Bao Nguyen
Assignment / Part: HW5 - Q1
Date Due: February 29, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
program_finished = False

while not program_finished:
    initial_velocity_check_input = input("Enter the initial velocity (m/s) or type 'DONE' to quit: ")

    if initial_velocity_check_input == "DONE":
        print("Program ended")
        program_finished = True

    else:
        initial_velocity = float(initial_velocity_check_input)

        acceleration = float(input("Enter the acceleration (m/s^2): "))
        while acceleration <= 0:
            acceleration = float(input("Acceleration must be greater than 0. Enter a valid acceleration: "))

        distance = (initial_velocity ** 2)/(2 * acceleration)
        print("Distance traveled until stopped:", distance, "\n")
