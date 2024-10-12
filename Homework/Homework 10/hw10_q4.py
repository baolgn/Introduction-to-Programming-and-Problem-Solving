"""
Author: Bao Nguyen
Assignment / Part: HW10 - Q4
Date Due: April 18, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []

    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))

    return merged


print(merge_intervals([(1, 3), (2, 6), (8, 10), (15, 18)]))
print(merge_intervals([(1, 4), (4, 5)]))
