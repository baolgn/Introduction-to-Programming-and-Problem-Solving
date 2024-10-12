"""
Author: Bao Nguyen
Assignment / Part: Lab 10 - Q4
Date: April 12
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""


def merge_databases(skyward_database, formulaic_database):
    merged_database = skyward_database.copy()
    highest_id = max(merged_database.keys())

    for empty_id, details in formulaic_database.items():

        if empty_id in merged_database:
            new_id = highest_id + 1
            print(f"{details[0]} had their employee ID changed from {empty_id} to {new_id}")
            merged_database[new_id] = details
            highest_id = new_id

        else:
            merged_database[empty_id] = details
            if empty_id > highest_id:
                highest_id = empty_id

    return merged_database


def main():
    skyward_database = {100: ["Alice", "Manager", "HR"], 101: ["Arnold", "Team Lead", "IT"], 102: ["Chris", "Developer", "IT"]}
    formulaic_database = {101: ["Lucas", "Developer", "IT"], 102: ["Anna", "Intern", "Marketing"], 103: ["Muhammad", "Research Analyst", "Marketing"]}
    merged_database = merge_databases(skyward_database, formulaic_database)
    print("Merged Database", merged_database)


main()
