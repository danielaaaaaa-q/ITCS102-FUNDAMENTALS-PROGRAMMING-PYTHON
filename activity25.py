from activity25_1 import *
from activity25_2 import *
#Creating a Menu Options with while loop and functions

name = input("Hello! Please enter your name: ")
print(f"\nHi, {name}. Welome to my Compiler Program.")

isContinue = True

while isContinue == True:
    print("Select a Program.")
    print("A - Hello\nB - Summation\nC - Ascending and Descending number\nD - Favorite Book\nE - Activity 16\nF - Nested Loop\nG - Exit Program")
    choice = input("What program / code would you like to run? ").lower()

    if choice == "a":
        hello()
        continue
    elif choice == "b":
        summation()
        continue
    elif choice == "c":
        ascending_descending()
        continue
    elif choice == "d":
        fav_book()
        continue
    elif choice == "e":
        activity16()
        continue
    elif choice == "f":
        nested_loop()
        continue
    elif choice == "g":
        print("System Exiting... Goodbye!")
        break
    else:
        print("Invalid Input. Please try again.")
        continue