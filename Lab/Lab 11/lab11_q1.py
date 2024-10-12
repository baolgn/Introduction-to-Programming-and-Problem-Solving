"""
Author: Bao Nguyen
Assignment / Part: Lab 11 - Q1
Date: April 19
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

powers_of_two = [2 ** i for i in range(8)]
print(powers_of_two)

even_numbers = [num * 2 for num in range(5)]
print(even_numbers)

squares_dict = {num: num ** 2 for num in range(0, 13, 4)}
print("{", end="")
for i, (key, value) in enumerate(squares_dict.items()):
    if i == 0:
        print(f"{key}: {value},", end=" ")
    else:
        print(f"\n{key}: {value}", end="")
print("}")


multiples_dict = {num: [num * i for i in range(1, 5)] for num in range(4, 9)}
print("{", end="")
for i, (key, value) in enumerate(multiples_dict.items()):
    if i == 0:
        print(f"{key}: {value},", end=" ")
    else:
        print(f"\n{key}: {value}", end="")
print("}")