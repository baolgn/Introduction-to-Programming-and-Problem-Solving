"""
Author: Bao Nguyen
Assignment / Part: HW11
Date Due: May 2, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

import random


class Instrument:
    def __init__(self, model, brand, strength):
        self.model = model
        self.brand = brand
        self.strength = strength

    def __str__(self):
        return f"{self.brand} {self.model} ({self.strength * 100:.1f} / 100 strength)"

    def break_test(self):
        return random.random() < self.strength


class Musician:
    def __init__(self, stage_name, instruments):
        self.stage_name = stage_name
        self.instruments = instruments
        self.number_of_instruments = len(instruments)

    def __str__(self):
        instrument_list = ", ".join(str(instrument) for instrument in self.instruments)
        return f"Musician object '{self.stage_name}', owning {instrument_list}"

    def pick_instrument(self, instrument_index=None):
        if not self.instruments:
            return None
        if instrument_index is None or instrument_index >= len(self.instruments):
            return random.choice(self.instruments)
        else:
            return self.instruments[min(instrument_index, len(self.instruments) - 1)]


def get_name_of_battle_winner(musician1, musician2):
    if not musician1.instruments and not musician2.instruments:
        return "NO CONTEST"
    elif not musician1.instruments:
        return musician2.stage_name
    elif not musician2.instruments:
        return musician1.stage_name

    instrument1 = random.choice(musician1.instruments)
    instrument2 = random.choice(musician2.instruments)

    print(f"{musician1.stage_name} picked a {instrument1}!")
    print(f"{musician2.stage_name} picked a {instrument2}!")

    if instrument1.strength == instrument2.strength:
        print("Both musicians' instruments are the same strength. The winner will be decided by the whim of chance.")
        return random.choice([musician1.stage_name, musician2.stage_name])
    elif instrument1.strength > instrument2.strength:
        breaking = instrument1.break_test()
        if breaking:
            print(f"{musician1.stage_name}'s {instrument1.model} broke!")
            return musician2.stage_name
        else:
            return musician1.stage_name
    else:
        breaking = instrument2.break_test()
        if breaking:
            print(f"{musician2.stage_name}'s {instrument2.model} broke!")
            return musician1.stage_name
        else:
            return musician2.stage_name


def main():
    danelectro = Instrument("Stock '59", "Danelectro", 0.25)
    fender_vi = Instrument("VI Bass", "Fender", 0.99)
    four_double_o_one = Instrument("4001C64 Bass", "Rickenbacker", 0.856)
    gear = [danelectro, fender_vi, four_double_o_one]

    sad_musician = Musician("Robert Smith", gear)
    less_sad_musician = Musician("Miki Berenyi", gear)

    num_duels = 10
    for duelCount in range(num_duels):
        winner_name = get_name_of_battle_winner(sad_musician, less_sad_musician)
        if duelCount == num_duels - 1:
            print(f"THE WINNER OF DUEL #{duelCount + 1} IS {winner_name}!")
        else:
            print(f"THE WINNER OF DUEL #{duelCount + 1} IS {winner_name}!\n")


main()
