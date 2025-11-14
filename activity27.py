print("\tAdding Data to Dictionary.")
print("===========================================")

con = True

def print_anime():
    for c,d in empty_dictionary.items():
        print(f"Code {c} : Title -- {d}")

def search(key):
    print("Searching...")
    print(f"Result: {empty_dictionary[key].upper()} on our database.")

empty_dictionary = {}

while con == True:
    key = input("Input keys for this anime: ")
    value = input("Enter anime title: ")

    #adding data to a dictionary
    empty_dictionary[key] = value

    choice = input("Would you like to continue adding anime? \ny - Yes\nn - No\np - Print\ns - Search\nAnswer here: ").lower()

    if choice == 'y':
        print("Continuing...")
        continue
    elif choice == 'n':
        print("Program stops...")
        break
    elif choice == 'p':
        print_anime()
        continue
    elif choice == 's':
        search(key)
        continue
    else:
        print("Invalid input. Please try again")
        continue

