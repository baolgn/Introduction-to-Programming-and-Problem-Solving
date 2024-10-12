"""
Author: Bao Nguyen
Assignment / Part: HW9 - Q1
Date Due: April 11, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def update_frequencies(old_frequencies, new_sequence):
    nucleotides = ["A", "C", "T", "G"]
    new_frequencies = [(nucleotides[i], old_frequencies[i][1]) for i in range(len(nucleotides))]
    nucleotide_additions = [0, 0, 0, 0]

    for nucleotide in new_sequence:
        index = nucleotides.index(nucleotide)
        new_frequencies[index] = (nucleotide, new_frequencies[index][1] + 1)
        nucleotide_additions[index] += 1

    print("Number of nucleotides added:", end=" ")
    for i in range(len(nucleotides)):
        if nucleotide_additions[i] != 0:
            if i > 0:
                print("|", nucleotides[i], "->", nucleotide_additions[i], end=" ")
            else:
                print(nucleotides[i], "->", nucleotide_additions[i], end=" ")
    print()

    return new_frequencies


def main():
    old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
    new_sequence = "ACCCGTTA"
    new_frequencies = update_frequencies(old_frequencies, new_sequence)
    print(new_frequencies)


main()
