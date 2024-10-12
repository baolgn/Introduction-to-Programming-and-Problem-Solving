"""
Author: Bao Nguyen
Assignment / Part: HW3 - Q5
Date Due: February 15, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
import random
import math

max_hp = float(input("Enter the max health of this Pokémon: "))
current_hp = random.uniform(1, max_hp)
ball_value = random.uniform(1, 255)
f_value = math.floor(((max_hp * 255 * 4)/(current_hp * ball_value)))
pseudorandom_value = random.uniform(0, 255)

if f_value >= pseudorandom_value:
    print("You've caught the Pokémon!")
else:
    print("Oh no! The Pokémon broke free!")
