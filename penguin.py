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
        print("\n")
        opt = input("Enter a number of your chosen topic (1-6): ")
        os.system('cls')
        if opt == '1':
            print(f"Hi, {name}! Welcome to Printing in Python.\n")
            printing_opt()
            print_menu()

            #repeating sub-menu for printing topic
            sub_menu = True
            while sub_menu == True:
                men = input("Select a letter of your choice (a-d): ").lower()
                os.system('cls')
                if men == 'a':
                    printing_opt()
                    print("\n~ Simple Printing ~")
                    print_output()
                    print_input()
                    print("\n")
                    os.system('pause')
                    #continue to sub-menu
                    os.system('cls')
                    print_menu()
                elif men == 'b':
                    os.system('cls')
                    print("~ Print with numbers ~")
                    print_numbers()
                    os.system('pause')
                    #continue to sub-menu
                    os.system('cls')
                    print_menu()
                elif men == 'c':
                    print("~ Printing with string and concatenation ~")
                    Var()
                    print_cont()
                    os.system('pause')
                    #continue to sub-menu
                    os.system('cls')
                    print_menu()
                elif men == 'd':
                    print("~ Escape Sequence ~")
                    escape_seq()
                    os.system('pause')
                    #continue to sub-menu
                    os.system('cls')
                    print_menu()
                elif men == 'e':
                    Menu()
                else:
                    print("Invalid input. Please try again")
                    continue
                continue
        elif opt == '2':
            print(f"Hi, {name}! Welcome to Conditional Statements in Python.\n")
            conditional_statements()
            conditional_menu()

            #repeating sub-menu for conditional statements topic
            cond_sub_menu = True
            while cond_sub_menu == True:
                answer = input("Select a letter of your choice (a-e): ").lower()
                os.system('cls')
                if answer == 'a':
                    conditional_statements()
                    if_statements()
                    os.system('pause')
                    #continue to sub-menu
                    os.system('cls')
                    conditional_menu()
                elif answer == 'b':
                    pass
                elif answer == 'c':
                    pass
                elif answer == 'd':
                    pass    
                elif answer == 'e':
                    Menu()
                else:
                    print("Invalid input. Please try again")
                    continue
        elif opt == '3':
            pass        
        elif opt == '4':
            pass
        elif opt == '5':
            pass
        elif opt == '6':
            print(f"Thank you for using the program, {name}! Goodbye!")
            break
    elif option == 'no':
        print('Okay, Thank You! Exiting the program...')
        break
    else:
        print("Invalid output")
        continue



