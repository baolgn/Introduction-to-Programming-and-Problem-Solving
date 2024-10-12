"""
Author: Bao Nguyen
Assignment / Part: Lab 5 - Q4
Date: March 1
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
hamming_distance = 0

for i in range(len(string1)):
    if string1[i] != string2[i]:
        hamming_distance += 1

print("\"", string1, "\"", " and ", "\"", string2, "\"", sep="", end=" ")
print("Hamming distance is", hamming_distance)
