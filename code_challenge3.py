from getpass import getpass

username = "danielaaaaaa-q"
password = "dani13"

user_name = input("Enter your username: ")
isPassword = getpass("Enter your password: ")


if username == user_name and password == isPassword:
	print("Access granted.")
else:

	print("Access denied.")
