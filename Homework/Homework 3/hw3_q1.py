"""
Author: Bao Nguyen
Assignment / Part: HW3 - Q1
Date Due: February 15, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
season = input("Enter the current season (summer/other): ")
small_cups = int(input("Enter the number of small cups of lemonade sold: "))
medium_cups = int(input("Enter the number of medium cups of lemonade sold: "))
large_cups = int(input("Enter the number of large cups of lemonade sold: "))

small_price = 2.00
medium_price = 2.50
large_price = 3.00
small_cost = 1.00
medium_cost = 1.25
large_cost = 1.50

if season == "summer":
    total_profit = (small_cups * (small_price - small_cost) + medium_cups * (medium_price - medium_cost) + large_cups *
                    (large_price - large_cost))
    print("Total profit for the day in the summer", end=": ")
    print("$", round(total_profit, 2), sep="")
elif season == "other":
    small_price -= 0.50
    medium_price -= 0.50
    large_price -= 0.50
    small_cost -= 0.25
    medium_cost -= 0.25
    large_cost -= 0.25
    total_profit = (small_cups * (small_price - small_cost) + medium_cups * (medium_price - medium_cost) + large_cups *
                    (large_price - large_cost))
    print("Total profit for the day in the summer", end=": ")
    print("$", round(total_profit, 2), sep="")
else:
    print("ERROR: Please enter either \"summer\" or \"other\" for the season.")
