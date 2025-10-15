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

