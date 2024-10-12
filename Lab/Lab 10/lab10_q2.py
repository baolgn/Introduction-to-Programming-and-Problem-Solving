"""
Author: Bao Nguyen
Assignment / Part: Lab 10 - Q2
Date: April 12
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def print_keys(my_dict):
    print("Keys:")
    for key in my_dict.keys():
        print(key)


def print_values(my_dict):
    print("\nValues:")
    for value in my_dict.values():
        print(value)


def print_key_value_pairs(my_dict):
    print("\nKey, Value pairs:")
    for key, value in my_dict.items():
        print(key, ", ", value, sep="")


def print_sorted_key_value_pairs(my_dict):
    print("\nKey, Value pairs in order by key:")
    sorted_items = sorted(my_dict.items())
    for key, value in sorted_items:
        print(key, ", ", value, sep="")


def main():
    my_dict = {"a": 15, "c": 35, "b": 20}
    print_keys(my_dict)
    print_values(my_dict)
    print_key_value_pairs(my_dict)
    print_sorted_key_value_pairs(my_dict)


main()
