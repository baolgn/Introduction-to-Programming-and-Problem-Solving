"""
Author: Bao Nguyen
Assignment / Part: HW9 - Q2, Q3
Date Due: April 11, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def count_syllables(line_number):
    return len(line_number.split(','))


def is_haiku(input_string):
    lines = input_string.split('/')

    if len(lines) != 3:
        print("WARNING: The haiku should contain 3 lines.")
        return False

    syllable_counts = [5, 7, 5]
    for i, line_number in enumerate(lines):
        if count_syllables(line_number) != syllable_counts[i]:
            line_word = "first" if i == 0 else "second" if i == 1 else "third"
            print("WARNING: The", line_word, "line is not", syllable_counts[i], "syllables long.")
            return False

    return True


def haiku_string_parser(input_string):
    if is_haiku(input_string):
        lines = input_string.split('/')
        formatted_haiku = "\n".join(line_number.replace(' ,', ' ').replace(',', '') for line_number in lines)
        return formatted_haiku
    else:
        return ""


def main():
    haiku_string = "clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding, ha,bit/ga,zing ,at ,the ,moon"
    formatted_haiku = haiku_string_parser(haiku_string)
    print(formatted_haiku)


main()
