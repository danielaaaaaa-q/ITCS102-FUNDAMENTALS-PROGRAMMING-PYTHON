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