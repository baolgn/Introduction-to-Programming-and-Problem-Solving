"""
Author: Bao Nguyen
Assignment / Part: Lab 2 - Q6
Date: February 09
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

venomous = input("Is the snake venomous? ")
small = input("Is the snake small? ")
aggressive = input("Is the snake aggressive? ")

if venomous == "yes":
    if small == "yes":
        if aggressive == "yes":
            snake = "Matlab Mamba"
            fun_fact = ("Commonly used to introduce mech-ies to working with snakes. They often hatch plots to catch "
                        "their prey and enjoy graphical images.")
        else:
            snake = "Verilog Viper"
            fun_fact = ("Many people first see these snakes around architectures. Reports claim that they like to chew "
                        "on circuit wires.")
    else:
        if aggressive == "yes":
            snake = "C++ Cobra"
            fun_fact = ("Evolved from the C Serpents many years ago. Reports show they have the weird habit of "
                        "pointing at objects with their tails.")
        else:
            snake = "C Serpent"
            fun_fact = ("Can be found in the sea. Has the ability to control their memory, being able to allocate "
                        "parts of their brain for certain tasks and permanently delete information from their "
                        "memories.")
else:
    if small == "yes":
        if aggressive == "yes":
            snake = "Javascript Treesnake"
            fun_fact = ("Despite its name, they are completely different from the Java Kingsnake. They like to lay on "
                        "the nodes of a tree to browse through nearby animals for their next meal.")
        else:
            snake = "Java Kingsnake"
            fun_fact = ("Very befitting of their name, they are objectively the most sophisticated snake species. One "
                        "may even say they are very classy.")
    else:
        if aggressive == "yes":
            snake = "Assembly Anaconda"
            fun_fact = ("Many people hate learning about these snakes, as they look very intimidating. In the Totally "
                        "Official CS1114 Snake Register, they are said to love being in low level altitudes.")
        else:
            snake = "Python Python"
            fun_fact = ("One of the largest and most famous snakes. However, they are pretty slow, and are commonly "
                        "used to introduce people to learning about snakes.")

print("That is a", snake, end=". ")
print(fun_fact)
