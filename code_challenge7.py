#-- ODD NUMBERS SUMMATION --

print("\t\tODD NUMBERS SUMMATION")

result = 0

for x in range(1, 10, 1):
    num = eval(input("Enter a number ---> "))
    if num % 2 != 0:
        result += num
print("- The summation of odd numbers is", result)