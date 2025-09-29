for x in range(1, 9, 1):
    for y in range(9, x, -1):
        print(" ", end=" ")
    for z in range(x, 1, -1):
        print(z, end=" ")
    for a in range(1, y, 1):
        print(a, end=" ")
    print() 


    