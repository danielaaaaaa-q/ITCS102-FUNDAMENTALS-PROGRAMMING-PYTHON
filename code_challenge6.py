print("\t\tFACTORIAL PROGRAM")

fact = eval(input("Enter a numbe ---> "))

num = 1
for y in range(fact, 0, -1):
    print(y)
    num *= y
print("\nThe factorial of", fact, "is", num)