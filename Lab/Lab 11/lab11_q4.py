"""
Author: Bao Nguyen
Assignment / Part: Lab 11 - Q4
Date: April 19
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def create_grocery_inventory():
    inventory = {}
    while True:
        user_input = input("Please enter the item and quantity you own separated by a comma or DONE when complete: ")
        if user_input.lower() == 'done':
            break
        item_name, item_amount = user_input.split(',')
        item_name = item_name.strip()
        item_amount = int(item_amount.strip())
        if item_name in inventory:
            inventory[item_name] += item_amount
        else:
            inventory[item_name] = item_amount
    return inventory


def create_grocery_shopping_list(fridge_inventory):
    shopping_list = {}
    while True:
        user_input = input("Please enter the item and quantity you desire separated by a comma or DONE when complete: ")
        if user_input.lower() == 'done':
            break
        item_name, item_desired_amount = user_input.split(',')
        item_name = item_name.strip()
        item_desired_amount = int(item_desired_amount.strip())
        if item_name in fridge_inventory:
            current_amount = fridge_inventory[item_name]
            amount_to_buy = max(0, item_desired_amount - current_amount)
            shopping_list[item_name] = amount_to_buy
        else:
            shopping_list[item_name] = item_desired_amount
    return shopping_list


def main():
    fridge_inventory = create_grocery_inventory()
    print()
    grocery_list = create_grocery_shopping_list(fridge_inventory)
    print()
    print("Your shopping list, based off of what you have in your fridge, should be:")
    print(grocery_list)


main()
