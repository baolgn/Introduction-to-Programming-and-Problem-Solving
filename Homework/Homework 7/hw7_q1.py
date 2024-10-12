"""
Author: Bao Nguyen
Assignment / Part: HW7 - Q1
Date Due: March 14, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def calculate_grade(assignments_score, midterm_score, final_score):
    weighted_grade = (assignments_score * 0.4) + (midterm_score * 0.3) + (final_score * 0.3)
    return weighted_grade


def get_valid_score(assignment_type):
    while True:
        score_str = input("Enter a score for " + assignment_type + ": ")
        if score_str.isdigit() or (score_str[0] == '-' and score_str[1:].isdigit()):
            score = float(score_str)
            if 0 <= score <= 100:
                return score
        print("Invalid, Enter a numeric value between 0 and 100.")


def display_result(grade):
    print("\nGrade: ", round(grade, 2), ".", sep="", end=" ")
    if grade >= 90:
        print("Outstanding performance")
    elif grade >= 80:
        print("Good work")
    elif grade >= 70:
        print("Can improve")
    elif grade >= 60:
        print("Passed")
    else:
        print("Failed")


def main():
    assignments_score = get_valid_score("Assignments")
    midterm_score = get_valid_score("Midterm")
    final_score = get_valid_score("Final")
    calculated_grade = calculate_grade(assignments_score, midterm_score, final_score)
    display_result(calculated_grade)


main()
