def greeting(name):
    print(f"Hello, {name}! Welcome to the program.")

greeting("Dynneal")
greeting("Antonio")
greeting("Mocha")

def summation(v):
    sum = 0 
    for ha in range(v, 0, -1):
        sum += ha
    print(f"The summation of {v} is {sum}. :O")

summation(5)
summation(13)
summation(23)