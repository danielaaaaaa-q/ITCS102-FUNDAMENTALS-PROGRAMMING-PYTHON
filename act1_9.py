def act1():
    print("print(\"Hello, World!\")")
    print("\nOutput:")
    print("Hello, World!")

def act2():
    a = "Dynneal Antonio"
    print("a = \"Dynneal Antonio\"\nprint(\"X = \", a)")
    print("\nOutput:")
    print("X = ", a)

def act3():
    print("Demonstrating escape sequences:")
    print("\tThe quick brown\n\t \rFox jumps over\n\t the Lazy Dog.")
    print("\"Hindi ako makulit.\"")

def act4():
    name = input("Enter your name --> ")

    print("Your name has ", len(name), "characters.")

def act5():
    something = eval(input("Input something --> "))
    print("The data type of something is ", type(something))

    answer = 6 + something
    print("The answer is ", answer)

def arithmetic():
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

def assignment():
    a = 7

    print("The value of a is", a)

    a += 13
    a -= 17
    a *= 3
    a += 18
    a /= 2

    print("The value of a is", a)

def relational():
    balance = 3000
    withdrawal = 600

    #print(balance <= withdrawal)

    name1 = "millicent"
    name2 = "Millicent"

    print(name1 == name2)

def act9():
    username = "dynneal"
    password = "miyrae17"

    #print(username == "dynneal")
    #print(password == "mirae17")
    print((username == "dynneal") and (password == "mirae17"))
    print(not((username == "dynneal") and (password == "mirae17")))

