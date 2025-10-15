loan_amount = eval(input("Enter loan amount: $ "))
loan_period = eval(input("Enter loan period in years: "))

loan_period *= 12
principal  = loan_amount / loan_period
balance = loan_amount
interest = 0

print("PAYMENT SCHEDULE")
print("-----------------------------------------------------------------------------------------------------------------")
print("|\tMonth\t|\tMonthly Payment\t\t|\tInterest\t|\tPrincipal\t|\tBalance\t\t|")
print("-----------------------------------------------------------------------------------------------------------------")

for i in range(1, loan_period + 1, 1):
    interest = balance * (0.03)
    balance -= principal
    monthly = interest + principal
    print(f"|\t{i}\t|\t{round(monthly, 2)}\t\t\t|\t{round(interest, 2)}\t\t|\t{round(principal, 2)}\t\t|\t{round(balance, 2)}\t\t|")


