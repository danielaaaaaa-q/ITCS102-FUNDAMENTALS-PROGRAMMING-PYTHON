temp = eval(input("Enter temperature --> "))

if temp <= 0:
    print("Temperature outside is freezing cold.")
elif 1 <= temp <= 20:
    print("Temperature outside is cold.")
elif 21 <= temp <= 30:
    print("Temperature outside is lukewarm.")
elif 31 <= temp <= 40:
    print("Temperature outside is warm.")
elif 41 <= temp <= 50:
    print("Temperature outside is hot.")
elif temp >= 51:
    print("Temperature outside is boiling hot.")
else:
    print("Invalid temperature.")