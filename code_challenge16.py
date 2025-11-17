import os

os.system('cls')
print("\tSTUDENT INFORMATION SYSTEM")
print("------------------------------------------")

students_record = {}

while True:
    print("\nSELECT FROM THE OPTIONS BELOW: \nA. Add Student Information\nB. Search a Record\nC. Delete a Record\nD. Modify a Record\nP. Print All Data\nE. Exit")
    choose = input("Enter your choice(a-e): ").lower()

    if choose == 'a':
        print("\n\tADDING STUDENT INFORMATION")
        print("-------------------------------------------")
        search_code = input("Key search for this Student (course IDNO): ")

        first_name = input("Enter Student's First Name: ").upper()
        last_name = input("Enter Student's Last Name: ").upper()
        course = input("Enter Student's Course: ").upper()
        email_add = input("Enter Student's Email Address: ")
        isSingle = input("Is the Student Single? (yes/no): ").lower()

        os.system('cls')

        students_record = {search_code : [first_name, last_name, course, email_add, isSingle]}
        print("--> Student Record Added Successfully!")

        continue

    elif choose == 'b':
        os.system('cls')
        print("\n\tSEARCHING A RECORD")
        print("---------------------------------------")

        code = input("Enter the Key Search of the Student to be Searched: ")
        
        for a in students_record.keys():
            if code in students_record.keys():
                print("--> Record Found!")

                print("\nStudent's Information:")
                print("-------------------------------")
                for b in students_record[code]:
                    print(b)
            else:
                print("--> Record Not Found!")
        continue

    elif choose == 'c':
        print("\n\tDELETING A RECORD")

    elif choose == 'd':
        pass
        continue
    elif choose == 'p':
        for i,j in students_record.items():
            print(f"CODE - {i} STORED INFORMATION --> {j}")
        continue
    elif choose == 'e':
        pass
        continue
    else:
