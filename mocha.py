def Menu():
    print("----------------------------------------------------")
    print("\t\t~ MAIN MENU ~")
    print("\t1. Printing in Python\n\t2. Variables\n\t3. Conditional Statements\n\t4. Operators\n\t5. Loops\n\t6. Lists\n\t7. Functions\n\t8. Exit")
    print("---------------------------------------------------")

def printing_opt():
    print('''
    Printing in python using the function "print()" is used to display the output on the console 
    or the screen such as variables, messages, computations results, formatted output."
    ''')

def print_menu():
    print("\n\t----------------------------------------------------------")
    print("\t\t\t~ Menu to Printing in Python ~\n")
    print("\t\ta. Simple Printing\n\t\tb. Print with numbers\n\t\tc. Strings\n\t\td. Back to Main Menu")
    print("\t------------------------------------------------------------")

def print_input():
    #Activity 1
    print('''
    In this example, we will print a message to the user. To print a string of text, 
    just enclose it in single or double quotes within the print() function. 
    
    This is an example of simple printing in Python:      

·INPUT:
          
        print("Hello, World!")
        print("Have a nice day!")   
        print("How are you?")
          
·OUTPUT:
          
        Hello, World!
        Have a nice day!
        How are you?

    ''')

def print_numbers():
    print('''
    We can also display numbers in print() function. However, we do not put it in double quotes.
          
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

def var_menu():
    print("\n\t----------------------------------------------------------")
    print("\t\t\t~ Menu to Variables in Python ~\n")
    print("\t\ta. Simple Variable\n\t\tb. Concatenation\n\t\tc. Data Types\n\t\td. Back to Main Menu")
    print("\t------------------------------------------------------------")

def data():
    print('''
    Data type is a classification that specifies the kind of value a variable can hold and the operations that can be performed on that data.
    Since everything in Python is an object, data types are essentially classes, and variables are instances (objects) of these classes. 

    Python has the following data types built-in by default, in these categories:
          
    Text Type : str
    Numeric Type : int, float, complex
    Sequence Type : list, tuple, range
    Mapping Type : dict
    Set Types : set, frozenset
    Boolean Type : bool
    
    Function to use: type()
          
''')
    
def data_ex():
    #activity 5
    print('''
    Example:      

    something = eval(input("Input something --> "))

    print("The data type of something is ", type(something))

    answer = 6 + something

    print("The answer is ", answer)

- Output:
        If we input number 7

        The data type of something is <class 'int'>
        The answer is 13
''')

def simple():
    print('''
    So, variable is created the moment you assign something to it.
    For example:    

    a = "Dynneal Antonio"

    print("X = ", a)

    - Output:
    X = Dynneal Antonio

    ''')

def cont():
    print('''
    Using a "+" operator (concatenation)
        - this operator joins two strings together.
          
For Example:
    #to use this, we should put some variables first
          
    name = "John"
    age = 19
          
    #then let us concatenate them using the "+" operator.
          
    message = "Hello, my name is " + name + "and I am " + age + "years old."
    print(message)

    - Output: 
    Hello, my name is John and I am 19 years old


    ''')

def f_string():
    #activity 15
    print('''
    Formatted String (f-strings)
          
    # we use f-strings to embed expressions inside string literals, using curly braces {}
    # simply put an f in front of the string literal, and add curly braces {} as placeholders for variables and other operations.
          
    
    # Write a Python program that takes a user's name and age as input and then prints a message using string formatting and its fav book

    name = input("Enter your name --> ")
    age = eval(input("Enter your age --> "))
    book = input("Enter your favourite book --> ")

    print(f"Hello, I am {name}, I am {age} years old and my favourite book is {book}.")
     
- Output:
    ''')

def f_ex():
    #STRING FORMATTING
    # Write a Python program that takes a user's name and age as input and then prints a message using string formatting and its fav book

    name = input("Enter your name --> ")
    age = eval(input("Enter your age --> "))
    book = input("Enter your favourite book --> ")

    print(f"Hello, I am {name}, I am {age} years old and my favourite book is {book}.")
    return

def escape_seq():
    #activity 3 and code_challenge 1
    print('''
    ~ Escape sequences are special characters that are used to represent certain whitespace or non-printable characters in a string. 
    Some common escape sequences in Python include:

    \\n : Newline
    \\t : Tab
    \\\\ : Backslash
    \\' : Single Quote
    \\" : Double Quote
    \\r : Carriage Return (moves the cursor to the start of the line.)

    ~ Example:
          
    print("\\tThe quick brown\\n\\t \\rFox jumps over\\n\\t the Lazy Dog.")
    print("\\\"Hindi ako makulit.\\"")
          
    - Output:
            The quick brown
    Fox jumps over
            the Lazy Dog.
    "Hindi ako makulit."
          
    ~ Another example:
          
    In this example, this shows the diamond * with a name that you are going to input 
    and then place it on the center. 
          
    name = input()

    print("\\t\\t\\t\\t\\t*\\n\\n" , "\\t\\t\\t\\t *\\t\\t*\\n\\n\\n" , "\\t\\t\\t*\\t\\t\\t\\t*\\n\\n\\n\\n" , "\\t\\t*                " , 
          "Hi, " , name , "\\t\\t\\t*\\n\\n\\n" ,  "\\t\\t\\t*\\t\\t\\t\\t*\\n\\n\\n\\n" , "\\t\\t\\t\\t*\\t\\t*\\n\\n\\n" , "\\t\\t\\t\\t\\t*\\n\\n")

    ''')

def diamond():
    name = input("Enter your name: ")

    print("\t\t\t\t\t*\n\n" , "\t\t\t\t *\t\t*\n\n\n" , "\t\t\t*\t\t\t\t*\n\n\n\n" , "\t\t*                " , "Hi, " , name , "\t\t\t*\n\n\n" ,  "\t\t\t*\t\t\t\t*\n\n\n\n" , "\t\t\t\t*\t\t*\n\n\n" , "\t\t\t\t\t*\n\n")
    return

def string():
    print('''
    Strings in python are surrounded by either single quotation marks, or double quotation marks.

    'hello' is the same as "hello".
    ''')

def strings_menu():
    print("\n\t----------------------------------------------------------")
    print("\t\t\t~ Menu to Strings in Python ~\n")
    print("\t\ta. Escape Sequence\n\t\tb. Formatted Strings\n\t\tc. Back to Main Menu")
    print("\t-----------------------------------------------------------")

def conditional_statements():
    print('''
    Python conditional statements are commands that let a program decide what action to take based on a condition. 
    They check whether something is true or false, and then run specific code depending on the result.''')

def conditional_menu():
    print("\n\t------------------------------------------------------------")
    print("\t\t\t~ Menu to Conditional Statements ~")
    print("\t\ta. If Statements\n\t\tb. If-Else Statements\n\t\tc. If-Elif-Else Statements\n\t\td. Nested If Statements\n\t\te. Back to Main Menu")
    print("\t----------------------------------------------------------") 

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
    ~ An if-else statement is a conditional statement that executes one block of code if a specified condition is true, 
      and another block of code if the condition is false.

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
    #activity 6
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
    #activity 7
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
    #activity 8 
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
    ~ Python provides two primary types of loops for repetitive execution of code blocks: 
      for loops and while loops.
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
    for variable x in range (Start, Stop, Step):
          code block

    # variable x - name of the loop variable
    # range(Start, Stop, Step) - creates a list of numbers starting from start, ending before stop, and changing by step
    # start - where the count begins
    # stop - where the counting end (but not included)
    # step - how much it increases or decreases each time      
    
    ''')

def loops_ex_menu():
    print("\n\t------------------------------------------------------------")
    print("\t\t\t~ Menu to Examples of for loop ~")
    print("\t\ta. Basic for loop\n\t\tb. Summation using for loop\n\t\tc. Ascending and Descending\n\t\td. New Line\n\t\te. Factorial\n\t\tf. Multiplication Table\n\t\tg. Timer\n\t\th. Back to Main Menu")
    print("\t-----------------------------------------------------------")

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

    for i in range(1, 11):                              # this will let you input number 10x
        number = eval(input("Enter a number:"))
        num += number                                   # after you input the first number, it will be added to the next number you will input and so on.
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
          
    print("\\t\\tFACTORIAL PROGRAM")

    fact = eval(input("Enter a numbe ---> "))

    num = 1
    for y in range(fact, 0, -1):
        print(y)
        num *= y
    print("\\nThe factorial of", fact, "is", num)

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

    print("\\nThe multiplication table for", num,":")
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

    print("\\nCountdown started:")

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

def nest_loop():
    print('''
    A nested for loop in Python refers to a for loop placed inside another for loop. 
    This structure allows for iteration over multiple sequences or for performing actions that require multiple layers of repetition.

    Syntax: 
        for outer_variable x in range():
            code block
            for inner_variable y in range():
                code block
          
    * Explanation:
               
    - for outer_variable x in range():  # This is the outer loop. 
      It iterates through each item in range, assigning the current item to outer_variable x in each iteration.

    - Indentation: The code block belonging to the outer loop (including the inner loop) must be indented.
          
    - for inner_variable y in range():  # This is the inner loop. It is placed inside the outer loop's code block. 
      For each iteration of the outer loop, the inner loop will execute completely, iterating through all items in range and assigning them to inner_variable y.
          
''')
    
def nest_menu():
    print("\n\t------------------------------------------------------------")
    print("\t\t\t~ Menu to Examples for Nested Loops ~\n")
    print("\t\ta. Number Loop\n\t\tb. Number Right Triangle\n\t\tc. Triangle\n\t\td. Number Pyramid\n\t\te. Back to Main Menu")
    print("\t-----------------------------------------------------------")
    
def nest_ex():
    #activity 17
    print('''
    #NESTED IN FOR LOOP

    for x in range(1, 11, 1):         # The outer loop controls how many lines to print.
        for i in range(1, 11):        # The inner loop controls what to print on each line.
            print(i, end=" ")
        print()

- Output:
          
    1 2 3 4 5 6 7 8 9 10 
    1 2 3 4 5 6 7 8 9 10 
    1 2 3 4 5 6 7 8 9 10 
    1 2 3 4 5 6 7 8 9 10 
    1 2 3 4 5 6 7 8 9 10 
    1 2 3 4 5 6 7 8 9 10 
    1 2 3 4 5 6 7 8 9 10 
    1 2 3 4 5 6 7 8 9 10 
    1 2 3 4 5 6 7 8 9 10 
    1 2 3 4 5 6 7 8 9 10 
    
    ''')

def nest_run():
    num = eval(input("Enter a number you want: "))
    for x in range(1, num, 1):
        for i in range(1, num):
            print(i, end=" ")
        print()
    return

def nest_right():
    print('''
    In this example, it will show you how for loops can make anything happen especially triangle.  

    for x in range(1, 11, 1):
        for y in range(1, x, 1):
            print(y, end=" ")
        print()
          
    ~ The outer loop controls the row number.
    ~ The inner loop prints numbers from 1 up to x−1.
          - When x = 1 → y runs from 1 to 0 → prints nothing
          - When x = 2 → y = 1 → prints: 1
          - When x = 3 → y = 1, 2 → prints: 1 2
          - When x = 4 → y = 1, 2, 3 → prints: 1 2 3 
    ~ This creates a growing number triangle.

    - Output:
          
    ''')

def act18():
    #act 18
    for x in range(1, 11, 1):
        for y in range(1, x, 1):
            print(y, end=" ")
        print()
    return

def triangle():
    print('''
    ~ The first loop prints spaces → makes the triangle centered.
    ~ The second loop prints the left half of triangle.
    ~ The third loop prints the right half of triangle.      

    for x in range(1, 11, 1):
        for y in range(10, x, -1):
            print(" ", end=" ")
        for z in range(1, x, 1):
            print("*", end=" ")
        for z in range(1, x, 1):
            print("*", end=" ")
        print() 

    - Output:
          
    ''')

def cc10():
    for x in range(1, 11, 1):
        for y in range(10, x, -1):
            print(" ", end=" ")
        for z in range(1, x, 1):
            print("*", end=" ")
        for z in range(1, x, 1):
            print("*", end=" ")
        print() 
    return

def num():
    print('''
         
    for x in range(1, 9, 1):
        for y in range(9, x, -1):
            print(" ", end=" ")
        for z in range(x, 1, -1):
            print(z, end=" ")
        for a in range(1, y, 1):
            print(a, end=" ")
        print() 

    - Output:

    ''')

def cc12():
    for x in range(1, 9, 1):
        for y in range(9, x, -1):
            print(" ", end=" ")
        for z in range(x, 1, -1):
            print(z, end=" ")
        for a in range(1, y, 1):
            print(a, end=" ")
        print() 
    return

def try_nest():
    for x in range(1, 9, 1):
        for y in range(9, x, -1):
            print(" ", end=" ")
        for z in range(x, 1, -1):
            print(z, end=" ")
        for a in range(1, y, 1):
            print(a, end=" ")
        print() 
    return

def while_loop():
    print('''
    A while loop in Python repeatedly executes a block of code as long as a specified condition remains True. 
    It is a fundamental control flow statement used for iteration when the number of repetitions is not known beforehand.

    Syntax: 
        while condition is TRUE:
            code block
            if condition:
                continue
            else:
                break

    ''')

def while_menu():
    print("\n\t------------------------------------------------------------")
    print("\t\t\t~ Menu to Examples for While Loops ~\n")
    print("\t\ta. Washing\n\t\tb. Odd Number Compiler\n\t\tc. Back to Main Menu")
    print("\t-----------------------------------------------------------")

def while_ex():
    print('''
    The while loop requires relevant variables to be ready.
    
    In this example we need to define an indexing variable, isDirty, which we set to True.     
    
    isDirty = True

    while isDirty == True:                                                                 # Keeps looping
        response = input("Do you wish to continue washing> (yes/no) --> ").lower()         # Asks the user if they want to continue washing

        if response == "yes":                                                              # If they say yes → washing continues
            print("Washing...")
            continue
        elif response == "no":                                                             # If they say no → stop the cycle
            print("Stopping the wash cycle.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")                            # If the input is wrong → ask again
            continue
    
''')

def try_while():
    #activity 21
    isDirty = True

    while isDirty == True:
        response = input("Do you wish to continue washing> (yes/no) --> ").lower()

        if response == "yes":
            print("Washing...")
            continue
        elif response == "no":
            print("Stopping the wash cycle.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue
    return

def odd_ex():
    print('''
    In this example, it asks user to input some numbers and only accepts the odd numbers. 
    It stops when the user input, and it will show all odd numbers and its total sum.
    
    name = input("Hi! What is your name? --> ")
    print("--------------------------------------------------")
    print("ODD number compiler, type '0' to terminate the loop.")

    sum = 0
    odd= ''
    gora = True

    while gora == True:
        number = eval(input("Please enter a number --> "))

        if number % 2 == 1:
            print("ODD number detected!")
            odd += str(number) + ','
            sum += number
            continue
        elif number == 0:
            print("Loop Terminated")
            break
        else:
            if number % 2 == 0:
                print("EVEN number detected, please try again.")
            else:
                print("Invalid input, please try again.")
            continue
    print("--------------------------------------------------")

    print(f"Hi {name}, The sum of all ODD number is {sum}.")
    print(f"All the ODD numbers you inputed are {odd}.")

''')
    
def try_odd():
    #cc 14
    name = input("Hi! What is your name? --> ")
    print("--------------------------------------------------")
    print("ODD number compiler, type '0' to terminate the loop.")

    sum = 0
    odd= ''
    gora = True

    while gora == True:
        number = eval(input("Please enter a number --> "))

        if number % 2 == 1:
            print("ODD number detected!")
            odd += str(number) + ','
            sum += number
            continue
        elif number == 0:
            print("Loop Terminated")
            break
        else:
            if number % 2 == 0:
                print("EVEN number detected, please try again.")
            else:
                print("Invalid input, please try again.")
            continue
    print("--------------------------------------------------")

    print(f"Hi {name}, The sum of all ODD number is {sum}.")
    print(f"All the ODD numbers you inputed are {odd}.")
    return

def lists():
    print('''
    A list is an ordered collection of elements that can be of any data type—numbers, strings, booleans, or even other lists. 
    Lists are created using square brackets.

    list = []
          
Common List Operations:
    list.append(item)          : adds an item to the end
    list.insert(index, item)   : inserts item at specified index
    list.remove(item)          : removes first occurence of item
    list.pop(index)            : removes the last items at index
    len(list)                  : returns number of elements
    list.sort()                : sorts the list (ascending by default)
    list.reverse()             : reverses the list order
          
    ''')

def list_menu():
    print("\n\t------------------------------------------------------------")
    print("\t\t\t~ Menu to Examples for Lists ~\n")
    print("\t\ta. Examples\n\t\tb. Indexing\n\t\tc. Slicing\n\t\td. Iteration\n\t\te. Back to Main Menu")
    print("\t-----------------------------------------------------------")

def example():
    print('''
          
    mylist = ["apple", "banana", "cherry"]

    print(mylist)
    mylist.append("strawberry")
    print(mylist)
    mylist.insert(2, blueberry)
    print(mylist)
    mylist.pop()
    print(mylist)
          
    - Output:

''')
    
def out_ex():
    mylist = ["apple", "banana", "cherry"]

    print(mylist)
    mylist.append("strawberry")
    print(mylist)
    mylist.insert(2, blueberry)
    print(mylist)
    mylist.pop()
    print(mylist)
    return

def examp():
    print('''
    Indexing means to access elements by position.
                 #0         #1       #2        #3      #4          #5         #6
    my_list = ["apple", "banana", "cherry", "date", "orange", "strawberry", "mango"]
                 #-7       #-6      #-5       #-4      #-3        #-2         #-1
    To access a single element, use square brackets [] after the list name, enclosing the desired index.      
    
    print(my_list[5])     # Output: strawberry
    print(my_list[2])     # Output: cherry
    print(my_list[-3])     # Output: orange
    
    ''')

def slicing():
    print('''
    Slicing means to extract sublists.
          
                 #0         #1       #2        #3      #4          #5         #6
    my_list = ["apple", "banana", "cherry", "date", "orange", "strawberry", "mango"]
                 #-7       #-6      #-5       #-4      #-3        #-2         #-1
    To access a single element, use square brackets [] after the list name, enclosing the desired index.

    print(my_list[2:5])   # Output: ["cherry", "date", "orange"]
    print(my_list[1:3])   # Output: ["banana", "cherry"]
    print(my_list[-7:-5])   # Output: ["apple", "banana"]
          
''')

def iteration():
    print('''
    Iteration means loop through elements.
          
    my_list = ["apple", "banana", "cherry", "date", "orange", "strawberry", "mango"]

    for each_fruit in my_list:
        print(f"I can eat {each_fruit}.")
          
- Output:

''')
    
def iterate():
    my_list = ["apple", "banana", "cherry", "date", "orange", "strawberry", "mango"]

    for each_fruit in my_list:
        print(f"I can eat {each_fruit}.")
    return

def function():
    print('''
    Functions are defined using the def keyword, followed by the function name, parentheses (which may contain parameters), and a colon. 
    The code within the function's body must be indented.

    There are types of functions:
          
''')

def function_type():
    print("\n\t------------------------------------------------------------")
    print("\t\t\t~ Types of Functions ~\n")
    print("\t\ta. Built-in Functions\n\t\tb. Programmer-Defined Functions\n\t\tc. Back to Main Menu")
    print("\t-----------------------------------------------------------")

def built():
    print('''
    These are functions that come pre-defined with the programming language. They are readily available and do not require any additional definition.

    Commonly Used in Python:
    print()
    input()
    int()
    float()
    bool()
    str()
    len()
    type()
    max()
          
Example:
    print("Hello, world!")       # Outputs text to the console
    len("Hello")                 # Returns the length of a string
    max([1, 2, 3])               # Returns the maximum value

''')

def user_def():
    #activity 24
    print('''
    These are functions created by the programmer to perform specific tasks. They help modularize code and avoid repetition.

Example:
    def greeting(name):
    print(f"Hello, {name}! Welcome to the program.")

    greeting("Dynneal")
    greeting("Antonio")
    greeting("Mocha")
        
    - Output:
          
''')

def greeting(name):
    print(f"Hello, {name}! Welcome to the program.")

    greeting("Dynneal")
    greeting("Antonio")
    greeting("Mocha")
    return
