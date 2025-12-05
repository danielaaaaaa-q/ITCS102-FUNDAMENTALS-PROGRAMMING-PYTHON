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

def operators():
    print('''
    ~ In Python programming, Operators in general are used to perform operations on values and variables.
''')
    
def operators_menu():
    print("\n\t----------------------------------------------------")
    print("\t\t\t~ Menu to Operators ~")
    print("\t\ta. Arithmetic Operators\n\t\tb. Assigment Operators\n\t\tc. Relational Operators\n\t\td. Logical Operators\n\t\te. Back to Main Menu")
    print("\t----------------------------------------------------")

def arith():
    print('''
    ~ Arithmetic operators are used to perform basic mathematical operations like addition, subtraction, multiplication and division.
          
    Operators:
    + : Addition
    - : Subtraction
    * : Multiplication
    / : Division            #returns float (decimal number)
    % : Modulus             #remainder of division 
    ** : Exponentiation
    // : Floor Division     #returns integer (whole number) by removing the decimal part
    
    ''')

def arith_ex():
    print('''
    ~ In this example, we will perform various arithmetic operations on two numbers provided by the user.      

    n1 = eval(input("Enter the first number --> "))
    n2 = eval(input("Enter the second number --> "))

    a = n1 + n2
    b = n1 - n2
    c = n1 * n2
    d = n1 / n2

    solution = ((n1 / n2) * 200 - 5) // 500
    print("\\nThe sum of", n1,"and", n2,"is", a)
    print("The difference of", n1,"and", n2,"is", b)
    print("The product of", n1,"and", n2,"is", c)
    print("The quotient of", n1,"and", n2,"is", d)
    print(n1, "exponent by", n2,"is", n1**n2)
    print("The remainder of", n1,"and", n2,"is", n1 % n2)
    print("The floor division of", n1,"and", n2,"is", n1//n2)

    - Output:
    If the user inputs 10 (n1) and 3 (n2), the output will be:
          
    The sum of 10 and 3 is 13
    The difference of 10 and 3 is 7    
    The product of 10 and 3 is 30
    The quotient of 10 and 3 is 3.33
    10 exponent by 3 is 1000
    The remainder of 10 and 3 is 1
    The floor division of 10 and 3 is 3
    ''')

def arith_run():
    n1 = eval(input("Enter the first number --> "))
    n2 = eval(input("Enter the second number --> "))

    a = n1 + n2
    b = n1 - n2
    c = n1 * n2
    d = n1 / n2

    solution = ((n1 / n2) * 200 - 5) // 500
    print("\nThe sum of", n1,"and", n2,"is", a)
    print("The difference of", n1,"and", n2,"is", b)
    print("The product of", n1,"and", n2,"is", c)
    print("The quotient of", n1,"and", n2,"is", d)
    print(n1, "exponent by", n2,"is", n1**n2)
    print("The remainder of", n1,"and", n2,"is", n1 % n2)
    print("The floor division of", n1,"and", n2,"is", n1//n2)   
    return

def assignment():
    print('''
    ~ Assignment Operators are used to assign values to variables.
    
    Operators:
    = : Assigns value from right side to left side
    += : Adds and assigns value
    -= : Subtracts and assigns value
    *= : Multiplies and assigns value
    /= : Divides and assigns value
    %= : Modulus and assigns value
    **= : Exponentiation and assigns value
    //= : Floor Division and assigns value   

    ''')

def assignment_ex():
    print('''
    ~ In this example, we will perform various assignment operators on one number. 
   
    a = 7

    print("The value of a is", a)

    a += 13
    a -= 17
    a *= 3
    a += 18
    a /= 2

    print("The value of a is", a)

    - Output:
    The value of a is 7
    The value of a is 13.5
          
    ''')

def run_ass():
    
    a = eval(input("Enter a number: "))

    print("The value of a is", a)

    a += 13
    a -= 17
    a *= 3
    a += 18
    a /= 2

    print("The value of a is", a)
    return

def relational():
    print('''
    ~ Relational Operators, also know as Comparison Operators, are used to compare two values and determine the relationship between them. They always return a boolean value: True if the comparison is true, and False otherwise.

    Operators:
    == : Equal to
    != : Not equal to 
    > : Greater than 
    < : Less than
    >= : Greater than or equal to
    <= : Less than or equal to

    ''')

def relational_ex():
    print('''
    ~ Example:
          
    #1
    balance = 3000
    withdrawal = 600

    print(balance >= withdrawal)
          
    - Output:
    True

    #2
    name1 = "millicent"
    name2 = "Millicent"

    print(name1 == name2)

    - Output:
    False

    ''')

def run_relational():
    num = eval(input("Enter a number to compare: "))
    number = eval(input("Enter another one: "))

    print(f"== \n- Output: {num == number}")
    print(f">= \n- Output: {num >= number}")
    print(f"<= \n- Output: {num <= number}")
    
def logical():
    print('''
    ~ Logical Operators perform Logical AND, Logical OR and Logical NOT operations. It is used to combine conditional statements.

    Operators:
    and : Returns True if both statements are true
    or : Returns True if one of the statement is true
    not : Reverses the result, returns False if the result is true

    ''')

def logical_ex():
    print('''
    *Example:
          
    a = True
    b = False
    print(a and b)
    print(a or b)
    print(not a)    

    - Output:
    False
    True
    False
          
''')
    
def run_logic():
    x = eval(input("Enter a number: "))
    y = eval(input("Enter a number: "))
    print("x > 0 and y > 5\n- Output: ")
    print(x > 0 and y > 5) 
    print("x < 0 or y > 5\n- Output: ") 
    print(x < 0 or y > 5)
    print("not y < 5\n- Output: ")
    print(not y < 5)
    return

def loops():
    print('''
    ~ Python provides two primary types of loops for repetitive execution of code blocks: for loops and while loops.

''')
    
def loops_menu():
    print("\n\t----------------------------------------------------")
    print("\t\t\t~ Menu to Loops ~")
    print("\t\ta. For Loops\n\t\tb. Nested for loops\n\t\tc. While Loops\n\t\td. Back to Main Menu")
    print("\t----------------------------------------------------")

def for_loops():
    print('''
    ~ for loop repeats a block of code many times depending on the numbers given in the range()
    ~ They execute a block of code for each item in the sequence.

    Syntax:
    for variable x in range (Start, Stop, Step)
          code block

    # variable x - name of the loop variable
    # range(Start, Stop, Step) - creates a list of numbers starting from start, ending before stop, and changing by step
    # start - where the count begins
    # stop - where the counting end (but not included)
    # step - how much it increases or decreases each time      
    
    ''')

def loops_ex_menu():
    print("\n\t----------------------------------------------------")
    print("\t\t\t~ Menu to Examples of for loop ~")
    print("\t\ta. Basic for loop\n\t\tb. Summation using for loop\n\t\tc. New Line\n\t\td. Ascending and Descending\n\t\te. Factorial\n\t\tf. Multiplication Table\n\t\tg. Timer\n\t\th. Back to Main Menu")
    print("\t----------------------------------------------------")

def for_ex():
    #activity 12
    print('''
    *Example
    
    #print("Hello World!")

    for i in range(1, 10, 1):
        print("Hello World!")
          
    - Ouput:
    ''')

def for_ex1():
    #print("Hello World!")

    for i in range(1, 10, 1):
        print("Hello World!")
    return

def for_ex2():
    print('''
    *Example:
          
    num = 0

    for i in range(1, 11):
        number = eval(input("Enter a number:"))
        num += number
        print("The current sum is:", num)
    print(num)

    - Output:
          
''')

def for_ex_2():
    #activity 13
    num = 0

    for i in range(1, 11):
        number = eval(input("Enter a number:"))
        num += number
        print("The current sum is:", num)
    print(num)
    return

def for_ex3():
    print('''
    *Example:
    
    #-- ascending order --
    for i in range(1, 11):
        print(i)

    #-- descending order --
    for i in range(10, 0, -1):
        print(i)  

    - Output:
          
''')

def for_ex_3():
    #activity 14
    #-- ascending order --
    for i in range(1, 11):
            print(i)

    #-- descending order --
    for i in range(10, 0, -1):
        print(i)

def for_ex4():
    print('''
    *Example:
          
    #new line in print

    for i in range(1, 11):
        print(i, end=" --- ")

    - Output:      
    
''')

def for_ex_4():
    #activity 16
    #new line in print

    for i in range(1, 11):
        print(i, end=" --- ")

def for_ex5():
    print('''
    *Example:
          
    print("\t\tFACTORIAL PROGRAM")

    fact = eval(input("Enter a numbe ---> "))

    num = 1
    for y in range(fact, 0, -1):
        print(y)
        num *= y
    print("\nThe factorial of", fact, "is", num)

    - Output:

''')
    
def for_ex_5():
    #cc6
    print("\t\tFACTORIAL PROGRAM")

    fact = eval(input("Enter a numbe ---> "))

    num = 1
    for y in range(fact, 0, -1):
        print(y)
        num *= y
    print("\nThe factorial of", fact, "is", num)
    return

def for_ex6():
    print('''
    *Example:
          
    
    print("MULTIPLICATION TABLE MAKER")

    num = eval(input("Enter a number ---> "))

    print("\nThe multiplication table for", num,":")
    for x in range(1, 11):
        print(num, "x", x, "=", num * x)5

    - Output:
          
''')
    
def for_ex_6():
    #cc8
    print("MULTIPLICATION TABLE MAKER")

    num = eval(input("Enter a number ---> "))

    print("\nThe multiplication table for", num,":")
    for x in range(1, 11):
        print(num, "x", x, "=", num * x)
    return

def for_ex7():
    print('''
    *Example: 
           
    print("⏳ COUNTDOWN TIMER SIMULATOR")

    num = eval(input("Enter the starting number for countdown: "))

    print("\nCountdown started:")

    for x in range(num, 0, -1):
        print(x)
    print("Liftoff!")

    - Output:

''')

def for_ex_7():
    #cc9
    print("⏳ COUNTDOWN TIMER SIMULATOR")

    num = eval(input("Enter the starting number for countdown: "))

    print("\nCountdown started:")

    for x in range(num, 0, -1):
        print(x)
    print("Liftoff!")
    return



