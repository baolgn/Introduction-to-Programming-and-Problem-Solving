"""
Author: Bao Nguyen
Assignment / Part: Lab 12 - Q2
Date: April 26
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


class VideoGameStore:
    def __init__(self, owner, games):
        self.owner = owner
        self.games = games

    def __str__(self):
        game_list = "\n".join([f"\t{title} by {company}" for title, company in self.games])
        return f"Welcome to {self.owner}'s Video Game Store!\nWe have the following titles available for you:\n{game_list}\n"

    def buy_game(self, game):
        if game in self.games:
            self.games.remove(game)
            print(f"Thank you for your purchase of {game[0]}!")
            return True
        else:
            print(f"Sorry, we do not have {game[0]}")
            return False

    def view_games(self):
        print("Available titles:")
        for title, _ in self.games:
            print(f"\t{title}")


def main():
    bobs_store = VideoGameStore("Bob", [("Overwatch", "Blizzard"), ("Super Meat Boy", "Team Meat"), ("Deltarune", "Toby Fox")])
    print(bobs_store)
    bobs_store.buy_game(("League of Legends", "Riot Games"))
    bobs_store.buy_game(("Overwatch", "Blizzard"))
    bobs_store.view_games()


main()
