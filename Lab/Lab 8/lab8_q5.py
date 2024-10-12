"""
Author: Bao Nguyen
Assignment / Part: Lab 8 - Q5
Date: March 29
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def remove_Es(msg):
    return msg.replace('E', '').replace('e', '')


def remove_Es_new_file(filename):
    try:
        with open(filename, 'r') as file:
            original_content = file.read()
            cleaned_content = remove_Es(original_content)
            new_filename = "cleaned_" + filename
            with open(new_filename, 'w') as new_file:
                new_file.write(cleaned_content)
            return True
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
        return False

def remove_Es_same_file(filename):
    try:
        with open(filename, 'r+') as file:
            original_content = file.read()
            cleaned_content = remove_Es(original_content)
            file.seek(0)
            file.write(cleaned_content)
            return True
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
        return False


def main():
    EVIL_ES_MSG = "evil_es_msg.txt"
    EVIL_ES_COPY = "evil_es_copy.txt"
    remove_Es_new_file(EVIL_ES_MSG)
    remove_Es_same_file(EVIL_ES_COPY)
    if remove_Es_new_file(EVIL_ES_MSG):
        print(f"Successfully created cleaned file based on '{EVIL_ES_MSG}'.")
    else:
        print("Operation unsuccessful.")


main()
