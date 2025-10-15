isDirty = True

while isDirty == True:
    response = input("Do you wish to continue washing> (yes/no) --> ").lower()

    if response == "yes":
        print("Washing...")
        continue
    elif response == "no":
        print("Stopping the wash cycle.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        continue
    