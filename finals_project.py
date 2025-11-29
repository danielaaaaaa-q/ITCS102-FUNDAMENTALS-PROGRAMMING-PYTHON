from penguin import *

def Menu():
    print("----------------------------------------------------")
    print("\t\t~ MAIN MENU ~")
    print("\t1. Printing in Python\n\t2. Conditional Statements\n\t3. Loops\n\t4. Functions\n\t5. Listing\n\t6. Exit")
    print("----------------------------------------------------")

def printing_opt():
    print("``Printing in python using the function \"print()\" is used to display the output on the console or the screen such as variables, messages, computations results, formatted output.``")

def print_menu():
    print("\n\t----------------------------------------------------")
    print("\t\t\tMenu to Printing in Python")
    print("\t\ta. Simple Printing\n\t\tb. Print with numbers\n\t\tc. Printing with string and concatenation\n\t\td. back to main menu")
    print("\t----------------------------------------------------")

def print_output():
    print("\n·OUTPUT:")
    print("\nHello, World!")
    print("Have a nice day!")
    print("How are you?")

def print_input():
    print("\n·INPUT:")
    print("\nprint(\"Hello, World!\")")
    print("print(\"Have a nice day!\")")
    print("print(\"How are you?\")")

def print_numbers():
    print('''
    
    *We can also display numbers in print() function. However, we do not put it in double quotes.
    ·INPUT:

    print(3)
    print(13)
    print(8677)

    ·OUTPUT:

    3
    13
    8677
    ''')

def Var():
    print('''
    In python, variables are used to store data or information that can be accessed in a program. 
    ''')

def print_cont():
    print('''
    1. Using a "+" operator

    #to use this, we should put some variables first
    name = "John"
    age = 19
    message = "Hello, my name is " + name + "and I am " + age + "years old."
    print(message)

    - Output: 
    Hello, my name is John and I am 19 years old

    2. Using commas

    city = "Lucena City" 
    year = 2015
    print("I live in", city,"since", year)

    - Output:
    I live in Lucena City since 2015
    ''')
