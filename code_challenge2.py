amount = eval(input("Enter amount to deposit: "))

ph_denomination = (1000, 500, 200, 100, 50, 20, 10, 5, 1)

a = amount // 1000
amount = amount % 1000

b = amount // 500
amount = amount % 500

c = amount // 200
amount = amount % 200

d = amount // 100
amount = amount % 100

e = amount // 50 
amount = amount % 50

f = amount // 20
amount = amount % 20

g = amount // 10 
amount = amount % 10

h = amount // 5
amount = amount % 5

i = amount // 1
amount = amount % 1



print("\nHere is a breakdown using Philippines denomination: ")

print("\n\t", str(a) + "         ₱1000")
print("\t", str(b) + "         ₱500")
print("\t", str(c) + "         ₱200")
print("\t", str(d) + "         ₱100")
print("\t", str(e) + "         ₱50")
print("\t", str(f) + "         ₱20")
print("\t", str(g) + "         ₱10")
print("\t", str(h) + "         ₱5")
print("\t", str(i) + "         ₱1")