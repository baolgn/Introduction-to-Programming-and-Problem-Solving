"""
Author: Bao Nguyen
Assignment / Part: HW4 - Q1
Date Due: February 22, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
MOCHIKO_CUPS_PER_BATCH = 3
SUGAR_CUPS_PER_BATCH = 1.5
CORNSTARCH_CUPS_PER_BATCH = 2
ANKO_CUPS_PER_BATCH = 1

mochiko_grams = float(input("Enter an amount (g) of mochiko: "))
sugar_grams = float(input("Enter an amount (g) of sugar: "))
cornstarch_grams = float(input("Enter an amount (g) of cornstarch: "))
anko_grams = float(input("Enter an amount (g) of anko: "))

mochiko_cups = mochiko_grams / 220
sugar_cups = sugar_grams / 220
cornstarch_cups = cornstarch_grams / 220
anko_cups = anko_grams / 220

batches_possible = mochiko_cups // MOCHIKO_CUPS_PER_BATCH
if sugar_cups // SUGAR_CUPS_PER_BATCH < batches_possible:
    batches_possible = sugar_cups // SUGAR_CUPS_PER_BATCH
if cornstarch_cups // CORNSTARCH_CUPS_PER_BATCH < batches_possible:
    batches_possible = cornstarch_cups // CORNSTARCH_CUPS_PER_BATCH
if anko_cups // ANKO_CUPS_PER_BATCH < batches_possible:
    batches_possible = anko_cups // ANKO_CUPS_PER_BATCH

if mochiko_cups < MOCHIKO_CUPS_PER_BATCH:
    print("Please enter an amount of mochiko greater than 660g!")
elif sugar_cups < SUGAR_CUPS_PER_BATCH:
    print("Please enter an amount of sugar greater than 330g!")
elif cornstarch_cups < CORNSTARCH_CUPS_PER_BATCH:
    print("Please enter an amount of cornstarch greater than 440g!")
elif anko_cups < ANKO_CUPS_PER_BATCH:
    print("Please enter an amount of anko greater than 220g!")
else:
    print("With this amount of ingredients, you can make", int(batches_possible), "batch(es) of 24 mochi.")
