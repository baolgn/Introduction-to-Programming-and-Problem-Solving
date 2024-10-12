"""
Author: Bao Nguyen
Assignment / Part: HW10 - Q1
Date Due: April 18, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def group_students(club_specs, student_prefs):
    available_seats = {club: capacity for club, capacity in club_specs}
    assigned_students = {club: [] for club, _ in club_specs}

    for student, preferred_club in student_prefs:
        if available_seats[preferred_club] > 0:
            assigned_students[preferred_club].append(student)
            available_seats[preferred_club] -= 1

    return assigned_students


def main():
    club_specs = [("Chess Club", 15), ("Art Club", 20), ("Writing Club", 3)]
    student_prefs = [
        ("Alice", "Chess Club"),
        ("Bob", "Chess Club"),
        ("Flora", "Writing Club"),
        ("Charlie", "Art Club"),
        ("David", "Writing Club"),
        ("Melody", "Writing Club"),
        ("Ana", "Writing Club")
    ]

    assigned_students = group_students(club_specs, student_prefs)

    print("[")
    for club, students in assigned_students.items():
        print(f"{students}")
    print("]")


main()
