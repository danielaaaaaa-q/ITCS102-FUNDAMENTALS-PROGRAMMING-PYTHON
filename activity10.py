#jeepney fare

name = input("Input your name: ")
isStudent = input("Are you a student (yes/no): ")
fare = eval(input("bayad: "))

if isStudent.lower() == "yes":
	discount = fare * .2
	new_fare = fare - discount
	print("Hi,", name, "your student discount is", discount, "\n\t     Discounted fare is", new_fare)
else:
	print("Sorry,", name," you are not eligible for student discount.")