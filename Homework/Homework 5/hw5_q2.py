"""
Author: Bao Nguyen
Assignment / Part: HW5 - Q2
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
        gravitational_acceleration = 9.81

        initial_velocity = float(initial_velocity_check_input)
        while initial_velocity <= 0:
            initial_velocity = float(input("Velocity must be greater than 0. Enter a valid velocity: "))

        max_height = (initial_velocity ** 2)/(2 * gravitational_acceleration)
        time = initial_velocity/gravitational_acceleration

        print("For initial velocity =", initial_velocity, "m/s:")
        print("Max height reached:", round(max_height, 2), "meters")
        print("Time to reach max height:", round(time, 2), "seconds\n")
