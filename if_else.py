def act10():
    #jeepney fare
    name = input("Input your name: ")
    isStudent = input("Are you a student (yes/no): ")
    fare = eval(input("bayad: "))
    if isStudent.lower() == "yes":
        discount = fare * .2
        new_fare = fare - discount
        print("Hi,", name, "your student discount is", discount, "\n\t     Discounted fare is", new_fare)
    else:
        print("Sorry,", name," you are not eligible for student discount.")

def act11():
    temp = eval(input("Enter temperature --> "))

    if temp <= 0:
        print("Temperature outside is freezing cold.")
    elif 1 <= temp <= 20:
        print("Temperature outside is cold.")
    elif 21 <= temp <= 30:
        print("Temperature outside is lukewarm.")
    elif 31 <= temp <= 40:
        print("Temperature outside is warm.")
    elif 41 <= temp <= 50:
        print("Temperature outside is hot.")
    elif temp >= 51:
        print("Temperature outside is boiling hot.")
    else:
        print("Invalid temperature.")

def act12():
    #print("Hello World!")

    for i in range(1, 10, 1):
        print("Hello World!")

def act13():
    num = 0

    for i in range(1, 11):
        number = eval(input("Enter a number:"))
        num += number
        print("The current sum is:", num)
    print(num)

def act14():
    #-- ascending order --
    for i in range(1, 11):
        print(i)

    #-- descending order --
    for i in range(10, 0, -1):
        print(i)

def act15():
    #STRING FORMATTING
    # Write a Python program that takes a user's name and age as input and then prints a message using string formatting and its fav book

    name = input("Enter your name --> ")
    age = eval(input("Enter your age --> "))
    book = input("Enter your favourite book --> ")

    print(f"Hello, I am {name}, I am {age} years old and my favourite book is {book}.")

def act16():
    #new line in print

    for i in range(1, 11):
        print(i, end=" --- ")

def act17():
    #NESTED IN FOR LOOP

    for x in range(1, 11, 1):
        for i in range(1, 11):
            print(i, end=" ")
        print()

def act18():
    for x in range(1, 11, 1):
        for y in range(1, x, 1):
            print(y, end=" ")
        print()

def act19():
    for x in range(1, 11, 1):
        for y in range(1, x, 1):
            print("*", end=" ")
        print()

def act20():
    for x in range(1, 11, 1):
        for y in range(1, x, 1):
            print(" ", end=" ")
        for z in range(10, x, -1):
            print(z, end=" ")
        print() 

