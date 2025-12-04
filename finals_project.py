from penguin import *

def Menu():
    print("----------------------------------------------------")
    print("\t\t~ MAIN MENU ~")
    print("\t1. Printing in Python with variables\n\t2. Conditional Statements\n\t3. Operators\n\t4. Loops\n\t5. Lists\n\t6. Functions\n\t7. Exit")
    print("----------------------------------------------------")

def printing_opt():
    print("``Printing in python using the function \"print()\" is used to display the output on the console or the screen such as variables, messages, computations results, formatted output.``")

def print_menu():
    print("\n\t----------------------------------------------------")
    print("\t\t\t~ Menu to Printing in Python ~")
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
    
    #we use commas to separate the variables and strings inside the print() function

    city = "Lucena City" 
    year = 2015
    print("I live in", city,"since", year)

    - Output:
    I live in Lucena City since 2015
          
    3. Formatted String (f-strings)
          
    #we use f-strings to embed expressions inside string literals, using curly braces {}
          
    country = "Philippines"
    province = "Quezon Province"
    print(f"I am from {province}, {country}")
          
    - Output:
    I am from Quezon Province, Philippines
    ''')

def escape_seq():
    print('''
    ~ Escape sequences are special characters that are used to represent certain whitespace or non-printable characters in a string. 
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
    print("\t\t\t~ Menu to Conditional Statements ~")
    print("\t\ta. If Statements\n\t\tb. If-Else Statements\n\t\tc. If-Elif-Else Statements\n\t\td. Nested If Statements\n\t\te. Back to Main Menu")
    print("\t----------------------------------------------------") 

def if_statements():
    print('''
    ~ An if statement is a conditional statement that executes a block of code if a specified condition is true.
          
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
    ~ An if-else statement is a conditional statement that executes one block of code if a specified condition is true, and another block of code if the condition is false.

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

def if_elif_else_statement():
    print('''
    ~ An if-elif-else statement allows for checking multiple conditions sequentially. If the if condition is False, the program checks the elif conditions in order. If none of the if or elif conditions are True, the else block is executed.
          
    Syntax:
    if conditional:
        #code to be executed if condition is true
    elif contional:
        #code to be executed if elif condition is true
    else:
        #code to be executed if all conditions are false
    
    *Note: There can be multiple elif statements, but only one else statement is allowed at the end.      

    ''')

def if_elif_else_ex():
    print('''
    Example:
          
    In this example, we will determine the grade of a student based on their score.
          
    score = eval(input("Enter your score (0-100): "))
    
    if score >= 90:
        print("Grade A")
    elif score >=80:
        print("Grade B")
    elif score >=70:
        print("Grade C")
    else:
        print("Grade F")
          
    - Output:
    If the user inputs 85, the output will be "Grade B".
    If the user inputs 65, the output will be "Grade F".

    ''')

def if_elif_else_run():
    score = eval(input("Enter your score (0-100): "))
    
    if score >= 90:
        print("Grade A")
    elif score >=80:
        print("Grade B")
    elif score >=70:
        print("Grade C")
    else:
        print("Grade F")
    return

def nest_statements():
    print('''
    ~ A nested if statement is an if statement placed inside another if statement, used to test multiple, dependent conditions. This structure allows a program or formula to execute different actions based on a series of tests, where the result of the first test determines if the inner if statement is even evaluated. 
    
    Syntax:
    if conditional:
        #code to be executed if condition is true
        if conditional1:
            #code to be executed if condition1 is true
        else:
            #code to be executed if condition1 is false
    else:
        #code to be executed if condition is false

    ''')

def nest_example():
    print('''
    Example:
          
    *In this example, we will check your grade and attendance to determine if you pass the course.
          
    grade = 90
    attendance = 85
          
    if grade >= 75:
        if attendance >= 80:
            print("You passed the course!")
        else:
            print("Improve your attendance.")
    else:
        print("You failed the subject.")

    - Output:
    If grade is 90 and attendance is 85, the output will be "You passed the course!".
    If grade is 70 and attendance is 85, the output will be "You failed the subject.".
    If grade is 80 and attendance is 75, the output will be "Improve your attendance."
    ''')

def nest_run():
    grade = input("Enter your grade: ")
    attendance = input("Enter your attendance percentage: ")
          
    if grade >= 75:
        if attendance >= 80:
            print("You passed the course!")
        else:
            print("Improve your attendance.")
    else:
        print("You failed the subject.")
    return
