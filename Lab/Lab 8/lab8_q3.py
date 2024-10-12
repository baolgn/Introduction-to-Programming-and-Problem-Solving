"""
Author: Bao Nguyen
Assignment / Part: Lab 8 - Q3
Date: March 29
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def decode_part(message, start, end, step):
    decoded = ""
    for i in range(start, end, step):
        decoded += message[i]
    return decoded


def decode_entire_msg(message):
    decoded_message = ""
    count = 0

    start = 1
    step = int(message[0])
    i = 1

    while count < 100:
        if message[i].isdigit():
            decoded = decode_part(message, start, i, step)
            decoded_message += decoded
            start = i + 1
            step = int(message[i])
        elif message[i].isalpha():
            count += 1
        i += 1
    return decoded_message


def decode_roman_file(roman_file, decoded_file):
    try:
        with open(roman_file, 'r') as file:
            message = file.read().strip()
            decoded_message = decode_entire_msg(message)
            with open(decoded_file, 'w') as decoded:
                decoded.write(decoded_message)
    except FileNotFoundError:
        print(f"The file '{roman_file}' does not exist.")


def main():
    ROMAN_FILE = "roman_code_msg.txt"
    ROMAN_DECODED_FILE = "secret_msg.txt"
    decode_roman_file(ROMAN_FILE, ROMAN_DECODED_FILE)


if __name__ == "__main__":
    main()
