from finals_project import *
import os

name = input("What's your name? ").capitalize()

os.system('cls')

print(f"Hi, {name}!")
option = input("Do you want to start the program? (yes/no)\n --> ").lower()

con = True

while con == True:
    if option == 'yes':
        Menu()
        opt = input("Enter a number of your chosen topic (1-6): ")
        os.system('cls')
        if opt == '1':
            printing_opt()
            print_menu()
            men = input("Select a letter of your choice (a-d): ").lower()
            if men == 'a':
                print("~ Simple Printing ~")
                print_output()
                print_input()
            elif men == 'b':
                os.system('cls')
                print("~ Print with numbers ~")
                print_numbers()
            elif men == 'c':
                print("~ Printing with string and concatenation ~")
                Var()
                print_cont()
            elif men == 'd':
                Menu()
            else:
                print("Invalid input. Please try again")
                continue
            continue
        elif opt == '2':
            pass
            continue
        elif opt -- '3':
            pass
            continue
        elif opt -- '4':
            pass
            continue
        elif opt -- '5':
            pass
            continue
        elif opt -- '6':
            pass
            continue
        else:
            pass
            continue
        continue
    elif option == 'no':
        print('Exiting the program...')
        break
    else:
        print("Invalid output")
    break



