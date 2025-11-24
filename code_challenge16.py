import os
import json

os.system('cls')
print("\tSTUDENT INFORMATION SYSTEM")
print("------------------------------------------")

students_record = {}

while True:
    print("\nSELECT FROM THE OPTIONS BELOW: \nA. Add Student Information\nB. Print All Data\nC. Search Student Record\nD. Delete a Record\nE. Edit Student Record\nF. Export Student Record\nG. Import Student Record\n\nX. Exit")
    choose = input("Enter your choice(a-f): ").lower()

    if choose == 'a':
        print("\n\tADDING STUDENT INFORMATION")
        print("-------------------------------------------")
        search_code = input("Key search for this Student (course IDNO): ").lower()

        first_name = input("Enter Student's First Name: ").upper()
        last_name = input("Enter Student's Last Name: ").upper()
        course = input("Enter Student's Course: ").upper()
        email_add = input("Enter Student's Email Address: ")
        isSingle = input("Is the Student Single? (yes/no): ").lower()

        os.system('cls')

        #adding data to a dictionary
        students_record[search_code] = [first_name, last_name, course, email_add, isSingle] #a list
        print("--> Student Record Added Successfully!")
        continue
    elif choose == 'b':
        print("\n\tPRINTING ALL STUDENT RECORDS")
        print("--------------------------------------------")

        for id, rec  in students_record.items():
            print(f"CODE - {id} STORED INFORMATION --> {rec}")
        continue
    elif choose == 'c':
        os.system('cls')
        print("\n\tSEARCHING A RECORD")
        print("-------------------------------------")

        code = input("Enter the key search of the Student to be Searched: ").lower()
        
        for a in students_record.keys():
            if code in students_record.keys():
                print("--> Record Found!")

                print("Student Information:")
                print("------------------------------")
                # Displaying the student information
                for b in students_record[code]:
                    print(f"- {b}")
            else:
                print("--> Record Not Found!")
            break
        continue
    elif choose == 'd':
        os.system('cls')
        print("\n\tDELETING A RECORD")
        print("-------------------------------------")

        code = input("Enter the key search of the Student to Delete: ").lower()

        for c in students_record.keys():
            if code in students_record.keys():
                print("--> Record Found!")
                print("\n")
                print("Student Information:")
                print("------------------------------")
                # Displaying the student information
                for d in students_record[code]:
                    print(f"- {d}")
                print("------------------------------")

                students_record.pop(code)
                print("\n--> Record Deleted Successfully!")
            else:
                print("--> Record Not Found!")
            break
        continue
    elif choose == 'e':
        os.system('cls')
        print("\n\tEDIT / MODIFY STUDENT RECORD")
        print("-------------------------------------")

        code = input("Enter the key search of the Student to be Edited: ").lower()

        for a in students_record.keys():
            if code in students_record.keys():
                print("--> Record Found!")
                print("Student Information:")
                print("------------------------------")
                    # Displaying the student information
                for b in students_record[code]:
                    print(f"- {b}")
        
                first_name = input("Enter NEW Student's First Name: ").upper()
                last_name = input("Enter NEW Student's Last Name: ").upper()
                course = input("Enter NEW Student's Course: ").upper()
                email_add = input("Enter NEW Student's Email Address: ")

                print("\n--> Student Record Updated Successfully!")
            else:
                print("--> Record Not Found!")
            break
        continue
    elif choose == 'f':
        os.system('cls')
        print("\n\tEXPORTING STUDENT RECORDS")
        print("-------------------------------------")

        with open('students_record.json', 'w') as new_file:
            json.dump(students_record, new_file)

        print("DATA EXPORTED TO JSON")
        continue
    elif choose == 'g':
        os.system('cls')
        print("\n\tIMPORTING STUDENT RECORDS")
        print("-------------------------------------")

        with open('students_record.json', 'r') as new_file:
            student_json = json.load(new_file)

        students_record = student_json

        print("DATA IMPORTED FROM JSON")
        continue
    elif choose == 'x':
        print("==========================================")
        print("Exiting the Program...")
        print("==========================================")
        break
    else:
        break