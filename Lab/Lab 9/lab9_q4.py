"""
Author: Bao Nguyen
Assignment / Part: Lab 9 - Q4
Date: April 5
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

import random


def shuffle_create(input_list):
    shuffled_list = []
    while input_list:
        index = random.randint(0, len(input_list) - 1)
        shuffled_list.append(input_list.pop(index))
    return shuffled_list


def shuffle_in_place(input_list):
    for i in range(len(input_list) - 1, 0, -1):
        j = random.randint(0, i)
        input_list[i], input_list[j] = input_list[j], input_list[i]


def main():
    list_one = ["Jean Valjean", "Javert", "Fantine", "Cosette", "Marius Pontmercy", "Eponine", "Enjolras"]
    print("ORIGINAL LIST_ONE: {}".format(list_one))

    # First function execution
    print("LIST CREATED BY SHUFFLE_CREATE: {}\n".format(shuffle_create(list_one)))

    list_two = ["A", 0, 0, 5, 1, 3, 2]
    print("ORIGINAL LIST_TWO: {}".format(list_two))

    # Second function execution
    shuffle_in_place(list_two)
    print("LIST_TWO AFTER SHUFFLE_IN_PLACE: {}".format(list_two))


main()
