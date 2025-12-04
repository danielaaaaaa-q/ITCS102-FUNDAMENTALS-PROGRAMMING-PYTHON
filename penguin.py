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
        opt = input("Enter a number of your chosen topic (1-7): ")
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
                    print("\nIn this example, we will print a message to the user. To print a string of text, just enclose it in single or double quotes within the print() function.\nThis is an example of simple printing in Python: \n")
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
                    sub_menu = False
                    print(f"Hi, {name}! Welcome to the program.\n")
                else:
                    print("Invalid input. Please try again")
                    #continue to sub-menu
                    print(f"Hi, {name}! Welcome to the program.\n")
                    print_menu()
            continue
        elif opt == '2':
            print(f"Hi, {name}! Welcome to Conditional Statements in Python.\n")
            conditional_statements()
            conditional_menu()
            #repeating sub-menu for conditional statements topic
            cond_sub_menu = True
            while cond_sub_menu == True:
                answer = input("\nSelect a letter of your choice (a-e): ").lower()
                os.system('cls')
                if answer == 'a':
                    print("~ If Statements ~")
                    if_statements()
                    os.system('pause')
                    ex_trial_if()
                    run_ex_if = input("*Do you want to try the example? (yes/no): ").lower()
                    print("\n")
                    if run_ex_if == 'yes':
                        run_ex()
                        os.system('pause')
                        print("\n")
                    elif run_ex_if == 'no':
                        print("You chose not to run the example.")
                        os.system('pause')
                    else:
                        print("Invalid input. Please try again.")
                        continue
                    #continue to sub-menu
                    os.system('cls')
                    print(f"Hi, {name}! Welcome to Conditional Statements in Python.\n")
                    conditional_menu()
                elif answer == 'b':
                    if_else_statements()
                    os.system('pause')
                    if_else_ex()
                    run_ex_if_else = input("*Do you want to try the example? (yes/no): ").lower()
                    print("\n")
                    if run_ex_if_else == 'yes':
                        if_else_run()
                        os.system('pause')
                        print("\n")
                    elif run_ex_if_else == 'no':
                        print("You chose not to run the example.")
                        os.system('pause')
                    else:
                        print("Invalid input. Please try again.")
                    #continue to sub-menu
                    os.system('cls')
                    print(f"Hi, {name}! Welcome to the program.\n")
                    conditional_menu()
                elif answer == 'c':
                    print("~ If-Elif -Else Statements ~")
                    if_elif_else_statement()
                    os.system('pause')
                    if_elif_else_ex()
                    run = input("*Do you want to try the example? (yes/no): ")
                    print("\n")
                    if run == 'yes':
                        if_elif_else_run()
                        os.system('pause')
                        print("\n")
                    elif run == 'no':
                        print("You chose not to run the example.")
                        os.system('pause')
                    else:
                        print("Invalid input. Please try again.")
                    #continue to sub-menu
                    os.system('cls')
                    print(f"Hi, {name}! Welcome to the program.\n")
                    conditional_menu()
                elif answer == 'd':
                    print("~ Nested If Statements ~")
                    nest_statements()
                    os.system('pause')
                    nest_example()
                    run_nest = input("*Do you want to try the example? (yes/no): ")
                    print("\n")
                    if run_nest == 'yes':
                        nest_run()
                        os.system('pause')
                        print("\n")
                    elif run_nest == 'no':
                        print("You chose not to run the example.")
                        os.system('pause')
                    else:
                        print("Invalid input. Please try again.")
                    #continue to sub-menu
                    os.system('cls')
                    print(f"Hi, {name}! Welcome to the program.\n")
                    conditional_menu()
                elif answer == 'e':
                    cond_sub_menu = False
                    print(f"Hi, {name}! Welcome to the program.\n")
                else:
                    print("Invalid input. Please try again")
                    #continue to sub-menu
                    print(f"Hi, {name}! Welcome to the program.\n")
                    conditional_menu()
                    continue
        elif opt == '3':
            pass        
        elif opt == '4':
            pass
        elif opt == '5':
            pass
        elif opt == '6':
            pass
        elif opt == '7':
            print(f"Thank you for using the program, {name}! Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")
            continue
    elif option == 'no':
        print(f'Thank You for using the program, {name}! Goodbye!')
        break
    else:
        print("Invalid output")
        continue



