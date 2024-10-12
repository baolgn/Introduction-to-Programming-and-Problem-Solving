"""
Author: Bao Nguyen
Assignment / Part: Lab 7 - Q3
Date: March 15
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


def main():
    message = "3Gn.olwo pd/Q gh5l!d pulAk c_kosk an2 moPn! .y\\oausr? 3mqei,sd+ktcbe.KrkcmOpsne!se odYpqo>kulq fag pozrtks dftpqh /ipaslk!dp4vm fkofwolp9 mjcnre"
    print(decode_entire_msg(message))


if __name__ == "__main__":
    main()
