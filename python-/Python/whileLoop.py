Password = input("Please select a password: ")

password = input("Please enter the password to login: ")

while password!= Password:
    if password == Password:
        print("You are logged in! Welcome %s" %password)
    else:
        print("ERROR: Password was not correct. Try again")
        password = input("Please enter the password to login: ")

print("You are logged in! Welcome %s" %password)
