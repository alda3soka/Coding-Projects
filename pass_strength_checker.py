import time

username = input("Enter your username: ")
password = input("Enter your password: ")

while len(password) < 8: # Checks password length
    print("Password must be at least 8 characters long.")
    password = input("Enter your password: ")
while password.isalpha(): # Checks if password contains at least one number
    print("Password must contain at least one number.")
    password = input("Enter your password: ")
while password.isdigit(): # Checks if password contains at least one letter
    print("Password must contain at least one letter.")
    password = input("Enter your password: ")
while password.islower(): # Checks if password contains at least one uppercase letter
    print("Password must contain at least one uppercase letter.")
    password = input("Enter your password: ")
while password.isupper(): # Checks if password contains at least one lowercase letter
    print("Password must contain at least one lowercase letter.")
    password = input("Enter your password: ")
while password.isalnum(): # Checks if password contains at least one special character
    print("Password must contain at least one special character.")
    password = input("Enter your password: ")
while password.find(" ") != -1: # Checks if password contains spaces
    print("Password cannot contain spaces.")
    password = input("Enter your password: ")
else:
    print("Your password is strong.")
    time.sleep(3)