"""
Author: Bao Nguyen
Assignment / Part: HW2 - Q2
Date Due: February 08, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
import math

frequency = float(input("Enter a value for the frequency: "))
duration = float(input("Enter a value for the duration of the sound wave, T: "))
amplitude_spectrum = float(2*math.sin(frequency * duration)/frequency)
print("\nThe amplitude spectrum of this Fourier transform is: ", round(amplitude_spectrum, 3))
