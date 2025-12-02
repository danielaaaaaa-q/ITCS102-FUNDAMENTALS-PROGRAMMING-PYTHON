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
    print("\t\ta. Simple Printing\n\t\tb. Print with numbers\n\t\tc. Printing with string and concatenation\n\t\td. Escape Sequence\n\t\te. Back to Main Menu")
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
    1. Using a "+" operator (concatenation)

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
          
    3. Formatted String (f-strings)
          
    country = "Philippines"
    province = "Quezon Province"
    print(f"I am from {province}, {country}")
          
    - Output:
    I am from Quezon Province, Philippines
    ''')

def escape_seq():
    print('''
    Escape sequences are special characters that are used to represent certain whitespace or non-printable characters in a string. 
    Some common escape sequences in Python include:

    \\n : Newline
    \\t : Tab
    \\\\ : Backslash
    \\' : Single Quote
    \\" : Double Quote

    Example:
    print("Hello, World!\\nWelcome to Python programming.")
          
    - Output:
    Hello, World!
    Welcome to Python programming.
    ''')

def conditional_statements():
    print('''Python conditional statements are commands that let a program decide what action to take based on a condition. They check whether something is true or false, and then run specific code depending on the result.''')

def conditional_menu():
    print("\n\t----------------------------------------------------")
    print("\t\t\tMenu to Conditional Statements")
    print("\t\ta. If Statements\n\t\tb. If-Else Statements\n\t\tc. Elif Statements\n\t\td. Nested If Statements\n\t\te. Back to Main Menu")
    print("\t----------------------------------------------------") 

def if_statements():
    print('''
    An if statement is a conditional statement that executes a block of code if a specified condition is true.
          
    == - equals
    != - not equals
    >  - greater than
    <  - less than
    >= - greater than or equal to
    <= - less than or equal to

    Syntax:
    if condition:
        # code to be executed if condition is true  
    ''')

def ex_trial_if():
    print('''
    Example: #jeepney fare

    This example shows how to use an if statement to check if a user is eligible for a student discount on jeepney fare.

    name = input("Input your name: ")
    isStudent = input("Are you a student (yes/no): ")
    fare = eval(input("bayad: "))

    if isStudent.lower() == "yes":
	    discount = fare * .2
	    new_fare = fare - discount
	    print("Hi,", name, "your student discount is", discount, "\n\t     Discounted fare is", new_fare)
    else:
	    print("Sorry,", name," you are not eligible for student discount.")
    
    ''')

def run_ex():
    name = input("Input your name: ")
    isStudent = input("Are you a student (yes/no): ")
    fare = eval(input("bayad: "))

    if isStudent.lower() == "yes":
        discount = fare * .2
        new_fare = fare - discount
        print("Hi,", name, "your student discount is", discount, "\n\t     Discounted fare is", new_fare)
    else:
        print("Sorry,", name," you are not eligible for student discount.")
    return 

def if_else_statements():
    print('''
    An if-else statement is a conditional statement that executes one block of code if a specified condition is true, and another block of code if the condition is false.

    Syntax:
    if condition:
        # code to be executed if condition is true  
    else:
        # code to be executed if condition is false  
    ''')
    
def if_else_ex():
    print('''
    Example:

    In this example, we will check if a number that the user inputs is even or odd.
          
    number = eval(input("Input a number: "))

    if number % 2 == 0:          #checks if the number is divisible by 2
	    print("EVEN")            #if true, print EVEN
    else:
	    print("ODD")             #if false, print ODD
    ''')

def if_else_run():
    number = eval(input("Input a number: "))

    if number % 2 == 0:          #checks if the number is divisible by 2
        print("EVEN")            #if true, print EVEN
    else:
        print("ODD")             #if false, print ODD
    return
