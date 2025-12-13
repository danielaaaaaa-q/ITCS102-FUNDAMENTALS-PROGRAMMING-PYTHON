from mocha import *
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
            print(f"Hi, {name}! Welcome to the program.\n")
            Menu()
            opt = input("Enter a number of your chosen topic (1-8): ")
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
                        print("\n~ Simple Printing ~")
                        print_input()
                        os.system('pause')
                        #continue to sub-menu
                        os.system('cls')
                        print(f"Hi, {name}! Welcome to Printing in Python.\n")
                        print_menu()
                    elif men == 'b':
                        os.system('cls')
                        print("~ Print with numbers ~")
                        print_numbers()
                        os.system('pause')
                        #continue to sub-menu
                        os.system('cls')
                        print(f"Hi, {name}! Welcome to Printing in Python.\n")
                        print_menu()
                    elif men == 'c':
                        print("~ Strings ~")
                        string()
                        strings_menu()

                        #repeating sub-menu
                        run = True
                        while run: 
                            ent = input("Select a letter of your choice (a-c): ").lower()
                            os.system('cls')
                            if ent == 'a':
                                print("~ Escape Sequence ~")
                                escape_seq()
                                os.system('pause')

                                #running the example
                                ha = True
                                while ha:
                                    ok = input("Do you want to try the last example? (yes/no): ").lower()
                                    print('\n')
                                    if ok == 'yes':
                                        diamond()
                                        os.system('pause')
                                        print('\n')
                                    elif ok == 'no':
                                        print("Going back to the sub-menu...")
                                        os.system('pause')
                                        break
                                    else:
                                        print("Invalid input. Please try again.")
                                        continue
                                #continue to sub-menu
                                os.system('cls')
                                print(f"Hi, {name}! Welcome to Strings in Python.\n")
                                strings_menu()   
                            elif ent == 'b':
                                print("~ Formatted Strings ~")
                                f_string()
                                f_ex()
                                os.system('pause')
                                #continue to sub-menu
                                os.system('cls')
                                strings_menu() 
                            elif ent == 'c':
                                run == False
                                print(f"Hi, {name}! Welcome to Printing in Python.")
                                print_menu()
                                break
                            else: 
                                print("Invalid input. Please try again.")
                                #continue to sub-menu
                                strings_menu()
                                continue
                    elif men == 'd':
                        sub_menu = False
                    else:
                        print("Invalid input. Please try again")
                        #continue to sub-menu
                        print_menu()
                continue
            elif opt == '2':
                print(f"Hi, {name}! Welcome to Variables in Python.\n")
                Var()
                var_menu()

                #repeating sub-menu
                run = True
                while run == True:
                    menu = input("Select a letter of your choice (a-d): ").lower()
                    os.system('cls')
                    if menu == 'a':
                        print("~ Simple Variable ~")
                        simple()
                        os.system('pause')
                        #continue to sub-menu
                        os.system('cls')
                        var_menu()
                    elif menu == 'b':
                        print("~ Concatenation ~")
                        cont()
                        os.system('pause')
                        #continue to sub-menu
                        os.system('cls')
                        var_menu()
                    elif menu == 'c':
                        print("~ Data Types ~")
                        data()
                        os.system('pause')
                        data_ex()
                        os.system('pause')
                        #continue to sub-menu
                        os.system('cls')
                        var_menu()
                    elif menu == 'd':
                        run == False
                        break
                    else:
                        print("Invalid input. Please try again.")
                        #continue to su-menu
                        var_menu()
                    continue
            elif opt == '3':
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
                                print("Going back to the menu...")
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
                                print("Going back to the menu...")
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
                                print("Going back to the menu...")
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
                                print("Going back to the menu...")
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
            elif opt == '4':
                print(f"Hi, {name}! Welcome to Operators in Python.\n")
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
                                print("Going back to the menu...")
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
                                print("Going back to the menu...")
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
                                print("Going back to the menu...")
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
                                print("Going back to the menu...")
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
                        break
                    else:
                        print("Invalid input. Please try again")
                        #continue to sub-menu
                        print(f"Hi, {name}! Welcome to Operators in Python.\n")
                        operators_menu()
                continue        
            elif opt == '5':
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
                            os.system('cls')
                            #repeating sub-menu
                            if opt == 'a':
                                print("~ Basic for loop ~")
                                for_ex()
                                for_ex1()
                                print('\n')
                                os.system('pause')
                                loops_ex_menu()
                                os.system('cls')
                            elif opt == 'b':
                                print("~ Summation using for loop ~")
                                for_ex2()
                                for_ex_2()
                                print('\n')
                                os.system('pause')
                                loops_ex_menu()
                                os.system('cls')
                            elif opt == 'c':
                                print("~ Ascending and Descending ~")
                                for_ex3()
                                for_ex_3()
                                print('n')
                                os.system('pause')
                                loops_ex_menu()
                                os.system('cls')
                            elif opt == 'd':
                                print("~ New line ~")
                                for_ex4()
                                for_ex_4()
                                print('\n')
                                os.system('pause')
                                loops_ex_menu()
                                os.system('cls')
                            elif opt == 'e':
                                print("~ Factorial ~")
                                for_ex5()
                                for_ex_5()
                                print('\n')
                                os.system('pause')
                                loops_ex_menu()
                                os.system('cls')
                            elif opt == 'f':
                                print("~ Multiplication Table ~")
                                for_ex6()
                                for_ex_6()
                                print('\n')
                                os.system('pause')
                                loops_ex_menu()
                                os.system('cls')
                            elif opt == 'g':
                                print("~ Timer ~")
                                for_ex7()
                                for_ex_7()
                                print('\n')
                                os.system('pause')
                                loops_ex_menu()
                                os.system('cls')
                            elif opt == 'h':
                                run == False
                                print(f"Hi, {name}! Welcome to Loops in Python.")
                                loops_menu()
                                break
                            else: 
                                os.system('cls')
                                print("Invalid input. Please try again.")
                                #continue to sub-menu
                                loops_ex_menu()
                            continue
                    elif ha == 'b':
                        print("~ Nested for loop ~")
                        nest_loop()
                        nest_menu()

                        #repeating sub-menu
                        yah = True
                        while yah:
                            ans = input("Select a letter of your choice (a-g): ").lower()
                            os.system('cls')
                            if ans == 'a':
                                print("~ Number Loop ~")
                                nest_ex()
                                os.system('pause')
                                print("Try it!\n")
                                nest_run()
                                os.system('pause')
                                #continue to sub-menu
                                os.system('cls')
                                nest_menu()
                            elif ans == 'b':
                                print("~ Number Right Triangle ~")
                                nest_right()
                                act18()
                                os.system('pause')
                                #continue to sub-menu
                                os.system('cls')
                                nest_menu()
                            elif ans == 'c':
                                print("~ Triangle ~")
                                triangle()
                                cc10()
                                os.system('pause')
                                #continue
                                os.system('cls')
                                nest_menu()
                            elif ans == 'd':
                                print("~ Number Pyramid ~")
                                num()
                                cc12()
                                os.system('pause')
                                print("Try it!")
                                try_nest()
                                os.system('pause')
                                #continue
                                os.system('cls')
                                nest_menu()
                            elif ans == 'e':
                                yah = False
                                print(f"Hi, {name}! Welcome to Loops in Python.\n")
                                loops_menu()
                                break
                            else:
                                print("Invalid input. Please try again.")
                                #continue to sub-menu
                                nest_menu()
                                continue
                    elif ha == 'c':
                        print("~ While loop ~")
                        while_loop()
                        while_menu()

                        #repeating sub-menu
                        aa = True
                        while aa: 
                            ans = input("Select a letter of your choice (a-c): ").lower()
                            os.system('cls')
                            if ans == 'a':
                                print("~ Washing ~")
                                while_ex()
                                os.system('pause')
                                print("Try it!\n")
                                try_while()
                                os.system('pause')
                                #continue to sub-menu
                                os.system('cls')
                                while_menu()
                            elif ans == 'b':
                                print("~ Odd Number Compiler")
                                odd_ex()
                                os.system('pause')
                                print("Try it!\n")
                                try_odd()
                                os.system('pause')
                                #continue to sub-menu
                                os.system('cls')
                                while_menu()
                            elif ans == 'c':
                                aa = False
                                print(f"Hi, {name}! Welcome to Loops in Python.\n")
                                loops_menu()
                                break
                            else:
                                print("Invalid input. Please try again.")
                                #continue to sub-menu
                                while_menu()
                                continue
                    elif ha == 'd':
                        menu == False
                        print(f"Hi, {name}! Welcome to the program.\n")
                        break
                    else:
                        print("Invalid input. Please try again.")
                        #continue to sub-menu
                        print(f"Hi, {name}! Welcome to Loops in Python.\n")
                        loops_menu()
                continue
            elif opt == '6':
                print(f"Hi, {name}! Welcome to Lists in Python.")
                lists()
                list_menu()

                aye = True
                while aye:
                    ha = input("Select a letter of your choice (a-e): ").lower()
                    os.system('cls')
                    if ha == 'a':
                        print("~ Examples ~")
                        example()
                        out_ex()
                        os.system('pause')
                        list_menu()
                        os.system('cls')
                    elif ha == 'b':
                        print("~ Indexing ")
                        examp()
                        os.system('pause')
                        list_menu()
                        os.system('cls')
                    elif ha == 'c':
                        print("~ Slicing ~")
                        slicing()
                        os.system('pause')
                        list_menu()
                        os.system('cls')
                    elif ha =='d':
                        print("~ Iteration ~")
                        iteration()
                        iterate()
                        os.system('pause')
                        list_menu()
                        os.system('cls')
                    elif ha == 'e':
                        aye = False
                        print(f"HI, {name}! Welcome to the program.")
                        break
                    else:
                        print("Invalid input. Please try again.")
                        print(f"Hi, {name}! Welcome to Lists in Python.")
                        list_menu()
                        continue
            elif opt == '7':
                print(f"Hi, {name}! Welcome to the topic of Functions in Python.")
                function()
                function_type()

                #repeating sub-menu
                hm = True
                while hm == True:
                    ans = input("Select a type of functions you want to discuss (a-c): ").lower()
                    os.system('cls')
                    if ans == 'a':
                        print("~ Built-in Functions ")
                        built()
                        os.system('pause')
                        os.system('cls')
                        function_type()
                    elif ans == 'b':
                        print("~ Proggramer-Defined Functions ~")
                        user_def()
                        greeting()
                        os.system('pause')
                        os.system('cls')
                        function_type
                    elif ans == 'c':
                        hm == False
                        print(f"Hi, {name}! Welcome to the program.\n")
                        break
                    else:
                        print("Invalid input. Please try again.")
                        #continue to sub-menu
                        function_type()
                    continue
            elif opt == '8':
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
    break    



