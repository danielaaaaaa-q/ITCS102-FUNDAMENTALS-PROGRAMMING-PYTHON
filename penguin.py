from finals_project import *
import os

name = input("What's your name? ").capitalize()

os.system('cls')

print(f"Hi, {name}!")

con = True

while con == True:
    option = input("Do you want to start the program? (yes/no)\n --> ").lower()
    os.system('cls')

    if option == 'yes':
        menu_running = True
        while menu_running:
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
                    men = input("Select a letter of your choice (a-e): ").lower()
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

                        run = True
                        while run:
                            run_ex_if = input("*Do you want to try the example? (yes/no): ").lower()
                            print("\n")
                            if run_ex_if == 'yes':
                                run_ex()
                                os.system('pause')
                                print("\n")
                            elif run_ex_if == 'no':
                                print("You chose not to run the example.")
                                os.system('pause')
                                break
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

                        run = True
                        while run: 
                            run_ex_if_else = input("*Do you want to try the example? (yes/no): ").lower()
                            print("\n")
                            if run_ex_if_else == 'yes':
                                if_else_run()
                                os.system('pause')
                                print("\n")
                            elif run_ex_if_else == 'no':
                                print("You chose not to run the example.")
                                os.system('pause')
                                break
                            else:
                                print("Invalid input. Please try again.")
                                continue
                        #continue to sub-menu
                        os.system('cls')
                        print(f"Hi, {name}! Welcome to the program.\n")
                        conditional_menu()
                    elif answer == 'c':
                        print("~ If-Elif -Else Statements ~")
                        if_elif_else_statement()
                        os.system('pause')
                        if_elif_else_ex()

                        hm = True
                        while hm:
                            run = input("*Do you want to try the example? (yes/no): ")
                            print("\n")
                            if run == 'yes':
                                if_elif_else_run()
                                os.system('pause')
                                print("\n")
                            elif run == 'no':
                                print("You chose not to run the example.")
                                os.system('pause')
                                break
                            else:
                                print("Invalid input. Please try again.")
                                continue
                        #continue to sub-menu
                        os.system('cls')
                        print(f"Hi, {name}! Welcome to the program.\n")
                        conditional_menu()
                    elif answer == 'd':
                        print("~ Nested If Statements ~")
                        nest_statements()
                        os.system('pause')
                        nest_example()

                        run = True
                        while run:
                            run_nest = input("*Do you want to try the example? (yes/no): ")
                            print("\n")
                            if run_nest == 'yes':
                                nest_run()
                                os.system('pause')
                                print("\n")
                            elif run_nest == 'no':
                                print("You chose not to run the example.")
                                os.system('pause')
                                break
                            else:
                                print("Invalid input. Please try again.")
                                continue
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
                print(f"Hi, {name}! Welcome to Operator topic.\n")
                operators()
                operators_menu()
                #repeating sub-menu for operator topic
                sub_menu = True
                while sub_menu == True:
                    men = input("Select a letter of your choice (a-f): ").lower()
                    os.system('cls')
                    if men == 'a':
                        operators()
                        print("\n~ Arithmetic Operators ~")
                        arith()
                        print("\n")
                        os.system('pause')
                        arith_ex()

                        run = True
                        while run:
                            run_arith = input("*Do you want to try the example? (yes/no): ").lower()
                            print("\n")
                            if run_arith == 'yes':
                                arith_run()
                                print("\n")
                                os.system('pause')
                            elif run_arith == 'no':
                                print("You chose not to run the example.")
                                os.system('pause')
                                break
                            else:
                                print("Invalid input. Please try again.")
                                continue
                        #continue to sub-menu
                        os.system('cls')
                        print(f"Hi, {name}! Welcome to Operator topic.\n")
                        operators_menu()
                    elif men == 'b':
                        os.system('cls')
                        print("~ Assignment Operators ~")
                        assignment()
                        os.system('pause')
                        assignment_ex()

                        run = True
                        while run: 
                            hm = input("Do you want to try the example? (yes/no): ").lower()
                            print("\n")
                            if hm == 'yes':
                                run_ass()
                                print("\n")
                                os.system('pause')
                            elif hm == 'no':
                                print("You chose not to run the example.")
                                os.system('pause')
                                break
                            else:
                                print("Invalid input. Please try again.")
                                continue
                        #continue to sub-menu
                        os.system('cls')
                        print(f"Hi, {name}! Welcome to Operator topic.\n")
                        operators_menu()
                    elif men == 'c':
                        print("~ Relational Operators ~")
                        relational()
                        os.system('pause')
                        relational_ex()
                        os.system('pause')

                        hm = True
                        while hm: 
                            print("\n")
                            run = input("*Do you want to try the example? (yes/no): ")
                            if run == 'yes':
                                run_relational()
                                print("\n")
                                os.system('pause')
                            elif run == 'no':
                                print("You chose not to try the example.")
                                os.system('pause')
                                break
                            else:
                                print("Invalid input. Please try again.")
                                continue
                        #continue to sub-menu
                        os.system('cls')
                        print(f"Hi, {name}! Welcome to Operator topic.\n")
                        operators_menu()
                    elif men == 'd':
                        print("~ Logical Operators ~")
                        logical()
                        os.system('pause')
                        logical_ex()
                        os.system('pause')

                        hm = True
                        while hm:
                            print("\n")
                            run = input("*Do you want to try the example? (yes/no): ")
                            if run == 'yes':
                                run_logic()
                                print("\n")
                                os.system('pause')
                            elif run == 'no':
                                print("You chose not to try the example.")
                                os.system('pause')
                                break
                            else:
                                print("Invalid input. Please try again.")
                                continue
                        #continue to sub-menu
                        os.system('cls')
                        print(f"Hi, {name}! Welcome to Operator topic.\n")
                        operators_menu()
                    elif men == 'e':
                        sub_menu = False
                        print(f"Hi, {name}! Welcome to the program.\n")
                    else:
                        print("Invalid input. Please try again")
                        #continue to sub-menu
                        print(f"Hi, {name}! Welcome to the program.\n")
                        operators_menu()
                continue        
            elif opt == '4':
                print(f"Hi, {name}! Welcome to Loops in Python.\n")
                loops()
                loops_menu()
                #repeating sub-menu for loops topic
                menu = True
                while menu == True:
                    ha = input("Select a letter of your choice (a-d): ").lower()
                    os.system('cls')
                    if ha == 'a':
                        print("~ For Loops ~")
                        for_loops()
                        print("\n")
                        os.system('pause')
                        os.system('cls')

                        run = True
                        while run:
                            #for examples
                            loops_ex_menu()
                            opt = input("Select a letter of your choice (a-h): ")
                            #repeating sub-menu
                            if opt == 'a':
                                print("~ Basic for loop ~")
                                for_ex()
                                for_ex1()
                                print('\n')
                                os.system('pause')
                                loops_ex_menu()
                            elif opt == 'b':
                                print("~ Summation using for loop ~")
                                for_ex2()
                                for_ex_2()
                                print('\n')
                                os.system('pause')
                                loops_ex_menu()
                            elif opt == 'c':
                                print("~ New line ~")
                                for_ex3()
                                for_ex_3()
                                print('n')
                                os.system('pause')
                                loops_ex_menu()
                            elif opt == 'd':
                                print("~ Ascending and Descending ~")
                                for_ex4()
                                for_ex_4()
                                print('\n')
                                os.system('pause')
                                loops_ex_menu()
                            elif opt == 'e':
                                print("~ Factorial ~")
                                for_ex5()
                                for_ex_5()
                                print('\n')
                                os.system('pause')
                                loops_ex_menu()
                            elif opt == 'f':
                                print("~ Multiplication Table ~")
                                for_ex6()
                                for_ex_6()
                                print('\n')
                                os.system('pause')
                                loops_ex_menu()
                            elif opt == 'g':
                                print("~ Timer ~")
                                for_ex7()
                                for_ex_7()
                                print('\n')
                                os.system('pause')
                                loops_ex_menu()
                            elif opt == 'h':
                                print(f"Hi, {name}! Welcome to the program.")
                                loops_ex_menu()
                            else: 
                                print("Invalid input. Please try again.")
                                #continue to sub-menu
                                print(f"Hi, {name}! Welcome to the program.")
                                loops_ex_menu()
                            continue
                    elif ha == 'b':
                        print("~ Nester for loop ~")
                        pass
                    elif ha == 'c':
                        print("~ While loop ~")
                        pass
                    elif ha == 'd':
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
        


