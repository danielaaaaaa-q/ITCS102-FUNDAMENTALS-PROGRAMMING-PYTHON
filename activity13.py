num = 0

for i in range(1, 11):
    number = eval(input("Enter a number:"))
    num += number
    print("The current sum is:", num)
print(num)