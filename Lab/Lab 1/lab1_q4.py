"""
Author: Bao Nguyen
Assignment / Part: Lab 1 - Q4
Date: February 02
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
days = int(input("How many days do you have? "))
hrs = int(input("How many hours do you have? "))
mins = int(input("How many minutes do you have? "))
secs = int(input("How many seconds do you have? "))
days_to_secs = days * 24 * 60 * 60
hrs_to_secs = hrs * 60 * 60
mins_to_secs = mins * 60
print(days, "Days", hrs, "Hours", mins, "Minutes and", secs, "Seconds result in a total of",
      days_to_secs + hrs_to_secs + mins_to_secs + secs, "seconds")
