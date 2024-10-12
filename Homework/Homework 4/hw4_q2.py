"""
Author: Bao Nguyen
Assignment / Part: HW4 - Q2
Date Due: February 22, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
num_players = int(input("How many players played this round? "))

while num_players <= 0:
    num_players = int(input("Invalid input. How many players played this round? "))

winner_value = 0
winning_player = 0

for player_index in range(1, num_players + 1):
    total_value = 0
    asset_value = input("Enter the value of a property/asset, or DONE to finish: ")

    while asset_value != 'DONE':
        total_value += float(asset_value)
        asset_value = input("Enter the value of a property/asset, or DONE to finish: ")

    if total_value > winner_value:
        winner_value = total_value
        winning_player = player_index

    print("Player", winning_player, "has", round(total_value, 2), "dollars.")

print("Congratulations, player", winning_player, end="! ")
print("You won with $", round(winner_value, 2), sep="", end="!")
