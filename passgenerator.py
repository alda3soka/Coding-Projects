import random


letters = list('abcdefghijklmnopqrstuvwxyz')
uppercase_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('!@#$%^&*()_+-')


length = int(input("Enter the length of the password: "))


while length < 8:
    print("Password length must be at least 8 characters.")
    length = int(input("Enter the length of the password: "))


all_chars = letters + uppercase_letters + numbers + symbols


password = ''.join(random.choice(all_chars) for _ in range(length))


print("Your password is: " + password)
