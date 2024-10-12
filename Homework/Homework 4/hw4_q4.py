"""
Author: Bao Nguyen
Assignment / Part: HW4 - Q4
Date Due: February 22, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
import random

play = input("Would you like to play 'Twenty-One'? [y/n] ")
player_score = 0
opponent_score = 0

if play == "n" or play == "no":
    print("Thank you for playing!")

elif play != "y" and play != "yes":
    print("ERROR: Invalid input.")

while play != "n" and play != "no":
    if play == "y" or play == "yes":
        card_1 = random.randint(1, 12)
        card_2 = random.randint(1, 12)
        print("Your cards are worth", card_1, "and", card_2, end=".")

        player_score = card_1 + card_2
        opponent_score = random.randint(0, 101)
        while opponent_score < 3 or opponent_score > 33:
            opponent_score = random.randint(0, 101)

        if player_score == 21:
            print("\nYour score is", player_score, end="!")
            print("\nYour opponent's score is", opponent_score, end="!")
            if opponent_score == 21:
                print("\nIt's a draw!")
            else:
                print("\nYou win! Your score was", player_score, end=".")

        elif opponent_score == 21:
            print("\nYour score is", player_score, end="!")
            print("\nYour opponent's score is", opponent_score, end="!")
            if opponent_score == 21:
                print("\nIt's a draw!")
            else:
                print("\nYour opponent wins! Their score was", opponent_score, end=".")

        else:
            draw_card = ""

            while draw_card != "n" and draw_card != "no":
                draw_card = input("\nWould you like another card? [y/n] ")

                if draw_card == "y" or draw_card == "yes":
                    additional_card = random.randint(1, 12)
                    player_score += additional_card
                    print("Your score is", player_score, end="!")
                    print("\nYour opponent's score is", opponent_score, end="!")
                    if player_score > 21:
                        if opponent_score > 21:
                            print("\nIt's a draw!")
                            play = "n"
                        else:
                            print("\nYour opponent wins! Their score was", opponent_score, end=".")
                            play = "n"

                elif draw_card == "n" or draw_card == "no":
                    print("Your score is", player_score, end="!")
                    print("\nYour opponent's score is", opponent_score, end="!")

                    if player_score > opponent_score:
                        if player_score > 21:
                            if opponent_score <= 21:
                                print("\nYour opponent wins! Their score was", opponent_score, end=".")
                                play = "n"
                            else:
                                print("\nIt's a draw!")
                                play = "n"
                        else:
                            print("\nYou win! Your score was", player_score, end=".")
                            play = "n"

                    elif opponent_score > player_score:
                        if opponent_score > 21:
                            if player_score <= 21:
                                print("\nYou win! Your score was", player_score, end=".")
                                play = "n"
                            else:
                                print("\nIt's a draw!")
                                play = "n"
                        else:
                            print("\nYour opponent wins! Their score was", opponent_score, end=".")
                            play = "n"

                    else:
                        print("\nIt's a draw!")
                        play = "n"

                else:
                    print("ERROR: Invalid input.")
