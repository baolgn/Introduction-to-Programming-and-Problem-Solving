"""
Author: Bao Nguyen
Assignment / Part: Lab 11 - Q5
Date: April 19
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def is_valid_phone_number(number):
    return len(number) == 10 and number.isdigit()


def add_entry(contacts, name, number):
    if name in contacts:
        print("Error: Contact already exists.")
        return
    if not is_valid_phone_number(number):
        print("Error: Invalid phone number. Phone number must have 10 digits.")
        return
    contacts[name] = number


def lookup(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return f"{name} is not in the contact list."


def delete_entry(contacts, name):
    if name in contacts:
        del contacts[name]
    else:
        print(f"Error: {name} not found in contacts.")


def print_all(contacts):
    for name, number in contacts.items():
        print(f"{name}\t{number}")


def main():
    contacts = {}
    option = ""
    while option != 'Q':
        option = input("Please enter an option: ").upper()
        if option == 'A':
            name = input("Please enter a name: ")
            number = input("Please enter a phone number: ")
            add_entry(contacts, name, number)
        elif option == 'L':
            name = input("Please enter a name: ")
            print(lookup(contacts, name))
        elif option == 'P':
            print_all(contacts)
        elif option == 'D':
            name = input("Please enter a name: ")
            delete_entry(contacts, name)
        elif option != 'Q':
            print("Error: Invalid option.")


main()
