from act1_9 import *
from if_else import *

print("\tProjects Compiler")
print(">>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<")

con = True

list_projects = []

name = input("Please enter your name: ")
print(f"\nHello, {name}! Welcome to my compiler.")
print("--> Here you can explore the topics and activities I have learned and done throughout the semester.")

while con == True:
    print("\nSelect a topic below: \n1. Variables and Data Types\n2. Functions and String\n3. Operators\n4. If-Elif-Else Statements\n5. Loops\n6. Lists\n7. Code Challenges\n8. Exit Compiler")
    user_input = input("Enter your choice (1-7): ")

    if user_input == "1":
        print("``````````````````````````````````````````")
        print("--> Selected Topic: Variables and Data Types")
        print("Available Activities: \na. Activity 2")
        activity = input("Select an activity (a): ")
        if activity.lower() == "a":
            act2()
            continue
        else:
            print("Invalid activity selection.")
            continue
        continue
    elif user_input == "2":
        print("``````````````````````````````````````````")
        print("--> Selected Topic: Functions and String")
        print("Available Activities: \na. Activity 1\nb. Activity 3\nc. Activity 4\nd. Activity 5\ne. Activity 15")
        activity1 = input("Select an activity (a-e): ")
        if activity1.lower() == 'a':
            act1()
            continue
        elif activity1.lower() == 'b':
            act3()
            continue
        elif activity1.lower() == 'c':
            act4()
            continue
        elif activity1.lower() == 'd':
            act5()
            continue
        elif activity1.lower() == 'e':
            act15()
            continue
        else:
            print("Invalid activity selection.")
            continue
    elif user_input == "3":
        print("``````````````````````````````````````````")
        print("--> Selected Topic: Operators")
        print("Available Activities: \na. Arithmetic Operations\nb. Assignment Operators\nc. Relational Operators")
        activity2 = input("Select an activity (a-c): ")
        if activity2.lower() == 'a':
            arithmetic()
            continue
        elif activity2.lower() == 'b':
            assignment()
            continue
        elif activity2.lower() == 'c':
            relational()
            continue    
        else:
            print("Invalid activity selection.")
            continue
        continue
    elif user_input == "4":
        print("``````````````````````````````````````````")
        print("--> Selected Topic: If-Elif-Else Statements")
        