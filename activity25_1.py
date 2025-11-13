def hello():
    for i in range(1, 10, 1):
        print("Hello World!")

def summation():
    num = 0

    for i in range(1, 11):
        number = eval(input("Enter a number: "))
        num += number
        print("The current sum is: ", num)
    print(num)

def ascending_descending():
    #-- ascending order --
    for i in range(1, 11):
        print(i)

    #-- descending order --
    for i in range(10, 0, -1):
        print(i)

def fav_book():
    name = input("Enter your name --> ")
    age = eval(input("Enter your age --> "))
    book = input("Enter your favourite book --> ")

    print(f"Hello, I am {name}, I am {age} years old and my favourite book is {book}.")
