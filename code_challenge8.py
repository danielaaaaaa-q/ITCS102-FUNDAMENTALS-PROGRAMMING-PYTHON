print("MULTIPLICATION TABLE MAKER")

num = eval(input("Enter a number ---> "))

print("\nThe multiplication table for", num,":")
for x in range(1, 11):
    print(num, "x", x, "=", num * x)5