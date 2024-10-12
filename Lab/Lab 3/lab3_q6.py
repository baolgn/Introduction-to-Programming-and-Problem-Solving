"""
Author: Bao Nguyen
Assignment / Part: Lab 3 - Q6
Date: February 16
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
import random

print("Welcome to Blackjack!")

dealer_sum = random.randint(2, 21)

player_sum = random.randint(1, 11)
print("Your current card sum is:", player_sum)

while True:
    action = input("What would you like to do next: (DEAL, STAND) ")

    if action == "DEAL":
        card_value = random.randint(1, 11)
        player_sum += card_value
        print("Your current card sum is:", player_sum)
        if player_sum > 21:
            print("You lost! Your card sum was", player_sum, "and the dealer's was", dealer_sum)
            break

    elif action == "STAND":
        if player_sum > dealer_sum or dealer_sum > 21:
            print("You won! Your card sum was", player_sum, "and the dealer's was", dealer_sum)
        elif player_sum == dealer_sum:
            print("It's a tie! Your card sum was", player_sum, "and the dealer's was", dealer_sum)
        else:
            print("You lost! Your card sum was", player_sum, "and the dealer's was", dealer_sum)
        break

    else:
        print("ERROR: Please either DEAL or STAND.")
